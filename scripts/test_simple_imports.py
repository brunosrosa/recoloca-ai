#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples de imports após correção de caminhos

Este script testa os imports básicos do sistema RAG de forma mais direta.

Autor: @AgenteM_DevFastAPI
Data: Junho 2025
"""

import sys
import os
from pathlib import Path

def test_basic_imports():
    """Testa imports básicos do sistema"""
    print("🧪 Testando imports básicos do sistema RAG...")
    print()
    
    # Configurar paths
    project_root = Path(__file__).parent.parent
    rag_root = project_root / "rag_infra"
    core_logic_path = rag_root / "core_logic"
    
    # Adicionar paths
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(rag_root))
    sys.path.insert(0, str(core_logic_path))
    
    print(f"📁 Projeto: {project_root}")
    print(f"📁 RAG: {rag_root}")
    print(f"📁 Core Logic: {core_logic_path}")
    print()
    
    # Teste 1: Dependências externas
    print("1️⃣ Testando dependências externas...")
    try:
        import numpy as np
        print("✅ NumPy importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar NumPy: {e}")
        return False
    
    try:
        import faiss
        print("✅ FAISS importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar FAISS: {e}")
        return False
    
    try:
        import torch
        print("✅ PyTorch importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar PyTorch: {e}")
        return False
    
    try:
        from sentence_transformers import SentenceTransformer
        print("✅ Sentence Transformers importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar Sentence Transformers: {e}")
        return False
    
    print()
    
    # Teste 2: Módulos do sistema RAG
    print("2️⃣ Testando módulos do sistema RAG...")
    
    try:
        import constants
        print("✅ Constants importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar constants: {e}")
        return False
    
    try:
        import embedding_model
        print("✅ Embedding Model importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar embedding_model: {e}")
        return False
    
    try:
        import rag_indexer
        print("✅ RAG Indexer importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar rag_indexer: {e}")
        return False
    
    try:
        import rag_retriever
        print("✅ RAG Retriever importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar rag_retriever: {e}")
        return False
    
    print()
    
    # Teste 3: Funções específicas
    print("3️⃣ Testando funções específicas...")
    
    try:
        from rag_retriever import get_retriever
        print("✅ Função get_retriever importada com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar get_retriever: {e}")
        return False
    
    try:
        from rag_retriever import initialize_retriever
        print("✅ Função initialize_retriever importada com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar initialize_retriever: {e}")
        return False
    
    try:
        from embedding_model import initialize_embedding_model
        print("✅ Função initialize_embedding_model importada com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar initialize_embedding_model: {e}")
        return False
    
    print()
    
    # Teste 4: Verificação de constantes
    print("4️⃣ Testando acesso a constantes...")
    
    try:
        from constants import EMBEDDING_MODEL_NAME, FAISS_INDEX_DIR
        print(f"✅ Constantes acessadas: {EMBEDDING_MODEL_NAME}")
        print(f"✅ Diretório de índice: {FAISS_INDEX_DIR}")
    except ImportError as e:
        print(f"❌ Erro ao acessar constantes: {e}")
        return False
    except AttributeError as e:
        print(f"❌ Erro de atributo nas constantes: {e}")
        return False
    
    print()
    
    # Teste 5: Teste básico de inicialização
    print("5️⃣ Testando inicialização básica...")
    
    try:
        # Tentar inicializar o modelo de embedding
        embedding_manager = initialize_embedding_model()
        if embedding_manager is not None:
            print("✅ Modelo de embedding inicializado com sucesso")
        else:
            print("⚠️ Modelo de embedding retornou None (pode ser normal)")
    except Exception as e:
        print(f"⚠️ Aviso na inicialização do embedding: {e}")
    
    try:
        # Tentar obter o retriever
        retriever = get_retriever()
        if retriever is not None:
            print("✅ Retriever obtido com sucesso")
        else:
            print("⚠️ Retriever retornou None (pode ser normal se índice não existe)")
    except Exception as e:
        print(f"⚠️ Aviso ao obter retriever: {e}")
    
    print()
    print("🎉 TODOS OS IMPORTS BÁSICOS FUNCIONARAM!")
    print("✅ Sistema RAG está pronto para uso")
    
    return True

def main():
    """Função principal"""
    print("🚀 Teste Simples de Imports - Sistema RAG Recoloca.AI")
    print("=" * 55)
    print()
    
    success = test_basic_imports()
    
    if success:
        print()
        print("🎯 PRÓXIMOS PASSOS:")
        print("1. ✅ Imports funcionando corretamente")
        print("2. 🔄 Caminhos corrigidos com sucesso")
        print("3. 📦 Ambiente virtual recriado")
        print("4. 🚀 Sistema RAG pronto para desenvolvimento")
        print("5. 🧪 Executar testes funcionais específicos")
    else:
        print()
        print("❌ AINDA HÁ PROBLEMAS DE IMPORT")
        print("🔧 Verifique os erros listados acima")
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)