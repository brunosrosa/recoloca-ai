# PLANO MESTRE DO PROJETO RECOLOCA.AI - VERSÃO RAG

**Documento Fonte**: `docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md`
**Versão RAG**: 1.0
**Data de Conversão**: Janeiro 2025
**Prioridade RAG**: CRÍTICA
**Categoria**: Documentação Central
**Tags**: #plano-mestre #visao-estrategica #mvp #recoloca-ai #desenvolvimento-solo #agentes-ia

---

## CONTEXTO ESTRATÉGICO FUNDAMENTAL

### Visão do Produto
O **Recoloca.ai** é um Micro-SaaS inovador que transforma a experiência de recolocação profissional no Brasil, atuando como o **"cockpit do candidato"** para profissionais de TI Pleno/Sênior.

### Problema de Mercado
- Gerenciamento ineficiente de múltiplas candidaturas
- Dificuldade em adaptar currículos para cada vaga
- Falta de preparo para entrevistas
- Sensação de isolamento durante o processo

### Solução Proposta
Plataforma integrada que combina:
- **Landing page atrativa** para aquisição de usuários
- **Gerenciamento inteligente de candidaturas** (Kanban)
- **Otimização de currículos com IA** (Momento AHA! Principal)
- **Assistente de IA para coaching** contextualizado

## METODOLOGIA DE DESENVOLVIMENTO

### Paradigma: "Desenvolvimento Solo Ágil Aumentado por IA"
- **Maestro** (Bruno S. Rosa) como desenvolvedor principal
- **Squad de Agentes IA Mentores** especializados
- **Orquestração Inteligente** com Human-in-the-Loop evolutivo
- **Documentação Viva** integrada ao sistema RAG

### Agentes IA Tier 1 (Essenciais)
1. **@AgenteM_Orquestrador** - PM Mentor + Validação Estratégica
2. **@AgenteM_ArquitetoTI** - Arquitetura e Infraestrutura
3. **@AgenteM_UXDesigner** - Design e Experiência
4. **@AgenteM_DevFastAPI** - Backend Python
5. **@AgenteM_DevFlutter** - Frontend PWA

## ARQUITETURA TÉCNICA CORE

### Stack Tecnológica Principal
- **Frontend**: Flutter Web (PWA)
- **Backend**: FastAPI + Python
- **Banco de Dados**: Supabase (PostgreSQL + RLS)
- **IA/LLM**: OpenRouter + Multiple Providers
- **Deploy**: Vercel (Frontend) + Render (Backend)
- **Pagamentos**: Stripe
- **Autenticação**: Supabase Auth + Google OAuth

### Componentes Arquiteturais
- **Sistema RAG** para contextualização de agentes
- **MCP Server** para integração TRAE IDE
- **Row Level Security (RLS)** para segurança multi-tenant
- **API RESTful** com documentação OpenAPI
- **Sistema de Notificações** em tempo real

## FUNCIONALIDADES MVP CORE

### 1. Gerenciamento de Candidaturas (Kanban)
- Pipeline visual estruturado
- Acompanhamento de status
- Métricas de progresso

### 2. Importação Inteligente de Vagas
- Processamento via LLM
- Extração automática de dados
- Categorização inteligente

### 3. Otimização de Currículo com IA (MOMENTO AHA!)
- Análise de adequação CV vs. vaga
- Score de compatibilidade
- Sugestões contextualizadas
- Otimização automática

### 4. Estimativa de Range Salarial
- Análise baseada em dados de mercado
- Contextualização por região/senioridade
- Benchmarking automático

### 5. Coach IA Proativo
- Monitoramento de progresso
- Orientações personalizadas
- Suporte contextual
- Insights estratégicos

### 6. Módulo de Métricas Pessoais
- Dashboard de acompanhamento
- KPIs de candidatura
- Análise de funil
- Relatórios de performance

## ESTRATÉGIA DE PRODUTO

### Diferencial Competitivo
**Coach IA proativo e contextual** que atua como "integrador e cockpit" do processo de recolocação.

### Modelo de Negócio
- **Freemium** com tiers diferenciados
- **Stripe** para gestão de pagamentos
- **Funcionalidades premium** para monetização

### Público-Alvo
- **Profissionais de TI Pleno/Sênior** no Brasil
- **Foco inicial**: Desenvolvedores, Arquitetos, Tech Leads
- **Expansão futura**: Outras áreas de tecnologia

## ROADMAP TEMPORAL

### Fase 0: Foundation RAG + Agents (Semanas 1-3)
- Operacionalização completa do RAG
- Configuração dos 5 Agentes Tier 1
- Setup do MCP Server
- Ambiente de desenvolvimento

### Fase 1: Validação Técnica e Estratégica (Semanas 4-5)
- HLD detalhado v1.2
- Protótipo RLS FastAPI/Supabase
- Validação de viabilidade técnica
- Refinamento de requisitos

### Fase 2: MVP Kanban + AHA! Moment (Semanas 6-11)
- Desenvolvimento do core MVP
- Implementação do Momento AHA!
- Integração com LLMs
- Testes de funcionalidade

### Fase 3: Testing + Launch Prep (Semanas 12-16)
- Beta limitado
- Testes de usuário
- Refinamentos finais
- Preparação para lançamento

## MÉTRICAS DE SUCESSO

### Técnicas
- **Cobertura de testes**: >80%
- **Performance API**: <200ms
- **Uptime**: >99.5%
- **Segurança**: Zero vulnerabilidades críticas

### Produto
- **Taxa de conversão**: >5% (freemium para premium)
- **Retenção 30 dias**: >40%
- **NPS**: >50
- **Tempo para primeiro valor**: <5 minutos

### Agentes IA
- **Precisão**: ≥90% em tarefas especializadas
- **Tempo de resposta**: ≤30 segundos
- **Contextualização RAG**: ≥85% relevância

## GESTÃO DE CONHECIMENTO

### Documentação Viva
- **Obsidian** como ferramenta central
- **Git** para versionamento
- **RAG** para contextualização automática
- **Markdown** como formato padrão

### Sistema RAG
- **Embedding model** para vetorização
- **Vector store** para busca semântica
- **Retrieval** contextual para agentes
- **Feedback loop** para melhoria contínua

## PRINCÍPIOS DE DESENVOLVIMENTO

### Qualidade de Código
- **Clean Architecture** e Repository Pattern
- **Validação rigorosa** com Pydantic
- **Async/await** para operações I/O
- **Princípios SOLID** e DRY
- **Documentação automática** de APIs

### Segurança
- **Row Level Security (RLS)** no Supabase
- **Autenticação robusta** com OAuth
- **Validação de entrada** em todas as camadas
- **Logs estruturados** para auditoria

### Performance
- **Otimização de queries** no banco
- **Cache estratégico** para dados frequentes
- **Lazy loading** no frontend
- **Monitoramento** de métricas em tempo real

## INTEGRAÇÃO E COLABORAÇÃO

### Workflow de Agentes
- **@AgenteM_Orquestrador** coordena estratégia
- **@AgenteM_ArquitetoTI** define arquitetura
- **@AgenteM_DevFastAPI** implementa backend
- **@AgenteM_DevFlutter** desenvolve frontend
- **@AgenteM_UXDesigner** otimiza experiência

### Ferramentas de Integração
- **TRAE IDE** como ambiente principal
- **MCP Server** para comunicação
- **RAG** para contexto compartilhado
- **Git** para versionamento colaborativo

## RISCOS E MITIGAÇÕES

### Técnicos
- **Complexidade RLS**: Prototipagem antecipada
- **Performance LLM**: Cache e otimização
- **Integração múltipla**: Testes automatizados

### Produto
- **Adoção lenta**: Estratégia de marketing focada
- **Concorrência**: Diferenciação por IA
- **Monetização**: Modelo freemium validado

### Operacionais
- **Desenvolvimento solo**: Agentes IA como multiplicadores
- **Conhecimento concentrado**: Documentação viva
- **Escalabilidade**: Arquitetura cloud-native

---

**NOTA IMPORTANTE**: Este documento é a **fonte da verdade** para o projeto Recoloca.ai. Todas as decisões estratégicas, técnicas e de produto devem estar alinhadas com as diretrizes aqui estabelecidas. Para detalhamentos específicos, consulte os documentos especializados referenciados.