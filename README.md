# 🧑🏻‍💼 Recoloca.AI

> **Micro-SaaS para Recolocação Profissional no Brasil**  
> *Desenvolvido com Metodologia "Solo Ágil Aumentado por IA"*

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)](https://github.com/)
[![Versão](https://img.shields.io/badge/Versão-MVP%20v0.1-blue)](https://github.com/)
[![Metodologia](https://img.shields.io/badge/Metodologia-Solo%20Ágil%20IA-green)](docs/01_Guias_Centrais/GUIA_AVANCADO.md)

## 🎯 Visão do Produto

O **Recoloca.AI** é um "Cockpit do Candidato" - uma plataforma integrada que oferece aos profissionais brasileiros **controle total e visibilidade** sobre seu processo de recolocação profissional, combinando ferramentas de gestão visual (Kanban) com inteligência artificial para otimização de currículos e coaching personalizado.

### 🚀 Proposta de Valor Central

- **📊 Gestão Visual de Candidaturas**: Kanban intuitivo para organizar e acompanhar o pipeline de oportunidades
- **🤖 Otimização Inteligente de CV**: IA que analisa e adapta currículos para vagas específicas
- **💬 Coach IA Proativo**: Assistente que oferece orientações personalizadas e acompanha o progresso
- **📈 Analytics de Carreira**: Insights sobre performance e tendências do mercado
- **🇧🇷 Foco no Mercado Brasileiro**: Adaptado às particularidades culturais e legais do Brasil

## 🏗️ Arquitetura e Stack Tecnológica

### Backend
- **FastAPI** (Python) - API REST principal
- **Supabase** - BaaS com PostgreSQL e Row Level Security (RLS)
- **LangChain** - Framework para integração com LLMs
- **FAISS-GPU** - Busca vetorial para sistema RAG

### Frontend
- **Flutter** - Aplicação web responsiva e mobile
- **Material Design 3** - Sistema de design

### IA e Dados
- **Gemini/OpenRouter** - LLMs para processamento de linguagem natural
- **BAAI/bge-m3** - Modelo de embedding multilíngue
- **RAG (Retrieval Augmented Generation)** - Sistema de conhecimento aumentado

### Infraestrutura
- **Vercel** - Deploy do frontend
- **Render/Railway** - Deploy do backend
- **Pipedream** - Automações e integrações

## 📋 Status do Projeto

### 🎯 Fase Atual: Validação e Estruturação (Fase 1)

**Prioridades Críticas:**
- ⏫ **Validação Técnica**: Protótipo RLS FastAPI/Supabase
- ⏫ **Validação de Negócio**: Estimativa detalhada de custos iniciais
- ⏫ **Validação UX/Valor**: Entrevistas com usuários-alvo (3-5 profissionais de TI)
- ⏫ **Protótipos**: Mockups de baixa fidelidade para validação

### 📊 Roadmap do MVP

#### **Core Features (Fase 1-2)**
1. **Sistema de Autenticação e Contas**
2. **Kanban de Candidaturas** (Feature Principal)
3. **Upload e Parsing de CV**
4. **Análise IA Vaga-CV (Score de Adequação)**
5. **Coach IA Básico**
6. **Sistema de Pagamentos (Freemium)**

#### **Features Avançadas (Fase 3+)**
- Importação inteligente de vagas
- Otimização avançada de CV
- Analytics e insights de mercado
- Integração com plataformas de emprego

## 🤖 Metodologia: "Solo Ágil Aumentado por IA"

Este projeto é desenvolvido usando uma metodologia inovadora onde um desenvolvedor solo ("Maestro") colabora intensivamente com **Agentes de IA Mentores** especializados:

### 🎭 Agentes de IA Mentores

- **@AgenteOrquestrador** - PM Mentor e Engenheiro de Prompt
- **@AgenteMentorDevFastAPI** - Especialista em Backend Python/FastAPI
- **@AgenteMentorDevFlutter** - Especialista em Frontend Flutter
- **@AgenteMentorArquitetoLLD** - Arquiteto de Software (Low Level Design)
- **@AgenteMentorPO** - Product Owner e UX Strategy
- **@AgenteM_UIDesigner** - UI/UX Designer
- **@AgenteMentorAPI** - Especialista em Design de APIs
- **@AgenteMentorQA** - Quality Assurance e Testes
- **@AgenteM_DevOps** - DevOps e Infraestrutura
- **@AgenteMentorSeguranca** - Segurança e Compliance

### 📚 Sistema RAG (Retrieval Augmented Generation)

Todos os agentes têm acesso à **"Documentação Viva"** do projeto através de um sistema RAG que inclui:
- Plano Mestre e especificações técnicas
- Conhecimento especializado em UX, Product Management, e tecnologias
- Contexto específico do mercado brasileiro
- Melhores práticas de desenvolvimento

## 📁 Estrutura do Projeto

```
🧑🏻‍💼 Recoloca.AI/
├── 📄 README.md                    # Este arquivo
├── 📁 docs/                        # Documentação Viva
│   ├── 📁 00_Gerenciamento_Projeto/ # Kanban, Tasks, Planejamento
│   ├── 📁 01_Guias_Centrais/       # Plano Mestre, Guia Avançado, Glossário
│   ├── 📁 02_Requisitos/           # ERS, Histórias de Usuário
│   ├── 📁 03_Arquitetura_e_Design/ # HLD, LLD, ADRs
│   ├── 📁 04_Agentes_IA/           # Perfis e configurações dos agentes
│   ├── 📁 05_Prompts/              # Templates e prompts otimizados
│   └── 📁 09_Pesquisa_e_Insights/  # Pesquisas de mercado e UX
├── 📁 src/                         # Código fonte
│   ├── 📁 backend_fastapi/         # API FastAPI
│   └── 📁 frontend_flutter/        # App Flutter
├── 📁 rag_infra/                   # Infraestrutura RAG
│   ├── 📁 source_documents/        # Base de conhecimento
│   └── 📄 environment.yml          # Ambiente Conda
└── 📁 .trae/                       # Configurações Trae IDE
```

## 🚀 Como Começar

### Pré-requisitos
- **Trae IDE** - IDE principal para desenvolvimento com IA
- **Conda** - Gerenciamento de ambiente Python
- **Git** - Controle de versão
- **Flutter SDK** - Para desenvolvimento frontend
- **Supabase CLI** - Para gerenciamento do backend

### Configuração do Ambiente

1. **Clone o repositório**
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd Recoloca.AI
   ```

2. **Configure o ambiente RAG**
   ```bash
   cd rag_infra
   conda env create -f environment.yml
   conda activate Agents_RAG_Env
   ```

3. **Configure o backend**
   ```bash
   cd src/backend_fastapi
   pip install -r requirements.txt
   ```

4. **Configure o frontend**
   ```bash
   cd src/frontend_flutter
   flutter pub get
   ```

### Executando o Projeto

```bash
# Backend (FastAPI)
cd src/backend_fastapi
uvicorn main:app --reload

# Frontend (Flutter Web)
cd src/frontend_flutter
flutter run -d web-server --web-port 3000
```

## 📖 Documentação Principal

- **[📋 Plano Mestre](docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md)** - Visão completa do projeto
- **[🎯 Guia Avançado](docs/01_Guias_Centrais/GUIA_AVANCADO.md)** - Metodologia e práticas
- **[📊 Kanban Interno](docs/00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md)** - Status e prioridades
- **[📝 ERS](docs/02_Requisitos/ERS.md)** - Especificação de requisitos
- **[🏗️ HLD](docs/03_Arquitetura_e_Design/HLD.md)** - Arquitetura de alto nível
- **[📚 Glossário](docs/01_Guias_Centrais/GLOSSARIO_Recoloca_AI.md)** - Termos e conceitos

## 🎯 Objetivos do MVP

### Funcionalidades Essenciais
1. **Autenticação segura** com Supabase Auth
2. **Kanban de candidaturas** com drag-and-drop
3. **Upload e parsing de CV** em PDF
4. **Score de adequação IA** para vagas
5. **Coach IA básico** com orientações
6. **Sistema freemium** com Stripe

### Métricas de Sucesso
- **Time-to-Value**: < 5 minutos para primeira vaga no Kanban
- **Engagement**: 70% dos usuários retornam em 7 dias
- **Conversão**: 15% dos usuários gratuitos migram para premium
- **Satisfação**: NPS > 50 após 30 dias de uso

## 🤝 Contribuição

Este é um projeto de desenvolvimento solo aumentado por IA. As contribuições são bem-vindas através de:

1. **Issues** - Reporte bugs ou sugira melhorias
2. **Feedback de UX** - Participe de entrevistas de usuário
3. **Documentação** - Ajude a melhorar a documentação
4. **Testes** - Teste funcionalidades em desenvolvimento

## 📄 Licença

[Definir licença apropriada]

## 📞 Contato

**Maestro (Desenvolvedor Principal)**: Bruno S. Rosa  
**Email**: [email]  
**LinkedIn**: [perfil]

---

> 💡 **Nota**: Este projeto representa uma exploração prática de como a IA pode amplificar as capacidades de um desenvolvedor solo, criando um produto completo e competitivo no mercado de recolocação profissional brasileiro.

**Última atualização**: Junho 2025