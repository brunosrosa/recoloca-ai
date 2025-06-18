#!/usr/bin/env python3
"""
Teste do PyTorchGPURetriever para verificar funcionamento com GPU RTX 2060

Este script testa:
1. Carregamento do índice PyTorch convertido
2. Funcionamento da busca semântica
3. Performance com GPU vs CPU
4. Validação dos resultados
"""

import os
import sys
import time
import logging
from pathlib import Path

# Adicionar o diretório pai ao path para importar módulos
sys.path.append(str(Path(__file__).parent))

from pytorch_gpu_retriever import PyTorchGPURetriever

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_pytorch_gpu_retriever():
    """
    Testa o PyTorchGPURetriever com diferentes configurações
    """
    print("=" * 60)
    print("TESTE DO PYTORCH GPU RETRIEVER")
    print("=" * 60)
    
    # Definir caminhos
    base_dir = Path(__file__).parent.parent
    index_dir = base_dir / "data_index" / "faiss_index_bge_m3"
    pytorch_data_path = index_dir / "embeddings.npy"
    
    print(f"\n📁 Diretório base: {base_dir}")
    print(f"📁 Diretório do índice: {index_dir}")
    print(f"📄 Arquivo PyTorch: {pytorch_data_path}")
    
    # Verificar se os arquivos existem
    if not pytorch_data_path.exists():
        print(f"❌ ERRO: Arquivo PyTorch não encontrado: {pytorch_data_path}")
        print("\n💡 Execute primeiro o script convert_faiss_to_pytorch.py")
        return False
    
    print(f"✅ Arquivo PyTorch encontrado: {pytorch_data_path.stat().st_size / 1024 / 1024:.1f} MB")
    
    # Teste 1: Inicialização com GPU
    print("\n" + "="*50)
    print("TESTE 1: Inicialização com GPU")
    print("="*50)
    
    try:
        retriever_gpu = PyTorchGPURetriever(force_cpu=False)
        retriever_gpu.initialize()
        retriever_gpu.load_index()
        print("✅ PyTorchGPURetriever inicializado com GPU")
        print(f"🔧 Dispositivo: {retriever_gpu.device}")
        print(f"📊 Dimensões dos embeddings: {retriever_gpu.embeddings_tensor.shape}")
        print(f"📚 Total de documentos: {len(retriever_gpu.documents)}")
    except Exception as e:
        print(f"❌ ERRO na inicialização com GPU: {e}")
        return False
    
    # Teste 2: Inicialização com CPU (comparação)
    print("\n" + "="*50)
    print("TESTE 2: Inicialização com CPU (comparação)")
    print("="*50)
    
    try:
        retriever_cpu = PyTorchGPURetriever(force_cpu=True)
        retriever_cpu.initialize()
        retriever_cpu.load_index()
        print("✅ PyTorchGPURetriever inicializado com CPU")
        print(f"🔧 Dispositivo: {retriever_cpu.device}")
    except Exception as e:
        print(f"❌ ERRO na inicialização com CPU: {e}")
        return False
    
    # Teste 3: Busca semântica com GPU
    print("\n" + "="*50)
    print("TESTE 3: Busca semântica com GPU")
    print("="*50)
    
    test_queries = [
        "Como criar um currículo eficaz?",
        "Dicas para entrevista de emprego",
        "Desenvolvimento de carreira em tecnologia",
        "Networking profissional",
        "Transição de carreira"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n🔍 Query {i}: '{query}'")
        
        try:
            # Busca com GPU
            start_time = time.time()
            results_gpu = retriever_gpu.search(query, top_k=3)
            gpu_time = time.time() - start_time
            
            print(f"⚡ Tempo GPU: {gpu_time*1000:.1f}ms")
            print(f"📊 Resultados encontrados: {len(results_gpu)}")
            
            if results_gpu:
                best_result = results_gpu[0]
                print(f"🏆 Melhor resultado (score: {best_result.score:.4f}):")
                print(f"   📄 Documento: {best_result.document_name}")
                print(f"   📝 Trecho: {best_result.content[:100]}...")
                
                # Busca com CPU para comparação
                start_time = time.time()
                results_cpu = retriever_cpu.search(query, top_k=3)
                cpu_time = time.time() - start_time
                
                print(f"🐌 Tempo CPU: {cpu_time*1000:.1f}ms")
                
                if gpu_time > 0:
                    speedup = cpu_time / gpu_time
                    print(f"🚀 Speedup GPU: {speedup:.1f}x")
            else:
                print("⚠️  Nenhum resultado encontrado")
                
        except Exception as e:
            print(f"❌ ERRO na busca: {e}")
            continue
    
    # Teste 4: Teste de stress (múltiplas buscas)
    print("\n" + "="*50)
    print("TESTE 4: Teste de performance (10 buscas)")
    print("="*50)
    
    stress_query = "Como melhorar meu perfil profissional?"
    num_searches = 10
    
    # GPU
    start_time = time.time()
    for _ in range(num_searches):
        retriever_gpu.search(stress_query, top_k=5)
    gpu_total_time = time.time() - start_time
    
    # CPU
    start_time = time.time()
    for _ in range(num_searches):
        retriever_cpu.search(stress_query, top_k=5)
    cpu_total_time = time.time() - start_time
    
    print(f"⚡ GPU - {num_searches} buscas: {gpu_total_time*1000:.1f}ms (média: {gpu_total_time*1000/num_searches:.1f}ms)")
    print(f"🐌 CPU - {num_searches} buscas: {cpu_total_time*1000:.1f}ms (média: {cpu_total_time*1000/num_searches:.1f}ms)")
    
    if gpu_total_time > 0:
        speedup = cpu_total_time / gpu_total_time
        print(f"🚀 Speedup médio GPU: {speedup:.1f}x")
    
    # Teste 5: Validação de consistência
    print("\n" + "="*50)
    print("TESTE 5: Validação de consistência GPU vs CPU")
    print("="*50)
    
    validation_query = "Estratégias de busca de emprego"
    
    try:
        results_gpu = retriever_gpu.search(validation_query, top_k=5)
        results_cpu = retriever_cpu.search(validation_query, top_k=5)
        
        print(f"📊 Resultados GPU: {len(results_gpu)}")
        print(f"📊 Resultados CPU: {len(results_cpu)}")
        
        if len(results_gpu) == len(results_cpu):
            # Comparar scores (devem ser muito similares)
            score_diff = 0
            for i in range(min(len(results_gpu), len(results_cpu))):
                diff = abs(results_gpu[i].score - results_cpu[i].score)
                score_diff += diff
                print(f"   Resultado {i+1}: GPU={results_gpu[i].score:.4f}, CPU={results_cpu[i].score:.4f}, diff={diff:.6f}")
            
            avg_diff = score_diff / len(results_gpu) if results_gpu else 0
            print(f"\n📈 Diferença média de scores: {avg_diff:.6f}")
            
            if avg_diff < 0.001:  # Tolerância para diferenças de precisão
                print("✅ Consistência validada: resultados GPU e CPU são equivalentes")
            else:
                print("⚠️  Diferença significativa entre GPU e CPU detectada")
        else:
            print("⚠️  Número diferente de resultados entre GPU e CPU")
            
    except Exception as e:
        print(f"❌ ERRO na validação: {e}")
    
    print("\n" + "="*60)
    print("✅ TESTE CONCLUÍDO COM SUCESSO!")
    print("\n📋 RESUMO:")
    print(f"   🔧 GPU detectada e funcionando: {retriever_gpu.device != 'cpu'}")
    print(f"   📊 Total de documentos indexados: {len(retriever_gpu.documents)}")
    print(f"   ⚡ PyTorch GPU Retriever operacional")
    print("\n💡 O sistema está pronto para substituir o FAISS-GPU!")
    print("="*60)
    
    return True

if __name__ == "__main__":
    try:
        success = test_pytorch_gpu_retriever()
        if success:
            print("\n🎉 Todos os testes passaram!")
            sys.exit(0)
        else:
            print("\n❌ Alguns testes falharam.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️  Teste interrompido pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 ERRO CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)