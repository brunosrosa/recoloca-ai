#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para converter embeddings do NumPy para PyTorch
"""

import numpy as np
import torch
from pathlib import Path
import json

def convert_embeddings():
    """Converte embeddings de NumPy para PyTorch"""
    
    # Caminhos dos arquivos
    faiss_dir = Path("rag_infra/data_index/faiss_index_bge_m3")
    pytorch_dir = Path("rag_infra/data_index/pytorch_index_bge_m3")
    
    # Carregar embeddings NumPy
    embeddings_path = faiss_dir / "embeddings.npy"
    if not embeddings_path.exists():
        print(f"❌ Arquivo não encontrado: {embeddings_path}")
        return False
    
    print(f"📂 Carregando embeddings de {embeddings_path}")
    embeddings_np = np.load(embeddings_path)
    print(f"✅ Shape dos embeddings: {embeddings_np.shape}")
    
    # Converter para PyTorch tensor
    embeddings_torch = torch.from_numpy(embeddings_np).float()
    
    # Salvar como arquivo PyTorch
    pytorch_embeddings_path = pytorch_dir / "embeddings.pt"
    torch.save(embeddings_torch, pytorch_embeddings_path)
    print(f"✅ Embeddings salvos em: {pytorch_embeddings_path}")
    
    # Criar arquivo de mapeamento
    mapping_data = {
        "embedding_dim": embeddings_torch.shape[1],
        "num_embeddings": embeddings_torch.shape[0],
        "dtype": str(embeddings_torch.dtype),
        "device": "cpu"
    }
    
    mapping_path = pytorch_dir / "mapping.json"
    with open(mapping_path, 'w', encoding='utf-8') as f:
        json.dump(mapping_data, f, indent=2, ensure_ascii=False)
    print(f"✅ Mapeamento salvo em: {mapping_path}")
    
    return True

if __name__ == "__main__":
    print("=== Conversão de Embeddings NumPy para PyTorch ===")
    success = convert_embeddings()
    if success:
        print("\n✅ Conversão concluída com sucesso!")
    else:
        print("\n❌ Falha na conversão!")