---

kanban-plugin: board
sticker: emoji//2b55

---

## 🧊 Backlog Geral

- [ ] **Validação de UX/Valor: Elaborar Roteiro de Entrevista com Usuários-Alvo & Realizar a Pesquisa** (Base para ERS Seção 6.3) \ #ux \ #pesquisa \ #validacao \ #prioridade \ #alta `@AgenteMentorPO` `@Maestro`
	- [ ] Definir objetivos da entrevista.
	- [ ] Listar perguntas chave abertas e fechadas.
	- [ ] Preparar material de apoio (se houver mockups iniciais).
- [ ] **Validação de UX/Valor: Conduzir Entrevistas com Usuários-Alvo** (3-5 profissionais de TI - ERS Seção 6.3) \ #ux \ #pesquisa \ #validacao \ #prioridade \ #alta `@Maestro`
	- [ ] Agendar e realizar as entrevistas.
	- [ ] Gravar (com permissão) e tomar notas detalhadas.
- [ ] **Análise Pós-Validação: Consolidar Feedback e Refinar Documentos** \ #ux \ #requisitos \ #validacao \ #prioridade \ #media `@Maestro` `@AgenteMentorPO`
	- [ ] Transcrever/Resumir principais pontos das entrevistas.
	- [ ] Identificar padrões e insights chave.
	- [ ] Atualizar [[docs/02_Requisitos/ERS.md]] e prioridades do backlog com base no feedback.
- [ ] **Configuração Ferramentas - FlutterFlow (Opcional):** \ #configuracao \ #ux \ #ui `@Maestro`
	- [ ] Criar conta (se for usar para prototipagem de UI).
- [ ] **Validação de UX/Valor: Criar Mockups/Protótipos Baixa Fidelidade para Validação** (Base para ERS Seção 6.3) \ #ux \ #design \ #validacao \ #prioridade \ #alta `@AgenteMentorUIDesigner` `@Maestro`
	- [ ] Esboçar wireframes das telas principais do MVP.
	- [ ] Considerar uso de Stitch/FlutterFlow para protótipo navegável simples.
- [ ] **Validação de Negócio: Estimativa Detalhada de Custos Iniciais** (ERS Seção 6.2) \ #negocio \ #pesquisa \ #prioridade \ #alta `@Maestro`
	- [ ] Estimar custos de APIs de LLMs (Gemini, OpenRouter).
	- [ ] Estimar custos de infraestrutura (Supabase, Vercel, Render, Pipedream).
	- [ ] Estimar outros custos operacionais iniciais.
- [ ] **Negócio: Estratégia de Precificação e Testes A/B (Pós-Validação MVP)** \ #negocio \ #marketing `@Maestro`
	- [ ] Detalhar Estratégia de Precificação para Tier Premium.
	- [ ] Planear Testes A/B para diferentes modelos de precificação (Pós-Validação com Usuários e análise de Custos).
- [ ] **Design: Criação do Style Guide Detalhado (`STYLE_GUIDE.md`)** \ #ux \ #ui \ #documentacao `@AgenteMentorUIDesigner` `@Maestro`
	- [ ] Definir e documentar paleta de cores, tipografia, iconografia.
	- [ ] Criar diretrizes de espaçamento, grids e layout.
	- [ ] Especificar componentes de UI reutilizáveis e seus estados.
	- [ ] Adicionar seções de tom de voz e UX Writing.
- [ ] **Requisitos: Detalhar HUs e ACs para o MVP** (Pós-Validação com Usuários) \ #requisitos \ #agile `@AgenteMentorPO` `@Maestro`
	- [ ] Para cada funcionalidade priorizada do MVP, escrever Histórias de Usuário claras.
	- [ ] Para cada HU, definir Critérios de Aceite testáveis.
	- [ ] Armazenar em [[docs/02_Requisitos/HU_AC/]].
- [ ] **Agente APO - Aprofundamento do Perfil e Ferramentas** \ #ia \ #agente \ #kpi \ #analise `@Maestro` `@AgenteAnalistaPerformanceOtimizacao` `@AgenteOrquestrador`
	- [ ] Brainstorm de KPIs para Aquisição, Ativação, Retenção, Receita, Referência (AARRR) para o MVP.
	- [ ] Para cada KPI selecionado: definir nome, descrição, fórmula, fonte de dados ideal, meta inicial, frequência de medição.
	- [ ] Documentar os KPIs no perfil do APO ou em documento dedicado.
	- [ ] Desenvolver conteúdo para `TPL_PRPT_APO_DefinirKPI.md`.
	- [ ] Desenvolver conteúdo para `TPL_PRPT_APO_AnalisarDadosTrend.md`.
	- [ ] Desenvolver conteúdo para `TPL_PRPT_APO_FormularHipoteseOtimizacao.md`.
	- [ ] Coletar/Resumir artigos sobre Product Analytics para [[rag_infra/source_documents/Analytics_Knowledge/]].
	- [ ] Coletar/Resumir material sobre Métricas de SaaS para [[rag_infra/source_documents/SaaS_Metrics_Knowledge/]].
- [ ] **Arquitetura: Detalhamento LLDs para Módulos do MVP** (Pós-Validação dos Passos Críticos) \ #arquitetura \ #documentacao `@AgenteMentorArquitetoLLD` `@Maestro`
	- [ ] Para `LLD_Modulo_Auth.md`: detalhar modelos de dados, classes, fluxos de autenticação.
	- [ ] Para `LLD_Modulo_Kanban.md`: detalhar estruturas de dados, lógica de manipulação de cards/colunas.
	- [ ] Para `LLD_Modulo_CV.md`: detalhar processos de upload, parsing e armazenamento de CVs.
	- [ ] Para `LLD_Modulo_Coach.md`: detalhar interações do chatbot, lógica de proatividade.
	- [ ] Para `LLD_Modulo_Pagamentos.md`: detalhar integração com gateway, gerenciamento de assinaturas.
- [ ] **IA Agentes - Documentação da Arquitetura do Sistema Multiagente** \ #ia \ #agente \ #arquitetura \ #documentacao `@Maestro` `@AgenteMentorArquitetoHLD` `@AgenteMentorDocumentacao`
	- [ ] Criar diagramas (ex: C 4 Model Nível 2 ou 3) para ilustrar componentes e interações.
	- [ ] Descrever fluxos de dados e de controle entre os agentes e o RAG/MCPs.
- [ ] **Criação de Perfis Detalhados para Agentes Futuros Prioritários** \ #ia \ #agente \ #documentacao \ #futuro `@Maestro` `@AgenteOrquestrador`
	- [ ] Selecionar 1-2 agentes da lista de "Agentes Futuros" (ex: `@AgenteMentorDados`) com base no roadmap pós-MVP.
	- [ ] Utilizar o [[docs/04_Agentes_IA/Templates_Modelos/TEMPLATE_PERFIL_AGENTE.md]] (tendo como base o perfil do `@AgenteOrquestrador`) para criar seus perfis detalhados.
- [ ] **API: Desenvolvimento das Especificações OpenAPI 3.0 (`RecolocaAPI_v1_OpenAPI.yaml`)** \ #api \ #arquitetura \ #documentacao `@AgenteMentorAPI` `@Maestro`
	- [ ] Definir todos os endpoints necessários para o MVP.
	- [ ] Para cada endpoint, detalhar métodos HTTP, parâmetros, request/response bodies e schemas.
	- [ ] Incluir definições de segurança (ex: JWT).
- [ ] Pesquisar sobre **BugBot** (Cursor Like) \ #Bug \ @Maestro
- [ ] **QA/Testes: Definição da Abordagem para Testes com IA** \ #qa \ #ia \ #estrategia `@AgenteMentorQA` `@Maestro`
	- [ ] Pesquisar e definir estratégias para testar funcionalidades que dependem de LLMs (ex: Otimização de CV, Coach IA).
	- [ ] Como definir oráculos de teste? Como lidar com a não-deterministicidade?
- [ ] **QA/Testes - Estratégia para Sistema Multiagente** \ #ia \ #agente \ #qa \ #estrategia `@Maestro` `@AgenteMentorQA`
	- [ ] Definir como testar o comportamento de agentes individuais.
	- [ ] Definir como testar a orquestração e a comunicação entre agentes.
	- [ ] Definir como testar a integração dos agentes com o RAG e outras ferramentas MCP.
- [ ] **Ambiente Dev/Deploy - Configuração Inicial e Esboço de CI/CD** \ #devops \ #infra `@Maestro` `@AgenteMentorDevOps`
	- [ ] Criar repositórios Git para frontend, backend, e possivelmente para MCPs.
	- [ ] Configurar linters, formatters e hooks de pré-commit.
	- [ ] Esboçar um pipeline de CI básico (build, test) para backend e frontend.
	- [ ] Esboçar um pipeline de CD básico para deploy em Vercel/Render.
- [ ] **Gerenciamento: Planejar 1ª Sprint de Desenvolvimento do MVP** (Pós-Validação dos Passos Críticos) \ #gerenciamento `@Maestro`
	- [ ] Selecionar HUs para a 1ª Sprint.
	- [ ] Estimar esforço (story points ou tempo).
	- [ ] Definir a meta da Sprint.
- [ ] **Configuração Ferramentas - Pipedream (Setup Inicial)** \ #configuracao \ #devops `@Maestro`
	- [ ] Criar conta no Pipedream (plano gratuito).
	- [ ] Explorar a interface e criar um workflow simples de teste (ex: notificação por email em trigger HTTP).
- [ ] **Desenvolvimento Feature - Contas e Autenticação (Core)** \ #desenvolvimento \ #feature \ #core \ #auth `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-AUTH-001` a `RF-AUTH-012`.
	- [ ] Implementar frontend para `RF-AUTH-001` a `RF-AUTH-012`.
- [ ] **Desenvolvimento Feature - Pagamentos (Core)** \ #desenvolvimento \ #feature \ #core \ #pagamento `@AgenteMentorDevFastAPI` `@Maestro`
	- [ ] Configurar Gateway de Pagamento.
	- [ ] Implementar Lógica de Assinaturas Freemium (`RF-PAY-SUB-001` a `RF-PAY-SUB-004`).
- [ ] **Desenvolvimento Feature - Kanban (Core)** \ #desenvolvimento \ #feature \ #core \ #kanban `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-KAN-001` a `RF-KAN-007`.
	- [ ] Implementar frontend para `RF-KAN-001` a `RF-KAN-007`.
	- [ ] Realizar testes de integração.
- [ ] **Desenvolvimento Feature - Importação de Vagas (Core)** \ #desenvolvimento \ #feature \ #core \ #ia \ #importacao `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-IMP-001`, `RF-IMP-002`.
	- [ ] Implementar frontend para `RF-IMP-001`, `RF-IMP-002`.
	- [ ] Testar integração com LLM para parsing.
- [ ] **Pesquisa/Definição: Ferramentas de Parsing PDF Alternativas** \ #pesquisa \ #tecnico `@Maestro`
	- [ ] Avaliar eficácia de `pymupdf` / `Tesseract` para `RF-CV-001`.
	- [ ] Se necessário, pesquisar e listar alternativas.
	- [ ] Realizar PoC (Prova de Conceito) com a melhor alternativa, se aplicável.
- [ ] **Desenvolvimento Feature - Otimização CV (Upload e Parsing)** \ #desenvolvimento \ #feature \ #core \ #cv `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para `RF-CV-001`, `RF-CV-002`.
	- [ ] Implementar frontend para `RF-CV-001`, `RF-CV-002`.
	- [ ] Integrar e testar ferramenta de parsing de PDF.
- [ ] **Desenvolvimento Feature - Otimização CV (Análise IA)** \ #desenvolvimento \ #feature \ #core \ #ia \ #cv `@AgenteMentorDevFastAPI` `@Maestro`
	- [ ] Implementar backend para Análise Vaga-CV (Score IA) (`RF-CV-003`).
	- [ ] Implementar backend para Sugestões de Otimização (`RF-CV-004`).
	- [ ] Implementar backend para Estimativa Salarial (`RF-CV-005`).
- [ ] **Desenvolvimento Feature - Otimização CV (Output e Versionamento)** \ #desenvolvimento \ #feature \ #core \ #cv `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para download PDF otimizado (`RF-CV-006`).
	- [ ] Implementar backend para gerenciamento de versões de CV (`RF-CV-007`).
	- [ ] Implementar frontend correspondente.
- [ ] **Infra/DevOps: Estratégia Detalhada de Monitoramento e Logging** \ #infra \ #devops `@AgenteMentorDevOps` `@Maestro`
	- [ ] Pesquisar e selecionar ferramentas (ex: Sentry, Better Uptime, Logtail) para `RNF-REL-003`.
	- [ ] Definir quais métricas e logs chave serão monitorados para backend, frontend e serviços.
	- [ ] Esboçar arquitetura de logging e monitoramento.
- [ ] **Desenvolvimento Feature - Coach IA (Core)** \ #desenvolvimento \ #feature \ #core \ #ia \ #coach `@AgenteMentorDevFastAPI` `@AgenteMentorDevFlutter` `@Maestro`
	- [ ] Implementar backend para Chatbot básico (`RF-COACH-001`).
	- [ ] Implementar lógica de atuação proativa (`RF-COACH-002`, `RF-COACH-003`).
	- [ ] Implementar backend para orientações (`RF-COACH-004`).
	- [ ] Implementar frontend para interação com Coach IA.
- [ ] **Desenvolvimento Pós-MVP - Extensão Chrome Web Clipper** \ #pos_mvp \ #desenvolvimento \ #extensao `@AgenteMentorDevJS` `@Maestro`
	- [ ] Detalhar requisitos técnicos da extensão (`RF-IMP-003`).
	- [ ] Desenvolver Manifest V 3 e scripts de conteúdo/background.
	- [ ] Implementar UI da extensão e comunicação com API backend.
- [ ] **Planeamento Estratégico Pós-MVP (Recoloca. AI e Sistema Multiagente)** \ #estrategia \ #roadmap \ #pos_mvp `@Maestro` `@AgenteOrquestrador`
	- [ ] Definir o roadmap de funcionalidades para o Recoloca. AI para os próximos 6-12 meses pós-MVP.
	- [ ] Identificar e priorizar quais novos agentes ou capacidades de agentes serão necessários para suportar o roadmap.
	- [ ] Planear a evolução da infraestrutura RAG/MCP com base nas necessidades futuras.
- [ ] **Legal: Documentação Jurídica (Pré-Lançamento Público)** \ #legal \ #prioridade \ #media `@Maestro` `@AgenteMentorLegal`
	- [ ] Elaborar primeira versão dos Termos de Uso.
	- [ ] Elaborar primeira versão da Política de Privacidade.
	- [ ] Submeter para validação jurídica especializada.


## 🎯 A Fazer

- [ ] **Análise Estratégica: Consistência da Documentação Core** \ #estrategia \ #documentacao \ #validacao \ #prioridade_alta \ `@AgenteOrquestrador` `@Maestro`
	- [ ] Verificar alinhamento e sinergia entre [[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]], [[docs/02_Requisitos/ERS.md]], e [[docs/03_Arquitetura_Solucao/HLD.md]].
	- [ ] Identificar e listar potenciais desalinhamentos, lacunas ou pontos que necessitem de esclarecimento/refinamento.
	- [ ] Propor atualizações nos documentos, se necessário, para garantir coesão estratégica.
- [ ] **Finalização e Operacionalização Inicial** do ``@AgenteOrquestrador`` (v 1.0)\ #ia_agente \ #orquestracao \ #configuracao \ #prioridade_alta \ `@Maestro` `@AgenteOrquestrador`
	- [ ] **(Revisão/Consolidação):** Refinar e validar o perfil completo do ``@AgenteOrquestrador`` em [[docs/04_Agentes_IA/Perfis/@AgenteOrquestrador.md]], com foco especial no "Prompt Base Inicial" e nas "Instruções Fundamentais", garantindo que os valores e pesos para sua atuação como assistente principal estejam claros.
	- [ ] **(Revisão/Consolidação):** Configurar o ``@AgenteOrquestrador`` no Trae IDE, inserindo o Prompt Base refinado e definindo as ferramentas iniciais que ele poderá acessar.
	- [ ] **(Nova):** Realizar testes de interação com o ``@AgenteOrquestrador`` (aqui com Gemini) utilizando a "Documentação Viva" como base de referência, focando em:
		- Capacidade de seguir o tom de voz e persona.
		- Compreensão e aplicação das `project_rules. Md` e `user_rules. Md`.
		- Habilidade de decompor problemas e sugerir próximos passos.
	- [ ] **(Nova):** Definir e documentar um fluxo de trabalho inicial de como você (Maestro) e o ``@AgenteOrquestrador`` colaborarão para avançar as próximas tarefas do projeto (ex: refinar ERS, planear sprints, co-criar prompts para outros agentes).
- [ ] **Operacionalização do Sistema RAG** (v 1.0) para Consumo pelo ``@AgenteOrquestrador`` \ #ia_agente \ #rag \ #mcp \ #desenvolvimento \ #prioridade_alta `@Maestro` `@AgenteMentorDevFastAPI` `@AgenteMentorDevOps`
	- [ ] **(Revisão/Consolidação):** Concluir o desenvolvimento e testes unitários/integração do servidor MCP para o RAG (conforme a tarefa "RAG - Design e Implementação do Servidor MCP" já existente, focando em torná-lo funcional).
	- [ ] **(Revisão/Consolidação):** Realizar a indexação inicial dos documentos chave da "Documentação Viva" (ex: ERS, Plano Mestre, Perfis de Agentes, Guias Centrais) para o RAG.
	- [ ] **(Nova):** Configurar a ferramenta RAG-MCP no Trae IDE e associá-la como uma ferramenta disponível para o ``@AgenteOrquestrador``.
	- [ ] **(Nova):** Instruir explicitamente o ``@AgenteOrquestrador`` (via prompt ou interação) sobre como e quando utilizar a ferramenta RAG para consultar a "Documentação Viva" de forma eficiente.
	- [ ] **(Nova):** Realizar testes de ponta a ponta: ``@AgenteOrquestrador`` recebendo uma tarefa do Maestro, identificando a necessidade de consultar a documentação, utilizando a ferramenta RAG-MCP para obter chunks de dados, e utilizando esses chunks para formular uma resposta ou plano de ação.
	- [ ] **(Revisão/Consolidação):** Validar a qualidade dos chunks recuperados pelo RAG e a capacidade do ``@AgenteOrquestrador`` de sintetizá-los efetivamente.
- [ ] **Validação Técnica: Protótipo RLS FastAPI/Supabase** (ERS Seção 6.1) \ #tecnico \ #validacao \ #prioridade \ #alta \ #risco_alto `@Maestro` `@AgenteMentorDevFastAPI` `@AgenteMentorSeguranca`
	- [ ] Configurar tabelas e políticas RLS no Supabase para um cenário de teste.
	- [ ] Desenvolver endpoints FastAPI mínimos para testar o acesso RLS.
	- [ ] Validar a segurança e funcionalidade do RLS.
- [ ] **IA Agentes - Prompts Base e Ferramentas para Squad Principal** \ #ia \ #agente \ #prompt_engineering \ #configuracao \ #prioridade_media `@Maestro` `@AgenteOrquestrador`
	- [ ] Para cada agente do squad principal, revisar e refinar seu "Prompt Base Inicial" (nos perfis individuais em [[docs/04_Agentes_IA/Perfis/]]).
	- [ ] Para cada agente, listar explicitamente as ferramentas MCP que ele precisaria (ex: RAG, APIs específicas, outros agentes).
	- [ ] Estabelecer e documentar o processo de co-criação de prompts para agentes especializados, com base no [[01_Guias_Centrais/GUIA_AVANCADO.md]] e nas capacidades definidas no [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]].
- [ ] Pesquisar sobre: **AG-UI: The Agent-User Interaction Protocol** #pesquisa #multi_agente
- [ ] **IA Agentes - Orquestração (``@AgenteOrquestrador``) - Projeto Detalhado** \ #ia \ #agente \ #orquestracao \ #arquitetura `@Maestro` `@AgenteOrquestrador`
	- [ ] Detalhar o processo de decomposição de tarefas.
	- [ ] Mapear quais agentes-ferramenta (MCPs) são chamados para quais tipos de subtarefas.
	- [ ] Definir como o estado da tarefa é mantido durante a orquestração (se necessário).
- [ ] **RAG - Design e Implementação do Servidor MCP** \ #ia \ #agente \ #rag \ #mcp \ #desenvolvimento `@Maestro` `@AgenteMentorDevFastAPI`
	- [ ] Desenhar a especificação da API do servidor MCP para o RAG (endpoints, formato de request/response).
	- [ ] Implementar a lógica do servidor em Python, expondo o retriever LangChain/FAISS.
	- [ ] Criar Dockerfile para o servidor MCP (se aplicável).
	- [ ] Realizar testes unitários e de integração do servidor MCP.
	- [ ] Configurar este servidor como uma ferramenta no Trae IDE e testar com um agente.
- [ ] **IA Agentes - Setup Trae IDE (Configuração Detalhada Agentes)**: \ #ia \ #agente \ #configuracao \ #prioridade_media `@Maestro`
	- [ ] Configurar o Agente ``@AgenteMentorPO`` no Trae IDE.
	- [ ] Configurar os demais agentes do Squad Principal no Trae IDE progressivamente, conforme forem sendo detalhados e necessitarem de operacionalização.
- [ ] **IA Agentes - Elaboração Detalhada de Regras (`project_rules. Md`, `user_rules. Md`)** \ #ia \ #agente \ #configuracao \ #documentacao `@Maestro` `@AgenteOrquestrador`
	- [ ] Popular `project_rules. Md` com padrões de codificação, segurança, documentação, etc.
	- [ ] Popular `user_rules. Md` com preferências do Maestro.
	- [ ] Definir como os agentes serão instruídos a consultar e seguir estas regras.
- [ ] **IA Agentes - Orquestração (``@AgenteOrquestrador``) - Implementação e Teste** \ #ia \ #agente \ #orquestracao \ #desenvolvimento `@Maestro` `@AgenteOrquestrador`
	- [ ] Escrever e refinar o prompt de sistema avançado para o ``@AgenteOrquestrador``.
	- [ ] Desenvolver/Configurar os servidores MCP para os agentes-membro a serem orquestrados.
	- [ ] Testar cenários de orquestração com 2-3 agentes.
- [ ] **RAG - Otimização e Processos de Manutenção** \ #ia \ #agente \ #rag \ #operacoes `@Maestro` `@AgenteMentorDevOps`
	- [ ] Realizar testes de carga e stress no retriever RAG para identificar gargalos.
	- [ ] Desenvolver script ou processo para reindexar la "Documentação Viva" automaticamente ou sob demanda.
	- [ ] Documentar o processo de manutenção e atualização do RAG.
- [ ] **IA Agentes - Gerenciamento de Segredos para MCPs** \ #ia \ #agente \ #mcp \ #seguranca `@Maestro` `@AgenteMentorSeguranca`
	- [ ] Pesquisar e selecionar a abordagem de gerenciamento de segredos (ex: HashiCorp Vault, variáveis de ambiente injetadas de forma segura no deploy do MCP).
	- [ ] Implementar la solução escolhida para o servidor RAG-MCP e outros MCPs futuros.
	- [ ] Documentar o procedimento de forma segura.
- [ ] **RAG - Criação e Curadoria de Conteúdo para Bases de Conhecimento** \ #ia \ #agente \ #rag \ #conteudo `@Maestro` `@AgenteOrquestrador`
	- [ ] Desenvolver estratégia e processo para identificar, curar e formatar documentos para as bases de conhecimento (ex: `Analytics_Knowledge`, `SaaS_Metrics_Knowledge`).
	- [ ] Processar e adicionar os primeiros lotes de documentos a estas bases.
- [ ] **RAG/Dados: Coleta de Fontes para Estimativa Salarial** \ #ia \ #agente \ #dados \ #pesquisa `@Maestro` `@AgenteMentorDados`
	- [ ] Identificar fontes de dados abertas ou acessíveis sobre salários de TI no Brasil (para `RF-CV-005`).
	- [ ] Coletar e pré-processar os dados para inclusão no RAG ou modelo específico.
- [ ] **Avaliação Contínua e Documentação de Limitações/Soluções de Contorno (Trae IDE e Ferramentas)** \ #aprendizagem \ #trae_ide \ #documentacao `@Maestro`
	- [ ] Manter um log de desafios encontrados e soluções aplicadas.
	- [ ] Documentar formalmente em ADRs ou secção de "Lições Aprendidas".
- [ ] **Protótipo Funcional do Recoloca. AI com Squad de IA (Slice Vertical)** \ #desenvolvimento \ #validacao \ #mvp `@Maestro` `@AgenteOrquestrador`
	- [ ] Selecionar uma User Story completa e pequena do MVP.
	- [ ] Executar o ciclo de vida completo (requisitos, design, dev (simulado/real), teste) usando os agentes de IA para assistir/executar cada etapa.
	- [ ] Documentar o processo e os resultados.
- [ ] **Desenvolvimento do "Playbook de Projeto Baseado em Agentes de IA" (Estrutura Reutilizável)** \ #metodologia \ #documentacao \ #reutilizavel `@Maestro` `@AgenteMentorDocumentacao`
	- [ ] Estruturar o índice do Playbook.
	- [ ] Documentar o processo de setup inicial do ambiente (Obsidian, Trae, RAG básico).
	- [ ] Detalhar o fluxo de trabalho com o ``@AgenteOrquestrador`` e o "Squad de IA".
	- [ ] Adicionar templates chave (perfil de agente, ADR, etc.).
	- [ ] Registrar aprendizados e melhores práticas.


## ⚙️ Em Andamento

- [ ] **Planejamento e Estratégia do Produto (MVP) - Alinhamento Inicial** \ #produto \ #estrategia \ #requisitos \ #prioridade_alta \ `@Maestro` `@AgenteOrquestrador` `@AgenteMentorPO`
	- [ ] Revisão detalhada e colaborativa do [[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] para consolidar entendimento da visão, objetivos, fases e prioridades do MVP.
	- [ ] Revisão detalhada e colaborativa do [[docs/02_Requisitos/ERS.md]] (v 0.5) com foco no escopo do MVP.
	- [ ] Identificar e discutir explicitamente os "componentes de núcleo" do projeto com base no Plano Mestre e ERS.
	- [ ] Aplicar framework de priorização (ex: RICE, MoSCoW) para as funcionalidades candidatas ao MVP, documentando as decisões.
	- [ ] Definir e documentar a lista final de funcionalidades priorizadas para o MVP.
	- [ ] Criar 2-3 User Personas detalhadas, alinhadas com o público-alvo do MVP.
	- [ ] Mapear a Jornada do Usuário principal para cada Persona no contexto das funcionalidades do MVP.
	- [ ] Validar internamente (Maestro e Agentes) as Personas e Jornadas criadas.
	- [ ] Pesquisar modelos de monetização e value proposition para produtos SaaS Freemium no nicho de carreira/IA.
	- [ ] Esboçar/Revisar o Lean Canvas (ou Business Model Canvas) para o Recoloca. AI, focando no MVP.


## 🧐 Validação/Revisão



## ✅ Concluído

- [ ] **Configuração Ferramentas - Ambientes de Desenvolvimento Locais** \ #configuracao \ #tecnico `@Maestro`
	- [x] Garantir instalação e configuração de Python e gerenciador de pacotes. ✅ 2025-06-05
	- [x] Garantir instalação e configuração do FastAPI e dependências. ✅ 2025-06-05
	- [x] Garantir instalação e configuração do Node. Js (para futuro dev JS). ✅ 2025-06-05
	- [x] Garantir instalação e configuração do Flutter SDK. ✅ 2025-06-05
- [x] **Pesquisa:** Realizar "Deep Research" (Mercado, Solução, MVP, Approach) `@Maestro` @Gemini 📅 2025-05-29
- [x] **Documentação:** Atualizar [[docs/02_Requisitos/ERS.md]] para v 0.5 `@Maestro` @Gemini 📅 2025-05-29
- [x] **Documentação:** Atualizar [[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] para v 1.3 `@Maestro` @Gemini 📅 2025-05-29
- [x] **Documentação:** Atualizar [[01_Guias_Centrais/GUIA_AVANCADO.md]] para v 2.1 `@Maestro` @Gemini 📅 2025-05-29
- [x] **Versionamento:** Fazer Commit dos 3 Guias Centrais no Git (ERS v 0.5, PM v 1.3, GA v 2.1) `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Obsidian:** Vault configurado para o projeto Recoloca. Ai `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Obsidian:** Estrutura de pastas criada (conforme Plano Mestre) `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Obsidian:** Plugin "Kanban" instalado e configurado `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Obsidian:** Plugin "Obsidian Git" instalado e configurado `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Git & GitHub/GitLab:** Repositório local inicializado `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Git & GitHub/GitLab:** Repositório remoto criado e conectado `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Trae IDE:** Instalado e configurado `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - Trae IDE:** Conexão com OpenRouter (ou APIs Gemini) estabelecida `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - OpenRouter (ou Google AI Studio):** Conta criada e chaves de API geradas `@Maestro` 📅 2025-05-29
- [x] **Configuração Ferramentas - VS Code:** IDE com extensões relevantes configurado `@Maestro` 📅 2025-05-29
- [x] **IA Agentes - Setup Trae IDE (v 1.0):** Refinar ` [[.trae/rules/user_rules.md]] ` e ` [[.trae/rules/project_rules.md]] ` para Agentes de IA \ #ia \ #agente \ #configuracao `@Maestro` ✅ 2025-06-04
- [x] **IA Agentes - Estrutura Documentação:** Definir e criar estrutura de pastas para Perfis de Agentes no Obsidian (`docs/04_Agentes_IA/Perfis/`, `Templates_Modelos/`) `@Maestro` @Gemini 📅 2025-06-04
- [x] **IA Agentes - Documentação Overview:** Criar e refinar ` [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]] ` (v 1.6) `@Maestro` @Gemini 📅 2025-06-04
- [x] **IA Agentes - Perfil APO:** Criar e refinar perfil (` [[docs/04_Agentes_IA/Perfis/@AgenteAnalistaPerformanceOtimizacao.md]] ` v 1.4) `@Maestro` @Gemini 📅 2025-06-04
- [x] **IA Agentes - Nomenclatura Prompts:** Definir e revisar convenção de nomenclatura para templates e prompts específicos (ex: `TPL_PRPT_`, `PRPT_`) `@Maestro` @Gemini 📅 2025-06-04
- [x] **IA Agentes - Template Perfil:** Definir estrutura para ` [[docs/04_Agentes_IA/Templates_Modelos/TEMPLATE_PERFIL_AGENTE.md]] ` `@Maestro` @Gemini 📅 2025-06-04
- [x] **Documentação Viva - Consolidação Inicial (Realizada pelo Maestro):** \ #documentacao \ #organizacao `@Maestro` 📅 2025-06-04
	- [x] Copiar conteúdo do artefacto `agentes_ia_overview_v 1` (v 1.6) para ` [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]] `. ✅ 2025-06-04
	- [x] Copiar conteúdo do artefacto `perfil_agente_apo_v 1` (v 1.4) para ` [[docs/04_Agentes_IA/Perfis/@AgenteAnalistaPerformanceOtimizacao.md]] `. ✅ 2025-06-04
	- [x] Popular os perfis individuais dos restantes agentes com conteúdo do `AGENTES_IA_MENTORES. Md` original, ajustando links e adicionando secção "Biblioteca de Prompts". ✅ 2025-06-04
	- [x] Renomear ficheiros de templates de prompt em ` [[docs/05_Prompts/01_Templates_Base/]] `. ✅ 2025-06-04
	- [x] Renomear/criar ficheiros de prompts específicos em ` [[docs/05_Prompts/02_Prompts_Especificos/]] `. ✅ 2025-06-04
	- [x] Criar/Atualizar ` [[docs/04_Agentes_IA/Templates_Modelos/TEMPLATE_PERFIL_AGENTE.md]] `. ✅ 2025-06-04




%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[null,false,false,true,false],"move-tags":true,"move-dates":true,"show-relative-date":true,"inline-metadata-position":"body","move-task-metadata":false,"show-checkboxes":false,"new-card-insertion-method":"prepend","full-list-lane-width":false,"lane-width":400,"append-archive-date":true}
```
%%