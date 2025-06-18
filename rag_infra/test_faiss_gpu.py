#!/usr/bin/env python3
"""
Teste para verificar se o FAISS-GPU está funcionando corretamente
"""

import faiss
import numpy as np
import sys

def test_faiss_gpu():
    print("=== Teste FAISS-GPU ===")
    print(f"FAISS version: {faiss.__version__}")
    
    # Verificar número de GPUs disponíveis
    num_gpus = faiss.get_num_gpus()
    print(f"Número de GPUs detectadas: {num_gpus}")
    
    if num_gpus == 0:
        print("❌ Nenhuma GPU detectada pelo FAISS")
        return False
    
    try:
        # Tentar criar recursos GPU
        print("\n🔧 Testando criação de recursos GPU...")
        res = faiss.StandardGpuResources()
        print("✅ Recursos GPU criados com sucesso")
        
        # Criar um índice simples para teste
        print("\n🔧 Testando criação de índice GPU...")
        d = 64  # dimensão
        nb = 100  # número de vetores na base
        nq = 10   # número de queries
        
        # Gerar dados aleatórios
        np.random.seed(1234)
        xb = np.random.random((nb, d)).astype('float32')
        xq = np.random.random((nq, d)).astype('float32')
        
        # Criar índice CPU primeiro
        index_cpu = faiss.IndexFlatL2(d)
        index_cpu.add(xb)
        
        # Transferir para GPU
        index_gpu = faiss.index_cpu_to_gpu(res, 0, index_cpu)
        print("✅ Índice transferido para GPU com sucesso")
        
        # Realizar busca
        print("\n🔧 Testando busca no índice GPU...")
        k = 4
        D, I = index_gpu.search(xq, k)
        print(f"✅ Busca realizada com sucesso. Shape dos resultados: D={D.shape}, I={I.shape}")
        
        print("\n🎉 Todos os testes passaram! FAISS-GPU está funcionando corretamente.")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        return False

if __name__ == "__main__":
    success = test_faiss_gpu()
    sys.exit(0 if success else 1)