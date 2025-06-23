#!/usr/bin/env python3
"""
Teste de alternativas para busca vetorial com GPU
Para RTX 2060 que não funciona com faiss-gpu devido a limitações WDDM
"""

import os
import sys
import time
import numpy as np
from typing import List, Tuple, Optional

def test_pytorch_cuda():
    """Testa se PyTorch consegue usar CUDA"""
    print("\n=== Testando PyTorch com CUDA ===")
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        
        if torch.cuda.is_available():
            print(f"CUDA version: {torch.version.cuda}")
            print(f"GPU count: {torch.cuda.device_count()}")
            print(f"Current GPU: {torch.cuda.current_device()}")
            print(f"GPU name: {torch.cuda.get_device_name(0)}")
            
            # Teste simples de operação GPU
            x = torch.randn(1000, 1000).cuda()
            y = torch.randn(1000, 1000).cuda()
            
            start_time = time.time()
            z = torch.mm(x, y)
            torch.cuda.synchronize()
            gpu_time = time.time() - start_time
            
            print(f"GPU matrix multiplication time: {gpu_time:.4f}s")
            
            # Comparação com CPU
            x_cpu = x.cpu()
            y_cpu = y.cpu()
            
            start_time = time.time()
            z_cpu = torch.mm(x_cpu, y_cpu)
            cpu_time = time.time() - start_time
            
            print(f"CPU matrix multiplication time: {cpu_time:.4f}s")
            print(f"GPU speedup: {cpu_time/gpu_time:.2f}x")
            
            return True
        else:
            print("CUDA não está disponível no PyTorch")
            return False
            
    except ImportError:
        print("PyTorch não está instalado")
        return False
    except Exception as e:
        print(f"Erro ao testar PyTorch: {e}")
        return False

def test_sklearn_with_gpu():
    """Testa scikit-learn com aceleração GPU via cuML se disponível"""
    print("\n=== Testando scikit-learn ===")
    try:
        from sklearn.neighbors import NearestNeighbors
        from sklearn.datasets import make_blobs
        
        # Gerar dados de teste
        X, _ = make_blobs(n_samples=10000, centers=10, n_features=128, random_state=42)
        query = X[:5]  # Primeiras 5 amostras como query
        
        # Teste com scikit-learn padrão
        start_time = time.time()
        nn = NearestNeighbors(n_neighbors=10, algorithm='auto')
        nn.fit(X)
        distances, indices = nn.kneighbors(query)
        sklearn_time = time.time() - start_time
        
        print(f"scikit-learn NearestNeighbors time: {sklearn_time:.4f}s")
        print(f"Found {len(indices)} results")
        
        return True
        
    except ImportError:
        print("scikit-learn não está instalado")
        return False
    except Exception as e:
        print(f"Erro ao testar scikit-learn: {e}")
        return False

def test_annoy():
    """Testa biblioteca Annoy para busca aproximada"""
    print("\n=== Testando Annoy ===")
    try:
        from annoy import AnnoyIndex
        
        # Configuração
        vector_dim = 128
        n_vectors = 10000
        n_trees = 10
        
        # Criar índice
        index = AnnoyIndex(vector_dim, 'angular')
        
        # Adicionar vetores aleatórios
        vectors = []
        for i in range(n_vectors):
            vector = np.random.normal(size=vector_dim)
            vectors.append(vector)
            index.add_item(i, vector)
        
        # Construir índice
        start_time = time.time()
        index.build(n_trees)
        build_time = time.time() - start_time
        
        print(f"Annoy index build time: {build_time:.4f}s")
        
        # Teste de busca
        query_vector = np.random.normal(size=vector_dim)
        
        start_time = time.time()
        similar_items = index.get_nns_by_vector(query_vector, 10, include_distances=True)
        search_time = time.time() - start_time
        
        print(f"Annoy search time: {search_time:.4f}s")
        print(f"Found {len(similar_items[0])} results")
        
        return True
        
    except ImportError:
        print("Annoy não está instalado. Instale com: pip install annoy")
        return False
    except Exception as e:
        print(f"Erro ao testar Annoy: {e}")
        return False

def test_hnswlib():
    """Testa biblioteca hnswlib para busca aproximada"""
    print("\n=== Testando hnswlib ===")
    try:
        import hnswlib
        
        # Configuração
        vector_dim = 128
        n_vectors = 10000
        
        # Gerar dados
        data = np.random.random((n_vectors, vector_dim)).astype(np.float32)
        
        # Criar índice
        index = hnswlib.Index(space='cosine', dim=vector_dim)
        index.init_index(max_elements=n_vectors, ef_construction=200, M=16)
        
        # Adicionar dados
        start_time = time.time()
        index.add_items(data, np.arange(n_vectors))
        build_time = time.time() - start_time
        
        print(f"hnswlib index build time: {build_time:.4f}s")
        
        # Teste de busca
        query = np.random.random((1, vector_dim)).astype(np.float32)
        
        start_time = time.time()
        labels, distances = index.knn_query(query, k=10)
        search_time = time.time() - start_time
        
        print(f"hnswlib search time: {search_time:.4f}s")
        print(f"Found {len(labels[0])} results")
        
        return True
        
    except ImportError:
        print("hnswlib não está instalado. Instale com: pip install hnswlib")
        return False
    except Exception as e:
        print(f"Erro ao testar hnswlib: {e}")
        return False

def test_pytorch_vector_search():
    """Implementa busca vetorial usando PyTorch com GPU"""
    print("\n=== Testando busca vetorial com PyTorch GPU ===")
    try:
        import torch
        import torch.nn.functional as F
        
        if not torch.cuda.is_available():
            print("CUDA não disponível, usando CPU")
            device = torch.device('cpu')
        else:
            device = torch.device('cuda')
            print(f"Usando GPU: {torch.cuda.get_device_name(0)}")
        
        # Configuração
        n_vectors = 10000
        vector_dim = 128
        k = 10
        
        # Gerar dados
        vectors = torch.randn(n_vectors, vector_dim, device=device)
        query = torch.randn(1, vector_dim, device=device)
        
        # Normalizar para similaridade coseno
        vectors_norm = F.normalize(vectors, p=2, dim=1)
        query_norm = F.normalize(query, p=2, dim=1)
        
        # Busca por similaridade coseno
        start_time = time.time()
        similarities = torch.mm(query_norm, vectors_norm.t())
        top_k_values, top_k_indices = torch.topk(similarities, k, dim=1)
        
        if device.type == 'cuda':
            torch.cuda.synchronize()
        
        search_time = time.time() - start_time
        
        print(f"PyTorch GPU vector search time: {search_time:.4f}s")
        print(f"Found {len(top_k_indices[0])} results")
        print(f"Top similarities: {top_k_values[0][:5].cpu().numpy()}")
        
        return True
        
    except ImportError:
        print("PyTorch não está instalado")
        return False
    except Exception as e:
        print(f"Erro ao testar PyTorch vector search: {e}")
        return False

def main():
    """Executa todos os testes"""
    print("Testando alternativas para busca vetorial com GPU")
    print("=" * 50)
    
    results = {
        'pytorch_cuda': test_pytorch_cuda(),
        'sklearn': test_sklearn_with_gpu(),
        'annoy': test_annoy(),
        'hnswlib': test_hnswlib(),
        'pytorch_vector_search': test_pytorch_vector_search()
    }
    
    print("\n" + "=" * 50)
    print("RESUMO DOS TESTES:")
    print("=" * 50)
    
    for test_name, success in results.items():
        status = "[OK] PASSOU" if success else "[ERROR] FALHOU"
        print(f"{test_name}: {status}")
    
    # Recomendações
    print("\n" + "=" * 50)
    print("RECOMENDAÇÕES:")
    print("=" * 50)
    
    if results['pytorch_cuda']:
        print("[OK] PyTorch com CUDA está funcionando!")
        print("   Recomendação: Use PyTorch para busca vetorial com GPU")
        print("   Comando: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121")
    
    if results['hnswlib']:
        print("[OK] hnswlib está funcionando!")
        print("   Recomendação: Use hnswlib para busca aproximada rápida (CPU)")
        print("   Comando: pip install hnswlib")
    
    if results['annoy']:
        print("[OK] Annoy está funcionando!")
        print("   Recomendação: Use Annoy como alternativa para busca aproximada")
        print("   Comando: pip install annoy")
    
    print("\n[EMOJI] NOTA: Para RTX 2060, PyTorch com CUDA é a melhor opção")
    print("   para aceleração GPU, já que faiss-gpu tem limitações com")
    print("   placas GeForce em modo WDDM.")

if __name__ == "__main__":
    main()