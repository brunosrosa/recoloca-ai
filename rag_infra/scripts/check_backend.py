#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar qual backend RAG está sendo usado
"""

import sys
from pathlib import Path

# Adicionar core_logic ao path
sys.path.append(str(Path(__file__).parent.parent / "core_logic"))

try:
    from rag_retriever import get_retriever
    
    print("🔍 Verificando configuração do backend RAG...")
    print("=" * 50)
    
    # Obter retriever
    retriever = get_retriever()
    
    # Informações básicas
    print(f"Backend em uso: {'PyTorch' if retriever.use_pytorch else 'FAISS'}")
    print(f"Force CPU: {retriever.force_cpu}")
    print(f"Force PyTorch: {retriever.force_pytorch}")
    print(f"Otimizações ativadas: {retriever.use_optimizations}")
    
    # Informações detalhadas do backend
    backend_info = retriever.get_backend_info()
    print("\n📊 Informações do Backend:")
    for key, value in backend_info.items():
        print(f"  {key}: {value}")
    
    # Verificar se FAISS-GPU está disponível
    print("\n🔧 Verificação FAISS-GPU:")
    try:
        import faiss
        print(f"  FAISS versão: {faiss.__version__ if hasattr(faiss, '__version__') else 'Desconhecida'}")
        
        if hasattr(faiss, 'StandardGpuResources'):
            print("  ✅ FAISS-GPU disponível")
        else:
            print("  ❌ FAISS-GPU não disponível")
            
    except ImportError as e:
        print(f"  ❌ Erro ao importar FAISS: {e}")
    
    # Verificar PyTorch
    print("\n🔥 Verificação PyTorch:")
    try:
        import torch
        print(f"  PyTorch versão: {torch.__version__}")
        print(f"  CUDA disponível: {torch.cuda.is_available()}")
        
        if torch.cuda.is_available():
            print(f"  GPU: {torch.cuda.get_device_name(0)}")
            print(f"  Dispositivos CUDA: {torch.cuda.device_count()}")
        
    except ImportError as e:
        print(f"  ❌ Erro ao importar PyTorch: {e}")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()