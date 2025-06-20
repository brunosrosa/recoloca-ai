# Configurações - Sistema RAG

Esta pasta contém arquivos de configuração para o sistema RAG.

## Arquivos de Configuração

### `environment.yml`
**Descrição:** Arquivo de configuração do ambiente Conda com todas as dependências necessárias.

**Uso:**
```bash
conda env create -f config/environment.yml
conda activate rag_env
```

**Dependências Principais:**
- Python 3.11+
- PyTorch com suporte CUDA
- Transformers (Hugging Face)
- FAISS (CPU e GPU)
- Watchdog para monitoramento
- MCP para integração

### `trae_mcp_config.json`
**Descrição:** Configuração do servidor MCP para integração com Trae IDE.

**Uso:**
- Copie este arquivo para a configuração do Trae IDE
- Configure o caminho do servidor MCP
- Reinicie o Trae IDE

**Estrutura:**
```json
{
  "mcpServers": {
    "rag-system": {
      "command": "python",
      "args": ["path/to/mcp_server.py"],
      "env": {
        "PYTHONPATH": "path/to/rag_infra"
      }
    }
  }
}
```

## Configuração do Ambiente

### 1. Ambiente Conda
```bash
# Criar ambiente
conda env create -f config/environment.yml

# Ativar ambiente
conda activate rag_env

# Verificar instalação
python -c "import torch; print(f'CUDA disponível: {torch.cuda.is_available()}')"
```

### 2. Configuração MCP
```bash
# Copiar configuração para Trae IDE
cp config/trae_mcp_config.json ~/.trae/mcp_config.json

# Ou configurar manualmente no Trae IDE
```

### 3. Variáveis de Ambiente
```bash
# Adicionar ao .bashrc ou .zshrc
export PYTHONPATH="$PYTHONPATH:/path/to/rag_infra"
export RAG_ROOT_DIR="/path/to/rag_infra"
```

## Personalização

### Modificar Dependências
1. Edite `environment.yml`
2. Recrie o ambiente:
   ```bash
   conda env remove -n rag_env
   conda env create -f config/environment.yml
   ```

### Configurar MCP
1. Edite `trae_mcp_config.json`
2. Ajuste caminhos para seu sistema
3. Reinicie o Trae IDE

## Troubleshooting

### Problemas Comuns
- **CUDA não detectado:** Verifique instalação do PyTorch com CUDA
- **MCP não conecta:** Verifique caminhos no arquivo de configuração
- **Dependências faltando:** Recrie o ambiente Conda