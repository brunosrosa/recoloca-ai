# Recoloca.AI FastAPI Backend

🚀 **Backend API robusta e escalável para a plataforma Recoloca.AI**

API RESTful construída com FastAPI que oferece funcionalidades de busca semântica, autenticação JWT, rate limiting e integração com sistema RAG para coaching de carreira com IA.

## 📋 Funcionalidades

### ✅ Implementado
- **Sistema RAG Integrado**: Consultas semânticas na base de conhecimento
- **Autenticação JWT**: Sistema completo com tokens de acesso e refresh
- **Rate Limiting**: Controle de requisições por usuário/IP com Redis
- **Logging Estruturado**: Logs em JSON com correlação de requisições
- **Middleware Avançado**: Segurança, CORS, tratamento de erros
- **Health Checks**: Monitoramento de saúde da API e serviços
- **Configuração Flexível**: Gerenciamento via variáveis de ambiente

### 🔄 Em Desenvolvimento
- Sistema de autenticação completo
- Gestão de vagas e candidaturas
- Perfil de usuário e preferências
- Sistema Kanban para acompanhamento
- Coach de IA personalizado
- Integração com Stripe para pagamentos

## 🏗️ Arquitetura

```
src/backend_fastapi/
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências Python
├── .env.example           # Exemplo de variáveis de ambiente
└── app/
    ├── __init__.py
    ├── api/                # Endpoints da API
    │   ├── __init__.py
    │   ├── dependencies/   # Dependências compartilhadas
    │   │   ├── auth.py     # Autenticação JWT
    │   │   └── rate_limit.py # Rate limiting
    │   └── v1/
    │       ├── api.py      # Roteador principal v1
    │       └── endpoints/
    │           └── rag.py  # Endpoints RAG
    ├── core/               # Configurações centrais
    │   ├── config.py       # Configurações da aplicação
    │   ├── logging.py      # Sistema de logging
    │   └── middleware.py   # Middlewares customizados
    └── services/           # Serviços de negócio
        └── rag_service.py  # Serviço RAG
```

## 🚀 Início Rápido

### 1. Pré-requisitos

- Python 3.11+
- Redis (para cache e rate limiting)
- Acesso ao Supabase (banco de dados)

### 2. Configuração do Ambiente

```bash
# Clone o repositório (se necessário)
cd src/backend_fastapi

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração das Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com suas configurações
# Especialmente importante:
# - SUPABASE_URL e SUPABASE_ANON_KEY
# - SECRET_KEY e JWT_SECRET_KEY
# - REDIS_URL
```

### 4. Executar a Aplicação

```bash
# Desenvolvimento (com auto-reload)
python main.py

# Ou usando uvicorn diretamente
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Acessar a Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🔧 Configuração

### Variáveis de Ambiente Principais

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `APP_NAME` | Nome da aplicação | "Recoloca.AI API" |
| `ENVIRONMENT` | Ambiente (development/staging/production) | "development" |
| `DEBUG` | Modo debug | `true` |
| `HOST` | Host do servidor | "0.0.0.0" |
| `PORT` | Porta do servidor | `8000` |
| `SECRET_KEY` | Chave secreta da aplicação | **OBRIGATÓRIO** |
| `SUPABASE_URL` | URL do Supabase | **OBRIGATÓRIO** |
| `SUPABASE_ANON_KEY` | Chave anônima do Supabase | **OBRIGATÓRIO** |
| `REDIS_URL` | URL do Redis | "redis://localhost:6379/0" |
| `RAG_ENABLED` | Habilitar sistema RAG | `true` |

### Configuração do Sistema RAG

```env
RAG_ENABLED=true
RAG_TIMEOUT=30
RAG_CACHE_TTL=3600
RAG_MAX_RESULTS=10
RAG_MIN_SCORE=0.2
```

### Rate Limiting

```env
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS_PER_MINUTE=60
RATE_LIMIT_BURST=10
```

## 📡 Endpoints da API

### Sistema RAG

- `POST /api/v1/rag/query` - Consulta semântica
- `GET /api/v1/rag/documents/{document_id}` - Recuperar documento
- `GET /api/v1/rag/status` - Status do sistema RAG
- `POST /api/v1/rag/reindex` - Reindexar base (admin)
- `GET /api/v1/rag/categories` - Listar categorias
- `GET /api/v1/rag/metrics` - Métricas de uso (admin)

### Health Checks

- `GET /` - Status básico da API
- `GET /health` - Health check detalhado

## 🔐 Autenticação

O sistema utiliza JWT (JSON Web Tokens) para autenticação:

```python
# Headers necessários
Authorization: Bearer <access_token>
```

### Tiers de Usuário

- **FREE**: Acesso básico com rate limiting
- **PREMIUM**: Acesso expandido
- **ADMIN**: Acesso completo a endpoints administrativos

## 🛡️ Segurança

### Middlewares de Segurança

- **CORS**: Configurado para origens permitidas
- **Trusted Host**: Validação de hosts em produção
- **Rate Limiting**: Proteção contra abuso
- **Request ID**: Rastreamento de requisições
- **Security Headers**: CSP, HSTS, X-Frame-Options

### Boas Práticas Implementadas

- Validação rigorosa com Pydantic
- Logs estruturados para auditoria
- Tratamento global de erros
- Timeouts configuráveis
- Cache inteligente com TTL

## 📊 Monitoramento

### Logs Estruturados

```json
{
  "timestamp": "2025-01-20T10:30:00Z",
  "level": "INFO",
  "service": "recoloca-api",
  "version": "1.0.0",
  "environment": "production",
  "request_id": "req_123456",
  "user_id": "user_789",
  "endpoint": "/api/v1/rag/query",
  "method": "POST",
  "status_code": 200,
  "duration_ms": 150,
  "message": "RAG query completed successfully"
}
```

### Health Checks

```bash
# Verificar saúde da API
curl http://localhost:8000/health

# Resposta esperada
{
  "status": "healthy",
  "version": "1.0.0",
  "environment": "development",
  "services": {
    "api": "healthy",
    "rag": "healthy"
  },
  "rag_details": {
    "initialized": true,
    "document_count": 150,
    "last_error": null
  }
}
```

## 🧪 Testes

```bash
# Executar testes (quando implementados)
pytest

# Com cobertura
pytest --cov=app

# Testes específicos
pytest tests/test_rag.py
```

## 🚀 Deploy

### Desenvolvimento

```bash
python main.py
```

### Produção

```bash
# Com Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# Com Docker (quando disponível)
docker build -t recoloca-api .
docker run -p 8000:8000 recoloca-api
```

## 🔄 Próximos Passos

### Prioridade Alta
1. **Sistema de Autenticação Completo**
   - Registro e login de usuários
   - Gestão de perfis
   - Integração com Supabase Auth

2. **Gestão de Vagas**
   - CRUD de vagas
   - Sistema de candidaturas
   - Matching inteligente

3. **Testes Automatizados**
   - Testes unitários
   - Testes de integração
   - Testes de carga

### Prioridade Média
1. **Sistema Kanban**
   - Acompanhamento de candidaturas
   - Workflow personalizado

2. **Coach de IA**
   - Integração com modelos de IA
   - Personalização por usuário

3. **Métricas e Analytics**
   - Dashboard de métricas
   - Análise de uso

## 🤝 Contribuição

1. Siga os padrões de código estabelecidos
2. Adicione testes para novas funcionalidades
3. Mantenha a documentação atualizada
4. Use commits semânticos

## 📞 Suporte

Para questões técnicas ou suporte:
- **Documentação**: Consulte os arquivos em `/docs`
- **Issues**: Abra uma issue no repositório
- **Contato**: Entre em contato com a equipe de desenvolvimento

---

**Desenvolvido com ❤️ pela equipe Recoloca.AI**