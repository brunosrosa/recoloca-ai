#!/usr/bin/env python3
"""
Script de Inicialização RAG - RTX 2060 Otimizado
Gerado automaticamente em 2025-06-18 21:03:05
"""

import os
import sys
from pathlib import Path

# Adicionar diretório do projeto ao path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Configurar variáveis de ambiente
os.environ['RAG_USE_OPTIMIZATIONS'] = 'true'
os.environ['RAG_CACHE_ENABLED'] = 'true'
os.environ['RAG_FORCE_PYTORCH'] = 'true'
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:512'
os.environ['OMP_NUM_THREADS'] = '2'

def main():
    """Inicializa RAG com configurações RTX 2060."""
    try:
        from rag_infra.core_logic.rag_retriever import RAGRetriever
        
        print("🚀 Inicializando RAG com otimizações RTX 2060...")
        
        retriever = RAGRetriever(
            use_optimizations=True,
            cache_enabled=True,
            batch_size=6,
            force_pytorch=True
        )
        
        print("✅ RAG inicializado com sucesso!")
        print(f"📊 Configurações aplicadas:")
        print(f"   • Cache: True")
        print(f"   • Lote: 6")
        print(f"   • PyTorch forçado: True")
        print(f"   • Limite VRAM: 4096MB")
        
        return retriever
        
    except Exception as e:
        print(f"❌ Erro ao inicializar RAG: {e}")
        return None

if __name__ == "__main__":
    retriever = main()
    if retriever:
        print("
🎯 RAG pronto para uso!")
        print("Use retriever.search('sua consulta') para buscar")
    else:
        sys.exit(1)
