#!/usr/bin/env python3
"""
Script de teste para o sistema de recuperação RAG
"""

import sys
from pathlib import Path

# Adicionar o diretório rag_infra ao path
rag_infra_path = Path(__file__).parent.parent
sys.path.insert(0, str(rag_infra_path))
sys.path.insert(0, str(rag_infra_path / "core_logic"))

try:
    from ..core_logic.rag_retriever import RAGRetriever
    
    print("🔍 Testando sistema de recuperação RAG...")
    
    # Inicializar o retriever
    retriever = RAGRetriever()
    print("✅ RAGRetriever inicializado")
    
    # Inicializar o modelo de embedding
    if retriever.initialize():
        print("✅ Modelo de embedding inicializado")
        
        # Carregar o índice
        if retriever.load_index():
            print("✅ Índice FAISS carregado com sucesso")
            
            # Teste de busca
            query = "Como funciona o sistema de agentes IA?"
            print(f"Testando busca: '{query}'")
            
            results = retriever.search(query, top_k=3)
            
            if results:
                print(f"✅ Busca realizada com sucesso! {len(results)} resultados encontrados")
                for i, result in enumerate(results, 1):
                    if hasattr(result, 'score') and hasattr(result, 'content'):
                        print(f"  {i}. Score: {result.score:.3f} - {result.content[:100]}...")
                    else:
                        print(f"  {i}. {result}")
            else:
                print("❌ Nenhum resultado encontrado")
        else:
            print("❌ Falha ao carregar índice FAISS")
    else:
        print("❌ Falha ao inicializar modelo de embedding")
        
except Exception as e:
    print(f"❌ Erro durante o teste: {e}")
    import traceback
    traceback.print_exc()