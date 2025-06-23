#!/usr/bin/env python3
"""
Script de debug para testar o sistema RAG
"""

import sys
<<<<<<< HEAD
sys.path.append('src')
=======
import os

# Adiciona o diretório 'rag_infra' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
>>>>>>> 1d8d89e (Messy. Needs to Refactore.)

from core.core_logic.rag_retriever import RAGRetriever
import json

def test_rag_system():
    print("=== TESTE DE DEBUG DO SISTEMA RAG ===")
    
    # Inicializar o retriever
    print("\n1. Inicializando RAGRetriever...")
    retriever = RAGRetriever(force_pytorch=True, force_cpu=True)
<<<<<<< HEAD
    print("✅ RAGRetriever inicializado")
=======
    print("[OK] RAGRetriever inicializado")
>>>>>>> 1d8d89e (Messy. Needs to Refactore.)
    
    # Carregar índice
    print("\n2. Carregando índice...")
    retriever.load_index()
<<<<<<< HEAD
    print("✅ Índice carregado")
=======
    print("[OK] Índice carregado")
>>>>>>> 1d8d89e (Messy. Needs to Refactore.)
    
    # Verificar dados carregados
    print("\n3. Verificando dados carregados...")
    print(f"   Documentos: {len(retriever.documents)}")
    print(f"   Metadados: {len(retriever.metadata)}")
    
    if len(retriever.documents) == 0:
<<<<<<< HEAD
        print("❌ PROBLEMA: Nenhum documento carregado!")
=======
        print("[ERROR] PROBLEMA: Nenhum documento carregado!")
>>>>>>> 1d8d89e (Messy. Needs to Refactore.)
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