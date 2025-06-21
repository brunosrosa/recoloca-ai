#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste de inicialização do RAG
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório core_logic ao path
project_root = Path(__file__).parent
core_logic_path = project_root / "rag_infra" / "src" / "core" / "core_logic"
sys.path.insert(0, str(core_logic_path))

print(f"Testing RAG initialization...")
print(f"Core logic path: {core_logic_path}")
print(f"Path exists: {core_logic_path.exists()}")

try:
    from rag_retriever import initialize_retriever, get_retriever
    print("✅ Import successful")
    
    print("\n🔄 Testing initialization...")
    success = initialize_retriever()
    print(f"Initialization result: {success}")
    
    if success:
        retriever = get_retriever()
        print(f"✅ Retriever type: {type(retriever)}")
        print(f"Is loaded: {retriever.is_loaded}")
        
        # Testar busca
        if retriever.is_loaded:
            print("\n🔍 Testing search...")
            results = retriever.search("teste", top_k=1)
            print(f"Search results: {len(results) if results else 'None'}")
        else:
            print("❌ Retriever not loaded")
    else:
        print("❌ Initialization failed")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()