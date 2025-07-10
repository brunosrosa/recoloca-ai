---
sticker: lucide//check
---
# PLANO MESTRE DO PROJETO RECOLOCA.AI

**Data de Criação**: 26 de maio de 2025

**Data de Última Atualização**: Janeiro de 2025

**Versão**: 1.1

**Autor Principal (Maestro)**: Bruno S. Rosa

**Assistência IA**: Gemini (Personalizado para colaboração e co-evolução)
## Sumário Executivo

Este **Plano Mestre** é o documento central e a **fonte da verdade** para o desenvolvimento, manutenção e evolução contínua do projeto **Recoloca.ai**. Ele consolida a visão estratégica, as decisões arquiteturais, o framework de "Desenvolvimento Solo Ágil Aumentado por IA", os fluxos de trabalho detalhados, as ferramentas selecionadas e o roadmap para a construção do Micro-SaaS Recoloca.ai. Este documento é uma **"Documentação Viva"**, mantida e atualizada no Obsidian e versionada com Git, servindo como guia para o desenvolvedor solo ("Maestro") e como base de conhecimento fundamental para seus Agentes de IA Mentores configurados no Trae IDE. Ele está alinhado com o [[docs/02_Requisitos/01_ERS.md]] (v0.5 ou mais recente) e o [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v0.9 ou mais recente).

## 1. Introdução ao Recoloca.ai

### 1.1. Visão Geral do Produto e Problema de Mercado

O **Recoloca.ai** é um Micro-SaaS inovador projetado para **transformar** a experiência de recolocação **profissional no Brasil**. O mercado de trabalho atual, especialmente no setor de tecnologia, é dinâmico e competitivo. Profissionais enfrentam desafios significativos como:

- Gerenciamento ineficiente de múltiplas candidaturas.
    
- Dificuldade em adaptar currículos de forma eficaz para cada vaga.
    
- Falta de preparo e confiança para entrevistas.
    
- Sensação de isolamento e falta de orientação durante o processo.

O Recoloca.ai visa solucionar essas dores oferecendo uma plataforma integrada que atua como o **"cockpit do candidato"**, combinando **uma landing page atrativa para aquisição de usuários**, **gerenciamento inteligente de candidaturas (Kanban)**, **otimização de currículos potencializada por Inteligência Artificial (IA)** e um **assistente de IA para coaching e suporte contextualizado**. Nosso objetivo é **transformar a experiência de recolocação profissional no Brasil**, empoderando os profissionais de TI Pleno/Sênior com ferramentas e orientação para que naveguem pelo processo com maior eficiência, estratégia e confiança, aumentando significativamente suas chances de sucesso e garantindo um alinhamento preciso com as demandas do mercado.

### 1.2. Propósito deste Plano Mestre

Este **Plano Mestre** serve como o **documento fundamental e unificador** para todas as fases do ciclo de vida do Recoloca.ai. Seu propósito é:

- **Consolidar a visão estratégica** e os objetivos de curto, médio e longo prazo do projeto.
    
- **Detalhar** a metodologia **de desenvolvimento** "Solo Ágil Aumentado por IA", adaptada às características do Maestro.
    
- **Definir a arquitetura de Agentes de** IA **Mentores** e sua implementação prática no Trae IDE, com destaque para o papel do `@AgenteM_Orquestrador` como PM Mentor.
    
- **Especificar a arquitetura técnica**, a stack tecnológica e as ferramentas de desenvolvimento e automação.
    
- **Estabelecer as práticas de gestão de conhecimento** através de uma "Documentação Viva" e um sistema RAG (Retrieval Augmented Generation).
    
- **Delinear os fluxos de trabalho de desenvolvimento**, o modelo de Human-in-the-Loop (HITL) evolutivo e a gestão de tarefas.
    
- **Servir** como guia para a configuração inicial do **ambiente** e como roadmap para o desenvolvimento do MVP e iterações subsequentes.

Este documento será a **referência central** para o desenvolvedor "Maestro" e a principal fonte de contexto para os Agentes de IA.

### 1.3. Objetivos e Escopo do MVP (Produto Mínimo Viável)

**Objetivo Principal do MVP:** Validar a proposta de valor central do Recoloca.ai – auxiliar profissionais a gerenciar candidaturas, otimizar currículos com IA e receber coaching básico – focando inicialmente em profissionais de tecnologia no Brasil, e coletar feedback para guiar a evolução do produto.

**Funcionalidades Centrais do MVP (Conforme [[docs/02_Requisitos/01_ERS.md]] v0.5):**

1. **Landing Page e Marketing `RF-LAND`:**
    
    - Página inicial atrativa e informativa para visitantes não autenticados.
        
    - Seção Hero com headline impactante e call-to-action (CTA) principal para registro.
        
    - CTA proeminente para registro de novos usuários com texto persuasivo.
        
    - Apresentação clara das principais funcionalidades do produto (Kanban, Otimização de CV, AI Coach).
        
    - Informações sobre planos (Gratuito vs Premium) e seus benefícios.
        
    - Design responsivo otimizado para dispositivos móveis e desktop.
        
    - Elementos de credibilidade e confiança (depoimentos, estatísticas, badges de segurança).
        
2. **Gerenciamento de Candidaturas (Kanban) `RF-KAN`:**
    
    - Criação, visualização, edição e exclusão de cartões de vagas.
        
    - Campos do cartão: Título da Vaga, Empresa, Link Original, Status (coluna), Data de Adição, Prioridade, Anotações (Markdown), Localização, Modalidade, Data de Publicação/Captura, Origem, Score de Adequação (se calculado), Prazo.
        
    - Colunas fixas e ordenadas: "Salvas", "Radar de Interesse", "Aplicadas", "Entrevista(s)", "Teste(s)", "Proposta", "Recusada/Fechada".
        
    - Movimentação de cartões via drag-and-drop.
        
    - Filtros e ordenação de cartões.
        
    - Registro de histórico de interações por vaga.
        
    - Dashboard de métricas pessoais (funil de candidatura).
        
    - Limite de 10 vagas ativas para o tier gratuito.
        
3. **Importação Inteligente de Vagas `RF-IMP` (MVP):**
    
    - Importação de vaga colando a URL da página da vaga.
        
    - IA (LLM) tenta extrair informações relevantes (Título, Empresa, Descrição, Requisitos, Localização, Modalidade, Idioma - PT, EN, ES).
        
    - Permite ao usuário revisar, editar e complementar os dados extraídos antes de salvar.
        
4. **Otimização de Currículo Baseada em IA `RF-CV`:**
    
    - Upload e gerenciamento de múltiplos currículos base (PDF - PT, EN, ES no MVP).
        
    - Extração de texto (pymupdf/Tesseract) e categorização semântica das seções via LLM.
        
    - Revisão, edição e validação obrigatória do conteúdo extraído pelo usuário ("Currículo Base Ativo").
        
    - Análise de adequação do "Currículo Base Ativo" com a descrição da vaga (Score de Adequação IA).
        
    - Sugestões específicas e contextualizadas para otimizar o currículo para a vaga.
        
    - Estimativa de range salarial para a vaga (IA + RAG de pesquisas salariais).
        
    - Download do currículo otimizado em PDF (templates profissionais ATS-friendly).
        
    - Gerenciamento de versões e atualização do "Currículo Base Ativo".
        
    - Limite de 3 "Otimizações Completas" por mês para o tier gratuito.
        
5. **Assistente de IA para Coaching Básico `RF-COACH`:**
    
    - Interface de chatbot interativo.
        
    - IA Coach (Gemini Flash para gratuito, Pro para pago) com persona definida (Animado, inspirador, empático, prático, especialista em recolocação BR).
        
    - Respostas baseadas em RAG (base de conhecimento curada) e contexto do usuário.
        
    - Atuação proativa (incentivar atualização no Kanban, dicas contextuais).
        
    - Orientações sobre soft skills, tendências de mercado, preparação para entrevistas.
        
    - Uso de métricas do usuário para identificar gargalos e sugerir foco.
        
    - Limite de 15 interações/dia para o tier gratuito.
        
5. **Autenticação e Gerenciamento de Conta `RF-AUTH`:**
    
    - Cadastro com Email/Senha, confirmação de email.
        
    - Login seguro (proteção brute-force).
        
    - Redefinição de senha.
        
    - Onboarding inicial (Nome, upload do Currículo Base).
        
    - Diferenciação de tiers (gratuito/premium).
        
    - Edição de perfil, gerenciamento de currículos base, preferências de notificação.
        
    - Visualização e gerenciamento de assinatura.
        
    - Exclusão de conta e dados (LGPD).
        
6. **Modelo Freemium e Pagamentos `RF-PAY-SUB`:**
    
    - Definição clara dos limites do plano gratuito e benefícios do plano premium.
        
    - Integração com gateway de pagamento seguro para assinaturas recorrentes.
        

**Visão de Evolução (Pós-MVP - Breve Menção, conforme [[docs/02_Requisitos/01_ERS.md]] v0.5):**

- **Extensão de Navegador (Web Clipper):** Para captura de vagas do LinkedIn (`RF-IMP-003`).
    
- **Autenticação Multifator (MFA):** Via TOTP (`RF-AUTH-004`).
    
- **Templates Avançados de Currículo e Customização (Tier Pago):** (`RF-CV-009`, Tier Pago).
    
- **Análises de Currículo Mais Detalhadas (Tier Pago):** (`RF-CV-009`, Tier Pago).
    
- **Treino Aprofundado para Entrevistas com IA (Tier Pago):** (`RF-COACH-006`, Tier Pago).
    
- Suporte a mais idiomas na interface.
    
- Funcionalidades de networking simplificado.
    
- Biblioteca de recursos curada.
    
- Modo "Manutenção de Carreira" e "Projetos de Carreira".
    
### 1.4. Público-Alvo

- **Primário:** Profissionais brasileiros, com foco inicial do MVP em **profissionais de TI Pleno/Sênior** (desenvolvedores, analistas, QAs, designers, gerentes de produto, etc.) que estão ativamente buscando uma nova oportunidade de emprego ou em transição de carreira.
    
- **Secundário:** Profissionais brasileiros de diversas áreas que desejam se manter preparados para futuras oportunidades, otimizar seus currículos e melhorar suas habilidades de entrevista.

**Características Esperadas:** Familiaridade com navegação na web, uso de aplicativos online e abertura para utilizar ferramentas baseadas em Inteligência Artificial. Valorizam a eficiência, a orientação personalizada, uma UX superior e a melhoria contínua.

## 2. Metodologia e Framework de Desenvolvimento Adotados

### 2.1. O Modelo "Desenvolvimento Solo Ágil Aumentado por IA"

A metodologia de desenvolvimento adotada para o Recoloca.ai é o **"Desenvolvimento Solo Ágil Aumentado por Inteligência Artificial"**, conforme detalhado conceitualmente no documento [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.3). Esta abordagem reinterpreta os princípios ágeis e a colaboração com IA para o contexto de um desenvolvedor individual com características neurodivergentes (TDAH/AHSD), visando maximizar a produtividade e o bem-estar.

**Princípios Chave (Resumo do [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] v2.3):**

- O desenvolvedor solo atua como um **"Maestro"** de uma orquestra de **Agentes de IA especializados ("Mentores")**.
    
- A IA transcende a função de ferramenta de codificação, tornando-se um **multiplicador de força** e um **parceiro de sparring intelectual** em todas as fases do SDLC.
    
- Foco na **automação** de **tarefas repetitivas** e aceleração do desenvolvimento, permitindo que o "Maestro" se concentre em desafios estratégicos, criativos e de maior valor agregado.
    
- Utilização de **Agentes de IA como especialistas virtuais** em diversas áreas (arquitetura, UX, segurança, etc.), complementando as habilidades do desenvolvedor solo e desafiando premissas. O `@AgenteM_Orquestrador` assume um papel chave como PM Mentor.
    
- Ênfase na **Documentação Viva** como fonte da verdade, gerenciada via RAG e acessível tanto ao Maestro quanto aos Agentes.
    
- Implementação de um ciclo de **Human-in-the-Loop (HITL)** evolutivo, que se adapta à confiança e ao desempenho dos agentes, equilibrando supervisão e autonomia.
    
- **Métricas de "Specialized Intelligence"** para avaliar a eficácia da orquestração: eficiência de orquestração (tempo de resposta dos agentes, taxa de automação, precisão de handoffs), qualidade do sistema RAG (precisão de retrieval, cobertura da base RAG, tempo de indexação) e satisfação/produtividade (satisfação do Maestro, redução de context switching, aceleração de desenvolvimento).
    
- **Critérios objetivos para agentes "Production-Ready"** em três tiers (Básicos, Intermediários, Avançados) que incluem precisão de output, tempo de resposta, capacidade de contextualização, integração com RAG e autonomia operacional.
    
### 2.2. Papel do Desenvolvedor como "Maestro"

No modelo adotado, o desenvolvedor solo (Eu, Bruno S. Rosa) assume o papel de **"Maestro"**. As responsabilidades incluem:

- **Definir a visão estratégica** e os objetivos de negócio e de produto, utilizando o `@AgenteM_Orquestrador` (atuando como PM Mentor e PO) para refinar, validar essa visão e traduzi-la em requisitos acionáveis.
    
- **Priorizar o backlog** de funcionalidades e tarefas, alinhando-as com os objetivos estratégicos, com o `@AgenteM_Orquestrador` (atuando como PM Mentor e PO) fornecendo insights e facilitando a priorização.
    
- **Orquestrar os Agentes de IA Mentores**, projetando e refinando seus prompts base, templates e fornecendo contexto rico através do RAG e de instruções diretas, com o `@AgenteM_Orquestrador` (atuando como PM Mentor, PO e Engenheiro de Prompt) como principal assistente e facilitador nesta tarefa.
    
- **Supervisionar, validar e refinar** o trabalho gerado pelos Agentes de IA (HITL), atuando como o principal ponto de controle de qualidade e alinhamento.
    
- **Tomar decisões arquiteturais** e de design críticas, utilizando os agentes como consultores e para explorar alternativas.
    
- **Desenvolver componentes complexos**, realizar integrações críticas ou tarefas que exijam um nível de nuance, criatividade ou julgamento ético que a IA ainda não alcança.
    
- **Gerenciar e curar a "Documentação Viva"** e a base de conhecimento RAG, garantindo sua precisão e relevância.
    
- **Aprender e evoluir continuamente** na arte da engenharia de prompts, na orquestração de agentes e na colaboração efetiva com sistemas de IA.
    
- **Manter o foco no valor para o usuário** e nos objetivos de negócio, garantindo que a tecnologia sirva a esses propósitos.
    
- **Gerenciar o próprio fluxo de trabalho e energia**, utilizando ferramentas e técnicas que se alinhem com suas características neurodivergentes para manter o foco e a produtividade.
    
### 2.3. Visão Geral do SDLC Ágil Adaptado para o Recoloca.ai

O Ciclo de Vida de Desenvolvimento de Software (SDLC) Ágil tradicional é adaptado para incorporar a colaboração intensiva com Agentes de IA Mentores, com ênfase em ciclos curtos e feedback rápido. O `@AgenteM_Orquestrador` (atuando como PM Mentor) desempenha um papel crucial no início de cada ciclo para alinhar a estratégia antes da execução:

1. **Concepção e Refinamento Estratégico de Ideias/Requisitos:**
    
    - Maestro identifica necessidades/oportunidades ou refina itens do backlog.
        
    - Interação com `@AgenteM_Orquestrador` (atuando como PM Mentor e PO) para validar a estratégia da ideia/requisito sob a ótica de Product Management (alinhamento com objetivos, valor para o usuário, métricas) e para traduzir esses insights em Histórias de Usuário (HUs) e Critérios de Aceite (ACs) claros e acionáveis, a partir do [[docs/02_Requisitos/01_ERS.md]].

- Maestro valida e refina HUs/ACs co-criados com o `@AgenteM_Orquestrador`.
        
2. **Design (HLD/LLD/API/UX/UI):**
    
    - Maestro define diretrizes de design.
        
    - `@AgenteM_ArquitetoTI`, `@AgenteMentorAPI`, `@AgenteMentorUIDesign`, `@AgenteMentorUX` auxiliam na criação de artefatos de design, com o `@AgenteM_Orquestrador` facilitando a comunicação e garantindo que o contexto estratégico seja mantido.
        
    - Maestro valida, itera e aprova os designs.
        
3. **Desenvolvimento (Codificação):**
    
    - `@AgentesMentoresDev` (Flutter, FastAPI), guiados pelo `@AgenteM_Orquestrador` e pelos LLDs/APIs, geram código boilerplate, componentes e lógica de negócios.
        
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
        
    - Análise de feedback e métricas para identificar melhorias e novas funcionalidades, alimentando o backlog, com apoio do `@AgenteM_Orquestrador` na análise estratégica.
        
    - O sistema RAG é continuamente atualizado com novos aprendizados e documentação, refinando o conhecimento dos agentes.
        
    - O ciclo recomeça.
        
## 3. Arquitetura de Agentes de IA Mentores

O Recoloca.ai operará com uma equipe de Agentes de IA Mentores especializados, cada um focado em uma área específica do ciclo de vida de desenvolvimento de software (SDLC) e da gestão de produto. Esta abordagem visa simular uma equipe multidisciplinar sênior, onde o Maestro (o desenvolvedor solo) atua como líder técnico, gestor de produto e principal ponto de integração.

A colaboração entre esses agentes é fundamental. Por exemplo, na criação de uma nova funcionalidade, o `@AgenteM_Orquestrador` trabalharia com o Maestro para definir a estratégia e os requisitos. Em seguida, o `@AgenteM_ArquitetoTI` poderia ser consultado para o design da solução, o `@AgenteM_API` para a especificação da interface, os agentes de desenvolvimento (`@AgenteM_DevFastAPI`, `@AgenteM_DevFlutter`) para a codificação, o `@AgenteM_QA` para os testes, e o `@AgenteM_Documentacao` para registrar o conhecimento gerado. Esse fluxo, orquestrado pelo Maestro com o suporte do `@AgenteM_Orquestrador`, visa garantir consistência e eficiência.

### 3.1. O Agente Orquestrador de Prompts e Mentor de Product Management

Este é o **primeiro e mais crucial agente**, atuando como um "meta-agente" ou "agente de interface" entre o Maestro e os demais Agentes Mentores, e como o principal **PM Mentor** do Maestro.

- **Persona no Trae IDE:** `@AgenteM_Orquestrador`
    
- **Papel Principal:** "Product Manager Mentor Sênior, Product Owner (PO) e Engenheiro de Prompt Especialista".
    
- **Objetivo:**
    
    1. Auxiliar o Maestro a aplicar consistentemente os princípios de Product Management (descoberta, estratégia, priorização, definição de valor) e as responsabilidades de Product Owner (definição e gestão do backlog, escrita de HUs/ACs) ao longo do ciclo de vida do Recoloca.ai.
        
    2. Auxiliar o Maestro a formular instruções (prompts) claras, precisas, contextualmente ricas e otimizadas para os outros Agentes Mentores, atuando como um especialista em engenharia de prompt.
        
    3. Garantir que os requisitos estratégicos sejam traduzidos em um backlog de produto claro, priorizado e pronto para o desenvolvimento pelos Agentes Mentores Dev.
        
- **Funcionalidades (Conforme [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] v2.3, Seção 3.2):**
    
    1. **Análise da Documentação Estratégica e Tática (via RAG):** Processa e "compreende" documentos chave do projeto (Plano Mestre, ERS, HLD, materiais de PM) para extrair contexto relevante.
        
    2. **Geração de Perguntas Estratégicas e Esclarecedoras (com viés de PM):** Antes de focar no prompt para um agente executor, formula perguntas ao Maestro para validar o "porquê", o problema do usuário, a UVP, métricas de sucesso, riscos e priorização.
        
    3. **Criação Assistida de Prompts Eficazes:** Após o diálogo estratégico com o Maestro, auxilia na montagem de prompts detalhados e estruturados para os agentes de destino, incorporando o contexto estratégico validado, referências diretas à documentação, sugerindo técnicas de engenharia de prompt e utilizando os templates de [[../05_Prompts/01_Templates_Base/]].
        
- **Implementação no Trae IDE:**
    
    - Será um agente customizado com um prompt base que o instrui sobre suas funções de PM Mentor e Engenheiro de Prompt, tom de voz colaborativo, questionador e proativo.
        
    - Utilizará a capacidade do Trae IDE de acessar o contexto do projeto e se integrará com o sistema RAG (que incluirá materiais de PM).
        
    - O Maestro interagirá com ele em um fluxo conversacional para primeiro validar a estratégia e depois co-criar o prompt otimizado.
        
### 3.2. Detalhamento dos Agentes Mentores por Fase do SDLC

Os seguintes Agentes Mentores serão configurados no Trae IDE, cada um com uma persona, conjunto de habilidades (definidas pelo prompt base, [[../../.trae/rules/project_rules.md]] e contexto RAG) e utilizando templates de prompts específicos de [[../05_Prompts/01_Templates_Base/]]. A referência principal para seus papéis é a **Tabela Essencial do [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] v2.3**. Nota: A referência ao `GUIA_AVANCADO.md` aqui está correta, pois é um documento central.

1. `@AgenteM_Orquestrador` **(Product Manager Mentor, Product Owner e Engenheiro de Prompt Especialista):**
    
    - **Foco:** Mentoria em Product Management, Definição e Refinamento de Requisitos (Product Ownership), e Engenharia de Prompts para outros agentes. Atua como o **hub central de comunicação e tradução estratégica**, garantindo que a visão do Maestro seja consistentemente transmitida, compreendida e implementada pelos demais agentes.
        
    - **Tarefas:** Colaborar com o Maestro na validação estratégica de ideias e requisitos; traduzir a estratégia em Histórias de Usuário (HUs) detalhadas (armazenadas em [[../02_Requisitos/HU_AC/]]) e Critérios de Aceite (ACs) precisos, baseando-se no [[../02_Requisitos/ERS.md]]; gerenciar e priorizar o backlog do produto; co-criar com o Maestro prompts otimizados para os demais Agentes Mentores, garantindo que o contexto estratégico e os requisitos táticos sejam claramente comunicados. É o principal facilitador para que a "intenção" do Maestro se materialize de forma coesa através da orquestra de agentes.
        
2. `@AgenteM_ArquitetoTI` **(Arquiteto de TI Completo - HLD + LLD):**
    
    - **Foco:** Arquitetura Completa (Alto e Baixo Nível).
        
    - **Tarefas:** Criar/otimizar o [[../03_Arquitetura_e_Design/HLD.md]], gerar diagramas de arquitetura (componentes, interações) em Mermaid.js, definir interações entre módulos e com sistemas externos, identificar riscos arquiteturais, detalhar classes, funções, modelos de dados e algoritmos para os módulos em [[../03_Arquitetura_e_Design/03_LLDs/]], criar diagramas de sequência e de classes em Mermaid.js.
        
4. `@AgenteM_API` **(Arquiteto de APIs):**
    
    - **Foco:** Especificação de APIs.
        
    - **Tarefas:** Gerar e manter as especificações OpenAPI 3.0 em YAML (ex: [[../03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]) para os serviços de backend.
        
5. `@AgenteM_DevFastAPI` **(Desenvolvedor Python/FastAPI):**
    
    - **Foco:** Desenvolvimento Backend.
        
    - **Tarefas:** Gerar código Python/FastAPI para endpoints, implementar lógica de negócios, interações com Supabase, e testes unitários (pytest).
        
6. `@AgenteM_DevFlutter` **(Desenvolvedor Flutter/Dart):**
    
    - **Foco:** Desenvolvimento Frontend (PWA).
        
    - **Tarefas:** Criar widgets de UI responsivos, implementar lógica de UI, gerenciamento de estado (Provider/Riverpod), chamadas à API backend, e testes unitários/widget.
        
7. `@AgenteM_DevJS` **(Desenvolvedor de Extensão Chrome - Pós-MVP):**
    
    - **Foco:** Desenvolvimento da Extensão de Navegador.
        
    - **Tarefas:** Implementar lógica de extração de dados de job boards, comunicação segura com o backend, e a UI da extensão.
        
8. `@AgenteM_QA` **(Analista de QA/Testes):**
    
    - **Foco:** Garantia de Qualidade.
        
    - **Tarefas:** Gerar planos de teste ([[../06_Qualidade_e_Testes/PGQ.md]]), casos de teste (em Gherkin, armazenados em [[../06_Qualidade_e_Testes/Casos_de_Teste/]]), e gerar scripts de testes unitários e de integração.
        
9. `@AgenteM_Seguranca` **(Analista de Segurança):**
    
    - **Foco:** Segurança de Código e Arquitetura.
        
    - **Tarefas:** Revisar código gerado e artefatos de design em busca de vulnerabilidades (OWASP Top 10, OWASP LLM Top 10), instruir outros agentes sobre práticas seguras, sugerir melhorias de segurança.
        
10. `@AgenteM_Documentacao` **(Documentador Técnico):**
    
    - **Foco:** Documentação de Código e Manutenção da "Documentação Viva".
        
    - **Tarefas:** Gerar comentários e docstrings (Python Google Style, Dartdoc), explicar algoritmos complexos, auxiliar na sincronização da "Documentação Viva" no Obsidian e na curadoria/atualização da base de conhecimento para o RAG ([[../../rag_infra/source_documents/]]).
        
11. `@AgenteM_DevOps` **(DevOps Engineer - Conceitual):**
    
    - **Foco:** Integração Contínua e Deploy.
        
    - **Tarefas:** Gerar scripts de CI/CD (conceituais), configurações de deploy, e instruções para automação via Pipedream.
        
12. `@AgenteM_UIDesigner` **(UI Designer):**
    
    - **Foco:** Design de Interface de Usuário.
        
    - **Tarefas:** Criar wireframes, mockups, protótipos de alta fidelidade, definir sistema de design (cores, tipografia, componentes), gerar especificações visuais para desenvolvedores.
        
13. `@AgenteM_UXDesigner` **(UX Designer):**
    
    - **Foco:** Design de Experiência do Usuário.
        
    - **Tarefas:** Conduzir pesquisa de usuário, criar personas, mapas de jornada do usuário, fluxos de usuário, protótipos interativos, testes de usabilidade.
        
14. `@AgenteM_Performance` **(Analista de Performance):**
    
    - **Foco:** Análise e Otimização de Performance.
        
    - **Tarefas:** Identificar gargalos de performance, sugerir otimizações de código e arquitetura, definir métricas de performance, gerar relatórios de análise.
        
## 4. Arquitetura Técnica e Tecnologias

### 4.1. Stack Tecnológica Principal

Conforme definido no [[docs/02_Requisitos/01_ERS.md]] (v0.5, Seção 2.4) e refinamentos:

- **Frontend (PWA):** **Flutter (Dart)**
    
- **Backend:** **Python com FastAPI**
    
- **Banco de Dados:** **PostgreSQL (Via Supabase)**
    
- **Autenticação & Storage de Arquivos:** **Supabase** (incluindo Google OAuth e gerenciamento de IDs de cliente/assinatura Stripe)
    
- **IA LLM:** APIs **Google Gemini Pro e Flash** (via OpenRouter ou diretamente)
    
- **Parsing de PDF:**
    
    - Primário: **`pymupdf` (Fitz)**
        
    - Fallback: **`Tesseract OCR`** (com modelos pt-BR)
        
    - Pós-processamento: **LLM (Gemini Flash/Pro)** para categorização semântica.
        
- **Vector DB (para RAG):** **FAISS-GPU** (local inicial, utilizando CUDA). Considerar **Supabase pgvector** (Pós-MVP).
    
- **Embedding Model (para RAG):** **`BAAI/bge-m3`** (via Sentence Transformers).

### 4.1.1. Estratégia de Banco de Dados (PostgreSQL/Supabase)

A escolha do PostgreSQL, acessado e gerenciado via Supabase, oferece uma base de dados relacional robusta e escalável, com funcionalidades adicionais de BaaS (Backend as a Service) que simplificam o desenvolvimento.

-   **Modelo de Dados Inicial:** As entidades centrais do MVP incluirão:
    -   `Usuarios`: Informações de perfil, autenticação (incluindo ID do provedor OAuth, ex: Google User ID), preferências, ID de cliente Stripe, status da assinatura Stripe.
    -   `Curriculos`: Dados estruturados e não estruturados dos currículos dos usuários, incluindo versões.
    -   `Vagas`: Informações sobre oportunidades de emprego, extraídas ou cadastradas.
    -   `Candidaturas`: Rastreamento das interações entre usuários/currículos e vagas.
    -   `TokensUsoAPI`: Para gerenciamento de cotas de uso das funcionalidades de IA (vinculado ao nível de assinatura).
    -   `Assinaturas`: Detalhes das assinaturas dos usuários (nível, data de início, data de término, status, ID da assinatura Stripe).
-   **Segurança:** Será implementada Row Level Security (RLS) no Supabase para garantir que os usuários acessem apenas seus próprios dados, reforçando a privacidade e a conformidade com a LGPD.
-   **Escalabilidade:** Supabase permite um crescimento gerenciado, começando com um plano gratuito e escalando conforme a necessidade. A natureza relacional do PostgreSQL suporta consultas complexas e integridade de dados.
-   **Extensões:** O uso de `pgvector` via Supabase é uma consideração Pós-MVP para otimizar o armazenamento e consulta de embeddings diretamente no banco de dados, potencialmente simplificando a arquitetura RAG.
    
- **Hospedagem:**
    
    - Frontend PWA (Flutter Web): **Vercel** (ou similar).
        
    - Backend FastAPI (Python): **Render** (ou similar).
        
    - Supabase para BaaS.
        
- **Extensão de Navegador (Pós-MVP):** JavaScript, HTML, CSS (Chrome).
    
### 4.2. Ferramentas de Desenvolvimento e IA

- **IDE Principal e Agentes de IA:** **Trae IDE**
    
- **Acesso a LLMs:** **OpenRouter**
    
- **Documentação e Gestão de Conhecimento:** **Obsidian**
    
- **Controle de Versão:** **Git** (com repositório remoto no **GitHub** ou GitLab)
    
- **Gestão de Tarefas e Fluxo de Trabalho:** **Obsidian Kanban Plugin** ([[../00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]])
    
- **Automação de Fluxos de Trabalho (CI/CD, Gatilhos):** **Pipedream**
    
- **Prototipagem de UI (Opcional):** **FlutterFlow**
    
- **Framework para RAG:** **LangChain** (Python)
    
- **Biblioteca para Embeddings:** **Sentence Transformers** (Python)
    
### 4.3. Arquitetura de Alto Nível (HLD) do Recoloca.ai

_O `@AgenteM_ArquitetoTI` detalhará e manterá este HLD no arquivo [[../03_Arquitetura_e_Design/HLD.md]]. Um esboço inicial dos componentes e suas interações é:_

1. **Frontend PWA (Flutter):** Interface do usuário, gerenciamento de estado, comunicação HTTPS/REST com Backend API.
    
2. **Backend API (Python/FastAPI):** Lógica de negócios, validações, orquestração de chamadas para LLMs e Supabase.
    
3. **Supabase (BaaS):** Autenticação (JWT, Google OAuth), Banco de Dados (PostgreSQL com dados de usuário, currículos, vagas, candidaturas, tokens, assinaturas Stripe), Storage de arquivos.
    
4. **Google Gemini APIs (via OpenRouter):** Capacidades de IA.
    
5. **Pipedream (Automação):** CI/CD, notificações, gatilhos RAG.
    
6. **Sistema RAG Local (LangChain + FAISS-GPU + Sentence Transformers):** Indexação da "Documentação Viva" utilizando o modelo `BAAI/bge-m3`.
    
7. **Extensão de Navegador (Chrome - Pós-MVP):** Extração de dados, comunicação com Backend API.

_(Um diagrama Mermaid.js detalhado será incluído e mantido no [[../03_Arquitetura_e_Design/HLD.md]].)_

## 5. Gestão de Conhecimento e Contexto (RAG & Documentação Viva)

### 5.1. Estratégia RAG para o Recoloca.ai

Para garantir que os Agentes de IA Mentores operem com informações atualizadas, específicas do projeto e consistentes com a "Documentação Viva", será implementado um sistema de **Retrieval Augmented Generation (RAG)**.

- **Base de Conhecimento para RAG:** Localizada na pasta [[../../rag_infra/source_documents/]]. Conterá versões otimizadas para RAG da documentação do projeto (ex: [[../../rag_infra/source_documents/02_Requisitos_e_Especificacoes/ERS_para_RAG.md]]) e materiais de referência (ex: [[../../rag_infra/source_documents/07_Conhecimento_Especializado/PM_Knowledge/]] para o `@AgenteM_Orquestrador`).
    
- **Tecnologias RAG:**
    
    - **Framework:** **LangChain** (Python).
        
    - **Vector Store:** **FAISS-GPU** (local inicial, utilizando CUDA para aceleração). Considerar Supabase pgvector (Pós-MVP).
        
    - **Embedding Model:** **`BAAI/bge-m3`**. Este modelo será carregado e utilizado através da biblioteca **Sentence Transformers**.
        
    - **Bibliotecas Adicionais:** `pymupdf` para extração de texto de PDFs na base de conhecimento, se necessário.
        
- **Processo de Indexação:** Script [[../../rag_infra/core_logic/rag_indexer.py]] para monitorar, carregar documentos (Markdown, PDF), dividir em chunks, gerar embeddings usando `BAAI/bge-m3` via Sentence Transformers, e atualizar o índice FAISS-GPU.
    
- **Processo de Consulta (Retrieval) pelos Agentes:** Agentes no Trae IDE, via `@AgenteM_Orquestrador` ou diretamente, consultam o RAG. A consulta do usuário é convertida em um embedding (usando o mesmo modelo `BAAI/bge-m3`), os chunks mais relevantes são recuperados do índice FAISS-GPU, e esses chunks são injetados no prompt do LLM (Gemini) para fornecer contexto.
    
- **Monitoramento e Refinamento do RAG:** Verificações periódicas da qualidade e relevância dos resultados. O feedback do Maestro durante o HITL será usado para refinar os chunks, a estratégia de splitting ou até mesmo considerar a reindexação com parâmetros ajustados. A qualidade e a curadoria contínua dos `source_documents` são cruciais: documentos desatualizados, mal formatados ou irrelevantes podem degradar significativamente a performance do sistema RAG, levando a respostas imprecisas ou enganosas por parte dos agentes.
    
### 5.2. A "Documentação Viva" no Obsidian e Git

Todo o conhecimento do projeto será mantido e interligado no **Obsidian**.

- **Estrutura de Pastas:** Conforme [[docs/01_Guias_Centrais/GUIA_AVANCADO.md#Apêndice A: Estrutura das Pastas]]. Nota: A referência ao `GUIA_AVANCADO.md` aqui está correta, pois é um documento central.
    
- **Links Bidirecionais:** Uso intensivo de links wiki (formato `[[docs/Caminho/Arquivo.md]]`).
    
- **Controle de Versão:** Todo o vault do Obsidian será um repositório **Git**.
    
- **Atualização Contínua:** Documentação como processo orgânico, com auxílio do `@AgenteM_Documentacao` e curadoria final do Maestro. A "Documentação Viva" transcende um mero repositório de informações; ela é uma ferramenta estratégica ativa. Ao centralizar e interconectar o conhecimento do projeto, reduz a carga cognitiva do Maestro, minimiza a necessidade de repetir explicações, acelera o onboarding de "novas instâncias" de agentes (ou do próprio Maestro ao revisitar partes do projeto) e serve como a fonte da verdade para o sistema RAG, garantindo que os agentes operem com o contexto mais preciso e atualizado.
    
## 6. Fluxo de Trabalho de Desenvolvimento e HITL

### 6.1. Fluxo de Trabalho Detalhado: Da ERS ao Deploy

O fluxo de trabalho será iterativo e incremental, seguindo os princípios ágeis.

1. **Planejamento da Iteração (Obsidian Kanban):** Maestro prioriza tarefas no [[../00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]].
    
2. **Refinamento Estratégico e de Requisitos (Colaborativo):** Maestro e `@AgenteM_Orquestrador` validam a estratégia e refinam HUs/ACs, integrando as funções de PM e PO.
    
3. **Design (Colaborativo):** Maestro e Agentes de Design (`@AgenteM_ArquitetoTI`, `@AgenteM_API`) criam artefatos de design.
    
4. **Desenvolvimento (Codificação Assistida):** Maestro delega tarefas aos `@AgentesMentoresDev` (ex: `@AgenteM_DevFastAPI`, `@AgenteM_DevFlutter`), que geram código. Maestro revisa (HITL), depura, refatora e implementa partes críticas.
    
5. **Testes e Garantia de Qualidade:** `@AgenteM_QA` auxilia na geração de testes. Maestro supervisiona e valida.
    
6. **Documentação Contínua:** `@AgenteM_Documentacao` auxilia. Maestro garante atualizações.
    
7. **Integração e Deploy:** Código mesclado ao branch principal. CI/CD (Pipedream) para deploy.
    
8. **Revisão da Iteração e Feedback:** Maestro analisa resultados, feedback e desempenho dos agentes.
    
### 6.2. Modelo de Human-in-the-Loop (HITL) Evolutivo para o Recoloca.ai

O HITL evoluirá em fases, adaptando-se à maturidade dos agentes, conforme detalhado no [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.3, Seção 6): Nota: A referência ao `GUIA_AVANCADO.md` aqui está correta, pois é um documento central.

- **Fase 1: Supervisão Intensa e Detalhada (MVP Inicial)**
    
- **Fase 2: Autonomia Guiada e Revisão por Amostragem (Funcionalidades Maduras)**
    
- **Fase 3: Controle Supervisor e Foco Estratégico (Longo Prazo)**

O feedback do Maestro durante o HITL é crucial para o refinamento contínuo dos prompts e da base RAG.

### 6.3. Diagrama Visual do Fluxo de Trabalho (Mermaid.js)

_(Um diagrama Mermaid.js será mantido no arquivo [[../03_Arquitetura_e_Design/FLUXO_TRABALHO_GERAL.md]].)_

## 7. Gestão de Projeto, Tarefas e Comunicação

### 7.1. Configuração e Uso do Obsidian Kanban e Métricas de Sucesso

O gerenciamento de tarefas será centralizado no **Obsidian** utilizando o plugin **"Kanban"**, conforme arquivo [[../00_Gerenciamento_Projeto/KANBAN_INTERNO_PROJETO.md]]. Este Kanban será fundamental para acompanhar o progresso em direção aos objetivos do MVP, cujas métricas de sucesso estão detalhadas no documento [[METRICAS_SUCESSO_BASE_MERCADO]].

- **Estrutura de Colunas:** `🧊 Backlog Geral`, `🎯 A Fazer - Próxima Iteração`, `✍️ Preparação/Revisão - Maestro`, `🤖 Em Processamento - Agente IA`, `⚙️ Em Processamento - Maestro`, `🧐 Validação - Maestro (HITL)`, `✅ Concluído na Iteração`, `🚀 Deployado/Arquivado`.
    
- **Cartões (Tarefas):** Título claro, links essenciais para documentos relevantes (ex: ERS, LLD, Métricas de Sucesso), tags detalhadas (responsável, agente, fase HITL, tipo, prioridade, módulo).
    
### 7.2. Templates de Prompts e Engenharia de Prompt Contínua

A eficácia dos Agentes de IA depende da qualidade dos prompts.

- **Localização Centralizada:** [[../05_Prompts/]] (com subpastas `01_Templates_Base/` e `02_Prompts_Especificos/`).
    
- **Estrutura Detalhada dos Templates:** Metadados, PERSONA, CONTEXTO (com placeholders para RAG e input do Maestro), TAREFA DETALHADA, RESTRIÇÕES, FORMATO DE SAÍDA ESPERADO (com exemplos).
    
- **Engenharia de Prompt Contínua:** Refinamento constante com base no desempenho dos agentes e no feedback HITL, liderado pelo Maestro com apoio do `@AgenteM_Orquestrador`.
    
## 8. Próximos Passos Críticos (Pós-Alinhamento Documental)

Após o alinhamento deste Plano Mestre (v1.0) e do [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v2.3) com o [[docs/02_Requisitos/01_ERS.md]] (v0.5), os próximos passos práticos imediatos, conforme detalhado na ERS e no Kanban, são: Nota: A referência ao `GUIA_AVANCADO.md` e `ERS.md` aqui está correta, pois são documentos centrais.

1. **Configuração do Ambiente de Desenvolvimento RAG:**
    
    - Criação do ambiente Conda (`Agents_RAG_Env` com Python 3.10).
        
    - Instalação das bibliotecas: `pytorch` (com CUDA 12.1), `faiss-gpu`, `langchain`, `sentence-transformers`, `pymupdf`, `python-dotenv`, `jupyter`.
        
    - Verificação da instalação e funcionamento do `faiss-gpu` com CUDA.
        
    - Download do modelo `BAAI/bge-m3`.
        
2. **Desenvolvimento do Script de Indexação RAG (`scripts/rag_indexer.py`):**
    
    - Implementar a lógica para carregar documentos Markdown da pasta `../../rag_infra/source_documents/`. (Corrigido para o caminho correto da base RAG)
        
    - Implementar o chunking de texto.
        
    - Implementar a geração de embeddings com `BAAI/bge-m3` via Sentence Transformers.
        
    - Implementar a criação e salvamento do índice FAISS-GPU.
        
3. **Teste Inicial do Pipeline RAG:**
    
    - Indexar um conjunto pequeno de documentos.
        
    - Realizar consultas de teste para verificar a relevância dos resultados.
        
4. **Configuração Inicial dos Agentes de IA no Trae IDE:** Foco no `@AgenteM_Orquestrador` unificado (PM + PO), integrando a capacidade de consulta ao RAG.
    
5. **Validação Técnica da Arquitetura de Autenticação e Pagamento:**
    - Protótipo de integração Google Login (Frontend/Backend/Supabase).
    - Protótipo de integração Stripe Checkout e Webhooks (Frontend/Backend/Supabase).
    - Teste de Row Level Security (RLS) com os novos fluxos.
    
6. **Estimativa Detalhada de Custos Operacionais (API Gemini, Infraestrutura)**
    
7. **Validação Qualitativa com Usuários-Alvo (Protótipos de Baixa Fidelidade e Entrevistas)**
    
Estes passos são cruciais para mitigar riscos e validar premissas antes do desenvolvimento intensivo do MVP.

## 9. Governança de IA e Conformidade Regulatória

### 9.1. Princípios de IA Responsável

O Recoloca.ai se compromete com o desenvolvimento e uso de Inteligência Artificial de forma ética, transparente e responsável. Nossos princípios incluem:

-   **Transparência e Explicabilidade (XAI):** As decisões e sugestões da IA, especialmente na otimização de currículos e análise de vagas, serão apresentadas de forma compreensível ao usuário, explicando os critérios e a lógica por trás das recomendações. O módulo de otimização de currículo incluirá um "Por que esta sugestão?" para cada recomendação.
-   **Mitigação de Vieses:** Serão implementados processos contínuos de auditoria e validação dos modelos de IA para identificar e mitigar vieses algorítmicos relacionados a gênero, raça, idade, origem ou qualquer outra característica discriminatória. O objetivo é garantir que as recomendações da IA sejam justas e equitativas para todos os usuários.
-   **Privacidade e Segurança de Dados:** Rigorosa aderência à LGPD e às melhores práticas de segurança da informação para proteger os dados sensíveis dos usuários, especialmente currículos e informações pessoais.
-   **Controle Humano:** O "Human-in-the-Loop" (HITL) é um componente central da nossa metodologia, garantindo que o Maestro e, em última instância, o usuário, tenham controle e capacidade de revisão sobre as saídas da IA.
-   **Módulo Educativo:** Será desenvolvido um módulo educativo dentro da plataforma para conscientizar os usuários sobre o funcionamento da IA, seus benefícios e limitações, promovendo o uso informado e responsável.

### 9.2. Conformidade Regulatória

O Recoloca.ai acompanhará ativamente e se adaptará às regulamentações emergentes sobre Inteligência Artificial no Brasil e globalmente. Em particular, haverá um foco proativo na conformidade com:

-   **Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018):** Todas as operações de coleta, tratamento, armazenamento e compartilhamento de dados pessoais estarão em conformidade com a LGPD.
-   **Projeto de Lei nº 2.338/2023 (Marco Legal da IA no Brasil):** Embora ainda em tramitação, o Recoloca.ai buscará antecipar e incorporar as diretrizes e requisitos propostos por este PL, especialmente no que tange a sistemas de IA de "alto risco", transparência, explicabilidade e responsabilidade.

### 9.3. Auditoria e Monitoramento Contínuo

Serão estabelecidos mecanismos de auditoria e monitoramento contínuo do desempenho dos modelos de IA, da qualidade dos dados e da aderência aos princípios de IA responsável e conformidade regulatória. Relatórios periódicos serão gerados para avaliar a equidade, a precisão e a segurança dos sistemas de IA.

## 10. Apêndices

### 10.1. Glossário de Termos Específicos do Projeto e Metodologia

Será mantido e atualizado no arquivo [[docs/01_Guias_Centrais/GLOSSARIO_Recoloca_AI.md]]. Nota: A referência ao `GLOSSARIO_Recoloca_AI.md` aqui está correta, pois é um documento central.

### 10.2. Referências Chave

- Documentação Oficial: Google Gemini, Flutter, FastAPI, Supabase, Trae IDE, OpenRouter, LangChain, FAISS, Sentence Transformers, Pymupdf, Pipedream, Vercel, Render, Mermaid.js.
    
- Padrões e Guias: Material Design 3, OWASP Top 10, OWASP LLM Top 10.
    
- Artigos e Livros sobre Product Management (para o RAG do `@AgenteM_Orquestrador`).
    
- Repositório do Modelo `BAAI/bge-m3` no Hugging Face.
    
## 11. Histórico de Versões

### v1.1 (Janeiro 2025)
- **Integração da Metodologia de "Orquestração Inteligente" e "Specialized Intelligence"**
- Adição de métricas específicas para avaliar eficácia da orquestração de agentes
- Inclusão de critérios objetivos para agentes "Production-Ready" em três tiers
- Estabelecimento de framework de medição para eficiência, qualidade RAG e produtividade
- Expansão dos indicadores de sucesso da metodologia de desenvolvimento
- Alinhamento metodológico com TAP.md v1.1 e GUIA_AVANCADO.md v1.1
- Consolidação da metodologia como diferencial competitivo do projeto

### v1.0 (Junho 2025)
- Versão inicial do Plano Mestre
- Definição da visão estratégica e objetivos do MVP
- Estabelecimento da metodologia "Desenvolvimento Solo Ágil Aumentado por IA"
- Especificação da arquitetura de Agentes de IA Mentores
- Definição da stack tecnológica e ferramentas
- Criação do roadmap de desenvolvimento

## 12. Documentos Relacionados

### Documentos de Gestão
- [[docs/00_Gerenciamento_Projeto/TAP.md]] - Termo de Abertura do Projeto (v1.1)
- [[docs/00_Gerenciamento_Projeto/KANBAN_Recoloca_AI.md]] - Gestão de Tarefas
- [[docs/01_Guias_Centrais/STYLE_GUIDE.md]] - Guia de Estilo

### Documentos Técnicos
- [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] - Guia Metodológico (v1.1)
- [[docs/02_Requisitos/01_ERS.md]] - Especificação de Requisitos
- [[docs/03_Arquitetura_e_Design/01_HLD.md]] - Arquitetura de Alto Nível

### Perfis de Agentes
- [[docs/04_Agentes_IA/02_AGENTES_IA_MENTORES_OVERVIEW.md]] - Visão Geral dos Agentes
- [[docs/04_Agentes_IA/01_Perfis/]] - Perfis Individuais dos Agentes Mentores

---

**Nota:** Este documento integra a metodologia de "Orquestração Inteligente" e "Specialized Intelligence" como pilares fundamentais do projeto Recoloca.ai, estabelecendo métricas objetivas e critérios de qualidade para maximizar a eficácia da colaboração entre o Maestro e os Agentes de IA Mentores.

--- FIM DO DOCUMENTO PLANO_MESTRE_RECOLOCA_AI.md (v1.1) ---