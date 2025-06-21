# Utilitários e Resultados - Sistema RAG

Esta pasta contém utilitários diversos e arquivos de resultados do sistema RAG.

## Arquivos de Resultados

### `rag_validation_results.json`
**Descrição:** Resultados da validação completa do sistema RAG.

**Conteúdo:**
- Métricas de performance
- Resultados de qualidade contextual
- Status da integração MCP
- Timestamps de execução
- Configurações utilizadas

**Estrutura:**
```json
{
  "timestamp": "2025-06-18T18:45:00Z",
  "performance": {
    "connectivity": "excellent",
    "response_time": 0.15,
    "success_rate": 1.0
  },
  "quality": {
    "contextual_relevance": "excellent",
    "accuracy_score": 0.95
  },
  "mcp_integration": {
    "status": "ready",
    "server_available": true
  }
}
```

## Utilitários

### Scripts de Análise
Esta pasta pode conter scripts para:
- Análise de resultados de validação
- Geração de relatórios
- Processamento de logs
- Métricas de performance

### Dados Temporários
- Caches de consultas
- Resultados intermediários
- Arquivos de backup

## Como Usar

### Visualizar Resultados
```bash
# Ver resultados da última validação
cat utils/rag_validation_results.json | jq .

# Extrair métricas específicas
cat utils/rag_validation_results.json | jq '.performance'
```

### Análise de Performance
```python
import json

# Carregar resultados
with open('utils/rag_validation_results.json', 'r') as f:
    results = json.load(f)

# Analisar performance
print(f"Performance: {results['performance']['connectivity']}")
print(f"Tempo de resposta: {results['performance']['response_time']}s")
```

## Manutenção

### Limpeza Periódica
```bash
# Remover arquivos antigos (mais de 30 dias)
find utils/ -name "*.json" -mtime +30 -delete

# Manter apenas os 10 resultados mais recentes
ls -t utils/rag_validation_results_*.json | tail -n +11 | xargs rm -f
```

### Backup
```bash
# Backup dos resultados importantes
cp utils/rag_validation_results.json backup/validation_$(date +%Y%m%d).json
```

## Desenvolvimento

Para adicionar novos utilitários:

1. Crie scripts na pasta `utils/`
2. Use nomenclatura descritiva
3. Documente a funcionalidade
4. Inclua exemplos de uso
5. Considere rotação de arquivos para evitar acúmulo