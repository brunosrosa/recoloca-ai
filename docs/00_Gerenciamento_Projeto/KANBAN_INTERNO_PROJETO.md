---

kanban-plugin: board
sticker: lucide//align-start-horizontal

---

## 🧊 Backlog Geral (Não Priorizado)

- [ ] **[PES-INF-001]** Pesquisa de Opções de Hospedagem ⏫ \ #pesquisa \ #infraestrutura \ #hospedagem \ #Fase1 #Validacao_Tec_Estrategica `@Maestro` `@AgenteM_ArquitetoTI`
	- [ ] Analisar e comparar opções de hospedagem para Frontend (Vercel, Netlify, Firebase Hosting, GitHub Pages)
	- [ ] Analisar e comparar opções de hospedagem para Backend (Render, Heroku, AWS Lightsail, Google Cloud Run)
	- [ ] Analisar e comparar opções de hospedagem para Supabase (auto-hospedado vs. nuvem)
	- [ ] Considerar custos, escalabilidade, facilidade de deploy e integração com CI/CD para cada opção
	- [ ] Documentar a análise comparativa e a recomendação.
- [ ] **[EST-AGT-001]** Discussão sobre Unificação/Colaboração de Agentes na Documentação 🔼 \ #estrategia \ #agentes \ #documentacao \ #Fase1_Validacao_Tec_Estrategica `@Maestro` `@AgenteOrquestrador`
	- [ ] Avaliar a viabilidade e implicações de unificar o `@AgenteOrquestrador` com o `@AgenteM_Documentacao` (se este for criado/mantido)
	- [ ] Discutir como outros agentes podem/devem contribuir para a atualização da "Documentação Viva"
	- [ ] Definir responsabilidades e fluxos para manter a consistência contextual da documentação.
- [ ] **[PES-EST-001]** Execução da Análise Competitiva Aprofundada (Gemini Pro) ⏫ \ #pesquisa \ #estrategia \ #competitivo \ #Fase1 #Validacao_Tec_Estrategica `@Maestro`
	- [ ] Executar o prompt [[docs/05_Prompts/02_Prompts_Especificos/PROMPT_DEEP_RESEARCH_ANALISE_COMPETITIVA.md]] com Gemini Pro
	- [ ] Analisar concorrentes diretos, indiretos e substitutos no mercado brasileiro
	- [ ] Mapear gaps de mercado e oportunidades de diferenciação
	- [ ] Documentar insights estratégicos para posicionamento
- [ ] **[PES-VAL-001] [MVP]** Implementação do Plano de Validação de Premissas de Negócio ⏫ \ #pesquisa \ #validacao \ #negocio \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [ ] Executar Fase 1 (Pré-desenvolvimento) conforme [[docs/01_Guias_Centrais/PLANO_VALIDACAO_PREMISSAS_NEGOCIO.md]]
	- [ ] Conduzir entrevistas com 5-8 profissionais de TI sobre dores de recolocação
	- [ ] Validar disposição para pagar por solução de recolocação
	- [ ] Testar conceito inicial e proposta de valor
	- [ ] Documentar resultados e ajustar estratégia conforme necessário
- [ ] **[EST-GTM-001] [MVP]** Implementação da Estratégia Go-to-Market ⏫ \ #estrategia \ #marketing \ #gtm \ #Fase1_Validacao_Tec_Estrategica `@Maestro`
	- [ ] Executar ações de pré-lançamento conforme [[docs/08_Marketing_e_Vendas/ESTRATEGIA_GO_TO_MARKET.md]]
	- [ ] Criar perfis detalhados das personas (Dev Pleno/Sênior, Tech Lead, etc.)
	- [ ] Desenvolver conteúdo inicial para LinkedIn e comunidades de desenvolvedores
	- [ ] Configurar ferramentas de marketing (Google Analytics, LinkedIn Analytics)
	- [ ] Preparar estratégia de pricing e modelo freemium
- [ ] **[MET-IMP-001] [MVP]** Implementação do Sistema de Métricas e KPIs ⏫ \ #metricas \ #analytics \ #kpi \ #Fase1_Validacao_Tec_Estrategica `@Maestro` `@AgenteM_Performance`
	- [ ] Implementar tracking conforme [[docs/07_Metricas_e_Analytics/METRICAS_SUCESSO_BASE_MERCADO.md]]
	- [ ] Configurar dashboard de métricas (aquisição, ativação, retenção, monetização)
	- [ ] Estabelecer baselines e metas por fase de crescimento
	- [ ] Implementar alertas e thresholds para métricas críticas
	- [ ] Configurar processo de revisão semanal/mensal de métricas
- [ ] **[EST-MOA-001] [MVP]** Construção Sistemática de Vantagens Competitivas (Moats) ⏫ \ #estrategia \ #moats \ #vantagem_competitiva \ #Fase1_Validacao_Tec_Estrategica `@Maestro` `@AgenteOrquestrador`
	- [ ] Implementar estratégias para construção dos 5 tipos de moats identificados
	- [ ] Fase 1: Focar em Inteligência Especializada + Brand & Trust
	- [ ] Implementar coleta de dados proprietários (Data Moats)
	- [ ] Desenvolver funcionalidades que aumentem Switching Costs
	- [ ] Preparar infraestrutura para Network Effects futuros
	- [ ] Monitorar métricas de moats mensalmente
	- [ ] Executar estratégias de defesa competitiva conforme [[docs/01_Guias_Centrais/VANTAGENS_COMPETITIVAS_SUSTENTAVEIS.md]]
- [ ] **[DOC-UXD-002] [MVP]** Design: Criação do Style Guide Detalhado (`STYLE_GUIDE.md`) \ #ux \ #ui \ #documentacao \ #Fase1 `@AgenteM_UIDesigner` `@Maestro`
	- [ ] Definir e documentar paleta de cores, tipografia, iconografia.
	- [ ] Criar diretrizes de espaçamento, grids e layout.
	- [ ] Especificar componentes de UI reutilizáveis e seus estados.
	- [ ] Adicionar seções de tom de voz e UX Writing.


## 🎯 A Fazer (Priorizado)

- [ ] **[IMP-RAG-003] [MVP]** Operacionalização Completa do Sistema RAG - Criação e Indexação 🔺 \ #tecnico \ #rag \ #critico \ #Semana1 \ #Fase0_RAG_Agentes `@AgenteOrquestrador` `@Maestro`
	- [ ] Setup ambiente Conda (`Agents_RAG_Env`)
	- [ ] Implementação `rag_indexer.py` funcional
	- [ ] Indexação de todos os documentos core
	- [ ] Testes de retrieval com queries reais
- [ ] **[CFG-AGT-001] [MVP]** Configuração dos 5 Agentes Essenciais Tier 1 🔺 \ #agentes \ #configuracao \ #critico \ #Semana1 \ #Fase0_RAG_Agentes `@AgenteOrquestrador` `@Maestro`
	- [ ] @AgenteOrquestrador v2.0 (PM + PO + Engenheiro Prompt)
	- [ ] @AgenteM_ArquitetoTI (HLD + LLD unificado)
	- [ ] @AgenteM_UXDesigner
	- [ ] @AgenteM_DevFastAPI
	- [ ] @AgenteM_DevFlutter
- [ ] **[CFG-INF-001] [MVP]** Ambiente Dev/Deploy - Configuração Inicial 🔺 \ #devops \ #infra \ #Semana1 \ #Fase0_RAG_Agentes `@Maestro`
	- [ ] Criar repositórios Git para frontend, backend
	- [ ] Configurar linters, formatters e hooks de pré-commit
	- [ ] Setup inicial Vercel/Render para deploy
- [ ] **[DOC-ARQ-001] [MVP]** HLD Detalhado - PRIORIDADE ANTECIPADA 🔺 \ #arquitetura \ #hld \ #critico \ #Semana2 \ #Fase1_Validacao_Tec_Estrategica `@AgenteM_ArquitetoTI` `@AgenteOrquestrador` `@Maestro`
	- [ ] Detalhamento completo da arquitetura de segurança (RLS)
	- [ ] Especificação de APIs e integrações com LLMs
	- [ ] Definição de modelos de dados e fluxos
	- [ ] Validação de viabilidade técnica de todas as funcionalidades core
- [ ] **[TST-VAL-001] [MVP]** Validação Técnica: Protótipo RLS FastAPI/Supabase 🔺 \ #tecnico \ #validacao \ #risco_alto \ #Semana2 \ #Fase1_Validacao_Tec_Estrategica `@Maestro` `@AgenteM_DevFastAPI`
	- [ ] Configurar tabelas e políticas RLS no Supabase para cenário de teste
	- [ ] Desenvolver endpoints FastAPI mínimos para testar o acesso RLS
	- [ ] Validar a segurança e funcionalidade do RLS
	- [ ] Documentar limitações e requisitos técnicos
- [ ] **[PES-NEG-001] [MVP]** Validação de Negócio: Estimativa Detalhada de Custos Iniciais 🔺 \ #negocio \ #pesquisa \ #Semana2 \ #Fase1_Validacao_Tec_Estrategica `@AgenteOrquestrador` `@Maestro`
	- [ ] Estimar custos de APIs de LLMs (Gemini, OpenRouter)
	- [ ] Estimar custos de infraestrutura (Supabase, Vercel, Render)
	- [ ] Calcular custos por usuário e breakeven
	- [ ] Validar viabilidade econômica do modelo freemium
- [ ] **[PES-UXD-001] [MVP]** Validação de UX/Valor: Elaborar Roteiro de Entrevista com Usuários-Alvo 🔺 \ #ux \ #pesquisa \ #validacao \ #Semana3 \ #Fase1_Validacao_Tec_Estrategica `@AgenteM_UXDesigner` `@AgenteOrquestrador` `@Maestro`
	- [ ] Definir objetivos da entrevista focados no "Momento AHA!"
	- [ ] Listar perguntas chave sobre dores de recolocação
	- [ ] Preparar protótipo de baixa fidelidade para validação
	- [ ] Criar roteiro de teste do "Momento AHA!" (Opções B+C)
- [ ] **[TST-UXD-001] [MVP]** Validação de UX/Valor: Conduzir Entrevistas com Usuários-Alvo (5-8 profissionais de TI) 🔺 \ #ux \ #pesquisa \ #validacao \ #Semana3 \ #Fase1_Validacao_Tec_Estrategica `@Maestro`
	- [ ] Agendar e realizar 5-8 entrevistas com profissionais de TI
	- [ ] Validar "Momento AHA!" com protótipo
	- [ ] Gravar (com permissão) e tomar notas detalhadas
	- [ ] Identificar padrões e insights chave
- [ ] **[DOC-REQ-002] [MVP]** Análise Pós-Validação: Consolidar Feedback e Refinar HLD ⏫ \ #ux \ #requisitos \ #validacao \ #Semana3 \ #Fase1_Validacao_Tec_Estrategica `@AgenteOrquestrador` `@Maestro`
	- [ ] Transcrever/Resumir principais pontos das entrevistas
	- [ ] Atualizar HLD baseado em feedback de usuários
	- [ ] Refinar prioridades do backlog com base no feedback
	- [ ] Validar sequência de desenvolvimento
- [ ] **[IMP-DEV-001] [MVP]** Desenvolvimento Backend - Kanban Core 🔺 \ #desenvolvimento \ #backend \ #core \ #Semana4 \ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteOrquestrador` `@Maestro`
	- [ ] Implementar autenticação e autorização (RLS)
	- [ ] Desenvolver endpoints para `RF-KAN-001` a `RF-KAN-007`
	- [ ] Integração com APIs de LLMs (Gemini/OpenRouter)
	- [ ] Implementar sistema de análise de currículos
	- [ ] Testes unitários e de integração
- [ ] **[IMP-DEV-002] [MVP]** Setup Infraestrutura Produção 🔺 \ #devops \ #deploy \ #Semana4 \ #Fase2_MVP_AHA `@Maestro`
	- [ ] Configurar pipeline CI/CD
	- [ ] Deploy backend em ambiente de staging
	- [ ] Configurar monitoramento e logs
	- [ ] Testes de carga básicos
- [ ] **[IMP-DEV-003] [MVP]** Desenvolvimento Frontend - Kanban Core 🔺 \ #desenvolvimento \ #frontend \ #core \ #Semana5 \ #Fase2_MVP_AHA `@AgenteM_DevFlutter` `@AgenteOrquestrador` `@Maestro`
	- [ ] Implementar telas de autenticação
	- [ ] Desenvolver interface do Kanban (`RF-KAN-001` a `RF-KAN-007`)
	- [ ] Implementar "Momento AHA!" - Análise Instantânea (Opção B)
	- [ ] Integração com backend via APIs
	- [ ] Testes de interface e usabilidade
- [ ] **[IMP-DEV-004] [MVP]** Integração Backend-Frontend 🔺 \ #desenvolvimento \ #integracao \ #Semana5 \ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Testes de integração completa
	- [ ] Validação de fluxos end-to-end
	- [ ] Correção de bugs de integração
	- [ ] Otimização de performance
- [ ] **[IMP-DEV-005] [MVP]** Implementação "Momento AHA!" Completo 🔺 \ #desenvolvimento \ #ux \ #core \ #Semana6 \ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@AgenteOrquestrador` `@Maestro`
	- [ ] Análise Instantânea (Opção B) - refinamento
	- [ ] Pequenos Ganhos Acumulativos (Opção C) - implementação inicial
	- [ ] Dashboard de progresso e insights
	- [ ] Sistema de notificações e gamificação básica
- [ ] **[IMP-DEV-006] [MVP]** Features de Retenção e Engajamento ⏫ \ #desenvolvimento \ #retencao \ #Semana6 \ #Fase3_Refinamento_Validacao `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Sistema de metas e objetivos
	- [ ] Histórico de progresso
	- [ ] Recomendações personalizadas
	- [ ] Exportação de relatórios
- [ ] **[TST-INT-001] [MVP]** Testes Integrados e Validação Completa 🔺 \ #testes \ #validacao \ #qualidade \ #Semana7 \ #Fase3_Refinamento_Validacao `@AgenteOrquestrador` `@Maestro`
	- [ ] Testes de aceitação com usuários beta
	- [ ] Validação do "Momento AHA!" em ambiente real
	- [ ] Testes de segurança e performance
	- [ ] Correção de bugs críticos
- [ ] **[DOC-USR-001] [MVP]** Documentação de Usuário e Onboarding ⏫ \ #documentacao \ #ux \ #Semana7 \ #Fase3_Refinamento_Validacao `@AgenteM_UXDesigner` `@AgenteOrquestrador` `@Maestro`
	- [ ] Criar guia de primeiros passos
	- [ ] Desenvolver tutoriais interativos
	- [ ] Documentar funcionalidades principais
	- [ ] Preparar materiais de suporte
- [ ] **[LAN-MVP-001] [MVP]** Lançamento MVP e Estratégia Go-to-Market 🔺 \ #lancamento \ #marketing \ #mvp \ #Semana8 \ #Fase3_Refinamento_Validacao `@AgenteOrquestrador` `@Maestro`
	- [ ] Deploy em produção
	- [ ] Configurar analytics e métricas
	- [ ] Lançamento para grupo beta expandido
	- [ ] Coleta de feedback inicial
	- [ ] Preparação para iterações pós-MVP
- [ ] **[MON-MVP-001] [MVP]** Monitoramento e Métricas Iniciais ⏫ \ #monitoramento \ #metricas \ #Semana8 \ #Fase3_Refinamento_Validacao `@Maestro`
	- [ ] Configurar dashboards de métricas
	- [ ] Monitorar "Momento AHA!" e conversão
	- [ ] Acompanhar retenção e engajamento
	- [ ] Planejar próximas iterações baseadas em dados
- [ ] **[IMP-DEV-002] [MVP]** Desenvolvimento Feature - Contas e Autenticação (Core) \ #desenvolvimento \ #feature \ #core \ #auth \ #Fase1 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-AUTH-001` a `RF-AUTH-012`.
	- [ ] Implementar frontend para `RF-AUTH-001` a `RF-AUTH-0012`.
- [ ] **[DOC-ARQ-001] [MVP]** Arquitetura: Detalhamento LLDs para Módulos do MVP (Pós-Validação dos Passos Críticos) \ #arquitetura \ #documentacao \ #Fase1 `@AgenteMentorArquitetoLLD` `@Maestro`
	- [ ] Para `LLD_Modulo_Auth.md`: detalhar modelos de dados, classes, fluxos de autenticação.
	- [ ] Para `LLD_Modulo_Kanban.md`: detalhar estruturas de dados, lógica de manipulação de cards/colunas.
	- [ ] Para `LLD_Modulo_CV.md`: detalhar processos de upload, parsing e armazenamento de CVs.
	- [ ] Para `LLD_Modulo_Coach.md`: detalhar interações do chatbot, lógica de proatividade.
	- [ ] Para `LLD_Modulo_Pagamentos.md`: detalhar integração com gateway, gerenciamento de assinaturas.
- [ ] **[DOC-REQ-001] [MVP]** Requisitos: Detalhar HUs e ACs para o MVP (Pós-Validação com Usuários) \ #requisitos \ #agile \ #Fase1 `@AgenteOrquestrador` `@Maestro`
	- [ ] Para cada funcionalidade priorizada do MVP, escrever Histórias de Usuário claras.
	- [ ] Para cada HU, definir Critérios de Aceite testáveis.
	- [ ] Armazenar em [[docs/02_Requisitos/HU_AC/]].
- [ ] **[IMP-DEV-003] [MVP]** Desenvolvimento Feature - Pagamentos (Core) \ #desenvolvimento \ #feature \ #core \ #pagamento \ #Fase2 `@AgenteMentorDevFastAPI` `@Maestro`
	- [ ] Configurar Gateway de Pagamento.
	- [ ] Implementar Lógica de Assinaturas Freemium (`RF-PAY-SUB-001` a `RF-PAY-SUB-004`).
- [ ] **[IMP-DEV-004] [MVP]** Desenvolvimento Feature - Importação de Vagas (Core) \ #desenvolvimento \ #feature \ #core \ #ia \ #importacao \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-IMP-001`, `RF-IMP-002`.
	- [ ] Implementar frontend para `RF-IMP-001`, `RF-IMP-002`.
	- [ ] Testar integração com LLM para parsing.
- [ ] **[IMP-DEV-005] [MVP]** Desenvolvimento Feature - Otimização CV (Upload e Parsing) \ #desenvolvimento \ #feature \ #core \ #cv \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-CV-001`, `RF-CV-002`.
	- [ ] Implementar frontend para `RF-CV-001`, `RF-CV-002`.
	- [ ] Integrar e testar ferramenta de parsing de PDF.
- [ ] **[IMP-DEV-006] [MVP]** Desenvolvimento Feature - Otimização CV (Análise IA) \ #desenvolvimento \ #feature \ #core \ #ia \ #cv \ #Fase2 `@AgenteMentorDevFastAPI` `@Maestro`
	- [ ] Implementar backend para Análise Vaga-CV (Score IA) (`RF-CV-003`).
	- [ ] Implementar backend para Sugestões de Otimização (`RF-CV-004`).
	- [ ] Implementar backend para Estimativa Salarial (`RF-CV-005`).
- [ ] **[IMP-DEV-007] [MVP]** Desenvolvimento Feature - Coach IA (Core) \ #desenvolvimento \ #feature \ #core \ #ia \ #coach \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para Chatbot básico (`RF-COACH-001`).
	- [ ] Implementar lógica de atuação proativa (`RF-COACH-002`, `RF-COACH-003`).
	- [ ] Implementar backend para orientações (`RF-COACH-004`).
	- [ ] Implementar frontend para interação com Coach IA.
- [ ] **[PES-UXD-001] [MVP]** Validação de UX/Valor: Elaborar Roteiro de Entrevista com Usuários-Alvo & Realizar a Pesquisa (Base para ERS Seção 6.3) ⏫ \ #ux \ #pesquisa \ #validacao \ #Fase1 `@AgenteOrquestrador` `@Maestro`
	- [ ] Definir objetivos da entrevista.
	- [ ] Listar perguntas chave abertas e fechadas.
	- [ ] Preparar material de apoio (se houver mockups iniciais).
- [ ] **[TST-UXD-001] [MVP]** Validação de UX/Valor: Conduzir Entrevistas com Usuários-Alvo (3-5 profissionais de TI - ERS Seção 6.3) ⏫ \ #ux \ #pesquisa \ #validacao \ #Fase1 `@Maestro`
	- [ ] Agendar e realizar as entrevistas.
	- [ ] Gravar (com permissão) e tomar notas detalhadas.
- [ ] **[DOC-UXD-001] [MVP]** Validação de UX/Valor: Criar Mockups/Protótipos Baixa Fidelidade para Validação (Base para ERS Seção 6.3) ⏫ \ #ux \ #design \ #validacao \ #Fase1 `@AgenteM_UIDesigner` `@Maestro`
	- [ ] Esboçar wireframes das telas principais do MVP.
	- [ ] Considerar uso de Stitch/FlutterFlow para protótipo navegável simples.


## 🚀 Em Progresso

- [ ] **[DOC-REV-001] [MVP]** Revisão Interativa dos Documentos Core (v1.0) 🔺 \ #documentacao \ #core \ #critico \ #Fase0_RAG_Agentes `@AgenteOrquestrador` `@Maestro`
	- [x] Revisar e aprovar [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] para v1.0 (Estratégico) ✅ 2025-06-11
	- [x] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/TAP.md]] para v1.0 (Termo de Abertura do Projeto) ✅ 2025-06-13
	- [x] Revisar e aprovar [[docs/02_Requisitos/ERS.md]] para v1.0 (Requisitos) ✅ 2025-06-13
	- [x] Revisar e aprovar [[docs/03_Arquitetura_e_Design/HLD.md]] para v1.0 (Arquitetura de Alto Nível) ✅ 2025-06-13
	- [ ] Revisar e aprovar [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] para v1.0 (Metodologia e Engenharia de Prompt)
	- [ ] Revisar e aprovar [[docs/03_Arquitetura_e_Design/FLUXO_TRABALHO_GERAL.md]] para v1.0 (Processos)
	- [ ] Revisar e aprovar [[docs/03_Arquitetura_e_Design/STYLE_GUIDE.md]] para v1.0 (Design)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/ROADMAP_TEMPORAL_RECOLOCA_AI.md]] para v1.0 (Planejamento Temporal)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/CAMINHO_CRITICO_MVP.md]] para v1.0 (Planejamento MVP)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]] para v1.0 (Gerenciamento de Tarefas)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/Maestro_Tasks.md]] para v1.0 (Tarefas do Maestro)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PCom.md]] para v1.0 (Plano de Comunicações)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PGC.md]] para v1.0 (Plano de Gerenciamento de Custos)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PGE.md]] para v1.0 (Plano de Gerenciamento de Escopo)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PGP.md]] para v1.0 (Plano de Gerenciamento de Prazos)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PGQ.md]] para v1.0 (Plano de Gerenciamento da Qualidade)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PGR.md]] para v1.0 (Plano de Gerenciamento de Riscos)
	- [ ] Revisar e aprovar [[docs/00_Gerenciamento_Projeto/PStakeholders.md]] para v1.0 (Plano de Gerenciamento das Partes Interessadas)


## 🔍 Em Revisão



## ✅ Concluído





%% kanban:settings
```
{"kanban-plugin":"board","lane-width":350}
```
%%