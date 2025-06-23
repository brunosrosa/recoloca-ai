# -*- coding: utf-8 -*-
"""
Retriever RAG para o Sistema Recoloca.ai

Este módulo é responsável por realizar consultas no índice FAISS,
retornando os documentos mais relevantes para uma query específica.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import faiss
import numpy as np

from .constants import (
    FAISS_INDEX_DIR,
    PYTORCH_INDEX_DIR,
    FAISS_INDEX_FILE,
    FAISS_DOCUMENTS_FILE,
    FAISS_METADATA_FILE,
    FAISS_EMBEDDINGS_FILE,
    FAISS_MAPPING_FILE,
    EMBEDDING_MODEL_NAME,
    USE_GPU,
    DEFAULT_TOP_K,
    MIN_SIMILARITY_SCORE,
    LOGS_DIR,
    STATUS_MESSAGES,
    RESULT_TEMPLATE
)
from .embedding_model import initialize_embedding_model, get_embedding_manager
from .pytorch_gpu_retriever import PyTorchGPURetriever
from .pytorch_optimizations import OptimizedPyTorchRetriever

# Importar sistema de métricas
try:
    from .rag_metrics_integration import track_query, track_batch_query, metrics_integration
    METRICS_AVAILABLE = True
except ImportError:
    METRICS_AVAILABLE = False
    # Decoradores vazios se métricas não disponíveis
    def track_query(func):
        return func
    def track_batch_query(func):
        return func

# Configurar logging
import sys
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger(__name__)

# Criar handler para arquivo de log
LOGS_DIR.mkdir(parents=True, exist_ok=True)
file_handler = logging.FileHandler(LOGS_DIR / "rag_retriever.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Constantes
MAX_TOP_K = 100
CACHE_MAX_SIZE = 1000

def _detect_gpu_compatibility() -> bool:
    """
    Detecta se a GPU é compatível com FAISS-GPU.
    
    Returns:
        bool: True se compatível com FAISS-GPU, False caso contrário
    """
    try:
        import torch
        if not torch.cuda.is_available():
            logger.info("CUDA não disponível - usando CPU")
            return False
            
        # Verificar se é RTX 2060 ou similar (problemas conhecidos com FAISS-GPU)
        gpu_name = torch.cuda.get_device_name(0).lower()
        incompatible_gpus = ['rtx 2060', 'gtx 1660', 'gtx 1650']
        
        for incompatible in incompatible_gpus:
            if incompatible in gpu_name:
                logger.info(f"GPU {gpu_name} detectada - usando PyTorch em vez de FAISS-GPU")
                return False
                
        # Tentar importar FAISS-GPU
        try:
            import faiss
            if hasattr(faiss, 'StandardGpuResources'):
                logger.info(f"GPU {gpu_name} compatível com FAISS-GPU")
                return True
        except Exception as e:
            logger.warning(f"FAISS-GPU não disponível: {e}")
            
        return False
        
    except Exception as e:
        logger.warning(f"Erro na detecção de GPU: {e}")
        return False

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
        return RESULT_TEMPLATE.format(
            source=self.metadata.get("source", "Desconhecido"),
            section=self.metadata.get("section", "main"),
            score=self.score,
            content=self.content[:500] + "..." if len(self.content) > 500 else self.content
        )
    
    def __str__(self) -> str:
        return f"SearchResult(rank={self.rank}, score={self.score:.3f}, source={self.metadata.get('source', 'Unknown')})"
    
    def __repr__(self) -> str:
        return self.__str__()

class RAGRetriever:
    """
    Classe principal para recuperação de documentos usando FAISS ou PyTorch.
    Implementa fallback inteligente baseado na compatibilidade da GPU.
    """
    
    def __init__(self, force_cpu: bool = False, force_pytorch: bool = False, use_optimizations: bool = False, cache_enabled: bool = True, batch_size: int = 5):
        """
        Inicializa o retriever.
        
        Args:
            force_cpu: Se True, força o uso de CPU mesmo com GPU disponível
            force_pytorch: Se True, força o uso do PyTorchGPURetriever
            use_optimizations: Usar versão otimizada com cache e batch processing
            cache_enabled: Habilitar cache persistente (apenas com otimizações)
            batch_size: Tamanho do batch para processamento (apenas com otimizações)
        """
        self.force_cpu = force_cpu
        self.force_pytorch = force_pytorch
        self.use_optimizations = use_optimizations
        self.cache_enabled = cache_enabled
        self.batch_size = batch_size
        self.embedding_manager = None
        
        # Detectar qual backend usar
        self.use_pytorch = self._should_use_pytorch()
        
        # Inicializar backend apropriado
        if self.use_pytorch:
            if use_optimizations:
                logger.info("Usando OptimizedPyTorchRetriever")
                self.pytorch_retriever = OptimizedPyTorchRetriever(
                    index_dir=PYTORCH_INDEX_DIR,
                    force_cpu=force_cpu,
                    cache_enabled=cache_enabled,
                    batch_size=batch_size
                )
            else:
                logger.info("Usando PyTorchGPURetriever")
                self.pytorch_retriever = PyTorchGPURetriever(index_dir=PYTORCH_INDEX_DIR, force_cpu=force_cpu)
            self.index = None
        else:
            logger.info("Usando FAISS")
            self.pytorch_retriever = None
            self.index = None
            
        self.documents = []
        self.metadata = []
        self.index_metadata = {}
        self.is_loaded = False
        
        # Cache de consultas
        self._query_cache: Dict[str, List[SearchResult]] = {}
        self._cache_max_size = 100
        
    @property
    def is_initialized(self) -> bool:
        """Verifica se o retriever foi inicializado corretamente."""
        if self.use_pytorch:
            return self.pytorch_retriever is not None and hasattr(self.pytorch_retriever, 'embedding_manager') and self.pytorch_retriever.embedding_manager is not None
        else:
            return self.embedding_manager is not None
        
    def _should_use_pytorch(self) -> bool:
        """
        Determina se deve usar PyTorch em vez de FAISS.
        
        Returns:
            bool: True se deve usar PyTorch
        """
        if self.force_pytorch:
            return True
            
        if self.force_cpu:
            return False
            
        # Usar PyTorch se GPU não for compatível com FAISS
        return not _detect_gpu_compatibility()
    
    def initialize(self) -> bool:
        """
        Inicializa o modelo de embedding e o backend apropriado.
        
        Returns:
            bool: True se inicializado com sucesso
        """
        try:
            logger.info("Inicializando modelo de embedding...")
            
            if self.use_pytorch:
                # Inicializar PyTorchGPURetriever
                success = self.pytorch_retriever.initialize()
                if not success:
                    logger.error("Falha ao inicializar PyTorchGPURetriever")
                    return False
                logger.info("[OK] PyTorchGPURetriever inicializado com sucesso")
            else:
                # Inicializar EmbeddingManager para FAISS
                self.embedding_manager = initialize_embedding_model(force_cpu=self.force_cpu)

            if self.embedding_manager is None:
                logger.error("Falha ao inicializar o EmbeddingModelManager. O RAGRetriever não pode operar sem ele.")
                raise RuntimeError("EmbeddingModelManager não inicializado.")

            if self.embedding_manager.is_loaded:
                logger.info("[OK] Modelo de embedding inicializado com sucesso.")
            else:
                logger.error("[ERROR] Falha crítica: Não foi possível inicializar o EmbeddingModelManager.")
                self.is_loaded = False
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Erro na inicialização: {str(e)}")
            return False
    
    def load_index(self) -> bool:
        """
        Carrega o índice do disco (FAISS ou PyTorch).
        
        Returns:
            bool: True se carregado com sucesso
        """
        try:
            logger.info(f"DEBUG: use_pytorch = {self.use_pytorch}")
            logger.info(f"DEBUG: pytorch_retriever = {self.pytorch_retriever}")
            
            if self.use_pytorch:
                # Carregar usando PyTorchGPURetriever
                logger.info("Carregando índice PyTorch...")
                
                if not self.pytorch_retriever:
                    logger.error("[ERROR] pytorch_retriever não está inicializado")
                    return False
                    
                success = self.pytorch_retriever.load_index()
                logger.info(f"DEBUG: pytorch_retriever.load_index() retornou: {success}")
                
                if success:
                    # Sincronizar dados com o retriever principal
                    # Para OptimizedPyTorchRetriever, acessar através do base_retriever
                    if hasattr(self.pytorch_retriever, 'base_retriever'):
                        # É um OptimizedPyTorchRetriever
                        self.documents = self.pytorch_retriever.base_retriever.documents
                        self.metadata = self.pytorch_retriever.base_retriever.metadata
                        self.index_metadata = self.pytorch_retriever.base_retriever.index_metadata
                    else:
                        # É um PyTorchGPURetriever direto
                        self.documents = self.pytorch_retriever.documents
                        self.metadata = self.pytorch_retriever.metadata
                        self.index_metadata = self.pytorch_retriever.index_metadata
                    
                    self.is_loaded = True
                    logger.info(f"[OK] Índice PyTorch carregado: {len(self.documents)} documentos")
                    return True
                else:
                    logger.error("[ERROR] Falha ao carregar índice PyTorch")
                    return False
            else:
                # Carregar usando FAISS (código original)
                logger.info("Carregando índice FAISS...")
                return self._load_faiss_index()
                
        except Exception as e:
            logger.error(f"Erro ao carregar índice: {str(e)}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            return False
            
    def _load_faiss_index(self) -> bool:
        """
        Carrega o índice FAISS e os dados associados com logging detalhado.
        """
        logger.info(f"Iniciando carregamento do índice FAISS de: {FAISS_INDEX_DIR}")
        start_time = time.time()
        try:
            # Construir caminhos completos
            faiss_index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            index_metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE # Reutilizando o de metadados por enquanto

            # 1. Carregar índice FAISS
            if not faiss_index_path.exists():
                logger.error(f"[FAISS Load] Arquivo de índice não encontrado: {faiss_index_path}")
                return False
            self.index = faiss.read_index(str(faiss_index_path))
            logger.info(f"[FAISS Load] Índice FAISS carregado com {self.index.ntotal} vetores.")

            # 2. Carregar documentos
            if not documents_path.exists():
                logger.error(f"[FAISS Load] Arquivo de documentos não encontrado: {documents_path}")
                return False
            with open(documents_path, 'r', encoding='utf-8') as f:
                self.documents = json.load(f)
            logger.info(f"[FAISS Load] Documentos carregados: {len(self.documents)} chunks.")

            # 3. Carregar metadados dos documentos
            if not metadata_path.exists():
                logger.error(f"[FAISS Load] Arquivo de metadados não encontrado: {metadata_path}")
                return False
            with open(metadata_path, 'r', encoding='utf-8') as f:
                self.metadata = json.load(f)
            logger.info(f"[FAISS Load] Metadados carregados: {len(self.metadata)} entradas.")

            # 4. Carregar metadados do índice
            if not index_metadata_path.exists():
                logger.warning(f"[FAISS Load] Arquivo de metadados do índice não encontrado: {index_metadata_path}")
                self.index_metadata = {} # Definir como vazio se não existir
            else:
                with open(index_metadata_path, 'r', encoding='utf-8') as f:
                    self.index_metadata = json.load(f)
                logger.info(f"[FAISS Load] Metadados do índice carregados.")

            # 5. Verificar consistência
            if len(self.documents) != len(self.metadata):
                logger.warning(f"[FAISS Consistency] Inconsistência: {len(self.documents)} documentos vs {len(self.metadata)} metadados.")
            if self.index.ntotal != len(self.documents):
                logger.warning(f"[FAISS Consistency] Inconsistência: {self.index.ntotal} vetores vs {len(self.documents)} documentos.")

            elapsed_time = time.time() - start_time
            logger.info(f"[FAISS Load] Índice FAISS e dados carregados com sucesso em {elapsed_time:.2f}s.")
            self.is_loaded = True
            return True

        except FileNotFoundError as e:
            logger.error(f"[FAISS Load Error] Arquivo não encontrado durante o carregamento: {e}", exc_info=True)
            return False
        except json.JSONDecodeError as e:
            logger.error(f"[FAISS Load Error] Erro de decodificação JSON, o arquivo pode estar corrompido: {e}", exc_info=True)
            return False
        except Exception as e:
            logger.error(f"[FAISS Load Error] Erro inesperado ao carregar índice FAISS: {e}", exc_info=True)
            return False
    
    @track_query
    def search(self, query: str, top_k: int = DEFAULT_TOP_K, 
                min_score: float = MIN_SIMILARITY_SCORE, 
                category_filter: Optional[str] = None) -> List[SearchResult]:
        """
        Realiza busca semântica no índice.
        
        Args:
            query: Consulta de busca
            top_k: Número de resultados a retornar
            min_score: Score mínimo de similaridade
            category_filter: Filtro por categoria (opcional)
            
        Returns:
            List[SearchResult]: Lista de resultados ordenados por relevância
        """
        if not self.is_loaded:
            logger.error("Índice não carregado. Chame load_index() primeiro.")
            return []
        
        # Validar parâmetros
        top_k = min(max(1, top_k), 100)  # MAX_TOP_K
        min_score = max(0.0, min(1.0, min_score))
        
        # Verificar cache
        cache_key = f"{query}_{top_k}_{min_score}_{category_filter}"
        cache_hit = False
        if cache_key in self._query_cache:
            cache_hit = True
            logger.debug(f"Resultado encontrado no cache para: {query[:50]}...")
            cached_results = self._query_cache[cache_key]
            # Adicionar informação de cache hit aos metadados
            for result in cached_results:
                if hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                    result.metadata['cache_hit'] = True
            return cached_results
        
        try:
            logger.info(STATUS_MESSAGES["query_start"].format(query=query[:100]))
            start_time = time.time()
            
            if self.use_pytorch:
                # Usar PyTorchGPURetriever
                pytorch_results = self.pytorch_retriever.search(
                    query=query,
                    top_k=top_k,
                    min_score=min_score
                )
                
                # Converter para SearchResult e aplicar filtro de categoria
                results = []
                for pytorch_result in pytorch_results:
                    # Aplicar filtro de categoria se especificado
                    if category_filter and pytorch_result.metadata.get("category") != category_filter:
                        continue
                        
                    # Converter para o formato SearchResult do RAGRetriever
                    result = SearchResult(
                        content=pytorch_result.content,
                        metadata=pytorch_result.metadata,
                        score=pytorch_result.score,
                        rank=pytorch_result.rank
                    )
                    results.append(result)
                    
                    if len(results) >= top_k:
                        break
                        
            else:
                # Usar FAISS (código original)
                results = self._search_faiss(query, top_k, min_score, category_filter)
            
            elapsed_time = time.time() - start_time
            logger.info(STATUS_MESSAGES["query_complete"].format(count=len(results)))
            logger.info(f"Busca realizada em {elapsed_time:.3f}s")
            
            # Adicionar informação de cache miss aos metadados
            for result in results:
                if hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                    result.metadata['cache_hit'] = False
            
            # Cache do resultado
            self._cache_result(cache_key, results)
            
            return results
            
        except Exception as e:
            logger.error(STATUS_MESSAGES["query_error"].format(error=str(e)))
            return []
    
    @track_batch_query
    def search_batch(self, queries: List[str], top_k: int = DEFAULT_TOP_K, 
                    min_score: float = MIN_SIMILARITY_SCORE, 
                    category_filter: Optional[str] = None) -> List[List[SearchResult]]:
        """
        Realiza busca semântica em lote para múltiplas consultas.
        
        Args:
            queries: Lista de consultas de busca
            top_k: Número de resultados a retornar por consulta
            min_score: Score mínimo de similaridade
            category_filter: Filtro por categoria (opcional)
            
        Returns:
            List[List[SearchResult]]: Lista de listas de resultados para cada consulta
        """
        if not queries:
            return []
        
        logger.info(f"Iniciando busca em lote para {len(queries)} consultas")
        start_time = time.time()
        
        results = []
        cache_hits = 0
        
        try:
            # Processar cada consulta
            for i, query in enumerate(queries):
                query_results = self.search(query, top_k, min_score, category_filter)
                
                # Contar cache hits
                for result in query_results:
                    if hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                        if result.metadata.get('cache_hit', False):
                            cache_hits += 1
                        # Adicionar informação de lote
                        result.metadata['batch_index'] = i
                        result.metadata['batch_size'] = len(queries)
                
                results.append(query_results)
            
            elapsed_time = time.time() - start_time
            total_results = sum(len(r) for r in results)
            cache_hit_rate = cache_hits / total_results if total_results > 0 else 0
            
            logger.info(f"Busca em lote concluída: {len(queries)} consultas, "
                       f"{total_results} resultados, {elapsed_time:.3f}s, "
                       f"cache hit rate: {cache_hit_rate:.2%}")
            
            return results
            
        except Exception as e:
            logger.error(f"Erro durante busca em lote: {e}")
            return [[] for _ in queries]
            
    def _search_faiss(self, query: str, top_k: int, min_score: float, 
                     category_filter: Optional[str] = None) -> List[SearchResult]:
        """
        Realiza busca usando FAISS (método original).
        
        Args:
            query: Consulta de busca
            top_k: Número de resultados a retornar
            min_score: Score mínimo de similaridade
            category_filter: Filtro por categoria (opcional)
            
        Returns:
            List[SearchResult]: Lista de resultados ordenados por relevância
        """
        if not self.embedding_manager:
            logger.error("Modelo de embedding não inicializado.")
            return []
            
        # 1. Gerar embedding da consulta
        query_embedding = self.embedding_manager.embed_query(query)
        if query_embedding is None:
            logger.error("Falha ao gerar embedding da consulta")
            return []
        
        # 2. Buscar no índice FAISS
        query_vector = query_embedding.reshape(1, -1).astype('float32')
        scores, indices = self.index.search(query_vector, top_k * 2)  # Buscar mais para filtrar
        
        # 3. Processar resultados
        results = []
        for rank, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx == -1:  # Índice inválido
                continue
            
            if score < min_score:
                continue
            
            # Obter documento e metadados
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
        
        # 4. Reordenar por score (descendente)
        results.sort(key=lambda x: x.score, reverse=True)
        
        # 5. Atualizar ranks
        for i, result in enumerate(results):
            result.rank = i + 1
        
        return results
    
    def search_by_document(self, document_pattern: str, top_k: int = DEFAULT_TOP_K) -> List[SearchResult]:
        """
        Busca documentos por padrão no nome/caminho.
        
        Args:
            document_pattern: Padrão para buscar no nome do documento
            top_k: Número máximo de resultados
            
        Returns:
            List[SearchResult]: Lista de resultados encontrados
        """
        if not self.is_loaded:
            logger.error("Índice não carregado.")
            return []
        
        try:
            results = []
            pattern_lower = document_pattern.lower()
            
            for idx, metadata in enumerate(self.metadata):
                source = metadata.get("source", "").lower()
                title = metadata.get("title", "").lower()
                
                if pattern_lower in source or pattern_lower in title:
                    if idx < len(self.documents):
                        result = SearchResult(
                            content=self.documents[idx],
                            metadata=metadata,
                            score=1.0,  # Score fixo para busca por documento
                            rank=len(results) + 1
                        )
                        results.append(result)
                        
                        if len(results) >= top_k:
                            break
            
            logger.info(f"Encontrados {len(results)} documentos para padrão: {document_pattern}")
            return results
            
        except Exception as e:
            logger.error(f"Erro na busca por documento: {str(e)}")
            return []
    
    def get_document_list(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retorna lista de documentos indexados.
        
        Args:
            category: Filtro por categoria (opcional)
            
        Returns:
            List[Dict]: Lista de informações dos documentos
        """
        if not self.is_loaded:
            logger.error("Índice não carregado.")
            return []
        
        try:
            documents_info = []
            
            # Agrupar chunks por documento fonte
            doc_groups = {}
            for metadata in self.metadata:
                source = metadata.get("source", "unknown")
                doc_category = metadata.get("category", "general")
                
                # Aplicar filtro de categoria se especificado
                if category and doc_category != category:
                    continue
                
                if source not in doc_groups:
                    doc_groups[source] = {
                        "source": source,
                        "title": metadata.get("title", "Sem título"),
                        "category": doc_category,
                        "file_type": metadata.get("file_type", "unknown"),
                        "chunks_count": 0,
                        "last_updated": metadata.get("timestamp", "unknown")
                    }
                
                doc_groups[source]["chunks_count"] += 1
            
            documents_info = list(doc_groups.values())
            documents_info.sort(key=lambda x: x["source"])
            
            logger.info(f"Retornando informações de {len(documents_info)} documentos")
            return documents_info
            
        except Exception as e:
            logger.error(f"Erro ao obter lista de documentos: {str(e)}")
            return []
    
    def get_index_info(self) -> Dict[str, Any]:
        """
        Retorna informações sobre o índice carregado.
        
        Returns:
            Dict: Informações do índice
        """
        if not self.is_loaded:
            return {"loaded": False, "error": "Índice não carregado"}
        
        base_info = {
            "loaded": True,
            "backend": "PyTorch_Optimized" if (self.use_pytorch and self.use_optimizations) else ("PyTorch" if self.use_pytorch else "FAISS"),
            "total_documents": len(self.documents),
            "total_metadata": len(self.metadata),
            "embedding_model": self.index_metadata.get("embedding_model", "unknown"),
            "created_at": self.index_metadata.get("created_at", "unknown"),
            "index_dimension": self.index_metadata.get("index_dimension", 0),
            "chunk_size": self.index_metadata.get("chunk_size", 0),
            "chunk_overlap": self.index_metadata.get("chunk_overlap", 0),
            "cache_size": len(self._query_cache),
            "optimizations_enabled": self.use_optimizations
        }
        
        if self.use_pytorch:
            # Informações específicas do PyTorch
            pytorch_info = self.pytorch_retriever.get_index_info()
            base_info.update({
                "total_vectors": pytorch_info.get("total_vectors", 0),
                "device": pytorch_info.get("device", "unknown"),
                "gpu_available": pytorch_info.get("gpu_available", False),
                "memory_usage": pytorch_info.get("memory_usage", "unknown")
            })
            
            # Adicionar estatísticas se usando otimizações
            if self.use_optimizations and hasattr(self.pytorch_retriever, 'get_stats'):
                base_info["performance_stats"] = self.pytorch_retriever.get_stats()
        else:
            # Informações específicas do FAISS
            base_info["total_vectors"] = self.index.ntotal if self.index else 0
            
        return base_info
    
    def get_backend_info(self) -> Dict[str, Any]:
        """Obtém informações sobre o backend atual."""
        import torch
        
        gpu_available = torch.cuda.is_available()
        recommended_backend = "pytorch" if gpu_available else "sklearn"
        
        backend_info = {
            "current_backend": "OptimizedPyTorch" if self.use_optimizations else "PyTorch" if self.force_pytorch else "Auto",
            "recommended_backend": recommended_backend,
            "gpu_available": gpu_available,
            "cuda_device_count": torch.cuda.device_count() if gpu_available else 0
        }
        
        if gpu_available:
            backend_info["gpu_name"] = torch.cuda.get_device_name(0)
            backend_info["gpu_memory_total"] = torch.cuda.get_device_properties(0).total_memory
        
        return backend_info
    
    def _cache_result(self, cache_key: str, results: List[SearchResult]) -> None:
        """
        Armazena resultado no cache.
        
        Args:
            cache_key: Chave do cache
            results: Resultados para cachear
        """
        # Limpar cache se estiver muito grande
        if len(self._query_cache) >= self._cache_max_size:
            # Remover entradas mais antigas (FIFO simples)
            oldest_key = next(iter(self._query_cache))
            del self._query_cache[oldest_key]
        
        self._query_cache[cache_key] = results
    
    def clear_cache(self) -> None:
        """
        Limpa o cache de consultas.
        """
        cache_size = len(self._query_cache)
        self._query_cache.clear()
        logger.info(f"Cache limpo. {cache_size} consultas removidas.")
    
    def reload_index(self) -> bool:
        """
        Recarrega o índice do disco.
        
        Returns:
            bool: True se recarregado com sucesso
        """
        logger.info("Recarregando índice...")
        self.is_loaded = False
        self.clear_cache()
        return self.load_index()

# Variável global para armazenar a instância do retriever
_retriever_instance: Optional[RAGRetriever] = None

def initialize_retriever(backend: Optional[str] = None, 
                           device: Optional[str] = None, 
                           use_optimizations: bool = True) -> Optional[RAGRetriever]:
    """
    Função de fábrica para criar e inicializar o RAGRetriever.
    Detecta automaticamente o melhor backend e dispositivo se não forem fornecidos.

    Args:
        backend (Optional[str]): O backend a ser usado ('pytorch' or 'faiss'). Auto-detecta se None.
        device (Optional[str]): O dispositivo a ser usado ('cuda' or 'cpu'). Auto-detecta se None.
        use_optimizations (bool): Habilitar otimizações de performance.

    Returns:
        Optional[RAGRetriever]: Instância do retriever ou None se falhar.
    """
    global _retriever_instance
    
    # Lógica de auto-detecção
    if backend is None or device is None:
        gpu_available = _detect_gpu_compatibility()
        if gpu_available and backend is None:
            backend = 'pytorch'
            logger.info("Backend auto-detectado: 'pytorch' (GPU disponível)")
        elif backend is None:
            backend = 'faiss'
            logger.info("Backend auto-detectado: 'faiss' (GPU não disponível ou incompatível)")

        if gpu_available and device is None:
            device = 'cuda'
            logger.info("Dispositivo auto-detectado: 'cuda'")
        elif device is None:
            device = 'cpu'
            logger.info("Dispositivo auto-detectado: 'cpu'")

    logger.info(f"Tentando inicializar RAGRetriever com: backend='{backend}', device='{device}', optimizations={use_optimizations}")
    
    try:
        # Força a recriação da instância para refletir novos parâmetros
        force_cpu = (device == 'cpu')
        force_pytorch = (backend == 'pytorch')

        _retriever_instance = RAGRetriever(
            force_cpu=force_cpu,
            force_pytorch=force_pytorch,
            use_optimizations=use_optimizations
        )

        logger.info("Etapa 1: Iniciando retriever.initialize()...")
        initialized_ok = _retriever_instance.initialize()
        logger.info(f"Etapa 1.1: retriever.initialize() concluído. Sucesso: {initialized_ok}")
        if not initialized_ok:
            logger.error("FALHA CRÍTICA na etapa de inicialização do retriever (embedding ou backend). Retornando None.")
            _retriever_instance = None # Garante que a instância falha seja descartada
            return None

        logger.info("Etapa 2: Iniciando retriever.load_index()...")
        loaded_ok = _retriever_instance.load_index()
        logger.info(f"Etapa 2.1: retriever.load_index() concluído. Sucesso: {loaded_ok}")
        if not loaded_ok:
            logger.error("FALHA CRÍTICA ao carregar o índice do retriever. Retornando None.")
            _retriever_instance = None # Garante que a instância falha seja descartada
            return None

        logger.info(f"[OK] Retriever (backend: {backend}, device: {device}) inicializado e índice carregado com sucesso.")
        return _retriever_instance

    except Exception as e:
        # Log aprimorado para capturar o traceback completo
        logger.critical(f"Exceção não tratada durante a inicialização do retriever: {e}", exc_info=True)
        _retriever_instance = None # Garante que a instância falha seja descartada
        return None

def get_retriever(force_reinitialization: bool = False) -> Optional[RAGRetriever]:
    """
    Retorna a instância global do RAGRetriever, inicializando se necessário.

    Args:
        force_reinitialization (bool): Se True, força a reinicialização do retriever.

    Returns:
        Optional[RAGRetriever]: A instância do retriever ou None se não inicializado.
    """
    global _retriever_instance
    # Se a instância não existir ou se a reinicialização for forçada
    if _retriever_instance is None or force_reinitialization:
        if force_reinitialization:
            logger.info("Forçando a reinicialização do retriever.")
        else:
            logger.warning("Retriever não inicializado. Tentando inicialização padrão.")
        
        # A chamada agora usa os padrões inteligentes de initialize_retriever
        initialize_retriever() 
    
    return _retriever_instance

def search_documents(query: str, top_k: int = DEFAULT_TOP_K, 
                    min_score: float = MIN_SIMILARITY_SCORE,
                    category_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Função de conveniência para busca de documentos.
    
    Args:
        query: Consulta de busca
        top_k: Número de resultados
        min_score: Score mínimo
        category_filter: Filtro por categoria
        
    Returns:
        List[Dict]: Resultados da busca
    """
    retriever = get_retriever()
    
    if not retriever.is_loaded:
        logger.error("Retriever não inicializado")
        return []
    
    results = retriever.search(query, top_k, min_score, category_filter)
    return [result.to_dict() for result in results]

if __name__ == "__main__":
    # Teste do módulo
    print("🧪 Testando módulo retriever...")
    
    # Inicializar retriever
    success = initialize_retriever()
    
    if success:
        retriever = get_retriever()
        
        # Teste de consulta
        query = "Como implementar autenticação no FastAPI?"
        results = retriever.search(query, top_k=3)
        
        print(f"\n[SEARCH] Consulta: {query}")
        print(f"[EMOJI] Resultados encontrados: {len(results)}")
        
        for result in results:
            print(f"\n{result.format_result()}")
        
        # Informações do índice
        info = retriever.get_index_info()
        print(f"\n[EMOJI] Info do índice: {info}")
        
    else:
        print("[ERROR] Falha ao inicializar retriever")
