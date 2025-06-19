#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core_logic'))

import logging
from rag_infra.core_logic.rag_retriever import RAGRetriever
from rag_infra.core_logic.embedding_model import EmbeddingModelManager
import numpy as np

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def test_architecture_search():
    """Testa especificamente a busca por arquitetura"""
    try:
        logger.info("=== TESTE DE BUSCA POR ARQUITETURA ===")
        
        # 1. Inicializar retriever
        logger.info("1. Inicializando RAGRetriever...")
        retriever = RAGRetriever()
        
        # 2. Carregar índice
        logger.info("2. Carregando índice...")
        retriever.load_index()
        logger.info(f"Índice carregado: {len(retriever.documents)} documentos")
        
        # 3. Testar diferentes queries relacionadas à arquitetura
        queries = [
            "arquitetura do sistema",
            "arquitetura",
            "sistema",
            "FastAPI",
            "backend",
            "API",
            "Supabase",
            "database",
            "estrutura"
        ]
        
        for query in queries:
            logger.info(f"\n--- Testando query: '{query}' ---")
            
            # Buscar
            results = retriever.search(query, top_k=3)
            logger.info(f"Resultados encontrados: {len(results)}")
            
            if results:
                for i, result in enumerate(results):
                    content = result.get('content', '')[:150]
                    score = result.get('score', 'N/A')
                    metadata = result.get('metadata', {})
                    source = metadata.get('source', 'N/A')
                    
                    logger.info(f"  {i+1}. Score: {score}")
                    logger.info(f"     Source: {source}")
                    logger.info(f"     Content: {content}...")
            else:
                logger.info("  Nenhum resultado encontrado")
        
        # 4. Verificar se há documentos com 'arquitetura' no conteúdo
        logger.info("\n4. Verificando documentos que contêm 'arquitetura'...")
        arch_docs = []
        for i, doc in enumerate(retriever.documents):
            if 'arquitetura' in doc.lower():
                arch_docs.append((i, doc[:100]))
        
        logger.info(f"Documentos com 'arquitetura': {len(arch_docs)}")
        for i, (idx, preview) in enumerate(arch_docs[:5]):
            logger.info(f"  {i+1}. Índice {idx}: {preview}...")
        
        # 5. Testar embedding manual
        logger.info("\n5. Testando embedding manual...")
        embedding_model = EmbeddingModelManager()
        embedding_model.load_model()
        
        query_embedding = embedding_model.embed_query("arquitetura do sistema")
        logger.info(f"Query embedding shape: {query_embedding.shape}")
        
        # Carregar embeddings do índice
        embeddings_path = os.path.join(retriever.index_dir, "embeddings.npy")
        if os.path.exists(embeddings_path):
            embeddings = np.load(embeddings_path)
            logger.info(f"Index embeddings shape: {embeddings.shape}")
            
            # Calcular similaridades manualmente
            similarities = np.dot(embeddings, query_embedding)
            top_indices = np.argsort(similarities)[::-1][:5]
            
            logger.info("Top 5 similaridades manuais:")
            for i, idx in enumerate(top_indices):
                sim = similarities[idx]
                doc_preview = retriever.documents[idx][:100] if idx < len(retriever.documents) else "N/A"
                logger.info(f"  {i+1}. Índice {idx}, Similaridade: {sim:.4f}")
                logger.info(f"     Documento: {doc_preview}...")
        
        assert True
        
    except Exception as e:
        logger.error(f"Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        assert False, f"Erro no teste: {e}"

if __name__ == "__main__":
    test_architecture_search()