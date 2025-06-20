#!/usr/bin/env python3
"""
Teste básico de imports do sistema RAG
"""

import sys
from pathlib import Path

# Adicionar core_logic ao path
sys.path.insert(0, str(Path(__file__).parent / "rag_infra" / "core_logic"))

print("🔍 Testando imports básicos do sistema RAG...")

try:
    from constants import *
    print("✅ Constants importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar constants: {e}")
    sys.exit(1)

try:
    from embedding_model import EmbeddingModel
    print("✅ EmbeddingModel importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar embedding_model: {e}")

try:
    from rag_retriever import RAGRetriever
    print("✅ RAGRetriever importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar rag_retriever: {e}")

try:
    from rag_indexer import RAGIndexer
    print("✅ RAGIndexer importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar rag_indexer: {e}")

print("\n🎯 Teste de imports básicos concluído!")