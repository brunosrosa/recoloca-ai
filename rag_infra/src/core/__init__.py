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
    from .rag_indexer import RAGIndexer
    from .rag_retriever import RAGRetriever
    from . import setup_rag

    __all__ = [
        "RAGIndexer",
        "RAGRetriever",
        "setup_rag"
    ]
except ImportError as e:
    # Fallback para desenvolvimento
    print(f"Warning: Could not import RAG components: {e}")
    __all__ = []