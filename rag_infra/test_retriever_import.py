#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para diagnosticar problemas de importação do retriever
"""

import sys
import os
from pathlib import Path

# Adicionar caminhos necessários
project_root = Path(__file__).parent
core_logic_path = project_root / "src" / "core" / "core_logic"

print(f"Project root: {project_root}")
print(f"Core logic path: {core_logic_path}")
print(f"Core logic exists: {core_logic_path.exists()}")

# Adicionar ao sys.path
sys.path.insert(0, str(core_logic_path))

print("\nSys.path:")
for i, path in enumerate(sys.path[:10]):
    print(f"  {i}: {path}")

try:
    print("\n🧪 Testando importação do rag_retriever...")
    import rag_retriever
    print("✅ rag_retriever importado com sucesso")
    
    print("\n🧪 Testando importação de get_retriever...")
    from rag_retriever import get_retriever
    print("✅ get_retriever importado com sucesso")
    
    print("\n🧪 Testando importação de initialize_retriever...")
    from rag_retriever import initialize_retriever
    print("✅ initialize_retriever importado com sucesso")
    
    print("\n🧪 Testando criação do retriever...")
    retriever = get_retriever(force_cpu=True)
    print(f"✅ Retriever criado: {retriever is not None}")
    print(f"   Tipo: {type(retriever)}")
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print(f"   Arquivos no diretório core_logic:")
    if core_logic_path.exists():
        for file in core_logic_path.iterdir():
            print(f"     - {file.name}")
except Exception as e:
    print(f"❌ Erro geral: {e}")
    import traceback
    traceback.print_exc()

print("\n🏁 Teste concluído")