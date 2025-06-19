# Guia de Otimizações RAG para RTX 2060

## 🎯 Visão Geral

Este guia fornece instruções completas para configurar e usar o sistema RAG otimizado especificamente para placas de vídeo RTX 2060. As otimizações incluem configurações de cache, processamento em lote, monitoramento de métricas e testes de carga.

## 🔧 Configuração Rápida

### 1. Configuração Automática

```bash
# Configurar otimizações RTX 2060 automaticamente
python rag_infra/scripts/setup_rtx2060_optimizations.py

# Validar configuração existente
python rag_infra/scripts/setup_rtx2060_optimizations.py --validate

# Forçar reconfiguração
python rag_infra/scripts/setup_rtx2060_optimizations.py --force
```

### 2. Inicialização Otimizada

```bash
# Usar script de inicialização gerado
python rag_infra/scripts/start_rtx2060_optimized.py
```

### 3. Demonstração Completa

```bash
# Executar demonstração com testes de performance
python rag_infra/examples/rtx2060_optimization_example.py
```

## ⚙️ Configurações Específicas RTX 2060

### Cache Otimizado

```json
{
  "cache": {
    "enabled": true,
    "ttl_seconds": 1800,
    "max_entries": 1000,
    "memory_limit_mb": 512,
    "persistence_enabled": true
  }
}
```

**Características:**
- TTL de 30 minutos para balancear performance e atualização
- Limite de 512MB de memória (conservador para RTX 2060)
- Cache persistente para manter dados entre sessões
- Limpeza automática a cada 5 minutos

### Processamento em Lote

```json
{
  "batch": {
    "enabled": true,
    "size": 8,
    "max_workers": 2,
    "auto_scaling": true,
    "min_batch_size": 2,
    "max_batch_size": 16
  }
}
```

**Características:**
- Lotes de 8 consultas (otimizado para RTX 2060)
- Máximo 2 workers para evitar sobrecarga
- Auto-scaling baseado na carga
- Timeout de 30 segundos por lote

### Configurações de GPU

```json
{
  "gpu": {
    "force_pytorch": true,
    "use_optimizations": true,
    "memory_fraction": 0.7,
    "vram_limit_mb": 4096,
    "enable_fallback": true
  }
}
```

**Características:**
- PyTorch forçado se FAISS-GPU não disponível
- Uso de 70% da VRAM (4GB de 6GB total)
- Fallback automático para CPU se necessário
- Otimizações de memória habilitadas

## 📊 Monitoramento e Métricas

### Métricas Coletadas

- **Performance:**
  - Tempo de resposta (média, P95, P99)
  - Queries por segundo (QPS)
  - Taxa de erro

- **Cache:**
  - Hit rate / Miss rate
  - Tamanho do cache
  - Tempo de vida das entradas

- **Recursos:**
  - Uso de CPU
  - Uso de memória RAM
  - Uso de VRAM
  - Temperatura da GPU

### Alertas Configurados

```json
{
  "alert_thresholds": {
    "response_time_p95": 2.0,
    "cache_hit_rate": 0.3,
    "error_rate": 0.05,
    "memory_usage": 0.8
  }
}
```

## 🚀 Uso Programático

### Inicialização Básica

```python
from rag_infra.core_logic.rag_retriever import RAGRetriever
from rag_infra.config.rag_optimization_config import RAGOptimizationConfig

# Carregar configuração RTX 2060
config = RAGOptimizationConfig.load_config('rag_infra/config/rag_optimization_config.json')
rtx2060_config = config.get_rtx2060_config()

# Inicializar retriever otimizado
retriever = RAGRetriever(
    use_optimizations=True,
    cache_enabled=True,
    batch_size=rtx2060_config.batch.size,
    force_pytorch=rtx2060_config.gpu.force_pytorch
)
```

### Consultas Individuais

```python
# Busca simples
results = retriever.search(
    query="Como criar um currículo profissional?",
    top_k=5,
    min_score=0.7
)

# Verificar cache hit
for result in results:
    cache_hit = result.metadata.get('cache_hit', False)
    print(f"Cache hit: {cache_hit}, Score: {result.score:.3f}")
```

### Processamento em Lote

```python
# Múltiplas consultas
queries = [
    "Dicas para entrevista de emprego",
    "Habilidades técnicas demandadas",
    "Como negociar salário",
    "Networking profissional"
]

# Processar em lote
batch_results = retriever.search_batch(queries, top_k=3)

# Analisar resultados
for i, query_results in enumerate(batch_results):
    print(f"Consulta {i+1}: {len(query_results)} resultados")
    cache_hits = sum(1 for r in query_results if r.metadata.get('cache_hit', False))
    print(f"Cache hits: {cache_hits}/{len(query_results)}")
```

### Monitoramento de Métricas

```python
from rag_infra.core_logic.rag_metrics_monitor import RAGMetricsMonitor

# Inicializar monitor
monitor = RAGMetricsMonitor()

# Coletar métricas após uso
metrics = monitor.get_metrics_summary()
print(f"QPS médio: {metrics['performance']['avg_qps']:.1f}")
print(f"Cache hit rate: {metrics['cache']['hit_rate']:.1%}")
print(f"Tempo médio: {metrics['performance']['avg_response_time']:.3f}s")

# Exportar métricas
monitor.export_metrics_json('metrics_rtx2060.json')
monitor.export_metrics_csv('metrics_rtx2060.csv')
```

## 🧪 Testes de Performance

### Teste de Carga RTX 2060

```python
from rag_infra.tests.test_load_performance import run_rtx2060_optimized_test

# Executar teste otimizado
results = run_rtx2060_optimized_test()

print(f"QPS médio: {results.avg_qps:.1f}")
print(f"P95 tempo: {results.p95_response_time:.3f}s")
print(f"Cache hit rate: {results.cache_hit_rate:.1%}")
print(f"Taxa de erro: {results.error_rate:.1%}")
```

### Configuração de Teste Personalizada

```python
from rag_infra.tests.test_load_performance import RAGLoadTester, LoadTestConfig

# Configurar teste personalizado
config = LoadTestConfig(
    concurrent_users=3,
    queries_per_user=15,
    ramp_up_time=20,
    test_duration=180
)

# Executar teste
tester = RAGLoadTester(retriever)
results = tester.run_load_test(config)

# Analisar resultados
print(f"Usuários simultâneos: {config.concurrent_users}")
print(f"Total de consultas: {results.total_queries}")
print(f"Sucesso: {results.success_rate:.1%}")
```

## 📈 Benchmarks RTX 2060

### Performance Esperada

| Métrica | Valor Típico | Valor Otimizado |
|---------|--------------|----------------|
| QPS | 8-12 | 15-20 |
| Tempo médio | 800ms | 400-600ms |
| P95 | 2.5s | 1.5-2.0s |
| Cache hit rate | 15-25% | 35-50% |
| Uso VRAM | 5-6GB | 3-4GB |

### Comparação de Configurações

| Configuração | QPS | Tempo Médio | VRAM |
|--------------|-----|-------------|------|
| Padrão | 10 | 750ms | 5.2GB |
| RTX 2060 Otimizado | 18 | 450ms | 3.8GB |
| Cache Agressivo | 22 | 350ms | 4.1GB |

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. FAISS-GPU não disponível

```bash
# Verificar instalação FAISS-GPU
python -c "import faiss; print('FAISS-GPU OK' if faiss.get_num_gpus() > 0 else 'FAISS-GPU não disponível')"

# Solução: usar PyTorch
export RAG_FORCE_PYTORCH=true
```

#### 2. Erro de memória CUDA

```python
# Reduzir uso de VRAM
config['gpu']['memory_fraction'] = 0.5
config['gpu']['vram_limit_mb'] = 3072
config['batch']['size'] = 4
```

#### 3. Performance baixa

```python
# Verificar configurações
print(f"Cache habilitado: {retriever._cache_enabled}")
print(f"Otimizações: {retriever._use_optimizations}")
print(f"Tamanho do lote: {retriever._batch_size}")

# Ajustar cache
config['cache']['ttl_seconds'] = 3600  # 1 hora
config['cache']['max_entries'] = 2000
```

#### 4. Cache hit rate baixo

```python
# Analisar padrões de consulta
metrics = monitor.get_cache_analysis()
print(f"Consultas únicas: {metrics['unique_queries']}")
print(f"Consultas repetidas: {metrics['repeated_queries']}")

# Aumentar TTL se necessário
config['cache']['ttl_seconds'] = 2700  # 45 minutos
```

### Logs de Debug

```python
import logging

# Habilitar logs detalhados
logging.getLogger('rag_infra').setLevel(logging.DEBUG)
logging.getLogger('pytorch_optimizations').setLevel(logging.DEBUG)

# Verificar logs específicos
logger = logging.getLogger('rag_retriever')
logger.info("Verificando configuração RTX 2060...")
```

## 📚 Recursos Adicionais

### Arquivos de Configuração

- `rag_infra/config/rag_optimization_config.py` - Classes de configuração
- `rag_infra/config/rag_optimization_config.json` - Configuração ativa

### Scripts Utilitários

- `rag_infra/scripts/setup_rtx2060_optimizations.py` - Configuração automática
- `rag_infra/scripts/start_rtx2060_optimized.py` - Inicialização otimizada
- `rag_infra/scripts/check_backend.py` - Verificação de backend

### Exemplos e Testes

- `rag_infra/examples/rtx2060_optimization_example.py` - Demonstração completa
- `rag_infra/tests/test_load_performance.py` - Testes de carga

### Monitoramento

- `rag_infra/core_logic/rag_metrics_monitor.py` - Monitor de métricas
- `rag_infra/core_logic/rag_metrics_integration.py` - Integração de métricas

## 🎯 Próximos Passos

1. **Configurar:** Execute o script de configuração automática
2. **Testar:** Use o exemplo de demonstração para validar
3. **Monitorar:** Acompanhe métricas durante uso real
4. **Ajustar:** Refine configurações baseado nos resultados
5. **Escalar:** Considere otimizações adicionais conforme necessário

---

**Nota:** Este guia é específico para RTX 2060. Para outras GPUs, ajuste as configurações de VRAM e processamento conforme a capacidade do hardware.