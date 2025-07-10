---
tags:
  - kanban
  - projeto
  - estrategico
  - backlog
status: ativo
versao: "1.0"
data_criacao: 2025-01-16
kanban-plugin: board
sticker: lucide//diamond
---

# 📋 KANBAN ESTRATÉGICO - BACKLOG RECOLOCA.AI

## 📊 **RESUMO EXECUTIVO**

**Status Atual:** Fase 0 (35-40% concluída) | **Foco:** Operacionalização RAG + Configuração Agentes Tier 1

**Próximas 4 Tarefas Críticas:**
1. Operacionalização Completa do RAG
2. Desenvolvimento do MCP Server  
3. Configuração RAG via MCP no TRAE IDE
4. Configuração dos 4 Agentes Tier 1 Restantes

**Critério de Transição Fase 1:** RAG + 5 Agentes + MCP 100% operacionais


## 🏗️ **FASE 0: RAG + AGENTES FOUNDATION** (Atual)
**Status:** 🟡 Em Andamento (60-65% concluído)  
**Objetivo:** Estabelecer base sólida de conhecimento e agentes especializados

### ✅ **CONCLUÍDO**
- [x] **[RAG-001]** Operacionalização do Sistema RAG
- [x] **[MCP-001]** Desenvolvimento do MCP Server para Integração RAG
- [x] **[CFG-001]** Configuração e Integração RAG via MCP no Trae IDE

### 🔄 **EM ANDAMENTO**
- [x] **[COR-RAG-001]** Correção do RAGRetriever Local 🔺 \ #rag \ #correção \ #local \ #retriever \ #critico \ #Fase0_RAG_Agentes `@AgenteM_ArquitetoTI` ✅ **CONCLUÍDO 19/06/2025**
	- [ ] Investigar incompatibilidade RAGRetriever com backend PyTorch
	- [ ] Corrigir interface de busca local
	- [ ] Implementar testes de validação
	- [ ] Documentar correções aplicadas
	- [ ] Validar consistência com MCP Server
	- **Dependências:** Sistema RAG operacional
	- **Definition of Done:** RAGRetriever local funcional + testes + documentação
- [x] **[DOC-ADR-001]** Documentação de ADRs Críticos 🔺 \ #documentacao \ #adr \ #arquitetura \ #decisoes \ #critico \ #Fase0_RAG_Agentes `@AgenteM_ArquitetoTI` ✅ **CONCLUÍDO 19/06/2025**
	- [ ] ADR-002: PyTorch vs FAISS-GPU
	- [ ] ADR-003: Otimizações RTX 2060
	- [ ] ADR-004: Evolução MCP Server
	- [ ] ADR-005: Reorganização estrutural
	- [ ] Consolidar decisões técnicas
	- **Dependências:** Infraestrutura RAG estável
	- **Definition of Done:** 4 ADRs documentados + consolidação técnica
- [x] **[DOC-LLD-001]** Consolidação do LLD 🔺 \ #lld \ #arquitetura \ #detalhamento \ #documentacao \ #Fase0_RAG_Agentes `@AgenteM_ArquitetoTI` ✅ **CONCLUÍDO 19/06/2025**
	- [x] Detalhar componentes RAG/MCP
	- [x] Especificar interfaces de integração
	- [x] Documentar estruturas de dados
	- [x] Definir padrões de implementação
	- [x] Validar com equipe técnica
	- **Dependências:** ADRs documentados
	- **Definition of Done:** LLD consolidado + validação técnica

### 📋 **PENDENTE**


- [ ] **[CFG-AGT-001] [ALTA]** Configuração dos Demais Agentes Tier 1
  - [ ] @AgenteM_DevFastAPI
  - [ ] @AgenteM_DevFlutter
  - [ ] @AgenteM_UXDesigner
  - **Responsável:** `@Maestro`
  - **Dependência:** Correção RAG local

- [ ] **[CFG-INF-001] [MVP]** Ambiente Dev/Deploy - Configuração Inicial 🔺 \\ #devops \\ #infra \\ #Semana1-2 \\ #Fase0_RAG_Agentes `@Maestro`
	- [ ] Criar repositórios Git para frontend, backend
	- [ ] Configurar linters, formatters e hooks de pré-commit
	- [ ] Setup inicial Vercel/Render para deploy

**Critério de Conclusão:** RAG + 5 Agentes + MCP 100% operacionais + Documentação arquitetural consolidada


## 📐 FASE 1: VALIDAÇÃO TÉCNICA E ESTRATÉGICA

- [ ] **Fase 1 (Semanas 3-7):** Validação Técnica e Estratégica + "AHA! Moments"
- [ ] **[DOC-ARQ-001] [MVP]** HLD Detalhado - Evolução para v1.2 🔺 \\ #arquitetura \\ #hld \\ #critico \\ #Semana1-2 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_ArquitetoTI` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Detalhamento completo da arquitetura de segurança (RLS)
	- [ ] Especificação de APIs e integrações com LLMs
	- [ ] Definição de modelos de dados e fluxos
	- [ ] Validação de viabilidade técnica de todas as funcionalidades core
- [ ] **[TST-VAL-001] [MVP]** Validação Técnica: Protótipo RLS FastAPI/Supabase 🔺 \\ #tecnico \\ #validacao \\ #risco_alto \\ #Semana1-2 \\ #Fase1_Validacao_Tec_Estrategica `@Maestro` `@AgenteM_DevFastAPI`
	- [ ] Configurar tabelas e políticas RLS no Supabase para cenário de teste
	- [ ] Desenvolver endpoints FastAPI mínimos para testar o acesso RLS
	- [ ] Validar a segurança e funcionalidade do RLS
	- [ ] Documentar limitações e requisitos técnicos
- [ ] **[PES-NEG-001] [MVP]** Validação de Negócio: Estimativa Detalhada de Custos Iniciais 🔺 \\ #negocio \\ #pesquisa \\ #Semana3-4 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Estimar custos de APIs de LLMs (Gemini, OpenRouter)
	- [ ] Estimar custos de infraestrutura (Supabase, Vercel, Render)
	- [ ] Calcular custos por usuário e breakeven
	- [ ] Validar viabilidade econômica do modelo freemium
- [ ] **[PES-UXD-001] [MVP]** Validação de UX/Valor: Elaborar Roteiro de Entrevista com Usuários-Alvo 🔺 \\ #ux \\ #pesquisa \\ #validacao \\ #Semana5-6 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_UXDesigner` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Focar na validação dos "AHA! Moments" definidos (Análise Instantânea + Pequenos Ganhos)
	- [ ] Incluir perguntas sobre "Specialized Intelligence" e diferenciação competitiva
	- [ ] Definir objetivos da entrevista focados no "Momento AHA!"
	- [ ] Listar perguntas chave sobre dores de recolocação
	- [ ] Preparar protótipo de baixa fidelidade para validação
	- [ ] Criar roteiro de teste do "Momento AHA!" (Opções B+C)
- [ ] **[TST-UXD-001] [MVP]** Validação de UX/Valor: Conduzir Entrevistas com Usuários-Alvo (5-8 profissionais de TI) 🔺 \\ #ux \\ #pesquisa \\ #validacao \\ #Semana5-6 \\ #Fase1_Validacao_Tec_Estrategica `@Maestro`
	- [ ] Validar "AHA! Moments" com protótipo funcional
	- [ ] Medir tempo para primeiro valor percebido
	- [ ] Avaliar percepção de "Specialized Intelligence"
	- [ ] Agendar e realizar 5-8 entrevistas com profissionais de TI
	- [ ] Validar "Momento AHA!" com protótipo
	- [ ] Gravar (com permissão) e tomar notas detalhadas
	- [ ] Identificar padrões e insights chave
- [ ] **[DOC-UXD-003] [MVP]** Validação de UX/Valor: Criar Mockups/Protótipos Baixa Fidelidade para Validação (Base para ERS Seção 6.3) ⏫ \\ #ux \\ #design \\ #validacao \\ #Semana4-5 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_UXDesigner` `@Maestro`
	- [ ] Protótipos focados em "AHA! Moments"
	- [ ] Validação de "Specialized Intelligence" na UX
	- [ ] Esboçar wireframes das telas principais do MVP
	- [ ] Considerar uso de Stitch/FlutterFlow para protótipo navegável simples
- [ ] **[DOC-REQ-002] [MVP]** Análise Pós-Validação: Consolidar Feedback e Refinar HLD ⏫ \\ #ux \\ #requisitos \\ #validacao \\ #Semana6-7 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Checkpoint de Validação Estratégica conforme metodologia "Intelligent Orchestration"
	- [ ] Refinar métricas de "AHA! Moments" baseadas no feedback
	- [ ] Transcrever/Resumir principais pontos das entrevistas
	- [ ] Atualizar HLD baseado em feedback de usuários
	- [ ] Refinar prioridades do backlog com base no feedback
	- [ ] Validar sequência de desenvolvimento
- [ ] **[DOC-REQ-001] [MVP]** Requisitos: Detalhar HUs e ACs para o MVP (Pós-Validação com Usuários) \\ #requisitos \\ #agile \\ #Semana6-7 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Para cada funcionalidade priorizada do MVP, escrever Histórias de Usuário claras
	- [ ] Para cada HU, definir Critérios de Aceite testáveis
	- [ ] Armazenar em [[docs/02_Requisitos/02_HU_AC/]]


## 🚀 FASE 2: DESENVOLVIMENTO MVP

- [ ] **Fase 2 (Semanas 8-13):** Desenvolvimento MVP com foco em "Specialized Intelligence"
- [ ] **[IMP-DEV-002] [MVP]** Setup Infraestrutura Produção 🔺 \\ #devops \\ #deploy \\ #Semana7-8 \\ #Fase2_MVP_AHA `@Maestro`
	- [ ] Configurar pipeline CI/CD
	- [ ] Deploy backend em ambiente de staging
	- [ ] Configurar monitoramento e logs
	- [ ] Testes de carga básicos
- [ ] **[IMP-DEV-001] [MVP]** Desenvolvimento Backend - Kanban Core 🔺 \\ #desenvolvimento \\ #backend \\ #core \\ #Semana7-9 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Priorizar funcionalidades que suportam "AHA! Moments"
	- [ ] Implementar analytics para medir "Specialized Intelligence"
	- [ ] Implementar autenticação e autorização (RLS)
	- [ ] Desenvolver endpoints para `RF-KAN-001` a `RF-KAN-007`
	- [ ] Integração com APIs de LLMs (Gemini/OpenRouter)
	- [ ] Implementar sistema de análise de currículos
	- [ ] Testes unitários e de integração
- [ ] **[IMP-DEV-003] [MVP]** Desenvolvimento Frontend - Kanban Core 🔺 \\ #desenvolvimento \\ #frontend \\ #core \\ #Semana9-11 \\ #Fase2_MVP_AHA `@AgenteM_DevFlutter` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Implementar UX otimizada para "AHA! Moments"
	- [ ] Dashboard de "Specialized Intelligence" e progresso
	- [ ] Implementar telas de autenticação
	- [ ] Desenvolver interface do Kanban (`RF-KAN-001` a `RF-KAN-007`)
	- [ ] Implementar "Momento AHA!" - Análise Instantânea (Opção B)
	- [ ] Integração com backend via APIs
	- [ ] Testes de interface e usabilidade
- [ ] **[IMP-DEV-002] [MVP]** Desenvolvimento Feature - Contas e Autenticação (Core) \\ #desenvolvimento \\ #feature \\ #core \\ #auth \\ #Semana7-9 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-AUTH-001` a `RF-AUTH-012`
	- [ ] Implementar frontend para `RF-AUTH-001` a `RF-AUTH-0012`
- [ ] **[IMP-DEV-007] [MVP]** Desenvolvimento Feature - Pagamentos (Core) \\ #desenvolvimento \\ #feature \\ #core \\ #pagamento \\ #Semana10-11 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@Maestro`
	- [ ] Configurar Gateway de Pagamento
	- [ ] Implementar Lógica de Assinaturas Freemium (`RF-PAY-SUB-001` a `RF-PAY-SUB-004`)
- [ ] **[IMP-DEV-008] [MVP]** Desenvolvimento Feature - Importação de Vagas (Core) \\ #desenvolvimento \\ #feature \\ #core \\ #ia \\ #importacao \\ #Semana9-10 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-IMP-001`, `RF-IMP-002`
	- [ ] Implementar frontend para `RF-IMP-001`, `RF-IMP-002`
	- [ ] Testar integração com LLM para parsing
- [ ] **[IMP-DEV-009] [MVP]** Desenvolvimento Feature - Otimização CV (Upload e Parsing) \\ #desenvolvimento \\ #feature \\ #core \\ #cv \\ #Semana10-11 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-CV-001`, `RF-CV-002`
	- [ ] Implementar frontend para `RF-CV-001`, `RF-CV-002`
	- [ ] Integrar e testar ferramenta de parsing de PDF
- [ ] **[IMP-DEV-010] [MVP]** Desenvolvimento Feature - Otimização CV (Análise IA) \\ #desenvolvimento \\ #feature \\ #core \\ #ia \\ #cv \\ #Semana11-12 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@Maestro`
	- [ ] Implementar "Specialized Intelligence" para análise de CV
	- [ ] Métricas de precisão e valor percebido
	- [ ] Implementar backend para Análise Vaga-CV (Score IA) (`RF-CV-003`)
	- [ ] Implementar backend para Sugestões de Otimização (`RF-CV-004`)
	- [ ] Implementar backend para Estimativa Salarial (`RF-CV-005`)
- [ ] **[IMP-DEV-011] [MVP]** Desenvolvimento Feature - Coach IA (Core) \\ #desenvolvimento \\ #feature \\ #core \\ #ia \\ #coach \\ #Semana12-13 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Implementar "Specialized Intelligence" no Coach IA
	- [ ] Focar em "AHA! Moments" através de insights personalizados
	- [ ] Implementar backend para Chatbot básico (`RF-COACH-001`)
	- [ ] Implementar lógica de atuação proativa (`RF-COACH-002`, `RF-COACH-003`)
	- [ ] Implementar backend para orientações (`RF-COACH-004`)
	- [ ] Implementar frontend para interação com Coach IA
- [ ] **[IMP-DEV-004] [MVP]** Integração Backend-Frontend 🔺 \\ #desenvolvimento \\ #integracao \\ #Semana11-12 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Testes de integração completa
	- [ ] Validação de fluxos end-to-end
	- [ ] Correção de bugs de integração
	- [ ] Otimização de performance
- [ ] **[IMP-DEV-005] [MVP]** Implementação "AHA! Moments" Completo 🔺 \\ #desenvolvimento \\ #ux \\ #core \\ #Semana12-13 \\ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] **AHA! Moment A:** Análise Instantânea de CV (< 30 segundos)
	- [ ] **AHA! Moment B:** Pequenos Ganhos Acumulativos (gamificação)
	- [ ] **AHA! Moment C:** Insights de "Specialized Intelligence"
	- [ ] Métricas de sucesso: tempo para primeiro valor, taxa de ativação
	- [ ] Análise Instantânea (Opção B) - refinamento
	- [ ] Pequenos Ganhos Acumulativos (Opção C) - implementação inicial
	- [ ] Dashboard de progresso e insights
	- [ ] Sistema de notificações e gamificação básica


## 🔗 FASE 3: REFINAMENTO E VALIDAÇÃO

- [ ] **Fase 3 (Semanas 14-15):** Refinamento e Validação Final
- [ ] **[DOC-ARQ-002] [MVP]** Arquitetura: Detalhamento LLDs para Módulos do MVP (Pós-Validação dos Passos Críticos) \\ #arquitetura \\ #documentacao \\ #Semana4-5 \\ #Fase1_Validacao_Tec_Estrategica `@AgenteM_ArquitetoTI` `@Maestro`
	- [ ] Para `LLD_Modulo_Auth.md`: detalhar modelos de dados, classes, fluxos de autenticação
	- [ ] Para `LLD_Modulo_Kanban.md`: detalhar estruturas de dados, lógica de manipulação de cards/colunas
	- [ ] Para `LLD_Modulo_CV.md`: detalhar processos de upload, parsing e armazenamento de CVs
	- [ ] Para `LLD_Modulo_Coach.md`: detalhar interações do chatbot, lógica de proatividade
	- [ ] Para `LLD_Modulo_Pagamentos.md`: detalhar integração com gateway, gerenciamento de assinaturas
- [ ] **[IMP-DEV-006] [MVP]** Features de Retenção e Engajamento ⏫ \\ #desenvolvimento \\ #retencao \\ #Semana13-14 \\ #Fase3_Refinamento_Validacao `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Sistema de metas baseado em "Specialized Intelligence"
	- [ ] Recomendações personalizadas usando IA especializada
	- [ ] Sistema de metas e objetivos
	- [ ] Histórico de progresso
	- [ ] Recomendações personalizadas
	- [ ] Exportação de relatórios
- [ ] **[TST-INT-001] [MVP]** Testes Integrados e Validação Completa 🔺 \\ #testes \\ #validacao \\ #qualidade \\ #Semana14-15 \\ #Fase3_Refinamento_Validacao `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Validação dos "AHA! Moments" em ambiente real
	- [ ] Testes de "Specialized Intelligence" e diferenciação
	- [ ] Checkpoint de Validação Estratégica final
	- [ ] Testes de aceitação com usuários beta
	- [ ] Validação do "Momento AHA!" em ambiente real
	- [ ] Testes de segurança e performance
	- [ ] Correção de bugs críticos
- [ ] **[DOC-USR-001] [MVP]** Documentação de Usuário e Onboarding ⏫ \\ #documentacao \\ #ux \\ #Semana15 \\ #Fase3_Refinamento_Validacao `@AgenteM_UXDesigner` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Onboarding otimizado para "AHA! Moments"
	- [ ] Tutoriais focados em "Specialized Intelligence"
	- [ ] Criar guia de primeiros passos
	- [ ] Desenvolver tutoriais interativos
	- [ ] Documentar funcionalidades principais
	- [ ] Preparar materiais de suporte


## 🎯 FASE 4: LANÇAMENTO E MONITORAMENTO

- [ ] **Fase 4 (Semana 16):** Lançamento MVP
- [ ] **[LAN-MVP-001] [MVP]** Lançamento MVP e Estratégia Go-to-Market 🔺 \\ #lancamento \\ #marketing \\ #mvp \\ #Semana16 \\ #Fase4_Lancamento `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Lançamento focado em "Specialized Intelligence" como diferencial
	- [ ] Métricas de "AHA! Moments" no go-to-market
	- [ ] Deploy em produção
	- [ ] Configurar analytics e métricas
	- [ ] Lançamento para grupo beta expandido
	- [ ] Coleta de feedback inicial
	- [ ] Preparação para iterações pós-MVP
- [ ] **[MON-MVP-001] [MVP]** Monitoramento e Métricas Iniciais ⏫ \\ #monitoramento \\ #metricas \\ #Semana16 \\ #Fase4_Lancamento `@Maestro`
	- [ ] Dashboard de "AHA! Moments" e conversão
	- [ ] Métricas de "Specialized Intelligence" e diferenciação
	- [ ] KPIs de vantagens competitivas sustentáveis
	- [ ] Configurar dashboards de métricas
	- [ ] Monitorar "Momento AHA!" e conversão
	- [ ] Acompanhar retenção e engajamento
	- [ ] Planejar próximas iterações baseadas em dados


## 📋 BACKLOG (Não Priorizado)

- [ ] **Tarefas futuras e melhorias pós-MVP**
- [ ] **Features avançadas para versões futuras**
- [ ] **Otimizações e refinamentos contínuos**

---

### 📋 **CONFIGURAÇÕES DO KANBAN**

%% kanban:settings
```
{"kanban-plugin":"board","lane-width":400,"list-collapse":[null,null,null,null,null,false]}
```
%%