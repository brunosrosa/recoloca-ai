---

kanban-plugin: board
sticker: lucide//align-start-horizontal

---

## 🧊 BACKLOG (Não Priorizado)

- [ ] **[MET-AHA-001]** Implementação de Métricas Específicas para "Momentos AHA!" ⏫ \ #metricas \ #aha_moments \ #analytics \ #Backlog `@Maestro` `@AgenteM_Performance`
	- [ ] Definir métricas específicas para medir a eficácia dos "Momentos AHA!"
	- [ ] Implementar tracking de tempo até primeiro valor percebido
	- [ ] Criar dashboards para monitoramento em tempo real
	- [ ] Estabelecer benchmarks e metas de performance
	- **Dependências:** MVP funcional
	- **Definition of Done:** Sistema de métricas AHA! operacional
- [ ] **[MET-PER-001]** Sistema de Monitoramento de Performance e Alertas ⏫ \ #performance \ #monitoramento \ #alertas \ #Backlog `@Maestro` `@AgenteM_Performance`
	- [ ] Configurar monitoramento de performance de APIs e frontend
	- [ ] Implementar alertas para degradação de performance
	- [ ] Criar dashboards de saúde do sistema
	- [ ] Implementar notificações automáticas para desvios críticos
	- [ ] Criar sistema de relatórios automatizados para stakeholders
- [ ] **[PES-INF-001]** Pesquisa de Opções de Hospedagem ⏫ \ #pesquisa \ #infraestrutura \ #hospedagem \ #Backlog `@Maestro` `@AgenteM_ArquitetoTI`
	- [ ] Analisar e comparar opções de hospedagem para Frontend (Vercel, Netlify, Firebase Hosting, GitHub Pages)
	- [ ] Analisar e comparar opções de hospedagem para Backend (Render, Railway, Fly.io, DigitalOcean App Platform)
	- [ ] Considerar custos, performance, facilidade de deploy e escalabilidade
	- [ ] Documentar recomendações com justificativas técnicas e financeiras
	- **Dependências:** Nenhuma
	- **Definition of Done:** Relatório de hospedagem com recomendações
- [ ] **[VAL-NEG-001]** Validação de Premissas de Negócio ⏫ \ #validacao \ #negocio \ #estrategia \ #Backlog `@Maestro`
	- [ ] Validar hipóteses sobre dor do usuário e proposta de valor
	- [ ] Testar conceito inicial e proposta de valor
	- [ ] Documentar resultados e ajustar estratégia conforme necessário
- [ ] **[EST-GTM-001]** Implementação da Estratégia Go-to-Market ⏫ \ #estrategia \ #marketing \ #gtm \ #Backlog `@Maestro`
	- [ ] Executar ações de pré-lançamento conforme [[docs/08_Marketing_e_Vendas/01_ESTRATEGIA_GO_TO_MARKET.md]]
	- [ ] Implementar canais de aquisição prioritários
	- [ ] Executar estratégia de pricing e monetização
	- [ ] Estabelecer parcerias estratégicas (RH, consultorias, etc.)
	- **Dependências:** MVP validado
	- **Definition of Done:** Estratégia GTM em execução
- [ ] **[EST-MOA-001]** Implementação de Moats Competitivos ⏫ \ #estrategia \ #competitivo \ #moats \ #Backlog `@Maestro`
	- [ ] Implementar vantagens competitivas sustentáveis
	- [ ] Monitorar métricas de moats mensalmente
	- [ ] Executar estratégias de defesa competitiva conforme [[docs/01_Guias_Centrais/03_VANTAGENS_COMPETITIVAS_SUSTENTAVEIS.md]]
- [ ] **[DOC-UXD-004]** Design: Criação do Style Guide Detalhado (`STYLE_GUIDE.md`) 🔼 \ #ux \ #ui \ #documentacao \ #Backlog `@AgenteM_UXDesigner` `@Maestro`
	- [ ] Incluir elementos visuais que reforcem "Specialized Intelligence"
	- [ ] Definir paleta de cores, tipografia e iconografia
	- [ ] Criar componentes de UI reutilizáveis
	- [ ] Documentar padrões de interação e micro-animações
	- **Dependências:** Wireframes aprovados
	- **Definition of Done:** Style Guide completo e aprovado
- [ ] **[CFG-ANA-001]** Setup Analytics e Métricas de Produto 🔻 \ #analytics \ #metricas \ #produto \ #BacklogEstrategico `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Configurar Google Analytics 4 ou Mixpanel
	- [ ] Definir eventos de conversão e funis
	- [ ] Implementar tracking de "AHA! Moments"
	- [ ] Dashboard de métricas de produto
	- **Dependências:** MVP funcional
	- **Definition of Done:** Sistema de analytics operacional
- [ ] **[PES-COM-001]** Análise Competitiva Detalhada 🔻 \ #pesquisa \ #competitivo \ #estrategia \ #BacklogEstrategico `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Mapear funcionalidades dos principais concorrentes
	- [ ] Identificar gaps e oportunidades de diferenciação
	- [ ] Análise de pricing e modelos de negócio
	- [ ] Benchmarking de UX e "AHA! Moments"
	- **Dependências:** Nenhuma
	- **Definition of Done:** Relatório competitivo completo
- [ ] **[GTM-EST-001]** Estratégia de Go-to-Market 🔻 \ #gtm \ #estrategia \ #crescimento \ #BacklogEstrategico `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Definir canais de aquisição prioritários
	- [ ] Estratégia de pricing e monetização
	- [ ] Plano de lançamento e comunicação
	- [ ] Parcerias estratégicas (RH, consultorias, etc.)
	- **Dependências:** MVP validado
	- **Definition of Done:** Plano de GTM executável
- [ ] **[DES-SYS-001]** Design System e Componentes 🔻 \ #design \ #ux \ #sistema \ #BacklogEstrategico `@AgenteM_UXDesigner` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Criar design system consistente
	- [ ] Biblioteca de componentes reutilizáveis
	- [ ] Guia de estilo e identidade visual
	- [ ] Documentação de padrões de UX
	- **Dependências:** MVP funcional
	- **Definition of Done:** Design system documentado e implementado


## 🚀 FASE 2: DESENVOLVIMENTO MVP

- [ ] **[CFG-INF-001]** Ambiente Dev/Deploy - Configuração Inicial 🔺 \ #devops \ #infra \ #Fase2_MVP_AHA `@Maestro`
	- [ ] Criar repositórios Git para frontend, backend
	- [ ] Configurar linters, formatters e hooks de pré-commit
	- [ ] Setup inicial Vercel/Render para deploy
	- **Dependências:** Fase 1 100% concluída
	- **Definition of Done:** Ambiente de desenvolvimento operacional
- [ ] **[IMP-DEV-001]** Desenvolvimento Backend - Kanban Core 🔺 \ #desenvolvimento \ #backend \ #core \ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Priorizar funcionalidades que suportam "AHA! Moments"
	- [ ] Implementar analytics para medir "Specialized Intelligence"
	- [ ] Implementar autenticação e autorização (RLS)
	- [ ] Desenvolver endpoints para RF-KAN-001 a RF-KAN-007
	- [ ] Integração com APIs de LLMs (Gemini/OpenRouter)
	- [ ] Implementar sistema de análise de currículos
	- [ ] Testes unitários e de integração
	- **Dependências:** [CFG-INF-001] concluído
	- **Definition of Done:** Backend core funcional com testes
- [ ] **[IMP-DEV-003]** Desenvolvimento Frontend - Kanban Core 🔺 \ #desenvolvimento \ #frontend \ #core \ #Fase2_MVP_AHA `@AgenteM_DevFlutter` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Implementar UX otimizada para "AHA! Moments"
	- [ ] Dashboard de "Specialized Intelligence" e progresso
	- [ ] Implementar telas de autenticação
	- [ ] Desenvolver interface do Kanban (RF-KAN-001 a RF-KAN-007)
	- [ ] Implementar "Momento AHA!" - Análise Instantânea (Opção B)
	- [ ] Integração com backend via APIs
	- [ ] Testes de interface e usabilidade
	- **Dependências:** [IMP-DEV-001] 70% concluído
	- **Definition of Done:** Frontend core funcional e testado
- [ ] **[IMP-DEV-004]** Integração Backend-Frontend 🔺 \ #desenvolvimento \ #integracao \ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@Maestro`
	- [ ] Testes de integração completa
	- [ ] Validação de fluxos end-to-end
	- [ ] Correção de bugs de integração
	- [ ] Otimização de performance
	- **Dependências:** [IMP-DEV-001] e [IMP-DEV-003] concluídos
	- **Definition of Done:** Sistema integrado e funcional
- [ ] **[IMP-DEV-005]** Implementação "AHA! Moments" Completo 🔺 \ #desenvolvimento \ #ux \ #core \ #Fase2_MVP_AHA `@AgenteM_DevFastAPI` `@AgenteM_DevFlutter` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] **AHA! Moment A:** Análise Instantânea de CV (< 30 segundos)
	- [ ] **AHA! Moment B:** Pequenos Ganhos Acumulativos (gamificação)
	- [ ] **AHA! Moment C:** Insights de "Specialized Intelligence"
	- [ ] Métricas de sucesso: tempo para primeiro valor, taxa de ativação
	- [ ] Dashboard de progresso e insights
	- [ ] Sistema de notificações e gamificação básica
	- **Dependências:** [IMP-DEV-004] concluído
	- **Definition of Done:** AHA! Moments implementados e medidos
- [ ] **[TST-INT-001]** Testes Integrados e Validação Completa 🔺 \ #testes \ #validacao \ #qualidade \ #Fase3_Refinamento_Validacao `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Validação dos "AHA! Moments" em ambiente real
	- [ ] Testes de "Specialized Intelligence" e diferenciação
	- [ ] Checkpoint de Validação Estratégica final
	- [ ] Testes de aceitação com usuários beta
	- [ ] Testes de segurança e performance
	- [ ] Correção de bugs críticos
	- **Dependências:** Fase 2 100% concluída
	- **Definition of Done:** Sistema validado e pronto para lançamento


## 🔄 FASE 1: VALIDAÇÃO TÉCNICA E ESTRATÉGICA

- [ ] **[TST-VAL-001]** Validação Técnica: Protótipo RLS FastAPI/Supabase 🔺 \ #tecnico \ #validacao \ #risco_alto \ #Fase1_Validacao_Tec_Estrategica `@Maestro` `@AgenteM_DevFastAPI`
	- [ ] Configurar tabelas e políticas RLS no Supabase para cenário de teste
	- [ ] Desenvolver endpoints FastAPI mínimos para testar o acesso RLS
	- [ ] Validar a segurança e funcionalidade do RLS
	- [ ] Documentar limitações e requisitos técnicos
	- **Dependências:** Fase 0 100% concluída
	- **Definition of Done:** RLS validado e documentado
- [ ] **[DOC-ARQ-001]** HLD Detalhado - Evolução para v1.2 🔺 \ #arquitetura \ #hld \ #critico \ #Fase1_Validacao_Tec_Estrategica `@AgenteM_ArquitetoTI` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Detalhamento completo da arquitetura de segurança (RLS)
	- [ ] Especificação de APIs e integrações com LLMs
	- [ ] Definição de modelos de dados e fluxos
	- [ ] Validação de viabilidade técnica de todas as funcionalidades core
	- **Dependências:** [TST-VAL-001] concluído
	- **Definition of Done:** HLD v1.2 aprovado e validado tecnicamente
- [ ] **[PES-NEG-001]** Validação de Negócio: Estimativa Detalhada de Custos 🔼 \ #negocio \ #pesquisa \ #Fase1_Validacao_Tec_Estrategica `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Estimar custos de APIs de LLMs (Gemini, OpenRouter)
	- [ ] Estimar custos de infraestrutura (Supabase, Vercel, Render)
	- [ ] Calcular custos por usuário e breakeven
	- [ ] Validar viabilidade econômica do modelo freemium
	- **Dependências:** [DOC-ARQ-001] concluído
	- **Definition of Done:** Modelo financeiro validado
- [ ] **[PES-UXD-001]** Elaborar Roteiro de Entrevista com Usuários-Alvo ⏫ \ #ux \ #pesquisa \ #validacao \ #Fase1_Validacao_Tec_Estrategica `@AgenteM_UXDesigner` `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Focar na validação dos "AHA! Moments" definidos
	- [ ] Incluir perguntas sobre "Specialized Intelligence" e diferenciação
	- [ ] Definir objetivos da entrevista focados no "Momento AHA!"
	- [ ] Preparar protótipo de baixa fidelidade para validação
	- [ ] Criar roteiro de teste do "Momento AHA!" (Opções B+C)
	- **Dependências:** [PES-NEG-001] concluído
	- **Definition of Done:** Roteiro validado e protótipo pronto
- [ ] **[TST-UXD-001]** Conduzir Entrevistas com Usuários-Alvo (5-8 profissionais) ⏫ \ #ux \ #pesquisa \ #validacao \ #Fase1_Validacao_Tec_Estrategica `@Maestro`
	- [ ] Validar "AHA! Moments" com protótipo funcional
	- [ ] Medir tempo para primeiro valor percebido
	- [ ] Avaliar percepção de "Specialized Intelligence"
	- [ ] Gravar (com permissão) e tomar notas detalhadas
	- [ ] Identificar padrões e insights chave
	- **Dependências:** [PES-UXD-001] concluído
	- **Definition of Done:** 5-8 entrevistas realizadas e documentadas
- [ ] **[DOC-REQ-002]** Análise Pós-Validação: Consolidar Feedback e Refinar HLD ⏫ \ #ux \ #requisitos \ #validacao \ #Fase1_Validacao_Tec_Estrategica `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Checkpoint de Validação Estratégica conforme metodologia
	- [ ] Refinar métricas de "AHA! Moments" baseadas no feedback
	- [ ] Transcrever/Resumir principais pontos das entrevistas
	- [ ] Atualizar HLD baseado em feedback de usuários
	- [ ] Refinar prioridades do backlog com base no feedback
	- [ ] Validar sequência de desenvolvimento
	- **Dependências:** [TST-UXD-001] concluído
	- **Definition of Done:** HLD refinado e backlog priorizado


## 🚨 FASE 0: FUNDAÇÃO RAG + AGENTES

- [ ] **[CFG-RAG-001]** Configuração e Integração RAG via MCP no Trae IDE 🔺 \ #rag \ #mcp \ #configuracao \ #critico \ #Fase0_RAG_Agentes `@Maestro`
	- [ ] Configuração do MCP Server no Trae IDE
	- [ ] Testes de consulta à documentação Recoloca.AI
	- [ ] Validação de respostas contextualizadas para agentes
	- [ ] Estabelecimento de rotina de indexação automática
	- [ ] Guia de uso do RAG para outros agentes
	- **Dependências:** [IMP-RAG-004] concluído
	- **Definition of Done:** RAG integrado e acessível via MCP no Trae IDE
- [ ] **[CFG-AGT-001]** Configuração dos 4 Agentes Tier 1 Restantes no Trae IDE 🔺 \ #agentes \ #configuracao \ #critico \ #Fase0_RAG_Agentes `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Configurar @AgenteM_ArquitetoTI no Trae IDE (HLD + LLD unificado)
	- [ ] Configurar @AgenteM_UXDesigner no Trae IDE
	- [ ] Configurar @AgenteM_DevFastAPI no Trae IDE
	- [ ] Configurar @AgenteM_DevFlutter no Trae IDE
	- [ ] Testar funcionalidade básica de cada agente com RAG
	- **Dependências:** [CFG-RAG-001] concluído
	- **Definition of Done:** 5 Agentes Tier 1 operacionais no Trae IDE
- [ ] **[EST-AGT-002]** Definição de Responsabilidades de Documentação para Agentes 🔼 \ #estrategia \ #agentes \ #documentacao \ #Fase0_RAG_Agentes `@AgenteM_Orquestrador` `@Maestro`
	- [ ] Discutir como outros agentes contribuem para "Documentação Viva"
	- [ ] Definir responsabilidades e fluxos para consistência contextual
	- [ ] Estabelecer processo de atualização automática de documentação
	- **Dependências:** [CFG-AGT-001] concluído
	- **Definition of Done:** Fluxos de documentação definidos e testados


## ♻️ SESSÃO ATUAL (Em Progresso)

- [ ] **[IMP-RAG-003]** Operacionalização Completa do Sistema RAG 🔺 \ #tecnico \ #rag \ #critico \ #Fase0_RAG_Agentes `@AgenteM_DevFastAPI` `@Maestro`
	- [x] Setup e validação ambiente Conda (`Agents_RAG_Env`) ✅ 2025-06-17
	- [x] Implementação e teste `rag_indexer.py` funcional ✅ 2025-06-17
	- [x] Indexação completa de todos os documentos core do projeto ✅ 2025-06-17
	- [x] **[RAG-INFRA]** Correção da infraestrutura RAG (dependências, embedding model, retrieval system) ✅ 2025-06-18
	- [ ] **[RAG-REINDEX]** Re-indexação completa e otimizada com validação de qualidade
	- [ ] **[RAG-MCP]** Integração robusta do servidor MCP com testes de conectividade
	- [ ] **[RAG-CONTEXT]** Validação contextual específica para @AgenteM_DevFastAPI
	- [ ] **[RAG-SYNC]** Implementação de rotina automática de sincronização
	- [ ] **[RAG-DOCS]** Documentação técnica e handoff para outros agentes
	- **Dependências:** Nenhuma
	- **Definition of Done:** RAG operacional com respostas contextualizadas de qualidade, infraestrutura corrigida e sistema de sincronização automática
- [ ] **[IMP-RAG-004]** Desenvolvimento do MCP Server para Integração RAG 🔺 \ #tecnico \ #mcp \ #rag \ #critico \ #Fase0_RAG_Agentes `@AgenteM_DevFastAPI` `@Maestro`
	- [ ] Desenvolvimento do servidor MCP funcional
	- [ ] Integração com sistema RAG existente
	- [ ] Testes de conectividade e performance
	- [ ] Documentação de configuração e uso
	- **Dependências:** [IMP-RAG-003] concluído
	- **Definition of Done:** MCP Server funcional e documentado
- [ ] **[REO-RAG-001]** Reorganização Estrutural da Infraestrutura RAG 🔺 \ #rag \ #reorganizacao \ #infraestrutura \ #critico \ #Fase0_RAG_Agentes `@AgenteM_DevFastAPI` `@Maestro`
	- [x] **[REO-DIR-001]** Criar estrutura de diretórios detalhada conforme proposta ✅ 2025-06-18
		- [x] Implementar separação `core_logic/`, `tests/`, `scripts/`, `results_and_reports/`
		- [x] Mover arquivos para diretórios apropriados por categoria
		- [x] Validar estrutura final com padrões de projeto
	- [x] **[REO-DEP-001]** Mapear e corrigir dependências entre arquivos ✅ 2025-06-18
		- [x] Identificar todas as dependências de imports entre módulos
		- [x] Documentar mapa de dependências atual
		- [x] Planejar sequência de migração para minimizar quebras
	- [x] **[REO-MIG-001]** Executar migração gradual por categoria ✅ 2025-06-18
		- [x] Migrar arquivos de `core_logic/` primeiro (rag_indexer, rag_retriever, etc.)
		- [x] Migrar testes de integração para `tests/`
		- [x] Migrar scripts utilitários e demos para `scripts/`
		- [x] Migrar relatórios e resultados para `results_and_reports/`
	- [x] **[REO-IMP-001]** Atualizar imports e configurações ✅ 2025-06-18
		- [x] Corrigir imports relativos em todos os arquivos migrados
		- [x] Adicionar constantes PyTorch faltantes em constants.py
		- [x] Validar funcionamento de todos os módulos core
		- [x] Corrigir erros de import absolutos
	- [ ] **[REO-TST-001]** Executar testes para validar reorganização
		- [ ] Executar suite completa de testes após migração
		- [ ] Validar funcionamento do MCP Server
		- [ ] Testar indexação e retrieval após reorganização
		- [ ] Manter cobertura de testes existente
	- [ ] **[REO-DOC-001]** Atualizar documentação pós-reorganização
		- [ ] Atualizar README.md da infraestrutura RAG
		- [ ] Revisar documentação de setup e instalação
		- [ ] Atualizar guias de desenvolvimento
		- [ ] Documentar nova estrutura para outros agentes
	- **Dependências:** [IMP-RAG-003] concluído
	- **Definition of Done:** Infraestrutura RAG reorganizada, testada e documentada com nova estrutura modular


## ✅ CONCLUÍDO

- [ ] **[KAN-REO-001]** Reorganização Completa do Kanban Interno do Projeto 🔺 \ #kanban \ #organizacao \ #gestao \ #Fase0_RAG_Agentes `@AgenteM_Orquestrador` `@Maestro`
	- [x] Consolidar tarefas duplicadas mantendo todos os detalhes já mapeados
	- [x] Reorganizar por fases claras (Fase 0, Fase 1, Fase 2, Concluído, Backlog)
	- [x] Adicionar seção "♻️ Sessão Atual (Em Progresso)" para tarefas da sessão
	- [x] Definir símbolos de prioridade e legenda clara
	- [x] Estabelecer "Definition of Done" para cada tipo de tarefa
	- [x] Criar seções de dependências explícitas
	- [x] Validar estrutura final com Maestro
- [x] **[CFG-RAG-001]** Setup Inicial RAG - Configuração Base ✅ \ #rag \ #setup \ #Fase0_Fundacao `@Maestro`
	- [x] Configuração inicial do sistema RAG
	- [x] Estrutura de documentos base
	- [x] Testes básicos de funcionamento
	- **Concluído em:** Sessões anteriores
- [x] **[VAL-PRM-001]** Validação de Prompts Base ✅ \ #prompts \ #validacao \ #Fase0_Fundacao `@Maestro`
	- [x] Teste e refinamento de prompts iniciais
	- [x] Validação de respostas dos agentes
	- [x] Ajustes de contexto e instruções
	- **Concluído em:** Sessões anteriores
- [x] **[UNI-AGE-001]** Unificação de Agentes ✅ \ #agentes \ #unificacao \ #Fase0_Fundacao `@Maestro`
	- [x] Consolidação de perfis de agentes
	- [x] Padronização de instruções
	- [x] Eliminação de redundâncias
	- **Concluído em:** Sessões anteriores
- [x] **[REV-DOC-001]** Review Documentos Core ✅ \ #documentacao \ #review \ #Fase0_Fundacao `@Maestro`
	- [x] Revisão do Plano Mestre
	- [x] Atualização do ERS
	- [x] Validação do HLD
	- [x] Refinamento do Guia Avançado
	- **Concluído em:** Sessões anteriores
- [x] **[CFG-TRA-001]** Configuração AgenteM_Orquestrador no TRAE IDE ✅ \ #configuracao \ #trae \ #agente \ #Fase0_Fundacao `@Maestro`
	- [x] Setup do agente principal no TRAE
	- [x] Configuração de instruções customizadas
	- [x] Testes de funcionamento
	- [x] Validação de integração com RAG
	- **Concluído em:** Sessões anteriores
- [x] **[KAN-ORG-001]** Reorganização do Kanban Interno ✅ \ #kanban \ #organizacao \ #Fase0_Fundacao `@AgenteM_Orquestrador` `@Maestro`
	- [x] Redução de colunas para compatibilidade com Obsidian
	- [x] Consolidação de tarefas duplicadas
	- [x] Estruturação por fases claras
	- [x] Adição da seção "Sessão Atual"
	- [x] Manutenção de todos os detalhes mapeados
	- **Concluído em:** Sessão atual




%% kanban:settings
```
{"kanban-plugin":"board","lane-width":400,"list-collapse":[null,null,null,null,null,false]}
```
%%