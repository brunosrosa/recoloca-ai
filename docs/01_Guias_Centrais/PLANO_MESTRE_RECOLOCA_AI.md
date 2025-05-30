# PLANO MESTRE DO PROJETO RECOLOCA.AI

**Data de Criação**: 26 de maio de 2025

**Data de Última Atualização**: 29 de maio de 2025

**Versão**: 1.3

**Autor Principal (Maestro)**: Bruno S. Rosa

**Assistência IA:** Gemini (Personalizado para colaboração e co-evolução)

## Sumário Executivo

Este **Plano Mestre** é o documento central e a **fonte da verdade** para o desenvolvimento, manutenção e evolução contínua do projeto **Recoloca.ai**. Ele consolida a visão estratégica, as decisões arquiteturais, o framework de "Desenvolvimento Solo Ágil Aumentado por IA", os fluxos de trabalho detalhados, as ferramentas selecionadas e o roadmap para a construção do Micro-SaaS Recoloca.ai. Este documento é uma **"Documentação Viva"**, mantida e atualizada no Obsidian e versionada com Git, servindo como guia para o desenvolvedor solo ("Maestro") e como base de conhecimento fundamental para seus Agentes de IA Mentores configurados no Trae IDE. Ele está alinhado com a [[02_Requisitos/ERS.md]] (v0.5 ou mais recente) e o [[01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.1 ou mais recente).

## 1. Introdução ao Recoloca.ai

### 1.1. Visão Geral do Produto e Problema de Mercado

O **Recoloca.ai** é um Micro-SaaS inovador projetado para **transformar** a experiência de recolocação **profissional no Brasil**. O mercado de trabalho atual, especialmente no setor de tecnologia, é dinâmico e competitivo. Profissionais enfrentam desafios significativos como:

- Gerenciamento ineficiente de múltiplas candidaturas.
    
- Dificuldade em adaptar currículos de forma eficaz para cada vaga.
    
- Falta de preparo e confiança para entrevistas.
    
- Sensação de isolamento e falta de orientação durante o processo.
    

O Recoloca.ai visa solucionar essas dores oferecendo uma plataforma integrada que atua como o **"cockpit do candidato"**, combinando **gerenciamento inteligente de candidaturas (Kanban)**, **otimização de currículos potencializada por Inteligência Artificial (IA)** e um **assistente de IA para coaching e suporte contextualizado**. O objetivo é empoderar os profissionais brasileiros, fornecendo ferramentas e orientação para que naveguem pelo processo de recolocação com maior eficiência, estratégia e confiança, aumentando significativamente suas chances de sucesso.

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

**Funcionalidades Centrais do MVP** (Conforme [[02_Requisitos/ERS.md]] v0.5):

1. **Gerenciamento de Candidaturas (Kanban)** `RF-KAN`:
    
    - Criação, visualização, edição e exclusão de cartões de vagas.
        
    - Campos do cartão: Título da Vaga, Empresa, Link Original, Status (coluna), Data de Adição, Prioridade, Anotações (Markdown), Localização, Modalidade, Data de Publicação/Captura, Origem, Score de Adequação (se calculado), Prazo.
        
    - Colunas fixas e ordenadas: "Salvas", "Radar de Interesse", "Aplicadas", "Entrevista(s)", "Teste(s)", "Proposta", "Recusada/Fechada".
        
    - Movimentação de cartões via drag-and-drop.
        
    - Filtros e ordenação de cartões.
        
    - Registro de histórico de interações por vaga.
        
    - Dashboard de métricas pessoais (funil de candidatura).
        
    - Limite de 15 vagas ativas para o tier gratuito.
        
2. **Importação Inteligente de Vagas** `RF-IMP` (MVP):
    
    - Importação de vaga colando a URL da página da vaga.
        
    - IA (LLM) tenta extrair informações relevantes (Título, Empresa, Descrição, Requisitos, Localização, Modalidade, Idioma - PT, EN, ES).
        
    - Permite ao usuário revisar, editar e complementar os dados extraídos antes de salvar.
        
3. **Otimização de Currículo Baseada em IA** `RF-CV`:
    
    - Upload e gerenciamento de múltiplos currículos base (PDF - PT, EN, ES no MVP).
        
    - Extração de texto (pymupdf/Tesseract) e categorização semântica das seções via LLM.
        
    - Revisão, edição e validação obrigatória do conteúdo extraído pelo usuário ("Currículo Base Ativo").
        
    - Análise de adequação do "Currículo Base Ativo" com a descrição da vaga (Score de Adequação IA).
        
    - Sugestões específicas e contextualizadas para otimizar o currículo para a vaga.
        
    - Estimativa de range salarial para a vaga (IA + RAG de pesquisas salariais).
        
    - Download do currículo otimizado em PDF (templates profissionais ATS-friendly).
        
    - Gerenciamento de versões e atualização do "Currículo Base Ativo".
        
    - Limite de 5 "Otimizações Completas" por mês para o tier gratuito.
        
4. **Assistente de IA para Coaching Básico** `RF-COACH`:
    
    - Interface de chatbot interativo.
        
    - IA Coach (Gemini Flash para gratuito, Pro para pago) com persona definida (Animado, inspirador, empático, prático, especialista em recolocação BR).
        
    - Respostas baseadas em RAG (base de conhecimento curada) e contexto do usuário.
        
    - Atuação proativa (incentivar atualização no Kanban, dicas contextuais).
        
    - Orientações sobre soft skills, tendências de mercado, preparação para entrevistas.
        
    - Uso de métricas do usuário para identificar gargalos e sugerir foco.
        
    - Limite de 30 interações/dia para o tier gratuito.
        
5. **Autenticação e Gerenciamento de Conta** `RF-AUTH`:
    
    - Cadastro com Email/Senha, confirmação de email.
        
    - Login seguro (proteção brute-force).
        
    - Redefinição de senha.
        
    - Onboarding inicial (Nome, upload do Currículo Base).
        
    - Diferenciação de tiers (gratuito/premium).
        
    - Edição de perfil, gerenciamento de currículos base, preferências de notificação.
        
    - Visualização e gerenciamento de assinatura.
        
    - Exclusão de conta e dados (LGPD).
        
6. **Modelo Freemium e Pagamentos** `RF-PAY-SUB`:
    
    - Definição clara dos limites do plano gratuito e benefícios do plano premium.
        
    - Integração com gateway de pagamento seguro para assinaturas recorrentes.
        

**Visão de Evolução** (Pós-MVP - Breve Menção, conforme [[02_Requisitos/ERS.md]] v0.5):

- **Extensão de Navegador (Web Clipper):** Para captura de vagas do LinkedIn (RF-IMP-003).
    
- **Autenticação Multifator (MFA):** Via TOTP (RF-AUTH-004).
    
- **Templates Avançados de Currículo e Customização (Tier Pago):** (RF-CV-009, Tier Pago).
    
- **Análises de Currículo Mais Detalhadas (Tier Pago):** (RF-CV-009, Tier Pago).
    
- **Treino Aprofundado para Entrevistas com IA (Tier Pago):** (RF-COACH-006, Tier Pago).
    
- Suporte a mais idiomas na interface.
    
- Funcionalidades de networking simplificado.
    
- Biblioteca de recursos curada.
    
- Modo "Manutenção de Carreira" e "Projetos de Carreira".
    

### 1.4. Público-Alvo

- **Primário:** Profissionais brasileiros, com foco inicial do MVP em **profissionais de tecnologia** (desenvolvedores, analistas, QAs, designers, gerentes de produto, etc.) que estão ativamente buscando uma nova oportunidade de emprego ou em transição de carreira.
    
- **Secundário:** Profissionais brasileiros de diversas áreas que desejam se manter preparados para futuras oportunidades, otimizar seus currículos e melhorar suas habilidades de entrevista.
    

**Características Esperadas:** Familiaridade com navegação na web, uso de aplicativos online e abertura para utilizar ferramentas baseadas em Inteligência Artificial. Valorizam a eficiência, a orientação personalizada, uma UX superior e a melhoria contínua.

## 2. Metodologia e Framework de Desenvolvimento Adotados

### 2.1. O Modelo "Desenvolvimento Solo Ágil Aumentado por IA"

A metodologia de desenvolvimento adotada para o Recoloca.ai é o **"Desenvolvimento Solo Ágil Aumentado por Inteligência Artificial"**, conforme detalhado conceitualmente no documento [[01_Guias_Centrais/GUIA_AVANCADO.md]]. Esta abordagem reinterpreta os princípios ágeis e a colaboração com IA para o contexto de um desenvolvedor individual com características neurodivergentes (TDAH/AHSD), visando maximizar a produtividade e o bem-estar.

**Princípios Chave** (Resumo do [[01_Guias_Centrais/GUIA_AVANCADO.md]]):

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
    
    - `@AgentesMentoresDev` (Flutter, FastAPI), guiados pelo `@AgenteOrquestrador` e pelos LLDs/APIs, geram código boilerplate, componentes e lógica de negócios.
        
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
        
7. **Monitoramento, Feedback e Iteração:**
    
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
    
- **Funcionalidades** (Conforme [[01_Guias_Centrais/GUIA_AVANCADO.md]] e refinamentos):
    
    1. **Análise da Documentação Existente (via RAG):** Processa e "compreende" documentos chave do projeto ([[02_Requisitos/ERS.md]], [[03_Arquitetura_e_Design/HLD.md]], etc.) para extrair contexto relevante para a tarefa em questão.
        
    2. **Geração de Perguntas Poderosas e Esclarecedoras:** Com base na tarefa e na análise documental, formula perguntas estratégicas ao Maestro para clarificar ambiguidades, identificar informações faltantes, definir escopo, restrições e sugerir a inclusão de contexto relevante.
        
    3. **Criação Assistida de Prompts Eficazes:** Após o diálogo com o Maestro, auxilia na montagem de prompts detalhados e estruturados para os agentes de destino, incorporando referências diretas à documentação, sugerindo técnicas de engenharia de prompt (Zero-Shot, Few-Shot, Chain-of-Thought) e utilizando os templates de [[05_Prompts/Templates_Base/]].
        
- **Implementação no Trae IDE:**
    
    - Será um agente customizado com um prompt base que o instrui sobre suas funções, tom de voz colaborativo e proativo.
        
    - Utilizará a capacidade do Trae IDE de acessar o contexto do projeto (arquivos abertos, estrutura de pastas) e idealmente se integrará com o sistema RAG para consultas mais profundas.
        
    - O Maestro interagirá com ele em um fluxo conversacional para "preparar" e otimizar os prompts antes de delegar tarefas aos outros agentes.
        

### 3.2. Detalhamento dos Agentes Mentores por Fase do SDLC

Os seguintes Agentes Mentores serão configurados no Trae IDE, cada um com uma persona, conjunto de habilidades (definidas pelo prompt base, [[.trae/rules/project_rules.md]] e contexto RAG) e utilizando templates de prompts específicos de [[05_Prompts/Templates_Base/]]. A referência principal para seus papéis é a **Tabela Essencial do [[01_Guias_Centrais/GUIA_AVANCADO.md]]**.

1. `@AgenteMentorPO` **(Product Owner)**
    
    - **Foco:** Definição e Refinamento de Requisitos.
        
    - **Tarefas:** Gerar Histórias de Usuário (em [[02_Requisitos/HU_AC/]]) e Critérios de Aceite (ACs) a partir da [[02_Requisitos/ERS.md]], refinar requisitos para clareza e testabilidade, identificar dependências e prioridades preliminares. Consultará o RAG para obter o contexto da ERS e do Plano Mestre.
        
2. `@AgenteMentorArquitetoHLD` **(Arquiteto de Software - HLD)**
    
    - **Foco:** Design de Alto Nível.
        
    - **Tarefas:** Criar/otimizar o [[03_Arquitetura_e_Design/HLD.md]], gerar diagramas de arquitetura (componentes, interações) em Mermaid.js, definir interações entre módulos e com sistemas externos, identificar riscos arquiteturais. Consultará o RAG para a ERS e o Plano Mestre.
        
3. `@AgenteMentorArquitetoLLD` **(Arquiteto/Designer de Software - LLD)**
    
    - **Foco:** Design de Baixo Nível.
        
    - **Tarefas:** Detalhar classes, funções, modelos de dados e algoritmos para os módulos em [[03_Arquitetura_e_Design/LLD/]], criar diagramas de sequência e de classes em Mermaid.js. Consultará o RAG para o [[03_Arquitetura_e_Design/HLD.md]] e a [[02_Requisitos/ERS.md]].
        
4. `@AgenteMentorAPI` **(Arquiteto de APIs)**
    
    - **Foco:** Especificação de APIs.
        
    - **Tarefas:** Gerar e manter as especificações OpenAPI 3.0 em YAML (ex: [[03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]) para os serviços de backend, garantindo consistência, segurança e boas práticas RESTful. Consultará o RAG para a [[02_Requisitos/ERS.md]] e o [[03_Arquitetura_e_Design/HLD.md]].
        
5. `@AgenteMentorDevFastAPI` **(Desenvolvedor Python/FastAPI)**
    
    - **Foco:** Desenvolvimento Backend.
        
    - **Tarefas:** Gerar código Python/FastAPI para endpoints, implementar lógica de negócios, interações com Supabase (usando SQLAlchemy ou ORM similar), e testes unitários (pytest). Consultará o RAG para especificações de API, LLDs e padrões de código seguro.
        
6. `@AgenteMentorDevFlutter` **(Desenvolvedor Flutter/Dart)**
    
    - **Foco:** Desenvolvimento Frontend (PWA).
        
    - **Tarefas:** Criar widgets de UI responsivos, implementar lógica de UI, gerenciamento de estado (Provider/Riverpod), chamadas à API backend, e testes unitários/widget. Consultará o RAG para especificações de API, LLDs e o [[03_Arquitetura_e_Design/STYLE_GUIDE.md]].
        
7. `@AgenteMentorDevJS` **(Desenvolvedor de Extensão Chrome - Pós-MVP)**
    
    - **Foco:** Desenvolvimento da Extensão de Navegador.
        
    - **Tarefas:** Implementar lógica de extração de dados de job boards (scraping ético e robusto), comunicação segura com o backend, e a UI da extensão. Consultará o RAG para a [[02_Requisitos/ERS.md]] (requisitos da extensão) e especificações de API.
        
8. `@AgenteMentorQA` **(Analista de QA/Testes)**
    
    - **Foco:** Garantia de Qualidade.
        
    - **Tarefas:** Gerar planos de teste ([[06_Qualidade_e_Testes/PGQ.md]]), casos de teste (em Gherkin, armazenados em [[06_Qualidade_e_Testes/Casos_de_Teste/]]) a partir de HUs/ACs, e gerar scripts de testes unitários e de integração. Consultará o RAG para [[02_Requisitos/ERS.md]], [[02_Requisitos/HU_AC/]], [[03_Arquitetura_e_Design/HLD.md]] e [[03_Arquitetura_e_Design/LLD/]].
        
9. `@AgenteMentorSeguranca` **(Analista de Segurança)**
    
    - **Foco:** Segurança de Código e Arquitetura.
        
    - **Tarefas:** Revisar código gerado e artefatos de design em busca de vulnerabilidades (OWASP Top 10, OWASP LLM Top 10), instruir outros agentes sobre práticas seguras, sugerir melhorias de segurança. Consultará o RAG para requisitos de segurança da [[02_Requisitos/ERS.md]] e padrões de código seguro.
        
10. `@AgenteMentorDocumentacao` **(Documentador Técnico)**
    
    - **Foco:** Documentação de Código e Manutenção da "Documentação Viva".
        
    - **Tarefas:** Gerar comentários e docstrings (Python Google Style, Dartdoc), explicar algoritmos complexos, auxiliar na sincronização da "Documentação Viva" no Obsidian e na curadoria/atualização da base de conhecimento para o RAG ([[08_Knowledge_Base_RAG_Sources/]]). Consultará o RAG para código, [[02_Requisitos/ERS.md]], [[03_Arquitetura_e_Design/HLD.md]] e [[03_Arquitetura_e_Design/LLD/]].
        

## 4. Arquitetura Técnica e Tecnologias

### 4.1. Stack Tecnológica Principal

Conforme definido na [[02_Requisitos/ERS.md]] (v0.5, Seção 2.4) e refinamentos:

- **Frontend (PWA):** **Flutter (Dart)** - Escolhido pela capacidade de construir PWAs robustas e visualmente consistentes, com boa performance e um ecossistema rico.
    
- **Backend:** **Python com FastAPI** - Selecionado pela rapidez de desenvolvimento, performance assíncrona, tipagem de dados com Pydantic e geração automática de documentação de API.
    
- **Banco de Dados:** **PostgreSQL (Via Supabase)** - Oferece a robustez do PostgreSQL com as facilidades de um BaaS.
    
- **Autenticação & Storage de Arquivos:** **Supabase** - Para simplificar o Backend as a Service, oferecendo autenticação JWT, gerenciamento de usuários e armazenamento de arquivos seguro.
    
- **IA LLM:** APIs **Google Gemini Pro e Flash** - Acessadas preferencialmente via **OpenRouter** para flexibilidade na escolha de modelos e gerenciamento de custos, ou diretamente se o Trae IDE oferecer integração otimizada. Gemini Pro para tarefas complexas (análise de CV, coaching avançado) e Gemini Flash para tarefas mais simples e rápidas (chatbot básico, categorização inicial, importação de vagas).
    
- **Parsing de PDF:**
    
    - Primário: **`pymupdf` (Fitz)** para extração de texto e metadados.
        
    - Fallback: **`Tesseract OCR`** (com modelos pt-BR de alta qualidade) para PDFs baseados em imagem.
        
    - Pós-processamento: **LLM (Gemini Flash/Pro)** para categorização semântica do texto extraído.
        
- **Vector DB (para RAG):** **FAISS** para implementação local inicial. Considerar **Supabase pgvector** como evolução Pós-MVP para maior integração.
    
- **Hospedagem:**
    
    - Frontend PWA (Flutter Web): **Vercel** (ou similar, ex: Netlify, Firebase Hosting).
        
    - Backend FastAPI (Python): **Render** (ou similar, ex: Fly.io, Google Cloud Run).
        
    - Supabase para BaaS.
        
- **Extensão de Navegador (Pós-MVP):** JavaScript, HTML, CSS - Padrão para desenvolvimento de extensões Chrome.
    

### 4.2. Ferramentas de Desenvolvimento e IA

- **IDE Principal e Agentes de IA:** **Trae IDE** - Plataforma central para codificação, interação com LLMs e implementação dos Agentes Mentores customizados. Suas funcionalidades de "Rules" ([[.trae/rules/user_rules.md]] e [[.trae/rules/project_rules.md]]) serão extensivamente utilizadas.
    
- **Acesso a LLMs:** **OpenRouter** - Gateway para acessar diversos modelos Gemini e, potencialmente, outros LLMs, facilitando testes e otimização de custos.
    
- **Documentação e Gestão de Conhecimento ("Documentação Viva"):** **Obsidian** - Para criar, organizar e interligar toda a documentação do projeto.
    
- **Controle de Versão:** **Git** (com repositório remoto no **GitHub** ou GitLab) - Para versionamento de toda a documentação e do código-fonte.
    
- **Gestão de Tarefas e Fluxo de Trabalho:** **Obsidian Kanban Plugin** - Para gerenciamento visual do backlog ([[KANBAN_Recoloca_AI.md]]).
    
- **Automação de Fluxos de Trabalho (CI/CD, Gatilhos):** **Pipedream** - Plataforma de automação para CI/CD, gatilhos para reindexar o RAG, notificações.
    
- **Prototipagem de UI (Opcional):** **FlutterFlow** - Pode ser utilizado para acelerar a criação de interfaces iniciais.
    

### 4.3. Arquitetura de Alto Nível (HLD) do Recoloca.ai

_O `@AgenteMentorArquitetoHLD` detalhará e manterá este HLD no arquivo [[03_Arquitetura_e_Design/HLD.md]]. Um esboço inicial dos componentes e suas interações é:_

1. **Frontend PWA (Flutter):** Interface do usuário principal, gerenciamento de estado, comunicação HTTPS/REST com o Backend API.
    
2. **Backend API (Python/FastAPI):** Lógica de negócios, validações, orquestração de chamadas para LLMs e Supabase. Comunicação HTTPS com Supabase e APIs Gemini (via OpenRouter).
    
3. **Supabase (BaaS):** Autenticação (JWT), Banco de Dados (PostgreSQL), Storage de arquivos.
    
4. **Google Gemini APIs (via OpenRouter):** Capacidades de IA para análise de texto, geração de sugestões, chatbot.
    
5. **Pipedream (Automação):** Orquestração de CI/CD, notificações, gatilhos para RAG.
    
6. **Sistema RAG Local (LangChain + FAISS):** Indexação da "Documentação Viva" para fornecer contexto aos Agentes de IA.
    
7. **Extensão de Navegador (Chrome - Pós-MVP):** Extração de dados de vagas, comunicação HTTPS com Backend API.
    

_(Um diagrama Mermaid.js detalhado será incluído e mantido no [[03_Arquitetura_e_Design/HLD.md]].)_
## 5. Gestão de Conhecimento e Contexto (RAG & Documentação Viva)

### 5.1. Estratégia RAG para o Recoloca.ai

Para garantir que os Agentes de IA Mentores operem com informações atualizadas, específicas do projeto e consistentes com a "Documentação Viva", será implementado um sistema de **Retrieval Augmented Generation (RAG)**.

- **Base de Conhecimento para RAG:** Localizada na pasta [[08_Knowledge_Base_RAG_Sources/]]. Conterá versões otimizadas para RAG da documentação do projeto.
    
- **Tecnologias RAG:**
    
    - **Framework:** **LangChain** (Python).
        
    - **Vector Store:** **FAISS** (local inicial), considerar Supabase pgvector (Pós-MVP).
        
    - **Embedding Model:** `all-MiniLM-L6-v2` (ou similar).
        
- **Processo de Indexação:** Script [[scripts/rag_indexer.py]] para monitorar, carregar, dividir, gerar embeddings e atualizar o índice FAISS.
    
- **Processo de Consulta (Retrieval) pelos Agentes:** Agentes no Trae IDE, via `@AgenteOrquestrador` ou diretamente, consultam o RAG.
    
- **Monitoramento e Refinamento do RAG:** Verificações periódicas da qualidade e relevância dos resultados.
    

### 5.2. A "Documentação Viva" no Obsidian e Git

Todo o conhecimento do projeto será mantido e interligado no **Obsidian**.

- **Estrutura de Pastas:** Conforme [[Apêndice A: Estrutura das Pastas]] do [[01_Guias_Centrais/GUIA_AVANCADO.md]].
    
- **Links Bidirecionais:** Uso intensivo de links wiki.
    
- **Controle de Versão:** Todo o vault do Obsidian será um repositório **Git**.
    
- **Atualização Contínua:** Documentação como processo orgânico, com auxílio do `@AgenteMentorDocumentacao` e curadoria final do Maestro.
    

## 6. Fluxo de Trabalho de Desenvolvimento e HITL

### 6.1. Fluxo de Trabalho Detalhado: Da ERS ao Deploy

O fluxo de trabalho será iterativo e incremental, seguindo os princípios ágeis.

1. **Planejamento da Iteração (Obsidian Kanban):** Maestro prioriza tarefas no [[KANBAN_Recoloca_AI.md]].
    
2. **Refinamento de Requisitos e Design (Colaborativo):** Maestro e Agentes (`@AgenteMentorPO`, `@AgenteMentorArquitetoHLD/LLD/API`) refinam HUs/ACs e criam artefatos de design.
    
3. **Desenvolvimento (Codificação Assistida):** Maestro delega tarefas aos `@AgentesMentoresDev`, que geram código. Maestro revisa (HITL), depura, refatora e implementa partes críticas.
    
4. **Testes e Garantia de Qualidade:** `@AgenteMentorQA` auxilia na geração de testes. Maestro supervisiona e valida.
    
5. **Documentação Contínua:** `@AgenteMentorDocumentacao` auxilia. Maestro garante atualizações.
    
6. **Integração e Deploy:** Código mesclado ao branch principal. CI/CD (Pipedream) para deploy.
    
7. **Revisão da Iteração e Feedback:** Maestro analisa resultados, feedback e desempenho dos agentes.
    

### 6.2. Modelo de Human-in-the-Loop (HITL) Evolutivo para o Recoloca.ai

O HITL evoluirá em fases, adaptando-se à maturidade dos agentes:

- **Fase 1: Supervisão Intensa e Detalhada (MVP Inicial)**
    
- **Fase 2: Autonomia Guiada e Revisão por Amostragem (Funcionalidades Maduras)**
    
- **Fase 3: Controle Supervisor e Foco Estratégico (Longo Prazo)**
    

O feedback do Maestro durante o HITL é crucial para o refinamento contínuo dos prompts e da base RAG.

### 6.3. Diagrama Visual do Fluxo de Trabalho (Mermaid.js)

_(Um diagrama Mermaid.js será mantido no arquivo [[03_Arquitetura_e_Design/FLUXO_TRABALHO_GERAL.md]].)_
## 7. Gestão de Projeto, Tarefas e Comunicação

### 7.1. Configuração e Uso do Obsidian Kanban

O gerenciamento de tarefas será centralizado no **Obsidian** utilizando o plugin **"Kanban"**, conforme arquivo [[KANBAN_Recoloca_AI.md]].

- **Estrutura de Colunas:** `🧊 Backlog Geral`, `🎯 A Fazer - Próxima Iteração`, `✍️ Preparação/Revisão - Maestro`, `🤖 Em Processamento - Agente IA`, `⚙️ Em Processamento - Maestro`, `🧐 Validação - Maestro (HITL)`, `✅ Concluído na Iteração`, `🚀 Deployado/Arquivado`.
    
- **Cartões (Tarefas):** Título claro, links essenciais, tags detalhadas (responsável, agente, fase HITL, tipo, prioridade, módulo).
    

### 7.2. Templates de Prompts e Engenharia de Prompt Contínua

A eficácia dos Agentes de IA depende da qualidade dos prompts.

- **Localização Centralizada:** [[05_Prompts/]] (`Templates_Base/` e `Prompts_Especificos/`).
    
- **Estrutura Detalhada dos Templates:** Metadados, PERSONA, CONTEXTO, TAREFA, RESTRIÇÕES, FORMATO DE SAÍDA.
    
- **Engenharia de Prompt Contínua:** Refinamento constante com base no desempenho e feedback HITL.
    

## 8. Próximos Passos Críticos (Pós-Alinhamento Documental)

Após o alinhamento deste Plano Mestre e do [[01_Guias_Centrais/GUIA_AVANCADO.md]] com a [[02_Requisitos/ERS.md]] v0.5, os próximos passos práticos imediatos, conforme detalhado na ERS, são:

1. **Validação Técnica da Arquitetura de Autenticação (Protótipo RLS FastAPI/Supabase)**
    
2. **Estimativa Detalhada de Custos Operacionais (API Gemini, Infraestrutura)**
    
3. **Validação Qualitativa com Usuários-Alvo (Protótipos de Baixa Fidelidade e Entrevistas)**
    

Estes passos são cruciais para mitigar riscos e validar premissas antes do desenvolvimento intensivo do MVP.
## 9. Apêndices

### 9.1. Glossário de Termos Específicos do Projeto e Metodologia

(Conforme versão 1.2, será revisado e atualizado se necessário no [[01_Guias_Centrais/GUIA_AVANCADO.md]] ou em um [[01_Guias_Centrais/GLOSSARIO_Recoloca_AI.md]] dedicado).

### 9.2. Referências Chave

(Conforme versão 1.2, será revisado e atualizado).

**FIM DO PLANO MESTRE RECOLOCA.AI (v1.3)**