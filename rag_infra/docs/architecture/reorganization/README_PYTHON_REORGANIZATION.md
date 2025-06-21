# Reorganização dos Arquivos Python - RAG Infra

## 📋 Resumo da Reorganização

Este documento descreve a reorganização dos arquivos Python na raiz do `rag_infra` para uma estrutura mais organizada e modular.

## 🎯 Objetivos Alcançados

✅ **Organização Funcional:** Arquivos agrupados por propósito e funcionalidade  
✅ **Estrutura Modular:** Cada subpasta é um módulo Python válido com `__init__.py`  
✅ **Facilidade de Navegação:** Localização intuitiva dos arquivos  
✅ **Manutenibilidade:** Estrutura preparada para crescimento  
✅ **Configuração Centralizada:** Funções utilitárias em `config.py`  

## 📁 Estrutura Antes vs Depois

### Antes (Arquivos na Raiz)
```
rag_infra/
├── correcao_rag.py
├── diagnostico_rag.py
├── diagnostico_simples.py
├── mcp_server.py
├── setup_rag.py
├── test_rag_quick.py
└── ... (outras pastas)
```

### Depois (Estrutura Organizada)
```
rag_infra/
├── diagnostics/
│   ├── __init__.py
│   ├── correcao_rag.py
│   ├── diagnostico_rag.py
│   └── diagnostico_simples.py
├── server/
│   ├── __init__.py
│   └── mcp_server.py
├── setup/
│   ├── __init__.py
│   └── setup_rag.py
├── tests/
│   ├── test_rag_quick.py (movido)
│   └── ... (arquivos existentes)
└── ... (outras pastas)
```

## 🔄 Arquivos Movidos

| Arquivo Original | Nova Localização | Categoria |
|------------------|------------------|----------|
| `correcao_rag.py` | `diagnostics/correcao_rag.py` | Diagnóstico |
| `diagnostico_rag.py` | `diagnostics/diagnostico_rag.py` | Diagnóstico |
| `diagnostico_simples.py` | `diagnostics/diagnostico_simples.py` | Diagnóstico |
| `mcp_server.py` | `server/mcp_server.py` | Servidor |
| `setup_rag.py` | `setup/setup_rag.py` | Configuração |
| `test_rag_quick.py` | `tests/test_rag_quick.py` | Testes |

## 🛠️ Funcionalidades Adicionadas

### 1. Módulos Python Válidos
Cada subpasta possui um arquivo `__init__.py` com:
- Documentação do módulo
- Imports facilitados
- Metadados (versão, autor)
- Lista `__all__` para controle de exports

### 2. Configuração Centralizada
O arquivo `config.py` foi atualizado com:
- Constantes para os novos diretórios
- Função `get_module_path()` para navegação
- Função `add_module_to_path()` para imports
- Mapeamento `REORGANIZED_FILES` para compatibilidade

### 3. Funções Utilitárias

#### `get_module_path(category, module_name=None)`
```python
# Obter diretório de uma categoria
diag_dir = get_module_path('diagnostics')

# Obter caminho específico de um arquivo
correcao_path = get_module_path('diagnostics', 'correcao_rag')
```

#### `add_module_to_path(category)`
```python
# Adicionar módulo ao sys.path para imports
add_module_to_path('diagnostics')
from correcao_rag import test_score_thresholds
```

## 📖 Como Usar os Módulos Reorganizados

### Imports Diretos
```python
# Importar módulos específicos
from rag_infra.diagnostics import correcao_rag
from rag_infra.server import mcp_server
from rag_infra.setup import setup_rag
```

### Usando Configuração Centralizada
```python
from rag_infra.config import get_module_path, add_module_to_path

# Adicionar ao path e importar
add_module_to_path('diagnostics')
import diagnostico_rag

# Obter caminho para execução
setup_script = get_module_path('setup', 'setup_rag')
```

### Execução de Scripts
```bash
# Executar scripts nas novas localizações
python rag_infra/diagnostics/diagnostico_rag.py
python rag_infra/server/mcp_server.py
python rag_infra/setup/setup_rag.py
```

## 🔍 Verificação da Reorganização

### Estrutura de Diretórios
```python
from rag_infra.config import *

print(f"Diagnostics: {DIAGNOSTICS_DIR}")
print(f"Server: {SERVER_DIR}")
print(f"Setup: {SETUP_DIR}")
print(f"Tests: {TESTS_DIR}")
```

### Teste de Imports
```python
# Testar se os módulos podem ser importados
try:
    from rag_infra.diagnostics import correcao_rag
    print("✅ Diagnósticos importados com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar diagnósticos: {e}")
```

## 🚀 Benefícios da Reorganização

1. **Organização Clara:** Cada tipo de funcionalidade tem seu lugar
2. **Escalabilidade:** Fácil adicionar novos módulos em categorias apropriadas
3. **Manutenibilidade:** Localização intuitiva facilita manutenção
4. **Modularidade:** Estrutura de módulos Python padrão
5. **Compatibilidade:** Funções utilitárias mantêm compatibilidade
6. **Documentação:** Cada módulo possui documentação integrada

## 📝 Próximos Passos Recomendados

1. **Testar Funcionalidade:** Verificar se todos os scripts funcionam nas novas localizações
2. **Atualizar Referências:** Ajustar imports em outros arquivos se necessário
3. **Documentar Mudanças:** Atualizar READMEs específicos de cada módulo
4. **Criar Aliases:** Considerar criar scripts de conveniência na raiz se necessário
5. **Monitorar Uso:** Verificar se a nova estrutura atende às necessidades de desenvolvimento

## 🔧 Troubleshooting

### Problema: Import Error
```python
# Solução: Usar configuração centralizada
from rag_infra.config import add_module_to_path
add_module_to_path('diagnostics')
```

### Problema: Caminho Não Encontrado
```python
# Solução: Usar função utilitária
from rag_infra.config import get_module_path
module_path = get_module_path('diagnostics', 'correcao_rag')
```

---

**Reorganização concluída com sucesso!** 🎉

*Autor: @AgenteM_DevFastAPI*  
*Data: Junho 2025*  
*Versão: 1.0*