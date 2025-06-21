#!/usr/bin/env python3
"""
Script para debugar especificamente o OptimizedPyTorchRetriever
usado através do RAGRetriever.
"""

import sys
import os
import logging
from pathlib import Path

# Adicionar o diretório raiz ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "rag_infra"))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def test_optimized_retriever_direct():
    """Testa OptimizedPyTorchRetriever diretamente."""
    logger.info("🔍 Testando OptimizedPyTorchRetriever diretamente...")
    
    try:
        from rag_infra.core_logic.pytorch_optimizations import OptimizedPyTorchRetriever
        
        retriever = OptimizedPyTorchRetriever(force_cpu=False)
        
        # Inicializar
        logger.info("Inicializando OptimizedPyTorchRetriever...")
        init_success = retriever.initialize()
        logger.info(f"Inicialização: {'✅ SUCESSO' if init_success else '❌ FALHA'}")
        
        if not init_success:
            return False
        
        # Carregar índice
        logger.info("Carregando índice...")
        load_success = retriever.load_index()
        logger.info(f"Carregamento: {'✅ SUCESSO' if load_success else '❌ FALHA'}")
        
        if not load_success:
            return False
        
        # Testar busca
        logger.info("Testando busca...")
        results = retriever.search("FastAPI", top_k=5)
        logger.info(f"Resultados: {len(results)}")
        
        if results:
            for i, result in enumerate(results[:3]):
                logger.info(f"  {i+1}. Score: {result.score:.4f} - {result.content[:100]}...")
            return True
        else:
            logger.error("❌ Nenhum resultado encontrado")
            return False
            
    except Exception as e:
        logger.error(f"❌ Erro: {e}")
        return False

def test_rag_retriever_with_optimizations():
    """Testa RAGRetriever com use_optimizations=True."""
    logger.info("🔍 Testando RAGRetriever com use_optimizations=True...")
    
    try:
        from rag_infra.core_logic.rag_retriever import RAGRetriever
        
        retriever = RAGRetriever(
            force_pytorch=True, 
            use_optimizations=True,
            cache_enabled=True,
            batch_size=5
        )
        
        # Debug: verificar estado inicial
        logger.info(f"use_pytorch: {retriever.use_pytorch}")
        logger.info(f"use_optimizations: {retriever.use_optimizations}")
        logger.info(f"pytorch_retriever type: {type(retriever.pytorch_retriever)}")
        
        # Inicializar
        logger.info("Inicializando RAGRetriever...")
        init_success = retriever.initialize()
        logger.info(f"Inicialização: {'✅ SUCESSO' if init_success else '❌ FALHA'}")
        
        if not init_success:
            return False
        
        # Debug: verificar estado após inicialização
        if hasattr(retriever.pytorch_retriever, 'base_retriever'):
            base = retriever.pytorch_retriever.base_retriever
            logger.info(f"Base retriever initialized: {hasattr(base, 'is_loaded') and base.is_loaded}")
        
        # Carregar índice
        logger.info("Carregando índice...")
        load_success = retriever.load_index()
        logger.info(f"Carregamento: {'✅ SUCESSO' if load_success else '❌ FALHA'}")
        
        if not load_success:
            return False
        
        # Debug: verificar estado após carregamento
        logger.info(f"is_loaded: {retriever.is_loaded}")
        logger.info(f"documents count: {len(retriever.documents)}")
        
        # Testar busca
        logger.info("Testando busca...")
        results = retriever.search("FastAPI", top_k=5, min_score=0.0)
        logger.info(f"Resultados: {len(results)}")
        
        if results:
            for i, result in enumerate(results[:3]):
                logger.info(f"  {i+1}. Score: {result.score:.4f} - {result.content[:100]}...")
            return True
        else:
            logger.error("❌ Nenhum resultado encontrado")
            
            # Debug adicional: testar busca direta no base_retriever
            if hasattr(retriever.pytorch_retriever, 'base_retriever'):
                logger.info("🔍 Testando busca direta no base_retriever...")
                base_results = retriever.pytorch_retriever.base_retriever.search(
                    "FastAPI", top_k=5, min_score=0.0
                )
                logger.info(f"Base retriever resultados: {len(base_results)}")
                
                if base_results:
                    logger.info("✅ Base retriever funciona - problema na delegação")
                else:
                    logger.error("❌ Base retriever também não funciona")
            
            return False
            
    except Exception as e:
        logger.error(f"❌ Erro: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

def main():
    """Função principal."""
    logger.info("🧪 Iniciando debug do OptimizedPyTorchRetriever")
    
    # Teste 1: OptimizedPyTorchRetriever direto
    logger.info("\n" + "="*60)
    direct_success = test_optimized_retriever_direct()
    
    # Teste 2: RAGRetriever com otimizações
    logger.info("\n" + "="*60)
    rag_success = test_rag_retriever_with_optimizations()
    
    # Resumo
    logger.info("\n" + "="*60)
    logger.info("📊 RESUMO DOS TESTES")
    logger.info(f"OptimizedPyTorchRetriever direto: {'✅ SUCESSO' if direct_success else '❌ FALHA'}")
    logger.info(f"RAGRetriever com otimizações: {'✅ SUCESSO' if rag_success else '❌ FALHA'}")
    
    if direct_success and not rag_success:
        logger.warning("⚠️ OptimizedPyTorchRetriever funciona diretamente, mas não através do RAGRetriever")
        logger.warning("⚠️ Problema na integração ou delegação")
    elif not direct_success and not rag_success:
        logger.error("❌ Problema fundamental com OptimizedPyTorchRetriever")
    elif direct_success and rag_success:
        logger.info("✅ Tudo funcionando corretamente")
    else:
        logger.warning("⚠️ Situação inesperada")

if __name__ == "__main__":
    main()