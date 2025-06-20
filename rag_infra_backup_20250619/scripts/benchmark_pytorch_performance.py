#!/usr/bin/env python3
"""
Benchmark de Performance do PyTorch GPU Retriever

Testa e otimiza:
- Batch processing para múltiplas consultas
- Uso de memória GPU
- Cache persistente
- Latência comparativa
"""

import sys
import os
import time
import json
import torch
import numpy as np
from typing import List, Dict, Any, Tuple
from pathlib import Path
import concurrent.futures
import threading
from dataclasses import dataclass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pytorch_gpu_retriever import PyTorchGPURetriever

@dataclass
class BenchmarkResult:
    """Resultado de um benchmark."""
    test_name: str
    duration: float
    queries_per_second: float
    memory_used_mb: float
    gpu_utilization: float
    success_rate: float
    additional_metrics: Dict[str, Any]

class PyTorchPerformanceBenchmark:
    """
    Classe para benchmarks de performance do PyTorch GPU Retriever.
    """
    
    def __init__(self):
        self.test_queries = [
            "Como implementar autenticação JWT no FastAPI?",
            "Configurar banco de dados PostgreSQL com SQLAlchemy",
            "Implementar sistema de cache Redis distribuído",
            "Deploy de aplicação Python com Docker",
            "Monitoramento e logging estruturado",
            "Testes automatizados com pytest",
            "Arquitetura de microserviços",
            "Performance e otimização de queries",
            "Segurança em APIs REST",
            "Configuração de CI/CD",
            "Implementar WebSockets",
            "Gerenciamento de estado",
            "Validação de dados com Pydantic",
            "Middleware personalizado",
            "Rate limiting e throttling"
        ]
        
        self.results: List[BenchmarkResult] = []
    
    def _get_gpu_memory_usage(self) -> float:
        """
        Retorna uso de memória GPU em MB.
        
        Returns:
            float: Memória usada em MB
        """
        if torch.cuda.is_available():
            return torch.cuda.memory_allocated() / (1024 * 1024)
        return 0.0
    
    def _get_gpu_utilization(self) -> float:
        """
        Estima utilização da GPU (simplificado).
        
        Returns:
            float: Utilização estimada (0-100)
        """
        if torch.cuda.is_available():
            # Simplificado: baseado no uso de memória
            used = torch.cuda.memory_allocated()
            total = torch.cuda.max_memory_allocated()
            if total > 0:
                return (used / total) * 100
        return 0.0
    
    def benchmark_single_queries(self, retriever: PyTorchGPURetriever) -> BenchmarkResult:
        """
        Benchmark de consultas individuais sequenciais.
        
        Args:
            retriever: Retriever inicializado
            
        Returns:
            BenchmarkResult: Resultados do benchmark
        """
        print("🔍 Benchmark: Consultas Individuais Sequenciais")
        
        start_memory = self._get_gpu_memory_usage()
        start_time = time.time()
        
        successful_queries = 0
        individual_times = []
        
        for i, query in enumerate(self.test_queries):
            query_start = time.time()
            
            try:
                results = retriever.search(query, top_k=5)
                query_time = time.time() - query_start
                individual_times.append(query_time)
                successful_queries += 1
                
                print(f"  Query {i+1}/{len(self.test_queries)}: {query_time:.3f}s ({len(results)} resultados)")
                
            except Exception as e:
                print(f"  Query {i+1} falhou: {e}")
        
        total_time = time.time() - start_time
        end_memory = self._get_gpu_memory_usage()
        
        return BenchmarkResult(
            test_name="single_queries",
            duration=total_time,
            queries_per_second=successful_queries / total_time if total_time > 0 else 0,
            memory_used_mb=end_memory - start_memory,
            gpu_utilization=self._get_gpu_utilization(),
            success_rate=successful_queries / len(self.test_queries),
            additional_metrics={
                "individual_times": individual_times,
                "avg_query_time": np.mean(individual_times) if individual_times else 0,
                "min_query_time": np.min(individual_times) if individual_times else 0,
                "max_query_time": np.max(individual_times) if individual_times else 0,
                "std_query_time": np.std(individual_times) if individual_times else 0
            }
        )
    
    def benchmark_batch_queries(self, retriever: PyTorchGPURetriever, batch_size: int = 5) -> BenchmarkResult:
        """
        Benchmark de consultas em batch (simulado com threading).
        
        Args:
            retriever: Retriever inicializado
            batch_size: Tamanho do batch
            
        Returns:
            BenchmarkResult: Resultados do benchmark
        """
        print(f"🚀 Benchmark: Consultas em Batch (batch_size={batch_size})")
        
        start_memory = self._get_gpu_memory_usage()
        start_time = time.time()
        
        def execute_query(query: str) -> Tuple[bool, float, int]:
            query_start = time.time()
            try:
                results = retriever.search(query, top_k=5)
                return True, time.time() - query_start, len(results)
            except Exception:
                return False, time.time() - query_start, 0
        
        successful_queries = 0
        batch_times = []
        
        # Processar em batches
        for i in range(0, len(self.test_queries), batch_size):
            batch = self.test_queries[i:i+batch_size]
            batch_start = time.time()
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=batch_size) as executor:
                futures = [executor.submit(execute_query, query) for query in batch]
                batch_results = [future.result() for future in concurrent.futures.as_completed(futures)]
            
            batch_time = time.time() - batch_start
            batch_times.append(batch_time)
            
            batch_success = sum(1 for success, _, _ in batch_results if success)
            successful_queries += batch_success
            
            print(f"  Batch {i//batch_size + 1}: {batch_time:.3f}s ({batch_success}/{len(batch)} sucessos)")
        
        total_time = time.time() - start_time
        end_memory = self._get_gpu_memory_usage()
        
        return BenchmarkResult(
            test_name=f"batch_queries_{batch_size}",
            duration=total_time,
            queries_per_second=successful_queries / total_time if total_time > 0 else 0,
            memory_used_mb=end_memory - start_memory,
            gpu_utilization=self._get_gpu_utilization(),
            success_rate=successful_queries / len(self.test_queries),
            additional_metrics={
                "batch_size": batch_size,
                "batch_times": batch_times,
                "avg_batch_time": np.mean(batch_times) if batch_times else 0,
                "total_batches": len(batch_times)
            }
        )
    
    def benchmark_concurrent_queries(self, retriever: PyTorchGPURetriever, max_workers: int = 10) -> BenchmarkResult:
        """
        Benchmark de consultas concorrentes.
        
        Args:
            retriever: Retriever inicializado
            max_workers: Número máximo de workers
            
        Returns:
            BenchmarkResult: Resultados do benchmark
        """
        print(f"⚡ Benchmark: Consultas Concorrentes (workers={max_workers})")
        
        start_memory = self._get_gpu_memory_usage()
        start_time = time.time()
        
        def execute_query(query: str) -> Dict[str, Any]:
            query_start = time.time()
            try:
                results = retriever.search(query, top_k=5)
                return {
                    "success": True,
                    "time": time.time() - query_start,
                    "results_count": len(results),
                    "query": query[:30] + "..."
                }
            except Exception as e:
                return {
                    "success": False,
                    "time": time.time() - query_start,
                    "error": str(e),
                    "query": query[:30] + "..."
                }
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(execute_query, query) for query in self.test_queries]
            concurrent_results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        total_time = time.time() - start_time
        end_memory = self._get_gpu_memory_usage()
        
        successful_queries = sum(1 for r in concurrent_results if r["success"])
        query_times = [r["time"] for r in concurrent_results if r["success"]]
        
        return BenchmarkResult(
            test_name=f"concurrent_queries_{max_workers}",
            duration=total_time,
            queries_per_second=successful_queries / total_time if total_time > 0 else 0,
            memory_used_mb=end_memory - start_memory,
            gpu_utilization=self._get_gpu_utilization(),
            success_rate=successful_queries / len(self.test_queries),
            additional_metrics={
                "max_workers": max_workers,
                "concurrent_results": concurrent_results,
                "avg_concurrent_time": np.mean(query_times) if query_times else 0,
                "min_concurrent_time": np.min(query_times) if query_times else 0,
                "max_concurrent_time": np.max(query_times) if query_times else 0
            }
        )
    
    def benchmark_cache_performance(self, retriever: PyTorchGPURetriever) -> BenchmarkResult:
        """
        Benchmark de performance do cache.
        
        Args:
            retriever: Retriever inicializado
            
        Returns:
            BenchmarkResult: Resultados do benchmark
        """
        print("💾 Benchmark: Performance do Cache")
        
        # Limpar cache
        retriever.clear_cache()
        
        start_memory = self._get_gpu_memory_usage()
        start_time = time.time()
        
        # Primeira execução (sem cache)
        first_run_times = []
        for query in self.test_queries[:5]:  # Usar apenas 5 queries para teste
            query_start = time.time()
            try:
                retriever.search(query, top_k=5)
                first_run_times.append(time.time() - query_start)
            except Exception:
                pass
        
        # Segunda execução (com cache)
        second_run_times = []
        for query in self.test_queries[:5]:
            query_start = time.time()
            try:
                retriever.search(query, top_k=5)
                second_run_times.append(time.time() - query_start)
            except Exception:
                pass
        
        total_time = time.time() - start_time
        end_memory = self._get_gpu_memory_usage()
        
        # Calcular speedup do cache
        cache_speedup = 0
        if first_run_times and second_run_times:
            avg_first = np.mean(first_run_times)
            avg_second = np.mean(second_run_times)
            if avg_second > 0:
                cache_speedup = avg_first / avg_second
        
        return BenchmarkResult(
            test_name="cache_performance",
            duration=total_time,
            queries_per_second=len(first_run_times + second_run_times) / total_time if total_time > 0 else 0,
            memory_used_mb=end_memory - start_memory,
            gpu_utilization=self._get_gpu_utilization(),
            success_rate=1.0,  # Assumindo sucesso se chegou até aqui
            additional_metrics={
                "first_run_times": first_run_times,
                "second_run_times": second_run_times,
                "avg_first_run": np.mean(first_run_times) if first_run_times else 0,
                "avg_second_run": np.mean(second_run_times) if second_run_times else 0,
                "cache_speedup": cache_speedup,
                "cache_hit_improvement": f"{((cache_speedup - 1) * 100):.1f}%" if cache_speedup > 1 else "0%"
            }
        )
    
    def benchmark_memory_optimization(self, retriever: PyTorchGPURetriever) -> BenchmarkResult:
        """
        Benchmark de otimização de memória.
        
        Args:
            retriever: Retriever inicializado
            
        Returns:
            BenchmarkResult: Resultados do benchmark
        """
        print("🧠 Benchmark: Otimização de Memória")
        
        start_time = time.time()
        
        # Medir memória inicial
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        initial_memory = self._get_gpu_memory_usage()
        
        # Executar consultas e monitorar memória
        memory_snapshots = []
        
        for i, query in enumerate(self.test_queries):
            try:
                retriever.search(query, top_k=5)
                current_memory = self._get_gpu_memory_usage()
                memory_snapshots.append({
                    "query_index": i,
                    "memory_mb": current_memory,
                    "memory_delta": current_memory - initial_memory
                })
            except Exception:
                pass
        
        # Limpar cache e medir memória final
        retriever.clear_cache()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        final_memory = self._get_gpu_memory_usage()
        
        total_time = time.time() - start_time
        
        # Calcular estatísticas de memória
        memory_deltas = [s["memory_delta"] for s in memory_snapshots]
        peak_memory = max([s["memory_mb"] for s in memory_snapshots]) if memory_snapshots else initial_memory
        
        return BenchmarkResult(
            test_name="memory_optimization",
            duration=total_time,
            queries_per_second=len(memory_snapshots) / total_time if total_time > 0 else 0,
            memory_used_mb=peak_memory - initial_memory,
            gpu_utilization=self._get_gpu_utilization(),
            success_rate=len(memory_snapshots) / len(self.test_queries),
            additional_metrics={
                "initial_memory_mb": initial_memory,
                "peak_memory_mb": peak_memory,
                "final_memory_mb": final_memory,
                "memory_snapshots": memory_snapshots,
                "avg_memory_delta": np.mean(memory_deltas) if memory_deltas else 0,
                "max_memory_delta": np.max(memory_deltas) if memory_deltas else 0,
                "memory_efficiency": (final_memory - initial_memory) / (peak_memory - initial_memory) if peak_memory > initial_memory else 1.0
            }
        )
    
    def run_comprehensive_benchmark(self) -> Dict[str, Any]:
        """
        Executa benchmark completo.
        
        Returns:
            Dict: Resultados completos
        """
        print("🏁 Iniciando Benchmark Completo de Performance")
        print("=" * 50)
        
        # Inicializar retriever
        print("🔧 Inicializando PyTorch GPU Retriever...")
        retriever = PyTorchGPURetriever(force_cpu=False)  # Usar GPU se disponível
        
        if not retriever.initialize():
            print("❌ Falha ao inicializar retriever")
            return {"error": "Falha na inicialização"}
        
        if not retriever.load_index():
            print("❌ Falha ao carregar índice")
            return {"error": "Falha ao carregar índice"}
        
        print(f"✅ Retriever inicializado: {retriever.get_index_info()}")
        
        # Executar benchmarks
        benchmarks = [
            lambda: self.benchmark_single_queries(retriever),
            lambda: self.benchmark_batch_queries(retriever, batch_size=3),
            lambda: self.benchmark_batch_queries(retriever, batch_size=5),
            lambda: self.benchmark_concurrent_queries(retriever, max_workers=5),
            lambda: self.benchmark_concurrent_queries(retriever, max_workers=10),
            lambda: self.benchmark_cache_performance(retriever),
            lambda: self.benchmark_memory_optimization(retriever)
        ]
        
        results = []
        for i, benchmark in enumerate(benchmarks):
            try:
                print(f"\n--- Benchmark {i+1}/{len(benchmarks)} ---")
                result = benchmark()
                results.append(result)
                self.results.append(result)
                
                print(f"✅ {result.test_name}: {result.queries_per_second:.2f} q/s, {result.success_rate*100:.1f}% sucesso")
                
            except Exception as e:
                print(f"❌ Erro no benchmark {i+1}: {e}")
                results.append(None)
        
        # Gerar relatório
        return self._generate_performance_report(results)
    
    def _generate_performance_report(self, results: List[BenchmarkResult]) -> Dict[str, Any]:
        """
        Gera relatório de performance.
        
        Args:
            results: Lista de resultados
            
        Returns:
            Dict: Relatório completo
        """
        valid_results = [r for r in results if r is not None]
        
        if not valid_results:
            return {"error": "Nenhum resultado válido"}
        
        # Encontrar melhor performance
        best_qps = max(valid_results, key=lambda x: x.queries_per_second)
        best_memory = min(valid_results, key=lambda x: x.memory_used_mb)
        best_success = max(valid_results, key=lambda x: x.success_rate)
        
        # Calcular médias
        avg_qps = np.mean([r.queries_per_second for r in valid_results])
        avg_memory = np.mean([r.memory_used_mb for r in valid_results])
        avg_success = np.mean([r.success_rate for r in valid_results])
        
        return {
            "timestamp": time.time(),
            "total_benchmarks": len(results),
            "successful_benchmarks": len(valid_results),
            "summary": {
                "avg_queries_per_second": avg_qps,
                "avg_memory_usage_mb": avg_memory,
                "avg_success_rate": avg_success,
                "best_performance": {
                    "queries_per_second": {
                        "test": best_qps.test_name,
                        "value": best_qps.queries_per_second
                    },
                    "memory_efficiency": {
                        "test": best_memory.test_name,
                        "value": best_memory.memory_used_mb
                    },
                    "reliability": {
                        "test": best_success.test_name,
                        "value": best_success.success_rate
                    }
                }
            },
            "detailed_results": [
                {
                    "test_name": r.test_name,
                    "duration": r.duration,
                    "queries_per_second": r.queries_per_second,
                    "memory_used_mb": r.memory_used_mb,
                    "gpu_utilization": r.gpu_utilization,
                    "success_rate": r.success_rate,
                    "additional_metrics": r.additional_metrics
                } for r in valid_results
            ],
            "recommendations": self._generate_recommendations(valid_results)
        }
    
    def _generate_recommendations(self, results: List[BenchmarkResult]) -> List[str]:
        """
        Gera recomendações baseadas nos resultados.
        
        Args:
            results: Lista de resultados
            
        Returns:
            List[str]: Lista de recomendações
        """
        recommendations = []
        
        if not results:
            return ["Não foi possível gerar recomendações"]
        
        # Analisar performance
        qps_values = [r.queries_per_second for r in results]
        max_qps = max(qps_values)
        
        # Encontrar melhor estratégia
        best_result = max(results, key=lambda x: x.queries_per_second)
        
        if "batch" in best_result.test_name:
            batch_size = best_result.additional_metrics.get("batch_size", "unknown")
            recommendations.append(f"Usar processamento em batch (tamanho {batch_size}) para melhor performance")
        
        if "concurrent" in best_result.test_name:
            workers = best_result.additional_metrics.get("max_workers", "unknown")
            recommendations.append(f"Usar {workers} workers concorrentes para máxima throughput")
        
        # Analisar cache
        cache_results = [r for r in results if "cache" in r.test_name]
        if cache_results:
            cache_result = cache_results[0]
            speedup = cache_result.additional_metrics.get("cache_speedup", 1)
            if speedup > 2:
                recommendations.append(f"Cache oferece {speedup:.1f}x speedup - implementar cache persistente")
        
        # Analisar memória
        memory_values = [r.memory_used_mb for r in results]
        if max(memory_values) > 1000:  # > 1GB
            recommendations.append("Considerar otimizações de memória para reduzir uso de GPU")
        
        # Analisar estabilidade
        success_rates = [r.success_rate for r in results]
        min_success = min(success_rates)
        if min_success < 0.9:
            recommendations.append("Melhorar tratamento de erros para aumentar estabilidade")
        
        return recommendations

def main():
    """
    Função principal.
    """
    print("🚀 PyTorch GPU Retriever Performance Benchmark")
    print("=" * 55)
    
    benchmark = PyTorchPerformanceBenchmark()
    
    # Executar benchmark completo
    results = benchmark.run_comprehensive_benchmark()
    
    # Salvar resultados
    results_file = Path("pytorch_performance_benchmark.json")
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Exibir resumo
    if "error" not in results:
        print("\n📊 RESUMO DE PERFORMANCE")
        print("=" * 30)
        
        summary = results["summary"]
        print(f"Queries/segundo médio: {summary['avg_queries_per_second']:.2f}")
        print(f"Uso de memória médio: {summary['avg_memory_usage_mb']:.1f} MB")
        print(f"Taxa de sucesso média: {summary['avg_success_rate']*100:.1f}%")
        
        print("\n🏆 MELHORES RESULTADOS")
        best = summary["best_performance"]
        print(f"Melhor QPS: {best['queries_per_second']['value']:.2f} ({best['queries_per_second']['test']})")
        print(f"Menor memória: {best['memory_efficiency']['value']:.1f} MB ({best['memory_efficiency']['test']})")
        print(f"Maior confiabilidade: {best['reliability']['value']*100:.1f}% ({best['reliability']['test']})")
        
        print("\n💡 RECOMENDAÇÕES")
        for rec in results["recommendations"]:
            print(f"  • {rec}")
    
    print(f"\n📄 Resultados detalhados salvos em: {results_file}")
    print("\n✅ Benchmark concluído!")

if __name__ == "__main__":
    main()