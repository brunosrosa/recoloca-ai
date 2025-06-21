# Configurações - RAG Infrastructure

Centralização de todas as configurações do sistema.

## Estrutura

- `environments/`: Configurações por ambiente (dev, staging, prod)
- `models/`: Configurações de modelos de IA
- `logging/`: Configurações de logging

## Segurança

Nunca commite arquivos com credenciais ou chaves de API.
Use variáveis de ambiente para dados sensíveis.