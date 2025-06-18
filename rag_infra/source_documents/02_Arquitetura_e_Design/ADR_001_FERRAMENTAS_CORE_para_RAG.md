---
rag_metadata:
  document_type: "adr"
  project: "Recoloca.ai"
  version: "1.0"
  last_updated: "2024-12-19"
  importance: "critical"
  category: "decisoes_arquiteturais"
  tags: ["adr", "arquitetura", "ferramentas", "stack", "tecnologia"]
  related_docs:
    - "HLD_para_RAG.md"
    - "ERS_para_RAG.md"
    - "METODOLOGIA_MVP_para_RAG.md"
  cross_references:
    - "[[docs/03_Arquitetura_e_Design/01_HLD.md]]"
    - "[[docs/02_Requisitos/01_ERS.md]]"
    - "[[docs/01_Guias_Centrais/03_METODOLOGIA_MVP.md]]"
---

# ADR-001: Ferramentas Core do Projeto Recoloca.ai

## Status
**ACEITO** - Implementação em andamento

## Contexto

O projeto Recoloca.ai é um micro-SaaS PWA focado em recolocação profissional para profissionais de TI. Precisamos definir as ferramentas e tecnologias core que formarão a base tecnológica do produto, considerando:

### Requisitos Principais
- **Velocidade de Desenvolvimento:** MVP deve ser entregue rapidamente
- **Escalabilidade:** Solução deve suportar crescimento futuro
- **Experiência do Usuário:** Interface moderna e responsiva
- **Custo-Benefício:** Ferramentas que otimizem recursos financeiros
- **Manutenibilidade:** Stack que facilite manutenção e evolução

### Contexto do Produto
- **Target:** Profissionais de TI em busca de recolocação
- **Funcionalidades Core:** Upload de CV, análise por IA, matching com vagas
- **Modelo de Negócio:** Freemium com funcionalidades premium
- **Arquitetura:** PWA com backend API

### Restrições
- **Orçamento:** Limitado para ferramentas pagas
- **Equipe:** Desenvolvimento solo com suporte de agentes IA
- **Tempo:** Pressão para entrega rápida do MVP
- **Experiência:** Aproveitar conhecimento existente da equipe

## Decisão

### Frontend: Flutter (Web)

**Tecnologia Escolhida:** Flutter para desenvolvimento web (PWA)

**Justificativa:**
- **Performance:** Compilação para JavaScript otimizado
- **Experiência Nativa:** Interface fluida similar a apps nativos
- **PWA Support:** Suporte nativo para Progressive Web Apps
- **Desenvolvimento Único:** Uma base de código para web e futuras expansões mobile
- **Ecossistema:** Rico em packages e widgets
- **Produtividade:** Hot reload e ferramentas de desenvolvimento avançadas

**Configuração:**
- **Framework:** Flutter 3.x
- **Target:** Web (com preparação para mobile futuro)
- **PWA:** Service workers, manifest, offline capabilities
- **State Management:** Provider ou Riverpod
- **HTTP Client:** Dio para comunicação com API

### Backend: Python com FastAPI

**Tecnologia Escolhida:** Python 3.11+ com FastAPI

**Justificativa:**
- **Velocidade de Desenvolvimento:** Sintaxe clara e produtiva
- **Performance:** FastAPI oferece performance comparável a Node.js
- **Documentação Automática:** OpenAPI/Swagger gerado automaticamente
- **Type Safety:** Suporte nativo a type hints
- **Ecossistema IA:** Excelente integração com bibliotecas de ML/IA
- **Async Support:** Suporte nativo a programação assíncrona
- **Validação:** Pydantic para validação robusta de dados

**Stack Complementar:**
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Validation:** Pydantic v2
- **Testing:** Pytest
- **Linting:** Black, Flake8, MyPy

### Backend-as-a-Service: Supabase

**Tecnologia Escolhida:** Supabase com PostgreSQL

**Justificativa:**
- **Velocidade de Setup:** Banco e autenticação prontos rapidamente
- **PostgreSQL:** Banco robusto e escalável
- **Autenticação:** Sistema completo de auth incluído
- **Real-time:** Subscriptions em tempo real
- **Storage:** Armazenamento de arquivos integrado
- **Row Level Security:** Segurança granular nativa
- **APIs Auto-geradas:** REST e GraphQL automáticas
- **Custo:** Tier gratuito generoso para MVP

**Recursos Utilizados:**
- **Database:** PostgreSQL com RLS
- **Auth:** JWT-based authentication
- **Storage:** Para upload de CVs e documentos
- **Edge Functions:** Para processamento serverless quando necessário
- **Real-time:** Para notificações e updates

## Alternativas Consideradas

### Frontend

#### React/Next.js
**Prós:**
- Ecossistema maduro e extenso
- Grande comunidade e recursos
- SSR/SSG nativo no Next.js
- Flexibilidade de customização

**Contras:**
- Maior complexidade de setup
- Necessidade de múltiplas bibliotecas
- Performance inferior para PWAs complexas
- Curva de aprendizado para state management

**Por que não escolhemos:** Flutter oferece melhor performance para PWAs e experiência mais próxima de apps nativos.

#### Vue.js/Nuxt.js
**Prós:**
- Sintaxe mais simples que React
- Boa performance
- Ecossistema crescente
- SSR/SSG no Nuxt.js

**Contras:**
- Ecossistema menor que React
- Menos recursos para PWAs avançadas
- Menor adoção no mercado

**Por que não escolhemos:** Flutter oferece vantagens superiores para PWAs e futuras expansões mobile.

### Backend

#### Node.js/Express
**Prós:**
- JavaScript unificado (frontend/backend)
- Performance excelente
- Ecossistema NPM extenso
- Desenvolvimento rápido

**Contras:**
- Menos adequado para processamento de IA
- Type safety opcional
- Callback hell (mesmo com async/await)
- Menos estruturado que FastAPI

**Por que não escolhemos:** Python oferece melhor integração com IA e FastAPI fornece estrutura mais robusta.

#### Django/Django REST Framework
**Prós:**
- Framework maduro e completo
- Admin interface automática
- ORM robusto
- Segurança built-in

**Contras:**
- Mais pesado para APIs simples
- Menos performance que FastAPI
- Configuração mais complexa
- Overhead desnecessário para MVP

**Por que não escolhemos:** FastAPI oferece melhor performance e simplicidade para APIs modernas.

### Backend-as-a-Service

#### Firebase
**Prós:**
- Integração excelente com Google Cloud
- Real-time database nativo
- Hosting integrado
- Autenticação robusta

**Contras:**
- Vendor lock-in forte
- NoSQL pode ser limitante
- Custos podem escalar rapidamente
- Menos flexibilidade para queries complexas

**Por que não escolhemos:** PostgreSQL oferece mais flexibilidade e Supabase tem melhor custo-benefício.

#### AWS Amplify
**Prós:**
- Integração completa com AWS
- Escalabilidade automática
- Ferramentas de desenvolvimento avançadas
- Flexibilidade de configuração

**Contras:**
- Complexidade de configuração
- Curva de aprendizado íngreme
- Custos podem ser imprevisíveis
- Overhead para projetos simples

**Por que não escolhemos:** Supabase oferece simplicidade superior para MVP com funcionalidades equivalentes.

## Consequências

### Positivas

#### Velocidade de Desenvolvimento
- **Flutter:** Hot reload acelera desenvolvimento frontend
- **FastAPI:** Documentação automática reduz tempo de integração
- **Supabase:** Setup de banco e auth em minutos

#### Performance
- **Flutter Web:** Compilação otimizada para JavaScript
- **FastAPI:** Performance comparável a frameworks mais rápidos
- **PostgreSQL:** Queries otimizadas e indexação avançada

#### Escalabilidade
- **Flutter:** Preparado para expansão mobile
- **FastAPI:** Suporte nativo a async para alta concorrência
- **Supabase:** Escalabilidade automática de infraestrutura

#### Custo-Benefício
- **Flutter:** Desenvolvimento único para múltiplas plataformas
- **Python:** Ecossistema gratuito e open-source
- **Supabase:** Tier gratuito generoso, custos previsíveis

#### Manutenibilidade
- **Type Safety:** Flutter (Dart) e FastAPI (Python) com tipagem forte
- **Documentação:** OpenAPI automática, código autodocumentado
- **Testing:** Ferramentas robustas em todas as camadas

### Negativas

#### Curva de Aprendizado
- **Flutter:** Dart pode ser nova linguagem para alguns desenvolvedores
- **FastAPI:** Conceitos async podem ser desafiadores
- **Supabase:** Menos maduro que alternativas estabelecidas

#### Limitações
- **Flutter Web:** Ainda em evolução, alguns recursos limitados
- **Supabase:** Vendor lock-in moderado
- **Python:** Performance inferior a linguagens compiladas

#### Riscos
- **Flutter Web:** Mudanças na plataforma podem afetar compatibilidade
- **Supabase:** Dependência de serviço terceirizado
- **Ecossistema:** Algumas bibliotecas podem ser menos maduras

## Implementação

### Fase 1: Setup Inicial

#### Frontend (Flutter)
```bash
# Criar projeto Flutter
flutter create recoloca_ai_frontend --platforms web
cd recoloca_ai_frontend

# Configurar PWA
flutter build web --pwa

# Dependências principais
# pubspec.yaml
dependencies:
  flutter:
    sdk: flutter
  dio: ^5.0.0          # HTTP client
  provider: ^6.0.0     # State management
  go_router: ^12.0.0   # Routing
  shared_preferences: ^2.0.0  # Local storage
```

#### Backend (FastAPI)
```bash
# Setup do ambiente
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install fastapi[all] uvicorn[standard] sqlalchemy alembic psycopg2-binary pydantic[email]

# Estrutura do projeto
mkdir -p app/{api,core,models,schemas,services}
touch app/{__init__.py,main.py}
```

#### Supabase
```sql
-- Configuração inicial do banco
-- Executar no SQL Editor do Supabase

-- Habilitar RLS
ALTER TABLE auth.users ENABLE ROW LEVEL SECURITY;

-- Criar tabelas principais
CREATE TABLE profiles (
  id UUID REFERENCES auth.users ON DELETE CASCADE,
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  avatar_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  PRIMARY KEY (id)
);

-- Políticas RLS
CREATE POLICY "Users can view own profile" ON profiles
  FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON profiles
  FOR UPDATE USING (auth.uid() = id);
```

### Fase 2: Integração

#### Configuração de Ambiente
```python
# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_anon_key: str
    supabase_service_key: str
    database_url: str
    secret_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

#### Cliente Supabase
```python
# app/core/supabase.py
from supabase import create_client, Client
from .config import settings

supabase: Client = create_client(
    settings.supabase_url,
    settings.supabase_anon_key
)
```

### Fase 3: Desenvolvimento

#### Estrutura de Pastas
```
recoloca-ai/
├── frontend/                 # Flutter Web
│   ├── lib/
│   │   ├── main.dart
│   │   ├── models/
│   │   ├── services/
│   │   ├── screens/
│   │   └── widgets/
│   └── web/
├── backend/                  # FastAPI
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── alembic/
│   └── tests/
└── docs/                     # Documentação
```

## Monitoramento e Métricas

### KPIs Técnicos
- **Performance Frontend:** Lighthouse score >90
- **Performance Backend:** Response time <200ms
- **Uptime:** >99.9% disponibilidade
- **Cobertura de Testes:** >80%

### Ferramentas de Monitoramento
- **Frontend:** Lighthouse, Web Vitals
- **Backend:** FastAPI metrics, Sentry
- **Database:** Supabase dashboard
- **Logs:** Structured logging com Python logging

## Revisão e Evolução

### Critérios de Revisão
Esta decisão será revisada quando:
- Performance não atender requisitos (>500ms response time)
- Custos excederem orçamento planejado
- Limitações técnicas impedirem funcionalidades críticas
- Surgimento de alternativas significativamente superiores

### Próximas Decisões
- **ADR-002:** Estratégia de autenticação e autorização
- **ADR-003:** Integração com serviços de IA
- **ADR-004:** Estratégia de deploy e CI/CD
- **ADR-005:** Monitoramento e observabilidade

## Referências

### Documentação Oficial
- [Flutter Web](https://docs.flutter.dev/platform-integration/web)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Supabase](https://supabase.com/docs)
- [PostgreSQL](https://www.postgresql.org/docs/)

### Benchmarks e Comparações
- [FastAPI Performance](https://fastapi.tiangolo.com/benchmarks/)
- [Flutter Web Performance](https://flutter.dev/web)
- [Supabase vs Firebase](https://supabase.com/alternatives/supabase-vs-firebase)

### Recursos da Comunidade
- [Flutter Community](https://flutter.dev/community)
- [FastAPI Community](https://github.com/tiangolo/fastapi)
- [Supabase Community](https://github.com/supabase/supabase)

---

## Histórico de Versões

| Versão | Data | Autor | Mudanças |
|--------|------|-------|----------|
| 1.0 | 2024-12-19 | Bruno S. Rosa | Versão inicial |

---

## Aprovação

**Decisão Tomada Por:** Bruno S. Rosa (Maestro)  
**Data da Decisão:** 2024-12-19  
**Status:** Aceito e em implementação  
**Próxima Revisão:** 2025-03-19 (ou quando critérios de revisão forem atingidos)

---

**Nota:** Este ADR é parte da documentação viva do projeto Recoloca.ai e deve ser consultado via sistema RAG para obter informações atualizadas sobre as decisões arquiteturais do projeto.