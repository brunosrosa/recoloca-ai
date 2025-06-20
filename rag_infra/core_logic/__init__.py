# -*- coding: utf-8 -*-
"""
RAG Core Logic Package

Módulos principais da lógica do sistema RAG

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

# Importações dos módulos principais
try:
    from .rag_indexer import RAGIndexer
except ImportError:
    try:
        from rag_indexer import RAGIndexer
    except ImportError:
        RAGIndexer = None

try:
    from .rag_retriever import RAGRetriever, get_retriever, initialize_retriever
except ImportError:
    try:
        from rag_retriever import RAGRetriever, get_retriever, initialize_retriever
    except ImportError:
        RAGRetriever = None
        get_retriever = None
        initialize_retriever = None

try:
    from .embedding_model import initialize_embedding_model, get_embedding_manager
except ImportError:
    try:
        from embedding_model import initialize_embedding_model, get_embedding_manager
    except ImportError:
        initialize_embedding_model = None
        get_embedding_manager = None

__all__ = [
    "RAGIndexer",
    "RAGRetriever",
    "get_retriever",
    "initialize_retriever",
    "initialize_embedding_model",
    "get_embedding_manager"
]