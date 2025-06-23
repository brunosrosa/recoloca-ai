#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug específico para o problema de carregamento do índice no RAGRetriever
"""

import sys
import os
import logging
from pathlib import Path

# Configurar logging para capturar todos os detalhes
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Adicionar o diretório raiz ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "rag_infra"))

print("=== DEBUG CARREGAMENTO DO ÍNDICE ===")

try:
    # Importar RAGRetriever
    try:
        from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
        print("[OK] Importação RAGRetriever via rag_infra.core_logic")
    except ImportError:
        from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
        print("[OK] Importação RAGRetriever via core_logic")
    
    print("\n=== CRIANDO RETRIEVER ===")
    retriever = RAGRetriever(force_pytorch=True, use_optimizations=True)
    print(f"[OK] RAGRetriever criado")
    
    print("\n=== INICIALIZANDO ===")
    init_result = retriever.initialize()
    print(f"Resultado da inicialização: {init_result}")
    
    if not init_result:
        print("[ERROR] Falha na inicialização - parando aqui")
        sys.exit(1)
    
    print("\n=== TENTANDO CARREGAR ÍNDICE ===")
    print("Chamando retriever.load_index()...")
    
    # Capturar todos os logs durante o carregamento
    load_result = retriever.load_index()
    
    print(f"\nResultado do carregamento: {load_result}")
    
    if load_result:
        print("[OK] SUCESSO no carregamento!")
        print(f"   - Documentos: {len(getattr(retriever, 'documents', []))}")
        print(f"   - is_loaded: {getattr(retriever, 'is_loaded', False)}")
    else:
        print("[ERROR] FALHA no carregamento")
        
        # Tentar carregamento direto do pytorch_retriever
        print("\n=== TESTE DIRETO DO PYTORCH_RETRIEVER ===")
        if hasattr(retriever, 'pytorch_retriever') and retriever.pytorch_retriever:
            print("Tentando carregamento direto...")
            direct_result = retriever.pytorch_retriever.load_index()
            print(f"Carregamento direto: {direct_result}")
            
            if direct_result:
                print("[OK] Carregamento direto funcionou!")
                print(f"   - Documentos no pytorch_retriever: {len(getattr(retriever.pytorch_retriever, 'documents', []))}")
            else:
                print("[ERROR] Carregamento direto também falhou")
        else:
            print("[ERROR] pytorch_retriever não está disponível")
        
except Exception as e:
    print(f"\n[ERROR] ERRO GERAL: {e}")
    import traceback
    traceback.print_exc()

print("\n=== FIM DO DEBUG ===")