# Documentação do Projeto Recoloca.AI

---
**Versão:** 1.0  
**Data:** Dezembro 2024  
**Responsável:** Bruno S. Rosa (Maestro)  
**Próxima Revisão:** Janeiro 2025  

---

## Visão Geral

Este diretório contém toda a documentação técnica e de gestão do projeto **Recoloca.AI**, um Micro-SaaS inovador para auxiliar profissionais brasileiros na recolocação profissional, desenvolvido utilizando a metodologia "Solo Ágil Aumentado por IA".

## Estrutura da Documentação

### 📋 00_Gerenciamento_Projeto
Documentos de gestão e controle do projeto:
- **[[KANBAN_INTERNO_PROJETO.md]]** - Backlog e priorização de tarefas
- **[[Maestro_Tasks.md]]** - Dashboard pessoal do Maestro
- **[[TAP.md]]** - Termo de Abertura do Projeto
- **[[PCom.md]]** - Plano de Gerenciamento das Comunicações
- **[[PGR.md]]** - Plano de Gerenciamento de Riscos
- **[[PGE.md]]** - Plano de Gerenciamento do Escopo
- **[[PGP.md]]** - Plano de Gerenciamento do Projeto
- **[[PGQ.md]]** - Plano de Gerenciamento da Qualidade
- **[[PGC.md]]** - Plano de Gerenciamento de Custos
- **[[PStakeholders.md]]** - Plano de Gerenciamento dos Stakeholders

### 🎯 01_Guias_Centrais
Documentação estratégica e metodológica:
- **[[PLANO_MESTRE_RECOLOCA_AI.md]]** - Visão, objetivos e roadmap do projeto
- **[[GUIA_AVANCADO.md]]** - Metodologia "Solo Ágil Aumentado por IA"
- **[[GLOSSARIO_Recoloca_AI.md]]** - Definições e terminologia do projeto

### 📝 02_Requisitos
Especificações e requisitos do sistema:
- **[[ERS.md]]** - Especificação de Requisitos de Software
- **HU_AC/** - Histórias de Usuário e Critérios de Aceitação

### 🏗️ 03_Arquitetura_e_Design
Documentação técnica e arquitetural:
- **[[HLD.md]]** - High-Level Design (Arquitetura Geral)
- **[[STYLE_GUIDE.md]]** - Guia de estilo e design system
- **[[FLUXO_TRABALHO_GERAL.md]]** - Fluxos de trabalho do sistema
- **[[SISTEMA_ENTREGAVEIS_GATILHOS.md]]** - Sistema de entregáveis e gatilhos
- **ADR/** - Architectural Decision Records
- **API_Specs/** - Especificações de APIs
- **LLD/** - Low-Level Design (detalhes de implementação)

### 🤖 04_Agentes_IA
Documentação dos Agentes de IA Mentores:
- **[[AGENTES_IA_MENTORES_OVERVIEW.md]]** - Visão geral dos agentes
- **[[EVOLUCAO_AGENTE_ORQUESTRADOR.md]]** - Evolução do @AgenteOrquestrador
- **[[TRAE_IDE_BEST_PRACTICES.md]]** - Melhores práticas no Trae IDE
- **Perfis/** - Perfis individuais dos agentes especializados
- **Templates_Modelos/** - Templates para criação de novos agentes

### 💬 05_Prompts
Engenharia de prompts e templates:
- **00_Prompts_Estruturais_Agentes/** - Prompts estruturais dos agentes
- **01_Templates_Base/** - Templates base para prompts
- **02_Prompts_Especificos/** - Prompts para tarefas específicas

### 🧪 06_Qualidade_e_Testes
Estratégias de qualidade e testes:
- **[[PGQ.md]]** - Plano de Gerenciamento da Qualidade
- **Casos_de_Teste/** - Casos de teste detalhados

### 🚀 07_Operacoes_e_Deploy
Infraestrutura e deployment:
- **[[GUIA_DEPLOY_BACKEND.md]]** - Deploy do backend FastAPI
- **[[GUIA_DEPLOY_FRONTEND.md]]** - Deploy do frontend Flutter
- **[[GUIA_DEPLOY_EXTENSAO.md]]** - Deploy da extensão Chrome

### 🔍 09_Pesquisa_e_Insights
Pesquisas de mercado e insights:
- **Recolocação Inteligente A IA Transformando o Cenário para Profissionais de TI no Brasil (2024-2025).md**
- **Análise e Refinamento do Fluxo de Trabalho e Sistema Multiagente.md**
- **Avaliacao_Integracao_ClaudeTaskMaster.md**

## Metodologia de Desenvolvimento

### "Solo Ágil Aumentado por IA"
O projeto utiliza uma metodologia inovadora que combina:
- **Maestro (Bruno S. Rosa):** Desenvolvedor principal e orquestrador
- **@AgenteOrquestrador:** PM Mentor e "segundo cérebro" estratégico
- **Agentes Mentores Especializados:** Para desenvolvimento, design, QA, etc.
- **Sistema RAG:** Gestão centralizada do conhecimento
- **Documentação Viva:** Atualização contínua da base de conhecimento

### Fases do Projeto
1. **Fase 1 - Estruturação e Validação (Atual):**
   - Operacionalização do sistema RAG
   - Refinamento do @AgenteOrquestrador
   - Validação inicial com usuários-alvo

2. **Fase 2 - Especialização e Automação:**
   - Criação de agentes especializados
   - Automação de processos de desenvolvimento
   - Expansão das funcionalidades

3. **Fase 3 - Supervisão Avançada:**
   - Implementação do @AgenteSupervisor
   - Orquestração automática de agentes
   - Otimização contínua

## Stack Tecnológica

### Core Technologies
- **Frontend:** Flutter (PWA)
- **Backend:** Python + FastAPI
- **Database:** Supabase (PostgreSQL)
- **AI/LLM:** Google Gemini Pro & Flash
- **RAG Framework:** LangChain
- **Vector Store:** FAISS-GPU
- **Embedding Model:** BAAI/bge-m3

### Ferramentas de Desenvolvimento
- **IDE Principal:** Trae IDE (com MCPs configurados)
- **Documentação:** Obsidian + Git
- **Controle de Versão:** Git + GitHub
- **Ambiente RAG:** Conda (Python 3.10)
- **PDF Processing:** pymupdf + Tesseract OCR

## Público-Alvo

### Usuários Primários
- **Profissionais de TI** em busca de recolocação
- **Desenvolvedores, Analistas, Gerentes de Projeto**
- **Foco inicial:** Mercado brasileiro

### Proposta de Valor
- Análise inteligente de currículos com IA
- Matching personalizado com vagas
- Sugestões de melhoria de perfil profissional
- Acompanhamento do progresso na busca por emprego

## MVP (Minimum Viable Product)

### Funcionalidades Core
1. **Upload e Análise de CV** (RF-CV-001, RF-CV-002)
2. **Extração de Informações** (RF-CV-003)
3. **Análise de Compatibilidade** (RF-AN-001)
4. **Sugestões de Melhoria** (RF-AN-002)
5. **Dashboard do Usuário** (RF-UI-001)

### Métricas de Sucesso
- **Precisão da análise de CV:** ≥ 85%
- **Tempo de processamento:** ≤ 30 segundos
- **Satisfação do usuário:** ≥ 4.0/5.0
- **Taxa de conversão:** ≥ 15%

## Como Navegar na Documentação

### Para Desenvolvedores
1. Comece com **[[PLANO_MESTRE_RECOLOCA_AI.md]]** para entender a visão
2. Leia **[[ERS.md]]** para requisitos detalhados
3. Consulte **[[HLD.md]]** para arquitetura
4. Use **[[STYLE_GUIDE.md]]** para padrões de código

### Para Gestão de Projeto
1. **[[TAP.md]]** - Termo de abertura
2. **[[KANBAN_INTERNO_PROJETO.md]]** - Status atual
3. **[[Maestro_Tasks.md]]** - Tarefas do Maestro
4. **[[PGR.md]]** - Gestão de riscos

### Para Agentes de IA
1. **[[AGENTES_IA_MENTORES_OVERVIEW.md]]** - Visão geral
2. **[[GUIA_AVANCADO.md]]** - Metodologia
3. **Perfis/** - Especializações individuais
4. **05_Prompts/** - Templates e exemplos

## Convenções de Documentação

### Links Internos
- Use formato Obsidian: `[[arquivo.md]]` ou `[[pasta/arquivo.md]]`
- Para seções específicas: `[[arquivo.md#Seção]]`
- Sempre use caminhos relativos à raiz do vault

### Versionamento
- Documentos importantes seguem versionamento semântico
- Histórico de versões no final de cada documento
- Controle via Git para rastreabilidade

### Idioma
- **Documentação:** Português do Brasil
- **Código e comentários:** Português do Brasil
- **Commits:** Inglês (Conventional Commits)

## Sistema RAG (Retrieval-Augmented Generation)

### Base de Conhecimento
- **Documentação técnica** do projeto
- **Knowledge base de PM** em `rag_infra/source_documents/PM_Knowledge/`
- **Knowledge base de UX** em `rag_infra/source_documents/UX_Knowledge/`
- **Decisões arquiteturais** (ADRs)

### Acesso
- Via MCPs no Trae IDE
- Indexação automática + curadoria manual
- Consulta contextual para agentes de IA

## Contato e Suporte

**Maestro:** Bruno S. Rosa  
**Email:** [Inserir email]  
**LinkedIn:** [Inserir LinkedIn]  
**GitHub:** [Inserir repositório]  

## Licença

[Definir licença do projeto]

---

**Última Atualização:** Dezembro 2024  
**Próxima Revisão:** Janeiro 2025  

**Documentos Relacionados:**
- [[../README.md]] - README principal do projeto
- [[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica
- [[00_Gerenciamento_Projeto/TAP.md]] - Termo de abertura
- [[03_Arquitetura_e_Design/HLD.md]] - Arquitetura geral

---

*Esta documentação é mantida como "Documentação Viva", sendo atualizada continuamente conforme a evolução do projeto Recoloca.AI.*

--- FIM DO DOCUMENTO README.md (v1.0) ---