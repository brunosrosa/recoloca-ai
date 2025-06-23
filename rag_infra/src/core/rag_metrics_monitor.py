# -*- coding: utf-8 -*-
"""
Sistema de Monitoramento de Métricas RAG - Recoloca.ai

Implementa monitoramento em tempo real de:
- Cache hit/miss rates
- Performance de consultas
- Uso de recursos GPU/CPU
- Alertas automáticos
- Exportação de métricas

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import json
import time
import threading
import psutil
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
from collections import deque, defaultdict
import csv

try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

@dataclass
class MetricSnapshot:
    """Snapshot de métricas em um momento específico."""
    timestamp: float
    cache_hits: int
    cache_misses: int
    cache_hit_rate: float
    total_queries: int
    avg_response_time: float
    p95_response_time: float
    cpu_usage: float
    memory_usage: float
    gpu_usage: Optional[float] = None
    gpu_memory_usage: Optional[float] = None
    active_cache_entries: int = 0
    cache_memory_mb: float = 0.0

@dataclass
class AlertConfig:
    """Configuração de alertas."""
    name: str
    metric: str
    threshold: float
    operator: str  # 'gt', 'lt', 'eq'
    enabled: bool = True
    cooldown_seconds: int = 300  # 5 minutos
    callback: Optional[Callable] = None

class MetricsCollector:
    """Coletor de métricas do sistema RAG."""
    
    def __init__(self, 
                 metrics_dir: str = "metrics",
                 collection_interval: int = 30,
                 retention_hours: int = 24):
        """
        Inicializa o coletor de métricas.
        
        Args:
            metrics_dir: Diretório para armazenar métricas
            collection_interval: Intervalo de coleta em segundos
            retention_hours: Horas de retenção de dados
        """
        self.metrics_dir = Path(metrics_dir)
        self.metrics_dir.mkdir(exist_ok=True)
        
        self.collection_interval = collection_interval
        self.retention_hours = retention_hours
        
        # Armazenamento de métricas
        self.snapshots: deque = deque(maxlen=int(retention_hours * 3600 / collection_interval))
        self.response_times: deque = deque(maxlen=1000)  # Últimas 1000 consultas
        
        # Contadores
        self.cache_hits = 0
        self.cache_misses = 0
        self.total_queries = 0
        
        # Thread de coleta
        self._collection_thread = None
        self._stop_collection = threading.Event()
        self._lock = threading.RLock()
        
        # Alertas
        self.alerts: List[AlertConfig] = []
        self.alert_history: Dict[str, float] = {}  # Último disparo de cada alerta
        
        # Configurar logging
        self.logger = logging.getLogger(__name__)
        
        # Arquivos de exportação
        self.metrics_file = self.metrics_dir / "rag_metrics.json"
        self.csv_file = self.metrics_dir / "rag_metrics.csv"
        self.alerts_file = self.metrics_dir / "alerts.json"
    
    def start_collection(self):
        """Inicia coleta automática de métricas."""
        if self._collection_thread and self._collection_thread.is_alive():
            return
        
        self._stop_collection.clear()
        self._collection_thread = threading.Thread(target=self._collect_loop, daemon=True)
        self._collection_thread.start()
        self.logger.info("Coleta de métricas iniciada")
    
    def stop_collection(self):
        """Para coleta automática de métricas."""
        self._stop_collection.set()
        if self._collection_thread:
            self._collection_thread.join(timeout=5)
        self.logger.info("Coleta de métricas parada")
    
    def _collect_loop(self):
        """Loop principal de coleta de métricas."""
        while not self._stop_collection.wait(self.collection_interval):
            try:
                self._collect_snapshot()
                self._check_alerts()
                self._cleanup_old_data()
            except Exception as e:
                self.logger.error(f"Erro na coleta de métricas: {e}")
    
    def _collect_snapshot(self):
        """Coleta um snapshot das métricas atuais."""
        with self._lock:
            # Calcular métricas de cache
            total_cache_requests = self.cache_hits + self.cache_misses
            cache_hit_rate = self.cache_hits / total_cache_requests if total_cache_requests > 0 else 0
            
            # Calcular métricas de performance
            avg_response_time = sum(self.response_times) / len(self.response_times) if self.response_times else 0
            p95_response_time = self._calculate_percentile(list(self.response_times), 95) if self.response_times else 0
            
            # Métricas do sistema
            cpu_usage = psutil.cpu_percent()
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            
            # Métricas GPU (se disponível)
            gpu_usage = None
            gpu_memory_usage = None
            
            if TORCH_AVAILABLE and torch.cuda.is_available():
                try:
                    gpu_usage = torch.cuda.utilization()
                    gpu_memory = torch.cuda.memory_stats()
                    gpu_memory_usage = (gpu_memory['allocated_bytes.all.current'] / 
                                      gpu_memory['reserved_bytes.all.current']) * 100 if gpu_memory['reserved_bytes.all.current'] > 0 else 0
                except Exception as e:
                    self.logger.warning(f"Erro ao coletar métricas GPU: {e}")
            
            # Criar snapshot
            snapshot = MetricSnapshot(
                timestamp=time.time(),
                cache_hits=self.cache_hits,
                cache_misses=self.cache_misses,
                cache_hit_rate=cache_hit_rate,
                total_queries=self.total_queries,
                avg_response_time=avg_response_time,
                p95_response_time=p95_response_time,
                cpu_usage=cpu_usage,
                memory_usage=memory_usage,
                gpu_usage=gpu_usage,
                gpu_memory_usage=gpu_memory_usage
            )
            
            self.snapshots.append(snapshot)
    
    def _calculate_percentile(self, data: List[float], percentile: int) -> float:
        """Calcula percentil dos dados."""
        if not data:
            return 0.0
        
        sorted_data = sorted(data)
        index = int((percentile / 100) * len(sorted_data))
        return sorted_data[min(index, len(sorted_data) - 1)]
    
    def record_query(self, response_time: float, cache_hit: bool):
        """Registra uma consulta.
        
        Args:
            response_time: Tempo de resposta em milissegundos
            cache_hit: Se foi um cache hit
        """
        with self._lock:
            self.total_queries += 1
            self.response_times.append(response_time)
            
            if cache_hit:
                self.cache_hits += 1
            else:
                self.cache_misses += 1
    
    def add_alert(self, alert: AlertConfig):
        """Adiciona um alerta.
        
        Args:
            alert: Configuração do alerta
        """
        self.alerts.append(alert)
        self.logger.info(f"Alerta adicionado: {alert.name}")
    
    def _check_alerts(self):
        """Verifica e dispara alertas."""
        if not self.snapshots:
            return
        
        current_snapshot = self.snapshots[-1]
        current_time = time.time()
        
        for alert in self.alerts:
            if not alert.enabled:
                continue
            
            # Verificar cooldown
            last_trigger = self.alert_history.get(alert.name, 0)
            if current_time - last_trigger < alert.cooldown_seconds:
                continue
            
            # Obter valor da métrica
            metric_value = getattr(current_snapshot, alert.metric, None)
            if metric_value is None:
                continue
            
            # Verificar condição
            triggered = False
            if alert.operator == 'gt' and metric_value > alert.threshold:
                triggered = True
            elif alert.operator == 'lt' and metric_value < alert.threshold:
                triggered = True
            elif alert.operator == 'eq' and abs(metric_value - alert.threshold) < 0.001:
                triggered = True
            
            if triggered:
                self._trigger_alert(alert, metric_value, current_snapshot)
                self.alert_history[alert.name] = current_time
    
    def _trigger_alert(self, alert: AlertConfig, value: float, snapshot: MetricSnapshot):
        """Dispara um alerta.
        
        Args:
            alert: Configuração do alerta
            value: Valor atual da métrica
            snapshot: Snapshot atual
        """
        alert_data = {
            "timestamp": datetime.now().isoformat(),
            "alert_name": alert.name,
            "metric": alert.metric,
            "threshold": alert.threshold,
            "current_value": value,
            "operator": alert.operator,
            "snapshot": asdict(snapshot)
        }
        
        # Log do alerta
        self.logger.warning(
            f"ALERTA: {alert.name} - {alert.metric} {alert.operator} {alert.threshold} "
            f"(atual: {value:.2f})"
        )
        
        # Salvar alerta
        self._save_alert(alert_data)
        
        # Callback personalizado
        if alert.callback:
            try:
                alert.callback(alert_data)
            except Exception as e:
                self.logger.error(f"Erro no callback do alerta {alert.name}: {e}")
    
    def _save_alert(self, alert_data: Dict[str, Any]):
        """Salva alerta em arquivo.
        
        Args:
            alert_data: Dados do alerta
        """
        alerts_list = []
        
        if self.alerts_file.exists():
            try:
                with open(self.alerts_file, 'r', encoding='utf-8') as f:
                    alerts_list = json.load(f)
            except Exception:
                pass
        
        alerts_list.append(alert_data)
        
        # Manter apenas últimos 100 alertas
        alerts_list = alerts_list[-100:]
        
        with open(self.alerts_file, 'w', encoding='utf-8') as f:
            json.dump(alerts_list, f, indent=2, ensure_ascii=False)
    
    def _cleanup_old_data(self):
        """Remove dados antigos baseado na retenção configurada."""
        cutoff_time = time.time() - (self.retention_hours * 3600)
        
        with self._lock:
            # Limpar snapshots antigos
            while self.snapshots and self.snapshots[0].timestamp < cutoff_time:
                self.snapshots.popleft()
    
    def get_current_metrics(self) -> Dict[str, Any]:
        """Retorna métricas atuais.
        
        Returns:
            Dict com métricas atuais
        """
        with self._lock:
            if not self.snapshots:
                return {}
            
            current = self.snapshots[-1]
            return {
                "timestamp": datetime.fromtimestamp(current.timestamp).isoformat(),
                "cache_hit_rate": current.cache_hit_rate,
                "total_queries": current.total_queries,
                "avg_response_time_ms": current.avg_response_time,
                "p95_response_time_ms": current.p95_response_time,
                "cpu_usage_percent": current.cpu_usage,
                "memory_usage_percent": current.memory_usage,
                "gpu_usage_percent": current.gpu_usage,
                "gpu_memory_usage_percent": current.gpu_memory_usage,
                "cache_hits": current.cache_hits,
                "cache_misses": current.cache_misses
            }
    
    def get_metrics_summary(self, hours: int = 1) -> Dict[str, Any]:
        """Retorna resumo de métricas para período especificado.
        
        Args:
            hours: Número de horas para análise
            
        Returns:
            Dict com resumo das métricas
        """
        cutoff_time = time.time() - (hours * 3600)
        
        with self._lock:
            recent_snapshots = [s for s in self.snapshots if s.timestamp >= cutoff_time]
            
            if not recent_snapshots:
                return {}
            
            # Calcular estatísticas
            hit_rates = [s.cache_hit_rate for s in recent_snapshots]
            response_times = [s.avg_response_time for s in recent_snapshots]
            cpu_usage = [s.cpu_usage for s in recent_snapshots]
            
            return {
                "period_hours": hours,
                "snapshots_count": len(recent_snapshots),
                "cache_hit_rate": {
                    "avg": sum(hit_rates) / len(hit_rates),
                    "min": min(hit_rates),
                    "max": max(hit_rates)
                },
                "response_time_ms": {
                    "avg": sum(response_times) / len(response_times),
                    "min": min(response_times),
                    "max": max(response_times)
                },
                "cpu_usage_percent": {
                    "avg": sum(cpu_usage) / len(cpu_usage),
                    "min": min(cpu_usage),
                    "max": max(cpu_usage)
                },
                "total_queries": recent_snapshots[-1].total_queries - recent_snapshots[0].total_queries
            }
    
    def export_metrics(self, format: str = "json") -> str:
        """Exporta métricas para arquivo.
        
        Args:
            format: Formato de exportação (json, csv)
            
        Returns:
            Caminho do arquivo exportado
        """
        if format == "json":
            return self._export_json()
        elif format == "csv":
            return self._export_csv()
        else:
            raise ValueError(f"Formato não suportado: {format}")
    
    def _export_json(self) -> str:
        """Exporta métricas em formato JSON."""
        data = {
            "export_timestamp": datetime.now().isoformat(),
            "collection_interval": self.collection_interval,
            "retention_hours": self.retention_hours,
            "snapshots": [asdict(s) for s in self.snapshots],
            "summary": self.get_metrics_summary(24)  # Últimas 24 horas
        }
        
        with open(self.metrics_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return str(self.metrics_file)
    
    def _export_csv(self) -> str:
        """Exporta métricas em formato CSV."""
        if not self.snapshots:
            return str(self.csv_file)
        
        fieldnames = list(asdict(self.snapshots[0]).keys())
        
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for snapshot in self.snapshots:
                writer.writerow(asdict(snapshot))
        
        return str(self.csv_file)

# Instância global do coletor
metrics_collector = MetricsCollector()

# Configurar alertas padrão
default_alerts = [
    AlertConfig(
        name="cache_hit_rate_low",
        metric="cache_hit_rate",
        threshold=0.6,
        operator="lt"
    ),
    AlertConfig(
        name="response_time_high",
        metric="avg_response_time",
        threshold=1000.0,
        operator="gt"
    ),
    AlertConfig(
        name="cpu_usage_high",
        metric="cpu_usage",
        threshold=80.0,
        operator="gt"
    ),
    AlertConfig(
        name="memory_usage_high",
        metric="memory_usage",
        threshold=85.0,
        operator="gt"
    )
]

# Adicionar alertas padrão
for alert in default_alerts:
    metrics_collector.add_alert(alert)

def start_monitoring():
    """Inicia monitoramento de métricas."""
    metrics_collector.start_collection()

def stop_monitoring():
    """Para monitoramento de métricas."""
    metrics_collector.stop_collection()

def get_metrics_dashboard() -> Dict[str, Any]:
    """Retorna dados para dashboard de métricas.
    
    Returns:
        Dict com dados do dashboard
    """
    return {
        "current": metrics_collector.get_current_metrics(),
        "last_hour": metrics_collector.get_metrics_summary(1),
        "last_24h": metrics_collector.get_metrics_summary(24),
        "alerts_count": len([a for a in metrics_collector.alerts if a.enabled])
    }

if __name__ == "__main__":
    # Exemplo de uso
    print("=== Iniciando Monitoramento de Métricas RAG ===")
    
    # Iniciar coleta
    start_monitoring()
    
    # Simular algumas consultas
    import random
    for i in range(10):
        response_time = random.uniform(100, 800)
        cache_hit = random.choice([True, False])
        metrics_collector.record_query(response_time, cache_hit)
        time.sleep(0.1)
    
    # Mostrar métricas atuais
    print("/n=== Métricas Atuais ===")
    current = metrics_collector.get_current_metrics()
    print(json.dumps(current, indent=2, ensure_ascii=False))
    
    # Exportar métricas
    json_file = metrics_collector.export_metrics("json")
    csv_file = metrics_collector.export_metrics("csv")
    
    print(f"/nMétricas exportadas:")
    print(f"JSON: {json_file}")
    print(f"CSV: {csv_file}")
    
    # Parar monitoramento
    stop_monitoring()