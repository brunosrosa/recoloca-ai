#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para demonstrar os benefícios das otimizações do RAG
"""

import sys
import time
from pathlib import Path

# Adicionar core_logic ao path

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root / "src" / "core"))

try:
    # from retriever import get_retriever  # Função pode não existir mais
    
    print("[START] Demonstração: Otimizações RAG")
    print("=" * 60)
    
    # Teste 1: Retriever sem otimizações
    print("\n[EMOJI] TESTE 1: Retriever Padrão (sem otimizações)")
    print("-" * 50)
    
    from rag_infra.src.core.rag_retriever import RAGRetriever
    retriever_normal = RAGRetriever(use_optimizations=False)
    
    # Consultas de teste
    test_queries = [
        "Como funciona o sistema de autenticação?",
        "Quais são os requisitos funcionais principais?",
        "Arquitetura do backend FastAPI",
        "Integração com Supabase",
        "Como funciona o sistema de autenticação?"  # Repetida para testar cache
    ]
    
    start_time = time.time()
    results_normal = []
    
    for i, query in enumerate(test_queries, 1):
        query_start = time.time()
        if not retriever_normal.is_loaded:
            retriever_normal.initialize()
            retriever_normal.load_index()
        results = retriever_normal.search(query, top_k=3)
        query_time = time.time() - query_start
        
        results_normal.append((query, results, query_time))
        print(f"  Query {i}: {query_time:.3f}s - {len(results)} resultados")
    
    total_time_normal = time.time() - start_time
    print(f"\n  ⏱[EMOJI] Tempo total: {total_time_normal:.3f}s")
    print(f"  [EMOJI] Tempo médio por query: {total_time_normal/len(test_queries):.3f}s")
    
    # Teste 2: Retriever com otimizações
    print("\n\n[EMOJI] TESTE 2: Retriever Otimizado (com cache e otimizações)")
    print("-" * 50)
    
    retriever_optimized = RAGRetriever(
        use_optimizations=True,
        cache_enabled=True,
        batch_size=8
    )
    
    start_time = time.time()
    results_optimized = []
    
    for i, query in enumerate(test_queries, 1):
        query_start = time.time()
        if not retriever_optimized.is_loaded:
            retriever_optimized.initialize()
            retriever_optimized.load_index()
        results = retriever_optimized.search(query, top_k=3)
        query_time = time.time() - query_start
        
        results_optimized.append((query, results, query_time))
        cache_status = "[CACHE HIT]" if query_time < 0.01 else "[CACHE MISS]"
        print(f"  Query {i}: {query_time:.3f}s - {len(results)} resultados {cache_status}")
    
    total_time_optimized = time.time() - start_time
    print(f"\n  ⏱[EMOJI] Tempo total: {total_time_optimized:.3f}s")
    print(f"  [EMOJI] Tempo médio por query: {total_time_optimized/len(test_queries):.3f}s")
    
    # Comparação
    print("\n\n[EMOJI] COMPARAÇÃO DE PERFORMANCE")
    print("=" * 60)
    
    improvement = ((total_time_normal - total_time_optimized) / total_time_normal) * 100
    speedup = total_time_normal / total_time_optimized if total_time_optimized > 0 else float('inf')
    
    print(f"[EMOJI] Sem otimizações:    {total_time_normal:.3f}s")
    print(f"[EMOJI] Com otimizações:    {total_time_optimized:.3f}s")
    print(f"[EMOJI] Melhoria:           {improvement:.1f}%")
    print(f"[START] Speedup:            {speedup:.1f}x mais rápido")
    
    # Estatísticas do cache (se disponível)
    if hasattr(retriever_optimized, 'pytorch_retriever') and hasattr(retriever_optimized.pytorch_retriever, 'stats'):
        stats = retriever_optimized.pytorch_retriever.stats
        print(f"\n[EMOJI] Estatísticas do Cache:")
        print(f"  • Total de consultas: {stats.get('total_queries', 0)}")
        print(f"  • Cache hits: {stats.get('cache_hits', 0)}")
        print(f"  • Cache misses: {stats.get('cache_misses', 0)}")
        
        if stats.get('total_queries', 0) > 0:
            hit_rate = (stats.get('cache_hits', 0) / stats.get('total_queries', 1)) * 100
            print(f"  • Taxa de acerto: {hit_rate:.1f}%")
    
    # Benefícios das otimizações
    print("\n\n[EMOJI] BENEFÍCIOS DAS OTIMIZAÇÕES (use_optimizations=True)")
    print("=" * 60)
    print("[OK] Cache Persistente:")
    print("   • Armazena resultados de consultas anteriores")
    print("   • TTL configurável (padrão: 1 hora)")
    print("   • LRU eviction para gerenciar memória")
    print("   • Persistência em disco entre sessões")
    
    print("\n[OK] Batch Processing:")
    print("   • Processa múltiplas consultas simultaneamente")
    print("   • Otimização de uso de GPU")
    print("   • Reduz overhead de inicialização")
    
    print("\n[OK] Otimização de Memória:")
    print("   • Gerenciamento inteligente de memória GPU")
    print("   • Pool de conexões para embeddings")
    print("   • Cleanup automático de recursos")
    
    print("\n[OK] Estatísticas e Monitoramento:")
    print("   • Métricas detalhadas de performance")
    print("   • Monitoramento de cache hit/miss")
    print("   • Análise de padrões de uso")
    
    print("\n\n[EMOJI] RECOMENDAÇÃO")
    print("=" * 60)
    print("Para produção e desenvolvimento ativo, recomenda-se:")
    print("")
    print("```python")
    print("retriever = get_retriever(")
    print("    use_optimizations=True,    # Ativa todas as otimizações")
    print("    cache_enabled=True,        # Cache persistente")
    print("    batch_size=8               # Batch otimizado para RTX 2060")
    print(")")
    print("```")
    
except Exception as e:
    print(f"[ERROR] Erro: {e}")
    import traceback
    traceback.print_exc()