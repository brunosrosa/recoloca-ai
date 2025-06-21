#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar a inicialização do retriever RAG
"""

import sys
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def test_retriever_initialization():
    """Testa a inicialização do retriever passo a passo"""
    try:
        # Adicionar path
        core_logic_path = Path(__file__).parent / 'rag_infra' / 'core_logic'
        sys.path.insert(0, str(core_logic_path))
        logger.info(f"Path adicionado: {core_logic_path}")
        
        # Importar módulos
        logger.info("Importando rag_retriever...")
        from rag_retriever import get_retriever, initialize_retriever
        logger.info("✅ rag_retriever importado com sucesso")
        
        # Obter retriever
        logger.info("Obtendo retriever...")
        retriever = get_retriever()
        logger.info(f"✅ Retriever obtido: {type(retriever)}")
        
        # Testar inicialização
        logger.info("Testando inicialização...")
        result = retriever.initialize()
        logger.info(f"Resultado da inicialização: {result}")
        
        if result:
            logger.info("✅ Inicialização bem-sucedida")
            
            # Testar carregamento do índice
            logger.info("Testando carregamento do índice...")
            load_result = retriever.load_index()
            logger.info(f"Resultado do carregamento: {load_result}")
            
            if load_result:
                logger.info("✅ Índice carregado com sucesso")
                logger.info(f"Documentos carregados: {len(retriever.documents)}")
            else:
                logger.error("❌ Falha ao carregar índice")
        else:
            logger.error("❌ Falha na inicialização")
            
        return result
        
    except Exception as e:
        logger.error(f"Erro durante o teste: {str(e)}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    print("=== Teste de Inicialização do Retriever RAG ===")
    success = test_retriever_initialization()
    print(f"\n=== Resultado Final: {'SUCESSO' if success else 'FALHA'} ===")