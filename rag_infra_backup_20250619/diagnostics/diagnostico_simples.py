#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Diagnóstico Simplificado do Sistema RAG - Recoloca.ai

Autor: @AgenteM_ArquitetoTI
Versão: 1.0
Data: Junho 2025
"""

import sys
import logging
from pathlib import Path
import time
import traceback

# Adicionar o diretório core_logic ao path
sys.path.insert(0, str(Path(__file__).parent / "core_logic"))

# Configurar logging para evitar problemas de encoding
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('diagnostico.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Executa diagnóstico simplificado."""
    print("DIAGNOSTICO COMPLETO DO SISTEMA RAG")
    print("=" * 50)
    
    # Teste 1: Imports
    print("\n=== TESTE DE IMPORTS ===")
    
    try:
        import torch
        print(f"PyTorch: {torch.__version__}")
        print(f"CUDA disponivel: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"GPU: {torch.cuda.get_device_name(0)}")
    except ImportError as e:
        print(f"ERRO PyTorch: {e}")
    
    try:
        import faiss
        print(f"FAISS: OK")
        print(f"FAISS-GPU disponivel: {hasattr(faiss, 'StandardGpuResources')}")
    except ImportError as e:
        print(f"ERRO FAISS: {e}")
    
    # Teste 2: RAGRetriever
    print("\n=== TESTE RAGRETRIEVER ===")
    
    try:
        from rag_retriever import RAGRetriever
        
        retriever = RAGRetriever()
        print(f"Backend selecionado: {'PyTorch' if retriever.use_pytorch else 'FAISS'}")
        
        # Inicialização
        print("Inicializando...")
        success = retriever.initialize()
        print(f"Inicializacao: {'OK' if success else 'FALHA'}")
        
        if success:
            # Carregamento do índice
            print("Carregando indice...")
            load_success = retriever.load_index()
            print(f"Carregamento: {'OK' if load_success else 'FALHA'}")
            
            if load_success:
                print(f"Documentos carregados: {len(retriever.documents)}")
                print(f"Status is_loaded: {retriever.is_loaded}")
                
                # Teste de busca
                print("\nTestando busca...")
                results = retriever.search("Recoloca.ai MVP", top_k=3)
                print(f"Resultados encontrados: {len(results)}")
                
                if results:
                    for i, result in enumerate(results[:2]):
                        print(f"[{i+1}] Score: {result.score:.4f}")
                        print(f"    Conteudo: {result.content[:80]}...")
                        print(f"    Categoria: {result.metadata.get('category', 'N/A')}")
                else:
                    print("PROBLEMA: Nenhum resultado encontrado")
                    
                    # Diagnóstico adicional
                    print("\n=== DIAGNOSTICO ADICIONAL ===")
                    print(f"Tipo do retriever: {type(retriever)}")
                    print(f"Use PyTorch: {retriever.use_pytorch}")
                    
                    if retriever.use_pytorch and retriever.pytorch_retriever:
                        print(f"PyTorch retriever: {type(retriever.pytorch_retriever)}")
                        print(f"PyTorch docs: {len(getattr(retriever.pytorch_retriever, 'documents', []))}")
                    
                    if hasattr(retriever, 'index') and retriever.index:
                        print(f"FAISS index: {retriever.index.ntotal} vetores")
        
    except Exception as e:
        print(f"ERRO no teste: {e}")
        traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("DIAGNOSTICO CONCLUIDO")

if __name__ == "__main__":
    main()