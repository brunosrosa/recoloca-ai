# HIGH-LEVEL DESIGN (HLD) DO PROJETO RECOLOCA.AI - VERSÃO RAG

**Versão:** 1.1 | **Data:** Janeiro 2025 | **Status:** Ativo

## Propósito e Escopo

Este documento define a arquitetura de alto nível do sistema Recoloca.ai, uma plataforma SaaS para otimização de currículos e gestão de candidaturas a vagas de emprego, potencializada por IA.

### Escopo do Sistema
- **Frontend PWA:** Interface principal do usuário
- **Backend API:** Lógica de negócios e orquestração
- **BaaS (Supabase):** Banco de dados, autenticação e storage
- **Integração LLM:** Google Gemini via OpenRouter
- **Sistema RAG:** Recuperação de contexto para IA
- **Ferramentas de Automação:** CI/CD e workflows
- **Extensão de Navegador:** Captura de vagas (Pós-MVP)

### Acrônimos e Termos
- **PWA:** Progressive Web Application
- **BaaS:** Backend as a Service
- **RAG:** Retrieval-Augmented Generation
- **LLM:** Large Language Model
- **RLS:** Row Level Security
- **JWT:** JSON Web Token
- **OAuth:** Open Authorization
- **CI/CD:** Continuous Integration/Continuous Deployment

## Paradigma Arquitetural

**Cloud-native, Microservices, Clean Architecture, RLS, OAuth 2.0, horizontal scalability, observability**

## Visão Geral da Arquitetura

### Componentes Principais
- **Landing Page:** Apresentação e marketing (HTML/CSS/JS)
- **Frontend PWA:** Interface principal (Flutter Web)
- **Backend API:** Lógica de negócios (Python/FastAPI)
- **Supabase:** BaaS completo (PostgreSQL, Auth, Storage)
- **Google Gemini:** LLMs via OpenRouter
- **Sistema RAG Local:** Indexação de documentação
- **Agentes de IA:** Assistentes especializados (Trae IDE)
- **Pipedream:** Automação e CI/CD
- **Extensão Chrome:** Captura de vagas (Pós-MVP)

### Ambientes

#### Ambiente de Desenvolvimento/Metodologia
- **Maestro:** Orquestrador humano principal
- **Trae IDE:** Ambiente de desenvolvimento com IA
- **Agentes de IA:** Assistentes especializados
- **RAG Local:** Sistema de recuperação de contexto
- **Obsidian:** Documentação viva
- **Git Repository:** Controle de versão

#### Sistema Recoloca.ai (Produção)
- **Landing Page:** Hospedada no Vercel
- **Frontend PWA:** Hospedado no Vercel
- **Backend API:** Hospedado no Render
- **Supabase:** BaaS gerenciado
- **Google OAuth:** Autenticação social
- **Stripe:** Pagamentos e assinaturas
- **Google Gemini:** APIs de IA via OpenRouter

## DESCRIÇÃO DETALHADA DOS COMPONENTES

### Landing Page e Marketing
- **Tecnologia:** HTML, CSS, JavaScript (vanilla ou framework leve como Alpine.js)
- **Hospedagem:** Vercel (mesmo domínio ou subdomínio do Frontend PWA)
- **Responsabilidades:**
  - Apresentar o produto Recoloca.ai de forma atrativa e convincente
  - Implementar seção Hero com proposta de valor clara e CTA
  - Exibir funcionalidades principais, benefícios e diferenciais
  - Apresentar informações sobre planos (Freemium/Premium) e preços
  - Garantir design responsivo e otimizado para conversão
  - Incluir elementos de credibilidade (depoimentos, estatísticas, garantias)
  - Implementar formulários de captura de leads
- **Interações Chave:**
  - Com o Usuário: Primeira impressão, apresentação do produto
  - Com o Frontend PWA: Redirecionamento via CTAs para registro/login
  - Com ferramentas de Analytics: Tracking de conversões

### Frontend (PWA - Flutter)
- **Tecnologia:** Flutter (Dart), compilado para Web (PWA)
- **Hospedagem:** Vercel
- **Responsabilidades:**
  - Renderizar a interface do usuário (UI) e gerenciar a experiência (UX)
  - Gerenciar o estado da aplicação no lado do cliente
  - Lidar com o fluxo de autenticação OAuth com Google (via Supabase)
  - Redirecionar para o Stripe Checkout e Stripe Customer Portal
  - Realizar chamadas HTTPS/REST para a API Backend
  - Lidar com a entrada do usuário e validações no lado do cliente
  - Implementar a lógica de apresentação das funcionalidades
  - Armazenamento local para preferências do usuário ou cache leve
- **Interações Chave:**
  - Com o Usuário: Recebe inputs, exibe informações
  - Com a API Backend: Envia requisições para operações de dados

### API Backend (Python/FastAPI)
- **Tecnologia:** Python 3.10+, FastAPI
- **Hospedagem:** Render
- **Responsabilidades:**
  - Expor endpoints RESTful seguros para Frontend PWA e Extensão
  - Implementar a lógica de negócios principal da aplicação
  - Orquestrar chamadas para os serviços do Supabase
  - Orquestrar chamadas para as APIs do Google Gemini (via OpenRouter)
  - Integrar-se com o sistema RAG para fornecer contexto aos LLMs
  - Interagir com a API do Stripe para pagamentos
  - Processar webhooks do Stripe para atualizar status das assinaturas
  - Gerenciar a lógica de parsing de PDFs de currículos
  - Implementar a lógica de tiers (Freemium/Premium)
- **Interações Chave:**
  - Com o Frontend PWA/Extensão: Recebe requisições, envia respostas JSON
  - Com o Supabase: Autentica usuários, realiza operações CRUD
  - Com Google Gemini APIs: Envia prompts e recebe respostas geradas
  - Com o Sistema RAG: Acessa o índice vetorial para buscar contexto

### Supabase (BaaS)
- **Tecnologia:** Plataforma BaaS utilizando PostgreSQL
- **Responsabilidades:**
  - **Autenticação:** Gerenciamento de identidades (Email/Senha e Google OAuth)
  - **Banco de Dados:** Persistência de todos os dados da aplicação
  - **Storage:** Armazenamento seguro de arquivos (PDFs de currículos)
  - **Realtime:** Para funcionalidades que exigem atualizações em tempo real
- **Interações Chave:**
  - Com a API Backend: Principal consumidor dos serviços do Supabase
  - Com o Frontend PWA: Pode interagir diretamente para autenticação

### Google Gemini LLMs (via OpenRouter)
- **Tecnologia:** Modelos Gemini Pro e Flash da Google
- **Acesso:** Primariamente via OpenRouter para flexibilidade
- **Responsabilidades:**
  - Importação inteligente de vagas (extração de dados de URLs)
  - Categorização semântica de seções de currículos
  - Análise de adequação CV vs. Vaga (Score de Adequação)
  - Geração de sugestões de otimização de CV
  - Estimativa de range salarial
  - Respostas e interações do Coach IA
- **Interações Chave:**
  - Com a API Backend: Recebe prompts enriquecidos com contexto RAG

### Sistema RAG Local (Infraestrutura em rag_infra/)
- **Tecnologias:** LangChain, FAISS-GPU, BAAI/bge-m3, Python, Conda
- **Status:** Componente de núcleo para implementação pós-MVP inicial
- **Responsabilidades Planejadas:**
  - Indexar a "Documentação Viva" (Markdown do Obsidian)
  - Processo: Carregar documentos, dividir em chunks, gerar embeddings
  - Armazenar vetores em índice FAISS-GPU
  - Fornecer consulta para Agentes de IA e Backend API
- **Integração Futura:**
  - Com a "Documentação Viva" (Obsidian): Lerá os documentos fonte
  - Com os Agentes de IA: Permitirá contexto específico do projeto
  - Com a API Backend: Consulta para enriquecer prompts para LLMs

### Agentes de IA (Trae IDE)
- **Tecnologia:** Configurações e prompts customizados no Trae IDE
- **Responsabilidades:**
  - Auxiliar o Maestro em todas as fases do SDLC
  - Utilizar o Sistema RAG para obter contexto do projeto
  - Gerar artefatos sob a supervisão do Maestro (HITL)
- **Interações Chave:**
  - Com o Maestro (via Trae IDE): Recebe instruções, fornece outputs
  - Com o Sistema RAG Local: Obtém contexto
  - Com os LLMs Gemini: Para capacidades de geração e raciocínio

### Pipedream (Automação)
- **Tecnologia:** Plataforma de automação baseada em nuvem
- **Responsabilidades:**
  - **CI/CD:** Automatizar processos de build, teste e deploy
  - **Automação de Tarefas:** Reindexação do RAG, notificações
- **Interações Chave:**
  - Com o Repositório Git: Monitora pushes/merges
  - Com Vercel/Render: Realiza deploys
  - Com o Sistema RAG Local: Pode acionar scripts de reindexação

### Extensão de Navegador (Chrome - Pós-MVP)
- **Tecnologia:** JavaScript, HTML, CSS
- **Responsabilidades:**
  - Permitir captura de informações de vagas de portais de emprego
  - Comunicar-se com a API Backend para enviar dados capturados
- **Interações Chave:**
  - Com o Usuário: Interface para captura e confirmação
  - Com Portais de Emprego: Extrai dados do DOM
  - Com a API Backend: Envia os dados da vaga capturada

## STACK TECNOLÓGICA DETALHADA

### Frontend (Camada de Apresentação)
- **Framework**: Flutter Web 3.x
- **Tipo**: Progressive Web App (PWA)
- **Estado**: Bloc/Cubit pattern
- **Roteamento**: GoRouter
- **HTTP**: Dio client
- **Cache**: Hive (local storage)
- **Responsividade**: Adaptive layouts

### Backend (Camada de Aplicação)
- **Framework**: FastAPI 0.104+
- **Linguagem**: Python 3.11+
- **ASGI Server**: Uvicorn
- **Validação**: Pydantic v2
- **ORM**: SQLAlchemy 2.0 (async)
- **Migrations**: Alembic
- **Cache**: Redis
- **Task Queue**: Celery (futuro)

### Banco de Dados (Camada de Persistência)
- **Primary DB**: Supabase (PostgreSQL 15+)
- **Segurança**: Row Level Security (RLS)
- **Backup**: Automático diário
- **Replicação**: Read replicas (produção)
- **Indexação**: Otimizada para queries frequentes

### Serviços de IA
- **LLM Gateway**: OpenRouter
- **Modelos**: GPT-4, Claude-3, Gemini Pro
- **Embeddings**: OpenAI text-embedding-3-small
- **Vector Store**: Supabase pgvector
- **RAG Framework**: LangChain

### Infraestrutura e Deploy
- **Frontend Deploy**: Vercel
- **Backend Deploy**: Render
- **CDN**: Vercel Edge Network
- **Monitoring**: Sentry + Custom metrics
- **CI/CD**: GitHub Actions

## FLUXOS DE DADOS PRINCIPAIS

### Fluxo 1: Autenticação de Usuário (Google OAuth)
1. **Frontend PWA** → Usuário clica em "Entrar com Google"
2. **Frontend PWA** → **Supabase Auth** (inicia fluxo OAuth)
3. **Supabase Auth** → **Google OAuth** (redirecionamento)
4. **Google OAuth** → **Supabase Auth** (callback com token)
5. **Supabase Auth** → **Frontend PWA** (sessão autenticada)
6. **Frontend PWA** → **API Backend** (requisições com JWT)

### Fluxo 2: Upload e Análise de CV
1. **Frontend PWA** → Usuário faz upload de PDF
2. **Frontend PWA** → **API Backend** (POST /cv/upload)
3. **API Backend** → **Supabase Storage** (armazena PDF)
4. **API Backend** → **PDF Parser** (extrai texto)
5. **API Backend** → **Sistema RAG** (busca contexto)
6. **API Backend** → **Google Gemini** (análise + contexto RAG)
7. **Google Gemini** → **API Backend** (seções categorizadas)
8. **API Backend** → **Supabase DB** (salva dados estruturados)
9. **API Backend** → **Frontend PWA** (resposta JSON)

### Fluxo 3: Importação Inteligente de Vaga
1. **Frontend PWA** → Usuário cola URL da vaga
2. **Frontend PWA** → **API Backend** (POST /jobs/import)
3. **API Backend** → **Web Scraper** (extrai conteúdo da URL)
4. **API Backend** → **Sistema RAG** (busca contexto sobre vagas)
5. **API Backend** → **Google Gemini** (estrutura dados + contexto)
6. **Google Gemini** → **API Backend** (dados estruturados da vaga)
7. **API Backend** → **Supabase DB** (salva vaga)
8. **API Backend** → **Frontend PWA** (vaga importada)

### Fluxo 4: Análise de Adequação CV vs. Vaga
1. **Frontend PWA** → Usuário solicita análise
2. **Frontend PWA** → **API Backend** (POST /analysis/match)
3. **API Backend** → **Supabase DB** (busca CV e vaga)
4. **API Backend** → **Sistema RAG** (contexto sobre análises)
5. **API Backend** → **Google Gemini** (análise + contexto)
6. **Google Gemini** → **API Backend** (score + sugestões)
7. **API Backend** → **Supabase DB** (salva análise)
8. **API Backend** → **Frontend PWA** (resultados)

### Fluxo 5: Processamento de Pagamento (Stripe)
1. **Frontend PWA** → Usuário escolhe plano Premium
2. **Frontend PWA** → **API Backend** (POST /subscription/create)
3. **API Backend** → **Stripe API** (cria Checkout Session)
4. **Stripe API** → **API Backend** (URL do Checkout)
5. **API Backend** → **Frontend PWA** (redirecionamento)
6. **Frontend PWA** → **Stripe Checkout** (processo de pagamento)
7. **Stripe** → **API Backend** (webhook de confirmação)
8. **API Backend** → **Supabase DB** (atualiza status)

## CONSIDERAÇÕES ARQUITETURAIS

### Escalabilidade

#### Plataformas PaaS
- **Frontend (Vercel):** Auto-scaling baseado em tráfego, CDN global
- **Backend (Render):** Auto-scaling horizontal, load balancing automático
- **Supabase:** Managed PostgreSQL com scaling automático

#### LLMs via OpenRouter
- **Flexibilidade:** Acesso a múltiplos provedores (Google, Anthropic, OpenAI)
- **Fallback:** Implementação de fallback entre modelos
- **Rate Limiting:** Controle de uso para evitar custos excessivos

#### Sistema RAG
- **Indexação:** FAISS-GPU para busca vetorial eficiente
- **Chunking:** Estratégia otimizada para documentos técnicos
- **Cache:** Cache de embeddings para consultas frequentes

### Segurança

#### Autenticação e Autorização
- **JWT Tokens:** Supabase gerencia tokens seguros
- **Row Level Security (RLS):** Políticas no PostgreSQL
- **OAuth 2.0:** Integração segura com Google

#### Comunicação
- **HTTPS/TLS:** Todas as comunicações criptografadas
- **CORS:** Configuração restritiva para APIs
- **Rate Limiting:** Proteção contra ataques DDoS

#### Validação de Dados
- **Pydantic:** Validação rigorosa no Backend
- **Sanitização:** Limpeza de inputs para prevenir XSS
- **SQL Injection:** Proteção via ORM (SQLAlchemy)

#### Gerenciamento de Segredos
- **Variáveis de Ambiente:** Chaves API nunca no código
- **Supabase Vault:** Armazenamento seguro de secrets
- **Rotação:** Política de rotação de chaves

#### Segurança Específica para LLMs (OWASP)
- **Prompt Injection:** Sanitização e validação de prompts
- **Data Leakage:** Controle rigoroso de dados sensíveis
- **Model DoS:** Rate limiting e timeouts
- **Supply Chain:** Validação de modelos e APIs

#### Conformidade LGPD
- **Consentimento:** Coleta explícita de consentimento
- **Minimização:** Coleta apenas dados necessários
- **Portabilidade:** Exportação de dados do usuário
- **Exclusão:** Direito ao esquecimento implementado
- **Auditoria:** Logs de acesso e modificação

#### Stripe Security Best Practices
- **Não Armazenar Dados de Cartão:** Stripe gerencia PCI compliance
- **Webhook Verification:** Validação de assinatura dos webhooks
- **Minimal API Keys:** Uso de chaves com privilégios mínimos
- **Idempotency:** Prevenção de cobranças duplicadas

### Performance

#### Frontend
- **Code Splitting:** Carregamento sob demanda
- **Lazy Loading:** Componentes carregados quando necessário
- **PWA Caching:** Cache inteligente de recursos
- **Image Optimization:** Compressão e formatos modernos

#### Backend
- **Async/Await:** Operações não-bloqueantes
- **Connection Pooling:** Reutilização de conexões DB
- **Caching:** Redis para dados frequentemente acessados
- **Database Indexing:** Índices otimizados para queries

#### LLM Performance
- **Model Selection:** Gemini Flash para tarefas rápidas
- **Prompt Optimization:** Prompts concisos e eficientes
- **Batch Processing:** Agrupamento de requisições quando possível
- **Streaming:** Respostas em tempo real quando aplicável

#### RAG Optimization
- **Embedding Cache:** Cache de embeddings computados
- **Chunk Size:** Otimização do tamanho dos chunks
- **Vector Search:** Índices FAISS otimizados
- **Relevance Scoring:** Filtros de relevância

### Manutenibilidade

#### Modularidade
- **Microservices Pattern:** Serviços bem definidos
- **Clean Architecture:** Separação clara de responsabilidades
- **Dependency Injection:** Baixo acoplamento
- **Interface Segregation:** Contratos bem definidos

#### Documentação Viva
- **OpenAPI/Swagger:** Documentação automática da API
- **Obsidian Vault:** Documentação técnica centralizada
- **Code Comments:** Documentação inline do código
- **ADRs:** Registro de decisões arquiteturais

#### Testes Automatizados
- **Unit Tests:** Cobertura >80% do código
- **Integration Tests:** Testes de APIs e integrações
- **E2E Tests:** Fluxos críticos do usuário
- **Load Tests:** Performance sob carga

#### CI/CD
- **GitHub Actions:** Pipeline automatizado
- **Automated Testing:** Testes em cada commit
- **Deployment:** Deploy automático em staging/production
- **Rollback:** Capacidade de rollback rápido

#### Stack Tecnológico Moderno
- **Python 3.10+:** Recursos modernos da linguagem
- **FastAPI:** Framework moderno e performático
- **Flutter:** UI moderna e responsiva
- **Supabase:** BaaS moderno e escalável

#### Monitoramento e Logging
- **Structured Logging:** Logs em formato JSON
- **Error Tracking:** Sentry para tracking de erros
- **Performance Monitoring:** APM para métricas
- **Health Checks:** Endpoints de saúde da aplicação

### Custos

#### Monitoramento de Custos
- **LLM Usage:** Tracking de tokens e requisições
- **Supabase:** Monitoramento de storage e compute
- **Hosting:** Acompanhamento de uso de recursos
- **Third-party APIs:** Controle de chamadas externas

#### Otimização
- **Caching:** Redução de chamadas desnecessárias
- **Efficient Prompts:** Minimização de tokens
- **Resource Scaling:** Scaling baseado em demanda
- **Cost Alerts:** Alertas para gastos excessivos

## IMPLICAÇÕES PARA O LOW-LEVEL DESIGN (LLD)

### Modelos de Dados Detalhados
- **User Schema:** Campos específicos, relacionamentos, índices
- **Job Schema:** Estrutura completa de vagas, metadados
- **CV Schema:** Seções categorizadas, versioning
- **Analysis Schema:** Resultados de análises, histórico
- **Subscription Schema:** Estados de assinatura, billing

### Endpoints Específicos da API Backend
- **Authentication:** `/auth/*` - Login, logout, refresh
- **User Management:** `/users/*` - CRUD de usuários
- **CV Management:** `/cv/*` - Upload, análise, otimização
- **Job Management:** `/jobs/*` - Import, CRUD, search
- **Analysis:** `/analysis/*` - Matching, scoring
- **Subscription:** `/subscription/*` - Stripe integration
- **Coaching:** `/coaching/*` - IA coaching features

### Integrações Detalhadas com APIs Externas
- **Stripe API:** Webhooks, error handling, idempotency
- **Google OAuth:** Scopes, token refresh, error handling
- **OpenRouter:** Model selection, fallbacks, rate limiting
- **Supabase APIs:** Auth, Database, Storage, Realtime

### Componentes de UI Frontend
- **Authentication Components:** Login, signup, profile
- **Dashboard Components:** Overview, metrics, navigation
- **CV Components:** Upload, viewer, editor, analysis
- **Job Components:** Import, kanban, details, matching
- **Subscription Components:** Plans, billing, portal

### Tratamento de Erros
- **API Error Responses:** Códigos HTTP, mensagens padronizadas
- **Frontend Error Handling:** User-friendly messages, retry logic
- **Logging Strategy:** Structured logs, error tracking
- **Fallback Mechanisms:** Graceful degradation

### Gerenciamento Seguro de Chaves API
- **Environment Variables:** Configuração por ambiente
- **Secret Rotation:** Estratégia de rotação automática
- **Access Control:** Princípio do menor privilégio
- **Audit Trail:** Logs de uso de chaves

## RISCOS ARQUITETURAIS E MITIGAÇÕES

### Dependência de APIs Externas
- **Risco:** Indisponibilidade de serviços críticos
- **Mitigação:** Implementação de fallbacks, circuit breakers, timeouts

### Gerenciamento de Estado de Assinatura
- **Risco:** Inconsistências entre Stripe e banco local
- **Mitigação:** Webhooks confiáveis, reconciliação periódica

### Segurança da Integração Stripe
- **Risco:** Vulnerabilidades em pagamentos
- **Mitigação:** Seguir best practices, validação de webhooks

### Complexidade do Sistema RAG
- **Risco:** Performance degradada, resultados irrelevantes
- **Mitigação:** Otimização contínua, métricas de qualidade

### Performance de Parsing de PDF
- **Risco:** Lentidão em uploads grandes
- **Mitigação:** Processamento assíncrono, otimização de bibliotecas

### Custos de APIs Externas
- **Risco:** Gastos excessivos com LLMs
- **Mitigação:** Rate limiting, caching, monitoramento de custos

## HISTÓRICO DE VERSÕES

- **v1.1:** Incorporação de métricas "Specialized Intelligence" e critérios de agentes
- **v1.0:** Versão inicial do HLD

## DOCUMENTOS RELACIONADOS

- [[docs/01_Guias_Centrais/TAP.md]] - Termo de Abertura do Projeto
- [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] - Plano Mestre
- [[rag_infra/source_documents/01_Documentacao_Central/GUIA_AVANCADO_para_RAG.md]] - Guia Avançado
- [[00_Gerenciamento_Projeto/KANBAN/]] - Kanban do Projeto
- [[docs/02_Requisitos/ERS.md]] - Especificação de Requisitos
- [[docs/03_Arquitetura_e_Design/ADR/]] - Architectural Decision Records
- [[docs/03_Arquitetura_e_Design/LLD/]] - Low-Level Designs
- [[docs/04_Metricas/METRICAS_SPECIALIZED_INTELLIGENCE.md]] - Métricas
- [[docs/04_Agentes_IA/02_AGENTES_IA_MENTORES_OVERVIEW.md]] - Perfis dos Agentes

---

**Documento:** HLD_para_RAG.md  
**Versão:** 1.2  
**Data:** 2024  
**Autor:** Equipe Recoloca.ai  
**Status:** Ativo

## ARQUITETURA DE COMPONENTES

### 1. Frontend PWA (Flutter Web)

#### Estrutura de Camadas
```
├── presentation/
│   ├── pages/          # Telas principais
│   ├── widgets/        # Componentes reutilizáveis
│   └── bloc/           # Gerenciamento de estado
├── domain/
│   ├── entities/       # Modelos de domínio
│   ├── repositories/   # Contratos de dados
│   └── usecases/       # Regras de negócio
├── data/
│   ├── datasources/    # APIs e cache
│   ├── repositories/   # Implementações
│   └── models/         # DTOs
└── core/
    ├── network/        # HTTP client
    ├── storage/        # Cache local
    └── utils/          # Utilitários
```

#### Módulos Principais
- **Auth Module**: Login, registro, OAuth
- **Kanban Module**: Gerenciamento de candidaturas
- **CV Optimization**: Upload e análise de currículos
- **Coach Module**: Chat com IA e notificações
- **Analytics Module**: Métricas e dashboards
- **Settings Module**: Configurações e perfil

### 2. API Backend (FastAPI)

#### Estrutura de Camadas
```
├── app/
│   ├── api/
│   │   ├── v1/         # Endpoints versioned
│   │   └── deps.py     # Dependencies
│   ├── core/
│   │   ├── config.py   # Configurações
│   │   ├── security.py # Auth & Security
│   │   └── database.py # DB connection
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   ├── repositories/   # Data access
│   └── utils/          # Utilitários
├── tests/              # Testes automatizados
└── migrations/         # Alembic migrations
```

#### Endpoints Principais
- **Auth**: `/auth/login`, `/auth/register`, `/auth/oauth`
- **Users**: `/users/profile`, `/users/settings`
- **Applications**: `/applications/` (CRUD + Kanban)
- **Jobs**: `/jobs/import`, `/jobs/analyze`
- **CV**: `/cv/upload`, `/cv/optimize`, `/cv/score`
- **Coach**: `/coach/chat`, `/coach/insights`
- **Analytics**: `/analytics/metrics`, `/analytics/reports`
- **Payments**: `/payments/subscribe`, `/payments/webhook`

### 3. Banco de Dados (Supabase)

#### Schema Principal
```sql
-- Usuários e autenticação
users (
  id UUID PRIMARY KEY,
  email VARCHAR UNIQUE,
  profile JSONB,
  subscription_tier VARCHAR,
  created_at TIMESTAMP
);

-- Candidaturas (Kanban)
applications (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  job_title VARCHAR,
  company VARCHAR,
  status VARCHAR,
  job_url TEXT,
  job_data JSONB,
  notes TEXT,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Currículos
cv_documents (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  filename VARCHAR,
  content_text TEXT,
  metadata JSONB,
  created_at TIMESTAMP
);

-- Análises de adequação
cv_analyses (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  application_id UUID REFERENCES applications(id),
  cv_id UUID REFERENCES cv_documents(id),
  score INTEGER,
  suggestions JSONB,
  optimized_cv TEXT,
  created_at TIMESTAMP
);

-- Interações com Coach IA
coach_interactions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  message TEXT,
  response TEXT,
  context JSONB,
  created_at TIMESTAMP
);

-- Métricas de usuário
user_metrics (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  metric_type VARCHAR,
  value NUMERIC,
  metadata JSONB,
  recorded_at TIMESTAMP
);
```

#### Row Level Security (RLS)
```sql
-- Política base: usuários só acessam seus próprios dados
CREATE POLICY "Users can only access their own data" ON applications
  FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can only access their own CVs" ON cv_documents
  FOR ALL USING (auth.uid() = user_id);

-- Políticas similares para todas as tabelas
```

### 4. Sistema de IA e RAG

#### Arquitetura RAG
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Documents     │───▶│   Embeddings     │───▶│  Vector Store   │
│   (Markdown)    │    │  (OpenAI API)    │    │  (pgvector)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │───▶│   Retrieval      │◀───│   Similarity    │
│                 │    │   (Top-K)        │    │   Search        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
┌─────────────────┐    ┌──────────────────┐
│   LLM Response  │◀───│   Augmented      │
│   (Contextual)  │    │   Generation     │
└─────────────────┘    └──────────────────┘
```

#### Componentes RAG
- **Document Processor**: Converte Markdown para chunks
- **Embedding Service**: Gera vetores via OpenAI API
- **Vector Store**: Supabase pgvector para busca semântica
- **Retrieval Engine**: Top-K similarity search
- **Context Builder**: Monta prompt com contexto relevante
- **LLM Gateway**: OpenRouter para múltiplos modelos

### 5. Integração com Serviços Externos

#### OpenRouter (LLMs)
```python
# Configuração multi-modelo
LLM_CONFIGS = {
    "gpt-4": {
        "model": "openai/gpt-4-turbo",
        "max_tokens": 4000,
        "temperature": 0.7
    },
    "claude-3": {
        "model": "anthropic/claude-3-sonnet",
        "max_tokens": 4000,
        "temperature": 0.7
    }
}
```

#### Stripe (Pagamentos)
```python
# Webhook para eventos de assinatura
@app.post("/payments/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    
    event = stripe.Webhook.construct_event(
        payload, sig_header, STRIPE_WEBHOOK_SECRET
    )
    
    if event['type'] == 'customer.subscription.created':
        await handle_subscription_created(event['data']['object'])
    
    return {"status": "success"}
```

#### Job Boards (Scraping/APIs)
```python
# Extração inteligente de vagas
class JobExtractor:
    async def extract_from_url(self, url: str) -> JobData:
        # 1. Detectar plataforma (LinkedIn, Gupy, etc.)
        platform = self.detect_platform(url)
        
        # 2. Extrair HTML/API data
        raw_data = await self.fetch_job_data(url, platform)
        
        # 3. Processar com LLM
        structured_data = await self.llm_extract(
            raw_data, JobDataSchema
        )
        
        return structured_data
```

## FLUXOS DE DADOS PRINCIPAIS

### 1. Fluxo de Autenticação
```
User → Frontend → Supabase Auth → JWT Token → Backend Validation → Access Granted
```

### 2. Fluxo de Importação de Vaga
```
URL Input → Job Extractor → LLM Processing → Structured Data → Database → Kanban Update
```

### 3. Fluxo de Otimização de CV
```
CV Upload → Text Extraction → Job Analysis → LLM Comparison → Score + Suggestions → Optimized CV
```

### 4. Fluxo do Coach IA
```
User Context → RAG Retrieval → Prompt Building → LLM Generation → Contextual Response
```

## PADRÕES DE SEGURANÇA

### Autenticação e Autorização
- **OAuth 2.0**: Google, LinkedIn (futuro)
- **JWT Tokens**: Stateless authentication
- **RLS**: Database-level security
- **RBAC**: Role-based access (futuro)

### Proteção de Dados
- **Encryption in Transit**: TLS 1.3
- **Encryption at Rest**: Database encryption
- **Data Anonymization**: PII protection
- **LGPD Compliance**: Data retention policies

### Validação e Sanitização
```python
# Pydantic schemas para validação
class ApplicationCreate(BaseModel):
    job_title: str = Field(..., min_length=1, max_length=200)
    company: str = Field(..., min_length=1, max_length=100)
    job_url: Optional[HttpUrl] = None
    notes: Optional[str] = Field(None, max_length=2000)
    
    @validator('job_title')
    def validate_job_title(cls, v):
        return sanitize_html(v.strip())
```

## PADRÕES DE PERFORMANCE

### Otimizações Backend
- **Async/Await**: Non-blocking I/O
- **Connection Pooling**: Database connections
- **Query Optimization**: Indexes + Query analysis
- **Caching**: Redis para dados frequentes
- **Rate Limiting**: Proteção contra abuse

### Otimizações Frontend
- **Lazy Loading**: Componentes sob demanda
- **Code Splitting**: Bundles otimizados
- **Image Optimization**: WebP + responsive
- **Service Worker**: Cache offline
- **Virtual Scrolling**: Listas grandes

### Monitoramento
```python
# Métricas customizadas
from prometheus_client import Counter, Histogram

api_requests = Counter('api_requests_total', 'Total API requests')
api_duration = Histogram('api_request_duration_seconds', 'API request duration')

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    api_requests.inc()
    api_duration.observe(duration)
    
    return response
```

## ESTRATÉGIA DE DEPLOY

### Ambientes
- **Development**: Local + Docker
- **Staging**: Render + Vercel (preview)
- **Production**: Render + Vercel + CDN

### CI/CD Pipeline
```yaml
# GitHub Actions
name: Deploy Backend
on:
  push:
    branches: [main]
    
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest --cov=app tests/
        
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Render
        uses: render-deploy-action@v1
        with:
          service-id: ${{ secrets.RENDER_SERVICE_ID }}
          api-key: ${{ secrets.RENDER_API_KEY }}
```

### Database Migrations
```python
# Alembic migration example
def upgrade():
    op.create_table(
        'applications',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('job_title', sa.String(200), nullable=False),
        sa.Column('company', sa.String(100), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'])
    )
    
    # RLS Policy
    op.execute("""
        ALTER TABLE applications ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Users can only access their own applications" 
        ON applications FOR ALL USING (auth.uid() = user_id);
    """)
```

## CONSIDERAÇÕES DE ESCALABILIDADE

### Horizontal Scaling
- **Stateless Backend**: Múltiplas instâncias
- **Load Balancer**: Distribuição de carga
- **Database Sharding**: Por tenant (futuro)
- **CDN**: Assets estáticos globais

### Vertical Scaling
- **Resource Monitoring**: CPU, Memory, I/O
- **Auto-scaling**: Baseado em métricas
- **Database Optimization**: Query performance
- **Cache Layers**: Multiple levels

### Limites e Quotas
```python
# Rate limiting por usuário
from slowapi import Limiter

limiter = Limiter(key_func=get_user_id)

@app.post("/cv/optimize")
@limiter.limit("5/minute")  # Max 5 otimizações por minuto
async def optimize_cv(request: Request, cv_data: CVOptimizeRequest):
    # Implementação
    pass
```

---

**NOTA IMPORTANTE**: Esta arquitetura foi projetada para suportar o crescimento do Recoloca.ai desde o MVP até escala empresarial, mantendo simplicidade operacional para desenvolvimento solo enquanto garante robustez e escalabilidade futuras.