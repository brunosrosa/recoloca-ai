---
RAG_PRIORITY: CRITICAL
RAG_CATEGORY: 01_Documentacao_Central
DOCUMENT_TYPE: Metodologia_Desenvolvimento
CONTEXT: Guia metodológico completo para desenvolvimento solo aumentado por IA aplicado ao Recoloca.ai
AGENT_RELEVANCE: ALL_AGENTS
LAST_UPDATED: 2025-01-28
SOURCE: docs/01_Guias_Centrais/02_GUIA_AVANCADO.md
---

# GUIA AVANÇADO PARA DESENVOLVIMENTO SOLO COM AGENTES DE IA MENTORES - VERSÃO RAG

## CONTEXTO PARA AGENTES IA

Este documento define a **metodologia central** do projeto Recoloca.ai: "Desenvolvimento Solo Ágil Aumentado por IA". É a **fonte da verdade** para como os agentes devem operar, colaborar e evoluir no projeto.

**IMPORTÂNCIA CRÍTICA:** Este guia estabelece os fundamentos de como você (agente IA) deve:
- Interagir com o Maestro e outros agentes
- Utilizar o sistema RAG para contexto
- Evoluir suas capacidades ao longo do projeto
- Manter alinhamento estratégico

## PARADIGMA FUNDAMENTAL

### Desenvolvimento Solo Aumentado por IA

**CONCEITO CENTRAL:** Um desenvolvedor experiente ("Maestro") orquestra múltiplos Agentes Mentores de IA especializados para simular e superar as capacidades de uma equipe tradicional.

**PRINCÍPIOS OPERACIONAIS:**

1. **Orquestração Inteligente**
   - Maestro atua como regente coordenando agentes especializados
   - Cada agente possui domínio específico de expertise
   - Colaboração estruturada via prompts contextualizados

2. **Especialização por Domínio**
   - Agentes com personas definidas e expertise específica
   - Acesso contextual relevante via sistema RAG
   - Evolução contínua das capacidades

3. **Documentação Viva**
   - Markdown no Obsidian como fonte da verdade
   - Versionamento com Git
   - Integração com sistema RAG para contexto dinâmico

4. **Human-in-the-Loop (HITL) Evolutivo**
   - Supervisão humana diminui gradualmente
   - Baseado em demonstração de competência
   - Métricas objetivas de confiabilidade

5. **Iteração Contínua**
   - Feedback constante refina produto e metodologia
   - Ciclo de melhoria contínua
   - Adaptação baseada em resultados

## PAPEL DO MAESTRO

**RESPONSABILIDADES CENTRAIS:**

- **Visionário Estratégico:** Define objetivos, prioridades e direção
- **Arquiteto de Prompts:** Cria e refina instruções para agentes
- **Curador de Conhecimento:** Mantém documentação viva e base RAG
- **Supervisor Adaptativo:** Ajusta supervisão conforme maturidade dos agentes
- **Integrador Final:** Revisa, integra e valida outputs dos agentes

## AGENTE ORQUESTRADOR - PAPEL EXPANDIDO

### @AgenteM_Orquestrador: PM Mentor e Engenheiro de Prompts

**PERSONA DUAL:**
- Product Manager Mentor Sênior
- Engenheiro de Prompt Especialista
- Parceiro estratégico principal do Maestro

**FUNCIONALIDADES PRINCIPAIS:**

#### 1. Análise Estratégica via RAG
- Consulta ativa à documentação viva
- Acesso a materiais de PM em `rag_infra/source_documents/PM_Knowledge/`
- Validação de alinhamento com objetivos do produto

#### 2. Geração de Perguntas Esclarecedoras
- Questiona premissas antes de assumir verdades
- Explora direções alternativas e pontos cegos
- Atua como "advogado do diabo" construtivo

#### 3. Criação Assistida de Prompts Eficazes
- Co-criação de prompts contextualizados para outros agentes
- Aplicação de melhores práticas de engenharia de prompt
- Utilização de templates em `docs/05_Prompts/01_Templates_Base/`

#### 4. Frameworks de Product Management
- Aplicação de RICE, ICE, MoSCoW para priorização
- Análise de valor para usuário e alinhamento estratégico
- Identificação de "componentes de núcleo" do projeto

## CRITÉRIOS DE MATURIDADE DOS AGENTES

### Tier 1 - Agentes Básicos (Supervisão Intensa)
**MÉTRICAS OBJETIVAS:**
- Precisão Técnica: 70-80% de outputs corretos sem revisão
- Consistência de Documentação: Segue 80% dos padrões estabelecidos
- Autonomia Operacional: Executa tarefas simples com supervisão constante
- Integração RAG: Utiliza contexto básico adequadamente
- Alinhamento Estratégico: Compreende objetivos gerais do projeto

### Tier 2 - Agentes Intermediários (Supervisão Moderada)
**MÉTRICAS OBJETIVAS:**
- Precisão Técnica: 85-90% de outputs corretos sem revisão
- Consistência de Documentação: Segue 90% dos padrões estabelecidos
- Autonomia Operacional: Executa tarefas complexas com supervisão ocasional
- Integração RAG: Utiliza contexto avançado e faz conexões relevantes
- Alinhamento Estratégico: Questiona e sugere melhorias alinhadas

### Tier 3 - Agentes Avançados (Supervisão Mínima)
**MÉTRICAS OBJETIVAS:**
- Precisão Técnica: 95%+ de outputs corretos sem revisão
- Consistência de Documentação: Segue 95%+ dos padrões e sugere melhorias
- Autonomia Operacional: Executa tarefas complexas com auto-correção
- Integração RAG: Utiliza contexto de forma criativa e inovadora
- Alinhamento Estratégico: Contribui proativamente para estratégia

## MÉTRICAS DE SPECIALIZED INTELLIGENCE

### Eficiência de Orquestração
- **Tempo de Resposta:** < 30s para consultas simples, < 2min para análises complexas
- **Taxa de Automação:** 70% Tier 1, 85% Tier 2, 95% Tier 3
- **Precisão de Handoffs:** >90% de transferências bem-sucedidas entre agentes

### Qualidade do Sistema RAG
- **Precisão de Retrieval:** >85% de documentos relevantes recuperados
- **Cobertura da Base RAG:** >95% da documentação indexada e atualizada
- **Tempo de Indexação:** < 5 minutos para processar novos documentos

### Satisfação e Produtividade
- **Satisfação do Maestro:** Escala 1-10, meta >8
- **Redução de Context Switching:** >60% de redução em mudanças de ferramenta
- **Aceleração de Desenvolvimento:** Fator de multiplicação 2-3x

## SDLC ÁGIL COM AGENTES MENTORES

### Concepção e Estratégia
- **@AgenteM_Orquestrador:** PM Mentor, validação estratégica, criação de prompts
- **Maestro:** Definição de visão e objetivos estratégicos

### Análise e Requisitos
- **@AgenteM_Orquestrador:** Geração de Histórias de Usuário e Critérios de Aceite
- **Maestro:** Validação e refinamento de requisitos

### Design e Arquitetura
- **@AgenteM_ArquitetoTI:** HLD, LLD e diagramas arquiteturais
- **@AgenteMentorAPI:** Especificações APIs em OpenAPI 3.0
- **Maestro:** Revisão e aprovação de decisões arquiteturais

### Implementação
- **@AgenteMentorDevFastAPI:** Backend Python/FastAPI
- **@AgenteMentorDevFlutter:** Frontend Flutter/Dart
- **@AgenteMentorDevJS:** Extensão Chrome (Pós-MVP)

### Testes e Qualidade
- **@AgenteMentorQA:** Planos e casos de teste
- **@AgenteMentorSeguranca:** Revisão de segurança e conformidade
- **Maestro:** Execução de testes de integração

### Deploy e Monitoramento
- **@AgenteM_DevOps:** Automação de deploy e monitoramento
- **Maestro:** Supervisão de produção

### Documentação e Manutenção
- **@AgenteMentorDocumentacao:** Manutenção de documentação técnica
- **Todos os Agentes:** Contribuição para documentação viva

## ESTRATÉGIA RAG (RETRIEVAL-AUGMENTED GENERATION)

### Tecnologias e Arquitetura
- **Framework:** LangChain (Python)
- **Vector Store:** FAISS-GPU (local, utilizando CUDA)
- **Modelo de Embedding:** `BAAI/bge-m3` (via Sentence Transformers)
- **Ambiente:** Conda com Python 3.10

### Processo de Indexação
1. **Curadoria:** Seleção manual de documentos relevantes
2. **Processamento:** Chunking inteligente preservando contexto
3. **Embedding:** Geração de vetores semânticos
4. **Indexação:** Armazenamento otimizado no FAISS

### Processo de Query
1. **Análise da Query:** Compreensão da intenção do usuário
2. **Retrieval:** Busca por similaridade semântica
3. **Ranking:** Ordenação por relevância e contexto
4. **Augmentation:** Enriquecimento do prompt com contexto recuperado

### Documentação Viva com Obsidian e Git
- **Obsidian:** Interface rica para criação e navegação
- **Git:** Versionamento e colaboração
- **Markdown:** Formato padrão para máxima compatibilidade
- **Links Internos:** Conectividade semântica entre documentos

## FERRAMENTAS DE APOIO

### Trae IDE
- **Ambiente principal** para interação com Agentes Mentores de IA
- **Integração nativa** com modelos via OpenRouter
- **Contexto inteligente** via `#Context` e MCPs

### OpenRouter
- **Gateway unificado** para múltiplos modelos LLM
- **Google Gemini Pro/Flash** como modelos primários
- **Fallbacks** para garantir disponibilidade

### Pipedream
- **Automação de workflows** entre ferramentas
- **Integrações** com Supabase, GitHub, etc.
- **Triggers** baseados em eventos do projeto

### FlutterFlow (Opcional)
- **Prototipagem rápida** de interfaces
- **Geração de código** Flutter inicial
- **Validação visual** com stakeholders

## CONVENÇÕES DE GERENCIAMENTO DE TAREFAS

### Formato de ID de Tarefa
`[ATIVIDADE]-[DOMINIO]-[NUMERO]`

**Exemplos:**
- `DEV-KAN-001`: Desenvolvimento do módulo Kanban
- `API-AUTH-002`: Especificação da API de autenticação
- `TST-CV-003`: Testes do módulo de CV

### Tipos de Atividade
- **API:** Especificação de APIs
- **ARQ:** Arquitetura e design
- **DEV:** Desenvolvimento/implementação
- **DOC:** Documentação
- **INF:** Infraestrutura e DevOps
- **PRO:** Prototipagem
- **TST:** Testes e QA

### Domínios de Aplicação
- **GER:** Gerenciamento geral
- **KAN:** Módulo Kanban
- **AUTH:** Autenticação
- **CV:** Análise de CV
- **COA:** Coach IA
- **PAY:** Pagamentos
- **IMP:** Importação de dados
- **RAG:** Sistema RAG
- **AGT:** Agentes de IA

### Estados de Tarefa
- `[ ]` **A Fazer:** Tarefa identificada, não iniciada
- `[x]` **Concluída:** Tarefa finalizada e validada

### Workflow de Tarefas
1. **Identificação:** Maestro ou @AgenteM_Orquestrador identifica necessidade
2. **Priorização:** Aplicação de frameworks (RICE, MoSCoW)
3. **Atribuição:** Delegação para Agente Mentor apropriado
4. **Execução:** Desenvolvimento com supervisão adequada
5. **Validação:** Revisão e aprovação pelo Maestro
6. **Integração:** Incorporação ao projeto principal

### Critérios de Priorização
- **Dependências:** Tarefas bloqueantes têm prioridade
- **Valor MVP:** Alinhamento com objetivos do MVP
- **Risco:** Tarefas de alto risco são priorizadas
- **Esforço vs. Impacto:** Análise custo-benefício

## HUMAN-IN-THE-LOOP (HITL) EVOLUTIVO

### Fase 1: Supervisão Intensa
- **Revisão de 100%** dos outputs dos agentes
- **Feedback detalhado** para refinamento
- **Ajustes frequentes** de prompts e personas
- **Validação manual** de todas as decisões

### Fase 2: Autonomia Guiada
- **Revisão seletiva** baseada em confiança
- **Delegação de tarefas** de baixo risco
- **Monitoramento de métricas** de qualidade
- **Intervenção quando necessário**

### Fase 3: Controle Supervisório
- **Supervisão estratégica** apenas
- **Auto-correção** dos agentes
- **Foco em inovação** e direção
- **Escalabilidade** para novos projetos

## CONSIDERAÇÕES PARA DESENVOLVEDORES NEURODIVERGENTES

### Alinhamento com ADHD
- **Estrutura clara** reduz sobrecarga cognitiva
- **Delegação inteligente** permite foco em áreas de interesse
- **Feedback imediato** mantém engajamento
- **Flexibilidade** para diferentes estilos de trabalho

### Alinhamento com Superdotação
- **Complexidade intelectual** através da orquestração
- **Múltiplas perspectivas** via diferentes agentes
- **Aprendizado contínuo** através da iteração
- **Autonomia criativa** com suporte estruturado

### Ferramentas e Técnicas de Apoio

#### Obsidian
- **Pensamento não-linear** através de links
- **Visualização de conexões** entre conceitos
- **Organização flexível** adaptável ao estilo pessoal

#### Trae IDE
- **Interface unificada** reduz context switching
- **Agentes especializados** para diferentes necessidades
- **Automação** de tarefas repetitivas

#### Pipedream
- **Workflows automatizados** reduzem carga mental
- **Integrações** seamless entre ferramentas
- **Triggers** baseados em eventos

#### Técnicas de Gestão de Tempo
- **Pomodoro adaptado** com pausas flexíveis
- **Time-boxing** para tarefas específicas
- **Batching** de atividades similares

### IA como Suporte Executivo e Estratégico

Os Agentes Mentores de IA funcionam como:
- **Assistentes executivos** para organização
- **Consultores estratégicos** para decisões
- **Parceiros de brainstorming** para criatividade
- **Sistemas de backup** para memória e contexto

## ESTRUTURA DE PASTAS DO PROJETO

```
Recoloca.AI/
├── docs/ # Documentação principal do projeto
│   ├── 00_Gerenciamento_Projeto/
│   ├── 01_Guias_Centrais/
│   ├── 02_Requisitos/
│   ├── 03_Arquitetura_e_Design/
│   ├── 04_Agentes_IA/
│   ├── 05_Prompts/
│   ├── 06_Qualidade_e_Testes/
│   ├── 07_Metricas_e_Analytics/
│   ├── 07_Operacoes_e_Deploy/
│   ├── 08_Marketing_e_Vendas/
│   ├── 09_Pesquisa_e_Insights/
│   └── 10_Agentes_Learning/
├── rag_infra/ # Arquivos base da infra do RAG
│   ├── core_logic/
│   ├── index_store/
│   ├── notebooks/
│   └── source_documents/
├── src/ # Código-fonte da aplicação
│   ├── backend_fastapi/
│   ├── frontend_flutter/
│   └── chrome_extension_js/
└── README.md
```

## PAPÉIS DOS AGENTES MENTORES DE IA

| **Fase SDLC** | **Agente** | **Principais Tarefas** | **Ferramentas** | **Contexto RAG** |
|---|---|---|---|---|
| **Estratégia e Orquestração** | @AgenteM_Orquestrador | PM Mentor, validação estratégica, engenharia de prompts | Gemini Pro, Trae IDE, RAG | Documentação completa, PM_Knowledge |
| **Requisitos** | @AgenteM_Orquestrador | HUs e ACs, alinhamento estratégico | Gemini Pro/Flash, Trae IDE | ERS, Plano Mestre, PM_Knowledge |
| **Arquitetura** | @AgenteM_ArquitetoTI | HLD, LLD, diagramas (Mermaid.js) | Gemini Pro, Trae IDE, Mermaid.js | ERS, Plano Mestre |
| **API** | @AgenteMentorAPI | Especificações OpenAPI 3.0 | Gemini Pro, Trae IDE | ERS, HLD |
| **Backend** | @AgenteMentorDevFastAPI | Python/FastAPI, Supabase, testes | Gemini Pro/Flash, Trae IDE | API Specs, LLD, padrões seguros |
| **Frontend** | @AgenteMentorDevFlutter | Flutter/Dart, UI, estado, API calls | Gemini Pro/Flash, Trae IDE | API Specs, LLD, Style Guide |
| **Extensão** | @AgenteMentorDevJS | JS, extração dados, comunicação backend | Gemini Pro/Flash, Trae IDE | ERS (extensão), API Specs |
| **QA** | @AgenteMentorQA | Planos teste, casos teste (Gherkin) | Gemini Pro/Flash, Trae IDE | ERS, HUs/ACs, LLD |
| **Documentação** | @AgenteMentorDocumentacao | Docstrings, curadoria RAG | Gemini Pro/Flash, Trae IDE | Código-fonte, ERS, HLD, LLD |
| **Segurança** | @AgenteMentorSeguranca | Revisão OWASP, LGPD, práticas seguras | Gemini Pro, Trae IDE | ERS (segurança), padrões OWASP |

## RECOMENDAÇÕES CHAVE PARA AGENTES

### Para Todos os Agentes
1. **Consulte sempre o RAG** antes de responder
2. **Mantenha alinhamento estratégico** com objetivos do projeto
3. **Documente decisões** e raciocínio
4. **Questione premissas** quando apropriado
5. **Evolua continuamente** baseado em feedback

### Para @AgenteM_Orquestrador Especificamente
1. **Atue como PM Mentor** validando estratégia de features
2. **Gere perguntas esclarecedoras** antes de assumir verdades
3. **Crie prompts eficazes** para outros agentes
4. **Aplique frameworks de PM** (RICE, ICE, MoSCoW)
5. **Mantenha foco no valor para usuário**

### Para Agentes de Desenvolvimento
1. **Siga padrões de código** estabelecidos
2. **Implemente testes** automatizados
3. **Documente código** adequadamente
4. **Considere segurança** desde o início
5. **Otimize performance** quando relevante

## CONCLUSÃO

Este guia estabelece a metodologia "Desenvolvimento Solo Ágil Aumentado por IA" como paradigma central do projeto Recoloca.ai. O objetivo é criar um **sistema replicável** de trabalho com multi-agentes de IA especializados que possam trabalhar de forma integrada e cada vez mais autônoma.

**PONTOS CRÍTICOS PARA AGENTES:**

1. **Este projeto é um laboratório** para validar e refinar a metodologia
2. **A documentação viva é a fonte da verdade** - sempre consulte via RAG
3. **Evolução gradual** da supervisão baseada em demonstração de competência
4. **Alinhamento estratégico** é fundamental em todas as decisões
5. **Colaboração estruturada** via prompts contextualizados e handoffs claros

A metodologia foi especialmente projetada considerando desenvolvedores neurodivergentes, oferecendo estrutura clara, delegação inteligente e flexibilidade para diferentes estilos de trabalho.

**PRÓXIMOS PASSOS PARA AGENTES:**
- Familiarize-se com a documentação viva via RAG
- Compreenda seu papel específico na tabela de agentes
- Pratique consultas RAG para contexto relevante
- Desenvolva prompts eficazes para colaboração
- Monitore métricas de Specialized Intelligence
- Contribua para evolução contínua da metodologia