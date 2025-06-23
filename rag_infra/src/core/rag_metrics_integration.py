# -*- coding: utf-8 -*-
"""
Integração de Métricas RAG - Recoloca.ai

Conecta o sistema de monitoramento de métricas com o otimizador RAG.
Implementa hooks para coleta automática de métricas durante consultas RAG.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import time
import logging
import functools
from typing import Dict, Any, Optional, Callable, List, Union
from pathlib import Path
import json

# Importar componentes RAG
from .rag_metrics_monitor import metrics_collector, start_monitoring
from .rag_optimization_config import RAGOptimizationConfig

# Configurar logging
logger = logging.getLogger(__name__)

class RAGMetricsIntegration:
    """Integração entre o sistema de métricas e o RAG Retriever."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Inicializa a integração de métricas.
        
        Args:
            config_path: Caminho para arquivo de configuração
        """
        # Carregar configuração
        self.config = RAGOptimizationConfig.load(config_path) if config_path else RAGOptimizationConfig()
        
        # Iniciar monitoramento se configurado
        if self.config.monitoring.enabled:
            start_monitoring()
            logger.info("Monitoramento de métricas RAG iniciado")
        
        # Estatísticas de integração
        self.integration_stats = {
            "decorated_functions": 0,
            "queries_tracked": 0,
            "batch_queries_tracked": 0,
            "errors": 0
        }
    
    def track_query(self, func: Callable) -> Callable:
        """Decorador para rastrear métricas de consultas RAG.
        
        Args:
            func: Função a ser decorada (normalmente search ou similar)
            
        Returns:
            Função decorada com rastreamento de métricas
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Verificar se o monitoramento está ativo
            if not self.config.monitoring.enabled:
                return func(*args, **kwargs)
            
            # Registrar início da consulta
            start_time = time.time()
            cache_hit = False
            
            try:
                # Verificar se há informação de cache nos kwargs
                if 'use_cache' in kwargs and not kwargs.get('use_cache'):
                    cache_hit = False
                
                # Executar função original
                result = func(*args, **kwargs)
                
                # Tentar detectar cache hit no resultado
                if hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                    cache_hit = result.metadata.get('cache_hit', False)
                elif isinstance(result, dict) and 'metadata' in result:
                    cache_hit = result['metadata'].get('cache_hit', False)
                
                # Calcular tempo de resposta
                response_time = (time.time() - start_time) * 1000  # ms
                
                # Registrar métricas
                metrics_collector.record_query(response_time, cache_hit)
                self.integration_stats["queries_tracked"] += 1
                
                # Registrar métricas detalhadas se disponíveis
                self._record_detailed_metrics(result, response_time)
                
                return result
            
            except Exception as e:
                # Registrar erro
                self.integration_stats["errors"] += 1
                logger.error(f"Erro durante rastreamento de métricas: {e}")
                # Re-lançar exceção original
                raise
        
        # Registrar função decorada
        self.integration_stats["decorated_functions"] += 1
        return wrapper
    
    def track_batch_query(self, func: Callable) -> Callable:
        """Decorador para rastrear métricas de consultas RAG em lote.
        
        Args:
            func: Função de consulta em lote a ser decorada
            
        Returns:
            Função decorada com rastreamento de métricas
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Verificar se o monitoramento está ativo
            if not self.config.monitoring.enabled:
                return func(*args, **kwargs)
            
            # Registrar início da consulta em lote
            start_time = time.time()
            
            try:
                # Executar função original
                results = func(*args, **kwargs)
                
                # Calcular tempo de resposta
                response_time = (time.time() - start_time) * 1000  # ms
                
                # Contar resultados
                results_count = len(results) if isinstance(results, list) else 1
                
                # Contar cache hits
                cache_hits = 0
                
                # Tentar detectar cache hits nos resultados
                if isinstance(results, list):
                    for result in results:
                        if hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                            if result.metadata.get('cache_hit', False):
                                cache_hits += 1
                        elif isinstance(result, dict) and 'metadata' in result:
                            if result['metadata'].get('cache_hit', False):
                                cache_hits += 1
                
                # Registrar métricas para cada resultado
                for i in range(results_count):
                    is_hit = (i < cache_hits)
                    # Dividir tempo igualmente entre resultados
                    individual_time = response_time / results_count
                    metrics_collector.record_query(individual_time, is_hit)
                
                # Atualizar estatísticas
                self.integration_stats["batch_queries_tracked"] += 1
                self.integration_stats["queries_tracked"] += results_count
                
                return results
            
            except Exception as e:
                # Registrar erro
                self.integration_stats["errors"] += 1
                logger.error(f"Erro durante rastreamento de métricas em lote: {e}")
                # Re-lançar exceção original
                raise
        
        # Registrar função decorada
        self.integration_stats["decorated_functions"] += 1
        return wrapper
    
    def _record_detailed_metrics(self, result: Any, response_time: float):
        """Registra métricas detalhadas do resultado.
        
        Args:
            result: Resultado da consulta
            response_time: Tempo de resposta em ms
        """
        try:
            # Extrair metadados se disponíveis
            metadata = None
            
            if hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                metadata = result.metadata
            elif isinstance(result, dict) and 'metadata' in result:
                metadata = result['metadata']
            
            if not metadata:
                return
            
            # Registrar métricas específicas do RAG
            if 'embedding_time' in metadata:
                logger.debug(f"Tempo de embedding: {metadata['embedding_time']:.2f}ms")
            
            if 'retrieval_time' in metadata:
                logger.debug(f"Tempo de recuperação: {metadata['retrieval_time']:.2f}ms")
            
            if 'documents_count' in metadata:
                logger.debug(f"Documentos recuperados: {metadata['documents_count']}")
            
        except Exception as e:
            logger.warning(f"Erro ao registrar métricas detalhadas: {e}")
    
    def get_integration_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas da integração.
        
        Returns:
            Dict com estatísticas
        """
        return self.integration_stats
    
    def export_stats(self, file_path: str) -> None:
        """Exporta estatísticas para arquivo.
        
        Args:
            file_path: Caminho do arquivo
        """
        stats = {
            "integration_stats": self.integration_stats,
            "current_metrics": metrics_collector.get_current_metrics(),
            "metrics_summary": metrics_collector.get_metrics_summary(24)
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)

# Instância global da integração
metrics_integration = RAGMetricsIntegration()

# Funções de conveniência para uso como decoradores
track_query = metrics_integration.track_query
track_batch_query = metrics_integration.track_batch_query

def apply_metrics_tracking(retriever_instance: Any) -> Any:
    """Aplica rastreamento de métricas a um retriever existente.
    
    Args:
        retriever_instance: Instância do retriever
        
    Returns:
        Retriever com rastreamento aplicado
    """
    if hasattr(retriever_instance, 'search'):
        retriever_instance.search = track_query(retriever_instance.search)
    
    if hasattr(retriever_instance, 'search_batch'):
        retriever_instance.search_batch = track_batch_query(retriever_instance.search_batch)
    
    logger.info(f"Rastreamento de métricas aplicado a {retriever_instance.__class__.__name__}")
    return retriever_instance

def get_metrics_dashboard() -> Dict[str, Any]:
    """Retorna dados para dashboard de métricas.
    
    Returns:
        Dict com dados do dashboard
    """
    from rag_infra.src.core.core_logic.rag_metrics_monitor import get_metrics_dashboard
    
    dashboard = get_metrics_dashboard()
    dashboard["integration"] = metrics_integration.get_integration_stats()
    
    return dashboard

if __name__ == "__main__":
    # Exemplo de uso
    print("=== Testando Integração de Métricas RAG ===")
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    
    # Classe de exemplo para demonstração
    class DummyRetriever:
        def search(self, query, use_cache=True):
            time.sleep(0.2)  # Simular processamento
            return {
                "results": ["Documento 1", "Documento 2"],
                "metadata": {"cache_hit": use_cache, "embedding_time": 50.0}
            }
        
        def search_batch(self, queries, use_cache=True):
            time.sleep(0.5)  # Simular processamento em lote
            return [
                {"results": ["Doc 1"], "metadata": {"cache_hit": use_cache}},
                {"results": ["Doc 2"], "metadata": {"cache_hit": False}}
            ]
    
    # Aplicar rastreamento
    retriever = DummyRetriever()
    retriever = apply_metrics_tracking(retriever)
    
    # Testar consultas
    print("/nExecutando consultas...")
    retriever.search("consulta de teste", use_cache=True)
    retriever.search("outra consulta", use_cache=False)
    retriever.search_batch(["consulta 1", "consulta 2"])
    
    # Mostrar estatísticas
    print("/n=== Estatísticas de Integração ===")
    stats = metrics_integration.get_integration_stats()
    print(json.dumps(stats, indent=2))
    
    # Mostrar dashboard
    print("/n=== Dashboard de Métricas ===")
    dashboard = get_metrics_dashboard()
    print(json.dumps(dashboard, indent=2))