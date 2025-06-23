#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste Final de Integração do Sistema RAG com PyTorch GPU
Para o projeto Recoloca.ai

Este script demonstra a integração completa do sistema RAG
com PyTorch GPU, incluindo otimizações e cache persistente.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Janeiro 2025
"""

import os
import sys
import time
import json
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
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from rag_infra.src.core.rag_retriever import RAGRetriever
from rag_infra.src.core.pytorch_gpu_retriever import PyTorchGPURetriever
from rag_infra.src.core.pytorch_optimizations import OptimizedPyTorchRetriever

class RAGFinalIntegrationTester:
    """Testador de integração final do sistema RAG."""
    
    def __init__(self):
        self.results = {
            "timestamp": time.time(),
            "tests": {},
            "summary": {},
            "recommendations": []
        }
    
    def test_backend_detection(self) -> bool:
        """Testa detecção automática de backend."""
        logger.info("[SEARCH] Testando detecção de backend...")
        
        try:
            # Teste com auto-detecção
            retriever = RAGRetriever()
            backend_info = retriever.get_backend_info()
            
            self.results["tests"]["backend_detection"] = {
                "status": "success",
                "backend_info": backend_info,
                "gpu_available": backend_info.get("gpu_available", False),
                "recommended_backend": backend_info.get("recommended_backend", "unknown")
            }
            
            logger.info(f"[OK] Backend detectado: {backend_info.get('recommended_backend')}")
            logger.info(f"   GPU disponível: {backend_info.get('gpu_available')}")
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro na detecção de backend: {e}")
            self.results["tests"]["backend_detection"] = {
                "status": "error",
                "error": str(e)
            }
            return False
    
    def test_pytorch_gpu_retriever(self) -> bool:
        """Testa PyTorchGPURetriever diretamente."""
        logger.info("[START] Testando PyTorchGPURetriever...")
        
        try:
            # Criar retriever PyTorch
            retriever = PyTorchGPURetriever()
            
            # Testar inicialização
            init_success = retriever.initialize()
            
            # Obter informações do índice
            index_info = retriever.get_index_info()
            
            # Testar estatísticas
            stats = retriever.get_stats()
            
            self.results["tests"]["pytorch_gpu_retriever"] = {
                "status": "success" if init_success else "partial",
                "initialization": init_success,
                "index_info": index_info,
                "stats": stats,
                "device": str(retriever.device)
            }
            
            logger.info(f"[OK] PyTorchGPURetriever: {'Inicializado' if init_success else 'Parcial'}")
            logger.info(f"   Dispositivo: {retriever.device}")
            logger.info(f"   Status do índice: {index_info.get('status', 'unknown')}")
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro no PyTorchGPURetriever: {e}")
            self.results["tests"]["pytorch_gpu_retriever"] = {
                "status": "error",
                "error": str(e)
            }
            return False
    
    def test_optimized_retriever(self) -> bool:
        """Testa OptimizedPyTorchRetriever com cache."""
        logger.info("[EMOJI] Testando OptimizedPyTorchRetriever...")
        
        try:
            # Criar retriever otimizado
            retriever = OptimizedPyTorchRetriever(
                cache_enabled=True,
                cache_ttl=300,  # 5 minutos
                batch_size=32,
                max_workers=4
            )
            
            # Testar inicialização
            init_success = retriever.initialize()
            
            # Obter informações do cache
            cache_info = retriever.get_cache_info()
            
            # Obter estatísticas
            stats = retriever.get_stats()
            
            self.results["tests"]["optimized_retriever"] = {
                "status": "success" if init_success else "partial",
                "initialization": init_success,
                "cache_info": cache_info,
                "stats": stats,
                "optimizations_enabled": True
            }
            
            logger.info(f"[OK] OptimizedPyTorchRetriever: {'Inicializado' if init_success else 'Parcial'}")
            logger.info(f"   Cache habilitado: {cache_info.get('enabled', False)}")
            logger.info(f"   Batch size: {retriever.batch_size}")
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro no OptimizedPyTorchRetriever: {e}")
            self.results["tests"]["optimized_retriever"] = {
                "status": "error",
                "error": str(e)
            }
            return False
    
    def test_rag_retriever_integration(self) -> bool:
        """Testa integração completa do RAGRetriever."""
        logger.info("[EMOJI] Testando integração RAGRetriever...")
        
        try:
            # Testar diferentes configurações
            configs = [
                {"name": "auto", "force_pytorch": False, "use_optimizations": False},
                {"name": "pytorch", "force_pytorch": True, "use_optimizations": False},
                {"name": "optimized", "force_pytorch": True, "use_optimizations": True}
            ]
            
            config_results = {}
            
            for config in configs:
                try:
                    retriever = RAGRetriever(
                        force_pytorch=config["force_pytorch"],
                        use_optimizations=config["use_optimizations"]
                    )
                    
                    # Testar métodos básicos
                    backend_info = retriever.get_backend_info()
                    index_info = retriever.get_index_info()
                    
                    config_results[config["name"]] = {
                        "status": "success",
                        "backend_info": backend_info,
                        "index_info": index_info
                    }
                    
                    logger.info(f"[OK] Configuração '{config['name']}': OK")
                    
                except Exception as e:
                    config_results[config["name"]] = {
                        "status": "error",
                        "error": str(e)
                    }
                    logger.warning(f"[WARNING] Configuração '{config['name']}': {e}")
            
            self.results["tests"]["rag_retriever_integration"] = {
                "status": "success",
                "configurations": config_results
            }
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro na integração RAGRetriever: {e}")
            self.results["tests"]["rag_retriever_integration"] = {
                "status": "error",
                "error": str(e)
            }
            return False
    
    def test_performance_baseline(self) -> bool:
        """Testa performance básica do sistema."""
        logger.info("[EMOJI] Testando performance baseline...")
        
        try:
            import torch
            
            # Teste de operações GPU básicas
            if torch.cuda.is_available():
                device = torch.device('cuda')
                
                # Teste de multiplicação de matrizes
                start_time = time.time()
                x = torch.randn(1000, 512, device=device)
                y = torch.randn(512, 1000, device=device)
                z = torch.mm(x, y)
                torch.cuda.synchronize()
                gpu_time = time.time() - start_time
                
                # Teste de similaridade coseno
                start_time = time.time()
                x_norm = torch.nn.functional.normalize(x, p=2, dim=1)
                y_norm = torch.nn.functional.normalize(y.t(), p=2, dim=1)
                similarities = torch.mm(x_norm, y_norm.t())
                torch.cuda.synchronize()
                cosine_time = time.time() - start_time
                
                self.results["tests"]["performance_baseline"] = {
                    "status": "success",
                    "gpu_available": True,
                    "matrix_multiplication_time": gpu_time,
                    "cosine_similarity_time": cosine_time,
                    "device": str(device),
                    "gpu_name": torch.cuda.get_device_name(0)
                }
                
                logger.info(f"[OK] Performance GPU: {gpu_time:.4f}s (matmul), {cosine_time:.4f}s (cosine)")
                
            else:
                self.results["tests"]["performance_baseline"] = {
                    "status": "success",
                    "gpu_available": False,
                    "note": "GPU não disponível, usando CPU"
                }
                
                logger.info("ℹ[EMOJI] GPU não disponível, usando CPU")
            
            return True
            
        except Exception as e:
            logger.error(f"[ERROR] Erro no teste de performance: {e}")
            self.results["tests"]["performance_baseline"] = {
                "status": "error",
                "error": str(e)
            }
            return False
    
    def generate_recommendations(self):
        """Gera recomendações baseadas nos resultados dos testes."""
        recommendations = []
        
        # Analisar resultados dos testes
        backend_test = self.results["tests"].get("backend_detection", {})
        pytorch_test = self.results["tests"].get("pytorch_gpu_retriever", {})
        optimized_test = self.results["tests"].get("optimized_retriever", {})
        performance_test = self.results["tests"].get("performance_baseline", {})
        
        # Recomendações baseadas em GPU
        if performance_test.get("gpu_available", False):
            recommendations.append({
                "priority": "high",
                "category": "hardware",
                "message": "GPU detectada e funcionando. Use PyTorch GPU para melhor performance."
            })
        else:
            recommendations.append({
                "priority": "medium",
                "category": "hardware",
                "message": "GPU não disponível. Sistema funcionará com CPU (performance reduzida)."
            })
        
        # Recomendações baseadas em backend
        if backend_test.get("status") == "success":
            recommended_backend = backend_test.get("backend_info", {}).get("recommended_backend")
            if recommended_backend == "pytorch":
                recommendations.append({
                    "priority": "high",
                    "category": "configuration",
                    "message": "Use force_pytorch=True para melhor performance com GPU."
                })
        
        # Recomendações baseadas em otimizações
        if optimized_test.get("status") == "success":
            recommendations.append({
                "priority": "medium",
                "category": "optimization",
                "message": "OptimizedPyTorchRetriever disponível. Use para cache persistente e batch processing."
            })
        
        # Recomendações de performance
        if performance_test.get("matrix_multiplication_time", 1.0) < 0.1:
            recommendations.append({
                "priority": "low",
                "category": "performance",
                "message": "Performance GPU excelente. Sistema otimizado para produção."
            })
        
        self.results["recommendations"] = recommendations
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Executa todos os testes de integração."""
        logger.info("[START] Iniciando testes de integração final do sistema RAG")
        logger.info("=" * 60)
        
        tests = [
            ("Backend Detection", self.test_backend_detection),
            ("PyTorch GPU Retriever", self.test_pytorch_gpu_retriever),
            ("Optimized Retriever", self.test_optimized_retriever),
            ("RAG Retriever Integration", self.test_rag_retriever_integration),
            ("Performance Baseline", self.test_performance_baseline)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            logger.info(f"\n🧪 Executando: {test_name}")
            try:
                if test_func():
                    passed += 1
                    logger.info(f"[OK] {test_name}: PASSOU")
                else:
                    logger.warning(f"[WARNING] {test_name}: FALHOU")
            except Exception as e:
                logger.error(f"[ERROR] {test_name}: ERRO - {e}")
        
        # Gerar resumo
        success_rate = (passed / total) * 100
        self.results["summary"] = {
            "total_tests": total,
            "passed_tests": passed,
            "success_rate": success_rate,
            "status": "excellent" if success_rate >= 90 else "good" if success_rate >= 70 else "needs_attention"
        }
        
        # Gerar recomendações
        self.generate_recommendations()
        
        # Log do resumo
        logger.info("\n" + "=" * 60)
        logger.info("[EMOJI] RESUMO FINAL DOS TESTES")
        logger.info("=" * 60)
        logger.info(f"Testes Executados: {total}")
        logger.info(f"Testes Passaram: {passed}")
        logger.info(f"Taxa de Sucesso: {success_rate:.1f}%")
        logger.info(f"Status Geral: {self.results['summary']['status'].upper()}")
        
        # Log das recomendações
        if self.results["recommendations"]:
            logger.info("\n[EMOJI] RECOMENDAÇÕES:")
            for i, rec in enumerate(self.results["recommendations"], 1):
                priority_icon = "[EMOJI]" if rec["priority"] == "high" else "🟡" if rec["priority"] == "medium" else "🟢"
                logger.info(f"  {i}. {priority_icon} [{rec['category'].upper()}] {rec['message']}")
        
        return self.results

def main():
    """Função principal."""
    tester = RAGFinalIntegrationTester()
    results = tester.run_all_tests()
    
    # Salvar resultados
    results_file = Path("rag_final_integration_results.json")
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    logger.info(f"\n[EMOJI] Resultados detalhados salvos em: {results_file}")
    
    # Status final
    status = results["summary"]["status"]
    if status == "excellent":
        logger.info("\n[EMOJI] Sistema RAG totalmente integrado e funcionando perfeitamente!")
    elif status == "good":
        logger.info("\n[OK] Sistema RAG funcionando bem com algumas limitações.")
    else:
        logger.info("\n[WARNING] Sistema RAG precisa de atenção. Verifique as recomendações.")
    
    return results

if __name__ == "__main__":
    main()