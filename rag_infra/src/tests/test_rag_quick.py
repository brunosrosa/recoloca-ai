#!/usr/bin/env python3
"""
Teste de diagnóstico do sistema RAG
"""

import sys
import os
sys.path.append('.')

from rag_infra.src.core.rag_retriever import RAGRetriever

def test_rag_complete():
    print("=== TESTE COMPLETO RAG SYSTEM ===")
    
    # Inicializar RAGRetriever
    print("Inicializando RAGRetriever...")
    retriever = RAGRetriever()
    
    print(f"Backend selecionado: {'PyTorch' if retriever.use_pytorch else 'FAISS'}")
    
    # Carregar índice
    try:
        print("Carregando indice...")
        success = retriever.load_index()
        print(f"Carregamento bem-sucedido: {success}")
        
        if success:
            print(f"Status carregado: {retriever.is_loaded}")
            print(f"Numero de documentos: {len(retriever.documents) if hasattr(retriever, 'documents') else 'N/A'}")
            
            # Teste de busca com diferentes queries
            test_queries = [
                "Recoloca.ai",
                "MVP",
                "projeto",
                "arquitetura",
                "agentes IA",
                "desenvolvimento"
            ]
            
            print("/n=== TESTES DE BUSCA ===")
            for query in test_queries:
                print(f"/nBuscando: '{query}'")
                try:
                    results = retriever.search(query, top_k=3, min_score=0.0)
                    print(f"  Resultados: {len(results)}")
                    
                    if results:
                        for i, result in enumerate(results[:2], 1):
                            if isinstance(result, dict):
                                content = result.get('content', '')[:80]
                                score = result.get('score', 0)
                                source = result.get('metadata', {}).get('source', 'Unknown')
                            else:
                                content = str(result)[:80]
                                score = getattr(result, 'score', 0)
                                source = getattr(result, 'metadata', {}).get('source', 'Unknown')
                            
                            print(f"    {i}. Score: {score:.3f} | Source: {source}")
                            print(f"       Content: {content}...")
                    else:
                        print("    Nenhum resultado encontrado")
                        
                except Exception as e:
                    print(f"    ERRO na busca: {e}")
            
            print("/n=== TESTE DE PERFORMANCE ===")
            import time
            start_time = time.time()
            results = retriever.search("Recoloca.ai MVP desenvolvimento", top_k=5)
            end_time = time.time()
            print(f"Tempo de busca: {(end_time - start_time)*1000:.2f}ms")
            print(f"Resultados retornados: {len(results)}")
            
        else:
            print("ERRO: Falha ao carregar o indice")
            
    except Exception as e:
        print(f"ERRO GERAL: {e}")
        import traceback
        traceback.print_exc()
    
    print("/n=== RESUMO DO TESTE ===")
    print(f"Sistema RAG: {'FUNCIONANDO' if success and retriever.is_loaded else 'COM PROBLEMAS'}")
    print(f"Backend: {'PyTorch' if retriever.use_pytorch else 'FAISS'}")
    print(f"Documentos indexados: {len(retriever.documents) if hasattr(retriever, 'documents') and retriever.documents else 0}")

if __name__ == "__main__":
    test_rag_complete()