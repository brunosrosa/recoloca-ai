#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Diagnóstico do Sistema RAG - Recoloca.ai

Este script realiza um diagnóstico completo do sistema RAG para identificar
problemas específicos com o RAGRetriever local.

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

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_imports():
    """Testa se todos os imports necessários estão funcionando."""
    print("\n=== TESTE DE IMPORTS ===")
    
    try:
        import torch
        print(f"✅ PyTorch: {torch.__version__}")
        print(f"   CUDA disponível: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"   GPU: {torch.cuda.get_device_name(0)}")
    except ImportError as e:
        print(f"❌ PyTorch: {e}")
    
    try:
        import faiss
        print(f"✅ FAISS: {faiss.__version__ if hasattr(faiss, '__version__') else 'versão desconhecida'}")
        print(f"   FAISS-GPU disponível: {hasattr(faiss, 'StandardGpuResources')}")
    except ImportError as e:
        print(f"❌ FAISS: {e}")
    
    try:
        from sentence_transformers import SentenceTransformer
        print("✅ SentenceTransformers: disponível")
    except ImportError as e:
        print(f"❌ SentenceTransformers: {e}")
    
    try:
        import constants
        print("✅ Constants: carregado")
    except ImportError as e:
        print(f"❌ Constants: {e}")

def test_gpu_compatibility():
    """Testa a compatibilidade da GPU."""
    print("\n=== TESTE DE COMPATIBILIDADE GPU ===")
    
    try:
        from rag_retriever import _detect_gpu_compatibility
        is_compatible = _detect_gpu_compatibility()
        print(f"GPU compatível com FAISS: {is_compatible}")
        
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            print(f"Nome da GPU: {gpu_name}")
            
            # Verificar GPUs incompatíveis conhecidas
            incompatible_gpus = ['rtx 2060', 'gtx 1660', 'gtx 1650']
            for incompatible in incompatible_gpus:
                if incompatible in gpu_name.lower():
                    print(f"⚠️  GPU {gpu_name} tem problemas conhecidos com FAISS-GPU")
                    break
        
    except Exception as e:
        print(f"❌ Erro no teste de GPU: {e}")
        traceback.print_exc()

def test_backend_selection():
    """Testa qual backend está sendo selecionado."""
    print("\n=== TESTE DE SELEÇÃO DE BACKEND ===")
    
    try:
        from rag_retriever import RAGRetriever
        
        # Teste com configurações padrão
        retriever = RAGRetriever()
        print(f"Backend selecionado (padrão): {'PyTorch' if retriever.use_pytorch else 'FAISS'}")
        
        # Teste forçando PyTorch
        retriever_pytorch = RAGRetriever(force_pytorch=True)
        print(f"Backend selecionado (force_pytorch=True): {'PyTorch' if retriever_pytorch.use_pytorch else 'FAISS'}")
        
        # Teste forçando CPU
        retriever_cpu = RAGRetriever(force_cpu=True)
        print(f"Backend selecionado (force_cpu=True): {'PyTorch' if retriever_cpu.use_pytorch else 'FAISS'}")
        
    except Exception as e:
        print(f"❌ Erro no teste de backend: {e}")
        traceback.print_exc()

def test_initialization():
    """Testa a inicialização do RAGRetriever."""
    print("\n=== TESTE DE INICIALIZAÇÃO ===")
    
    try:
        from rag_retriever import RAGRetriever
        
        retriever = RAGRetriever()
        print(f"RAGRetriever criado: {type(retriever)}")
        print(f"Backend: {'PyTorch' if retriever.use_pytorch else 'FAISS'}")
        
        # Teste de inicialização
        print("Inicializando...")
        success = retriever.initialize()
        print(f"Inicialização: {'✅ Sucesso' if success else '❌ Falha'}")
        
        if success:
            # Teste de carregamento do índice
            print("Carregando índice...")
            load_success = retriever.load_index()
            print(f"Carregamento do índice: {'✅ Sucesso' if load_success else '❌ Falha'}")
            
            if load_success:
                print(f"Documentos carregados: {len(retriever.documents)}")
                print(f"Metadados carregados: {len(retriever.metadata)}")
                print(f"Status is_loaded: {retriever.is_loaded}")
        
    except Exception as e:
        print(f"❌ Erro na inicialização: {e}")
        traceback.print_exc()

def test_index_files():
    """Testa a existência dos arquivos de índice."""
    print("\n=== TESTE DE ARQUIVOS DE ÍNDICE ===")
    
    try:
        from constants import FAISS_INDEX_DIR, PYTORCH_INDEX_DIR
        
        # Verificar arquivos FAISS
        print("Arquivos FAISS:")
        faiss_files = [
            "faiss_index.bin",
            "documents.pkl",
            "metadata.pkl"
        ]
        
        for file in faiss_files:
            file_path = FAISS_INDEX_DIR / file
            exists = file_path.exists()
            size = file_path.stat().st_size if exists else 0
            print(f"  {file}: {'✅' if exists else '❌'} ({size} bytes)")
        
        # Verificar arquivos PyTorch
        print("\nArquivos PyTorch:")
        pytorch_files = [
            "pytorch_index.pt",
            "documents.pkl",
            "metadata.pkl"
        ]
        
        for file in pytorch_files:
            file_path = PYTORCH_INDEX_DIR / file
            exists = file_path.exists()
            size = file_path.stat().st_size if exists else 0
            print(f"  {file}: {'✅' if exists else '❌'} ({size} bytes)")
        
    except Exception as e:
        print(f"❌ Erro na verificação de arquivos: {e}")
        traceback.print_exc()

def test_search_functionality():
    """Testa a funcionalidade de busca."""
    print("\n=== TESTE DE FUNCIONALIDADE DE BUSCA ===")
    
    try:
        from rag_retriever import RAGRetriever
        
        retriever = RAGRetriever()
        
        if not retriever.initialize():
            print("❌ Falha na inicialização - pulando teste de busca")
            return
        
        if not retriever.load_index():
            print("❌ Falha no carregamento do índice - pulando teste de busca")
            return
        
        # Teste de busca simples
        test_queries = [
            "Recoloca.ai MVP",
            "arquitetura sistema",
            "desenvolvimento",
            "API"
        ]
        
        for query in test_queries:
            print(f"\nTestando busca: '{query}'")
            start_time = time.time()
            
            results = retriever.search(query, top_k=3)
            
            elapsed = time.time() - start_time
            print(f"  Resultados: {len(results)} em {elapsed:.3f}s")
            
            for i, result in enumerate(results[:2]):
                print(f"  [{i+1}] Score: {result.score:.4f}")
                print(f"      Conteúdo: {result.content[:100]}...")
                print(f"      Categoria: {result.metadata.get('category', 'N/A')}")
        
    except Exception as e:
        print(f"❌ Erro no teste de busca: {e}")
        traceback.print_exc()

def main():
    """Executa todos os testes de diagnóstico."""
    print("🔍 DIAGNÓSTICO COMPLETO DO SISTEMA RAG")
    print("=" * 50)
    
    test_imports()
    test_gpu_compatibility()
    test_backend_selection()
    test_index_files()
    test_initialization()
    test_search_functionality()
    
    print("\n" + "=" * 50)
    print("🏁 DIAGNÓSTICO CONCLUÍDO")

if __name__ == "__main__":
    main()