# Guia de Configuração MCP para Trae IDE - Sistema RAG Recoloca.ai

Data: 2025-06-20

## 📋 Resumo dos Problemas Identificados

A configuração original do MCP apresentava alguns problemas:

1. **Caminho absoluto no comando**: Usar caminho absoluto para o script Python pode causar problemas de portabilidade
2. **PYTHONPATH complexo**: Múltiplos caminhos no PYTHONPATH podem causar conflitos de importação
3. **Falta de isolamento de dependências**: Não há garantia de que todas as dependências estejam disponíveis
4. **Problema UVX**: UVX requer `pyproject.toml` ou `setup.py` para funcionar corretamente
5. **Sintaxe UVX**: Argumentos `--from .` causam conflitos de resolução de dependências
6. **Problema de Interpretação de Caminho**: Trae IDE não respeitando `cwd` corretamente

## 🔧 Soluções Propostas

### 1. 🌟 **RECOMENDADA**: Configuração Simples (`trae_mcp_config_simple.json`)

**Vantagens:**
- Máxima compatibilidade
- Configuração direta e confiável
- PYTHONPATH otimizado para todos os módulos
- Não depende de ferramentas externas
- **CORREÇÃO**: Usa caminho absoluto completo no `args`

**Arquivo:** `trae_mcp_config_simple.json`

**Alternativa com Barras Normais:** 📁 `trae_mcp_config_simple_forward_slash.json`
- Mesma configuração, mas usando `/` em vez de `\` nos caminhos
- Pode resolver problemas de interpretação em alguns sistemas

### 2. **AVANÇADA**: Configuração com UVX (`trae_mcp_config_final.json`)

**Vantagens:**
- Isolamento completo de dependências
- Conformidade com práticas modernas do MCP
- Gestão automática de ambiente virtual

**Requisitos:**
- `pyproject.toml` criado
- UVX instalado e funcionando

**Arquivo:** `trae_mcp_config_final.json`

```json
{
  "mcpServers": {
    "recoloca-rag": {
      "command": "uvx",
      "args": [
        "--from", ".",
        "--with-requirements", "requirements.txt",
        "python", "server/mcp_server.py"
      ],
      "cwd": "C:\\Users\\rosas\\OneDrive\\Documentos\\Obisidian DB\\🟢 Projects\\Projects/Recoloca.AI\\rag_infra",
      "env": {
        "PYTHONPATH": ".",
        "CUDA_VISIBLE_DEVICES": "0",
        "RAG_CONFIG_PATH": "config/rag_optimization_config.json",
        "RAG_DATA_PATH": "data",
        "RAG_LOGS_PATH": "logs"
      }
    }
  }
}
```

**Vantagens**:
- ✅ Isolamento automático de dependências
- ✅ Gerenciamento automático do ambiente Python
- ✅ Caminhos relativos mais limpos
- ✅ Seguindo as melhores práticas do Trae IDE

### 3. **ALTERNATIVA**: Configuração Python Direto (`trae_mcp_config_python_direct.json`)

**Vantagens:**
- Configuração intermediária
- PYTHONPATH simplificado

**Arquivo:** `trae_mcp_config_python_direct.json`

```json
{
  "mcpServers": {
    "recoloca-rag": {
      "command": "python",
      "args": ["server/mcp_server.py"],
      "cwd": "C:\\Users\\rosas\\OneDrive\\Documentos\\Obisidian DB\\🟢 Projects\\Projects/Recoloca.AI\\rag_infra",
      "env": {
        "PYTHONPATH": "C:\\Users\\rosas\\OneDrive\\Documentos\\Obisidian DB\\🟢 Projects\\Projects/Recoloca.AI\\rag_infra;..."
      }
    }
  }
}
```

**Vantagens**:
- ✅ Usa o Python do sistema
- ✅ Define diretório de trabalho correto
- ✅ PYTHONPATH mais completo

## 📦 Dependências Criadas

Criamos um arquivo `requirements.txt` com todas as dependências necessárias:

```txt
# Core MCP and AI dependencies
mcp>=1.0.0
sentence-transformers>=2.2.0
faiss-cpu>=1.7.0
torch>=2.0.0
transformers>=4.30.0

# Data processing
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0

# Environment and utilities
python-dotenv>=1.0.0
pyyaml>=6.0
requests>=2.31.0

# Logging and monitoring
loguru>=0.7.0

# File processing
chardet>=5.0.0
python-magic>=0.4.27
```

## 🚀 Próximos Passos

### Para Configuração Simples (Recomendada):

1. **Usar a configuração simples**:
   - Copie o conteúdo de `trae_mcp_config_simple.json`
   - Cole no arquivo de configuração do Trae IDE

2. **Verificar dependências**:
   ```bash
   cd "C:\Users\rosas\OneDrive\Documentos\Obisidian DB\Projects/Recoloca.AI\rag_infra"
   pip install -r requirements.txt
   ```

3. **Testar a conexão**:
   - Reinicie o Trae IDE
   - Verifique se o servidor MCP está funcionando

### Para Configuração UVX (Avançada):

1. **Instalar UVX** (se não estiver instalado):
   ```bash
   pip install uvx
   ```

2. **Usar a configuração UVX**:
   - Copie o conteúdo de `trae_mcp_config_final.json`
   - Cole no arquivo de configuração do Trae IDE
   - O `pyproject.toml` já foi criado

3. **Testar a conexão**:
   - Reinicie o Trae IDE
   - Verifique se o servidor MCP está funcionando

### Para Configuração Python Direto:

1. **Verificar ambiente Python**:
   - Certifique-se de que todas as dependências estão instaladas
   - Verifique se o Python está no PATH

2. **Usar a configuração alternativa**:
   - Copie o conteúdo de `trae_mcp_config_python_direct.json`
   - Cole no arquivo de configuração do Trae IDE

## 🔍 Diagnóstico de Problemas

### Problema: "python: can't open file 'C:\\Users\\rosas\\server\\mcp_server.py'"
**Causa**: Trae IDE não está respeitando o `cwd` e está interpretando caminhos relativos incorretamente
**Solução**: 
1. Use caminho absoluto completo no campo `args`
2. Exemplo: `"C:\\Users\\rosas\\OneDrive\\...\\server\\mcp_server.py"`
3. Alternativa: Use barras normais `/` em vez de barras duplas `\\`

### Problema: "name 'get_retriever' is not defined"
**Causa**: Problemas de importação ou inicialização do módulo
**Solução**: 
1. Verificar se todas as dependências estão instaladas
2. Usar a configuração com UVX para isolamento
3. Verificar se o PYTHONPATH está correto

### Problema: "Failed to resolve `--with` requirement"
**Causa**: UVX não encontra `pyproject.toml` ou `setup.py`
**Solução**: Use a configuração simples ou crie `pyproject.toml`

### Problema: "No module named 'rag_infra'"
**Causa**: PYTHONPATH não configurado corretamente
**Solução**: Verifique os caminhos no PYTHONPATH

### Problema: Módulo não encontrado
**Causa**: PYTHONPATH incorreto ou dependências faltando
**Solução**:
1. Usar `cwd` para definir diretório de trabalho
2. Simplificar PYTHONPATH para "."
3. Instalar dependências via requirements.txt

### Servidor não inicia
**Causa**: Dependências não instaladas
**Solução**: Execute `pip install -r requirements.txt`

## 📚 Referências

- [Documentação oficial do Trae IDE MCP](https://docs.trae.ai/ide/model-context-protocol)
- [Documentação do UVX](https://docs.astral.sh/uv/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## ✅ Recomendação Final

**Use a configuração `trae_mcp_config_final.json`** que utiliza UVX com requirements.txt. Esta é a abordagem mais robusta e segue as melhores práticas recomendadas pela documentação do Trae IDE.