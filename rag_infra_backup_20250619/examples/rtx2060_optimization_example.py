#!/usr/bin/env python3
"""
Exemplo de Uso das Otimizações RAG para RTX 2060

Este script demonstra como configurar e usar o sistema RAG otimizado
especificamente para placas RTX 2060, incluindo:
- Configurações de cache otimizadas
- Monitoramento de métricas
- Testes de carga
- Processamento em lote

Autor: Agente Backend Sênior
Data: 2024
"""

import asyncio
import json
import logging
import sys
import time
from pathlib import Path
from typing import List, Dict, Any

# Adicionar o diretório raiz ao path para importações
sys.path.append(str(Path(__file__).parent.parent.parent))

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Imports do sistema RAG
try:
    from rag_infra.core_logic.rag_retriever import RAGRetriever
    from rag_infra.config.rag_optimization_config import RAGOptimizationConfig
    from rag_infra.core_logic.rag_metrics_monitor import MetricsCollector, start_monitoring, stop_monitoring
    from rag_infra.tests.test_load_performance import RAGLoadTester, run_rtx2060_optimized_test
except ImportError as e:
    logger.error(f"Erro ao importar módulos RAG: {e}")
    logger.info("Certifique-se de que o sistema RAG está instalado corretamente")
    exit(1)


class RTX2060OptimizationDemo:
    """
    Demonstração das otimizações RAG para RTX 2060.
    """
    
    def __init__(self, data_dir: str = "rag_infra/data"):
        self.data_dir = Path(data_dir)
        self.config = None
        self.retriever = None
        self.metrics_monitor = None
        self.results_dir = Path("rag_infra/results")
        self.results_dir.mkdir(exist_ok=True)
    
    def setup_rtx2060_config(self) -> RAGOptimizationConfig:
        """
        Configura otimizações específicas para RTX 2060.
        """
        logger.info("🔧 Configurando otimizações para RTX 2060...")
        
        from rag_infra.config.rag_optimization_config import get_config_for_environment
        config = get_config_for_environment("rtx_2060_optimized")
        
        # Salvar configuração
        config_path = self.results_dir / 'rtx2060_config.json'
        config.save_to_file(str(config_path))
        
        logger.info(f"✅ Configuração RTX 2060 salva em: {config_path}")
        logger.info(f"📊 Cache TTL: {config.cache.ttl_seconds}s")
        logger.info(f"💾 Limite de memória: {config.cache.memory_limit_mb}MB")
        logger.info(f"📦 Tamanho do lote: {config.batch.default_batch_size}")
        
        return config
    
    def initialize_retriever(self, config: RAGOptimizationConfig) -> RAGRetriever:
        """
        Inicializa o retriever com otimizações.
        """
        logger.info("🚀 Inicializando RAG Retriever otimizado...")
        
        try:
            retriever = RAGRetriever(
                use_optimizations=True,
                cache_enabled=True,
                batch_size=config.batch.default_batch_size,
                force_pytorch=True  # Forçar PyTorch para RTX 2060
            )
            
            logger.info("✅ RAG Retriever inicializado com sucesso")
            return retriever
            
        except Exception as e:
            logger.error(f"❌ Erro ao inicializar retriever: {e}")
            raise
    
    def setup_monitoring(self) -> MetricsCollector:
        """
        Configura monitoramento de métricas.
        """
        logger.info("📊 Configurando monitoramento de métricas...")
        
        monitor = MetricsCollector(
            metrics_dir="rag_infra/metrics",
            collection_interval=30,
            retention_hours=24
        )
        
        # Iniciar monitoramento
        start_monitoring()
        
        logger.info("✅ Monitoramento configurado")
        return monitor
    
    def run_basic_queries(self, retriever: RAGRetriever, monitor: MetricsCollector) -> Dict[str, Any]:
        """
        Executa consultas básicas para testar o sistema.
        """
        logger.info("🔍 Executando consultas básicas...")
        
        test_queries = [
            "Como criar um currículo profissional?",
            "Dicas para entrevista de emprego",
            "Habilidades técnicas mais demandadas",
            "Como se preparar para mudança de carreira?",
            "Networking profissional efetivo"
        ]
        
        results = []
        start_time = time.time()
        
        for i, query in enumerate(test_queries, 1):
            logger.info(f"📝 Consulta {i}/{len(test_queries)}: {query[:30]}...")
            
            query_start = time.time()
            search_results = retriever.search(query, top_k=5)
            query_time = time.time() - query_start
            
            # Verificar cache hits
            cache_hits = sum(1 for r in search_results 
                           if r.metadata.get('cache_hit', False))
            
            result_info = {
                'query': query,
                'results_count': len(search_results),
                'response_time': query_time,
                'cache_hits': cache_hits,
                'cache_hit_rate': cache_hits / len(search_results) if search_results else 0
            }
            
            results.append(result_info)
            logger.info(f"⏱️  Tempo: {query_time:.3f}s, Resultados: {len(search_results)}, "
                       f"Cache hits: {cache_hits}")
        
        total_time = time.time() - start_time
        avg_time = total_time / len(test_queries)
        total_cache_hits = sum(r['cache_hits'] for r in results)
        total_results = sum(r['results_count'] for r in results)
        overall_cache_rate = total_cache_hits / total_results if total_results > 0 else 0
        
        summary = {
            'total_queries': len(test_queries),
            'total_time': total_time,
            'average_time': avg_time,
            'total_results': total_results,
            'cache_hit_rate': overall_cache_rate,
            'queries': results
        }
        
        logger.info(f"📊 Resumo: {len(test_queries)} consultas em {total_time:.2f}s "
                   f"(média: {avg_time:.3f}s), cache hit rate: {overall_cache_rate:.1%}")
        
        return summary
    
    def run_batch_test(self, retriever: RAGRetriever) -> Dict[str, Any]:
        """
        Testa processamento em lote.
        """
        logger.info("📦 Testando processamento em lote...")
        
        batch_queries = [
            "Estratégias de busca de emprego",
            "Desenvolvimento de soft skills",
            "Tendências do mercado de trabalho",
            "Certificações profissionais importantes",
            "Como negociar salário",
            "Trabalho remoto vs presencial",
            "Gestão de tempo no trabalho",
            "Liderança e gestão de equipes"
        ]
        
        start_time = time.time()
        batch_results = retriever.search_batch(batch_queries, top_k=3)
        batch_time = time.time() - start_time
        
        total_results = sum(len(results) for results in batch_results)
        avg_time_per_query = batch_time / len(batch_queries)
        
        # Analisar cache hits no lote
        total_cache_hits = 0
        for query_results in batch_results:
            for result in query_results:
                if result.metadata.get('cache_hit', False):
                    total_cache_hits += 1
        
        batch_cache_rate = total_cache_hits / total_results if total_results > 0 else 0
        
        summary = {
            'batch_size': len(batch_queries),
            'total_time': batch_time,
            'avg_time_per_query': avg_time_per_query,
            'total_results': total_results,
            'cache_hit_rate': batch_cache_rate,
            'queries_per_second': len(batch_queries) / batch_time
        }
        
        logger.info(f"📦 Lote processado: {len(batch_queries)} consultas em {batch_time:.2f}s "
                   f"({avg_time_per_query:.3f}s/consulta), QPS: {summary['queries_per_second']:.1f}")
        
        return summary
    
    def run_load_test(self) -> Dict[str, Any]:
        """
        Executa teste de carga otimizado para RTX 2060.
        """
        logger.info("🚀 Executando teste de carga RTX 2060...")
        
        try:
            results = run_rtx2060_optimized_test()
            
            logger.info(f"📊 Teste de carga concluído:")
            logger.info(f"   • QPS médio: {results.avg_qps:.1f}")
            logger.info(f"   • Tempo médio: {results.avg_response_time:.3f}s")
            logger.info(f"   • P95: {results.p95_response_time:.3f}s")
            logger.info(f"   • Cache hit rate: {results.cache_hit_rate:.1%}")
            logger.info(f"   • Taxa de erro: {results.error_rate:.1%}")
            
            return results.to_dict()
            
        except Exception as e:
            logger.error(f"❌ Erro no teste de carga: {e}")
            return {'error': str(e)}
    
    def save_results(self, results: Dict[str, Any], filename: str):
        """
        Salva resultados em arquivo JSON.
        """
        filepath = self.results_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False, default=str)
        
        logger.info(f"💾 Resultados salvos em: {filepath}")
    
    def run_complete_demo(self):
        """
        Executa demonstração completa das otimizações RTX 2060.
        """
        logger.info("🎯 Iniciando demonstração completa RTX 2060...")
        
        try:
            # 1. Configuração
            config = self.setup_rtx2060_config()
            
            # 2. Inicialização
            retriever = self.initialize_retriever(config)
            monitor = self.setup_monitoring()
            
            # 3. Testes básicos
            basic_results = self.run_basic_queries(retriever, monitor)
            self.save_results(basic_results, 'rtx2060_basic_queries.json')
            
            # 4. Teste em lote
            batch_results = self.run_batch_test(retriever)
            self.save_results(batch_results, 'rtx2060_batch_test.json')
            
            # 5. Teste de carga
            load_results = self.run_load_test()
            self.save_results(load_results, 'rtx2060_load_test.json')
            
            # 6. Métricas finais
            final_metrics = monitor.get_metrics_summary(24)  # Últimas 24 horas
            self.save_results(final_metrics, 'rtx2060_metrics_summary.json')
            
            # 7. Relatório final
            config_dict = {
                'cache': {
                    'ttl_seconds': config.cache.ttl_seconds,
                    'max_entries': config.cache.max_entries,
                    'memory_limit_mb': config.cache.memory_limit_mb
                },
                'batch': {
                    'default_batch_size': config.batch.default_batch_size,
                    'max_batch_size': config.batch.max_batch_size
                },
                'gpu': {
                    'memory_fraction': config.gpu.memory_fraction
                }
            }
            
            final_report = {
                'timestamp': time.time(),
                'config': config_dict,
                'basic_queries': basic_results,
                'batch_test': batch_results,
                'load_test': load_results,
                'metrics': final_metrics
            }
            
            self.save_results(final_report, 'rtx2060_complete_report.json')
            
            logger.info("🎉 Demonstração RTX 2060 concluída com sucesso!")
            logger.info(f"📁 Resultados disponíveis em: {self.results_dir}")
            
            return final_report
            
        except Exception as e:
            logger.error(f"❌ Erro durante demonstração: {e}")
            raise


def main():
    """
    Função principal para executar a demonstração.
    """
    print("🚀 Demonstração de Otimizações RAG para RTX 2060")
    print("=" * 50)
    
    demo = RTX2060OptimizationDemo()
    
    try:
        results = demo.run_complete_demo()
        
        print("\n✅ Demonstração concluída com sucesso!")
        print(f"📊 Resultados salvos em: {demo.results_dir}")
        
        # Exibir resumo
        if 'basic_queries' in results:
            basic = results['basic_queries']
            print(f"\n📈 Resumo de Performance:")
            print(f"   • Consultas básicas: {basic['total_queries']} em {basic['total_time']:.2f}s")
            print(f"   • Tempo médio: {basic['average_time']:.3f}s")
            print(f"   • Cache hit rate: {basic['cache_hit_rate']:.1%}")
        
        if 'batch_test' in results:
            batch = results['batch_test']
            print(f"   • Lote: {batch['batch_size']} consultas em {batch['total_time']:.2f}s")
            print(f"   • QPS: {batch['queries_per_second']:.1f}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erro durante execução: {e}")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)