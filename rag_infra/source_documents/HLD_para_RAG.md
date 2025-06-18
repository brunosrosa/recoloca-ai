---
# RAG Metadata
document_type: "arquitetura_sistema"
project: "Recoloca.AI"
version: "1.1"
last_updated: "2025-06-11"
rag_keywords: ["arquitetura", "high level design", "hld", "sistema", "frontend", "backend", "baas", "llm", "rag", "ci cd", "browser extension", "flutter", "fastapi", "supabase"]
related_documents: [
  "PLANO_MESTRE_RECOLOCA_AI_para_RAG.md",
  "ERS_para_RAG.md",
  "ESTRATEGIA_MOMENTO_AHA_para_RAG.md",
  "CAMINHO_CRITICO_MVP_para_RAG.md"
]
cross_references: [
  "arquitetura sistema", "design alto nivel", "componentes sistema",
  "frontend flutter", "backend fastapi", "banco dados supabase",
  "integracao llm", "sistema rag", "ci cd pipeline", "extensao browser"
]
---

# HIGH-LEVEL DESIGN (HLD) - RECOLOCA.AI

## Informações do Documento
- **Versão**: 1.1 (Orquestração Inteligente e Specialized Intelligence)
- **Data de Criação**: 11 de junho de 2025
- **Data de Última Atualização**: Junho de 2025
- **Autor**: @AgenteArquitetoTI
- **Contexto**: Arquitetura de sistema para MVP e evolução
- **Baseado em**: ERS v1.1, PLANO_MESTRE_RECOLOCA_AI v1.1

## 🎯 PROPÓSITO E ESCOPO

### Propósito
Definir a arquitetura de alto nível do sistema Recoloca.ai, estabelecendo a estrutura técnica, componentes principais, integrações e fluxos de dados para suportar todas as funcionalidades do MVP e evolução futura.

### Escopo Arquitetural

#### **1. Frontend (Flutter Web/Mobile)**
- Interface de usuário responsiva
- Experiência multiplataforma
- Componentes reutilizáveis
- Estado global gerenciado

#### **2. Backend (FastAPI + Python)**
- APIs RESTful robustas
- Processamento de dados
- Integração com serviços externos
- Lógica de negócio centralizada

#### **3. BaaS (Supabase)**
- Banco de dados PostgreSQL
- Autenticação e autorização
- Storage de arquivos
- Real-time subscriptions

#### **4. LLMs (Google Gemini)**
- Análise de CVs
- Geração de conteúdo
- Processamento de linguagem natural
- Insights personalizados

#### **5. RAG (Retrieval-Augmented Generation)**
- Base de conhecimento
- Busca semântica
- Contexto enriquecido
- Respostas precisas

#### **6. CI/CD (GitHub Actions)**
- Deploy automatizado
- Testes contínuos
- Qualidade de código
- Monitoramento

#### **7. Browser Extension (Futuro)**
- Integração com sites de emprego
- Análise em tempo real
- Aplicação automática
- Sincronização de dados

## 🏗️ ARQUITETURA GERAL DO SISTEMA

### Visão de Alto Nível

```
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE APRESENTAÇÃO                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Flutter   │  │   Flutter   │  │  Browser    │        │
│  │     Web     │  │   Mobile    │  │  Extension  │        │
│  │             │  │             │  │  (Futuro)   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE APLICAÇÃO                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                FastAPI Backend                     │   │
│  │                                                     │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │   CV    │ │  User   │ │  Job    │ │  Coach  │   │   │
│  │  │ Service │ │ Service │ │ Service │ │ Service │   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE INTEGRAÇÃO                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Supabase  │  │   Google    │  │     RAG     │        │
│  │    (BaaS)   │  │   Gemini    │  │   System    │        │
│  │             │  │    (LLM)    │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE DADOS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ PostgreSQL  │  │   Storage   │  │   Vector    │        │
│  │  Database   │  │   (Files)   │  │  Database   │        │
│  │             │  │             │  │   (RAG)     │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🎨 CAMADA DE APRESENTAÇÃO

### Flutter Frontend

#### **Arquitetura de Componentes**

```
src/
├── core/
│   ├── constants/
│   ├── utils/
│   ├── services/
│   └── models/
├── features/
│   ├── auth/
│   │   ├── presentation/
│   │   ├── domain/
│   │   └── data/
│   ├── cv_analysis/
│   │   ├── presentation/
│   │   ├── domain/
│   │   └── data/
│   ├── job_matching/
│   │   ├── presentation/
│   │   ├── domain/
│   │   └── data/
│   └── coaching/
│       ├── presentation/
│       ├── domain/
│       └── data/
├── shared/
│   ├── widgets/
│   ├── themes/
│   └── extensions/
└── main.dart
```

#### **Gerenciamento de Estado**

```dart
// Provider + Riverpod para estado global
class AppState {
  final UserState userState;
  final CVState cvState;
  final JobState jobState;
  final CoachState coachState;
}

// Estados específicos por feature
class CVState {
  final List<CVDocument> cvs;
  final CVAnalysisResult? currentAnalysis;
  final bool isAnalyzing;
  final String? error;
}
```

#### **Componentes Principais**

1. **AuthenticationScreen**
   - Login/Registro
   - Integração com Supabase Auth
   - Validação de formulários

2. **DashboardScreen**
   - Visão geral do usuário
   - Métricas e progresso
   - Navegação principal

3. **CVAnalysisScreen**
   - Upload de CV
   - Análise em tempo real
   - Resultados e insights

4. **JobMatchingScreen**
   - Lista de vagas
   - Filtros e busca
   - Score de compatibilidade

5. **CoachingScreen**
   - Chat com IA
   - Planos de carreira
   - Recursos educacionais

### Responsividade e UX

#### **Breakpoints**
```dart
class Breakpoints {
  static const double mobile = 600;
  static const double tablet = 900;
  static const double desktop = 1200;
}
```

#### **Design System**
```dart
class AppTheme {
  static ThemeData lightTheme = ThemeData(
    primarySwatch: Colors.blue,
    fontFamily: 'Inter',
    // Definições de cores, tipografia, etc.
  );
}
```

## ⚙️ CAMADA DE APLICAÇÃO

### FastAPI Backend

#### **Estrutura de Projeto**

```
backend/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py
│   │   │   │   ├── cv.py
│   │   │   │   ├── jobs.py
│   │   │   │   └── coaching.py
│   │   │   └── api.py
│   │   └── deps.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── cv.py
│   │   ├── job.py
│   │   └── coaching.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── cv.py
│   │   ├── job.py
│   │   └── coaching.py
│   ├── services/
│   │   ├── cv_service.py
│   │   ├── job_service.py
│   │   ├── coaching_service.py
│   │   └── llm_service.py
│   └── main.py
├── tests/
├── requirements.txt
└── Dockerfile
```

#### **Arquitetura de Serviços**

```python
# Exemplo: CV Service
class CVService:
    def __init__(self, db: Session, llm_service: LLMService):
        self.db = db
        self.llm_service = llm_service
    
    async def analyze_cv(self, cv_content: str, user_id: int) -> CVAnalysisResult:
        # 1. Processar CV
        parsed_cv = await self.parse_cv(cv_content)
        
        # 2. Análise com LLM
        analysis = await self.llm_service.analyze_cv(parsed_cv)
        
        # 3. Salvar resultados
        result = await self.save_analysis(analysis, user_id)
        
        return result
```

#### **Endpoints Principais**

```python
# CV Endpoints
@router.post("/cv/upload")
async def upload_cv(file: UploadFile, current_user: User = Depends(get_current_user)):
    pass

@router.post("/cv/analyze")
async def analyze_cv(cv_id: int, current_user: User = Depends(get_current_user)):
    pass

@router.get("/cv/{cv_id}/analysis")
async def get_cv_analysis(cv_id: int, current_user: User = Depends(get_current_user)):
    pass

# Job Endpoints
@router.get("/jobs/search")
async def search_jobs(query: str, filters: JobFilters, current_user: User = Depends(get_current_user)):
    pass

@router.post("/jobs/{job_id}/match")
async def match_job(job_id: int, cv_id: int, current_user: User = Depends(get_current_user)):
    pass

# Coaching Endpoints
@router.post("/coaching/chat")
async def chat_with_coach(message: str, current_user: User = Depends(get_current_user)):
    pass
```

#### **Middleware e Segurança**

```python
# Middleware de autenticação
class AuthMiddleware:
    async def __call__(self, request: Request, call_next):
        # Validar JWT token
        # Verificar permissões
        # Adicionar user context
        pass

# Rate limiting
class RateLimitMiddleware:
    async def __call__(self, request: Request, call_next):
        # Implementar rate limiting por usuário
        # Prevenir abuso de API
        pass
```

## 🗄️ CAMADA DE DADOS

### Supabase (BaaS)

#### **Schema do Banco de Dados**

```sql
-- Usuários
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR UNIQUE NOT NULL,
    full_name VARCHAR,
    avatar_url VARCHAR,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- CVs
CREATE TABLE cvs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    title VARCHAR NOT NULL,
    content TEXT,
    file_url VARCHAR,
    status VARCHAR DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Análises de CV
CREATE TABLE cv_analyses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cv_id UUID REFERENCES cvs(id),
    score INTEGER,
    strengths JSONB,
    improvements JSONB,
    keywords JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Vagas
CREATE TABLE jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR NOT NULL,
    company VARCHAR NOT NULL,
    description TEXT,
    requirements JSONB,
    location VARCHAR,
    salary_range VARCHAR,
    external_url VARCHAR,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Matches CV-Vaga
CREATE TABLE job_matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cv_id UUID REFERENCES cvs(id),
    job_id UUID REFERENCES jobs(id),
    match_score INTEGER,
    analysis JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Sessões de Coaching
CREATE TABLE coaching_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    messages JSONB,
    session_type VARCHAR,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### **Row Level Security (RLS)**

```sql
-- Política para CVs
CREATE POLICY "Users can only access their own CVs" ON cvs
    FOR ALL USING (auth.uid() = user_id);

-- Política para análises
CREATE POLICY "Users can only access their own analyses" ON cv_analyses
    FOR ALL USING (auth.uid() = (SELECT user_id FROM cvs WHERE cvs.id = cv_analyses.cv_id));
```

#### **Storage Configuration**

```sql
-- Bucket para CVs
INSERT INTO storage.buckets (id, name, public) VALUES ('cvs', 'cvs', false);

-- Política de storage
CREATE POLICY "Users can upload their own CVs" ON storage.objects
    FOR INSERT WITH CHECK (bucket_id = 'cvs' AND auth.uid()::text = (storage.foldername(name))[1]);
```

### Vector Database (RAG)

#### **Configuração do pgvector**

```sql
-- Extensão para vetores
CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela para embeddings
CREATE TABLE document_embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_type VARCHAR NOT NULL,
    content TEXT NOT NULL,
    embedding vector(1536),
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Índice para busca de similaridade
CREATE INDEX ON document_embeddings USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

## 🤖 INTEGRAÇÃO COM IA

### Google Gemini Integration

#### **LLM Service**

```python
class LLMService:
    def __init__(self, api_key: str):
        self.client = genai.GenerativeModel('gemini-pro')
        self.api_key = api_key
    
    async def analyze_cv(self, cv_content: str, job_description: str = None) -> dict:
        prompt = self._build_analysis_prompt(cv_content, job_description)
        response = await self.client.generate_content(prompt)
        return self._parse_analysis_response(response.text)
    
    async def optimize_cv(self, cv_content: str, analysis: dict) -> str:
        prompt = self._build_optimization_prompt(cv_content, analysis)
        response = await self.client.generate_content(prompt)
        return response.text
    
    async def coach_conversation(self, message: str, context: dict) -> str:
        prompt = self._build_coaching_prompt(message, context)
        response = await self.client.generate_content(prompt)
        return response.text
```

#### **Prompt Templates**

```python
class PromptTemplates:
    CV_ANALYSIS = """
    Analise o seguinte CV e forneça:
    1. Score de adequação (0-100)
    2. Pontos fortes (máximo 5)
    3. Áreas de melhoria (máximo 5)
    4. Sugestões específicas
    
    CV: {cv_content}
    Vaga (opcional): {job_description}
    
    Responda em JSON estruturado.
    """
    
    CV_OPTIMIZATION = """
    Otimize o CV aplicando as melhorias sugeridas:
    
    CV Original: {cv_content}
    Análise: {analysis}
    
    Mantenha a veracidade e melhore a apresentação.
    """
```

### RAG System

#### **RAG Service**

```python
class RAGService:
    def __init__(self, vector_db: VectorDB, llm_service: LLMService):
        self.vector_db = vector_db
        self.llm_service = llm_service
    
    async def query(self, question: str, context_type: str = None) -> str:
        # 1. Buscar documentos relevantes
        relevant_docs = await self.vector_db.similarity_search(
            question, 
            filter={"type": context_type} if context_type else None
        )
        
        # 2. Construir contexto
        context = self._build_context(relevant_docs)
        
        # 3. Gerar resposta com LLM
        response = await self.llm_service.generate_with_context(
            question, context
        )
        
        return response
```

## 🔄 FLUXOS DE DADOS PRINCIPAIS

### Fluxo de Análise de CV

```
1. Usuário faz upload do CV (Frontend)
   ↓
2. Arquivo enviado para Supabase Storage (Backend)
   ↓
3. Conteúdo extraído e processado (Backend)
   ↓
4. Análise enviada para Google Gemini (LLM Service)
   ↓
5. Resultados processados e salvos (Database)
   ↓
6. Resposta enviada para Frontend (API)
   ↓
7. Resultados exibidos ao usuário (UI)
```

### Fluxo de Matching de Vagas

```
1. Usuário busca vagas (Frontend)
   ↓
2. Filtros aplicados na busca (Backend)
   ↓
3. CVs do usuário recuperados (Database)
   ↓
4. Análise de compatibilidade (LLM Service)
   ↓
5. Scores calculados e ordenados (Backend)
   ↓
6. Resultados retornados (API)
   ↓
7. Lista de vagas exibida (UI)
```

### Fluxo de Coaching

```
1. Usuário envia mensagem (Frontend)
   ↓
2. Contexto do usuário recuperado (Database)
   ↓
3. Busca por informações relevantes (RAG)
   ↓
4. Resposta gerada com contexto (LLM Service)
   ↓
5. Conversa salva no histórico (Database)
   ↓
6. Resposta enviada ao usuário (API)
   ↓
7. Chat atualizado (UI)
```

## 🚀 CI/CD E DEPLOYMENT

### GitHub Actions Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy Recoloca.AI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Run linting
        run: flake8
  
  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to production
        run: |
          # Deploy backend to cloud provider
  
  deploy-frontend:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Build Flutter web
        run: flutter build web
      - name: Deploy to hosting
        run: |
          # Deploy frontend to hosting provider
```

### Ambientes

#### **Desenvolvimento**
- Backend: Local (FastAPI dev server)
- Frontend: Local (Flutter dev server)
- Database: Supabase development project
- LLM: Google Gemini (development quota)

#### **Staging**
- Backend: Cloud hosting (staging environment)
- Frontend: Staging URL
- Database: Supabase staging project
- LLM: Google Gemini (production quota)

#### **Produção**
- Backend: Cloud hosting (production environment)
- Frontend: Production domain
- Database: Supabase production project
- LLM: Google Gemini (production quota)
- CDN: Para assets estáticos
- Monitoring: Logs e métricas

## 📊 MONITORAMENTO E OBSERVABILIDADE

### Logging

```python
# Configuração de logging estruturado
import structlog

logger = structlog.get_logger()

# Exemplo de uso
logger.info(
    "CV analysis completed",
    user_id=user.id,
    cv_id=cv.id,
    score=analysis.score,
    duration_ms=duration
)
```

### Métricas

```python
# Métricas de negócio
class Metrics:
    CV_UPLOADS = "cv_uploads_total"
    CV_ANALYSES = "cv_analyses_total"
    JOB_MATCHES = "job_matches_total"
    COACHING_SESSIONS = "coaching_sessions_total"
    
    # Métricas técnicas
    API_REQUESTS = "api_requests_total"
    API_DURATION = "api_request_duration_seconds"
    LLM_REQUESTS = "llm_requests_total"
    LLM_DURATION = "llm_request_duration_seconds"
```

### Health Checks

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "version": app.version,
        "dependencies": {
            "database": await check_database(),
            "llm_service": await check_llm_service(),
            "storage": await check_storage()
        }
    }
```

## 🔒 SEGURANÇA

### Autenticação e Autorização

```python
# JWT Token validation
class SecurityService:
    def verify_token(self, token: str) -> User:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("sub")
            if user_id is None:
                raise HTTPException(status_code=401)
            return self.get_user(user_id)
        except JWTError:
            raise HTTPException(status_code=401)
```

### Validação de Dados

```python
# Pydantic schemas para validação
class CVUploadRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: Optional[str] = None
    
    @validator('title')
    def validate_title(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()
```

### Rate Limiting

```python
# Rate limiting por usuário
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/cv/analyze")
@limiter.limit("5/minute")
async def analyze_cv(request: Request, ...):
    pass
```

## 📈 ESCALABILIDADE

### Estratégias de Escala

#### **Horizontal Scaling**
- Load balancer para múltiplas instâncias do backend
- Auto-scaling baseado em métricas
- Database read replicas

#### **Caching**
```python
# Redis para cache de resultados
class CacheService:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    async def get_cv_analysis(self, cv_id: str) -> Optional[dict]:
        cached = await self.redis.get(f"cv_analysis:{cv_id}")
        return json.loads(cached) if cached else None
    
    async def set_cv_analysis(self, cv_id: str, analysis: dict, ttl: int = 3600):
        await self.redis.setex(
            f"cv_analysis:{cv_id}", 
            ttl, 
            json.dumps(analysis)
        )
```

#### **Database Optimization**
- Índices otimizados para queries frequentes
- Particionamento de tabelas grandes
- Connection pooling
- Query optimization

#### **CDN e Assets**
- CDN para arquivos estáticos
- Compressão de imagens
- Lazy loading de componentes

## 🔮 EVOLUÇÃO FUTURA

### Versão 2.0 - Expansão
- **Microserviços**: Quebra do monolito em serviços especializados
- **Event-Driven Architecture**: Comunicação assíncrona entre serviços
- **Multi-tenant**: Suporte para empresas
- **Mobile Apps**: Apps nativos iOS/Android

### Versão 3.0 - Inteligência Avançada
- **ML Pipeline**: Modelos próprios de machine learning
- **Real-time Analytics**: Dashboards em tempo real
- **Advanced RAG**: Sistema RAG mais sofisticado
- **Integration Hub**: Integrações com múltiplas plataformas

## 📚 Referências e Documentos Relacionados

### Documentos Base
- **ERS_para_RAG.md**: Requisitos funcionais e não-funcionais
- **PLANO_MESTRE_RECOLOCA_AI_para_RAG.md**: Visão geral do produto
- **ESTRATEGIA_MOMENTO_AHA_para_RAG.md**: Estratégia de experiência do usuário
- **CAMINHO_CRITICO_MVP_para_RAG.md**: Cronograma de desenvolvimento

### Documentos Técnicos
- **ADRs**: Decisões arquiteturais específicas
- **API_SPECS**: Especificações detalhadas das APIs
- **LLDs**: Designs de baixo nível por componente
- **STYLE_GUIDE**: Diretrizes de código e design

### Documentos de Processo
- **KANBAN_ESTRATEGICO_FASES_para_RAG.md**: Gestão de desenvolvimento
- **MAESTRO_TASKS_para_RAG.md**: Tarefas e responsabilidades
- **ROADMAP_TEMPORAL_RECOLOCA_AI_para_RAG.md**: Cronograma estratégico

---

**Documento**: HLD_para_RAG.md (v1.1)
**Otimizado para**: Sistema RAG - Consulta de arquitetura e design de sistema
**Palavras-chave RAG**: arquitetura, high level design, hld, sistema, frontend, backend, baas, llm, rag, ci cd, browser extension, flutter, fastapi, supabase, componentes sistema, integracao

--- FIM DO DOCUMENTO HLD_para_RAG.md (v1.1) ---