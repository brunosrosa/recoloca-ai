---
sticker: lucide//check
---
# GUIA AVANÇADO PARA DESENVOLVIMENTO SOLO COM AGENTES DE IA MENTORES (Aplicado ao Projeto Recoloca.ai)

**Versão:** 2.3
**Data de Criação:** 28 de maio de 2025
**Data de Última Atualização:** 03 de junho de 2025
**Baseado em:**
- [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5)
- [[docs/02_Requisitos/ERS.md]] (v0.5)
- [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.2 - este documento, versão anterior)
## Seção 1: Introdução – A Nova Fronteira do Desenvolvimento Solo com Mentoria de IA

### 1.1. O Paradigma do Desenvolvimento Solo Aumentado por IA

O desenvolvimento de software está em um ponto de inflexão, impulsionado pela ascensão da Inteligência Artificial (IA). Para o desenvolvedor solo, essa era não representa uma ameaça, mas uma **oportunidade sem precedentes** de amplificar suas capacidades, transcender limitações tradicionais e construir produtos sofisticados de forma independente. Este guia reinterpreta os princípios da colaboração homem-máquina, adaptando-os à realidade do **desenvolvedor individual que atua como "Maestro"** de uma orquestra de Agentes de IA especializados.

No contexto do projeto **Recoloca.ai**, um Micro-SaaS para auxiliar profissionais brasileiros na recolocação, esta abordagem não é apenas uma escolha metodológica, mas uma **necessidade estratégica**. A IA deixa de ser uma mera ferramenta de codificação para se tornar um conjunto de **mentores e assistentes qualificados**, engajados em todas as fases do Ciclo de Vida de Desenvolvimento de Software (SDLC).
### 1.2. Propósito e Escopo deste Guia

Este documento é a **pedra angular metodológica** para o desenvolvimento do Recoloca.ai. Seu propósito é detalhar o framework de "Desenvolvimento Solo Ágil Aumentado por IA", o papel do desenvolvedor "Maestro", a arquitetura e interação dos Agentes de IA Mentores (com ênfase no papel estratégico do `@AgenteOrquestrador`), as ferramentas e tecnologias chave, e as estratégias de **Retrieval Augmented Generation (RAG)** e **Human-in-the-Loop (HITL)**.

Enquanto o [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] define o "o quê" e o "quando" do projeto, este guia foca no "**porquê**" e no "**como**" metodológico, utilizando o Recoloca.ai como o principal estudo de caso e campo de aplicação.
### 1.3. O Projeto Recoloca.ai como Campo de Provas

O **Recoloca.ai**, conforme detalhado na [[docs/02_Requisitos/ERS.md]] (v0.5), visa oferecer:

1.  **Gerenciamento Inteligente de Candidaturas (Kanban)**
2.  **Otimização de Currículos Potencializada por IA**
3.  **Assistente de IA para Coaching e Suporte Contextualizado**

Desenvolvido com **Flutter (PWA)**, **Python/FastAPI (Backend)**, **Supabase (DB/Auth)** e **Google Gemini (Pro/Flash via OpenRouter)**, o projeto apresenta desafios inerentes ao desenvolvimento solo, como a amplitude da stack e a complexidade das funcionalidades de IA (ex: parsing de PDF, análise semântica, importação de vagas via link com LLM). Este guia demonstrará como a mentoria de IA pode mitigar esses desafios.
## Seção 2: O Framework de Desenvolvimento Solo Aumentado por IA

### 2.1. Princípios Fundamentais

O modelo "Desenvolvimento Solo Ágil Aumentado por IA" se baseia nos seguintes pilares:

-   **Maestro e Orquestra de IA:** O desenvolvedor solo ("Maestro") lidera e coordena Agentes de IA especializados ("Mentores").
-   **IA como Multiplicador de Força:** A IA automatiza tarefas, acelera o desenvolvimento e atua como um "sparring partner" intelectual.
-   **Foco no Estratégico e Criativo:** O Maestro se concentra em atividades de maior valor agregado, delegando tarefas operacionais e de análise inicial aos agentes.
-   **Mentoria Especializada e Estratégica:** Agentes de IA atuam como consultores virtuais em diversas áreas, complementando as habilidades do Maestro. O `@AgenteOrquestrador` assume um papel de "PM Mentor".
-   **Documentação Viva e RAG:** A documentação do projeto, mantida no **Obsidian** e versionada com **Git**, serve como a "fonte da verdade" e alimenta um sistema RAG para fornecer contexto dinâmico aos agentes.
-   **HITL Evolutivo:** Um processo de Human-in-the-Loop que se adapta à confiança e ao desempenho dos agentes, equilibrando supervisão e autonomia.
-   **Adaptação Neurodivergente:** A metodologia e as ferramentas são escolhidas para se alinhar com as características de um desenvolvedor com TDAH/AHSD, promovendo foco e produtividade sustentável.
### 2.2. O Papel do Desenvolvedor "Maestro"

Conforme detalhado no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 2.2), o Maestro é responsável por:

-   Definir a **visão estratégica** e priorizar o backlog, com o apoio consultivo do `@AgenteOrquestrador`.
-   **Orquestrar os Agentes de IA Mentores**, projetando e refinando prompts, com o `@AgenteOrquestrador` atuando como principal assistente nessa tarefa.
-   **Supervisionar, validar e refinar** o output da IA (HITL).
-   Tomar **decisões arquiteturais** e de design críticas.
-   Desenvolver **componentes complexos** e realizar integrações críticas.
-   Gerenciar a **"Documentação Viva"** e a base de conhecimento RAG.
-   **Aprender e evoluir continuamente** na colaboração com a IA.
-   Manter o foco no **valor para o usuário** e nos objetivos de negócio.
-   Gerenciar o próprio **fluxo de trabalho e energia**.
### 2.3. O SDLC Ágil Adaptado

O Ciclo de Vida de Desenvolvimento de Software (SDLC) Ágil é adaptado para integrar intensivamente os Agentes de IA Mentores, conforme descrito no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 2.3). A interação inicial com o `@AgenteOrquestrador` para refinar a estratégia e o escopo da tarefa é um passo fundamental antes da delegação aos agentes especializados. O fluxo geral é:

1.  **Concepção e Refinamento de Ideias/Requisitos:**
    -   Maestro identifica necessidades/oportunidades ou refina itens do backlog.
    -   Interação com `@AgenteOrquestrador` para validar a estratégia da ideia/requisito sob a ótica de Product Management.
    -   `@AgenteMentorPO` auxilia na tradução para Histórias de Usuário (HUs) e Critérios de Aceite (ACs) a partir da [[docs/02_Requisitos/ERS.md]] e insights do Maestro/`@AgenteOrquestrador`.
    -   Maestro valida e refina HUs/ACs.
2.  **Design (HLD/LLD/API/UX/UI):**
    -   Maestro define diretrizes de design.
    -   `@AgenteMentorArquitetoHLD`, `@AgenteMentorArquitetoLLD`, `@AgenteMentorAPI`, `@AgenteMentorUIDesign`, `@AgenteMentorUX` auxiliam na criação de artefatos de design (diagramas, especificações, mockups conceituais, fluxos), com o `@AgenteOrquestrador` facilitando a comunicação e o contexto.
    -   Maestro valida, itera e aprova os designs.
3.  **Desenvolvimento (Codificação):**
    -   `@AgentesMentoresDev` (Flutter, FastAPI), guiados pelo `@AgenteOrquestrador` e pelos LLDs/APIs, geram código boilerplate, componentes e lógica de negócios.
    -   Maestro revisa, depura, refatora, integra e implementa partes críticas ou que exigem codificação manual. O `@AgenteMentorDevJS` atuará em Pós-MVP para a extensão.
4.  **Testes e Garantia de Qualidade:**
    -   `@AgenteMentorQA` auxilia na geração de planos de teste, casos de teste (Gherkin) e scripts de testes unitários/integração.
    -   Maestro implementa/supervisiona testes E2E, revisa a cobertura e valida a qualidade.
5.  **Documentação Contínua:**
    -   `@AgenteMentorDocumentacao` auxilia na geração de comentários, docstrings e na manutenção da "Documentação Viva" no Obsidian.
    -   Maestro garante que todas as decisões e implementações sejam documentadas.
6.  **Deploy e Operações (DevOps):**
    -   `@AgenteM_DevOps` (conceitual, implementado via scripts e **Pipedream**) auxilia na automação de CI/CD para Vercel, Render e Supabase.
    -   Maestro supervisiona e gerencia a infraestrutura e os processos de deploy.
7.  **Monitoramento, Feedback e Iteração:**
    -   Coleta de feedback do usuário (pós-MVP) e métricas de uso.
    -   Análise de feedback e métricas para identificar melhorias e novas funcionalidades, alimentando o backlog.
    -   O sistema RAG é continuamente atualizado com novos aprendizados e documentação, refinando o conhecimento dos agentes.
    -   O ciclo recomeça.
## Seção 3: O Agente Orquestrador de Prompts e Mentor de Product Management

### 3.1. A Necessidade de um Orquestrador e Mentor Estratégico para o Maestro

Para o "Maestro" que gerencia uma equipe de Agentes de IA e, simultaneamente, atua como o principal Product Manager, a **clareza estratégica e a precisão da comunicação são primordiais**. O **`@AgenteOrquestrador`** (implementado como um agente customizado no **Trae IDE**) transcende a função de um simples "engenheiro de prompt assistente". Ele atua como o **primeiro mentor e principal "sparring partner" estratégico do Maestro**, auxiliando-o a:

1.  **Refinar o pensamento estratégico de Product Management:** Antes de formular prompts para outros agentes, o `@AgenteOrquestrador` ajuda o Maestro a validar a estratégia da feature, o alinhamento com os objetivos do produto, a proposta de valor para o usuário e a consideração de métricas de sucesso.
2.  **Formular instruções otimizadas para os demais agentes:** Garante que os prompts sejam claros, contextualmente ricos e alinhados com a visão estratégica co-criada.

Ele é a ponte entre a "Documentação Viva" (acessada via RAG), as ideias e a visão estratégica do Maestro, e as capacidades dos outros Agentes Mentores.
### 3.2. Funcionalidades e Persona do `@AgenteOrquestrador` como PM Mentor

Conforme delineado no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 3.1) e expandido aqui:

-   **Persona no Trae IDE:** `@AgenteOrquestrador`
-   **Papel Principal:** "Product Manager Mentor Sênior e Engenheiro de Prompt Especialista".
-   **Objetivo:**
    1.  Auxiliar o Maestro a aplicar consistentemente os princípios de Product Management (descoberta, estratégia, priorização, definição de valor) ao longo do ciclo de vida do Recoloca.ai.
    2.  Auxiliar o Maestro a formular instruções (prompts) claras, precisas, contextualmente ricas e otimizadas para os outros Agentes Mentores.
-   **Funcionalidades Detalhadas:**
    1.  **Análise** da Documentação Estratégica e Tática (via RAG): Processa e "compreende" documentos chave do projeto (ex: [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]], [[docs/02_Requisitos/ERS.md]], [[docs/03_Arquitetura_e_Design/HLD.md]]) e, se disponível no RAG, materiais sobre Product Management (frameworks, artigos) para extrair contexto.
    2.  **Geração de Perguntas Estratégicas e Esclarecedoras (com viés de PM):** Antes de focar no prompt para um agente executor, formula perguntas ao Maestro para:
        -   Validar o "porquê" da feature/tarefa.
        -   Clarificar o problema do usuário que está sendo resolvido.
        -   Identificar a Proposta Única de Valor (UVP) relacionada.
        -   Considerar métricas de sucesso e KPIs.
        -   Analisar possíveis riscos e dependências.
        -   Sugerir frameworks de priorização (RICE, ICE, etc.) quando aplicável.
    3.  **Criação Assistida de Prompts Eficazes:** Após o diálogo estratégico com o Maestro, auxilia na montagem de prompts detalhados e estruturados para os agentes de destino, incorporando o contexto estratégico validado, referências diretas à documentação, sugerindo técnicas de engenharia de prompt (Zero-Shot, Few-Shot, Chain-of-Thought) e utilizando os templates de [[docs/05_Prompts/01_Templates_Base/]].
### 3.3. Interação e Implementação no Trae IDE

-   O `@AgenteOrquestrador` é um agente customizado no Trae IDE, com um prompt base que define suas funções de PM Mentor e Engenheiro de Prompt, tom de voz colaborativo, questionador e proativo.
-   Utiliza a capacidade do Trae IDE de acessar o contexto do projeto e se integra ao sistema RAG (que incluirá materiais de PM).
-   O Maestro interage com ele em um fluxo conversacional para:
    1.  **Primeiro,** validar **e refinar a estratégia e o escopo da tarefa/feature** sob a ótica de Product Management.
    2.  **Segundo, co-criar o prompt otimizado** para o agente executor.
-   As regras de interação e comportamento são também definidas em [[.trae/rules/user_rules.md]] e [[.trae/rules/project_rules.md]].

Este agente não apenas traduz, mas **desafia e refina a visão estratégica e os requisitos** ao forçar uma análise mais profunda, atuando como um "tutor de Product Management e engenharia de prompt" para o Maestro.
## Seção 4: Arquitetura de Agentes de IA Mentores no SDLC Ágil Solo

A metodologia se apoia em um conjunto de Agentes de IA Mentores especializados, configurados no **Trae IDE** e acessando modelos **Google Gemini Pro/Flash** via **OpenRouter**. Cada agente possui uma persona, habilidades (definidas por prompt base e regras em [[.trae/rules/project_rules.md]]) e utiliza templates de [[docs/05_Prompts/01_Templates_Base/]]. O RAG fornece o contexto específico do projeto.

A referência primária para seus papéis é a **Tabela Essencial** (ver Apêndice B) e o detalhamento no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 3.2).
### 4.1. Agentes por Fase do SDLC (Resumo Alinhado com ERS v0.5 e Plano Mestre v1.5)

-   `@AgenteM_PO` **(Product Owner):**
    -   **Foco:** Definição e Refinamento de Requisitos Táticos.
    -   **Tarefas:** Gerar HUs (em [[docs/02_Requisitos/HU_AC/]]) e ACs a partir da [[docs/02_Requisitos/ERS.md]] (v0.5), após alinhamento estratégico com o Maestro e o `@AgenteOrquestrador`. **Deve ser instruído a considerar o contexto estratégico fornecido pelo `@AgenteOrquestrador`**.
-   `@AgenteM_ArquitetoHLD` **(Arquiteto de Software - HLD):**
    -   **Foco:** Design de Alto Nível.
    -   **Tarefas:** Criar/otimizar [[docs/03_Arquitetura_e_Design/HLD.md]], gerar diagramas de arquitetura (Mermaid.js).
-   `@AgenteM_ArquitetoLLD` **(Arquiteto/Designer de Software - LLD):**
    -   **Foco:** Design de Baixo Nível.
    -   **Tarefas:** Detalhar classes, funções, modelos de dados em [[docs/03_Arquitetura_e_Design/LLD/]], diagramas de sequência/classes (Mermaid.js).
-   `@AgenteM_API` **(Arquiteto de APIs):**
    -   **Foco:** Especificação de APIs.
    -   **Tarefas:** Gerar/manter especificações OpenAPI 3.0 (ex: [[docs/03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]).
-   `@AgenteM_DevFastAPI` **(Desenvolvedor Python/FastAPI):**
    -   **Foco:** Desenvolvimento Backend.
    -   **Tarefas:** Gerar código Python/FastAPI, interações com Supabase, testes unitários (pytest).
-   `@AgenteM_DevFlutter` **(Desenvolvedor Flutter/Dart):**
    -   **Foco:** Desenvolvimento Frontend (PWA).
    -   **Tarefas:** Criar widgets, lógica de UI, gerenciamento de estado (Provider/Riverpod), chamadas à API, testes.
-   `@AgenteM_DevJS` **(Desenvolvedor de Extensão Chrome - Pós-MVP):**
    -   **Foco:** Desenvolvimento da Extensão.
    -   **Tarefas:** Lógica de extração de dados, comunicação com backend, UI da extensão.
-   `@AgenteM_QA` **(Analista de QA/Testes):**
    -   **Foco:** Garantia de Qualidade.
    -   **Tarefas:** Gerar planos de teste ([[docs/06_Qualidade_e_Testes/PGQ.md]]), casos de teste (Gherkin em [[docs/06_Qualidade_e_Testes/Casos_de_Teste/]]), scripts de testes.
-   `@AgenteM_Seguranca` **(Analista de Segurança):**
    -   **Foco:** Segurança de Código e Arquitetura.
    -   **Tarefas:** Revisar código e design, instruir sobre práticas seguras (OWASP Top 10, OWASP LLM Top 10, LGPD).
-   `@AgenteM_Documentacao` **(Documentador Técnico):**
    -   **Foco:** Documentação de Código e "Documentação Viva".
    -   **Tarefas:** Gerar comentários/docstrings, auxiliar na manutenção da "Documentação Viva" e curadoria da base RAG ([[rag_infra/souce_documents/]]).
### 4.2. Interação e Colaboração entre Agentes

O `@AgenteOrquestrador` é o ponto central para iniciar a maioria das interações complexas. Ele garante que o contexto estratégico e os requisitos estejam bem definidos antes de passar a tarefa (ou o prompt preparado) para um agente especialista. A "Documentação Viva" e o RAG continuam sendo a base de conhecimento compartilhada. Os agentes podem, em cenários mais avançados e sob supervisão do Maestro, interagir entre si (ex: `@AgenteMentorDevFastAPI` solicitando clarificações da especificação OpenAPI ao `@AgenteMentorAPI` através do `@AgenteOrquestrador`).
## Seção 5: Mantendo os Agentes Afiados e o Conhecimento Fluido (RAG, Ferramentas)

Para que os Agentes de IA Mentores sejam eficazes, eles precisam de acesso a informações atualizadas e contextualmente relevantes. Isso é alcançado através de uma combinação de **Retrieval Augmented Generation (RAG)**, uma **"Documentação Viva"** bem mantida, e o uso estratégico de ferramentas.
### 5.1. A Estratégia RAG do Recoloca.ai

Conforme detalhado no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 5.1), o sistema RAG é crucial para fornecer contexto específico do projeto aos LLMs.

-   **Base de Conhecimento:** Documentos Markdown do projeto (ERS, Plano Mestre, HLD, LLDs, este Guia, etc.) armazenados em [[rag_infra/souce_documents/]].
    -   **Base de Conhecimento Adicional para `@AgenteOrquestrador`:** Incluir artigos, resumos de livros e frameworks de Product Management em [[rag_infra/souce_documents/PM_Knowledge/]].
-   **Tecnologias:**
    -   **Framework:** **LangChain** (Python) para orquestrar o pipeline RAG.
    -   **Vector Store:** **FAISS** para uma implementação local e eficiente. Considerar Supabase pgvector como evolução Pós-MVP.
    -   **Embedding Model:** O modelo **`BAAI/bge-m3`** foi o escolhido. Ele é um modelo de embedding multilíngue e de alto desempenho, acessível via Hugging Face e compatível com Sentence Transformers. Sua capacidade de lidar com múltiplos idiomas e a qualidade dos embeddings gerados são vantajosas para o contexto do Recoloca.ai, que pode evoluir para diferentes cenários de linguagem.
-   **Processo de Indexação:** Um script ([[rag_infra/core_logic/rag_indexer.py]]) monitora alterações na base de conhecimento, carrega, divide em chunks, gera embeddings e atualiza o índice FAISS.
-   **Processo de Consulta:** Agentes no Trae IDE, via `@AgenteOrquestrador` ou diretamente, consultam o RAG. A consulta é convertida em embedding, busca os chunks mais relevantes, e estes são injetados no prompt do LLM.
-   **Benefícios:** Melhora a precisão, reduz alucinações e fornece acesso a informações atuais e específicas do domínio do Recoloca.ai, incluindo conhecimento estratégico de Product Management para o `@AgenteOrquestrador`.
### 5.2. "Documentação Viva": Obsidian e Git como Pilares

A "Documentação Viva" é o coração da gestão de conhecimento do projeto.

-   **Ferramenta Central:** **Obsidian**, para criar, organizar e interligar toda a documentação. Sua capacidade de linking e a interface limpa são ideais para manter um "segundo cérebro" digital.
-   **Controle de Versão:** **Git** (repositório no GitHub ou GitLab), com o vault do Obsidian sendo versionado. O plugin "Obsidian Git" facilita commits, pushes e pulls diretamente da interface do Obsidian, garantindo rastreabilidade e a capacidade de reverter alterações.
-   **Atualização Contínua:** A documentação é um artefato dinâmico, não um entregável estático. O `@AgenteMentorDocumentacao` auxilia na geração e manutenção, e o Maestro é o curador final, responsável por garantir que todas as decisões, aprendizados e alterações no projeto sejam refletidos na documentação de forma precisa e tempestiva.
-   **Estrutura:** Organizada conforme [[Apêndice A: Estrutura das Pastas]] para facilitar a navegação, a descoberta de informações e o processamento eficiente pelo sistema RAG.
### 5.3. Ferramentas de Suporte e Integração

-   **Trae IDE:** Ambiente central para codificação e interação com os Agentes Mentores. Suas "Rules" ([[.trae/rules/user_rules.md]], [[.trae/rules/project_rules.md]]) customizam o comportamento dos agentes, permitindo ao Maestro refinar suas especializações e diretrizes operacionais.
-   **OpenRouter:** Gateway para acesso flexível e gerenciado aos modelos Gemini (Pro e Flash). Permite testar diferentes modelos, otimizar custos e evitar vendor lock-in com um único provedor de LLM.
-   **Pipedream:** Plataforma de automação para CI/CD (deploy em Vercel/Render), gatilhos para reindexar o RAG em commits na documentação, notificações por email ou Slack, e outras automações de fluxo de trabalho que podem surgir.
-   **FlutterFlow:** Opcional, para prototipagem rápida de UI pelo `@AgenteMentorDevFlutter` ou Maestro. Pode acelerar a criação de mockups interativos ou gerar código Flutter base para telas menos complexas.

A combinação dessas ferramentas e estratégias garante que os Agentes de IA operem com o máximo de informação relevante, mantendo-se "afiados" e alinhados com a evolução do projeto Recoloca.ai.
## Seção 6: Convenções de Gerenciamento de Tarefas com Kanban

### 6.1. Sistema de Identificação de Tarefas (IDs)

Para garantir organização, rastreabilidade e facilitar a comunicação entre o Maestro e os Agentes de IA, todas as tarefas no [[docs/00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]] seguem um sistema estruturado de identificação:

**Formato:** `[TIPO-DOMÍNIO-###]`

#### 6.1.1. Tipos de Atividade (TIPO)

- **EST** - Estratégia: Atividades de planejamento estratégico, definição de roadmap, análise de mercado
- **REQ** - Requisitos: Elaboração e refinamento de requisitos, HUs, ACs
- **ARC** - Arquitetura: Design de alto nível (HLD), baixo nível (LLD), decisões arquiteturais
- **UXD** - UX/UI Design: Design de experiência do usuário, interfaces, mockups, protótipos
- **DEV** - Desenvolvimento: Codificação, implementação de features, correções de bugs
- **QAT** - Qualidade e Testes: Testes unitários, integração, E2E, estratégias de QA
- **DOC** - Documentação: Criação e manutenção da documentação viva, comentários de código
- **IMP** - Implementação de Infraestrutura: RAG, agentes, ferramentas, automações
- **VAL** - Validação: Pesquisas com usuários, testes de usabilidade, validação de hipóteses
- **ENV** - Ambiente e Deploy: Configuração de ambientes, CI/CD, infraestrutura
- **MNG** - Gerenciamento: Atividades de gestão de projeto, planejamento de sprints
- **CFG** - Configuração: Setup inicial de ferramentas, configurações de desenvolvimento
- **PES** - Pesquisa: Investigação de tecnologias, análise de concorrentes, estudos de mercado
- **AGT** - Agentes: Criação, refinamento e operacionalização de agentes de IA
- **API** - APIs: Especificação, documentação e refinamento de APIs
- **INF** - Infraestrutura: Monitoramento, logging, performance
- **PRO** - Protótipo: Desenvolvimento de protótipos e provas de conceito

#### 6.1.2. Domínios de Aplicação (DOMÍNIO)

- **GER** - Geral/Transversal: Atividades que afetam todo o projeto
- **KAN** - Módulo Kanban: Funcionalidades do sistema de gerenciamento de candidaturas
- **AUTH** - Módulo de Autenticação: Sistema de login, registro, segurança
- **CV** - Módulo de Otimização de CV: Parsing, análise e otimização de currículos
- **COA** - Módulo Coach IA: Assistente inteligente e coaching
- **PAY** - Módulo de Pagamentos: Sistema de cobrança e assinaturas
- **IMP** - Módulo de Importação: Importação de vagas via links
- **RAG** - Sistema RAG: Retrieval Augmented Generation
- **AGT** - Agentes de IA: Configuração e operação dos agentes mentores
- **UX** - Experiência do Usuário: Design e usabilidade transversal
- **TEC** - Técnico: Aspectos técnicos transversais
- **NEG** - Negócio: Estratégia de negócio e monetização
- **VAL** - Validação: Testes com usuários e validação de mercado
- **DEV** - Desenvolvimento: Aspectos gerais de desenvolvimento
- **SPR** - Sprint: Planejamento e gestão de sprints
- **FER** - Ferramentas: Pesquisa e configuração de ferramentas
- **PLA** - Planejamento: Atividades de planejamento estratégico
- **PRF** - Perfis: Criação e refinamento de perfis de agentes
- **ARC** - Arquitetura: Documentação e decisões arquiteturais
- **FUT** - Futuro: Planejamento de features pós-MVP
- **JUR** - Jurídico: Aspectos legais e conformidade (LGPD)
- **CFG** - Configuração: Setup e configuração de ferramentas
- **MCP** - MCPs: Model Context Protocol e integrações
- **DAT** - Dados: Coleta e processamento de dados
- **PRO** - Protótipo: Desenvolvimento de protótipos
- **PLA** - Playbook: Documentação de processos e metodologias

#### 6.1.3. Numeração Sequencial (###)

- Numeração sequencial de 001 a 999 dentro de cada combinação TIPO-DOMÍNIO
- Permite até 999 tarefas por categoria, suficiente para o escopo do projeto

### 6.2. Estados e Fluxo de Trabalho

#### 6.2.1. Estados das Tarefas

- **[ ]** - **A Fazer**: Tarefa identificada e priorizada, aguardando início
- **[x]** - **Concluída**: Tarefa finalizada e validada pelo Maestro

#### 6.2.2. Fluxo de Estados

1. **Criação**: Nova tarefa é adicionada com status "A Fazer" [ ]
2. **Execução**: Maestro trabalha na tarefa (pode envolver agentes de IA)
3. **Validação**: Maestro revisa e valida o resultado
4. **Conclusão**: Tarefa marcada como concluída [x]

### 6.3. Priorização e Organização

#### 6.3.1. Critérios de Priorização

1. **Dependências**: Tarefas que desbloqueiam outras têm prioridade
2. **Valor para o MVP**: Funcionalidades core do MVP têm precedência
3. **Risco**: Tarefas com maior incerteza técnica são priorizadas para validação antecipada
4. **Esforço vs. Impacto**: Aplicação de frameworks como RICE quando necessário

#### 6.3.2. Organização no Arquivo

- **Tarefas A Fazer**: Organizadas por prioridade (mais prioritárias no topo)
- **Tarefas Concluídas**: Mantidas no final do arquivo para histórico
- **Agrupamento**: Tarefas relacionadas podem ser agrupadas com sub-itens quando apropriado

### 6.4. Integração com Agentes de IA

#### 6.4.1. Referenciamento em Prompts

Ao interagir com agentes de IA, sempre referencie o ID da tarefa:
- "Trabalhando na tarefa **[DEV-KAN-001]** - Desenvolvimento do Módulo Kanban..."
- "Esta implementação refere-se ao **[IMP-RAG-001]** - RAG - Operacionalização..."

#### 6.4.2. Contexto para o @AgenteOrquestrador

O `@AgenteOrquestrador` deve:
- Consultar o Kanban via RAG para entender prioridades atuais
- Questionar alinhamento de novas ideias com tarefas priorizadas
- Sugerir criação de novos IDs quando necessário
- Auxiliar na decomposição de tarefas grandes em sub-tarefas

### 6.5. Sincronização com Plugin Obsidian Kanban

#### 6.5.1. Configuração do Plugin

- **Arquivo Base**: [[docs/00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]]
- **Colunas**: "A Fazer" e "Concluído" (mapeadas para [ ] e [x])
- **Filtros**: Possibilidade de filtrar por TIPO ou DOMÍNIO usando tags

#### 6.5.2. Manutenção da Consistência

- Alterações no plugin devem ser refletidas no arquivo Markdown
- Commits regulares para versionamento das mudanças no Kanban
- Backup automático via Obsidian Git plugin

### 6.6. Métricas e Acompanhamento

#### 6.6.1. Métricas de Produtividade

- **Velocity**: Número de tarefas concluídas por período
- **Lead Time**: Tempo médio entre criação e conclusão de tarefas
- **Distribuição por Tipo**: Análise de onde o tempo está sendo investido

#### 6.6.2. Análise de Padrões

- Identificação de gargalos por domínio ou tipo de atividade
- Análise de dependências críticas
- Evolução da complexidade das tarefas ao longo do tempo

### 6.7. Evolução e Refinamento

Este sistema de convenções é vivo e deve evoluir conforme as necessidades do projeto:

- **Novos Tipos/Domínios**: Podem ser adicionados conforme necessário
- **Refinamento de Critérios**: Priorização pode ser ajustada com base na experiência
- **Automações**: Futuras integrações podem automatizar parte do processo
- **Feedback dos Agentes**: Insights dos agentes de IA podem sugerir melhorias

A manutenção dessas convenções garante que o Kanban permaneça uma ferramenta eficaz de gestão e comunicação, tanto para o Maestro quanto para os Agentes de IA Mentores.
## Seção 7: O Processo de Human-in-the-Loop (HITL) Evolutivo

O **Human-in-the-Loop (HITL)** é um componente não negociável desta metodologia, garantindo qualidade, segurança, alinhamento ético e aprendizado contínuo tanto para o Maestro quanto para os Agentes de IA. Conforme descrito no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 6.2), o processo HITL evoluirá em fases:
### 7.1. Fase 1: Supervisão Intensa e Detalhada

-   **Aplicabilidade:** MVP Inicial, novas funcionalidades críticas, ou quando um agente é usado para uma tarefa inédita ou de alta complexidade.
-   **Descrição:** O Maestro revisa minuciosamente **todo o output significativo** dos Agentes de IA (HUs, ACs, diagramas, especificações de API, blocos de código > X linhas, casos de teste críticos, etc.). A revisão não é apenas sobre correção, mas sobre entendimento do "raciocínio" do agente.
-   **Foco:** Validação rigorosa da correção, alinhamento com os requisitos e a estratégia, identificação de padrões de erro dos agentes, e aprendizado sobre como otimizar prompts e refinar as regras dos agentes.
-   **Critérios de Confiança:** Baixa a média confiança inicial no agente para a tarefa específica.
-   **Feedback para Agentes:** Detalhado e estruturado, explicando correções, o porquê das alterações, e sugerindo melhorias no processo de geração do agente. Este feedback é crucial para "treinar" implicitamente os agentes (refinando seus prompts base, templates ou as regras no Trae IDE).
### 6.2. Fase 2: Autonomia Guiada e Revisão por Amostragem

-   **Aplicabilidade:** Funcionalidades maduras, tarefas repetitivas onde os agentes já demonstraram um bom nível de proficiência e consistência.
-   **Descrição:** O Maestro foca a revisão detalhada em áreas de **maior risco, complexidade ou impacto no usuário**. Para tarefas onde os agentes são consistentemente confiáveis (ex: gerar CRUD básico a partir de um LLD claro e testado), a revisão pode ser por amostragem ou focada em pontos chave (ex: segurança, performance, integração).
-   **Foco:** Eficiência na delegação, manutenção da qualidade com menor sobrecarga de revisão, monitoramento de métricas de desempenho dos agentes (ex: taxa de retrabalho, tempo para conclusão da tarefa).
-   **Critérios de Confiança:** Média a alta confiança em agentes específicos para tarefas bem definidas e com histórico de sucesso.
-   **Feedback para Agentes:** Focado em exceções, otimizações ou melhorias incrementais. O Maestro pode começar a identificar padrões de sucesso que podem ser incorporados em novos templates de prompt ou regras.
### 6.3. Fase 3: Controle Supervisor e Foco Estratégico

-   **Aplicabilidade:** Ideal de longo prazo, com agentes e sistema RAG altamente maduros e confiáveis.
-   **Descrição:** O Maestro atua mais como um **revisor final de alto nível** (arquitetura global, UX, estratégia de produto) e tomador de decisões estratégicas. Agentes operam com maior autonomia em domínios onde são consistentemente confiáveis, com sistemas de alerta para anomalias, baixa confiança na geração ou desvios de padrões.
-   **Foco:** Inovação, pesquisa de novas tecnologias, estratégia de produto de longo prazo, e mentoria de alto nível para os agentes (refinando suas "especializações" e a base de conhecimento RAG).
-   **Critérios de Confiança:** Alta confiança, baseada em histórico de desempenho robusto e métricas de qualidade consistentes. O sistema RAG está maduro e a base de conhecimento é abrangente e precisa.
-   **Feedback para Agentes:** Focado em refinar a base RAG com conhecimento de ponta, ajustar regras de alto nível dos agentes, e explorar novas formas de colaboração.

O feedback fornecido pelo Maestro durante o HITL é crucial para o **refinamento contínuo** dos [[docs/05_Prompts/01_Templates_Base/]], das regras em [[.trae/rules/]], e da base RAG. É um ciclo de aprendizado mútuo.
## Seção 8: Considerações para o Desenvolvedor Solo Neurodivergente

A metodologia de "Desenvolvimento Solo Ágil Aumentado por IA" foi concebida levando em consideração as características de um desenvolvedor **neurodivergente**, especificamente com **TDAH (Transtorno do Déficit de Atenção com Hiperatividade)** e **Altas Habilidades/Superdotação (AH/SD)** – um perfil também conhecido como Dupla Excepcionalidade (2e). O objetivo é criar um ambiente de trabalho que potencialize os pontos fortes e mitigue os desafios associados.
### 8.1. Alinhando a Metodologia com o Perfil Neurodivergente

-   **Hiperfoco e Variedade:** A alternância entre papéis (Maestro, executor, estrategista, revisor) e a interação com múltiplos Agentes de IA especializados em diferentes domínios oferece a variedade e o nível de estímulo que podem engajar o hiperfoco de forma produtiva.
-   **Estrutura e Clareza Externa:**
    -   A **"Documentação Viva" no Obsidian**, com seus links e estrutura visual, serve como um "segundo cérebro" confiável, ajudando a organizar pensamentos e a rastrear informações.
    -   O **`@AgenteOrquestrador`**, especialmente com seu papel de PM Mentor, auxilia na quebra de tarefas complexas em partes menores e mais gerenciáveis, e na manutenção do foco estratégico.
    -   O **Kanban no Obsidian** ([[docs/00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]]) oferece uma visualização clara do progresso e das prioridades, reduzindo a sobrecarga mental de ter que lembrar de todas as tarefas.
-   **Redução de Tarefas Monótonas e Repetitivas:** A delegação de tarefas como geração de boilerplate, documentação inicial ou testes básicos para os Agentes de IA libera o Maestro para se concentrar em aspectos mais desafiadores e interessantes do projeto.
-   **Feedback Imediato e Iteração Rápida:** A capacidade de obter respostas e resultados rápidos dos Agentes de IA pode manter o engajamento e a motivação, características importantes para quem tem TDAH.
-   **Estímulo Intelectual e Resolução de Problemas Complexos:** A colaboração com IA, a engenharia de prompt, o design de sistemas de agentes e a resolução de problemas complexos inerentes ao projeto são altamente estimulantes para mentes com AH/SD.
### 8.2. Ferramentas e Técnicas de Suporte

-   **Obsidian:** Além da organização, a capacidade de customização com plugins (Kanban, Git, Dataview, etc.) permite adaptar a ferramenta às preferências individuais de fluxo de trabalho.
-   **Trae IDE:** A configuração de Agentes customizados e "Rules" permite que o Maestro molde o comportamento da IA para melhor se adequar ao seu estilo de pensamento e necessidades.
-   **Pipedream:** A automação de fluxos de trabalho reduz a necessidade de lembrar e executar manualmente tarefas rotineiras de CI/CD ou manutenção do RAG.
-   **Técnicas de Gerenciamento de Tempo:** O uso consciente de técnicas como Pomodoro, time blocking (com o Kanban como base para definir os blocos) e a definição de metas claras para cada sessão de trabalho podem ajudar a gerenciar o foco e a energia.
-   **Minimização de Distrações:** O ambiente de desenvolvimento solo, combinado com interações estruturadas e focadas com os agentes (em vez de interrupções imprevisíveis de uma equipe humana), pode ser benéfico.
### 8.3. O Papel da IA como Suporte Executivo e Estratégico

Para o desenvolvedor com desafios nas funções executivas (planejamento, organização, iniciação de tarefas, memória de trabalho), a IA pode oferecer um suporte valioso:

-   `@AgenteOrquestrador`: Ajuda no **planejamento estratégico inicial**, na **quebra de features complexas em tarefas menores e mais gerenciáveis**, na manutenção do alinhamento com os objetivos do produto, e pode até mesmo ser configurado para fornecer "lembretes" ou "check-ins" sobre o progresso de tarefas delegadas ou prioridades.
-   `@AgenteMentorPO`: Auxilia na manutenção da perspectiva do usuário e na priorização tática das funcionalidades, garantindo que o trabalho esteja sempre focado no que entrega mais valor.
-   `@AgenteMentorDocumentacao`: Reduz a carga da tarefa de documentar, que pode ser um desafio para a manutenção do foco, garantindo que o conhecimento não se perca.

Ao reconhecer e integrar proativamente as necessidades do perfil neurodivergente, o objetivo é criar um sistema de desenvolvimento **produtivo, sustentável e gratificante**, onde a IA não apenas aumenta a capacidade técnica, mas também apoia o bem-estar e a eficácia do Maestro.
## Seção 9: Conclusão e Recomendações Metodológicas

O "Guia Avançado para Desenvolvimento Solo com Agentes de IA Mentores", aplicado ao projeto Recoloca.ai, representa uma **abordagem inovadora e pragmática**. Ao posicionar o desenvolvedor como um **"Maestro"** e os Agentes de IA como **"Mentores"** (com o `@AgenteOrquestrador` atuando como um PM Mentor chave), esta metodologia visa amplificar as capacidades humanas de forma holística.
### 9.1. Síntese dos Benefícios

-   **Aumento de Produtividade:** Automação de tarefas repetitivas e aceleração do desenvolvimento.
-   **Ampliação de Expertise:** Acesso a "especialistas virtuais" em diversas áreas, incluindo estratégia de produto.
-   **Melhoria da Qualidade:** Processos HITL robustos e revisão por IA podem identificar problemas mais cedo.
-   **Foco** no Valor **Agregado:** O Maestro se concentra em aspectos estratégicos, criativos e de alto impacto.
-   **Gestão de Conhecimento Eficaz:** A "Documentação Viva" e o sistema RAG garantem que o conhecimento seja preservado e utilizado.
-   **Desenvolvimento Sustentável e Adaptado:** A metodologia considera e busca apoiar as características do desenvolvedor solo, incluindo o perfil neurodivergente.
### 9.2. Recomendações Chave para o Maestro do Recoloca.ai

1.  **Abrace a Iteração Contínua:** Tanto o software quanto a metodologia de colaboração com a IA devem evoluir com base nos aprendizados.
2.  **Invista na Engenharia de Prompt e na Curadoria do `@AgenteOrquestrador`:** A clareza, o contexto estratégico e a qualidade dos prompts são cruciais. O `@AgenteOrquestrador` é seu principal aliado nisso.
3.  **Mantenha a "Documentação Viva" Realmente Viva:** A precisão e a atualização da base RAG são essenciais para a eficácia dos agentes.
4.  **Seja um Curador Ativo e Exigente do HITL:** Sua supervisão e feedback são insubstituíveis para garantir qualidade e direcionamento.
5.  **Cultive a Parceria com a IA:** Encare os agentes como colaboradores e mentores, aprendendo com suas capacidades e limitações.
6.  **Priorize a Segurança e a Ética:** Especialmente com dados de usuários e o uso responsável da IA.
7.  **Cuide da Sua Energia e Foco:** Utilize a metodologia e as ferramentas para criar um ambiente de trabalho que respeite seus ritmos e maximize seu potencial.

O sucesso do Recoloca.ai reside na **sinergia eficaz entre a inteligência humana e a artificial**, com o Maestro conduzindo a orquestra com visão estratégica e discernimento.
## Apêndice A: Estrutura das Pastas (Referência)

A organização da "Documentação Viva" no Obsidian é crucial para a gestão do conhecimento, a eficiência do sistema RAG e a clareza para o Maestro e os Agentes de IA. A estrutura base do vault `Recoloca.AI`.
Ela está detalhada no [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] e replicada aqui para referência rápida (pode haver pequenas variações conforme a evolução do projeto):

```
Recoloca.AI/
├── .git/ # Diretório do Git (gerenciado pelo sistema)
├── .obsidian/ # Configurações do Obsidian (gerenciado pelo Obsidian)
├── .trae/ # Configurações do Trae IDE
│ └── rules/
│ ├── user_rules.md # Regras de IA de nível de usuário/preferências
│ └── project_rules.md # Regras de IA específicas do projeto Recoloca.ai
├── docs/ # Documentação principal do projeto
│ ├── 00_Gerenciamento_Projeto/
│ │ ├── KANBAN_INTERNO_PROJETO.md # Kanban principal do projeto
│ │ ├── TAP.md # Termo de Abertura do Projeto
│ │ ├── PGE.md # Plano de Gerenciamento do Projeto
│ │ ├── PGP.md # Plano de Gerenciamento do Escopo
│ │ ├── PGR.md # Plano de Gerenciamento de Riscos
│ │ ├── PGC.md # Plano de Gerenciamento de Custos (Pós-MVP)
│ │ ├── PGQ_Doc.md # Plano de Gerenciamento da Qualidade (Documento, PGQ.md em 06_ é o plano de testes)
│ │ ├── PCom.md # Plano de Gerenciamento das Comunicações
│ │ └── PStakeholders.md # Plano de Gerenciamento dos Stakeholders (inicialmente, o Maestro)
│ ├── 01_Guias_Centrais/
│ │ ├── PLANO_MESTRE_RECOLOCA_AI.md # Documento estratégico central
│ │ ├── GUIA_AVANCADO.md # Metodologia de Dev Solo com IA (este doc)
│ │ └── GLOSSARIO_Recoloca_AI.md # Termos e definições do projeto
│ ├── 02_Requisitos/
│ │ ├── ERS.md # Especificação de Requisitos de Software
│ │ └── HU_AC/ # Histórias de Usuário e Critérios de Aceite
│ │ └── HU_Exemplo_RF-ABC.md # Exemplo ou arquivos de HUs
│ ├── 03_Arquitetura_e_Design/
│ │ ├── HLD.md # High-Level Design da Arquitetura
│ │ ├── LLD/ # Low-Level Design por módulo
│ │ │ ├── LLD_Modulo_Auth.md
│ │ │ ├── LLD_Modulo_Kanban.md
│ │ │ ├── LLD_Modulo_CV.md
│ │ │ ├── LLD_Modulo_Coach.md
│ │ │ └── LLD_Modulo_Pagamentos.md
│ │ ├── API_Specs/
│ │ │ └── RecolocaAPI_v1_OpenAPI.yaml # Especificação da API Backend
│ │ ├── STYLE_GUIDE.md # Guia de Estilo Visual e de UX Writing
│ │ ├── ADR/ # Registros de Decisão Arquitetural
│ │ │ └── ADR_001_Ferramentas_Core.md # Exemplo de ADR
│ │ └── FLUXO_TRABALHO_GERAL.md # Diagrama do fluxo de desenvolvimento
│ ├── 04_Agentes_IA/
│ │ └── AGENTES_IA_MENTORES.md # Descrição das personas e papéis dos agentes
│ ├── 05_Prompts/
│ │ ├── 01_Templates_Base/ # Templates genéricos de prompts
│ │ │ ├── TPL_Gerar_HU_AC.md
│ │ │ └── (Outros templates .md)
│ │ └── 02_Prompts_Especificos/ # Prompts complexos e reutilizáveis
│ │ └── PRM_Exemplo_Refinamento_Requisito.md
│ ├── 06_Qualidade_e_Testes/
│ │ ├── PGQ.md # Plano de Garantia de Qualidade (foco em Testes)
│ │ └── Casos_de_Teste/
│ │ ├── CT_Autenticacao.md
│ │ └── (Outros casos de teste em Gherkin)
│ ├── 07_Operacoes_e_Deploy/
│ │ ├── GUIA_DEPLOY_FRONTEND.md
│ │ ├── GUIA_DEPLOY_BACKEND.md
│ │ └── GUIA_DEPLOY_EXTENSAO.md (Pós-MVP)
│ └── 09_Pesquisa_e_Insights/ # Notas de pesquisa, artigos, etc.
├── rag_infra/ # Arquivos base da infra do RAG para Agentes
│ └── core_logic/ # Scripts base da infra do RAG
│ │ └── rag_indexer.py
│ │ └── rag_retriever.py
│ │ └── verifica_faiss_gpu.py
│ └── index_store/ # Index criado para o RAG
│ │ └── Index (?)
│ └── notebooks/ # ???
│ │ └── (arquivos de notebooks?)
│ └── source_documents/ # Documentos base para o RAG
│ │ └── GUIA_AVANCADO_para_RAG.md 
│ │ └── API_Specs_Sumario_para_RAG.md
│ │ └── ERS_para_RAG.md
│ │ └── HLD_para_RAG.md
│ │ └── STYLE_GUIDE_para_RAG.md
│ │ └── PM_Knowledge/ # Pasta com documentos para o Agente PM (Product Manager)
│ │ │ └── (arquivos diversos)
│ └── environment.yml # Definição do Ambiente de RAG exportado do Conda
├── logs/ # Logs gerados por scripts ou processos (se aplicável localmente)
│ └── (arquivos de log)
├── scripts/ # Scripts de automação do projeto
│ └── (arquivos de scripts)
├── src/ # Código-fonte da aplicação
│ ├── backend_fastapi/ # Código do backend em FastAPI
│ ├── frontend_flutter/ # Código do frontend PWA em Flutter
│ └── chrome_extension_js/ # Código da extensão Chrome (Pós-MVP)
└── README.md # README principal do projeto (no Git)
```
## Apêndice B: Tabela Essencial - Papéis dos Agentes Mentores de IA

Esta tabela resume os Agentes de IA Mentores. A principal mudança é o papel expandido do `@AgenteOrquestrador`.

| **Fase do SDLC Ágil** | **Agente Mentor de IA (Trae IDE)** | **Principais Tarefas Assistidas para Recoloca.ai** | **Ferramentas/Modelos de IA Chave** | **Contexto RAG Primário** |
| -------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Estratégia e Orquestração** | `@AgenteOrquestrador`              | **Atuar como PM Mentor:** Auxiliar o Maestro a validar estratégia de features, alinhar com objetivos, usar frameworks de PM. **Engenharia de Prompt:** Analisar docs (RAG), gerar perguntas, criar prompts eficazes. | Google Gemini (Pro via OpenRouter), Trae IDE, LangChain/FAISS (via RAG)                       | Toda a "Documentação Viva" (ERS, Plano Mestre, etc.), Materiais de PM em [[rag_infra/souce_documents/PM_Knowledge/]]                        |
| **Definição de Requisitos** | `@AgenteMentorPO`                  | Gerar Histórias de Usuário e Critérios de Aceite (em [[docs/02_Requisitos/HU_AC/]]) a partir da [[docs/02_Requisitos/ERS.md]] (v0.5), **considerando o alinhamento estratégico provido pelo `@AgenteOrquestrador`**.           | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5), Contexto estratégico do `@AgenteOrquestrador`        |
| **Design de Alto Nível (HLD)** | `@AgenteMentorArquitetoHLD`        | Criar/refinar [[docs/03_Arquitetura_e_Design/HLD.md]], diagramas de arquitetura (Mermaid.js), definir interações entre módulos.                                                                                           | Google Gemini (Pro via OpenRouter), Trae IDE, Mermaid.js                                      | [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5)                                                       |
| **Design de Baixo Nível (LLD)** | `@AgenteMentorArquitetoLLD`        | Detalhar classes, funções, modelos de dados para módulos em [[docs/03_Arquitetura_e_Design/LLD/]], diagramas de sequência/classes (Mermaid.js).                                                                           | Google Gemini (Pro via OpenRouter), Trae IDE, Mermaid.js                                      | [[docs/03_Arquitetura_e_Design/HLD.md]], [[docs/02_Requisitos/ERS.md]] (v0.5)                                                                             |
| **Especificação de API** | `@AgenteMentorAPI`                 | Gerar/manter especificações OpenAPI 3.0 (ex: [[docs/03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]).                                                                                                     | Google Gemini (Pro via OpenRouter), Trae IDE                                                  | [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/03_Arquitetura_e_Design/HLD.md]]                                                                             |
| **Desenvolvimento Backend** | `@AgenteMentorDevFastAPI`          | Gerar código Python/FastAPI para endpoints, lógica de negócios, interação com Supabase, testes unitários (pytest).                                                                                                   | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]], [[docs/03_Arquitetura_e_Design/LLD/]], Padrões Seguros                            |
| **Desenvolvimento Frontend** | `@AgenteMentorDevFlutter`          | Criar widgets Flutter/Dart, lógica de UI, gerenciamento de estado (Provider/Riverpod), chamadas à API, testes.                                                                                                       | Google Gemini (Pro/Flash via OpenRouter), Trae IDE, (Opcional: FlutterFlow para prototipagem) | [[docs/03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]], [[docs/03_Arquitetura_e_Design/LLD/]], [[docs/03_Arquitetura_e_Design/STYLE_GUIDE.md]] |
| **Desenvolvimento Extensão (Pós-MVP)** | `@AgenteMentorDevJS`               | Implementar lógica de extração de dados (JS), comunicação com backend, UI da extensão.                                                                                                                               | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/02_Requisitos/ERS.md]] (v0.5 - seção da extensão), [[docs/03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]                          |
| **Testes e QA** | `@AgenteMentorQA`                  | Gerar planos de teste ([[docs/06_Qualidade_e_Testes/PGQ.md]]), casos de teste (Gherkin em [[docs/06_Qualidade_e_Testes/Casos_de_Teste/]]), scripts de testes unitários/integração.                                             | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/02_Requisitos/HU_AC/]], [[docs/03_Arquitetura_e_Design/LLD/]]                                                     |
| **Documentação** | `@AgenteMentorDocumentacao`        | Gerar comentários/docstrings, explicar algoritmos, auxiliar na manutenção da "Documentação Viva" e curadoria da base RAG ([[rag_infra/souce_documents/]]).                                                       | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | Código-fonte, [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/03_Arquitetura_e_Design/HLD.md]], [[docs/03_Arquitetura_e_Design/LLD/]]                             |
| **Segurança** | `@AgenteMentorSeguranca`           | Revisar código e design (OWASP Top 10, OWASP LLM Top 10, LGPD), instruir sobre práticas seguras.                                                                                                                     | Google Gemini (Pro via OpenRouter), Trae IDE                                                  | [[docs/02_Requisitos/ERS.md]] (v0.5 - seção de segurança), Padrões de Código Seguro, Documentação OWASP                                              |
## Apêndice C: Exemplos de Prompts Base para Agentes

Os templates de prompts detalhados e específicos para cada agente e tarefa são gerenciados na pasta [[docs/05_Prompts/01_Templates_Base/]] e [[docs/05_Prompts/02_Prompts_Especificos/]] dentro do vault do Obsidian.

A estrutura geral de um template de prompt (conforme [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] v1.5, Seção 7.2) inclui:

1.  **Metadados:** Agente Alvo, Versão, Objetivo.
2.  **PERSONA DO AGENTE:** Instruções sobre papel, expertise, tom de voz, interação com RAG.
3.  **CONTEXTO FORNECIDO:** Placeholders para links (`[[Arquivo.md#Cabeçalho]]`) e input do Maestro.
4.  **TAREFA DETALHADA:** Descrição passo a passo.
5.  **RESTRIÇÕES E DIRETRIZES:** O que NÃO fazer, padrões, segurança.
6.  **FORMATO DE SAÍDA ESPERADO:** Estrutura, exemplos (few-shot), tipo de artefato.

**Exemplo Conceitual de Interação (Maestro para `@AgenteOrquestrador` com foco em PM):**

**Maestro:** "`@AgenteOrquestrador`, estou considerando o `RF-KAN-005` (Dashboard de Métricas Pessoais) da [[docs/02_Requisitos/ERS.md]] v0.5 para a próxima sprint. Ajude-me a validar a estratégia e depois a preparar o prompt para o `@AgenteMentorPO` gerar as HUs."

`@AgenteOrquestrador` (como PM Mentor, após consulta RAG): "Ótimo, Maestro! O `RF-KAN-005` parece alinhar-se com a dor do usuário sobre 'falta de visibilidade do progresso'. Antes de detalharmos para o `@AgenteMentorPO`:

1.  Qual o **principal Job-To-Be-Done** que este dashboard resolve para o nosso profissional de TI? É 'ajudar-me a entender onde estou falhando para melhorar' ou 'dar-me uma sensação de controle e progresso'? A clareza aqui impactará as métricas prioritárias.
2.  Considerando nossos concorrentes (conforme pesquisa), qual seria o **diferencial chave** do nosso dashboard de métricas? Seria a simplicidade, a profundidade dos insights ou a integração com o Coach IA?
3.  Quais **1-2 métricas de sucesso** para _esta feature específica_ nos indicariam que ela está entregando valor? (Ex: % de usuários que acessam o dashboard semanalmente, ou uma melhoria na taxa de conversão do funil do usuário após X tempo de uso).
4.  Pensando em MVP para este dashboard, quais são as 2-3 métricas absolutamente essenciais que precisamos exibir para validar a hipótese de valor, versus métricas 'nice-to-have' que podem vir depois? (Podemos usar MoSCoW aqui).
    Após alinharmos esses pontos estratégicos, posso ajudá-lo a formular um prompt rico para o @AgenteMentorPO detalhar as HUs e ACs para o MVP deste dashboard."

--- FIM DO DOCUMENTO GUIA_AVANCADO.md (v2.3) ---