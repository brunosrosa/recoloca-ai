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

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core_logic.constants import (
    FAISS_INDEX_DIR,
    FAISS_INDEX_FILE,
    FAISS_DOCUMENTS_FILE,
    FAISS_METADATA_FILE,
    DEFAULT_TOP_K,
    MIN_SIMILARITY_SCORE,
    EMBEDDING_MODEL_NAME,
    STATUS_MESSAGES,
    RESULT_TEMPLATE,
    LOGS_DIR
)
from core_logic.embedding_model import initialize_embedding_model, get_embedding_manager
from core_logic.pytorch_gpu_retriever import PyTorchGPURetriever
from core_logic.pytorch_optimizations import OptimizedPyTorchRetriever

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
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
                logger.info("🔥 Usando OptimizedPyTorchRetriever")
                self.pytorch_retriever = OptimizedPyTorchRetriever(
                    force_cpu=force_cpu,
                    cache_enabled=cache_enabled,
                    batch_size=batch_size
                )
            else:
                logger.info("🔥 Usando PyTorchGPURetriever")
                self.pytorch_retriever = PyTorchGPURetriever(force_cpu=force_cpu)
            self.index = None
        else:
            logger.info("📊 Usando FAISS")
            self.pytorch_retriever = None
            self.index = None
            
        self.documents = []
        self.metadata = []
        self.index_metadata = {}
        self.is_loaded = False
        
        # Cache de consultas
        self._query_cache: Dict[str, List[SearchResult]] = {}
        self._cache_max_size = 100
        
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
                logger.info("✅ PyTorchGPURetriever inicializado com sucesso")
            else:
                # Inicializar EmbeddingManager para FAISS
                success = initialize_embedding_model(force_cpu=self.force_cpu)
                if success:
                    self.embedding_manager = get_embedding_manager()
                    logger.info("✅ Modelo de embedding inicializado")
                else:
                    logger.error("❌ Falha ao inicializar modelo de embedding")
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
            if self.use_pytorch:
                # Carregar usando PyTorchGPURetriever
                logger.info("Carregando índice PyTorch...")
                success = self.pytorch_retriever.load_index()
                if success:
                    # Sincronizar dados com o retriever principal
                    self.documents = self.pytorch_retriever.documents
                    self.metadata = self.pytorch_retriever.metadata
                    self.index_metadata = self.pytorch_retriever.index_metadata
                    self.is_loaded = True
                    logger.info(f"✅ Índice PyTorch carregado: {len(self.documents)} documentos")
                    return True
                else:
                    logger.error("❌ Falha ao carregar índice PyTorch")
                    return False
            else:
                # Carregar usando FAISS (código original)
                return self._load_faiss_index()
                
        except Exception as e:
            logger.error(f"Erro ao carregar índice: {str(e)}")
            return False
            
    def _load_faiss_index(self) -> bool:
        """
        Carrega o índice FAISS do disco (método original).
        
        Returns:
            bool: True se carregado com sucesso
        """
        try:
            # Verificar se os arquivos existem
            index_path = FAISS_INDEX_DIR / FAISS_INDEX_FILE
            documents_path = FAISS_INDEX_DIR / FAISS_DOCUMENTS_FILE
            metadata_path = FAISS_INDEX_DIR / FAISS_METADATA_FILE
            
            if not all([index_path.exists(), documents_path.exists(), metadata_path.exists()]):
                logger.error("Arquivos do índice não encontrados. Execute a indexação primeiro.")
                return False
            
            logger.info("Carregando índice FAISS...")
            start_time = time.time()
            
            # Carregar índice FAISS usando diretório temporário para evitar problemas com Unicode
            import tempfile
            import shutil
            import os
            from uuid import uuid4
            
            # Usar diretório temporário seguro
            temp_dir = "C:\\Temp" if os.name == "nt" else "/tmp"
            if not Path(temp_dir).exists():
                Path(temp_dir).mkdir(parents=True, exist_ok=True)
            
            with tempfile.TemporaryDirectory(dir=temp_dir) as temp_path:
                temp_file_path = Path(temp_path) / f"faiss_index_{uuid4().hex}.bin"
                shutil.copy2(str(index_path), str(temp_file_path))
                self.index = faiss.read_index(str(temp_file_path))
            
            logger.info(f"Índice FAISS carregado: {self.index.ntotal} vetores")
            
            # Carregar documentos
            with open(documents_path, 'r', encoding='utf-8') as f:
                self.documents = json.load(f)
            logger.info(f"Documentos carregados: {len(self.documents)} chunks")
            
            # Carregar metadados
            with open(metadata_path, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
                self.index_metadata = index_data
                self.metadata = index_data.get("documents_metadata", [])
            logger.info(f"Metadados carregados: {len(self.metadata)} entradas")
            
            # Verificar consistência
            if len(self.documents) != len(self.metadata):
                logger.warning(f"Inconsistência: {len(self.documents)} documentos vs {len(self.metadata)} metadados")
            
            if self.index.ntotal != len(self.documents):
                logger.warning(f"Inconsistência: {self.index.ntotal} vetores vs {len(self.documents)} documentos")
            
            elapsed_time = time.time() - start_time
            logger.info(f"Índice carregado em {elapsed_time:.2f}s")
            
            self.is_loaded = True
            return True
            
        except Exception as e:
            logger.error(f"Erro ao carregar índice FAISS: {str(e)}")
            return False
    
    def search(self, query: str, top_k: int = DEFAULT_TOP_K, min_score: float = MIN_SIMILARITY_SCORE, 
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
        if cache_key in self._query_cache:
            logger.debug(f"Resultado encontrado no cache para: {query[:50]}...")
            return self._query_cache[cache_key]
        
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
            
            # Cache do resultado
            self._cache_result(cache_key, results)
            
            return results
            
        except Exception as e:
            logger.error(STATUS_MESSAGES["query_error"].format(error=str(e)))
            return []
            
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

# Instância global do retriever (singleton pattern)
_retriever: Optional[RAGRetriever] = None

def get_retriever(force_cpu: bool = False, force_pytorch: bool = False) -> RAGRetriever:
    """
    Retorna a instância global do retriever.
    
    Args:
        force_cpu: Se True, força o uso de CPU
        force_pytorch: Se True, força o uso do PyTorchGPURetriever
        
    Returns:
        RAGRetriever: Instância do retriever
    """
    global _retriever
    
    if _retriever is None:
        _retriever = RAGRetriever(force_cpu=force_cpu, force_pytorch=force_pytorch)
    
    return _retriever

def initialize_retriever(force_cpu: bool = False, force_pytorch: bool = False) -> bool:
    """
    Inicializa o retriever global.
    
    Args:
        force_cpu: Se True, força o uso de CPU
        force_pytorch: Se True, força o uso do PyTorchGPURetriever
        
    Returns:
        bool: True se inicializado com sucesso
    """
    retriever = get_retriever(force_cpu=force_cpu, force_pytorch=force_pytorch)
    
    # Inicializar modelo de embedding
    if not retriever.initialize():
        return False
    
    # Carregar índice
    return retriever.load_index()

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
        
        print(f"\n🔍 Consulta: {query}")
        print(f"📊 Resultados encontrados: {len(results)}")
        
        for result in results:
            print(f"\n{result.format_result()}")
        
        # Informações do índice
        info = retriever.get_index_info()
        print(f"\n📈 Info do índice: {info}")
        
    else:
        print("❌ Falha ao inicializar retriever")