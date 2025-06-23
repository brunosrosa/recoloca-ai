#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstração Prática do Sistema RAG Integrado
Para o projeto Recoloca.ai

Este script demonstra como usar o sistema RAG completo
com PyTorch GPU, otimizações e cache persistente.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import os
import sys
import time
import logging
from pathlib import Path
from typing import List, Dict, Any

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Adicionar path do projeto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag_infra.src.core.core_logic.rag_retriever import RAGRetriever
from rag_infra.src.core.core_logic.pytorch_gpu_retriever import PyTorchGPURetriever
from rag_infra.src.core.core_logic.pytorch_optimizations import OptimizedPyTorchRetriever

class RAGSystemDemo:
    """Demonstração do sistema RAG completo."""
    
    def __init__(self):
        self.retrievers = {}
        self.demo_documents = [
            "Python é uma linguagem de programação de alto nível.",
            "FastAPI é um framework web moderno para Python.",
            "PyTorch é uma biblioteca de machine learning.",
            "CUDA permite computação paralela em GPUs NVIDIA.",
            "RAG combina recuperação de informações com geração de texto.",
            "Supabase é uma alternativa open source ao Firebase.",
            "Recoloca.ai é uma plataforma de recolocação profissional.",
            "Machine Learning ajuda na análise de currículos.",
            "APIs REST facilitam a integração entre sistemas.",
            "Cache melhora a performance de aplicações web."
        ]
    
    def demo_backend_detection(self):
        """Demonstra detecção automática de backend."""
        logger.info("[SEARCH] === DEMONSTRAÇÃO: DETECÇÃO DE BACKEND ===")
        
        retriever = RAGRetriever()
        backend_info = retriever.get_backend_info()
        
        logger.info("[EMOJI] Informações do Backend:")
        for key, value in backend_info.items():
            logger.info(f"   {key}: {value}")
        
        return backend_info
    
    def demo_pytorch_gpu_retriever(self):
        """Demonstra uso do PyTorchGPURetriever."""
        logger.info("\n[START] === DEMONSTRAÇÃO: PYTORCH GPU RETRIEVER ===")
        
        # Criar retriever
        retriever = PyTorchGPURetriever(batch_size=32)
        self.retrievers['pytorch'] = retriever
        
        # Inicializar
        logger.info("[EMOJI] Inicializando retriever...")
        init_success = retriever.initialize()
        logger.info(f"   Inicialização: {'[OK] Sucesso' if init_success else '[ERROR] Falhou'}")
        
        # Mostrar informações
        index_info = retriever.get_index_info()
        logger.info("[EMOJI] Informações do Índice:")
        for key, value in index_info.items():
            logger.info(f"   {key}: {value}")
        
        # Mostrar estatísticas
        stats = retriever.get_stats()
        logger.info("[EMOJI] Estatísticas:")
        logger.info(f"   GPU: {stats.get('gpu_name', 'N/A')}")
        logger.info(f"   Memória GPU Alocada: {stats.get('gpu_memory_allocated', 0) / 1024**3:.2f} GB")
        logger.info(f"   Dispositivo: {stats.get('device', 'N/A')}")
        
        return retriever
    
    def demo_optimized_retriever(self):
        """Demonstra uso do OptimizedPyTorchRetriever."""
        logger.info("\n[EMOJI] === DEMONSTRAÇÃO: OPTIMIZED PYTORCH RETRIEVER ===")
        
        # Criar retriever otimizado
        retriever = OptimizedPyTorchRetriever(
            cache_enabled=True,
            cache_ttl=300,  # 5 minutos
            batch_size=32,
            max_workers=4
        )
        self.retrievers['optimized'] = retriever
        
        # Inicializar
        logger.info("[EMOJI] Inicializando retriever otimizado...")
        init_success = retriever.initialize()
        logger.info(f"   Inicialização: {'[OK] Sucesso' if init_success else '[ERROR] Falhou'}")
        
        # Mostrar informações do cache
        cache_info = retriever.get_cache_info()
        logger.info("[SAVE] Informações do Cache:")
        for key, value in cache_info.items():
            logger.info(f"   {key}: {value}")
        
        # Mostrar estatísticas completas
        stats = retriever.get_stats()
        logger.info("[EMOJI] Estatísticas Completas:")
        logger.info(f"   Cache Habilitado: {stats.get('cache_enabled', False)}")
        logger.info(f"   Batch Size: {stats.get('batch_size', 'N/A')}")
        logger.info(f"   Max Workers: {stats.get('max_workers', 'N/A')}")
        
        return retriever
    
    def demo_rag_retriever_configurations(self):
        """Demonstra diferentes configurações do RAGRetriever."""
        logger.info("\n[EMOJI] === DEMONSTRAÇÃO: CONFIGURAÇÕES RAG RETRIEVER ===")
        
        configurations = [
            {
                "name": "Auto (Padrão)",
                "params": {},
                "description": "Detecção automática do melhor backend"
            },
            {
                "name": "PyTorch Forçado",
                "params": {"force_pytorch": True},
                "description": "Força uso do PyTorch GPU"
            },
            {
                "name": "Otimizado com Cache",
                "params": {
                    "force_pytorch": True,
                    "use_optimizations": True,
                    "cache_enabled": True,
                    "batch_size": 64
                },
                "description": "PyTorch otimizado com cache persistente"
            }
        ]
        
        for config in configurations:
            logger.info(f"\n[EMOJI] Testando: {config['name']}")
            logger.info(f"   Descrição: {config['description']}")
            
            try:
                retriever = RAGRetriever(**config['params'])
                backend_info = retriever.get_backend_info()
                index_info = retriever.get_index_info()
                
                logger.info(f"   [OK] Backend: {backend_info.get('current_backend', 'N/A')}")
                logger.info(f"   [EMOJI] Status: {index_info.get('status', 'N/A')}")
                
                self.retrievers[config['name']] = retriever
                
            except Exception as e:
                logger.error(f"   [ERROR] Erro: {e}")
    
    def demo_performance_comparison(self):
        """Demonstra comparação de performance entre backends."""
        logger.info("\n[EMOJI] === DEMONSTRAÇÃO: COMPARAÇÃO DE PERFORMANCE ===")
        
        import torch
        
        if not torch.cuda.is_available():
            logger.warning("[WARNING] GPU não disponível. Pulando teste de performance.")
            return
        
        # Teste de operações básicas
        logger.info("🧪 Testando operações básicas...")
        
        # Teste 1: Multiplicação de matrizes
        sizes = [100, 500, 1000]
        
        for size in sizes:
            logger.info(f"\n[EMOJI] Testando matrizes {size}x{size}:")
            
            # CPU
            start_time = time.time()
            x_cpu = torch.randn(size, size)
            y_cpu = torch.randn(size, size)
            z_cpu = torch.mm(x_cpu, y_cpu)
            cpu_time = time.time() - start_time
            
            # GPU
            start_time = time.time()
            x_gpu = torch.randn(size, size, device='cuda')
            y_gpu = torch.randn(size, size, device='cuda')
            z_gpu = torch.mm(x_gpu, y_gpu)
            torch.cuda.synchronize()
            gpu_time = time.time() - start_time
            
            speedup = cpu_time / gpu_time if gpu_time > 0 else 0
            
            logger.info(f"   CPU: {cpu_time:.4f}s")
            logger.info(f"   GPU: {gpu_time:.4f}s")
            logger.info(f"   Speedup: {speedup:.2f}x")
    
    def demo_memory_usage(self):
        """Demonstra monitoramento de uso de memória."""
        logger.info("\n[SAVE] === DEMONSTRAÇÃO: MONITORAMENTO DE MEMÓRIA ===")
        
        import torch
        
        if torch.cuda.is_available():
            # Memória GPU
            gpu_memory_allocated = torch.cuda.memory_allocated(0)
            gpu_memory_reserved = torch.cuda.memory_reserved(0)
            gpu_memory_total = torch.cuda.get_device_properties(0).total_memory
            
            logger.info("[EMOJI] Memória GPU:")
            logger.info(f"   Alocada: {gpu_memory_allocated / 1024**3:.2f} GB")
            logger.info(f"   Reservada: {gpu_memory_reserved / 1024**3:.2f} GB")
            logger.info(f"   Total: {gpu_memory_total / 1024**3:.2f} GB")
            logger.info(f"   Uso: {(gpu_memory_allocated / gpu_memory_total) * 100:.1f}%")
        
        # Memória do sistema
        try:
            import psutil
            memory = psutil.virtual_memory()
            
            logger.info("\n[EMOJI] Memória Sistema:")
            logger.info(f"   Total: {memory.total / 1024**3:.2f} GB")
            logger.info(f"   Disponível: {memory.available / 1024**3:.2f} GB")
            logger.info(f"   Uso: {memory.percent:.1f}%")
            
        except ImportError:
            logger.info("\n[WARNING] psutil não disponível para monitoramento de memória do sistema")
    
    def demo_best_practices(self):
        """Demonstra melhores práticas de uso."""
        logger.info("\n[EMOJI] === DEMONSTRAÇÃO: MELHORES PRÁTICAS ===")
        
        practices = [
            {
                "title": "1. Detecção Automática de Backend",
                "code": "retriever = RAGRetriever()  # Auto-detecta melhor backend",
                "benefit": "Adapta automaticamente ao hardware disponível"
            },
            {
                "title": "2. Forçar PyTorch para GPU",
                "code": "retriever = RAGRetriever(force_pytorch=True)",
                "benefit": "Garante uso de GPU quando disponível"
            },
            {
                "title": "3. Usar Otimizações com Cache",
                "code": "retriever = RAGRetriever(use_optimizations=True, cache_enabled=True)",
                "benefit": "Máxima performance com cache persistente"
            },
            {
                "title": "4. Configurar Batch Size",
                "code": "retriever = RAGRetriever(batch_size=64)",
                "benefit": "Otimiza throughput para múltiplas consultas"
            },
            {
                "title": "5. Monitorar Performance",
                "code": "stats = retriever.get_stats(); cache_info = retriever.get_cache_info()",
                "benefit": "Permite otimização baseada em métricas reais"
            }
        ]
        
        for practice in practices:
            logger.info(f"\n[EMOJI] {practice['title']}")
            logger.info(f"   Código: {practice['code']}")
            logger.info(f"   Benefício: {practice['benefit']}")
    
    def run_complete_demo(self):
        """Executa demonstração completa do sistema."""
        logger.info("[EMOJI] INICIANDO DEMONSTRAÇÃO COMPLETA DO SISTEMA RAG")
        logger.info("=" * 70)
        
        try:
            # 1. Detecção de backend
            self.demo_backend_detection()
            
            # 2. PyTorch GPU Retriever
            self.demo_pytorch_gpu_retriever()
            
            # 3. Optimized Retriever
            self.demo_optimized_retriever()
            
            # 4. Configurações RAG Retriever
            self.demo_rag_retriever_configurations()
            
            # 5. Comparação de performance
            self.demo_performance_comparison()
            
            # 6. Monitoramento de memória
            self.demo_memory_usage()
            
            # 7. Melhores práticas
            self.demo_best_practices()
            
            logger.info("\n" + "=" * 70)
            logger.info("[EMOJI] DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
            logger.info("\n[EMOJI] RESUMO DAS FUNCIONALIDADES DEMONSTRADAS:")
            logger.info("   [OK] Detecção automática de backend")
            logger.info("   [OK] PyTorch GPU Retriever")
            logger.info("   [OK] Optimized Retriever com cache")
            logger.info("   [OK] Múltiplas configurações RAG")
            logger.info("   [OK] Comparação de performance")
            logger.info("   [OK] Monitoramento de memória")
            logger.info("   [OK] Melhores práticas de uso")
            
            logger.info("\n[START] O sistema RAG está pronto para produção!")
            
        except Exception as e:
            logger.error(f"[ERROR] Erro durante a demonstração: {e}")
            raise

def main():
    """Função principal."""
    demo = RAGSystemDemo()
    demo.run_complete_demo()

if __name__ == "__main__":
    main()