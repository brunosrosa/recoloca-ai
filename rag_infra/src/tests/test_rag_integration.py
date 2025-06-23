#!/usr/bin/env python3
"""
Teste de Integração do RAGRetriever com PyTorchGPURetriever

Testa:
- Detecção automática de compatibilidade GPU
- Fallback inteligente FAISS → PyTorch
- Performance comparativa entre backends
- Testes de stress com múltiplas consultas
"""

import time
import asyncio
import concurrent.futures
from typing import List, Dict, Any
from pathlib import Path

import sys
import os
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag_infra.src.core.rag_retriever import RAGRetriever

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RAGIntegrationTester:
    """
    Classe para testes de integração do RAGRetriever.
    """
    
    def __init__(self):
        self.test_queries = [
            "Como implementar autenticação no FastAPI?",
            "Quais são as melhores práticas de segurança?",
            "Como configurar banco de dados PostgreSQL?",
            "Implementar sistema de cache Redis",
            "Configurar logging estruturado",
            "Deploy com Docker e Kubernetes",
            "Monitoramento e observabilidade",
            "Testes automatizados Python",
            "Arquitetura de microserviços",
            "Performance e otimização"
        ]
        
    def test_backend_detection(self) -> Dict[str, Any]:
        """
        Testa a detecção automática de backend.
        
        Returns:
            Dict: Resultados do teste
        """
        logger.info("[SEARCH] Testando detecção automática de backend...")
        
        results = {
            "auto_detection": None,
            "force_faiss": None,
            "force_pytorch": None,
            "force_cpu": None
        }
        
        try:
            # 1. Detecção automática
            retriever_auto = RAGRetriever()
            results["auto_detection"] = {
                "backend": "PyTorch" if retriever_auto.use_pytorch else "FAISS",
                "force_cpu": retriever_auto.force_cpu,
                "force_pytorch": retriever_auto.force_pytorch
            }
            
            # 2. Forçar FAISS
            retriever_faiss = RAGRetriever(force_pytorch=False)
            results["force_faiss"] = {
                "backend": "PyTorch" if retriever_faiss.use_pytorch else "FAISS",
                "force_cpu": retriever_faiss.force_cpu,
                "force_pytorch": retriever_faiss.force_pytorch
            }
            
            # 3. Forçar PyTorch
            retriever_pytorch = RAGRetriever(force_pytorch=True)
            results["force_pytorch"] = {
                "backend": "PyTorch" if retriever_pytorch.use_pytorch else "FAISS",
                "force_cpu": retriever_pytorch.force_cpu,
                "force_pytorch": retriever_pytorch.force_pytorch
            }
            
            # 4. Forçar CPU
            retriever_cpu = RAGRetriever(force_cpu=True)
            results["force_cpu"] = {
                "backend": "PyTorch" if retriever_cpu.use_pytorch else "FAISS",
                "force_cpu": retriever_cpu.force_cpu,
                "force_pytorch": retriever_cpu.force_pytorch
            }
            
            logger.info("[OK] Detecção de backend testada com sucesso")
            return results
            
        except Exception as e:
            logger.error(f"[ERROR] Erro no teste de detecção: {e}")
            return {"error": str(e)}
    
    def test_initialization_performance(self) -> Dict[str, Any]:
        """
        Testa performance de inicialização dos backends.
        
        Returns:
            Dict: Métricas de performance
        """
        logger.info("[EMOJI] Testando performance de inicialização...")
        
        results = {}
        
        # Testar PyTorch
        try:
            start_time = time.time()
            success = initialize_retriever(force_pytorch=True)
            pytorch_time = time.time() - start_time
            
            results["pytorch"] = {
                "success": success,
                "initialization_time": pytorch_time,
                "backend": "PyTorch"
            }
            
            if success:
                retriever = RAGRetriever(force_pytorch=True)
                retriever.initialize()
                retriever.load_index()
                info = retriever.get_index_info()
                results["pytorch"].update(info)
                
        except Exception as e:
            results["pytorch"] = {"error": str(e)}
        
        # Testar FAISS (se disponível)
        try:
            start_time = time.time()
            success = initialize_retriever(force_pytorch=False)
            faiss_time = time.time() - start_time
            
            results["faiss"] = {
                "success": success,
                "initialization_time": faiss_time,
                "backend": "FAISS"
            }
            
            if success:
                retriever = RAGRetriever(force_pytorch=False)
                retriever.initialize()
                retriever.load_index()
                info = retriever.get_index_info()
                results["faiss"].update(info)
                
        except Exception as e:
            results["faiss"] = {"error": str(e)}
        
        logger.info("[OK] Performance de inicialização testada")
        return results
    
    def test_search_performance(self, backend: str = "auto") -> Dict[str, Any]:
        """
        Testa performance de busca.
        
        Args:
            backend: "auto", "pytorch", "faiss"
            
        Returns:
            Dict: Métricas de performance
        """
        logger.info(f"[SEARCH] Testando performance de busca ({backend})...")
        
        # Configurar retriever
        if backend == "pytorch":
            retriever = RAGRetriever(force_pytorch=True)
        elif backend == "faiss":
            retriever = RAGRetriever(force_pytorch=False)
        else:
            retriever = RAGRetriever()
        
        # Inicializar
        if not retriever.initialize() or not retriever.load_index():
            return {"error": "Falha na inicialização"}
        
        results = {
            "backend": "PyTorch" if retriever.use_pytorch else "FAISS",
            "queries_tested": len(self.test_queries),
            "individual_times": [],
            "total_time": 0,
            "average_time": 0,
            "min_time": float('inf'),
            "max_time": 0,
            "total_results": 0,
            "cache_hits": 0
        }
        
        total_start = time.time()
        
        for i, query in enumerate(self.test_queries):
            start_time = time.time()
            
            try:
                search_results = retriever.search(query, top_k=5)
                elapsed = time.time() - start_time
                
                results["individual_times"].append({
                    "query": query[:50] + "...",
                    "time": elapsed,
                    "results_count": len(search_results)
                })
                
                results["total_results"] += len(search_results)
                results["min_time"] = min(results["min_time"], elapsed)
                results["max_time"] = max(results["max_time"], elapsed)
                
                # Testar cache (segunda consulta)
                cache_start = time.time()
                cached_results = retriever.search(query, top_k=5)
                cache_time = time.time() - cache_start
                
                if cache_time < elapsed * 0.1:  # Cache hit se for 10x mais rápido
                    results["cache_hits"] += 1
                
                logger.info(f"Query {i+1}/{len(self.test_queries)}: {elapsed:.3f}s ({len(search_results)} resultados)")
                
            except Exception as e:
                logger.error(f"Erro na query {i+1}: {e}")
                results["individual_times"].append({
                    "query": query[:50] + "...",
                    "error": str(e)
                })
        
        results["total_time"] = time.time() - total_start
        results["average_time"] = results["total_time"] / len(self.test_queries)
        
        logger.info(f"[OK] Performance testada: {results['average_time']:.3f}s média")
        return results
    
    def test_concurrent_queries(self, backend: str = "auto", max_workers: int = 5) -> Dict[str, Any]:
        """
        Testa consultas concorrentes.
        
        Args:
            backend: "auto", "pytorch", "faiss"
            max_workers: Número de workers concorrentes
            
        Returns:
            Dict: Métricas de concorrência
        """
        logger.info(f"[START] Testando consultas concorrentes ({backend}, {max_workers} workers)...")
        
        # Configurar retriever
        if backend == "pytorch":
            retriever = RAGRetriever(force_pytorch=True)
        elif backend == "faiss":
            retriever = RAGRetriever(force_pytorch=False)
        else:
            retriever = RAGRetriever()
        
        # Inicializar
        if not retriever.initialize() or not retriever.load_index():
            return {"error": "Falha na inicialização"}
        
        def execute_query(query: str) -> Dict[str, Any]:
            start_time = time.time()
            try:
                results = retriever.search(query, top_k=3)
                return {
                    "query": query[:30] + "...",
                    "time": time.time() - start_time,
                    "results_count": len(results),
                    "success": True
                }
            except Exception as e:
                return {
                    "query": query[:30] + "...",
                    "time": time.time() - start_time,
                    "error": str(e),
                    "success": False
                }
        
        # Executar consultas concorrentes
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(execute_query, query) for query in self.test_queries]
            concurrent_results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        total_time = time.time() - start_time
        
        # Analisar resultados
        successful = [r for r in concurrent_results if r.get("success", False)]
        failed = [r for r in concurrent_results if not r.get("success", False)]
        
        results = {
            "backend": "PyTorch" if retriever.use_pytorch else "FAISS",
            "max_workers": max_workers,
            "total_queries": len(self.test_queries),
            "successful_queries": len(successful),
            "failed_queries": len(failed),
            "total_time": total_time,
            "queries_per_second": len(self.test_queries) / total_time,
            "average_query_time": sum(r["time"] for r in successful) / len(successful) if successful else 0,
            "concurrent_results": concurrent_results
        }
        
        logger.info(f"[OK] Concorrência testada: {results['queries_per_second']:.2f} queries/s")
        return results
    
    def run_comprehensive_test(self) -> Dict[str, Any]:
        """
        Executa bateria completa de testes.
        
        Returns:
            Dict: Resultados completos
        """
        logger.info("🧪 Iniciando bateria completa de testes...")
        
        comprehensive_results = {
            "timestamp": time.time(),
            "backend_detection": None,
            "initialization_performance": None,
            "search_performance": {},
            "concurrent_performance": {},
            "summary": {}
        }
        
        try:
            # 1. Teste de detecção de backend
            comprehensive_results["backend_detection"] = self.test_backend_detection()
            
            # 2. Performance de inicialização
            comprehensive_results["initialization_performance"] = self.test_initialization_performance()
            
            # 3. Performance de busca (ambos backends se disponíveis)
            for backend in ["auto", "pytorch"]:
                try:
                    comprehensive_results["search_performance"][backend] = self.test_search_performance(backend)
                except Exception as e:
                    comprehensive_results["search_performance"][backend] = {"error": str(e)}
            
            # 4. Teste de concorrência
            for backend in ["auto", "pytorch"]:
                try:
                    comprehensive_results["concurrent_performance"][backend] = self.test_concurrent_queries(backend)
                except Exception as e:
                    comprehensive_results["concurrent_performance"][backend] = {"error": str(e)}
            
            # 5. Resumo
            comprehensive_results["summary"] = self._generate_summary(comprehensive_results)
            
            logger.info("[OK] Bateria completa de testes concluída")
            return comprehensive_results
            
        except Exception as e:
            logger.error(f"[ERROR] Erro na bateria de testes: {e}")
            comprehensive_results["error"] = str(e)
            return comprehensive_results
    
    def _generate_summary(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera resumo dos resultados.
        
        Args:
            results: Resultados dos testes
            
        Returns:
            Dict: Resumo
        """
        summary = {
            "recommended_backend": "auto",
            "performance_winner": None,
            "stability_assessment": "unknown",
            "recommendations": []
        }
        
        try:
            # Analisar performance de busca
            search_perf = results.get("search_performance", {})
            if "auto" in search_perf and "pytorch" in search_perf:
                auto_avg = search_perf["auto"].get("average_time", float('inf'))
                pytorch_avg = search_perf["pytorch"].get("average_time", float('inf'))
                
                if pytorch_avg < auto_avg:
                    summary["performance_winner"] = "pytorch"
                    summary["recommended_backend"] = "pytorch"
                else:
                    summary["performance_winner"] = "auto"
            
            # Analisar estabilidade
            concurrent_perf = results.get("concurrent_performance", {})
            if "auto" in concurrent_perf:
                auto_success_rate = concurrent_perf["auto"].get("successful_queries", 0) / concurrent_perf["auto"].get("total_queries", 1)
                if auto_success_rate > 0.95:
                    summary["stability_assessment"] = "excellent"
                elif auto_success_rate > 0.8:
                    summary["stability_assessment"] = "good"
                else:
                    summary["stability_assessment"] = "poor"
            
            # Gerar recomendações
            if summary["performance_winner"] == "pytorch":
                summary["recommendations"].append("PyTorch oferece melhor performance")
            
            if summary["stability_assessment"] == "excellent":
                summary["recommendations"].append("Sistema estável para produção")
            elif summary["stability_assessment"] == "poor":
                summary["recommendations"].append("Revisar configuração antes de produção")
            
        except Exception as e:
            summary["error"] = f"Erro ao gerar resumo: {e}"
        
        return summary

def main():
    """
    Função principal para executar os testes.
    """
    print("🧪 RAG Integration Tester")
    print("=" * 50)
    
    tester = RAGIntegrationTester()
    
    # Executar bateria completa
    results = tester.run_comprehensive_test()
    
    # Exibir resumo
    print("\n[EMOJI] RESUMO DOS TESTES")
    print("=" * 30)
    
    summary = results.get("summary", {})
    print(f"Backend Recomendado: {summary.get('recommended_backend', 'unknown')}")
    print(f"Melhor Performance: {summary.get('performance_winner', 'unknown')}")
    print(f"Estabilidade: {summary.get('stability_assessment', 'unknown')}")
    
    recommendations = summary.get("recommendations", [])
    if recommendations:
        print("\n[EMOJI] Recomendações:")
        for rec in recommendations:
            print(f"  • {rec}")
    
    # Salvar resultados detalhados
    import json
    results_file = Path("rag_integration_test_results.json")
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n[EMOJI] Resultados detalhados salvos em: {results_file}")
    print("\n[OK] Testes concluídos!")

if __name__ == "__main__":
    main()