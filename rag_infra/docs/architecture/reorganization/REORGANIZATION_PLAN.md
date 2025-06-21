# Plano de Reorganização da Infraestrutura RAG

**Data:** 2025-06-18
**Tarefa:** [REO-DIR-001] - Criar estrutura de diretórios detalhada
**Status:** Em Execução

## Estrutura Atual vs. Proposta

### Estrutura Atual:
```
rag_infra/
├── core_logic/          # Mistura de lógica core, testes e demos
├── scripts/             # Scripts utilitários ✓
├── tests/               # Testes de integração ✓
├── results and reports/ # Relatórios e resultados ✓
└── outros diretórios...
```

### Estrutura Proposta:
```
rag_infra/
├── core_logic/          # APENAS lógica principal de negócio
├── tests/               # Testes de integração (mantém atual + move de core_logic)
├── scripts/             # Scripts utilitários e demos (mantém atual + move de core_logic)
├── results_and_reports/ # Relatórios e resultados (renomear para padrão snake_case)
└── outros diretórios...
```

## Categorização dos Arquivos em core_logic/

### 🔧 MANTER em core_logic/ (Lógica Principal):
- `constants.py` - Constantes do sistema
- `embedding_model.py` - Modelo de embedding
- `mcp_server.py` - Servidor MCP principal
- `rag_indexer.py` - Indexador RAG
- `rag_retriever.py` - Recuperador RAG
- `pytorch_gpu_retriever.py` - Recuperador GPU otimizado
- `pytorch_optimizations.py` - Otimizações PyTorch
- `torch_utils.py` - Utilitários PyTorch
- `rag_metrics_integration.py` - Integração de métricas
- `rag_metrics_monitor.py` - Monitor de métricas

### 🧪 MOVER para tests/ (Testes de Integração):
- `test_gpu_alternatives.py`
- `test_pytorch_gpu_retriever.py`
- `test_rag_final_integration.py`
- `test_rag_integration.py`
- `test_rag_simple.py`
- `verificar_faiss_gpu.py` (teste de verificação)

### 📜 MOVER para scripts/ (Scripts e Demos):
- `benchmark_pytorch_performance.py` - Script de benchmark
- `convert_faiss_to_pytorch.py` - Script de conversão
- `demo_rag_system.py` - Demo do sistema

### 📊 MOVER para results_and_reports/ (Relatórios e Resultados):
- `GPU_OPTIMIZATION_REPORT.md`
- `pytorch_performance_benchmark.json`
- `rag_final_integration_results.json`
- `constants.py.backup` (backup)

### 📁 MANTER cache/ em core_logic/
- Diretório cache permanece em core_logic pois é usado pela lógica principal

## Ações a Executar:

1. ✅ Criar este plano de reorganização
2. ✅ Renomear `results and reports/` para `results_and_reports/`
3. ✅ Mover arquivos de teste de `core_logic/` para `tests/`
4. ✅ Mover scripts e demos de `core_logic/` para `scripts/`
5. ✅ Mover relatórios de `core_logic/` para `results_and_reports/`
6. ⏳ Atualizar imports nos arquivos movidos
7. ⏳ Executar testes para validar reorganização
8. ⏳ Atualizar documentação

## ✅ REORGANIZAÇÃO CONCLUÍDA

**Data de Conclusão:** 2025-06-18
**Status:** Estrutura de diretórios reorganizada com sucesso

### Arquivos Movidos:

**Para `tests/`:**
- `test_gpu_alternatives.py`
- `test_pytorch_gpu_retriever.py`
- `test_rag_final_integration.py`
- `test_rag_integration.py`
- `test_rag_simple.py`
- `verificar_faiss_gpu.py`

**Para `scripts/`:**
- `benchmark_pytorch_performance.py`
- `convert_faiss_to_pytorch.py`
- `demo_rag_system.py`

**Para `results_and_reports/`:**
- `GPU_OPTIMIZATION_REPORT.md`
- `pytorch_performance_benchmark.json`
- `rag_final_integration_results.json`
- `constants.py.backup`

### Arquivos Mantidos em `core_logic/`:
- `constants.py` - Constantes do sistema
- `embedding_model.py` - Modelo de embedding
- `mcp_server.py` - Servidor MCP principal
- `pytorch_gpu_retriever.py` - Recuperador GPU otimizado
- `pytorch_optimizations.py` - Otimizações PyTorch
- `rag_indexer.py` - Indexador RAG
- `rag_metrics_integration.py` - Integração de métricas
- `rag_metrics_monitor.py` - Monitor de métricas
- `rag_retriever.py` - Recuperador RAG
- `torch_utils.py` - Utilitários PyTorch
- `cache/` - Diretório de cache

## Considerações Importantes:

- **Imports:** Todos os imports relativos precisarão ser atualizados
- **Paths:** Scripts que referenciam paths absolutos precisarão ser ajustados
- **Testes:** Configuração de pytest pode precisar de ajustes
- **MCP Server:** Verificar se paths do servidor MCP continuam funcionais

---
**Próximo Passo:** Executar renomeação e movimentação de arquivos