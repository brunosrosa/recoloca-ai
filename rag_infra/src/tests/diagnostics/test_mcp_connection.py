#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste de Diagnóstico do Servidor MCP

Este script testa a conectividade e funcionalidade básica do servidor MCP
para identificar problemas de conexão.

Autor: @AgenteM_ArquitetoTI
Data: Junho 2025
"""

import sys
import json
import asyncio
from pathlib import Path

# Adicionar paths necessários
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src" / "core" / "core_logic"))

def test_imports():
    """Testa se todos os módulos necessários podem ser importados."""
    print("=== TESTE DE IMPORTAÇÕES ===")
    
    try:
        from mcp.server import Server
        print("[OK] MCP Server importado com sucesso")
    except ImportError as e:
        print(f"[ERROR] Erro ao importar MCP Server: {e}")
        return False
    
    try:
        from rag_indexer import RAGIndexer
        print("[OK] RAGIndexer importado com sucesso")
    except ImportError as e:
        print(f"[ERROR] Erro ao importar RAGIndexer: {e}")
        return False
    
    try:
        from rag_retriever import RAGRetriever, initialize_retriever
        print("[OK] RAGRetriever importado com sucesso")
    except ImportError as e:
        print(f"[ERROR] Erro ao importar RAGRetriever: {e}")
        return False
    
    try:
        from constants import (
            MCP_SERVER_NAME,
            MCP_SERVER_VERSION,
            SOURCE_DOCUMENTS_DIR,
            FAISS_INDEX_DIR
        )
        print("[OK] Constantes importadas com sucesso")
        print(f"   - Servidor: {MCP_SERVER_NAME} v{MCP_SERVER_VERSION}")
        print(f"   - Documentos: {SOURCE_DOCUMENTS_DIR}")
        print(f"   - Índice FAISS: {FAISS_INDEX_DIR}")
    except ImportError as e:
        print(f"[ERROR] Erro ao importar constantes: {e}")
        return False
    
    return True

def test_paths():
    """Testa se os caminhos necessários existem."""
    print("\n=== TESTE DE CAMINHOS ===")
    
    from constants import SOURCE_DOCUMENTS_DIR, FAISS_INDEX_DIR, LOGS_DIR
    
    paths_to_check = [
        ("Documentos", SOURCE_DOCUMENTS_DIR),
        ("Índice FAISS", FAISS_INDEX_DIR),
        ("Logs", LOGS_DIR)
    ]
    
    all_good = True
    for name, path in paths_to_check:
        if path.exists():
            print(f"[OK] {name}: {path}")
        else:
            print(f"[ERROR] {name} não encontrado: {path}")
            all_good = False
    
    return all_good

def test_mcp_server_creation():
    """Testa se o servidor MCP pode ser criado."""
    print("\n=== TESTE DE CRIAÇÃO DO SERVIDOR MCP ===")
    
    try:
        from mcp.server import Server
        from constants import MCP_SERVER_NAME
        
        server = Server(MCP_SERVER_NAME)
        print(f"[OK] Servidor MCP '{MCP_SERVER_NAME}' criado com sucesso")
        return True
    except Exception as e:
        print(f"[ERROR] Erro ao criar servidor MCP: {e}")
        return False

def test_rag_initialization():
    """Testa se o sistema RAG pode ser inicializado."""
    print("\n=== TESTE DE INICIALIZAÇÃO RAG ===")
    
    try:
        from rag_retriever import initialize_retriever
        from constants import FAISS_INDEX_DIR
        
        if not FAISS_INDEX_DIR.exists():
            print(f"[WARNING]  Índice FAISS não encontrado em: {FAISS_INDEX_DIR}")
            print("   Execute a indexação primeiro com: python rag_infra/setup/setup_rag.py")
            return False
        
        # Tentar inicializar o retriever
        retriever = initialize_retriever(force_cpu=True)  # Usar CPU para teste
        if retriever:
            print("[OK] Sistema RAG inicializado com sucesso (CPU)")
            return True
        else:
            print("[ERROR] Falha ao inicializar sistema RAG")
            return False
            
    except Exception as e:
        print(f"[ERROR] Erro ao inicializar RAG: {e}")
        return False

def main():
    """Executa todos os testes de diagnóstico."""
    print("[SEARCH] DIAGNÓSTICO DO SERVIDOR MCP - RECOLOCA.AI")
    print("=" * 50)
    
    tests = [
        ("Importações", test_imports),
        ("Caminhos", test_paths),
        ("Servidor MCP", test_mcp_server_creation),
        ("Inicialização RAG", test_rag_initialization)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"[ERROR] Erro inesperado no teste '{test_name}': {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("[EMOJI] RESUMO DOS TESTES")
    print("=" * 50)
    
    all_passed = True
    for test_name, passed in results:
        status = "[OK] PASSOU" if passed else "[ERROR] FALHOU"
        print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n[EMOJI] Todos os testes passaram! O servidor MCP deve funcionar corretamente.")
        print("\n[EMOJI] Se ainda houver problemas de conexão no TRAE IDE:")
        print("   1. Verifique se o TRAE IDE está usando a configuração correta")
        print("   2. Reinicie o TRAE IDE")
        print("   3. Verifique os logs do TRAE IDE para erros específicos")
    else:
        print("\n[WARNING]  Alguns testes falharam. Corrija os problemas antes de usar o MCP.")
        print("\n[EMOJI] Ações recomendadas:")
        print("   1. Execute: python rag_infra/setup/setup_rag.py (se RAG falhou)")
        print("   2. Verifique se todas as dependências estão instaladas")
        print("   3. Verifique se os caminhos estão corretos")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)