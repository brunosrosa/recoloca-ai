---

kanban-plugin: board
sticker: emoji//2b55

---

## 🧊 Backlog Geral

- [ ] **[TST-VAL-001]** Validação Técnica: Protótipo RLS FastAPI/Supabase (ERS Seção 6.1) \ #tecnico \ #validacao \ #prioridade_alta \ #risco_alto \ #Fase1 `@Maestro` `@AgenteMentorDevFastAPI` `@AgenteMentorSeguranca`
	- [ ] Configurar tabelas e políticas RLS no Supabase para um cenário de teste.
	- [ ] Desenvolver endpoints FastAPI mínimos para testar o acesso RLS.
	- [ ] Validar a segurança e funcionalidade do RLS.
- [ ] **[PES-NEG-001]** Validação de Negócio: Estimativa Detalhada de Custos Iniciais (ERS Seção 6.2) \ #negocio \ #pesquisa \ #prioridade_alta \ #Fase1 `@Maestro`
	- [ ] Estimar custos de APIs de LLMs (Gemini, OpenRouter).
	- [ ] Estimar custos de infraestrutura (Supabase, Vercel, Render, Pipedream).
	- [ ] Estimar outros custos operacionais iniciais.
- [ ] **[IMP-DEV-001]** Desenvolvimento Feature - Kanban (Core) \ #desenvolvimento \ #feature \ #core \ #kanban \ #Fase1 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-KAN-001` a `RF-KAN-007`.
	- [ ] Implementar frontend para `RF-KAN-001` a `RF-KAN-007`.
	- [ ] Realizar testes de integração.
- [ ] **[IMP-DEV-002]** Desenvolvimento Feature - Contas e Autenticação (Core) \ #desenvolvimento \ #feature \ #core \ #auth \ #Fase1 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-AUTH-001` a `RF-AUTH-012`.
	- [ ] Implementar frontend para `RF-AUTH-001` a `RF-AUTH-012`.
- [ ] **[DOC-ARQ-001]** Arquitetura: Detalhamento LLDs para Módulos do MVP (Pós-Validação dos Passos Críticos) \ #arquitetura \ #documentacao \ #Fase1 `@AgenteMentorArquitetoLLD` `@Maestro`
	- [ ] Para `LLD_Modulo_Auth.md`: detalhar modelos de dados, classes, fluxos de autenticação.
	- [ ] Para `LLD_Modulo_Kanban.md`: detalhar estruturas de dados, lógica de manipulação de cards/colunas.
	- [ ] Para `LLD_Modulo_CV.md`: detalhar processos de upload, parsing e armazenamento de CVs.
	- [ ] Para `LLD_Modulo_Coach.md`: detalhar interações do chatbot, lógica de proatividade.
	- [ ] Para `LLD_Modulo_Pagamentos.md`: detalhar integração com gateway, gerenciamento de assinaturas.
- [ ] **[DOC-REQ-001]** Requisitos: Detalhar HUs e ACs para o MVP (Pós-Validação com Usuários) \ #requisitos \ #agile \ #Fase1 `@AgenteMentorPO` `@Maestro`
	- [ ] Para cada funcionalidade priorizada do MVP, escrever Histórias de Usuário claras.
	- [ ] Para cada HU, definir Critérios de Aceite testáveis.
	- [ ] Armazenar em [[docs/02_Requisitos/HU_AC/]].
- [ ] **[IMP-DEV-003]** Desenvolvimento Feature - Pagamentos (Core) \ #desenvolvimento \ #feature \ #core \ #pagamento \ #Fase2 `@AgenteMentorDevFastAPI` `@Maestro`
	- [ ] Configurar Gateway de Pagamento.
	- [ ] Implementar Lógica de Assinaturas Freemium (`RF-PAY-SUB-001` a `RF-PAY-SUB-004`).
- [ ] **[IMP-DEV-004]** Desenvolvimento Feature - Importação de Vagas (Core) \ #desenvolvimento \ #feature \ #core \ #ia \ #importacao \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-IMP-001`, `RF-IMP-002`.
	- [ ] Implementar frontend para `RF-IMP-001`, `RF-IMP-002`.
	- [ ] Testar integração com LLM para parsing.
- [ ] **[IMP-DEV-005]** Desenvolvimento Feature - Otimização CV (Upload e Parsing) \ #desenvolvimento \ #feature \ #core \ #cv \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-CV-001`, `RF-CV-002`.
	- [ ] Implementar frontend para `RF-CV-001`, `RF-CV-002`.
	- [ ] Integrar e testar ferramenta de parsing de PDF.
- [ ] **[IMP-DEV-006]** Desenvolvimento Feature - Otimização CV (Análise IA) \ #desenvolvimento \ #feature \ #core \ #ia \ #cv \ #Fase2 `@AgenteMentorDevFastAPI` `@Maestro`
	- [ ] Implementar backend para Análise Vaga-CV (Score IA) (`RF-CV-003`).
	- [ ] Implementar backend para Sugestões de Otimização (`RF-CV-004`).
	- [ ] Implementar backend para Estimativa Salarial (`RF-CV-005`).
- [ ] **[IMP-DEV-007]** Desenvolvimento Feature - Coach IA (Core) \ #desenvolvimento \ #feature \ #core \ #ia \ #coach \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para Chatbot básico (`RF-COACH-001`).
	- [ ] Implementar lógica de atuação proativa (`RF-COACH-002`, `RF-COACH-003`).
	- [ ] Implementar backend para orientações (`RF-COACH-004`).
	- [ ] Implementar frontend para interação com Coach IA.
- [ ] **[PES-UXD-001]** Validação de UX/Valor: Elaborar Roteiro de Entrevista com Usuários-Alvo & Realizar a Pesquisa (Base para ERS Seção 6.3) \ #ux \ #pesquisa \ #validacao \ #prioridade_alta \ #Fase1 `@AgenteMentorPO` `@Maestro`
	- [ ] Definir objetivos da entrevista.
	- [ ] Listar perguntas chave abertas e fechadas.
	- [ ] Preparar material de apoio (se houver mockups iniciais).
- [ ] **[TST-UXD-001]** Validação de UX/Valor: Conduzir Entrevistas com Usuários-Alvo (3-5 profissionais de TI - ERS Seção 6.3) \ #ux \ #pesquisa \ #validacao \ #prioridade_alta \ #Fase1 `@Maestro`
	- [ ] Agendar e realizar as entrevistas.
	- [ ] Gravar (com permissão) e tomar notas detalhadas.
- [ ] **[DOC-UXD-001]** Validação de UX/Valor: Criar Mockups/Protótipos Baixa Fidelidade para Validação (Base para ERS Seção 6.3) \ #ux \ #design \ #validacao \ #prioridade_alta \ #Fase1 `@AgenteM_UIDesigner` `@Maestro`
	- [ ] Esboçar wireframes das telas principais do MVP.
	- [ ] Considerar uso de Stitch/FlutterFlow para protótipo navegável simples.
- [ ] **[DOC-UXD-002]** Design: Criação do Style Guide Detalhado (`STYLE_GUIDE.md`) \ #ux \ #ui \ #documentacao \ #Fase1 `@AgenteM_UIDesigner` `@Maestro`
	- [ ] Definir e documentar paleta de cores, tipografia, iconografia.
	- [ ] Criar diretrizes de espaçamento, grids e layout.
	- [ ] Especificar componentes de UI reutilizáveis e seus estados.
	- [ ] Adicionar seções de tom de voz e UX Writing.
- [ ] **[DOC-API-001]** API: Desenvolvimento das Especificações OpenAPI 3.0 (`RecolocaAPI_v1_OpenAPI.yaml`) \ #api \ #arquitetura \ #documentacao \ #Fase1 `@AgenteMentorAPI` `@Maestro`
	- [ ] Definir todos os endpoints necessários para o MVP.
	- [ ] Para cada endpoint, detalhar métodos HTTP, parâmetros, request/response bodies e schemas.
	- [ ] Incluir definições de segurança (ex: JWT).
- [ ] **[CFG-INF-001]** Ambiente Dev/Deploy - Configuração Inicial e Esboço de CI/CD \ #devops \ #infra \ #Fase1 `@Maestro` `@AgenteM_DevOps`
	- [ ] Criar repositórios Git para frontend, backend, e possivelmente para MCPs.
	- [ ] Configurar linters, formatters e hooks de pré-commit.
	- [ ] Esboçar um pipeline de CI básico (build, test) para backend e frontend.
	- [ ] Esboçar um pipeline de CD básico para deploy em Vercel/Render.
- [ ] **[IMP-DEV-008]** Desenvolvimento Feature - Otimização CV (Output e Versionamento) \ #desenvolvimento \ #feature \ #core \ #cv \ #Fase2 `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para download PDF otimizado (`RF-CV-006`).
	- [ ] Implementar backend para gerenciamento de versões de CV (`RF-CV-007`).
	- [ ] Implementar frontend correspondente.
- [ ] **[DOC-REQ-002]** Análise Pós-Validação: Consolidar Feedback e Refinar Documentos \ #ux \ #requisitos \ #validacao \ #prioridade_media \ #Fase1 `@Maestro` `@AgenteMentorPO`
	- [ ] Transcrever/Resumir principais pontos das entrevistas.
	- [ ] Identificar padrões e insights chave.
	- [ ] Atualizar [[docs/02_Requisitos/ERS.md]] e prioridades do backlog com base no feedback.
- [ ] **[EST-NEG-001]** Gerenciamento: Planejar 1ª Sprint de Desenvolvimento do MVP (Pós-Validação dos Passos Críticos) \ #gerenciamento \ #Fase1 `@Maestro`
	- [ ] Selecionar HUs para a 1ª Sprint.
	- [ ] Estimar esforço (story points ou tempo).
	- [ ] Definir a meta da Sprint.
- [ ] **[DOC-INF-001]** Infra/DevOps: Estratégia Detalhada de Monitoramento e Logging \ #infra \ #devops \ #Fase2 `@AgenteM_DevOps` `@Maestro`
	- [ ] Pesquisar e selecionar ferramentas (ex: Sentry, Better Uptime, Logtail) para `RNF-REL-003`.
	- [ ] Definir quais métricas e logs chave serão monitorados para backend, frontend e serviços.
	- [ ] Esboçar arquitetura de logging e monitoramento.
- [ ] **[EST-QUA-001]** QA/Testes: Definição da Abordagem para Testes com IA \ #qa \ #ia \ #estrategia \ #Fase2 `@AgenteMentorQA` `@Maestro`
	- [ ] Pesquisar e definir estratégias para testar funcionalidades que dependem de LLMs (ex: Otimização de CV, Coach IA).
	- [ ] Como definir oráculos de teste? Como lidar com a não-deterministicidade?
- [ ] **[EST-QUA-002]** QA/Testes - Estratégia para Sistema Multiagente \ #ia \ #agente \ #qa \ #estrategia \ #Fase2 `@Maestro` `@AgenteMentorQA`
	- [ ] Definir como testar o comportamento de agentes individuais.
	- [ ] Definir como testar a orquestração e a comunicação entre agentes.
- [ ] **[PES-DEV-001]** Pesquisa/Definição: Ferramentas de Parsing PDF Alternativas \ #pesquisa \ #tecnico \ #Fase2 `@Maestro`
	- [ ] Avaliar eficácia de `pymupdf` / `Tesseract` para `RF-CV-001`.
	- [ ] Se necessário, pesquisar e listar alternativas.
	- [ ] Realizar PoC (Prova de Conceito) com a melhor alternativa, se aplicável.
- [ ] **[EST-NEG-002]** Negócio: Estratégia de Precificação e Testes A/B (Pós-Validação MVP) \ #negocio \ #marketing \ #Fase3 `@Maestro`
	- [ ] Detalhar Estratégia de Precificação para Tier Premium.
	- [ ] Planear Testes A/B para diferentes modelos de precificação (Pós-Validação com Usuários e análise de Custos).
- [ ] **[DOC-AGT-001]** Agente APO - Aprofundamento do Perfil e Ferramentas \ #ia \ #agente \ #kpi \ #analise \ #Fase2 `@Maestro` `@AgenteM_Performance` `@AgenteOrquestrador`
	- [ ] Brainstorm de KPIs para Aquisição, Ativação, Retenção, Receita, Referência (AARRR) para o MVP.
	- [ ] Para cada KPI selecionado: definir nome, descrição, fórmula, fonte de dados ideal, meta inicial, frequência de medição.
	- [ ] Documentar os KPIs no perfil do APO ou em documento dedicado.
	- [ ] Desenvolver conteúdo para `TPL_PRPT_APO_DefinirKPI.md`.
	- [ ] Desenvolver conteúdo para `TPL_PRPT_APO_AnalisarDadosTrend.md`.
	- [ ] Desenvolver conteúdo para `TPL_PRPT_APO_FormularHipoteseOtimizacao.md`.
	- [ ] Coletar/Resumir artigos sobre Product Analytics para [[rag_infra/source_documents/Analytics_Knowledge/]].
	- [ ] Coletar/Resumir material sobre Métricas de SaaS para [[rag_infra/source_documents/SaaS_Metrics_Knowledge/]].
- [ ] **[DOC-AGT-002]** IA Agentes - Documentação da Arquitetura do Sistema Multiagente \ #ia \ #agente \ #arquitetura \ #documentacao \ #Fase2 `@Maestro` `@AgenteMentorArquitetoHLD` `@AgenteMentorDocumentacao`
	- [ ] Criar diagramas (ex: C 4 Model Nível 2 ou 3) para ilustrar componentes e interações.
	- [ ] Descrever fluxos de dados e de controle entre os agentes e o RAG/MCPs.
- [ ] **[DOC-AGT-003]** Criação de Perfis Detalhados para Agentes Futuros Prioritários \ #ia \ #agente \ #documentacao \ #futuro \ #Fase3 `@Maestro` `@AgenteOrquestrador`
	- [ ] Selecionar 1-2 agentes da lista de "Agentes Futuros" (ex: `@AgenteMentorDados`) com base no roadmap pós-MVP.
	- [ ] Utilizar o [[docs/04_Agentes_IA/Templates_Modelos/TEMPLATE_PERFIL_AGENTE.md]] (tendo como base o perfil do `@AgenteOrquestrador`) para criar seus perfis detalhados.
- [ ] **[IMP-DEV-009]** Desenvolvimento Pós-MVP - Extensão Chrome Web Clipper \ #pos_mvp \ #desenvolvimento \ #extensao \ #Fase3 `@AgenteMentorDevJS` `@Maestro`
	- [ ] Detalhar requisitos técnicos da extensão (`RF-IMP-003`).
	- [ ] Desenvolver Manifest V 3 e scripts de conteúdo/background.
	- [ ] Implementar UI da extensão e comunicação com API backend.
- [ ] **[EST-NEG-003]** Planeamento Estratégico Pós-MVP (Recoloca.AI e Sistema Multiagente) \ #estrategia \ #roadmap \ #pos_mvp \ #Fase3 `@Maestro` `@AgenteOrquestrador`
	- [ ] Definir o roadmap de funcionalidades para o Recoloca.AI para os próximos 6-12 meses pós-MVP.
	- [ ] Identificar e priorizar quais novos agentes ou capacidades de agentes serão necessários para suportar o roadmap.
	- [ ] Planear a evolução da infraestrutura RAG/MCP com base nas necessidades futuras.
- [ ] **[DOC-LEG-001]** Legal: Documentação Jurídica (Pré-Lançamento Público) \ #legal \ #prioridade_media \ #Fase3 `@Maestro` `@AgenteMentorLegal`
	- [ ] Elaborar primeira versão dos Termos de Uso.
	- [ ] Elaborar primeira versão da Política de Privacidade.
	- [ ] Submeter para validação jurídica especializada.
- [ ] **[CFG-UXD-001]** Configuração Ferramentas - FlutterFlow (Opcional) \ #configuracao \ #ux \ #ui \ #Fase1 `@Maestro`
	- [ ] Criar conta (se for usar para prototipagem de UI).
- [ ] **[CFG-INF-002]** Configuração Ferramentas - Pipedream (Setup Inicial) \ #configuracao \ #devops \ #Fase2 `@Maestro`
	- [ ] Criar conta no Pipedream (plano gratuito).
	- [ ] Explorar a interface e criar um workflow simples de teste (ex: notificação por email em trigger HTTP).
- [ ] **[PES-NEG-002]** Coleta de Dados para Estimativa Salarial (Base para `RF-CV-005`) \ #pesquisa \ #dados \ #cv \ #Fase2 `@Maestro`
	- [ ] Identificar fontes de dados salariais confiáveis para o mercado brasileiro de TI.
	- [ ] Avaliar APIs disponíveis (ex: Glassdoor, LinkedIn, sites de emprego brasileiros).
	- [ ] Definir estratégia de coleta e atualização dos dados salariais.
- [ ] **[TST-INF-001]** Avaliação Contínua de Ferramentas e Tecnologias \ #avaliacao \ #tecnologia \ #Fase1 `@Maestro`
	- [ ] Monitorar atualizações e novas versões das ferramentas core (FastAPI, Flutter, Supabase, etc.).
	- [ ] Avaliar impacto de mudanças nas ferramentas sobre o roadmap do projeto.
	- [ ] Documentar decisões de upgrade ou mudança de ferramentas.
- [ ] **[PES-DEV-002]** Pesquisar sobre **BugBot** (Cursor Like) \ #Bug \ #Fase3 `@Maestro`


## 🎯 A Fazer



## 🔄 Próximas Fases da Estratégia Refinada (MVP)

- [ ] **[MVP-EST-REF-002]** MVP - Estratégia Refinada: Base Sólida + Aprendizado Iterativo [FASE 2] - Protótipo da Base Sólida \ #mvp \ #desenvolvimento \ #base_solida \ #prioridade_alta \ #fluxo_core `@Maestro` `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter`
	- [ ] Configurar autenticação com Supabase
	- [ ] Criar API FastAPI básica com endpoints essenciais
	- [ ] Implementar upload de arquivo (sem parsing avançado)
	- [ ] Desenvolver Kanban básico (3 colunas: Interessante, Aplicado, Resposta)
	- [ ] Criar interface Flutter PWA responsiva
	- [ ] Integrar frontend com backend via API
- [ ] **[MVP-EST-REF-003]** MVP - Estratégia Refinada: Base Sólida + Aprendizado Iterativo [FASE 3] - Aprendizado sobre Limitações \ #mvp \ #desenvolvimento \ #limitacoes \ #aprendizado \ #prioridade_media_alta \ #fluxo_core `@Maestro` `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter`
	- [ ] Implementar parsing de CV (PDF → dados estruturados)
	- [ ] Desenvolver integração básica com LinkedIn (scraping/API)
	- [ ] Criar formulário inteligente de vaga (LinkedIn-focused)
	- [ ] Implementar validações e tratamento de erros robusto
	- [ ] Documentar limitações descobertas e soluções propostas
- [ ] **[MVP-EST-REF-004]** MVP - Estratégia Refinada: Base Sólida + Aprendizado Iterativo [FASE 4] - Refinamento do "Momento AHA!" \ #mvp \ #desenvolvimento \ #ia \ #coach \ #momento_aha \ #prioridade_alta \ #fluxo_core `@Maestro` `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter`
	- [ ] Configurar pipeline RAG para análise de CVs
	- [ ] Implementar Coach AI para otimização de CV
	- [ ] Desenvolver sistema de sugestões personalizadas
	- [ ] Criar interface de feedback e iteração
	- [ ] Realizar testes de validação com usuários reais
	- [ ] Refinar algoritmos baseado no feedback


## 📋 Documentação Paralela (MVP)

- [ ] **[DOC-MVP-001]** Criação de LLDs para Componentes Core do MVP \ #documentacao \ #lld \ #mvp \ #prioridade_media \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [ ] Criar LLD_Autenticacao_Supabase.md
	- [ ] Criar LLD_CV_Parsing_Pipeline.md
	- [ ] Criar LLD_Kanban_Vagas.md
	- [ ] Criar LLD_Otimizacao_CV_IA.md
- [ ] **[DOC-MVP-002]** Especificação OpenAPI para Backend MVP \ #documentacao \ #api \ #openapi \ #prioridade_media \ #Fase1 `@Maestro` `@AgenteMentorDevFastAPI`
	- [ ] Definir endpoints para autenticação
	- [ ] Definir endpoints para gestão de CVs
	- [ ] Definir endpoints para gestão de vagas
	- [ ] Definir endpoints para otimização com IA


## 🤖 Infraestrutura de Agentes (Suporte ao MVP)

- [ ] **[EST-REQ-001]** Análise Estratégica: Consistência da Documentação Core \ #estrategia \ #documentacao \ #validacao \ #prioridade_alta \ #Fase1 `@AgenteOrquestrador` `@Maestro`
	- [ ] Verificar alinhamento e sinergia entre [[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]], [[docs/02_Requisitos/ERS.md]], e [[docs/03_Arquitetura_Solucao/HLD.md]].
	- [ ] Identificar e listar potenciais desalinhamentos, lacunas ou pontos que necessitem de esclarecimento/refinamento.
	- [ ] Propor atualizações nos documentos, se necessário, para garantir coesão estratégica.
- [ ] **[CFG-AGT-001]** Finalização e Operacionalização Inicial do `@AgenteOrquestrador` (v 1.0) \ #ia_agente \ #orquestracao \ #configuracao \ #prioridade_alta \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [ ] **(Revisão/Consolidação):** Refinar e validar o perfil completo do `@AgenteOrquestrador` em [[docs/04_Agentes_IA/Perfis/@AgenteOrquestrador.md]], com foco especial no "Prompt Base Inicial" e nas "Instruções Fundamentais", garantindo que os valores e pesos para sua atuação como assistente principal estejam claros.
	- [ ] **(Revisão/Consolidação):** Configurar o `@AgenteOrquestrador` no Trae IDE, inserindo o Prompt Base refinado e definindo as ferramentas iniciais que ele poderá acessar.
	- [ ] **(Nova):** Realizar testes de interação com o `@AgenteOrquestrador` (aqui com Gemini) utilizando a "Documentação Viva" como base de referência, focando em:
		- Capacidade de seguir o tom de voz e persona.
		- Compreensão e aplicação das `project_rules.md` e `user_rules.md`.
		- Habilidade de decompor problemas e sugerir próximos passos.
	- [ ] **(Nova):** Definir e documentar um fluxo de trabalho inicial de como você (Maestro) e o `@AgenteOrquestrador` colaborarão para avançar as próximas tarefas do projeto (ex: refinar ERS, planear sprints, co-criar prompts para outros agentes).
- [ ] **[IMP-RAG-001]** Operacionalização do Sistema RAG (v 1.0) para Consumo pelo `@AgenteOrquestrador` \ #ia_agente \ #rag \ #mcp \ #desenvolvimento \ #prioridade_alta \ #Fase1 `@Maestro` `@AgenteM_DevFastAPI` `@AgenteM_DevOps`
	- [ ] **(Revisão/Consolidação):** Concluir o desenvolvimento e testes unitários/integração do servidor MCP para o RAG (conforme a tarefa "RAG - Design e Implementação do Servidor MCP" já existente, focando em torná-lo funcional).
	- [ ] **(Revisão/Consolidação):** Realizar a indexação inicial dos documentos chave da "Documentação Viva" (ex: ERS, Plano Mestre, Perfis de Agentes, Guias Centrais) para o RAG.
	- [ ] **(Nova):** Configurar a ferramenta RAG-MCP no Trae IDE e associá-la como uma ferramenta disponível para o `@AgenteOrquestrador`.
	- [ ] **(Nova):** Instruir explicitamente o `@AgenteOrquestrador` (via prompt ou interação) sobre como e quando utilizar a ferramenta RAG para consultar a "Documentação Viva" de forma eficiente.
	- [ ] **(Nova):** Realizar testes de ponta a ponta: `@AgenteOrquestrador` recebendo uma tarefa do Maestro, identificando a necessidade de consultar a documentação, utilizando a ferramenta RAG-MCP para obter chunks de dados, e utilizando esses chunks para formular uma resposta ou plano de ação.
	- [ ] **(Revisão/Consolidação):** Validar a qualidade dos chunks recuperados pelo RAG e a capacidade do `@AgenteOrquestrador` de sintetizá-los efetivamente.
- [ ] **[IMP-RAG-002]** RAG - Design e Implementação do Servidor MCP \ #ia \ #agente \ #rag \ #mcp \ #desenvolvimento \ #Fase1 `@Maestro` `@AgenteMentorDevFastAPI`
	- [ ] Desenhar a especificação da API do servidor MCP para o RAG (endpoints, formato de request/response).
	- [ ] Implementar a lógica do servidor em Python, expondo o retriever LangChain/FAISS.
	- [ ] Criar Dockerfile para o servidor MCP (se aplicável).
	- [ ] Realizar testes unitários e de integração do servidor MCP.
	- [ ] Configurar este servidor como uma ferramenta no Trae IDE e testar com um agente.
- [ ] **[CFG-AGT-002]** IA Agentes - Prompts Base e Ferramentas para Squad Principal \ #ia \ #agente \ #prompt_engineering \ #configuracao \ #prioridade_media \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [ ] Para cada agente do squad principal, revisar e refinar seu "Prompt Base Inicial" (nos perfis individuais em [[docs/04_Agentes_IA/Perfis/]]).
	- [ ] Para cada agente, listar explicitamente as ferramentas MCP que ele precisaria (ex: RAG, APIs específicas, outros agentes).
	- [ ] Estabelecer e documentar o processo de co-criação de prompts para agentes especializados, com base no [[01_Guias_Centrais/GUIA_AVANCADO.md]] e nas capacidades definidas no [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]].
- [ ] **[CFG-AGT-003]** IA Agentes - Setup Trae IDE (Configuração Detalhada Agentes) \ #ia \ #agente \ #configuracao \ #prioridade_media \ #Fase1 `@Maestro`
	- [ ] Configurar o Agente `@AgenteMentorPO` no Trae IDE.
	- [ ] Configurar os demais agentes do Squad Principal no Trae IDE progressivamente, conforme forem sendo detalhados e necessitarem de operacionalização.
- [ ] **[DOC-AGT-004]** IA Agentes - Orquestração (`@AgenteOrquestrador`) - Projeto Detalhado \ #ia \ #agente \ #orquestracao \ #arquitetura \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [ ] Detalhar o processo de decomposição de tarefas.
	- [ ] Mapear quais agentes-ferramenta (MCPs) são chamados para quais tipos de subtarefas.
	- [ ] Definir como o estado da tarefa é mantido durante a orquestração (se necessário).
- [ ] **[DOC-AGT-005]** IA Agentes - Elaboração Detalhada de Regras (`project_rules.md`, `user_rules.md`) \ #ia \ #agente \ #configuracao \ #documentacao \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [ ] Popular `project_rules.md` com padrões de codificação, segurança, documentação, etc.
	- [ ] Popular `user_rules.md` com preferências do Maestro.
	- [ ] Definir como os agentes serão instruídos a consultar e seguir estas regras.


## 🔧 Tarefas de Suporte e Infraestrutura

- [ ] **[IMP-AGT-001]** IA Agentes - Orquestração (`@AgenteOrquestrador`) - Implementação e Teste \ #ia \ #agente \ #orquestracao \ #desenvolvimento \ #Fase2 `@Maestro` `@AgenteOrquestrador`
	- [ ] Escrever e refinar o prompt de sistema avançado para o `@AgenteOrquestrador`.
	- [ ] Desenvolver/Configurar os servidores MCP para os agentes-membro a serem orquestrados.
	- [ ] Testar cenários de orquestração com 2-3 agentes.
- [ ] **[DOC-RAG-001]** RAG - Otimização e Processos de Manutenção \ #ia \ #agente \ #rag \ #operacoes \ #Fase2 `@Maestro` `@AgenteM_DevOps`
	- [ ] Realizar testes de carga e stress no retriever RAG para identificar gargalos.
	- [ ] Desenvolver script ou processo para reindexar a "Documentação Viva" automaticamente ou sob demanda.
	- [ ] Documentar o processo de manutenção e atualização do RAG.
- [ ] **[CFG-AGT-004]** IA Agentes - Gerenciamento de Segredos para MCPs \ #ia \ #agente \ #mcp \ #seguranca \ #Fase2 `@Maestro` `@AgenteMentorSeguranca`
	- [ ] Pesquisar e selecionar a abordagem de gerenciamento de segredos (ex: HashiCorp Vault, variáveis de ambiente injetadas de forma segura no deploy do MCP).
	- [ ] Implementar a solução escolhida para o servidor RAG-MCP e outros MCPs futuros.
	- [ ] Documentar o procedimento de forma segura.
- [ ] **[DOC-RAG-002]** RAG - Criação e Curadoria de Conteúdo para Bases de Conhecimento \ #ia \ #agente \ #rag \ #conteudo \ #Fase2 `@Maestro` `@AgenteOrquestrador`
	- [ ] Desenvolver estratégia e processo para identificar, curar e formatar documentos para as bases de conhecimento (ex: `Analytics_Knowledge`, `SaaS_Metrics_Knowledge`).
	- [ ] Processar e adicionar os primeiros lotes de documentos a estas bases.


## ⚡ Em Andamento

- [ ] **[MVP-EST-REF-001]** MVP - Estratégia Refinada: Base Sólida + Aprendizado Iterativo [FASE 1] - Configuração dos Agentes Essenciais \ #mvp \ #estrategia \ #agentes \ #configuracao \ #prioridade_critica \ #fluxo_core `@Maestro` `@AgenteOrquestrador`
	- [ ] Configurar @AgenteM_UXDesigner no Trae AI
	- [ ] Configurar @AgenteMentorDevFastAPI no Trae AI
	- [ ] Configurar @AgenteMentorPO no Trae AI
	- [ ] Testar comunicação e delegação entre agentes
	- [ ] Validar acesso ao RAG e MCPs pelos agentes configurados


## 🔍 Validação/Revisão



## ✅ Concluído

- [x] **[EST-DEV-001]** Estratégia de Produto: Definição de Prioridades e Sequenciamento de Features para o MVP \ #estrategia \ #produto \ #mvp \ #prioridade_alta \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [x] Revisar e validar as funcionalidades core definidas no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]].
	- [x] Aplicar frameworks de priorização (ex: RICE, MoSCoW) para sequenciar o desenvolvimento.
	- [x] Definir critérios claros para o que constitui um MVP viável.
	- [x] Documentar as decisões de priorização e suas justificativas.
	- [x] Criar jornada completa do usuário wizard-style em [[docs/02_Requisitos/HU_AC/HU_MVP_Jornada_Usuario.md]].
- [x] **[IMP-AGT-002]** Desenvolvimento de um Protótipo Funcional com Agentes de IA \ #ia \ #agente \ #prototipo \ #desenvolvimento \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [x] Configurar ambiente de desenvolvimento com Trae IDE.
	- [x] Implementar interações básicas entre Maestro e `@AgenteOrquestrador`.
	- [x] Testar capacidades de decomposição de tarefas e sugestões estratégicas.
	- [x] Documentar lições aprendidas e próximos passos.
- [x] **[DOC-AGT-006]** Criação de um "Playbook de Projeto Baseado em Agentes de IA" \ #ia \ #agente \ #documentacao \ #metodologia \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [x] Documentar metodologia "Desenvolvimento Solo Ágil Aumentado por IA".
	- [x] Criar templates e guias para interação eficaz com agentes.
	- [x] Estabelecer melhores práticas para orquestração de agentes.
	- [x] Incluir exemplos práticos e casos de uso.
- [x] **[CFG-INF-003]** Configuração de Ambiente de Desenvolvimento (Obsidian, Git, Trae IDE, OpenRouter, VS Code) \ #configuracao \ #ambiente \ #Fase1 `@Maestro`
	- [x] Configurar Obsidian com plugins necessários (Kanban, Git, etc.).
	- [x] Configurar repositório Git e estrutura de versionamento.
	- [x] Configurar Trae IDE com agentes iniciais.
	- [x] Configurar OpenRouter para acesso a LLMs.
	- [x] Configurar VS Code com extensões relevantes.
- [x] **[CFG-AGT-005]** Setup Inicial de Agentes de IA no Trae IDE \ #ia \ #agente \ #configuracao \ #Fase1 `@Maestro`
	- [x] Configurar `@AgenteOrquestrador` com prompt base inicial.
	- [x] Testar funcionalidades básicas de interação.
	- [x] Documentar configurações e ajustes necessários.
- [x] **[DOC-AGT-007]** Definição da Estrutura de Documentação para Perfis de Agentes \ #ia \ #agente \ #documentacao \ #estrutura \ #Fase1 `@Maestro`
	- [x] Criar template padrão para perfis de agentes.
	- [x] Definir seções obrigatórias e opcionais.
	- [x] Estabelecer convenções de nomenclatura.
	- [x] Criar exemplos de referência.
- [x] **[DOC-AGT-008]** Criação e Refinamento de Documentos de Overview e Perfis de Agentes \ #ia \ #agente \ #documentacao \ #Fase1 `@Maestro` `@AgenteOrquestrador`
	- [x] Criar [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]].
	- [x] Criar perfil detalhado do `@AgenteOrquestrador`.
	- [x] Criar perfis iniciais para agentes do squad principal.
	- [x] Revisar e refinar documentação existente.
- [x] **[DOC-AGT-009]** Definição de Nomenclatura para Prompts e Templates \ #ia \ #agente \ #documentacao \ #nomenclatura \ #Fase1 `@Maestro`
	- [x] Estabelecer convenções para nomes de arquivos de prompts.
	- [x] Definir estrutura de pastas para organização.
	- [x] Criar templates base para diferentes tipos de prompts.
	- [x] Documentar diretrizes de nomenclatura.
- [x] **[DOC-REQ-003]** Consolidação Inicial da Documentação Viva \ #documentacao \ #consolidacao \ #Fase1 `@Maestro`
	- [x] Copiar conteúdo relevante de artefatos para arquivos de documentação.
	- [x] Organizar estrutura de pastas e arquivos.
	- [x] Estabelecer links internos entre documentos.
	- [x] Criar índices e sumários para navegação.
- [x] **[DOC-AGT-010]** Organização de Arquivos de Prompts \ #ia \ #agente \ #prompts \ #organizacao \ #Fase1 `@Maestro`
	- [x] Criar estrutura de pastas em [[docs/05_Prompts/]].
	- [x] Organizar templates base e prompts específicos.
	- [x] Estabelecer convenções de versionamento.
	- [x] Documentar processo de criação e manutenção de prompts.




%% kanban:settings
```
{"kanban-plugin":"board","lane-width":400,"list-collapse":[null,null,null,false,false]}
```
%%