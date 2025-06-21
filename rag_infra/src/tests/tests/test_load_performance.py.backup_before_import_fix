# -*- coding: utf-8 -*-
"""
Teste de Carga e Performance RAG - Recoloca.ai

Implementa testes de carga para validar performance do sistema RAG
em cenários de produção com múltiplas consultas simultâneas.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import asyncio
import time
import threading
import statistics
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, asdict
from pathlib import Path
import random

# Importar componentes RAG
try:
    from rag_infra.core_logic.rag_retriever import RAGRetriever
    from rag_infra.core_logic.rag_metrics_monitor import metrics_collector, start_monitoring, stop_monitoring
    from rag_infra.core_logic.rag_metrics_integration import apply_metrics_tracking
    from rag_infra.config.rag_optimization_config import RAGOptimizationConfig
except ImportError as e:
    print(f"Aviso: Não foi possível importar componentes RAG: {e}")
    print("Executando em modo de simulação")
    RAGRetriever = None

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class LoadTestConfig:
    """Configuração para teste de carga."""
    concurrent_users: int = 10
    queries_per_user: int = 20
    ramp_up_time: int = 30  # segundos
    test_duration: int = 300  # segundos
    query_delay_min: float = 0.1  # segundos
    query_delay_max: float = 2.0  # segundos
    use_cache: bool = True
    batch_size: int = 5
    timeout_per_query: float = 10.0  # segundos

@dataclass
class QueryResult:
    """Resultado de uma consulta individual."""
    query_id: str
    user_id: int
    query_text: str
    response_time: float
    success: bool
    error_message: Optional[str] = None
    cache_hit: bool = False
    timestamp: float = 0.0
    documents_count: int = 0

@dataclass
class LoadTestResults:
    """Resultados do teste de carga."""
    config: LoadTestConfig
    total_queries: int
    successful_queries: int
    failed_queries: int
    avg_response_time: float
    p50_response_time: float
    p95_response_time: float
    p99_response_time: float
    min_response_time: float
    max_response_time: float
    queries_per_second: float
    cache_hit_rate: float
    error_rate: float
    test_duration: float
    errors_by_type: Dict[str, int]
    response_times: List[float]
    timestamps: List[float]

class LoadTestSimulator:
    """Simulador para testes de carga quando componentes RAG não estão disponíveis."""
    
    def __init__(self):
        self.cache = {}
        self.cache_hit_rate = 0.7  # 70% de cache hits
    
    def search(self, query: str, use_cache: bool = True) -> Dict[str, Any]:
        """Simula uma consulta RAG.
        
        Args:
            query: Texto da consulta
            use_cache: Se deve usar cache
            
        Returns:
            Resultado simulado
        """
        # Simular tempo de processamento
        base_time = random.uniform(0.1, 0.8)
        
        # Verificar cache
        cache_hit = False
        if use_cache and query in self.cache:
            if random.random() < self.cache_hit_rate:
                cache_hit = True
                base_time *= 0.1  # Cache é muito mais rápido
        
        # Simular processamento
        time.sleep(base_time)
        
        # Adicionar ao cache
        if use_cache and not cache_hit:
            self.cache[query] = True
        
        # Simular falhas ocasionais
        if random.random() < 0.02:  # 2% de falhas
            raise Exception("Erro simulado de rede")
        
        return {
            "results": [f"Documento {i}" for i in range(random.randint(1, 5))],
            "metadata": {
                "cache_hit": cache_hit,
                "embedding_time": random.uniform(10, 50),
                "retrieval_time": random.uniform(20, 100),
                "documents_count": random.randint(1, 5)
            }
        }

class RAGLoadTester:
    """Testador de carga para sistema RAG."""
    
    def __init__(self, config: LoadTestConfig, retriever: Optional[Any] = None):
        """Inicializa o testador de carga.
        
        Args:
            config: Configuração do teste
            retriever: Instância do retriever (opcional)
        """
        self.config = config
        self.retriever = retriever or LoadTestSimulator()
        
        # Aplicar rastreamento de métricas se disponível
        if hasattr(self.retriever, 'search') and 'apply_metrics_tracking' in globals():
            self.retriever = apply_metrics_tracking(self.retriever)
        
        # Resultados
        self.results: List[QueryResult] = []
        self.start_time = 0.0
        self.end_time = 0.0
        
        # Controle de execução
        self._stop_event = threading.Event()
        
        # Consultas de exemplo
        self.sample_queries = [
            "Como melhorar meu currículo?",
            "Quais são as melhores práticas para entrevistas?",
            "Como me preparar para uma mudança de carreira?",
            "Dicas para networking profissional",
            "Como negociar salário?",
            "Habilidades mais demandadas no mercado",
            "Como se destacar no LinkedIn?",
            "Preparação para entrevistas técnicas",
            "Como lidar com ansiedade em entrevistas?",
            "Estratégias para busca de emprego",
            "Como escrever uma carta de apresentação?",
            "Dicas para primeiro emprego",
            "Como fazer transição de carreira?",
            "Importância do desenvolvimento contínuo",
            "Como construir um portfólio profissional?"
        ]
    
    def run_load_test(self) -> LoadTestResults:
        """Executa o teste de carga.
        
        Returns:
            Resultados do teste
        """
        logger.info(f"Iniciando teste de carga: {self.config.concurrent_users} usuários, "
                   f"{self.config.queries_per_user} consultas por usuário")
        
        # Iniciar monitoramento se disponível
        if 'start_monitoring' in globals():
            start_monitoring()
        
        self.start_time = time.time()
        
        try:
            # Executar teste com threads
            with ThreadPoolExecutor(max_workers=self.config.concurrent_users) as executor:
                # Criar tarefas para cada usuário
                futures = []
                
                for user_id in range(self.config.concurrent_users):
                    # Calcular delay de ramp-up
                    ramp_delay = (user_id * self.config.ramp_up_time) / self.config.concurrent_users
                    
                    future = executor.submit(self._simulate_user, user_id, ramp_delay)
                    futures.append(future)
                
                # Aguardar conclusão de todas as tarefas
                for future in as_completed(futures):
                    try:
                        user_results = future.result()
                        self.results.extend(user_results)
                    except Exception as e:
                        logger.error(f"Erro em thread de usuário: {e}")
        
        finally:
            self.end_time = time.time()
            
            # Parar monitoramento se disponível
            if 'stop_monitoring' in globals():
                stop_monitoring()
        
        # Calcular e retornar resultados
        return self._calculate_results()
    
    def _simulate_user(self, user_id: int, ramp_delay: float) -> List[QueryResult]:
        """Simula um usuário fazendo consultas.
        
        Args:
            user_id: ID do usuário
            ramp_delay: Delay inicial para ramp-up
            
        Returns:
            Lista de resultados das consultas
        """
        user_results = []
        
        # Aguardar ramp-up
        time.sleep(ramp_delay)
        
        logger.info(f"Usuário {user_id} iniciado")
        
        for query_num in range(self.config.queries_per_user):
            if self._stop_event.is_set():
                break
            
            # Verificar timeout do teste
            if time.time() - self.start_time > self.config.test_duration:
                break
            
            # Executar consulta
            result = self._execute_query(user_id, query_num)
            user_results.append(result)
            
            # Delay entre consultas
            delay = random.uniform(self.config.query_delay_min, self.config.query_delay_max)
            time.sleep(delay)
        
        logger.info(f"Usuário {user_id} concluído: {len(user_results)} consultas")
        return user_results
    
    def _execute_query(self, user_id: int, query_num: int) -> QueryResult:
        """Executa uma consulta individual.
        
        Args:
            user_id: ID do usuário
            query_num: Número da consulta
            
        Returns:
            Resultado da consulta
        """
        query_id = f"user_{user_id}_query_{query_num}"
        query_text = random.choice(self.sample_queries)
        
        start_time = time.time()
        
        try:
            # Executar consulta
            result = self.retriever.search(query_text, use_cache=self.config.use_cache)
            
            response_time = (time.time() - start_time) * 1000  # ms
            
            # Extrair metadados
            cache_hit = False
            documents_count = 0
            
            if isinstance(result, dict) and 'metadata' in result:
                metadata = result['metadata']
                cache_hit = metadata.get('cache_hit', False)
                documents_count = metadata.get('documents_count', 0)
            
            return QueryResult(
                query_id=query_id,
                user_id=user_id,
                query_text=query_text,
                response_time=response_time,
                success=True,
                cache_hit=cache_hit,
                timestamp=start_time,
                documents_count=documents_count
            )
        
        except Exception as e:
            response_time = (time.time() - start_time) * 1000  # ms
            
            return QueryResult(
                query_id=query_id,
                user_id=user_id,
                query_text=query_text,
                response_time=response_time,
                success=False,
                error_message=str(e),
                timestamp=start_time
            )
    
    def _calculate_results(self) -> LoadTestResults:
        """Calcula os resultados finais do teste.
        
        Returns:
            Resultados calculados
        """
        if not self.results:
            raise ValueError("Nenhum resultado disponível")
        
        # Filtrar resultados bem-sucedidos
        successful_results = [r for r in self.results if r.success]
        failed_results = [r for r in self.results if not r.success]
        
        # Calcular métricas de tempo de resposta
        response_times = [r.response_time for r in successful_results]
        
        if response_times:
            avg_response_time = statistics.mean(response_times)
            p50_response_time = statistics.median(response_times)
            p95_response_time = self._percentile(response_times, 95)
            p99_response_time = self._percentile(response_times, 99)
            min_response_time = min(response_times)
            max_response_time = max(response_times)
        else:
            avg_response_time = p50_response_time = p95_response_time = p99_response_time = 0
            min_response_time = max_response_time = 0
        
        # Calcular taxa de cache hit
        cache_hits = sum(1 for r in successful_results if r.cache_hit)
        cache_hit_rate = cache_hits / len(successful_results) if successful_results else 0
        
        # Calcular QPS
        test_duration = self.end_time - self.start_time
        queries_per_second = len(self.results) / test_duration if test_duration > 0 else 0
        
        # Agrupar erros por tipo
        errors_by_type = {}
        for result in failed_results:
            error_type = type(Exception(result.error_message)).__name__ if result.error_message else "Unknown"
            errors_by_type[error_type] = errors_by_type.get(error_type, 0) + 1
        
        # Calcular taxa de erro
        error_rate = len(failed_results) / len(self.results) if self.results else 0
        
        # Extrair timestamps
        timestamps = [r.timestamp for r in self.results]
        
        return LoadTestResults(
            config=self.config,
            total_queries=len(self.results),
            successful_queries=len(successful_results),
            failed_queries=len(failed_results),
            avg_response_time=avg_response_time,
            p50_response_time=p50_response_time,
            p95_response_time=p95_response_time,
            p99_response_time=p99_response_time,
            min_response_time=min_response_time,
            max_response_time=max_response_time,
            queries_per_second=queries_per_second,
            cache_hit_rate=cache_hit_rate,
            error_rate=error_rate,
            test_duration=test_duration,
            errors_by_type=errors_by_type,
            response_times=response_times,
            timestamps=timestamps
        )
    
    def _percentile(self, data: List[float], percentile: int) -> float:
        """Calcula percentil dos dados.
        
        Args:
            data: Lista de valores
            percentile: Percentil desejado (0-100)
            
        Returns:
            Valor do percentil
        """
        if not data:
            return 0.0
        
        sorted_data = sorted(data)
        index = int((percentile / 100) * len(sorted_data))
        return sorted_data[min(index, len(sorted_data) - 1)]
    
    def stop_test(self):
        """Para o teste de carga."""
        self._stop_event.set()
        logger.info("Parando teste de carga...")

def run_rtx2060_optimized_test() -> LoadTestResults:
    """Executa teste otimizado para RTX 2060.
    
    Returns:
        Resultados do teste
    """
    config = LoadTestConfig(
        concurrent_users=8,  # Otimizado para RTX 2060
        queries_per_user=15,
        ramp_up_time=20,
        test_duration=180,
        query_delay_min=0.2,
        query_delay_max=1.5,
        use_cache=True,
        batch_size=4,
        timeout_per_query=8.0
    )
    
    # Tentar usar retriever real se disponível
    retriever = None
    if RAGRetriever:
        try:
            # Configurar para RTX 2060
            retriever = RAGRetriever(
                use_optimizations=True,
                cache_enabled=True,
                batch_size=4
            )
        except Exception as e:
            logger.warning(f"Não foi possível inicializar RAGRetriever: {e}")
            logger.info("Usando simulador")
    
    tester = RAGLoadTester(config, retriever)
    return tester.run_load_test()

def export_results(results: LoadTestResults, output_dir: str = "load_test_results"):
    """Exporta resultados do teste para arquivos.
    
    Args:
        results: Resultados do teste
        output_dir: Diretório de saída
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    timestamp = int(time.time())
    
    # Exportar resumo JSON
    summary_file = output_path / f"load_test_summary_{timestamp}.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        # Converter para dict, excluindo listas grandes
        summary_dict = asdict(results)
        summary_dict.pop('response_times', None)
        summary_dict.pop('timestamps', None)
        
        json.dump(summary_dict, f, indent=2, ensure_ascii=False)
    
    # Exportar dados detalhados
    detailed_file = output_path / f"load_test_detailed_{timestamp}.json"
    with open(detailed_file, 'w', encoding='utf-8') as f:
        json.dump(asdict(results), f, indent=2, ensure_ascii=False)
    
    logger.info(f"Resultados exportados para {output_path}")
    logger.info(f"Resumo: {summary_file}")
    logger.info(f"Detalhado: {detailed_file}")

def print_results_summary(results: LoadTestResults):
    """Imprime resumo dos resultados.
    
    Args:
        results: Resultados do teste
    """
    print("\n" + "="*60)
    print("RESUMO DO TESTE DE CARGA RAG")
    print("="*60)
    
    print(f"\n📊 CONFIGURAÇÃO:")
    print(f"   Usuários Simultâneos: {results.config.concurrent_users}")
    print(f"   Consultas por Usuário: {results.config.queries_per_user}")
    print(f"   Duração do Teste: {results.test_duration:.1f}s")
    print(f"   Cache Habilitado: {results.config.use_cache}")
    
    print(f"\n📈 RESULTADOS GERAIS:")
    print(f"   Total de Consultas: {results.total_queries}")
    print(f"   Consultas Bem-sucedidas: {results.successful_queries}")
    print(f"   Consultas Falharam: {results.failed_queries}")
    print(f"   Taxa de Erro: {results.error_rate:.2%}")
    print(f"   Consultas por Segundo: {results.queries_per_second:.2f}")
    
    print(f"\n⚡ PERFORMANCE:")
    print(f"   Tempo Médio de Resposta: {results.avg_response_time:.2f}ms")
    print(f"   Mediana (P50): {results.p50_response_time:.2f}ms")
    print(f"   P95: {results.p95_response_time:.2f}ms")
    print(f"   P99: {results.p99_response_time:.2f}ms")
    print(f"   Mínimo: {results.min_response_time:.2f}ms")
    print(f"   Máximo: {results.max_response_time:.2f}ms")
    
    print(f"\n🎯 CACHE:")
    print(f"   Taxa de Cache Hit: {results.cache_hit_rate:.2%}")
    
    if results.errors_by_type:
        print(f"\n❌ ERROS POR TIPO:")
        for error_type, count in results.errors_by_type.items():
            print(f"   {error_type}: {count}")
    
    # Avaliação da performance
    print(f"\n🎯 AVALIAÇÃO:")
    
    if results.avg_response_time < 500:
        print("   ✅ Tempo de resposta: EXCELENTE (<500ms)")
    elif results.avg_response_time < 1000:
        print("   ✅ Tempo de resposta: BOM (<1000ms)")
    elif results.avg_response_time < 2000:
        print("   ⚠️  Tempo de resposta: ACEITÁVEL (<2000ms)")
    else:
        print("   ❌ Tempo de resposta: PRECISA MELHORAR (>2000ms)")
    
    if results.error_rate < 0.01:
        print("   ✅ Taxa de erro: EXCELENTE (<1%)")
    elif results.error_rate < 0.05:
        print("   ✅ Taxa de erro: BOA (<5%)")
    else:
        print("   ❌ Taxa de erro: ALTA (>5%)")
    
    if results.cache_hit_rate > 0.7:
        print("   ✅ Cache hit rate: EXCELENTE (>70%)")
    elif results.cache_hit_rate > 0.5:
        print("   ✅ Cache hit rate: BOA (>50%)")
    else:
        print("   ⚠️  Cache hit rate: PODE MELHORAR (<50%)")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    print("=== Teste de Carga RAG - Recoloca.ai ===")
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        # Executar teste otimizado para RTX 2060
        print("\nExecutando teste de carga otimizado para RTX 2060...")
        results = run_rtx2060_optimized_test()
        
        # Mostrar resultados
        print_results_summary(results)
        
        # Exportar resultados
        export_results(results)
        
    except KeyboardInterrupt:
        print("\nTeste interrompido pelo usuário")
    except Exception as e:
        logger.error(f"Erro durante teste de carga: {e}")
        raise