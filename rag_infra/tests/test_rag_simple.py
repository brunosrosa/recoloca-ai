#!/usr/bin/env python3
"""
Teste Simples de Integração do RAGRetriever

Testa apenas a detecção de backend e inicialização básica
sem carregar modelos pesados.
"""

import sys
import os
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from rag_infra.core_logic.rag_retriever import RAGRetriever

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_backend_detection():
    """
    Testa apenas a detecção de backend sem inicialização completa.
    """
    print("🔍 Testando detecção de backend...")
    
    try:
        # 1. Detecção automática
        retriever_auto = RAGRetriever()
        print(f"  Auto: Backend = {'PyTorch' if retriever_auto.use_pytorch else 'FAISS'}")
        print(f"        force_cpu = {retriever_auto.force_cpu}")
        print(f"        force_pytorch = {retriever_auto.force_pytorch}")
        
        # 2. Forçar PyTorch
        retriever_pytorch = RAGRetriever(force_pytorch=True)
        print(f"  PyTorch: Backend = {'PyTorch' if retriever_pytorch.use_pytorch else 'FAISS'}")
        print(f"           force_pytorch = {retriever_pytorch.force_pytorch}")
        
        # 3. Forçar CPU
        retriever_cpu = RAGRetriever(force_cpu=True)
        print(f"  CPU: Backend = {'PyTorch' if retriever_cpu.use_pytorch else 'FAISS'}")
        print(f"       force_cpu = {retriever_cpu.force_cpu}")
        
        # 4. Tentar forçar FAISS
        retriever_faiss = RAGRetriever(force_pytorch=False)
        print(f"  FAISS: Backend = {'PyTorch' if retriever_faiss.use_pytorch else 'FAISS'}")
        print(f"         force_pytorch = {retriever_faiss.force_pytorch}")
        
        print("✅ Detecção de backend funcionando")
        assert True
        
    except Exception as e:
        print(f"❌ Erro na detecção de backend: {e}")
        assert False, f"Erro na detecção de backend: {e}"

def test_gpu_compatibility():
    """
    Testa a detecção de compatibilidade GPU.
    """
    print("\n🔧 Testando compatibilidade GPU...")
    
    try:
        # Importar função de detecção
        # from retriever import _detect_gpu_compatibility  # Função pode não existir mais
        
        compatibility = _detect_gpu_compatibility()
        print(f"  GPU Compatível: {compatibility}")
        
        # Verificar CUDA
        try:
            import torch
            cuda_available = torch.cuda.is_available()
            print(f"  CUDA Disponível: {cuda_available}")
            
            if cuda_available:
                gpu_name = torch.cuda.get_device_name(0)
                print(f"  GPU: {gpu_name}")
                
        except ImportError:
            print("  PyTorch não disponível")
        
        print("✅ Teste de compatibilidade GPU concluído")
        assert True
        
    except Exception as e:
        print(f"❌ Erro no teste de compatibilidade: {e}")
        assert False, f"Erro no teste de compatibilidade: {e}"

def test_pytorch_retriever_creation():
    """
    Testa apenas a criação do PyTorchGPURetriever sem inicialização.
    """
    print("\n🏗️ Testando criação do PyTorchGPURetriever...")
    
    try:
        from pytorch_gpu_retriever import PyTorchGPURetriever
        
        # Criar retriever sem inicializar
        retriever = PyTorchGPURetriever(force_cpu=True)  # Usar CPU para evitar problemas
        print(f"  Retriever criado: {type(retriever).__name__}")
        print(f"  Force CPU: {retriever.force_cpu}")
        print(f"  Device: {retriever.device}")
        print(f"  Batch Size: {retriever.batch_size}")
        
        # Testar método get_index_info sem inicialização
        info = retriever.get_index_info()
        print(f"  Index Info: {info}")
        
        print("✅ Criação do PyTorchGPURetriever funcionando")
        assert True
        
    except Exception as e:
        print(f"❌ Erro na criação do PyTorchGPURetriever: {e}")
        assert False, f"Erro na criação do PyTorchGPURetriever: {e}"

def test_rag_retriever_methods():
    """
    Testa métodos básicos do RAGRetriever sem inicialização completa.
    """
    print("\n🔍 Testando métodos do RAGRetriever...")
    
    try:
        retriever = RAGRetriever(force_pytorch=True)
        
        # Testar get_index_info sem inicialização
        info = retriever.get_index_info()
        print(f"  Index Info (não inicializado): {info}")
        
        # Testar clear_cache
        retriever.clear_cache()
        print("  Clear cache: OK")
        
        print("✅ Métodos básicos do RAGRetriever funcionando")
        assert True
        
    except Exception as e:
        print(f"❌ Erro nos métodos do RAGRetriever: {e}")
        assert False, f"Erro nos métodos do RAGRetriever: {e}"

def main():
    """
    Executa todos os testes simples.
    """
    print("🧪 RAG Simple Integration Test")
    print("=" * 40)
    
    tests = [
        test_backend_detection,
        test_gpu_compatibility,
        test_pytorch_retriever_creation,
        test_rag_retriever_methods
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Erro no teste {test.__name__}: {e}")
            results.append(False)
    
    # Resumo
    print("\n📊 RESUMO DOS TESTES")
    print("=" * 25)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Testes Passaram: {passed}/{total}")
    print(f"Taxa de Sucesso: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n✅ Todos os testes passaram! Sistema básico funcionando.")
        print("\n🎯 Próximos passos:")
        print("  1. Otimizar carregamento de modelos")
        print("  2. Implementar testes de performance")
        print("  3. Configurar cache persistente")
    else:
        print("\n⚠️ Alguns testes falharam. Revisar configuração.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)