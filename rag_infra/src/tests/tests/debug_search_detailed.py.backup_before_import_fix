#!/usr/bin/env python3

import sys
import os
import json
import numpy as np
import logging
from pathlib import Path

# Adicionar diretórios ao path
sys.path.insert(0, 'core_logic')

from rag_retriever import RAGRetriever
from rag_infra.core_logic.embedding_model import EmbeddingModelManager

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def debug_search_process():
    """Debug detalhado do processo de busca."""
    try:
        logger.info("=== DEBUG DETALHADO DO PROCESSO DE BUSCA ===")
        
        # 1. Inicializar retriever
        logger.info("1. Inicializando RAGRetriever...")
        retriever = RAGRetriever()
        
        # 2. Carregar índice
        logger.info("2. Carregando índice...")
        success = retriever.load_index()
        if not success:
            logger.error("Falha ao carregar índice")
            return False
            
        logger.info(f"Índice carregado: {len(retriever.documents)} documentos")
        
        # 3. Verificar alguns documentos
        logger.info("3. Verificando primeiros documentos...")
        for i in range(min(3, len(retriever.documents))):
            doc = retriever.documents[i]
            logger.info(f"Doc {i}: {doc[:100]}...")
            
        # 4. Testar embedding da consulta
        query = "arquitetura do sistema"
        logger.info(f"4. Testando embedding da consulta: '{query}'")
        
        # Inicializar embedding model
        embedding_model = EmbeddingModelManager()
        embedding_model.load_model()
        
        query_embedding = embedding_model.embed_query(query)
        logger.info(f"Query embedding shape: {query_embedding.shape}")
        logger.info(f"Query embedding norm: {np.linalg.norm(query_embedding)}")
        
        # 5. Carregar embeddings do índice
        logger.info("5. Carregando embeddings do índice...")
        emb_file = "data_index/faiss_index_bge_m3/embeddings.npy"
        index_embeddings = np.load(emb_file)
        logger.info(f"Index embeddings shape: {index_embeddings.shape}")
        
        # 6. Calcular similaridades manualmente
        logger.info("6. Calculando similaridades manualmente...")
        
        # Normalizar embeddings
        query_norm = query_embedding / np.linalg.norm(query_embedding)
        index_norm = index_embeddings / np.linalg.norm(index_embeddings, axis=1, keepdims=True)
        
        # Calcular similaridade coseno
        similarities = np.dot(index_norm, query_norm.T).flatten()
        logger.info(f"Similaridades calculadas: {len(similarities)}")
        logger.info(f"Similaridade máxima: {np.max(similarities)}")
        logger.info(f"Similaridade mínima: {np.min(similarities)}")
        logger.info(f"Similaridade média: {np.mean(similarities)}")
        
        # Top 5 similaridades
        top_indices = np.argsort(similarities)[::-1][:5]
        logger.info("\nTop 5 similaridades:")
        for i, idx in enumerate(top_indices):
            sim = similarities[idx]
            doc_preview = retriever.documents[idx][:100] if idx < len(retriever.documents) else "N/A"
            logger.info(f"  {i+1}. Índice {idx}, Similaridade: {sim:.4f}")
            logger.info(f"     Documento: {doc_preview}...")
            
        # 7. Testar busca com threshold baixo
        logger.info("\n7. Testando busca com threshold baixo...")
        
        # Verificar se o retriever tem método para ajustar threshold
        if hasattr(retriever, 'similarity_threshold'):
            original_threshold = retriever.similarity_threshold
            logger.info(f"Threshold original: {original_threshold}")
            
            # Tentar com threshold muito baixo
            retriever.similarity_threshold = 0.0
            logger.info("Threshold ajustado para 0.0")
            
            results = retriever.search(query, top_k=5)
            logger.info(f"Resultados com threshold 0.0: {len(results)}")
            
            if results:
                for i, result in enumerate(results[:3]):
                    logger.info(f"Resultado {i+1}: {result.get('content', '')[:100]}...")
                    logger.info(f"Score: {result.get('score', 'N/A')}")
            
            # Restaurar threshold
            retriever.similarity_threshold = original_threshold
        else:
            logger.info("Retriever não tem atributo similarity_threshold")
            
        # 8. Verificar se há filtros ativos
        logger.info("\n8. Verificando filtros...")
        if hasattr(retriever, 'filters'):
            logger.info(f"Filtros ativos: {retriever.filters}")
        else:
            logger.info("Nenhum filtro encontrado")
            
        # 9. Testar busca direta no backend
        logger.info("\n9. Testando busca direta no backend...")
        if hasattr(retriever, 'backend_retriever'):
            backend = retriever.backend_retriever
            logger.info(f"Backend type: {type(backend)}")
            
            if hasattr(backend, 'search'):
                backend_results = backend.search(query, top_k=5)
                logger.info(f"Resultados do backend: {len(backend_results) if backend_results else 0}")
        
        return True
        
    except Exception as e:
        logger.error(f"Erro no debug: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    debug_search_process()