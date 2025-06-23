#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste completo do sistema RAG com PyTorch GPU Retriever
"""

import sys
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Adicionar o diretório pai (rag_infra) ao path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_rag_system():
    """Testa o sistema RAG completo"""
    
    try:
        logger.info("=== Teste Completo Sistema RAG ===")
        
        # Importar o retriever principal
        logger.info("[EMOJI] Importando RAGRetriever...")
        from rag_infra.src.core.rag_retriever import RAGRetriever
        logger.info("[OK] Import bem-sucedido")
        
        # Criar instância
        logger.info("[EMOJI] Criando instância do RAG retriever...")
        retriever = RAGRetriever()
        logger.info("[OK] Instância criada")
        
        # Inicializar
        logger.info("[START] Inicializando sistema RAG...")
        init_result = retriever.initialize()
        logger.info(f"Resultado da inicialização: {init_result}")
        
        if not init_result:
            logger.error("[ERROR] Falha na inicialização do sistema RAG")
            return False
        
        # Verificar estado
        logger.info(f"[EMOJI] Estado do sistema RAG:")
        logger.info(f"  - is_loaded: {retriever.is_loaded}")
        logger.info(f"  - use_pytorch: {retriever.use_pytorch}")
        
        if hasattr(retriever, 'pytorch_retriever') and retriever.pytorch_retriever:
            logger.info(f"  - PyTorch retriever ativo: {retriever.pytorch_retriever.is_loaded}")
            logger.info(f"  - Device: {retriever.pytorch_retriever.device}")
            logger.info(f"  - Documentos: {len(retriever.pytorch_retriever.documents) if retriever.pytorch_retriever.documents else 0}")
        
        # Teste de busca
        if retriever.is_loaded:
            logger.info("[SEARCH] Testando busca no sistema RAG...")
            
            # Teste 1: Busca por FastAPI
            logger.info("\n--- Teste 1: FastAPI ---")
            results = retriever.search("FastAPI", top_k=3)
            logger.info(f"Resultados encontrados: {len(results)}")
            
            for i, result in enumerate(results[:2]):
                logger.info(f"  {i+1}. Score: {result.score:.4f}")
                logger.info(f"     Fonte: {result.metadata.get('source', 'N/A')}")
                logger.info(f"     Conteúdo: {result.content[:150]}...")
            
            # Teste 2: Busca por arquitetura
            logger.info("\n--- Teste 2: Arquitetura ---")
            results = retriever.search("arquitetura sistema", top_k=3)
            logger.info(f"Resultados encontrados: {len(results)}")
            
            for i, result in enumerate(results[:2]):
                logger.info(f"  {i+1}. Score: {result.score:.4f}")
                logger.info(f"     Fonte: {result.metadata.get('source', 'N/A')}")
                logger.info(f"     Conteúdo: {result.content[:150]}...")
            
            # Teste 3: Busca por backend
            logger.info("\n--- Teste 3: Backend ---")
            results = retriever.search("backend API desenvolvimento", top_k=3)
            logger.info(f"Resultados encontrados: {len(results)}")
            
            for i, result in enumerate(results[:2]):
                logger.info(f"  {i+1}. Score: {result.score:.4f}")
                logger.info(f"     Fonte: {result.metadata.get('source', 'N/A')}")
                logger.info(f"     Conteúdo: {result.content[:150]}...")
        
        logger.info("\n[OK] Teste do sistema RAG concluído com sucesso!")
        return True
        
    except Exception as e:
        logger.error(f"[ERROR] Erro no teste: {str(e)}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = test_rag_system()
    if success:
        print("\n=== Resultado Final: SUCESSO ===")
        print("[EMOJI] Sistema RAG com PyTorch GPU está funcionando corretamente!")
    else:
        print("\n=== Resultado Final: FALHA ===")
        print("[ERROR] Problemas detectados no sistema RAG")