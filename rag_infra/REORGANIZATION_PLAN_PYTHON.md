# Plano de Reorganização dos Arquivos Python - RAG Infra

## 📋 Situação Atual

Arquivos Python na raiz do `rag_infra` que precisam ser reorganizados:

### Arquivos Identificados:
1. `correcao_rag.py` - Script de correção do sistema RAG
2. `diagnostico_rag.py` - Script de diagnóstico completo
3. `diagnostico_simples.py` - Script de diagnóstico simplificado
4. `mcp_server.py` - Servidor MCP para integração
5. `setup_rag.py` - Script de configuração inicial
6. `test_rag_quick.py` - Teste rápido do sistema

## 🎯 Estrutura de Reorganização Proposta

### 1. Subpasta `diagnostics/`
**Finalidade:** Scripts de diagnóstico e correção do sistema
- `correcao_rag.py` → `diagnostics/correcao_rag.py`
- `diagnostico_rag.py` → `diagnostics/diagnostico_rag.py`
- `diagnostico_simples.py` → `diagnostics/diagnostico_simples.py`

### 2. Subpasta `server/`
**Finalidade:** Componentes de servidor e integração
- `mcp_server.py` → `server/mcp_server.py`

### 3. Subpasta `setup/`
**Finalidade:** Scripts de configuração e inicialização
- `setup_rag.py` → `setup/setup_rag.py`

### 4. Manter em `tests/`
**Finalidade:** Testes rápidos (já existe estrutura)
- `test_rag_quick.py` → `tests/test_rag_quick.py`

## 🔧 Benefícios da Reorganização

1. **Organização Funcional:** Agrupamento por propósito
2. **Facilidade de Navegação:** Estrutura mais clara
3. **Manutenibilidade:** Localização intuitiva dos arquivos
4. **Escalabilidade:** Estrutura preparada para crescimento
5. **Consistência:** Padrão organizacional uniforme

## 📁 Estrutura Final Esperada

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
└── ... (outras pastas existentes)
```

## ⚠️ Considerações de Implementação

1. **Imports:** Verificar e ajustar imports relativos
2. **Paths:** Atualizar referências de caminhos nos scripts
3. **Configuração:** Atualizar `config.py` se necessário
4. **Documentação:** Atualizar READMEs das subpastas
5. **Testes:** Verificar se os scripts funcionam após a movimentação

## 🚀 Próximos Passos

1. Criar as subpastas necessárias
2. Criar arquivos `__init__.py` em cada subpasta
3. Mover os arquivos para suas respectivas subpastas
4. Ajustar imports e paths conforme necessário
5. Testar funcionalidade após reorganização
6. Atualizar documentação