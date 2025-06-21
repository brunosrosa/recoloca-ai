# -*- coding: utf-8 -*-
"""
RAG Infrastructure Package

Pacote principal da infraestrutura RAG do Recoloca.ai

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

__version__ = "1.0.0"
__author__ = "@AgenteM_DevFastAPI"

# Importações principais
try:
    from .core_logic.rag_indexer import RAGIndexer
    from .core_logic.rag_retriever import RAGRetriever
    
    __all__ = [
        "RAGIndexer",
        "RAGRetriever"
    ]
except ImportError as e:
    # Fallback para desenvolvimento
    print(f"Warning: Could not import RAG components: {e}")
    __all__ = []