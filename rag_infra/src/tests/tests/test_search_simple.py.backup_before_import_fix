# -*- coding: utf-8 -*-
"""
Teste simples de busca com threshold 0.0
"""

import os
import sys
from pathlib import Path

# Adicionar o diretório rag_infra ao path
project_root = Path(__file__).parent
rag_infra_path = project_root / "rag_infra"
sys.path.insert(0, str(rag_infra_path))

try:
    from core_logic.rag_retriever import RAGRetriever
except ImportError as e:
    print(f"Erro ao importar módulos RAG: {e}")
    sys.exit(1)

def test_search_with_zero_threshold():
    """
    Testa busca com threshold 0.0
    """
    print("=== Teste de Busca com Threshold 0.0 ===")
    
    # Inicializar retriever
    retriever = RAGRetriever()
    
    try:
        retriever.initialize()
        print("✅ RAGRetriever inicializado")
    except Exception as e:
        print(f"❌ Erro na inicialização: {e}")
        return
    
    try:
        retriever.load_index()
        print(f"✅ Índice carregado: {len(retriever.documents)} documentos")
    except Exception as e:
        print(f"❌ Erro ao carregar índice: {e}")
        return
    
    # Testar busca com threshold 0.0
    query = "FastAPI"
    print(f"\nTestando busca: '{query}' com min_score=0.0")
    
    try:
        results = retriever.search(query, top_k=5, min_score=0.0)
        print(f"Resultados encontrados: {len(results)}")
        
        if results:
            for i, result in enumerate(results):
                print(f"\nResultado {i+1}:")
                print(f"  Score: {result.score:.4f}")
                print(f"  Conteúdo: {result.content[:100]}...")
                print(f"  Metadata: {result.metadata}")
        else:
            print("❌ Nenhum resultado encontrado mesmo com threshold 0.0")
            
    except Exception as e:
        print(f"❌ Erro na busca: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_search_with_zero_threshold()