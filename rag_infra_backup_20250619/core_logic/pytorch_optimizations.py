#!/usr/bin/env python3
"""
Otimizações de Performance para PyTorch GPU Retriever

Implementa:
- Batch processing para múltiplas consultas
- Cache persistente com TTL
- Otimização de memória GPU
- Pool de conexões para embeddings
"""

import sys
import os
import time
import json
import torch
import hashlib
import pickle
from typing import List, Dict, Any, Optional, Tuple, Union
from pathlib import Path
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from collections import OrderedDict
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from .pytorch_gpu_retriever import PyTorchGPURetriever, SearchResult
except ImportError:
    from pytorch_gpu_retriever import PyTorchGPURetriever, SearchResult

@dataclass
class CacheEntry:
    """Entrada do cache com metadados."""
    query_hash: str
    results: List[SearchResult]
    timestamp: float
    access_count: int
    last_access: float
    top_k: int
    
    def is_expired(self, ttl_seconds: int) -> bool:
        """Verifica se a entrada expirou."""
        return time.time() - self.timestamp > ttl_seconds
    
    def update_access(self):
        """Atualiza estatísticas de acesso."""
        self.access_count += 1
        self.last_access = time.time()

class PersistentCache:
    """
    Cache persistente com TTL e LRU para resultados de busca.
    """
    
    def __init__(self, 
                 cache_dir: str = "cache",
                 max_entries: int = 1000,
                 ttl_seconds: int = 3600,  # 1 hora
                 auto_save_interval: int = 300):  # 5 minutos
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        
        self.max_entries = max_entries
        self.ttl_seconds = ttl_seconds
        self.auto_save_interval = auto_save_interval
        
        self.cache: OrderedDict[str, CacheEntry] = OrderedDict()
        self.cache_file = self.cache_dir / "search_cache.pkl"
        self.stats_file = self.cache_dir / "cache_stats.json"
        
        # Estatísticas
        self.stats = {
            "hits": 0,
            "misses": 0,
            "evictions": 0,
            "saves": 0,
            "loads": 0
        }
        
        # Thread safety
        self._lock = threading.RLock()
        
        # Auto-save timer
        self._last_save = time.time()
        
        # Carregar cache existente
        self.load_cache()
    
    def _generate_cache_key(self, query: str, top_k: int) -> str:
        """Gera chave única para a consulta."""
        content = f"{query.strip().lower()}:{top_k}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def get(self, query: str, top_k: int) -> Optional[List[SearchResult]]:
        """Recupera resultados do cache."""
        cache_key = self._generate_cache_key(query, top_k)
        
        with self._lock:
            if cache_key in self.cache:
                entry = self.cache[cache_key]
                
                # Verificar expiração
                if entry.is_expired(self.ttl_seconds):
                    del self.cache[cache_key]
                    self.stats["misses"] += 1
                    return None
                
                # Atualizar acesso e mover para o final (LRU)
                entry.update_access()
                self.cache.move_to_end(cache_key)
                
                self.stats["hits"] += 1
                return entry.results
            
            self.stats["misses"] += 1
            return None
    
    def put(self, query: str, top_k: int, results: List[SearchResult]):
        """Armazena resultados no cache."""
        cache_key = self._generate_cache_key(query, top_k)
        
        with self._lock:
            # Criar entrada
            entry = CacheEntry(
                query_hash=cache_key,
                results=results,
                timestamp=time.time(),
                access_count=1,
                last_access=time.time(),
                top_k=top_k
            )
            
            # Adicionar ao cache
            self.cache[cache_key] = entry
            self.cache.move_to_end(cache_key)
            
            # Verificar limite de tamanho
            while len(self.cache) > self.max_entries:
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
                self.stats["evictions"] += 1
            
            # Auto-save periódico
            if time.time() - self._last_save > self.auto_save_interval:
                self.save_cache()
    
    def clear(self):
        """Limpa o cache."""
        with self._lock:
            self.cache.clear()
            if self.cache_file.exists():
                self.cache_file.unlink()
    
    def save_cache(self):
        """Salva cache no disco."""
        try:
            with self._lock:
                with open(self.cache_file, 'wb') as f:
                    pickle.dump(dict(self.cache), f)
                
                with open(self.stats_file, 'w') as f:
                    json.dump(self.stats, f, indent=2)
                
                self._last_save = time.time()
                self.stats["saves"] += 1
                
        except Exception as e:
            print(f"Erro ao salvar cache: {e}")
    
    def load_cache(self):
        """Carrega cache do disco."""
        try:
            if self.cache_file.exists():
                with open(self.cache_file, 'rb') as f:
                    cached_data = pickle.load(f)
                
                with self._lock:
                    # Filtrar entradas expiradas
                    current_time = time.time()
                    for key, entry in cached_data.items():
                        if not entry.is_expired(self.ttl_seconds):
                            self.cache[key] = entry
                
                self.stats["loads"] += 1
            
            if self.stats_file.exists():
                with open(self.stats_file, 'r') as f:
                    saved_stats = json.load(f)
                    self.stats.update(saved_stats)
                    
        except Exception as e:
            print(f"Erro ao carregar cache: {e}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do cache."""
        with self._lock:
            total_requests = self.stats["hits"] + self.stats["misses"]
            hit_rate = self.stats["hits"] / total_requests if total_requests > 0 else 0
            
            return {
                "entries": len(self.cache),
                "max_entries": self.max_entries,
                "hit_rate": hit_rate,
                "total_hits": self.stats["hits"],
                "total_misses": self.stats["misses"],
                "evictions": self.stats["evictions"],
                "saves": self.stats["saves"],
                "loads": self.stats["loads"],
                "cache_size_mb": self._estimate_cache_size()
            }
    
    def _estimate_cache_size(self) -> float:
        """Estima tamanho do cache em MB."""
        try:
            if self.cache_file.exists():
                return self.cache_file.stat().st_size / (1024 * 1024)
        except:
            pass
        return 0.0

class BatchProcessor:
    """
    Processador de consultas em batch para otimizar throughput.
    """
    
    def __init__(self, 
                 retriever: PyTorchGPURetriever,
                 batch_size: int = 5,
                 max_workers: int = 10):
        self.retriever = retriever
        self.batch_size = batch_size
        self.max_workers = max_workers
        
    def process_batch(self, queries: List[Tuple[str, int]]) -> List[Tuple[bool, List[SearchResult], str]]:
        """
        Processa um batch de consultas.
        
        Args:
            queries: Lista de (query, top_k)
            
        Returns:
            Lista de (success, results, error_msg)
        """
        def execute_single_query(query_data: Tuple[str, int]) -> Tuple[bool, List[SearchResult], str]:
            query, top_k = query_data
            try:
                results = self.retriever.search(query, top_k=top_k)
                return True, results, ""
            except Exception as e:
                return False, [], str(e)
        
        # Processar em paralelo
        with ThreadPoolExecutor(max_workers=min(self.max_workers, len(queries))) as executor:
            futures = [executor.submit(execute_single_query, query_data) for query_data in queries]
            results = [future.result() for future in as_completed(futures)]
        
        return results
    
    def process_queries(self, queries: List[Tuple[str, int]]) -> List[Tuple[bool, List[SearchResult], str]]:
        """
        Processa lista de consultas em batches.
        
        Args:
            queries: Lista de (query, top_k)
            
        Returns:
            Lista de resultados
        """
        all_results = []
        
        # Dividir em batches
        for i in range(0, len(queries), self.batch_size):
            batch = queries[i:i + self.batch_size]
            batch_results = self.process_batch(batch)
            all_results.extend(batch_results)
        
        return all_results

class OptimizedPyTorchRetriever:
    """
    Versão otimizada do PyTorch GPU Retriever com cache e batch processing.
    """
    
    def __init__(self,
                 force_cpu: bool = False,
                 cache_enabled: bool = True,
                 cache_dir: str = "cache",
                 cache_ttl: int = 3600,
                 batch_size: int = 5,
                 max_workers: int = 10):
        
        # Inicializar retriever base
        self.base_retriever = PyTorchGPURetriever(force_cpu=force_cpu)
        
        # Cache persistente
        self.cache_enabled = cache_enabled
        if cache_enabled:
            self.cache = PersistentCache(
                cache_dir=cache_dir,
                ttl_seconds=cache_ttl
            )
        else:
            self.cache = None
        
        # Batch processor
        self.batch_processor = None  # Será inicializado após o retriever
        self.batch_size = batch_size
        self.max_workers = max_workers
        
        # Estatísticas
        self.stats = {
            "total_queries": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "batch_queries": 0,
            "single_queries": 0,
            "total_time": 0.0,
            "avg_query_time": 0.0
        }
    
    def initialize(self) -> bool:
        """Inicializa o retriever otimizado."""
        success = self.base_retriever.initialize()
        
        if success:
            # Inicializar batch processor
            self.batch_processor = BatchProcessor(
                self.base_retriever,
                batch_size=self.batch_size,
                max_workers=self.max_workers
            )
        
        return success
    
    def load_index(self) -> bool:
        """Carrega o índice."""
        return self.base_retriever.load_index()
    
    def search(self, query: str, top_k: int = 5, min_score: float = 0.0) -> List[SearchResult]:
        """
        Busca otimizada com cache.
        
        Args:
            query: Consulta
            top_k: Número de resultados
            min_score: Score mínimo para filtrar resultados
            
        Returns:
            Lista de resultados
        """
        start_time = time.time()
        
        # Verificar cache primeiro
        if self.cache_enabled and self.cache:
            cached_results = self.cache.get(query, top_k)
            if cached_results is not None:
                self.stats["cache_hits"] += 1
                self.stats["total_queries"] += 1
                self._update_timing_stats(time.time() - start_time)
                return cached_results
            
            self.stats["cache_misses"] += 1
        
        # Executar busca
        results = self.base_retriever.search(query, top_k=top_k, min_score=min_score)
        
        # Armazenar no cache
        if self.cache_enabled and self.cache:
            self.cache.put(query, top_k, results)
        
        # Atualizar estatísticas
        self.stats["single_queries"] += 1
        self.stats["total_queries"] += 1
        self._update_timing_stats(time.time() - start_time)
        
        return results
    
    def search_batch(self, queries: List[Tuple[str, int]]) -> List[Tuple[bool, List[SearchResult], str]]:
        """
        Busca em batch otimizada.
        
        Args:
            queries: Lista de (query, top_k)
            
        Returns:
            Lista de (success, results, error)
        """
        start_time = time.time()
        
        if not self.batch_processor:
            raise RuntimeError("Retriever não inicializado")
        
        # Verificar cache para cada query
        cached_results = []
        uncached_queries = []
        query_indices = []
        
        if self.cache_enabled and self.cache:
            for i, (query, top_k) in enumerate(queries):
                cached = self.cache.get(query, top_k)
                if cached is not None:
                    cached_results.append((i, True, cached, ""))
                    self.stats["cache_hits"] += 1
                else:
                    uncached_queries.append((query, top_k))
                    query_indices.append(i)
                    self.stats["cache_misses"] += 1
        else:
            uncached_queries = queries
            query_indices = list(range(len(queries)))
        
        # Processar queries não cacheadas
        batch_results = []
        if uncached_queries:
            batch_results = self.batch_processor.process_queries(uncached_queries)
            
            # Armazenar no cache
            if self.cache_enabled and self.cache:
                for (query, top_k), (success, results, _) in zip(uncached_queries, batch_results):
                    if success:
                        self.cache.put(query, top_k, results)
        
        # Combinar resultados
        final_results = [None] * len(queries)
        
        # Adicionar resultados cacheados
        for i, success, results, error in cached_results:
            final_results[i] = (success, results, error)
        
        # Adicionar resultados do batch
        for i, (success, results, error) in zip(query_indices, batch_results):
            final_results[i] = (success, results, error)
        
        # Atualizar estatísticas
        self.stats["batch_queries"] += len(queries)
        self.stats["total_queries"] += len(queries)
        self._update_timing_stats(time.time() - start_time)
        
        return final_results
    
    def _update_timing_stats(self, query_time: float):
        """Atualiza estatísticas de tempo."""
        self.stats["total_time"] += query_time
        if self.stats["total_queries"] > 0:
            self.stats["avg_query_time"] = self.stats["total_time"] / self.stats["total_queries"]
    
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas completas."""
        base_stats = self.stats.copy()
        
        # Adicionar estatísticas do cache
        if self.cache_enabled and self.cache:
            cache_stats = self.cache.get_stats()
            base_stats["cache"] = cache_stats
        
        # Adicionar informações do retriever base
        if hasattr(self.base_retriever, 'get_index_info'):
            base_stats["index_info"] = self.base_retriever.get_index_info()
        
        return base_stats
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Obtém informações detalhadas do cache."""
        if not self.cache_enabled or not self.cache:
            return {
                "enabled": False,
                "size": 0,
                "hits": 0,
                "misses": 0,
                "hit_rate": 0.0,
                "ttl": 0,
                "max_size": 0
            }
        
        cache_stats = self.cache.get_stats()
        return {
            "enabled": True,
            "size": cache_stats.get("entries", 0),
            "hits": cache_stats.get("total_hits", 0),
            "misses": cache_stats.get("total_misses", 0),
            "hit_rate": cache_stats.get("hit_rate", 0.0),
            "ttl": self.cache.ttl_seconds,
            "max_size": cache_stats.get("max_entries", 0),
            "memory_usage_mb": cache_stats.get("cache_size_mb", 0.0)
        }
    
    def _estimate_cache_memory_usage(self) -> float:
        """Estima o uso de memória do cache em MB."""
        if not self.cache or not self.cache.cache:
            return 0.0
        
        try:
            import sys
            total_size = 0
            for key, entry in self.cache.cache.items():
                total_size += sys.getsizeof(key)
                total_size += sys.getsizeof(entry)
                if hasattr(entry, 'results'):
                    total_size += sys.getsizeof(entry.results)
            
            return total_size / (1024 * 1024)  # Convert to MB
        except Exception:
            return 0.0
    
    def clear_cache(self):
        """Limpa o cache."""
        if self.cache_enabled and self.cache:
            self.cache.clear()
    
    def save_cache(self):
        """Força salvamento do cache."""
        if self.cache_enabled and self.cache:
            self.cache.save_cache()
    
    def get_index_info(self) -> Dict[str, Any]:
        """Retorna informações do índice."""
        base_info = self.base_retriever.get_index_info()
        base_info["optimizations"] = {
            "cache_enabled": self.cache_enabled,
            "batch_size": self.batch_size,
            "max_workers": self.max_workers
        }
        return base_info

def create_optimized_retriever(force_cpu: bool = False,
                             cache_enabled: bool = True,
                             cache_dir: str = "cache",
                             cache_ttl: int = 3600,
                             batch_size: int = 5,
                             max_workers: int = 10) -> OptimizedPyTorchRetriever:
    """
    Factory function para criar retriever otimizado.
    
    Args:
        force_cpu: Forçar uso de CPU
        cache_enabled: Habilitar cache
        cache_dir: Diretório do cache
        cache_ttl: TTL do cache em segundos
        batch_size: Tamanho do batch
        max_workers: Máximo de workers
        
    Returns:
        OptimizedPyTorchRetriever: Retriever otimizado
    """
    return OptimizedPyTorchRetriever(
        force_cpu=force_cpu,
        cache_enabled=cache_enabled,
        cache_dir=cache_dir,
        cache_ttl=cache_ttl,
        batch_size=batch_size,
        max_workers=max_workers
    )

def main():
    """
    Exemplo de uso das otimizações.
    """
    print("🚀 Testando Otimizações do PyTorch GPU Retriever")
    print("=" * 50)
    
    # Criar retriever otimizado
    retriever = create_optimized_retriever(
        cache_enabled=True,
        batch_size=3,
        max_workers=5
    )
    
    # Inicializar
    if not retriever.initialize():
        print("❌ Falha ao inicializar")
        return
    
    if not retriever.load_index():
        print("❌ Falha ao carregar índice")
        return
    
    print("✅ Retriever otimizado inicializado")
    
    # Teste de consultas individuais
    print("\n🔍 Teste de Consultas Individuais")
    test_queries = [
        "Como implementar autenticação JWT?",
        "Configurar banco de dados PostgreSQL",
        "Como implementar autenticação JWT?",  # Repetida para testar cache
    ]
    
    for query in test_queries:
        start = time.time()
        results = retriever.search(query, top_k=3)
        duration = time.time() - start
        print(f"  '{query[:30]}...': {len(results)} resultados em {duration:.3f}s")
    
    # Teste de batch
    print("\n🚀 Teste de Batch")
    batch_queries = [
        ("Deploy com Docker", 3),
        ("Testes automatizados", 3),
        ("Monitoramento de APIs", 3),
    ]
    
    start = time.time()
    batch_results = retriever.search_batch(batch_queries)
    duration = time.time() - start
    
    successful = sum(1 for success, _, _ in batch_results if success)
    print(f"  Batch de {len(batch_queries)} queries: {successful} sucessos em {duration:.3f}s")
    
    # Exibir estatísticas
    print("\n📊 Estatísticas")
    stats = retriever.get_stats()
    print(f"  Total de queries: {stats['total_queries']}")
    print(f"  Cache hits: {stats['cache_hits']}")
    print(f"  Cache misses: {stats['cache_misses']}")
    print(f"  Tempo médio por query: {stats['avg_query_time']:.3f}s")
    
    if "cache" in stats:
        cache_stats = stats["cache"]
        print(f"  Hit rate do cache: {cache_stats['hit_rate']*100:.1f}%")
        print(f"  Entradas no cache: {cache_stats['entries']}")
    
    # Salvar cache
    retriever.save_cache()
    print("\n💾 Cache salvo")
    
    print("\n✅ Teste concluído!")

if __name__ == "__main__":
    main()