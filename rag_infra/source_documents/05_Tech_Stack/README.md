# 💻 Tech Stack

## 🎯 Propósito

Esta pasta contém toda a **documentação técnica sobre tecnologias, frameworks, bibliotecas e ferramentas** utilizadas no projeto Recoloca.ai.

## 📋 Tipos de Documentos

### ✅ Incluir Aqui:
- **Documentação de Frameworks** - FastAPI, React, etc.
- **Guias de Bibliotecas** - Pydantic, SQLAlchemy, etc.
- **Configurações de Ambiente** - Docker, deployment
- **Manuais de Ferramentas** - IDEs, CI/CD, monitoramento
- **Best Practices** - Padrões de uso específicos
- **Troubleshooting** - Soluções para problemas comuns
- **Comparações Técnicas** - Análises de alternativas
- **Tutoriais Específicos** - Como usar tecnologias escolhidas

### ❌ Não Incluir:
- Código fonte (manter no repositório)
- Arquitetura geral (usar 03_Arquitetura_e_Design)
- Processos de desenvolvimento (usar 01_Gestao_e_Processos)

## 🔍 Prioridade RAG

**Alta Prioridade** - Essencial para:
- @AgenteM_DevFastAPI - Implementação backend
- @AgenteM_ArquitetoTI - Decisões técnicas
- @AgenteM_DevOps - Deploy e infraestrutura
- Todos os agentes técnicos para referência

## 📝 Convenções de Nomenclatura

```
[CATEGORIA]_[TECNOLOGIA]_para_RAG.md

Exemplos:
- FRAMEWORK_FASTAPI_para_RAG.md
- LIB_PYDANTIC_para_RAG.md
- TOOL_DOCKER_para_RAG.md
- DB_SUPABASE_para_RAG.md
- DEPLOY_VERCEL_para_RAG.md
```

## 🏷️ Categorias

### 🚀 Backend
- **FastAPI** - Framework principal
- **Pydantic** - Validação de dados
- **SQLAlchemy** - ORM
- **Uvicorn** - ASGI server
- **Python** - Linguagem base

### 🎨 Frontend
- **React** - Framework UI
- **TypeScript** - Linguagem
- **Tailwind CSS** - Styling
- **Next.js** - Framework React

### 🗄️ Banco de Dados
- **Supabase** - Backend as a Service
- **PostgreSQL** - Banco principal
- **Redis** - Cache (se aplicável)

### ☁️ Infraestrutura
- **Docker** - Containerização
- **Vercel** - Deploy frontend
- **Railway/Heroku** - Deploy backend
- **GitHub Actions** - CI/CD

### 🤖 IA e ML
- **OpenAI API** - LLMs
- **LangChain** - Framework IA
- **ChromaDB** - Vector database
- **Embeddings** - Processamento de texto

### 🛠️ Ferramentas
- **Git** - Controle de versão
- **VS Code** - IDE principal
- **Postman** - Testes de API
- **Pytest** - Testes automatizados

## 📚 Estrutura de Documentação

Cada tecnologia deve incluir:

### 📖 Visão Geral
- Propósito no projeto
- Versão utilizada
- Justificativa da escolha

### ⚙️ Configuração
- Instalação e setup
- Configurações específicas
- Variáveis de ambiente

### 🎯 Uso Prático
- Exemplos de código
- Padrões estabelecidos
- Best practices

### 🔧 Troubleshooting
- Problemas comuns
- Soluções testadas
- Logs e debugging

## 🔄 Manutenção

- **Frequência de Atualização**: Mensal ou quando há mudanças
- **Responsável**: @AgenteM_ArquitetoTI (coordenação)
- **Colaboradores**: Agentes técnicos conforme especialidade
- **Revisão**: A cada sprint para atualizações

## 📊 Versionamento

- Manter histórico de versões utilizadas
- Documentar mudanças e migrações
- Planos de atualização de dependências

## 🎯 Objetivos

- **Padronização** - Uso consistente das tecnologias
- **Eficiência** - Referência rápida para desenvolvimento
- **Qualidade** - Best practices documentadas
- **Onboarding** - Facilitar entrada de novos desenvolvedores

---

*Última atualização: $(date +"%Y-%m-%d")*