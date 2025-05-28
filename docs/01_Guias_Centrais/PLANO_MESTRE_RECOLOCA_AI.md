# PLANO MESTRE DO PROJETO RECOLOCA.AI

**Data de Criação**: 26 de maio de 2025

**Data de Última Atualização**: 28 de maio de 2025

**Versão**: 1.2

**Autor Principal (Maestro)**: Bruno S. Rosa

**Assistência IA:** Gemini (Personalizado para colaboração e co-evolução)

## Sumário Executivo

Este **Plano Mestre** é o documento central e a **fonte da verdade** para o desenvolvimento, manutenção e evolução contínua do projeto **Recoloca.ai**. Ele consolida a visão estratégica, as decisões arquiteturais, o framework de "Desenvolvimento Solo Ágil Aumentado por IA", os fluxos de trabalho detalhados, as ferramentas selecionadas e o roadmap para a construção do Micro-SaaS Recoloca.ai. Este documento é uma **"Documentação Viva"**, mantida e atualizada no Obsidian e versionada com Git, servindo como guia para o desenvolvedor solo ("Maestro") e como base de conhecimento fundamental para seus Agentes de IA Mentores configurados no Trae IDE.

## 1. Introdução ao Recoloca.ai

### 1.1. Visão Geral do Produto e Problema de Mercado

O **Recoloca.ai** é um Micro-SaaS inovador projetado para **transformar** a experiência de recolocação **profissional no Brasil**. O mercado de trabalho atual, especialmente no setor de tecnologia, é dinâmico e competitivo. Profissionais enfrentam desafios significativos como:

- Gerenciamento ineficiente de múltiplas candidaturas.
    
- Dificuldade em adaptar currículos de forma eficaz para cada vaga.
    
- Falta de preparo e confiança para entrevistas.
    
- Sensação de isolamento e falta de orientação durante o processo.
    

O Recoloca.ai visa solucionar essas dores oferecendo uma plataforma integrada que combina **gerenciamento inteligente de candidaturas (Kanban)**, **otimização de currículos potencializada por Inteligência Artificial (IA)** e um **assistente de IA para coaching e suporte contextualizado**. O objetivo é empoderar os profissionais brasileiros, fornecendo ferramentas e orientação para que naveguem pelo processo de recolocação com maior eficiência, estratégia e confiança, aumentando significativamente suas chances de sucesso.

### 1.2. Propósito deste Plano Mestre

Este **Plano Mestre** serve como o **documento fundamental e unificador** para todas as fases do ciclo de vida do Recoloca.ai. Seu propósito é:

- **Consolidar a visão estratégica** e os objetivos de curto, médio e longo prazo do projeto.
    
- **Detalhar** a metodologia **de desenvolvimento** "Solo Ágil Aumentado por IA", adaptada às características do Maestro.
    
- **Definir a arquitetura de Agentes de** IA **Mentores** e sua implementação prática no Trae IDE.
    
- **Especificar a arquitetura técnica**, a stack tecnológica e as ferramentas de desenvolvimento e automação.
    
- **Estabelecer as práticas de gestão de conhecimento** através de uma "Documentação Viva" e um sistema RAG (Retrieval Augmented Generation).
    
- **Delinear os fluxos de trabalho de desenvolvimento**, o modelo de Human-in-the-Loop (HITL) evolutivo e a gestão de tarefas.
    
- **Servir** como guia para a configuração inicial do **ambiente** e como roadmap para o desenvolvimento do MVP e iterações subsequentes.
    

Este documento será a **referência central** para o desenvolvedor "Maestro" e a principal fonte de contexto para os Agentes de IA.

### 1.3. Objetivos e Escopo do MVP (Produto Mínimo Viável)

**Objetivo Principal do MVP:** Validar a proposta de valor central do Recoloca.ai – auxiliar profissionais a gerenciar candidaturas, otimizar currículos com IA e receber coaching básico – focando inicialmente em profissionais de tecnologia no Brasil, e coletar feedback para guiar a evolução do produto.

**Funcionalidades Centrais do MVP (conforme [[02_Requisitos/ERS.md]]):**

1. **Gerenciamento de Candidaturas (Kanban):**
    
    - Captura de vagas via extensão de navegador (Chrome) para LinkedIn e Gupy, com extração automática de dados (Título, Empresa, Link, Descrição, etc.).
        
    - Input manual de vagas.
        
    - Quadro Kanban com colunas fixas para rastreamento visual do status das candidaturas.
        
    - Funcionalidade de drag-and-drop para mover cards.
        
    - Adição de notas (Markdown simples) e prazos aos cards.
        
    - Busca e filtros avançados no Kanban.
        
2. **Otimização de Currículo com IA:**
    
    - Upload do currículo base em PDF (com parsing robusto via pymupdf/Tesseract e categorização semântica por IA).
        
    - Validação e edição obrigatória do conteúdo extraído pelo usuário.
        
    - Análise pela IA (Google Gemini Pro) da descrição da vaga e do "Currículo Ativo" validado.
        
    - Output da IA: Score de Congruência Geral, Relatório Detalhado (pontos fortes, gaps, melhorias), Sub-Scores e Sugestões de Adaptações Contextualizadas.
        
    - Apresentação das sugestões com "antes e depois", permitindo aceitar/editar/rejeitar.
        
    - Download do currículo otimizado em PDF (layout padronizado).
        
    - Gerenciamento do "Currículo Ativo".
        
3. **Acompanhamento e "Coaching" com IA (Chatbot):**
    
    - Interface de chatbot acessível.
        
    - Base de conhecimento curada (via RAG) focada no mercado brasileiro.
        
    - Persona do LLM definida (Animado, inspirador, empático, especialista).
        
    - Dicas contextuais baseadas no status da vaga no Kanban.
        
    - Notificações na plataforma (e push PWA).
        

**Visão de Evolução (Pós-MVP - Breve Menção):**

- **Templates Avançados de Currículo e Customização (Tier Pago):** Conforme RF-CV-011 da [[02_Requisitos/ERS.md]].
    
- **Análises de Currículo Mais Detalhadas (Tier Pago):** Incluindo análise de sentimento, benchmarking de habilidades, otimização de impacto (STAR/CAR), previsão de perguntas de entrevista (conforme RF-CV-012 da [[02_Requisitos/ERS.md]]).
    
- **Treino Aprofundado para Entrevistas com IA (Tier Pago):** Simulação interativa (conforme RF-CHAT-007 da [[02_Requisitos/ERS.md]]).
    
- Integração com mais job boards.
    
- Funcionalidades de análise de perfil comportamental (soft skills).
    
- Matching proativo de vagas.
    

### 1.4. Público-Alvo

- **Primário:** Profissionais brasileiros, com foco inicial do MVP em **profissionais de tecnologia** (desenvolvedores, analistas, gerentes de produto, designers, etc.) que estão ativamente buscando uma nova oportunidade de emprego ou em transição de carreira.
    
- **Secundário:** Profissionais brasileiros de diversas áreas que desejam se manter preparados para futuras oportunidades, otimizar seus currículos e melhorar suas habilidades de entrevista.
    

**Características Esperadas:** Familiaridade com navegação na web, uso de aplicativos online e abertura para utilizar ferramentas baseadas em Inteligência Artificial. Valorizam a eficiência, a orientação personalizada e a melhoria contínua.

## 2. Metodologia e Framework de Desenvolvimento Adotados

### 2.1. O Modelo "Desenvolvimento Solo Ágil Aumentado por IA"

A metodologia de desenvolvimento adotada para o Recoloca.ai é o **"Desenvolvimento Solo Ágil Aumentado por Inteligência Artificial"**, conforme detalhado conceitualmente no documento [[01_Guias_Centrais/GUIA_AVANCADO_V1.md]]. Esta abordagem reinterpreta os princípios ágeis e a colaboração com IA para o contexto de um desenvolvedor individual com características neurodivergentes (TDAH/AHSD), visando maximizar a produtividade e o bem-estar.

**Princípios Chave (Resumo do [[GUIA_AVANCADO]]):**

- O desenvolvedor solo atua como um **"Maestro"** de uma orquestra de **Agentes de IA especializados ("Mentores")**.
    
- A IA transcende a função de ferramenta de codificação, tornando-se um **multiplicador de força** e um **parceiro de sparring intelectual** em todas as fases do SDLC.
    
- Foco na **automação** de **tarefas repetitivas** e aceleração do desenvolvimento, permitindo que o "Maestro" se concentre em desafios estratégicos, criativos e de maior valor agregado.
    
- Utilização de **Agentes de IA como especialistas virtuais** em diversas áreas (arquitetura, UX, segurança, etc.), complementando as habilidades do desenvolvedor solo e desafiando premissas.
    
- Ênfase na **Documentação Viva** como fonte da verdade, gerenciada via RAG e acessível tanto ao Maestro quanto aos Agentes.
    
- Implementação de um ciclo de **Human-in-the-Loop (HITL)** evolutivo, que se adapta à confiança e ao desempenho dos agentes, equilibrando supervisão e autonomia.
    

### 2.2. Papel do Desenvolvedor como "Maestro"

No modelo adotado, o desenvolvedor solo (Eu, Bruno S. Rosa) assume o papel de **"Maestro"**. As responsabilidades incluem:

- **Definir a visão estratégica** e os objetivos de negócio e de produto.
    
- **Priorizar o backlog** de funcionalidades e tarefas, alinhando-as com os objetivos estratégicos.
    
- **Orquestrar os Agentes de IA Mentores**, projetando e refinando seus prompts base, templates e fornecendo contexto rico através do RAG e de instruções diretas.
    
- **Supervisionar, validar e refinar** o trabalho gerado pelos Agentes de IA (HITL), atuando como o principal ponto de controle de qualidade e alinhamento.
    
- **Tomar decisões arquiteturais** e de design críticas, utilizando os agentes como consultores e para explorar alternativas.
    
- **Desenvolver componentes complexos**, realizar integrações críticas ou tarefas que exijam um nível de nuance, criatividade ou julgamento ético que a IA ainda não alcança.
    
- **Gerenciar e curar a "Documentação Viva"** e a base de conhecimento RAG, garantindo sua precisão e relevância.
    
- **Aprender e evoluir continuamente** na arte da engenharia de prompts, na orquestração de agentes e na colaboração efetiva com sistemas de IA.
    
- **Manter o foco no valor para o usuário** e nos objetivos de negócio, garantindo que a tecnologia sirva a esses propósitos.
    
- **Gerenciar o próprio fluxo de trabalho e energia**, utilizando ferramentas e técnicas que se alinhem com suas características neurodivergentes para manter o foco e a produtividade.
    

### 2.3. Visão Geral do SDLC Ágil Adaptado para o Recoloca.ai

O Ciclo de Vida de Desenvolvimento de Software (SDLC) Ágil tradicional é adaptado para incorporar a colaboração intensiva com Agentes de IA Mentores, com ênfase em ciclos curtos e feedback rápido:

1. **Concepção e Refinamento de Ideias/Requisitos:**
    
    - Maestro identifica necessidades/oportunidades ou refina itens do backlog.
        
    - `@AgenteMentorPO` auxilia na tradução para Histórias de Usuário (HUs) e Critérios de Aceite (ACs) a partir da [[02_Requisitos/ERS.md]] e insights do Maestro.
        
    - Maestro valida e refina HUs/ACs.
        
2. **Design (HLD/LLD/API/UX/UI):**
    
    - Maestro define diretrizes de design.
        
    - `@AgenteMentorArquitetoHLD`, `@AgenteMentorArquitetoLLD`, `@AgenteMentorAPI`, `@AgenteMentorUIDesign`, `@AgenteMentorUX` auxiliam na criação de artefatos de design (diagramas, especificações, mockups conceituais, fluxos).
        
    - Maestro valida, itera e aprova os designs.
        
3. **Desenvolvimento (Codificação):**
    
    - `@AgentesMentoresDev` (Flutter, FastAPI, JS), guiados pelo `@AgenteOrquestrador` e pelos LLDs/APIs, geram código boilerplate, componentes e lógica de negócios.
        
    - Maestro revisa, depura, refatora, integra e implementa partes críticas ou que exigem codificação manual.
        
4. **Testes e Garantia de Qualidade:**
    
    - `@AgenteMentorQA` auxilia na geração de planos de teste, casos de teste (Gherkin) e scripts de testes unitários/integração.
        
    - Maestro implementa/supervisiona testes E2E, revisa a cobertura e valida a qualidade.
        
5. **Documentação Contínua:**
    
    - `@AgenteMentorDocumentacao` auxilia na geração de comentários, docstrings e na manutenção da "Documentação Viva" no Obsidian.
        
    - Maestro garante que todas as decisões e implementações sejam documentadas.
        
6. **Deploy e Operações (DevOps):**
    
    - `@AgenteMentorDevOps` (conceitual, implementado via scripts e Pipedream) auxilia na automação de CI/CD para Vercel, Render e Supabase.
        
    - Maestro supervisiona e gerencia a infraestrutura e os processos de deploy.
        
7. **Monitoramento,** Feedback e **Iteração:**
    
    - Coleta de feedback do usuário (pós-MVP) e métricas de uso.
        
    - Análise de feedback e métricas para identificar melhorias e novas funcionalidades, alimentando o backlog.
        
    - O sistema RAG é continuamente atualizado com novos aprendizados e documentação, refinando o conhecimento dos agentes.
        
    - O ciclo recomeça.
        

## 3. Arquitetura de Agentes de IA Mentores do Recoloca.ai

A espinha dorsal da metodologia de desenvolvimento é uma arquitetura de Agentes de IA Mentores, implementados primariamente como agentes customizados ("Gems" ou funcionalidade equivalente) no **Trae IDE**. Estes agentes utilizarão o **Google Gemini Pro/Flash** (acessados via **OpenRouter** para flexibilidade e gerenciamento de custos, ou diretamente se o Trae permitir) e serão guiados pelas regras definidas em [[.trae/rules/user_rules.md]] e [[.trae/rules/project_rules.md]].

### 3.1. O Agente Orquestrador de Prompts (Implementação no Trae IDE)

Este é o **primeiro e mais crucial agente**, atuando como um "meta-agente" ou "agente de interface" entre o Maestro e os demais Agentes Mentores.

- **Persona no Trae IDE:** `@AgenteOrquestrador`
    
- **Objetivo:** Auxiliar o Maestro a refinar seu pensamento estratégico e a formular instruções (prompts) claras, precisas, contextualmente ricas e otimizadas para os outros Agentes Mentores. Atua como um "engenheiro de prompt assistente".
    
- **Funcionalidades (Conforme [[01_Guias_Centrais/GUIA_AVANCADO_V1.md]] e refinamentos):**
    
    1. **Análise da Documentação Existente (via RAG):** Processa e "compreende" documentos chave do projeto ([[02_Requisitos/ERS.md]], [[03_Arquitetura_e_Design/HLD.md]], etc.) para extrair contexto relevante para a tarefa em questão.
        
    2. **Geração de Perguntas Poderosas e Esclarecedoras:** Com base na tarefa e na análise documental, formula perguntas estratégicas ao Maestro para clarificar ambiguidades, identificar informações faltantes, definir escopo, restrições e sugerir a inclusão de contexto relevante.
        
    3. **Criação Assistida de Prompts Eficazes:** Após o diálogo com o Maestro, auxilia na montagem de prompts detalhados e estruturados para os agentes de destino, incorporando referências diretas à documentação, sugerindo técnicas de engenharia de prompt (Zero-Shot, Few-Shot, Chain-of-Thought) e utilizando os templates de [[05_Prompts/Templates_Base/]].
        
- **Implementação no Trae IDE:**
    
    - Será um agente customizado com um prompt base que o instrui sobre suas funções, tom de voz colaborativo e proativo.
        
    - Utilizará a capacidade do Trae IDE de acessar o contexto do projeto (arquivos abertos, estrutura de pastas) e idealmente se integrará com o sistema RAG para consultas mais profundas.
        
    - O Maestro interagirá com ele em um fluxo conversacional para "preparar" e otimizar os prompts antes de delegar tarefas aos outros agentes.
        

### 3.2. Detalhamento dos Agentes Mentores por Fase do SDLC

Os seguintes Agentes Mentores serão configurados no Trae IDE, cada um com uma persona, conjunto de habilidades (definidas pelo prompt base, [[.trae/rules/project_rules.md]] e contexto RAG) e utilizando templates de prompts específicos de [[05_Prompts/Templates_Base/]]. A referência principal para seus papéis é a **Tabela Essencial 1.1 do [[01_Guias_Centrais/GUIA_AVANCADO_V1.md]]**.

1. `@AgenteMentorPO` **(Product Owner)**
    
    - **Foco:** Definição e Refinamento de Requisitos.
        
    - **Tarefas:** Gerar Histórias de Usuário (em [[02_Requisitos/HU_AC/]]) e Critérios de Aceite (ACs) a partir da [[02_Requisitos/ERS.md]], refinar requisitos para clareza e testabilidade, identificar dependências e prioridades preliminares. Consultará o RAG para obter o contexto da ERS e do Plano Mestre.
        
    - **Prompt Base no Trae (resumido):** "Você é um Product Owner IA especialista em metodologias ágeis, UX e no mercado brasileiro de tecnologia. Sua tarefa é analisar requisitos formais ([[02_Requisitos/ERS.md]]) e gerar Histórias de Usuário centradas no usuário e Critérios de Aceite SMART..."
        
2. `@AgenteMentorArquitetoHLD` **(Arquiteto de Software - HLD)**
    
    - **Foco:** Design de Alto Nível.
        
    - **Tarefas:** Criar/otimizar o [[03_Arquitetura_e_Design/HLD.md]], gerar diagramas de arquitetura (componentes, interações) em Mermaid.js, definir interações entre módulos e com sistemas externos, identificar riscos arquiteturais. Consultará o RAG para a ERS e o Plano Mestre.
        
    - **Prompt Base no Trae (resumido):** "Você é um Arquiteto de Software IA experiente, com foco em sistemas web escaláveis, Micro-SaaS e segurança. Sua tarefa é analisar requisitos ([[02_Requisitos/ERS.md]]) e propor arquiteturas de alto nível robustas e eficientes..."
        
3. `@AgenteMentorArquitetoLLD` (**Arquiteto/Designer de Software - LLD**)
    
    - **Foco:** Design de Baixo Nível.
        
    - **Tarefas:** Detalhar classes, funções, modelos de dados e algoritmos para os módulos em [[03_Arquitetura_e_Design/LLD/]], criar diagramas de sequência e de classes em Mermaid.js. Consultará o RAG para o [[03_Arquitetura_e_Design/HLD.md]] e a [[02_Requisitos/ERS.md]].
        
    - **Prompt Base no Trae (resumido):** "Você é um Designer de Software IA detalhista e pragmático, capaz de traduzir arquiteturas de alto nível em especificações de baixo nível precisas e implementáveis..."
        
4. `@AgenteMentorAPI` **(Arquiteto de APIs)**
    
    - **Foco:** Especificação de APIs.
        
    - **Tarefas:** Gerar e manter as especificações OpenAPI 3.0 em YAML (ex: [[03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]) para os serviços de backend, garantindo consistência, segurança e boas práticas RESTful. Consultará o RAG para a [[02_Requisitos/ERS.md]] e o [[03_Arquitetura_e_Design/HLD.md]].
        
    - **Prompt Base no Trae (resumido):** "Você é um Arquiteto de APIs IA especialista em design de APIs RESTful seguras, bem documentadas e na especificação OpenAPI 3.0. Sua tarefa é gerar e manter a documentação da API do Recoloca.ai..."
        
5. `@AgenteMentorDevFastAPI` **(Desenvolvedor Python/FastAPI)**
    
    - **Foco:** Desenvolvimento Backend.
        
    - **Tarefas:** Gerar código Python/FastAPI para endpoints, implementar lógica de negócios, interações com Supabase (usando SQLAlchemy ou ORM similar), e testes unitários (pytest). Consultará o RAG para especificações de API, LLDs e padrões de código seguro.
        
    - **Prompt Base no Trae (resumido):** "Você é um Desenvolvedor Python Sênior especialista em FastAPI, Pydantic, Supabase/PostgreSQL e desenvolvimento de APIs seguras e eficientes. Siga as melhores práticas PEP 8, SOLID e as diretrizes de segurança do projeto..."
        
6. `@AgenteMentorDevFlutter` (Desenvolvedor **Flutter/Dart)**
    
    - **Foco:** Desenvolvimento Frontend (PWA).
        
    - **Tarefas:** Criar widgets de UI responsivos, implementar lógica de UI, gerenciamento de estado (Provider/Riverpod), chamadas à API backend, e testes unitários/widget. Consultará o RAG para especificações de API, LLDs e o [[03_Arquitetura_e_Design/STYLE_GUIDE.md]].
        
    - **Prompt Base no Trae (resumido):** "Você é um Desenvolvedor Flutter Sênior experiente na criação de PWAs responsivas, performáticas e visualmente atraentes, utilizando Dart e gerenciamento de estado moderno. Siga o [[03_Arquitetura_e_Design/STYLE_GUIDE.md]] e as melhores práticas de UX..."
        
7. `@AgenteMentorDevJS` **(Desenvolvedor de Extensão Chrome)**
    
    - **Foco:** Desenvolvimento da Extensão de Navegador.
        
    - **Tarefas:** Implementar lógica de extração de dados de job boards (scraping ético e robusto), comunicação segura com o backend, e a UI da extensão. Consultará o RAG para a [[02_Requisitos/ERS.md]] (requisitos da extensão) e especificações de API.
        
    - **Prompt Base no Trae (resumido):** "Você é um Desenvolvedor JavaScript experiente na criação de Extensões Chrome seguras, eficientes e fáceis de usar, com conhecimento em manipulação do DOM, APIs de extensão e comunicação assíncrona..."
        
8. `@AgenteMentorQA` **(Analista de QA/Testes)**
    
    - **Foco:** Garantia de Qualidade.
        
    - **Tarefas:** Gerar planos de teste ([[06_Qualidade_e_Testes/PGQ.md]]), casos de teste (em Gherkin, armazenados em [[06_Qualidade_e_Testes/Casos_de_Teste/]]) a partir de HUs/ACs, e gerar scripts de testes unitários e de integração. Consultará o RAG para [[02_Requisitos/ERS.md]], [[02_Requisitos/HU_AC/]], [[03_Arquitetura_e_Design/HLD.md]] e [[03_Arquitetura_e_Design/LLD/]].
        
    - **Prompt Base no Trae (resumido):** "Você é um Analista de QA IA meticuloso e criativo, especialista em derivar casos de teste abrangentes (funcionais, de usabilidade, segurança básica, performance) e em BDD/Gherkin. Seu objetivo é garantir a máxima cobertura e qualidade do produto..."
        
9. `@AgenteMentorSeguranca` **(Analista de Segurança)**
    
    - **Foco:** Segurança de Código e Arquitetura.
        
    - **Tarefas:** Revisar código gerado e artefatos de design em busca de vulnerabilidades (OWASP Top 10, OWASP LLM Top 10), instruir outros agentes sobre práticas seguras, sugerir melhorias de segurança. Consultará o RAG para requisitos de segurança da [[02_Requisitos/ERS.md]] e padrões de código seguro.
        
    - **Prompt Base no Trae (resumido):** "Você é um Especialista em Segurança de Aplicações IA (AppSec), com profundo conhecimento do OWASP Top 10, OWASP LLM Top 10, LGPD e práticas de codificação segura para Python/FastAPI, Dart/Flutter e JavaScript..."
        
10. `@AgenteMentorDocumentacao` **(Documentador Técnico)**
    
    - **Foco:** Documentação de Código e Manutenção da "Documentação Viva".
        
    - **Tarefas:** Gerar comentários e docstrings (Python Google Style, Dartdoc), explicar algoritmos complexos, auxiliar na sincronização da "Documentação Viva" no Obsidian e na curadoria/atualização da base de conhecimento para o RAG ([[08_Knowledge_Base_RAG_Sources/]]). Consultará o RAG para código, [[02_Requisitos/ERS.md]], [[03_Arquitetura_e_Design/HLD.md]] e [[03_Arquitetura_e_Design/LLD/]].
        
    - **Prompt Base no Trae (resumido):** "Você é um Escritor Técnico IA especialista em criar documentação de software clara, concisa e útil. Siga os padrões de documentação especificados para cada linguagem e ajude a manter a base de conhecimento do projeto Recoloca.ai precisa e atualizada..."
        

## 4. Arquitetura Técnica e Tecnologias

### 4.1. Stack Tecnológica Principal

Conforme definido na [[02_Requisitos/ERS.md#2.4. Restrições Gerais]] e refinamentos:

- **Frontend (PWA):** **Flutter (Dart)** - Escolhido pela capacidade de construir PWAs robustas e visualmente consistentes, com boa performance e um ecossistema rico.
    
- **Backend:** **Python com FastAPI** - Selecionado pela rapidez de desenvolvimento, performance assíncrona, tipagem de dados com Pydantic e geração automática de documentação de API.
    
- **Banco de Dados:** **PostgreSQL (Via Supabase)** - Oferece a robustez do PostgreSQL com as facilidades de um BaaS.
    
- **Autenticação & Storage de Arquivos:** **Supabase** - Para simplificar o Backend as a Service, oferecendo autenticação JWT, gerenciamento de usuários e armazenamento de arquivos seguro.
    
- **Extensão de Navegador:** **JavaScript, HTML, CSS** - Padrão para desenvolvimento de extensões Chrome.
    
- **IA LLM:** **APIs Google Gemini (Pro e Flash)** - Acessadas preferencialmente via **OpenRouter** para flexibilidade na escolha de modelos e gerenciamento de custos, ou diretamente se o Trae IDE oferecer integração otimizada. Gemini Pro para tarefas complexas (análise de CV, coaching) e Gemini Flash para tarefas mais simples e rápidas (chatbot básico, categorização).
    

### 4.2. Ferramentas de Desenvolvimento e IA

- **IDE Principal e Agentes de IA:** **Trae IDE** - Plataforma central para codificação, interação com LLMs e implementação dos Agentes Mentores customizados. Suas funcionalidades de "Rules" ([[.trae/rules/user_rules.md]] e [[.trae/rules/project_rules.md]]) serão extensivamente utilizadas.
    
- **Acesso a LLMs:** **OpenRouter** - Gateway para acessar diversos modelos Gemini e, potencialmente, outros LLMs, facilitando testes e otimização de custos.
    
- **Documentação e Gestão de Conhecimento ("Documentação Viva"):** **Obsidian** - Para criar, organizar e interligar toda a documentação do projeto, incluindo este Plano Mestre, ERS, HLD, LLDs, ADRs, notas de pesquisa e templates de prompts.
    
- **Controle de Versão:** **Git** (com repositório remoto no **GitHub** ou GitLab) - Para versionamento de toda a documentação (arquivos Markdown do Obsidian) e do código-fonte da aplicação, garantindo rastreabilidade e colaboração (mesmo que solo).
    
- **Gestão de Tarefas e Fluxo de Trabalho:** **Obsidian Kanban Plugin** - Para gerenciamento visual do backlog, sprints e fluxo de tarefas do Maestro e dos Agentes de IA, diretamente integrado à documentação.
    
- **Automação de Fluxos de Trabalho (CI/CD, Gatilhos):** **Pipedream** - Plataforma de automação focada em desenvolvedores, escolhida por sua flexibilidade com código (Node.js, Python), plano gratuito generoso e capacidade de integrar com Git, APIs e outros serviços para automações como:
    
    - CI/CD para deploy em Vercel/Render.
        
    - Gatilhos para reindexar a base RAG em commits na documentação.
        
    - Notificações.
        
- **Prototipagem de UI (Opcional):** **FlutterFlow** - Pode ser utilizado pelo `@AgenteMentorDevFlutter` ou pelo Maestro para acelerar a criação de interfaces iniciais, explorar layouts e gerar código Flutter base.
    

### 4.3. Arquitetura de Alto Nível (HLD) do Recoloca.ai

_O `@AgenteMentorArquitetoHLD` detalhará e manterá este HLD no arquivo [[03_Arquitetura_e_Design/HLD.md]]. Um esboço inicial dos componentes e suas interações é:_

1. **Frontend PWA (Flutter):**
    
    - **Responsabilidades:** Interface do usuário principal (Kanban, formulários de CV, Chatbot), gerenciamento de estado da UI, interações do usuário.
        
    - **Comunicação:** HTTPS/REST com o Backend API para todas as operações de dados e lógica de negócios.
        
2. **Backend API (Python/FastAPI):**
    
    - **Responsabilidades:** Lógica de negócios central, validações, processamento de dados, orquestração de chamadas para LLMs e Supabase.
        
    - **Endpoints:** Autenticação, CRUD para vagas/Kanban, operações de CV (upload, parsing, análise, otimização), interações do chatbot.
        
    - **Comunicação:** HTTPS com Supabase (PostgreSQL) para persistência; HTTPS com APIs Google Gemini (via OpenRouter).
        
3. **Extensão de Navegador (Chrome - JS/HTML/CSS):**
    
    - **Responsabilidades:** Extração de dados de vagas de job boards (LinkedIn, Gupy), interface de usuário da extensão.
        
    - **Comunicação:** HTTPS com o Backend API para enviar dados capturados e autenticar.
        
4. **Supabase (BaaS):**
    
    - **Auth:** Gerenciamento de usuários (registro, login, JWT).
        
    - **Database (PostgreSQL):** Armazenamento de dados de usuários, vagas, currículos, notas.
        
    - **Storage:** Armazenamento de arquivos PDF de currículos.
        
5. **Google Gemini APIs (via OpenRouter):**
    
    - **Gemini Pro/Flash:** Fornecem as capacidades de IA para análise de texto, geração de sugestões, respostas do chatbot, etc.
        
6. **Pipedream (Automação):**
    
    - **Responsabilidades:** Orquestrar fluxos de CI/CD, notificações, gatilhos para atualização do RAG.
        
    - **Comunicação:** Interage com GitHub (webhooks), Vercel/Render (APIs de deploy), serviços de email.
        
7. **Sistema RAG Local (LangChain + FAISS):**
    
    - **Responsabilidades:** Indexar a "Documentação Viva" e fornecer contexto relevante aos Agentes de IA no Trae IDE.
        
    - **Comunicação:** Acessado pelos Agentes de IA (potencialmente via uma ferramenta customizada no Trae ou script local).
        

_(Um diagrama Mermaid.js detalhado será incluído e mantido no [[03_Arquitetura_e_Design/HLD.md]].)_

## 5. Gestão de Conhecimento e Contexto (RAG & Documentação Viva)

### 5.1. Estratégia RAG para o Recoloca.ai

Para garantir que os Agentes de IA Mentores operem com informações atualizadas, específicas do projeto e consistentes com a "Documentação Viva", será implementado um sistema de **Retrieval Augmented Generation (RAG)**.

- **Base de Conhecimento para RAG:**
    
    - Localizada na pasta [[08_Knowledge_Base_RAG_Sources/]] dentro do vault do Obsidian.
        
    - Conterá versões em Markdown (ou texto puro, otimizadas para RAG) de:
        
        - [[02_Requisitos/ERS.md]]
            
        - [[03_Arquitetura_e_Design/HLD.md]]
            
        - Seções chave dos [[03_Arquitetura_e_Design/LLD/]]
            
        - [[03_Arquitetura_e_Design/STYLE_GUIDE.md]]
            
        - Sumários ou pontos chave das [[03_Arquitetura_e_Design/API_Specs/]]
            
        - Trechos relevantes da documentação oficial dos SDKs/APIs chave (Flutter, FastAPI, Supabase, Gemini).
            
        - Decisões de arquitetura importantes ([[03_Arquitetura_e_Design/ADR/]]).
            
        - Este próprio [[PLANO_MESTRE_RECOLOCA_AI.md]].
            
- **Tecnologias RAG:**
    
    - **Framework:** **LangChain** (Python) - Para construir e orquestrar o pipeline RAG (carregamento de documentos, divisão de texto, geração de embeddings, interação com banco de dados vetorial, e formatação do contexto para o LLM).
        
    - **Vector Store:** **FAISS** (Facebook AI Similarity Search) - Escolhido para uma implementação local, eficiente e leve, armazenando os embeddings vetoriais.
        
    - **Embedding Model:** Um modelo de embedding eficiente e de alta qualidade, como `all-MiniLM-L6-v2` (via Sentence Transformers/Hugging Face) ou outro que demonstre bom desempenho para textos em Português.
        
- **Processo de Indexação (Automatizado e Manual):**
    
    - Um script Python ([[scripts/rag_indexer.py]]) utilizará LangChain para:
        
        1. Monitorar alterações ou ser acionado (ex: via hook do Git ou Pipedream) na pasta [[08_Knowledge_Base_RAG_Sources/]].
            
        2. Carregar os documentos modificados ou novos.
            
        3. Dividi-los em chunks semânticos (experimentar tamanhos e sobreposições para otimizar a relevância).
            
        4. Gerar embeddings para cada chunk.
            
        5. Salvar ou atualizar os embeddings no índice FAISS local.
            
    - O Maestro também poderá acionar a reindexação manualmente após grandes atualizações na documentação.
        
- **Processo de Consulta (Retrieval) pelos Agentes:**
    
    - O `@AgenteOrquestrador` e os Agentes Mentores no Trae IDE, ao necessitarem de contexto específico do projeto, utilizarão uma ferramenta configurada no Trae (ou um comando especial) que invoca o sistema RAG.
        
    - A consulta do agente será convertida em um vetor de embedding e usada para buscar os chunks de informação mais relevantes (por similaridade de cosseno) no índice FAISS.
        
    - Os chunks recuperados serão injetados como contexto adicional no prompt final enviado ao LLM (Gemini), permitindo que o modelo gere respostas mais precisas e fundamentadas na "Documentação Viva".
        
- **Monitoramento e Refinamento do RAG:** O Maestro realizará verificações periódicas da qualidade e relevância dos resultados do RAG, ajustando o processo de chunking, o modelo de embedding ou o conteúdo da base de conhecimento conforme necessário para otimizar o desempenho.
    

### 5.2. A "Documentação Viva" no Obsidian e Git

Todo o conhecimento do projeto – este Plano Mestre, ERS, HLD, LLDs, ADRs, Style Guide, API Specs, notas de pesquisa, templates de prompts, e o Kanban de tarefas – será mantido e interligado no **Obsidian**.

- **Estrutura de Pastas:** Conforme a estrutura detalhada em [[Estrutura de Pastas e Arquivos Recoloca.ai (v2.0)]] (ou o nome do arquivo correspondente que você criou para a estrutura de pastas).
    
- **Links Bidirecionais:** Uso intensivo de links wiki ([[Nome do Arquivo.md#Cabeçalho Opcional]]) para criar uma rede de conhecimento coesa, navegável e que facilite a descoberta de informações relacionadas.
    
- **Controle de Versão:** Todo o vault do Obsidian (ou a pasta específica do projeto `Recoloca.ai/`) será um repositório **Git**, com commits frequentes e detalhados, e push para um repositório remoto (GitHub). O plugin "Obsidian Git" será utilizado para facilitar commits, pushes e pulls diretamente da interface do Obsidian.
    
- **Atualização Contínua:** A documentação é um processo orgânico e contínuo, não uma fase estática. O `@AgenteMentorDocumentacao` auxiliará na geração e manutenção, e o Maestro é o curador final, responsável por garantir que todas as decisões, aprendizados e alterações no projeto sejam refletidos na documentação de forma precisa e tempestiva.
    

### 5.3. Interação com Ferramentas Externas (APIs, SDKs)

- **Abordagem Primária (Gemini Function Calling):** Para interações diretas dos agentes com APIs (ex: chamar uma API do Supabase, interagir com uma ferramenta de análise de código), a funcionalidade de **Gemini Function Calling** (ou equivalente no Trae IDE/OpenRouter) será a primeira opção. Isso permite que o LLM descreva a função que precisa ser chamada e os parâmetros, e o Maestro (ou um código de suporte) executa a função e retorna o resultado para o LLM.
    
- **Contexto de SDKs (via RAG e Context7):** Para garantir que os agentes usem SDKs e APIs de forma correta e atualizada, o RAG fornecerá contexto da documentação. Ferramentas como **Context7** (se integrável ou como inspiração para scripts locais) podem ser exploradas para fornecer contexto de SDKs diretamente no IDE.
    
- **MCP (Model Context Protocol):** O MCP continua sendo uma tecnologia promissora para o futuro. Sua adoção será considerada à medida que o protocolo e suas implementações seguras se tornarem mais maduras e disponíveis nas ferramentas utilizadas (Trae IDE, LangChain).
    

## 6. Fluxo de Trabalho de Desenvolvimento e HITL

### 6.1. Fluxo de Trabalho Detalhado: Da ERS ao Deploy

O fluxo de trabalho será iterativo e incremental, seguindo os princípios ágeis e integrando o Maestro e os Agentes de IA de forma colaborativa.

1. **Planejamento da Iteração (Obsidian Kanban):**
    
    - Maestro revisa o backlog (HUs, tarefas técnicas, bugs) e prioriza o trabalho para a iteração atual (ex: sprint de 1-2 semanas).
        
    - Tarefas são detalhadas no Kanban ([[KANBAN_Recoloca_AI.md]]), com links para HUs/ACs, e designadas para "Humano" (Maestro) ou "Agente IA" (com especificação do agente).
        
2. **Refinamento de Requisitos e Design (Colaborativo):**
    
    - Para HUs complexas, o Maestro interage com `@AgenteMentorPO` e `@AgenteOrquestrador` para refinar HUs/ACs.
        
    - Maestro e `@AgenteMentorArquitetoHLD/LLD/API` colaboram no design, com o agente gerando rascunhos e o Maestro validando, iterando e aprovando. Artefatos de design são salvos e versionados.
        
3. **Desenvolvimento** (Codificação **Assistida):**
    
    - Maestro delega tarefas de codificação aos `@AgentesMentoresDev` relevantes, fornecendo prompts claros (gerados com ajuda do `@AgenteOrquestrador`) que incluem links para LLDs, API specs, Style Guide e contexto RAG.
        
    - Agentes geram código, que é commitado em branches de feature separadas.
        
    - Maestro revisa o código (HITL - Fase 1 ou 2), depura, refatora, otimiza e implementa partes mais complexas ou integrações críticas.
        
4. **Testes e Garantia de Qualidade:**
    
    - `@AgenteMentorQA` auxilia na geração de testes unitários (baseados no código) e casos de teste (baseados em HUs/ACs).
        
    - Maestro implementa/supervisiona testes de integração e E2E.
        
    - Execução automatizada de testes como parte do CI (via Pipedream/GitHub Actions).
        
    - `@AgenteMentorSeguranca` pode ser invocado para revisões de segurança em pontos críticos.
        
5. **Documentação Contínua:**
    
    - `@AgenteMentorDocumentacao` auxilia na geração de docstrings, comentários e na atualização da documentação do usuário ou técnica.
        
    - Maestro garante que a "Documentação Viva" (ERS, HLD, LLDs, ADRs) seja atualizada para refletir as implementações e decisões.
        
6. **Integração e Deploy:**
    
    - Código da feature branch é mesclado ao branch principal após aprovação e testes.
        
    - Processo de CI/CD (orquestrado por Pipedream) realiza build, testes finais e deploy para ambiente de staging e, posteriormente, produção (Vercel, Render).
        
    - Maestro monitora o deploy e realiza smoke tests.
        
7. **Revisão da Iteração e Feedback:**
    
    - Maestro analisa os resultados da iteração, o feedback dos usuários (quando aplicável) e o desempenho dos agentes.
        
    - Learnings são documentados e usados para refinar processos, prompts e a base RAG.
        
    - O ciclo recomeça com o planejamento da próxima iteração.
        

### 6.2. Modelo de Human-in-the-Loop (HITL) Evolutivo para o Recoloca.ai

O HITL é um pilar central, garantindo qualidade, segurança, alinhamento ético e aprendizado contínuo. Ele evoluirá em fases, adaptando-se à maturidade dos agentes e à complexidade das tarefas:

- **Fase** 1: Supervisão Intensa **e Detalhada (MVP Inicial e Novas Funcionalidades Críticas)**
    
    - **Descrição:** O Maestro revisa minuciosamente _todo_ o output significativo dos Agentes de IA (HUs, ACs, diagramas, especificações de API, blocos de código > X linhas, casos de teste críticos). O foco é em validação, correção e aprendizado sobre como otimizar prompts e guiar os agentes.
        
    - **Pontos de Checagem:** Após cada tarefa principal de um agente.
        
    - **Critérios de Confiança:** Baixa a média confiança inicial nos agentes para tarefas novas ou complexas.
        
    - **Feedback para Agentes:** Detalhado, explicando correções e o porquê, para "treinar" implicitamente os agentes (refinando seus prompts base ou templates).
        
- **Fase 2: Autonomia Guiada e Revisão por Amostragem (Funcionalidades Maduras e Tarefas Repetitivas)**
    
    - **Descrição:** O Maestro foca a revisão detalhada em áreas de maior risco, complexidade ou impacto no usuário. Para tarefas onde os agentes já demonstraram alta proficiência (ex: gerar CRUD básico a partir de um LLD claro), a revisão pode ser por amostragem ou focada em pontos chave.
        
    - **Pontos de Checagem:** Definidos para entregas chave, integrações ou módulos sensíveis. Uso de checklists de revisão.
        
    - **Critérios de Confiança:** Média a alta confiança em agentes específicos para tarefas bem definidas. Métricas de qualidade (bugs, retrabalho) são monitoradas.
        
- **Fase 3: Controle Supervisor e Foco Estratégico (Ideal de Longo Prazo)**
    
    - **Descrição:** O Maestro atua mais como um revisor final de alto nível (arquitetura, UX global) e tomador de decisões estratégicas. Agentes operam com maior autonomia em domínios onde são consistentemente confiáveis, com sistemas de alerta para anomalias, baixa confiança na geração ou desvios de padrões.
        
    - **Pontos de Checagem:** Revisões de design de novas features, aprovações de release, auditorias periódicas de qualidade e segurança.
        
    - **Critérios de Confiança:** Alta confiança, baseada em histórico de desempenho e métricas robustas. O sistema RAG está maduro e a base de conhecimento é abrangente.
        
    - **Foco do Maestro:** Inovação, pesquisa de novas tecnologias, estratégia de produto e mentoria de alto nível para os agentes (refinando suas "especializações").
        

O feedback fornecido pelo Maestro durante as revisões HITL é crucial. Ele não apenas valida o trabalho, mas também serve como dados para o refinamento contínuo dos [[05_Prompts/Templates_Base/]] e das instruções nos [[04_Agentes_IA/AGENTES_IA_MENTORES.md]], melhorando o desempenho futuro dos agentes.

### 6.3. Diagrama Visual do Fluxo de Trabalho (Mermaid.js)

_(Este diagrama será inserido e mantido no arquivo [[03_Arquitetura_e_Design/FLUXO_TRABALHO_GERAL.md]] e pode ser linkado ou transcluído aqui. Ele ilustrará o fluxo da Seção 6.1.)_

**Exemplo de Código Mermaid.js para o Fluxo:**

```graph TD
    A[1. ERS/Backlog no Kanban] --> B{2. Maestro Prioriza & Prepara Tarefa};
    B -- Tarefa para Agente --> C{3. @AgenteOrquestrador Assiste na Criação do Prompt};
    C --> D[4. Agente Mentor Específico Executa Tarefa (Design/Código/Teste)];
    D --> E{5. Maestro Revisa Output (HITL)};
    E -- Ajustes Necessários --> D;
    E -- Aprovado --> F[6. Integração ao Código Base / Documentação];
    F --> G[7. Testes Automatizados (CI)];
    G -- Falha --> E;
    G -- Sucesso --> H[8. Deploy (Staging/Produção)];
    H --> I{9. Monitoramento & Feedback};
    I --> A;
    B -- Tarefa para Humano --> J[3a. Maestro Executa Tarefa Manual];
    J --> F;
```

## 7. Gestão de Projeto, Tarefas e Comunicação

### 7.1. Configuração e Uso do Obsidian Kanban

O gerenciamento de tarefas será centralizado no **Obsidian** utilizando o plugin **"Kanban"**, conforme arquivo [[KANBAN_Recoloca_AI.md]].

- **Estrutura de Colunas:**
    
    - `🧊 Backlog Geral` (Novas ideias, HUs da ERS, bugs reportados)
        
    - `🎯 A Fazer - Próxima Iteração` (Tarefas priorizadas para a iteração atual)
        
    - `✍️ Preparação/Revisão - Maestro` (Tarefas que exigem input humano antes da delegação ou revisão de output de agente)
        
    - `🤖 Em Processamento - Agente IA` (Tarefas delegadas e em execução por um agente)
        
    - `⚙️` Em Processamento - `Maestro` (Tarefas sendo executadas manualmente pelo Maestro)
        
    - `🧐 Validação - Maestro (HITL)` (Output de agentes aguardando revisão e aprovação)
        
    - `✅ Concluído na Iteração`
        
    - `🚀 Deployado/Arquivado`
        
- **Cartões (Tarefas):**
    
    - Título claro e acionável.
        
    - **Links Essenciais:** Para [[02_Requisitos/ERS.md]], [[02_Requisitos/HU_AC/]], [[03_Arquitetura_e_Design/LLD/]], [[05_Prompts/]] relevantes, etc.
        
    - **Tags Detalhadas:**
        
        - Responsável: `#maestro`, `#agente`
            
        - Agente Específico: `#agente_po`, `#agente_arquiteto_hld`, `#agente_dev_fastapi`, etc.
            
        - Fase HITL: `#hitl_fase1` (revisão detalhada), `#hitl_fase2` (revisão por amostragem).
            
        - Tipo: `#bug`, `#feature`, `#refactor`, `#pesquisa`, `#documentacao`.
            
        - Prioridade: `#p0_critica`, `#p1_alta`, `#p2_media`, `#p3_baixa`.
            
        - Módulo/Feature: `#auth`, `#kanban`, `#cv_optimization`.
            
- **Fluxo:** O Maestro move os cartões entre as colunas, atualizando status, adicionando notas e garantindo que todo o contexto necessário esteja linkado.
    

### 7.2. Templates de Prompts e Engenharia de Prompt Contínua

A eficácia dos Agentes de IA depende diretamente da qualidade e do refinamento contínuo dos prompts.

- **Localização Centralizada:** [[05_Prompts/]]
    
    - [[05_Prompts/Templates_Base/]]: Contém templates estruturados e reutilizáveis para cada tipo de tarefa e agente (ex: `TPL_Gerar_HU_AC.md`, `TPL_Gerar_Codigo_FastAPI_Endpoint.md`).
        
    - [[05_Prompts/Prompts_Especificos/]]: Armazena prompts mais elaborados, que foram significativamente customizados para tarefas complexas ou que resultaram em outputs de alta qualidade e podem ser reutilizados ou adaptados.
        
- **Estrutura Detalhada dos Templates (conforme exemplo em [[05_Prompts/Templates_Base/TPL_Exemplo.md]]):**
    
    - **Metadados:** Nome do Agente Alvo, Versão do Template, Objetivo da Tarefa.
        
    - **PERSONA DO AGENTE:** Instruções claras sobre o papel, expertise, tom de voz e como deve interagir com a base de conhecimento (RAG).
        
    - **CONTEXTO FORNECIDO:** Placeholders para links para documentos relevantes ([[02_Requisitos/ERS.md#RF-ABC]], LLDs, ADRs) e para contexto pontual do Maestro.
        
    - **TAREFA DETALHADA:** Descrição passo a passo e inequívoca do que o agente deve realizar.
        
    - **RESTRIÇÕES E DIRETRIZES:** O que NÃO fazer, limites, padrões de código, segurança, etc.
        
    - **FORMATO DE SAÍDA ESPERADO:** Descrição da estrutura da resposta, exemplos (few-shot prompting), e tipo de artefato (código, Markdown, Mermaid).
        
- **Engenharia de Prompt Contínua:**
    
    - O Maestro, com auxílio do `@AgenteOrquestrador`, refinará constantemente os templates e prompts específicos com base no desempenho dos agentes, no feedback do HITL e nos resultados obtidos.
        
    - Testes A/B com diferentes formulações de prompt podem ser realizados para otimizar os resultados.
        
    - Os aprendizados serão documentados (ex: em notas no Obsidian linkadas aos templates).
        

## 9. Apêndices

### 9.1. Glossário de Termos Específicos do Projeto e Metodologia

- **Maestro:** O desenvolvedor solo (Bruno S. Rosa) que define a estratégia, orquestra os Agentes de IA, e realiza a validação crítica (HITL) do projeto Recoloca.ai.
    
- **Agente Mentor de IA:** Um agente de IA especializado, configurado no Trae IDE com uma persona e conhecimento específico (via prompt base, [[.trae/rules/project_rules.md]] e RAG), para assistir o Maestro em uma determinada fase ou tarefa do SDLC.
    
- **RAG (Retrieval Augmented Generation):** Geração Aumentada por Recuperação. Técnica que permite a um LLM acessar e utilizar informações de uma base de conhecimento externa (a "Documentação Viva" do Recoloca.ai) para gerar respostas mais precisas, contextuais e atualizadas.
    
- **Gemini Function Calling:** Funcionalidade das APIs Gemini que permite aos LLMs descreverem funções que precisam ser executadas no ambiente do cliente (Maestro), que então executa a função e retorna o resultado para o LLM continuar o processamento. Abordagem primária para interação com ferramentas.
    
- **MCP (Model Context Protocol):** Protocolo de Contexto de Modelo. Padrão aberto para interação de LLMs com ferramentas externas. A ser observado para adoção futura.
    
- **HITL (Human-in-the-Loop):** Humano no Loop. Processo onde o Maestro revisa, valida, corrige ou guia o output de um sistema de IA.
    
- **SDLC (Software Development Life Cycle):** Ciclo de Vida de Desenvolvimento de Software.
    
- **PWA (Progressive Web Application):** Aplicação Web Progressiva.
    
- **BaaS (Backend as a Service):** Backend como Serviço (ex: Supabase).
    
- **CRUD (Create, Read, Update, Delete):** Operações básicas de dados.
    
- **JWT (JSON Web Token):** Padrão para tokens de acesso.
    
- **TOTP (Time-based One-Time Password):** Senha de Uso Único Baseada em Tempo (para MFA).
    
- **OWASP (Open Web Application Security Project):** Referência para riscos de segurança.
    
- **YAML (YAML Ain't Markup Language):** Linguagem de serialização de dados.
    
- **Markdown:** Linguagem de marcação para a "Documentação Viva".
    
- **Mermaid.js / PlantUML:** Linguagens textuais para gerar diagramas.
    
- **FAISS (Facebook AI Similarity Search):** Biblioteca para busca de similaridade vetorial (Vector Store).
    
- **LangChain:** Framework para desenvolvimento de aplicações com LLMs.
    
- **OpenRouter:** Gateway para acesso a múltiplos LLMs.
    
- **Trae IDE:** Ambiente de Desenvolvimento Integrado com IA, plataforma para os Agentes Mentores.
    
- **Pipedream:** Plataforma de automação de fluxos de trabalho.
    
- **FlutterFlow:** Plataforma low-code para prototipagem Flutter.
    
- **Supabase:** BaaS open-source (PostgreSQL, Auth, Storage).
    
- **FastAPI:** Framework web Python.
    
- **Vercel / Render:** Plataformas de deploy.
    
- **ADR (Architecture Decision Record):** Documento que captura uma decisão arquitetural importante, seu contexto e consequências.
    

### 9.2. Referências Chave

- **Documentos Internos do Projeto (Links Obsidian):**
    
    - [[00_Gerenciamento_Projeto/TAP.md]]
        
    - [[01_Guias_Centrais/GUIA_AVANCADO_V1.md]]
        
    - [[02_Requisitos/ERS.md]]
        
    - [[03_Arquitetura_e_Design/HLD.md]]
        
    - [[03_Arquitetura_e_Design/STYLE_GUIDE.md]]
        
    - [[.trae/rules/user_rules.md]] (Embora este seja mais uma configuração do Trae, seu conteúdo é relevante)
        
    - [[.trae/rules/project_rules.md]]
        
- **Documentação Oficial das Ferramentas Principais:**
    
    - **Obsidian**: [https://help.obsidian.md/](https://help.obsidian.md/ "null")
        
    - **Git**: [https://git-scm.com/doc](https://git-scm.com/doc "null")
        
    - **Trae IDE**: https://docs.trae.ai/ [https://docs.trae.ai/](https://docs.trae.ai/ "null")
        
    - **Google Gemini API**: [https://ai.google.dev/docs](https://ai.google.dev/docs "null")
        
    - **LangChain**: [https://python.langchain.com/docs/get_started/introduction](https://python.langchain.com/docs/get_started/introduction "null")
        
    - **FastAPI**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/ "null")
        
    - **Flutter**: [https://docs.flutter.dev/](https://docs.flutter.dev/ "null")
        
    - **Dart**: [https://dart.dev/guides](https://dart.dev/guides "null")
        
    - **Supabase**: [https://supabase.com/docs](https://supabase.com/docs "null")
        
    - **Pipedream**: [https://pipedream.com/docs/](https://pipedream.com/docs/ "null")
        
    - **OpenRouter**: [https://openrouter.ai/docs](https://openrouter.ai/docs "null")
        
    - **FAISS**:  [https://faiss.ai/](https://faiss.ai/ "null") 
        
    - **FlutterFlow**: [https://docs.flutterflow.io/](https://docs.flutterflow.io/ "null")
        
    - **Vercel**: [https://vercel.com/docs](https://vercel.com/docs "null")
        
    - **Render**: [https://render.com/docs](https://render.com/docs "null")
        
    - **Mermaid.js**: [https://mermaid.js.org/](https://mermaid.js.org/ "null")
        
- **Padrões e Guias de Referência:**
    
    - **Material Design 3**: [https://m3.material.io/](https://m3.material.io/ "null")
        
    - **OWASP Top 10**: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/ "null")
        
    - **OWASP LLM Top 10**: [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/ "null")
        
    - **PEP 8 (Python Style Guide)**: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/ "null")
        
    - **Effective Dart**: [https://dart.dev/guides/language/effective-dart](https://dart.dev/guides/language/effective-dart "null")
        
    - **Conventional Commits**: [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/ "null")
        

**FIM DO PLANO MESTRE RECOLOCA.AI (v1.2)**