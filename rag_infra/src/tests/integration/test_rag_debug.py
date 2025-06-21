#!/usr/bin/env python3
"""
Script de debug para testar o sistema RAG
"""

import sys
sys.path.append('src')

from core.core_logic.rag_retriever import RAGRetriever
import json

def test_rag_system():
    print("=== TESTE DE DEBUG DO SISTEMA RAG ===")
    
    # Inicializar o retriever
    print("\n1. Inicializando RAGRetriever...")
    retriever = RAGRetriever(force_pytorch=True, force_cpu=True)
    print("✅ RAGRetriever inicializado")
    
    # Carregar índice
    print("\n2. Carregando índice...")
    retriever.load_index()
    print("✅ Índice carregado")
    
    # Verificar dados carregados
    print("\n3. Verificando dados carregados...")
    print(f"   Documentos: {len(retriever.documents)}")
    print(f"   Metadados: {len(retriever.metadata)}")
    
    if len(retriever.documents) == 0:
        print("❌ PROBLEMA: Nenhum documento carregado!")
        return
    
    # Testar busca com diferentes min_scores
    print("\n4. Testando buscas...")
    
    queries = ['arquitetura', 'sistema', 'RAG', 'agente']
    min_scores = [0.0, 0.1, 0.3, 0.5]
    
    for query in queries:
        print(f"\n   Query: '{query}'")
        for min_score in min_scores:
            try:
                results = retriever.search(query, top_k=3, min_score=min_score)
                print(f"     Min_score {min_score}: {len(results)} resultados")
                if results:
                    print(f"       Primeiro resultado (score: {results[0].score:.3f}): {results[0].content[:100]}...")
                    break  # Se encontrou resultados, não precisa testar scores maiores
            except Exception as e:
                print(f"     Min_score {min_score}: ERRO - {e}")
    
    print("\n=== TESTE CONCLUÍDO ===")

if __name__ == "__main__":
    test_rag_system()