#!/usr/bin/env python3
"""
Script para debugar diferenças entre RAGRetriever e PyTorchGPURetriever direto.
"""

import sys
import os
import time
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Adicionar o diretório rag_infra ao path
rag_infra_path = Path(__file__).parent / "rag_infra"
sys.path.insert(0, str(rag_infra_path))

def test_pytorch_direct():
    """Testa PyTorchGPURetriever diretamente."""
    logger.info("=== Testando PyTorchGPURetriever Direto ===")
    
    try:
        from rag_infra.src.core.core_logic.pytorch_gpu_retriever import PyTorchGPURetriever
        
        retriever = PyTorchGPURetriever(force_cpu=False)
        
        if not retriever.initialize():
            logger.error("Falha na inicialização do PyTorchGPURetriever")
            return False
            
        if not retriever.load_index():
            logger.error("Falha no carregamento do índice PyTorchGPURetriever")
            return False
            
        logger.info(f"PyTorchGPURetriever inicializado: {len(retriever.documents)} documentos")
        
        # Teste de busca
        query = "FastAPI"
        logger.info(f"Buscando por: '{query}'")
        
        start_time = time.time()
        results = retriever.search(query, top_k=3, min_score=0.0)
        end_time = time.time()
        
        logger.info(f"PyTorchGPURetriever - Resultados: {len(results)} em {end_time - start_time:.3f}s")
        
        for i, result in enumerate(results[:2]):
            logger.info(f"  Resultado {i+1}: Score {result.score:.4f}")
            logger.info(f"    Conteúdo: {result.content[:100]}...")
            
        return len(results) > 0
        
    except Exception as e:
        logger.error(f"Erro no teste PyTorchGPURetriever: {e}")
        return False

def test_rag_retriever():
    """Testa RAGRetriever."""
    logger.info("=== Testando RAGRetriever ===")
    
    try:
        from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
        
        retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
        
        if not retriever.initialize():
            logger.error("Falha na inicialização do RAGRetriever")
            return False
            
        if not retriever.load_index():
            logger.error("Falha no carregamento do índice RAGRetriever")
            return False
            
        logger.info(f"RAGRetriever inicializado: {len(retriever.documents)} documentos")
        logger.info(f"Backend usado: {type(retriever.pytorch_retriever).__name__ if hasattr(retriever, 'pytorch_retriever') else 'Desconhecido'}")
        
        # Teste de busca
        query = "FastAPI"
        logger.info(f"Buscando por: '{query}'")
        
        start_time = time.time()
        results = retriever.search(query, top_k=3, min_score=0.0)
        end_time = time.time()
        
        logger.info(f"RAGRetriever - Resultados: {len(results)} em {end_time - start_time:.3f}s")
        
        for i, result in enumerate(results[:2]):
            logger.info(f"  Resultado {i+1}: Score {result.score:.4f}")
            logger.info(f"    Conteúdo: {result.content[:100]}...")
            
        return len(results) > 0
        
    except Exception as e:
        logger.error(f"Erro no teste RAGRetriever: {e}")
        return False

def main():
    """Função principal."""
    logger.info("🧪 Iniciando comparação RAGRetriever vs PyTorchGPURetriever")
    
    query = "FastAPI"
    pytorch_success = False
    rag_success = False
    
    try:
        from rag_infra.src.core.core_logic.pytorch_gpu_retriever import PyTorchGPURetriever
        
        # Teste com PyTorchGPURetriever direto
        logger.info("[SEARCH] Testando PyTorchGPURetriever direto...")
        pytorch_retriever = PyTorchGPURetriever(force_cpu=False)
        
        if pytorch_retriever.initialize() and pytorch_retriever.load_index():
            results_pytorch = pytorch_retriever.search(query, top_k=5, min_score=0.0)
            logger.info(f"PyTorchGPURetriever - Resultados: {len(results_pytorch)}")
            
            if results_pytorch:
                logger.info("[OK] PyTorchGPURetriever funcionando")
                for i, result in enumerate(results_pytorch[:3]):
                    logger.info(f"  {i+1}. Score: {result.score:.4f} - {result.content[:100]}...")
                pytorch_success = True
            else:
                logger.error("[ERROR] PyTorchGPURetriever não retornou resultados")
        else:
            logger.error("[ERROR] Falha ao inicializar PyTorchGPURetriever")
    except Exception as e:
        logger.error(f"[ERROR] Erro com PyTorchGPURetriever: {e}")
    
    print("\n" + "="*60 + "\n")
    
    try:
        from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
        
        # Teste com RAGRetriever
        logger.info("[SEARCH] Testando RAGRetriever...")
        rag_retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
        
        if rag_retriever.initialize() and rag_retriever.load_index():
            results_rag = rag_retriever.search(query, top_k=5, min_score=0.0)
            logger.info(f"RAGRetriever - Resultados: {len(results_rag)}")
            
            if results_rag:
                logger.info("[OK] RAGRetriever funcionando")
                for i, result in enumerate(results_rag[:3]):
                    logger.info(f"  {i+1}. Score: {result.score:.4f} - {result.content[:100]}...")
                rag_success = True
            else:
                logger.error("[ERROR] RAGRetriever não retornou resultados")
        else:
            logger.error("[ERROR] Falha ao inicializar RAGRetriever")
    except Exception as e:
        logger.error(f"[ERROR] Erro com RAGRetriever: {e}")
    
    print("\n" + "="*60 + "\n")
    
    # Teste adicional: verificar se o problema é com OptimizedPyTorchRetriever
    logger.info("[SEARCH] Testando se o problema é com OptimizedPyTorchRetriever...")
    try:
        from rag_infra.src.core.core_logic.pytorch_optimizations import OptimizedPyTorchRetriever
        opt_retriever = OptimizedPyTorchRetriever(force_cpu=False)
        
        if opt_retriever.initialize() and opt_retriever.load_index():
            # OptimizedPyTorchRetriever não aceita min_score
            results_opt = opt_retriever.search(query, top_k=5)
            logger.info(f"OptimizedPyTorchRetriever - Resultados: {len(results_opt)}")
            
            if results_opt:
                logger.info("[OK] OptimizedPyTorchRetriever funcionando")
                for i, result in enumerate(results_opt[:3]):
                    logger.info(f"  {i+1}. Score: {result.score:.4f} - {result.content[:100]}...")
            else:
                logger.error("[ERROR] OptimizedPyTorchRetriever não retornou resultados")
        else:
            logger.error("[ERROR] Falha ao inicializar OptimizedPyTorchRetriever")
    except Exception as e:
        logger.error(f"[ERROR] Erro com OptimizedPyTorchRetriever: {e}")
    
    print("\n" + "="*60)
    logger.info("[EMOJI] RESUMO DOS TESTES")
    logger.info(f"PyTorchGPURetriever direto: {'[OK] SUCESSO' if pytorch_success else '[ERROR] FALHA'}")
    logger.info(f"RAGRetriever: {'[OK] SUCESSO' if rag_success else '[ERROR] FALHA'}")
    
    if pytorch_success and not rag_success:
        logger.warning("[WARNING] PyTorchGPURetriever funciona, mas RAGRetriever não - possível problema na delegação")
    elif not pytorch_success and not rag_success:
        logger.error("[ERROR] Ambos falharam - problema no índice ou configuração")
    elif pytorch_success and rag_success:
        logger.info("[OK] Ambos funcionam corretamente")
    else:
        logger.warning("[WARNING] Situação inesperada")

if __name__ == "__main__":
    main()