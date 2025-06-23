#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug específico para testar o fluxo exato do RAGRetriever usado no test_rag_final.py
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "rag_infra"))

print("=== DEBUG RAG RETRIEVER FLOW ===")
print(f"Python path: {sys.path[:3]}")

try:
    # Importar RAGRetriever
    try:
        from rag_infra.core_logic.rag_retriever import RAGRetriever
        print("✅ Importação RAGRetriever via rag_infra.core_logic")
    except ImportError:
        from core_logic.rag_retriever import RAGRetriever
        print("✅ Importação RAGRetriever via core_logic")
    
    print("\n=== TESTE 1: Inicialização ===")
    retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
    print(f"✅ RAGRetriever criado")
    print(f"   - use_pytorch: {getattr(retriever, 'use_pytorch', 'ATRIBUTO NÃO ENCONTRADO')}")
    print(f"   - pytorch_retriever: {getattr(retriever, 'pytorch_retriever', 'ATRIBUTO NÃO ENCONTRADO')}")
    
    print("\n=== TESTE 2: Inicialização ===")
    init_result = retriever.initialize()
    print(f"Resultado da inicialização: {init_result}")
    
    if init_result:
        print(f"   - use_pytorch após init: {getattr(retriever, 'use_pytorch', 'ATRIBUTO NÃO ENCONTRADO')}")
        print(f"   - pytorch_retriever após init: {type(getattr(retriever, 'pytorch_retriever', None))}")
        
        print("\n=== TESTE 3: Carregamento do Índice ===")
        load_result = retriever.load_index()
        print(f"Resultado do carregamento: {load_result}")
        
        if load_result:
            print(f"   - Documentos carregados: {len(getattr(retriever, 'documents', []))}")
            print(f"   - Metadados carregados: {len(getattr(retriever, 'metadata', []))}")
            print(f"   - is_loaded: {getattr(retriever, 'is_loaded', 'ATRIBUTO NÃO ENCONTRADO')}")
            
            # Verificar atributos para determinar backend
            if hasattr(retriever, 'pytorch_retriever') and retriever.pytorch_retriever:
                backend_type = type(retriever.pytorch_retriever).__name__
                print(f"   - Backend detectado: {backend_type}")
            else:
                print(f"   - Backend: FAISS ou não detectado")
                
            print("\n✅ SUCESSO: RAGRetriever funcionando completamente")
        else:
            print("\n❌ FALHA: Carregamento do índice falhou")
            
            # Debug adicional
            print("\n=== DEBUG ADICIONAL ===")
            if hasattr(retriever, 'pytorch_retriever') and retriever.pytorch_retriever:
                print("Testando carregamento direto do pytorch_retriever...")
                direct_load = retriever.pytorch_retriever.load_index()
                print(f"Carregamento direto: {direct_load}")
    else:
        print("\n❌ FALHA: Inicialização falhou")
        
except Exception as e:
    print(f"\n❌ ERRO GERAL: {e}")
    import traceback
    traceback.print_exc()

print("\n=== FIM DO DEBUG ===")