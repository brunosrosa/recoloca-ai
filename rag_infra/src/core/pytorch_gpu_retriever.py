#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Retriever RAG com PyTorch GPU para o Sistema Recoloca.ai

Este módulo implementa busca vetorial usando PyTorch com aceleração GPU,
substituindo o FAISS que tem limitações com placas GeForce RTX em modo WDDM.

Autor: @AgenteM_DevFastAPI
Versão: 2.0 - PyTorch GPU Edition
Data: Janeiro 2025
"""

import json
import logging
import pickle
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

from .constants import (
    PYTORCH_INDEX_DIR, PYTORCH_INDEX_FILE, PYTORCH_DOCUMENTS_FILE, PYTORCH_METADATA_FILE,
    PYTORCH_EMBEDDINGS_FILE, PYTORCH_MAPPING_FILE,
    FAISS_INDEX_DIR, FAISS_DOCUMENTS_FILE, FAISS_METADATA_FILE,
    EMBEDDING_MODEL_NAME, USE_GPU, DEFAULT_TOP_K, MIN_SIMILARITY_SCORE,
    PYTORCH_BATCH_SIZE, PYTORCH_MAX_MEMORY_GB,
    LOGS_DIR, CACHE_DIR, METRICS_DIR,
    ENABLE_METRICS, ENABLE_CACHING,
    STATUS_MESSAGES
)
from .torch_utils import is_cuda_available, safe_cuda_empty_cache, safe_tensor_cleanup
from .embedding_model import initialize_embedding_model, get_embedding_manager

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Criar handler para arquivo de log
LOGS_DIR.mkdir(parents=True, exist_ok=True)
file_handler = logging.FileHandler(LOGS_DIR / "pytorch_gpu_retriever.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

class SearchResult:
    """
    Classe para representar um resultado de busca.
    """
    
    def __init__(self, content: str, metadata: Dict[str, Any], score: float, rank: int):
        self.content = content
        self.metadata = metadata
        self.score = score
        self.rank = rank
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o resultado para dicionário.
        
        Returns:
            Dict: Representação em dicionário do resultado
        """
        return {
            "content": self.content,
            "metadata": self.metadata,
            "score": self.score,
            "rank": self.rank
        }
    
    def format_result(self) -> str:
        """
        Formata o resultado para exibição.
        
        Returns:
            str: Resultado formatado
        """
        return f"Fonte: {self.metadata.get('source', 'Desconhecido')}\nSeção: {self.metadata.get('section', 'main')}\nScore: {self.score:.3f}\nConteúdo: {self.content[:500] + '...' if len(self.content) > 500 else self.content}"
    
    def __str__(self) -> str:
        return f"SearchResult(rank={self.rank}, score={self.score:.3f}, source={self.metadata.get('source', 'Unknown')})"
    
    def __repr__(self) -> str:
        return self.__str__()

class PyTorchGPURetriever:
    """
    Retriever RAG usando PyTorch com aceleração GPU.
    """
    
    def __init__(self, index_dir: Optional[Path] = None, force_cpu: bool = False, batch_size: int = 1000):
        """
        Inicializa o retriever PyTorch GPU.
        
        Args:
            force_cpu: Se True, força o uso de CPU
            batch_size: Tamanho do batch para processamento em lote
        """
        self.embedding_manager = None
        self.index_dir = index_dir or PYTORCH_INDEX_DIR
        self.force_cpu = force_cpu
        self.batch_size = batch_size
        
        # Configurar dispositivo
        if force_cpu or not is_cuda_available():
            self.device = torch.device('cpu')
            logger.info("Usando CPU para busca vetorial")
        else:
            self.device = torch.device('cuda')
            logger.info(f"Usando GPU para busca vetorial: {torch.cuda.get_device_name(0)}")
        
        # Dados
        self.embeddings_tensor = None
        self.documents = []
        self.metadata = []
        self.index_metadata = {}
        self.is_loaded = False

        # Nomes dos arquivos de índice
        self.embeddings_file = PYTORCH_EMBEDDINGS_FILE
        self.documents_file = PYTORCH_DOCUMENTS_FILE
        self.metadata_file = PYTORCH_METADATA_FILE
        
        # Cache de consultas
        self._query_cache: Dict[str, List[SearchResult]] = {}
        self._cache_max_size = 100
    
    def initialize(self) -> bool:
        """
        Inicializa o modelo de embedding.
        
        Returns:
            bool: True se inicializado com sucesso
        """
        try:
            logger.info("Inicializando modelo de embedding...")
            success = initialize_embedding_model(force_cpu=self.force_cpu)
            
            if success:
                self.embedding_manager = get_embedding_manager()
                logger.info("[OK] Modelo de embedding inicializado")
                return True
            else:
                logger.error("[ERROR] Falha ao inicializar modelo de embedding")
                return False
                
        except Exception as e:
            logger.error(f"Erro na inicialização: {str(e)}")
            return False
    
    def load_index(self, use_pytorch_files: bool = True) -> bool:
        """
        Carrega o índice (embeddings, documentos, metadados) da memória.
        Tenta carregar arquivos .pt por padrão, com fallback para .npy.
        
        Args:
            use_pytorch_files: Se True, tenta carregar arquivos .pt primeiro.
            
        Returns:
            bool: True se o índice foi carregado com sucesso, False caso contrário.
        """
        start_time = time.time()
        logger.info(STATUS_MESSAGES["loading_pytorch_index"])

        try:
            index_dir = Path(self.index_dir)
            embeddings_path = index_dir / (self.embeddings_file if use_pytorch_files else self.embeddings_file.replace('.pt', '.npy'))
            documents_path = index_dir / self.documents_file
            metadata_path = index_dir / self.metadata_file

            # --- Verificação de arquivos ---
            required_files = {
                "Embeddings": embeddings_path,
                "Documentos": documents_path,
                "Metadados": metadata_path
            }
            for name, path in required_files.items():
                if not path.exists():
                    logger.error(f"Arquivo de {name} não encontrado em: {path}")
                    return False
                logger.debug(f"Arquivo de {name} encontrado: {path}")

            # --- Carregamento de Documentos ---
            logger.debug(f"Carregando documentos de {documents_path}...")
            with open(documents_path, 'r', encoding='utf-8-sig') as f:
                self.documents = json.load(f)
            logger.info(f"{len(self.documents)} chunks de documentos carregados.")

            # --- Carregamento de Metadados ---
            logger.debug(f"Carregando metadados de {metadata_path}...")
            with open(metadata_path, 'r', encoding='utf-8-sig') as f:
                index_data = json.load(f)
                if isinstance(index_data, list):
                    self.metadata = index_data
                    self.index_metadata = {"documents_metadata": index_data}
                else:
                    self.index_metadata = index_data
                    self.metadata = index_data.get("documents_metadata", [])
            logger.info(f"{len(self.metadata)} entradas de metadados carregadas.")

            # --- Carregamento de Embeddings ---
            logger.debug(f"Carregando embeddings de {embeddings_path}...")
            if use_pytorch_files and embeddings_path.suffix == '.pt':
                self.embeddings_tensor = torch.load(embeddings_path, map_location=self.device)
                logger.info(f"Embeddings PyTorch carregados. Shape: {self.embeddings_tensor.shape}")
            else:
                embeddings_np = np.load(str(embeddings_path))
                self.embeddings_tensor = torch.from_numpy(embeddings_np).float().to(self.device)
                logger.info(f"Embeddings NumPy convertidos para PyTorch. Shape: {self.embeddings_tensor.shape}")

            # --- Verificação de Consistência ---
            if len(self.documents) != len(self.metadata):
                logger.warning(f"Inconsistência de contagem: {len(self.documents)} documentos vs {len(self.metadata)} metadados.")
            if self.embeddings_tensor.shape[0] != len(self.documents):
                logger.warning(f"Inconsistência de contagem: {self.embeddings_tensor.shape[0]} embeddings vs {len(self.documents)} documentos.")

            # --- Finalização ---
            logger.debug("Normalizando embeddings para similaridade de cosseno...")
            self.embeddings_tensor = F.normalize(self.embeddings_tensor, p=2, dim=1)
            
            elapsed_time = time.time() - start_time
            logger.info(f"Índice PyTorch carregado com sucesso em {elapsed_time:.2f}s. Dispositivo: {self.device}")
            self.is_loaded = True
            return True

        except FileNotFoundError as e:
            logger.error(f"Erro de arquivo não encontrado ao carregar índice PyTorch: {e}")
            return False
        except (json.JSONDecodeError, pickle.UnpicklingError) as e:
            logger.error(f"Erro de desserialização ao carregar índice PyTorch: {e}")
            return False
        except RuntimeError as e:
            logger.error(f"Erro de tempo de execução do PyTorch ao carregar índice: {e}")
            safe_cuda_empty_cache()
            return False
        except Exception as e:
            logger.critical(f"Erro inesperado ao carregar índice PyTorch: {e}", exc_info=True)
            safe_cuda_empty_cache()
            return False
    
    def _compute_similarities_batch(self, query_embedding: torch.Tensor, top_k: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Computa similaridades em lotes para otimizar uso de memória GPU.
        
        Args:
            query_embedding: Embedding da consulta normalizado
            top_k: Número de resultados desejados
            
        Returns:
            Tuple[torch.Tensor, torch.Tensor]: (scores, indices) dos top_k resultados
        """
        n_embeddings = self.embeddings_tensor.shape[0]
        
        # Se o dataset é pequeno, processar tudo de uma vez
        if n_embeddings <= self.batch_size:
            similarities = torch.mm(query_embedding, self.embeddings_tensor.t())
            top_k_values, top_k_indices = torch.topk(similarities, min(top_k, n_embeddings), dim=1)
            return top_k_values[0], top_k_indices[0]
        
        # Para datasets grandes, processar em lotes
        all_similarities = []
        all_indices = []
        
        for start_idx in range(0, n_embeddings, self.batch_size):
            end_idx = min(start_idx + self.batch_size, n_embeddings)
            batch_embeddings = self.embeddings_tensor[start_idx:end_idx]
            
            # Computar similaridades para este lote
            batch_similarities = torch.mm(query_embedding, batch_embeddings.t())
            
            # Manter apenas os top_k deste lote
            batch_top_k = min(top_k, batch_similarities.shape[1])
            batch_values, batch_indices = torch.topk(batch_similarities, batch_top_k, dim=1)
            
            # Ajustar índices para posição global
            global_indices = batch_indices[0] + start_idx
            
            all_similarities.append(batch_values[0])
            all_indices.append(global_indices)
        
        # Combinar resultados de todos os lotes
        combined_similarities = torch.cat(all_similarities)
        combined_indices = torch.cat(all_indices)
        
        # Selecionar top_k global
        final_top_k = min(top_k, len(combined_similarities))
        final_values, final_order = torch.topk(combined_similarities, final_top_k)
        final_indices = combined_indices[final_order]
        
        return final_values, final_indices
    
    def search(self, query: str, top_k: int = DEFAULT_TOP_K, min_score: float = MIN_SIMILARITY_SCORE, 
               category_filter: Optional[str] = None) -> List[SearchResult]:
        """
        Realiza busca semântica usando PyTorch GPU.
        
        Args:
            query: Consulta de busca
            top_k: Número de resultados a retornar
            min_score: Score mínimo de similaridade
            category_filter: Filtro por categoria (opcional)
            
        Returns:
            List[SearchResult]: Lista de resultados ordenados por relevância
        """
        if not self.is_loaded:
            logger.error("Dados não carregados. Chame load_index() primeiro.")
            return []
        
        if not self.embedding_manager:
            logger.error("Modelo de embedding não inicializado.")
            return []
        
        # Validar parâmetros
        top_k = min(max(1, top_k), 100)
        min_score = max(0.0, min(1.0, min_score))
        
        # Verificar cache
        cache_key = f"{query}_{top_k}_{min_score}_{category_filter}"
        if cache_key in self._query_cache:
            logger.debug(f"Resultado encontrado no cache para: {query[:50]}...")
            return self._query_cache[cache_key]
        
        try:
            logger.info(STATUS_MESSAGES["query_start"].format(query=query[:100]))
            start_time = time.time()
            
            # 1. Gerar embedding da consulta
            query_embedding = self.embedding_manager.embed_query(query)
            if query_embedding is None:
                logger.error("Falha ao gerar embedding da consulta")
                return []
            
            # 2. Converter para tensor PyTorch e normalizar
            query_tensor = torch.from_numpy(query_embedding).float().to(self.device)
            query_tensor = F.normalize(query_tensor.unsqueeze(0), p=2, dim=1)
            
            # 3. Buscar similaridades usando PyTorch GPU
            with torch.no_grad():
                scores, indices = self._compute_similarities_batch(query_tensor, top_k * 2)
            
            # 4. Processar resultados
            results = []
            for rank, (score, idx) in enumerate(zip(scores.cpu().numpy(), indices.cpu().numpy())):
                if score < min_score:
                    continue
                
                # Verificar se o índice é válido
                if idx >= len(self.documents) or idx >= len(self.metadata):
                    logger.warning(f"Índice fora do range: {idx}")
                    continue
                
                document = self.documents[idx]
                metadata = self.metadata[idx]
                
                # Aplicar filtro de categoria se especificado
                if category_filter and metadata.get("category") != category_filter:
                    continue
                
                result = SearchResult(
                    content=document,
                    metadata=metadata,
                    score=float(score),
                    rank=rank + 1
                )
                
                results.append(result)
                
                # Parar se já temos resultados suficientes
                if len(results) >= top_k:
                    break
            
            # 5. Atualizar ranks finais
            for i, result in enumerate(results):
                result.rank = i + 1
            
            elapsed_time = time.time() - start_time
            logger.info(STATUS_MESSAGES["query_complete"].format(
                count=len(results),
                time=elapsed_time,
                query=query[:50]
            ))
            
            # 6. Adicionar ao cache
            if len(self._query_cache) >= self._cache_max_size:
                # Remover entrada mais antiga
                oldest_key = next(iter(self._query_cache))
                del self._query_cache[oldest_key]
            
            self._query_cache[cache_key] = results
            
            return results
            
        except Exception as e:
            logger.error(f"Erro na busca: {str(e)}")
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Retorna estatísticas do retriever.
        
        Returns:
            Dict: Estatísticas do sistema
        """
        stats = {
            "is_loaded": self.is_loaded,
            "device": str(self.device),
            "cuda_available": is_cuda_available(),
            "documents_count": len(self.documents),
            "cache_size": len(self._query_cache),
            "batch_size": self.batch_size
        }
        
        if is_cuda_available() and not self.force_cpu:
            stats.update({
                "gpu_name": torch.cuda.get_device_name(0),
                "gpu_memory_allocated": torch.cuda.memory_allocated(0),
                "gpu_memory_reserved": torch.cuda.memory_reserved(0)
            })
        
        if self.embeddings_tensor is not None:
            stats["embeddings_shape"] = list(self.embeddings_tensor.shape)
            stats["embeddings_device"] = str(self.embeddings_tensor.device)
        
        return stats
    
    def get_index_info(self) -> Dict[str, Any]:
        """
        Retorna informações sobre o índice carregado.
        Compatibilidade com RAGRetriever.
        
        Returns:
            Dict: Informações do índice
        """
        if not self.is_loaded or self.embeddings_tensor is None:
            return {
                "status": "not_loaded",
                "backend": "PyTorch",
                "device": str(self.device),
                "documents_count": 0,
                "embeddings_shape": None
            }
        
        return {
            "status": "loaded",
            "backend": "PyTorch", 
            "device": str(self.device),
            "documents_count": len(self.documents),
            "embeddings_shape": list(self.embeddings_tensor.shape),
            "embedding_dimension": self.embeddings_tensor.shape[1] if len(self.embeddings_tensor.shape) > 1 else 0,
            "memory_usage_mb": self.embeddings_tensor.element_size() * self.embeddings_tensor.nelement() / (1024 * 1024),
            "force_cpu": self.force_cpu,
            "batch_size": self.batch_size
        }
    
    def clear_cache(self):
        """
        Limpa o cache de consultas.
        """
        self._query_cache.clear()
        logger.info("Cache de consultas limpo")
    
    def __del__(self):
        """
        Cleanup ao destruir o objeto.
        """
        safe_tensor_cleanup('embeddings_tensor', self)
        safe_cuda_empty_cache()

# Função de conveniência para criar retriever
def create_pytorch_gpu_retriever(force_cpu: bool = False, batch_size: int = 1000) -> PyTorchGPURetriever:
    """
    Cria e inicializa um retriever PyTorch GPU.
    
    Args:
        force_cpu: Se True, força o uso de CPU
        batch_size: Tamanho do batch para processamento
        
    Returns:
        PyTorchGPURetriever: Retriever inicializado
    """
    retriever = PyTorchGPURetriever(force_cpu=force_cpu, batch_size=batch_size)
    
    if not retriever.initialize():
        logger.error("Falha ao inicializar retriever")
        return None
    
    if not retriever.load_index():
        logger.error("Falha ao carregar índice")
        return None
    
    return retriever

if __name__ == "__main__":
    # Teste básico
    print("Testando PyTorch GPU Retriever...")
    
    retriever = create_pytorch_gpu_retriever()
    if retriever:
        print("[OK] Retriever criado com sucesso")
        print(f"Estatísticas: {retriever.get_stats()}")
        
        # Teste de busca
        results = retriever.search("teste de busca", top_k=5)
        print(f"Resultados encontrados: {len(results)}")
        
        for result in results:
            print(f"  - {result}")
    else:
        print("[ERROR] Falha ao criar retriever")