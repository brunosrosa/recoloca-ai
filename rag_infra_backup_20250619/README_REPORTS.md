# 📊 Sistema de Relatórios RAG - Configuração Centralizada

## 🎯 Objetivo

Este documento descreve a implementação da configuração centralizada para relatórios do sistema RAG, garantindo que todos os arquivos `*report.json` sejam criados no diretório correto: `rag_infra/results_and_reports/`.

## 📁 Estrutura de Diretórios

```
rag_infra/
├── config.py                 # ✅ Configuração centralizada
├── results_and_reports/       # 📊 Todos os relatórios aqui
│   ├── rag_final_test_report.json
│   ├── rag_diagnosis_report.json
│   ├── index_rebuild_report.json
│   └── ...
├── scripts/                   # 🔧 Scripts modificados
│   ├── test_rag_final.py     # ✅ Usa config centralizada
│   ├── diagnose_rag_issues.py # ✅ Usa config centralizada
│   ├── rebuild_index.py      # ✅ Usa config centralizada
│   ├── fix_rag_issues.py     # ✅ Usa config centralizada
│   └── fix_index_loading.py  # ✅ Usa config centralizada
└── logs/                      # 📝 Logs do sistema
```

## 🔧 Configuração Implementada

### Arquivo `config.py`

Criado arquivo de configuração centralizada com:

- **Caminhos padronizados**: Todos os relatórios vão para `results_and_reports/`
- **Funções utilitárias**: `get_report_path()` e `get_log_path()`
- **Configurações de formato**: Encoding, indentação, etc.
- **Configurações RAG**: Parâmetros do modelo e sistema

### Scripts Modificados

Todos os scripts que geram relatórios foram atualizados para usar a configuração centralizada:

1. **test_rag_final.py** - Relatórios de teste final
2. **diagnose_rag_issues.py** - Diagnósticos do sistema
3. **rebuild_index.py** - Reconstrução de índices
4. **fix_rag_issues.py** - Correções de problemas
5. **fix_index_loading.py** - Correções de carregamento

## 📋 Arquivos Movidos

Os seguintes arquivos foram movidos da raiz para `results_and_reports/`:

- `index_rebuild_report.json` → `index_rebuild_report_moved.json`
- `rag_diagnosis_report.json` → `rag_diagnosis_report_moved.json`
- `rag_final_test_report.json` → `rag_final_test_report_moved.json`

## 🚀 Como Usar

### Para Desenvolvedores

```python
# Em qualquer script que precise gerar relatórios
from config import get_report_path, REPORT_CONFIG
import json

# Gerar caminho do relatório
report_path = get_report_path("meu_relatorio.json")

# Salvar relatório com configurações padronizadas
with open(report_path, 'w', encoding=REPORT_CONFIG['encoding']) as f:
    json.dump(data, f, 
             indent=REPORT_CONFIG['indent'], 
             ensure_ascii=REPORT_CONFIG['ensure_ascii'], 
             default=REPORT_CONFIG['default_serializer'])
```

### Para Novos Scripts

1. Importe a configuração:
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import get_report_path, REPORT_CONFIG
```

2. Use as funções utilitárias:
```python
# Para relatórios
report_path = get_report_path("nome_do_relatorio.json")

# Para logs
log_path = get_log_path("nome_do_log.log")
```

## ✅ Benefícios

1. **Organização**: Todos os relatórios em um local centralizado
2. **Consistência**: Formato e configurações padronizadas
3. **Manutenibilidade**: Mudanças de configuração em um só lugar
4. **Escalabilidade**: Fácil adição de novos tipos de relatório
5. **Automação**: Criação automática de diretórios necessários

## 🔄 Migração Automática

O sistema agora:

- ✅ Cria automaticamente o diretório `results_and_reports/` se não existir
- ✅ Todos os novos relatórios são salvos no local correto
- ✅ Configurações centralizadas para formato e encoding
- ✅ Funções utilitárias para facilitar o desenvolvimento

## 📝 Próximos Passos

1. **Testar scripts modificados** para garantir funcionamento correto
2. **Documentar padrões** para novos desenvolvedores
3. **Criar validação automática** de localização de relatórios
4. **Implementar rotação de logs** se necessário

---

**Nota**: Esta implementação garante que todos os futuros relatórios relacionados ao RAG sejam criados automaticamente no diretório correto, mantendo a organização e consistência do projeto.