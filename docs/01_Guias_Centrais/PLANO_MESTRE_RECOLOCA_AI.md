# PLANO MESTRE DO PROJETO RECOLOCA.AI (v1.0)

**Data de Criação:** 26 de maio de 2025 
**Versão:** 1.0 
**Autor Principal (Maestro):** Bruno S. Rosa
**Assistência IA:** Gemini 2.5 Pro

## Sumário Executivo

Este **Plano Mestre** é o documento central para o desenvolvimento, manutenção e evolução do projeto **Recoloca.ai**. Ele consolida a visão estratégica, as decisões arquiteturais, o framework de desenvolvimento ágil assistido por Inteligência Artificial (IA), os fluxos de trabalho, as ferramentas e os próximos passos para a construção do Micro-SaaS Recoloca.ai. Este documento é uma **"Documentação Viva"** e será continuamente atualizado no Obsidian, servindo como a principal fonte da verdade para o desenvolvedor solo ("Maestro") e seus Agentes de IA Mentores.

## 1. Introdução ao Recoloca.ai

### 1.1. Visão Geral do Produto e Problema de Mercado

O **Recoloca.ai** é um Micro-SaaS inovador projetado para **transformar a experiência de recolocação profissional no Brasil**. O mercado de trabalho atual, especialmente no setor de tecnologia, é dinâmico e competitivo. Profissionais enfrentam desafios significativos como:

- Gerenciamento ineficiente de múltiplas candidaturas.
- Dificuldade em adaptar currículos de forma eficaz para cada vaga.
- Falta de preparo e confiança para entrevistas.
- Sensação de isolamento e falta de orientação durante o processo.

O Recoloca.ai visa solucionar essas dores oferecendo uma plataforma integrada que combina **gerenciamento inteligente de candidaturas (Kanban)**, **otimização de currículos potencializada por Inteligência Artificial (IA)** e um **assistente** de IA para coaching e **suporte contextualizado**. O objetivo é empoderar os profissionais brasileiros, fornecendo ferramentas e orientação para que naveguem pelo processo de recolocação com maior eficiência, estratégia e confiança, aumentando significativamente suas chances de sucesso.

### 1.2. Propósito deste Plano Mestre

Este **Plano** Mestre serve como o **documento fundamental e unificador** para todas as fases do ciclo de vida do Recoloca.ai. Seu propósito é:

- **Consolidar a visão estratégica** e os objetivos do projeto.
    
- **Detalhar a metodologia de desenvolvimento** "Solo Ágil Aumentado por IA".
    
- **Definir a arquitetura de Agentes de IA Mentores** e sua implementação.
    
- **Especificar a arquitetura técnica**, tecnologias e ferramentas a serem utilizadas.
    
- **Estabelecer as práticas de gestão de conhecimento** (RAG e Documentação Viva).
    
- **Delinear** os fluxos **de trabalho**, o modelo de Human-in-the-Loop (HITL) e a gestão de tarefas.
    
- **Guiar a configuração inicial do ambiente** e os passos subsequentes para o desenvolvimento do MVP.
    

Este documento será a **referência central** para o desenvolvedor "Maestro" e a base de conhecimento para os Agentes de IA.

### 1.3. Objetivos e Escopo do MVP (Produto Mínimo Viável)

**Objetivo Principal do MVP:** Validar a proposta de valor central do Recoloca.ai, que é auxiliar profissionais a gerenciar suas candidaturas, otimizar seus currículos com IA e receber coaching básico, focando inicialmente em profissionais de tecnologia no Brasil.

**Funcionalidades Centrais do MVP (conforme `[[ERS.md]]`):**

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
        

**Visão de Futuro (Pós-MVP - Breve Menção):**

- **Templates Avançados de Currículo e Customização (Tier Pago):** Conforme RF-CV-011.
    
- **Análises de Currículo Mais Detalhadas (Tier Pago):** Incluindo análise de sentimento, benchmarking de habilidades, otimização de impacto (STAR/CAR), previsão de perguntas de entrevista (conforme RF-CV-012).
    
- **Treino Aprofundado para Entrevistas com IA (Tier Pago):** Simulação interativa (conforme RF-CHAT-007).
    

### 1.4. Público-Alvo

- **Primário:** Profissionais brasileiros, com foco inicial do MVP em **profissionais de tecnologia** (desenvolvedores, analistas, gerentes de produto, designers, etc.) que estão ativamente buscando uma nova oportunidade de emprego ou em transição de carreira.
    
- **Secundário:** Profissionais brasileiros de diversas áreas que desejam se manter preparados para futuras oportunidades, otimizar seus currículos e melhorar suas habilidades de entrevista.
    

**Características Esperadas:** Familiaridade com navegação na web, uso de aplicativos online e abertura para utilizar ferramentas baseadas em Inteligência Artificial.

## 2. Metodologia e Framework de Desenvolvimento Adotados

### 2.1. O Modelo "Desenvolvimento Solo Ágil Aumentado por IA"

A metodologia de desenvolvimento adotada para o Recoloca.ai é o **"Desenvolvimento Solo Ágil Aumentado por Inteligência Artificial"**, conforme detalhado conceitualmente no documento `[[GUIA_AVANCADO_V1.md]]`. Esta abordagem reinterpreta os princípios ágeis e a colaboração com IA para o contexto de um desenvolvedor individual.

**Princípios Chave (Resumo do `[[GUIA_AVANCADO_V1.md]]`):**

- O desenvolvedor solo atua como um **"Maestro"** de uma orquestra de **Agentes de IA especializados ("Mentores")**.
    
- A IA transcende a função de ferramenta de codificação, tornando-se um **multiplicador de força** em todas as fases do SDLC.
    
- Foco na **automação de tarefas repetitivas** e aceleração do desenvolvimento, permitindo que o "Maestro" se concentre em desafios estratégicos e criativos.
    
- Utilização de **Agentes de IA como especialistas virtuais** em diversas áreas (arquitetura, UX, segurança, etc.), complementando as habilidades do desenvolvedor solo.
    
- Ênfase na **Documentação Viva** como fonte da verdade, gerenciada via RAG.
    
- Implementação de um ciclo de **Human-in-the-Loop (HITL)** que evolui de supervisão intensa para maior autonomia dos agentes.
    

### 2.2. Papel do Desenvolvedor como "Maestro"

No modelo adotado, o desenvolvedor solo (Eu, [Seu Nome Aqui]) assume o papel de **"Maestro"**. As responsabilidades incluem:

- **Definir a visão estratégica** e os objetivos do produto.
    
- **Priorizar o backlog** e as funcionalidades.
    
- **Orquestrar os Agentes de IA Mentores**, fornecendo prompts claros e contexto rico.
    
- **Supervisionar e validar** o trabalho gerado pelos Agentes de IA (HITL).
    
- **Tomar decisões arquiteturais** e de design críticas.
    
- **Desenvolver componentes complexos** ou que exijam um nível de nuance que a IA ainda não alcança.
    
- **Gerenciar a "Documentação Viva"** e a base de conhecimento RAG.
    
- **Aprender e evoluir continuamente** na arte da engenharia de prompts e na colaboração com IA.
    
- **Manter** o foco no valor **para o usuário** e nos objetivos de negócio.
    

### 2.3. Visão Geral do SDLC Ágil Adaptado para o Recoloca.ai

O Ciclo de Vida de Desenvolvimento de Software (SDLC) Ágil tradicional é adaptado para incorporar a colaboração intensiva com Agentes de IA Mentores:

1. **Definição de Requisitos (ERS, HUs, ACs):**
    
    - Maestro define/refina a ERS.
        
    - `@AgenteMentorPO` (via Trae IDE) auxilia na geração de Histórias de Usuário e Critérios de Aceite a partir da ERS.
        
    - Maestro valida e refina.
        
2. **Design de Alto Nível (HLD):**
    
    - Maestro define diretrizes.
        
    - `@AgenteMentorArquitetoHLD` (via Trae IDE) auxilia na criação de diagramas de arquitetura e definição de interações entre módulos.
        
    - Maestro valida e aprova.
        
3. **Design de Baixo Nível (LLD) e Especificação de API:**
    
    - `@AgenteMentorArquitetoLLD` ou `@AgenteMentorAPI` (via Trae IDE) detalha componentes, classes, funções e gera especificações OpenAPI.
        
    - Maestro valida e aprova.
        
4. **Desenvolvimento (Codificação):**
    
    - `@AgentesMentoresDev` (Flutter, FastAPI, JS via Trae IDE) geram código boilerplate, componentes e lógica de negócios com base no LLD e especificações.
        
    - Maestro revisa, depura, refatora e implementa partes críticas.
        
5. **Testes:**
    
    - `@AgenteMentorQA` (via Trae IDE) auxilia na geração de casos de teste e scripts de testes unitários/integração.
        
    - Maestro implementa testes E2E e supervisiona a execução.
        
6. **Documentação:**
    
    - `@AgenteMentorDocumentacao` (via Trae IDE) auxilia na geração de comentários, docstrings e na manutenção da "Documentação Viva".
        
    - Todos os artefatos são armazenados e versionados no Obsidian/Git.
        
7. **Deploy e DevOps:**
    
    - `@AgenteMentorDevOps` (conceitual, pode ser scripts/Pipedream) auxilia na automação de CI/CD para Vercel/Render/Supabase.
        
    - Maestro supervisiona e gerencia a infraestrutura.
        
8. **Manutenção e Evolução:**
    
    - Ciclo iterativo, com feedback do usuário alimentando novas HUs.
        
    - RAG é continuamente atualizado para manter os agentes informados.
        

## 3. Arquitetura de Agentes de IA Mentores do Recoloca.ai

A espinha dorsal da metodologia de desenvolvimento é uma arquitetura de Agentes de IA Mentores, implementados primariamente como agentes customizados (Gems/equivalente) no **Trae IDE**, utilizando o **Google Gemini Pro/Flash via OpenRouter** (ou diretamente, se o Trae permitir).

### 3.1. O Agente Orquestrador de Prompts (Implementação no Trae IDE)

Este é o **primeiro** e mais crucial **agente**, atuando como um "meta-agente" ou "agente de interface".

- **Persona no Trae IDE:** `@AgenteOrquestrador`
    
- **Objetivo:** Auxiliar o Maestro a refinar o pensamento e a formular instruções (prompts) claras, precisas e contextualmente ricas para os outros Agentes Mentores.
    
- **Funcionalidades (Conforme `[[GUIA_AVANCADO_V1.md]]`):**
    
    1. **Análise da Documentação Existente:** Capacidade de processar (via RAG ou contexto direto no Trae) documentos como `[[ERS.md]]`, `[[HLD.md]]`, e outros relevantes.
        
    2. **Geração de Perguntas Poderosas:** Para clarificar ambiguidades, identificar informações faltantes, definir escopo e sugerir contexto relevante.
        
    3. **Criação Assistida de Prompts Eficazes:** Ajudar a montar prompts detalhados, estruturados, incluindo referências diretas e sugerindo técnicas de engenharia de prompt.
        
- **Implementação no Trae:**
    
    - Será um agente customizado com um prompt base que o instrui sobre suas funções.
        
    - Utilizará a capacidade do Trae de acessar arquivos locais (se disponível) ou o Maestro fornecerá o contexto relevante (trechos de documentos, links para notas no Obsidian).
        
    - O Maestro interagirá com ele para "preparar" os prompts para os outros agentes.
        
    - Os templates de prompts serão armazenados em `[[05_Prompts/Templates_Base/]]`.
        

### 3.2. Detalhamento dos Agentes Mentores por Fase do SDLC

Os seguintes Agentes Mentores serão configurados no Trae IDE, cada um com uma persona, conjunto de habilidades (definidas pelo prompt base e contexto RAG) e templates de prompts específicos. A referência principal para seus papéis é a **Tabela Essencial 1.1 do `[[GUIA_AVANCADO_V1.md]]`**.

1. **`@AgenteMentorPO` (Product Owner)**
    
    - **Foco:** Definição de Requisitos.
        
    - **Tarefas:** Gerar Histórias de Usuário (`[[02_Requisitos/HU_AC/]]`) e Critérios de Aceite a partir da `[[02_Requisitos/ERS.md]]`, refinar requisitos para clareza da IA. Consultará o RAG para obter o contexto da ERS.
        
    - **Prompt Base no Trae:** "Você é um Product Owner IA especialista em metodologias ágeis e no mercado brasileiro de tecnologia. Sua tarefa é analisar requisitos formais e gerar Histórias de Usuário centradas no usuário e Critérios de Aceite SMART..."
        
    - **Ferramentas/Contexto:** Acesso à `[[02_Requisitos/ERS.md]]` via RAG, templates de HU/AC em `[[05_Prompts/Templates_Base/TPL_Gerar_HU.md]]`.
        
2. **`@AgenteMentorArquitetoHLD` (Arquiteto de Software - HLD)**
    
    - **Foco:** Design de Alto Nível.
        
    - **Tarefas:** Criar/otimizar `[[03_Arquitetura_e_Design/HLD.md]]`, diagramas de arquitetura (componentes, interações), definir interações entre módulos. Sugerir diagramas em Mermaid.js ou PlantUML. Consultará o RAG para a ERS e o Plano Mestre.
        
    - **Prompt** Base no **Trae:** "Você é um Arquiteto de Software IA experiente, com foco em sistemas web escaláveis e Micro-SaaS. Sua tarefa é analisar requisitos e propor arquiteturas de alto nível, incluindo diagramas de componentes e suas interações..."
        
    - **Ferramentas/Contexto:** Acesso à `[[02_Requisitos/ERS.md]]` e `[[PLANO_MESTRE_RECOLOCA_AI.md#4. Arquitetura Técnica e Tecnologias]]` via RAG.
        
3. `@AgenteMentorArquitetoLLD` **(Arquiteto/Designer de Software - LLD)**
    
    - **Foco:** Design de Baixo Nível.
        
    - **Tarefas:** Detalhar classes e funções para os módulos em `[[03_Arquitetura_e_Design/LLD/]]`, criar diagramas de sequência (Mermaid/PlantUML), especificar algoritmos. Consultará o RAG para HLD e ERS.
        
    - **Prompt Base no Trae:** "Você é um Designer de Software IA detalhista, capaz de traduzir arquiteturas de alto nível em especificações de baixo nível precisas, incluindo diagramas de classes, sequências e algoritmos..."
        
    - **Ferramentas/Contexto:** Acesso ao `[[03_Arquitetura_e_Design/HLD.md]]` e `[[02_Requisitos/ERS.md]]` via RAG.
        
4. `@AgenteMentorAPI` **(Arquiteto de APIs)**
    
    - **Foco:** Especificação de APIs.
        
    - **Tarefas:** Gerar especificações OpenAPI (ex: `[[03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]`) para os serviços de backend. Consultará o RAG para ERS e HLD.
        
    - **Prompt Base no Trae:** "Você é um Arquiteto de APIs IA especialista em RESTful APIs e na especificação OpenAPI 3.0. Sua tarefa é gerar documentação de API completa, segura e consistente a partir de requisitos funcionais..."
        
    - **Ferramentas/Contexto:** Acesso à `[[02_Requisitos/ERS.md]]` e `[[03_Arquitetura_e_Design/HLD.md]]` via RAG.
        
5. **`@AgenteMentorDevFastAPI` (Desenvolvedor Python/FastAPI)**
    
    - **Foco:** Desenvolvimento Backend.
        
    - **Tarefas:** Gerar código Python/FastAPI para endpoints, implementar lógica de negócios, testes unitários (pytest). Consultará o RAG para especificações de API, LLDs e padrões de código.
        
    - **Prompt Base no Trae:** "Você é um Desenvolvedor Python Sênior especialista em FastAPI, Pydantic, SQLAlchemy (para Supabase) e desenvolvimento de APIs seguras e eficientes. Siga as melhores práticas PEP 8 e SOLID..."
        
    - **Ferramentas/Contexto:** Acesso às especificações de API, `[[03_Arquitetura_e_Design/LLD/]]` via RAG, templates de código em `[[05_Prompts/Templates_Base/TPL_Gerar_Codigo_FastAPI.md]]`.
        
6. **`@AgenteMentorDevFlutter` (Desenvolvedor Flutter/Dart)**
    
    - **Foco:** Desenvolvimento Frontend (PWA).
        
    - **Tarefas:** Criar widgets de UI, implementar lógica de UI, chamadas à API backend, testes unitários/widget. Consultará o RAG para especificações de API, LLDs e Guia de Estilo.
        
    - **Prompt Base no Trae:** "Você é um Desenvolvedor Flutter Sênior experiente na criação de PWAs responsivas e de alta performance, utilizando Dart e gerenciamento de estado (Provider/Riverpod). Siga o `[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]`..."
        
    - **Ferramentas/Contexto:** Acesso às especificações de API, `[[03_Arquitetura_e_Design/LLD/]]`, `[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]` via RAG, mockups visuais (se disponíveis), FlutterFlow para prototipagem.
        
7. **`@AgenteMentorDevJS` (Desenvolvedor de Extensão Chrome)**
    
    - **Foco:** Desenvolvimento da Extensão de Navegador.
        
    - **Tarefas:** Implementar lógica de extração de dados de job boards (scraping ético), comunicação com backend, UI da extensão. Consultará o RAG para ERS e especificações de API.
        
    - **Prompt Base no Trae:** "Você é um Desenvolvedor JavaScript experiente na criação de Extensões Chrome seguras e eficientes, com conhecimento em manipulação do DOM, comunicação entre scripts e APIs de extensão..."
        
    - **Ferramentas/Contexto:** Acesso à `[[02_Requisitos/ERS.md]]` (requisitos da extensão) e especificações de API via RAG.
        
8. **`@AgenteMentorQA` (Analista de QA/Testes)**
    
    - **Foco:** Garantia de Qualidade.
        
    - **Tarefas:** Gerar planos de teste (`[[05_Qualidade_e_Testes/PGQ.md]]`), casos de teste (`[[05_Qualidade_e_Testes/Casos_de_Teste/]]`) a partir de HUs/ACs, gerar scripts de testes unitários e de integração. Consultará o RAG para ERS, HUs/ACs, HLD e LLDs.
        
    - **Prompt Base no Trae:** "Você é um Analista de QA IA meticuloso, especialista em derivar casos de teste abrangentes (positivos, negativos, de borda) e em BDD/Gherkin. Seu objetivo é garantir a máxima cobertura e qualidade..."
        
    - **Ferramentas/Contexto:** Acesso à `[[02_Requisitos/ERS.md]]`, `[[02_Requisitos/HU_AC/]]`, `[[03_Arquitetura_e_Design/HLD.md]]`, `[[03_Arquitetura_e_Design/LLD/]]` via RAG.
        
9. **`@AgenteMentorSeguranca` (Analista de Segurança)**
    
    - **Foco:** Segurança de Código.
        
    - **Tarefas:** Revisar código gerado em busca de vulnerabilidades (OWASP Top 10), instruir outros agentes sobre práticas seguras. Consultará o RAG para requisitos de segurança da ERS e padrões de código seguro.
        
    - **Prompt Base no Trae:** "Você é um Especialista em Segurança de Aplicações IA (AppSec), com profundo conhecimento do OWASP Top 10 e práticas de codificação segura para Python/FastAPI, Dart/Flutter e JavaScript..."
        
    - **Ferramentas/Contexto:** Acesso ao código gerado, `[[02_Requisitos/ERS.md]]` (requisitos de segurança) via RAG.
        
10. **`@AgenteMentorDocumentacao` (Documentador Técnico)**
    
    - **Foco:** Documentação de Código e Manutenção da Base de Conhecimento.
        
    - **Tarefas:** Gerar comentários e docstrings (Python Google Style, Dartdoc), explicar algoritmos, auxiliar na sincronização da "Documentação Viva" e na atualização do RAG. Consultará o RAG para código, ERS, HLD e LLDs.
        
    - **Prompt Base no Trae:** "Você é um Escritor Técnico IA especialista em documentar código de forma clara e concisa. Siga os padrões de documentação especificados para cada linguagem e ajude a manter a base de conhecimento do projeto atualizada..."
        
    - **Ferramentas/Contexto:** Acesso ao código, `[[02_Requisitos/ERS.md]]`, `[[03_Arquitetura_e_Design/HLD.md]]`, `[[03_Arquitetura_e_Design/LLD/]]` via RAG.
        

## 4. Arquitetura Técnica e Tecnologias

### 4.1. Stack Tecnológica Principal

Conforme definido na `[[02_Requisitos/ERS.md#2.4. Restrições Gerais]]`:

- **Frontend (PWA):** Flutter (Dart) - Para um PWA robusto e multiplataforma.
    
- **Backend:** Python com FastAPI - Para desenvolvimento rápido, performance e tipagem.
    
- **Banco de Dados:** PostgreSQL (Via Supabase) - Pela robustez e funcionalidades do Supabase.
    
- **Autenticação & Storage de Arquivos:** Supabase - Para simplificar o BaaS.
    
- **Extensão de Navegador:** JavaScript, HTML, CSS - Padrão para extensões Chrome.
    
- **IA LLM:** APIs Google Gemini (Flash para tarefas simples/rápidas, Pro para análises complexas e geração de alta qualidade) - Acessadas via OpenRouter ou diretamente.
    

### 4.2. Ferramentas de Desenvolvimento e IA

- **IDE Principal e Agentes de IA:** **Trae IDE** - Para codificação e implementação dos Agentes Mentores customizados.
    
- **Acesso a LLMs:** **OpenRouter** - Para flexibilidade no uso de diferentes modelos Gemini e outros, gerenciando custos.
    
- **Documentação e Gestão de Conhecimento:** **Obsidian** - Para a "Documentação Viva", notas, links bidirecionais.
    
- **Controle de Versão:** **Git** (com GitHub/GitLab) - Para versionamento de toda a documentação e código.
    
- **Gestão de Tarefas:** **Obsidian Kanban Plugin** (ou Trello, se preferir) - Para gerenciamento do backlog e fluxo de trabalho.
    
- **Automação de Fluxos de Trabalho (Orquestração leve/Gatilhos):** **Pipedream** - Escolhido por seu foco em desenvolvedores, permitindo a escrita de código Node.js ou Python diretamente nos passos, e por seu generoso plano gratuito, ideal para automações como reindexação do RAG e notificações.
    
- **Prototipagem de UI (Opcional):** **FlutterFlow** - Pode ser usado pelo `@AgenteMentorDevFlutter` ou pelo Maestro para acelerar a criação de interfaces iniciais ou explorar layouts.
    

### 4.3. Arquitetura de Alto Nível (HLD) do Recoloca.ai (Esboço Inicial)

_O `@AgenteMentorArquitetoHLD` detalhará isso no arquivo `[[03_Arquitetura_e_Design/HLD.md]]`. Um esboço inicial inclui:_

1. **Frontend PWA (Flutter):**
    
    - Interface do usuário principal, responsável pela renderização do Kanban, formulários de CV, interface do Chatbot.
        
    - Comunicação com o Backend API via HTTPS/REST para todas as operações de dados e lógica de negócios.
        
    - Gerenciamento de estado local (ex: Provider, Riverpod) para interações de UI e dados temporários.
        
2. **Backend API (Python/FastAPI):**
    
    - Núcleo da lógica de negócios: validações, processamentos, orquestração de chamadas a serviços externos.
        
    - Endpoints RESTful para autenticação, gerenciamento de vagas (Kanban), operações de CV (upload, parsing, análise, otimização), interações do chatbot.
        
    - Comunicação segura com Supabase (PostgreSQL) para persistência de dados (CRUD de usuários, vagas, currículos).
        
    - Comunicação com APIs Google Gemini (via OpenRouter) para funcionalidades de IA (análise de texto, geração de sugestões, respostas do chatbot).
        
    - Serviços dedicados para parsing de PDF (pymupdf, Tesseract) e categorização semântica do conteúdo do currículo.
        
3. **Extensão de Navegador (Chrome - JS/HTML/CSS):**
    
    - Content scripts injetados em páginas de job boards (LinkedIn, Gupy) para extração de dados das vagas (título, empresa, descrição, etc.).
        
    - Comunicação com o Backend API para enviar dados capturados e autenticar o usuário da extensão.
        
    - Interface de usuário (popup) simples para feedback da extração, edição manual de campos e acionamento da captura.
        
4. **Supabase (BaaS):**
    
    - **Auth:** Gerenciamento completo de ciclo de vida de usuários (registro, login, confirmação de email, reset de senha), utilizando autenticação baseada em Token JWT.
        
    - **Database (PostgreSQL):** Armazenamento estruturado de dados de usuários, vagas, currículos (base e ativos), notas, configurações e logs de atividade.
        
    - **Storage:** Armazenamento seguro de arquivos PDF de currículos enviados pelos usuários.
        
5. **Google Gemini APIs (via OpenRouter):**
    
    - **Gemini Flash:** Utilizado para tarefas de IA que exigem respostas rápidas e menor custo, como sugestões contextuais simples no chatbot ou categorizações iniciais.
        
    - **Gemini Pro:** Empregado para análises complexas e geração de texto de alta qualidade, como a comparação detalhada entre currículo e vaga, geração de relatórios de otimização e respostas elaboradas do chatbot de coaching.
        
6. **Pipedream (ou similar):**
    
    - Orquestração de fluxos de automação, como:
        
        - Envio de notificações transacionais (email via Postmark/SES para confirmação de conta, reset de senha; notificações push PWA via FCM para lembretes).
            
        - Gatilhos para reindexar a base RAG em atualizações da documentação no repositório Git.
            
        - Possíveis webhooks para integrar com outros serviços, se necessário.
            

_(Um diagrama Mermaid.js ou PlantUML será incluído no `[[03_Arquitetura_e_Design/HLD.md]]` para visualizar estas interações.)_

## 5. Gestão de Conhecimento e Contexto (RAG & Documentação Viva)

### 5.1. Estratégia RAG para o Recoloca.ai

Para garantir que os Agentes de IA Mentores operem com informações atualizadas e específicas do projeto, será implementado um sistema de **Retrieval Augmented Generation (RAG)**.

- **Base de Conhecimento:**
    
    - Localizada na pasta `[[07_Knowledge_Base_RAG_Sources/]]` dentro do vault do Obsidian.
        
    - Conterá versões em Markdown (ou texto puro) de:
        
        - `[[02_Requisitos/ERS.md]]`
            
        - `[[03_Arquitetura_e_Design/HLD.md]]`
            
        - `[[03_Arquitetura_e_Design/LLD/]]` (arquivos relevantes)
            
        - `[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]`
            
        - `[[03_Arquitetura_e_Design/API_Specs/]]` (descrições chave)
            
        - Documentação oficial dos SDKs/APIs chave (Flutter, FastAPI, Supabase, Gemini) - _trechos mais relevantes ou sumários_.
            
        - Decisões de arquitetura importantes (`[[03_Arquitetura_e_Design/ADR/]]`).
            
- **Tecnologias RAG:**
    
    - **Framework:** **LangChain** (Python) - Para orquestrar o pipeline RAG (carregamento, chunking, embedding, retrieval, geração).
        
    - **Vector Store:** **FAISS** (Facebook AI Similarity Search) - Para uma implementação local e leve, armazenando os embeddings.
        
    - **Embedding Model:** Um modelo eficiente como `all-MiniLM-L6-v2` (via Sentence Transformers/Hugging Face) ou similar.
        
- **Processo de Indexação:**
    
    - Um script Python (`scripts/rag_indexer.py` - a ser criado) usará LangChain para:
        
        1. Monitorar ou ser acionado por mudanças na pasta `[[07_Knowledge_Base_RAG_Sources/]]`.
            
        2. Carregar os documentos.
            
        3. Dividi-los em chunks semânticos.
            
        4. Gerar embeddings para cada chunk.
            
        5. Salvar/atualizar os embeddings no índice FAISS local.
            
    - Este script pode ser acionado manualmente ou via um hook do Git (ou Pipedream monitorando o repositório).
        
- **Processo de Consulta (Retrieval):**
    
    - O `@AgenteOrquestrador` ou diretamente os Agentes Mentores no Trae IDE, antes de gerar uma resposta complexa, farão uma consulta semântica ao índice FAISS.
        
    - Os chunks de informação mais relevantes recuperados serão injetados no prompt final enviado ao LLM (Gemini), fornecendo contexto "just-in-time".
        
- **Monitoramento da Qualidade do RAG:** O Maestro deve realizar verificações periódicas da relevância dos resultados do RAG para garantir que a base de conhecimento esteja sendo indexada e recuperada corretamente, ajustando o processo de chunking ou os modelos de embedding conforme necessário.
    

### 5.2. A "Documentação Viva" no Obsidian e Git

Todo o conhecimento do projeto, incluindo este Plano Mestre, ERS, HLD, LLDs, ADRs, notas de pesquisa, templates de prompts e o Kanban de tarefas, será mantido no **Obsidian**.

- **Estrutura de Pastas:** Conforme definido na seção "Estrutura de Pastas Atualizada e Mais Completa" (referenciada em discussões anteriores e a ser detalhada no `[[README.md]]` do repositório de documentação).
    
- **Links Bidirecionais:** Uso intensivo de links (`[[...]]`) para conectar informações relacionadas, criando uma rede de conhecimento navegável.
    
- **Controle de Versão:** Todo o vault do Obsidian (ou a pasta específica do projeto `Recoloca.ai/`) será um repositório **Git**, com commits frequentes e push para um repositório remoto (GitHub/GitLab). O plugin "Obsidian Git" facilitará este processo.
    
- **Atualização Contínua:** A documentação não é uma fase, mas um processo contínuo. O `@AgenteMentorDocumentacao` auxiliará na manutenção, e o Maestro é responsável por garantir que as decisões e aprendizados sejam registrados.
    

### 5.3. Uso e Riscos de MCPs (Model Context Protocol)

Conforme discutido no `[[GUIA_AVANCADO_V1.md]]`, o **Model Context Protocol (MCP)** é um protocolo promissor para padronizar a interação de LLMs com ferramentas externas.

- **Uso Potencial (Futuro):** Poderia permitir que os Agentes de IA interajam de forma mais segura e padronizada com APIs (Supabase, Gemini), sistema de arquivos ou executar código, se ferramentas como o Trae IDE ou bibliotecas como LangChain adotarem ou fornecerem adaptadores para MCP.
    
- **Riscos:** Prompt Injection, Tool Poisoning. A segurança é uma consideração primordial.
    
- **Abordagem Atual:** No momento, a interação com ferramentas será gerenciada primariamente pelas capacidades do Trae IDE (incluindo Gemini Function Calling) e/ou LangChain, com foco em RAG para fornecer contexto de APIs e SDKs. A adoção de MCPs mais complexos será avaliada conforme a maturidade e segurança do protocolo e suas implementações, priorizando o Gemini Function Calling para ações diretas e Context7 para acesso a documentação de SDKs.
    

## 6. Fluxo de Trabalho de Desenvolvimento e HITL

### 6.1. Fluxo de Trabalho Detalhado: Da ERS ao Deploy

O fluxo de trabalho será iterativo e incremental, seguindo os princípios ágeis e integrando os Agentes de IA e o Maestro.

1. **Planejamento da Sprint/Iteração (Obsidian Kanban):**
    
    - Maestro prioriza HUs do backlog.
        
    - Tarefas são criadas no Kanban, designadas para "Humano" ou "Agente IA".
        
2. **Refinamento de Requisitos:**
    
    - Tarefa para `@AgenteMentorPO`: "Gerar/Refinar HUs e ACs para `[[02_Requisitos/ERS.md#RF-XYZ]]`".
        
    - Maestro revisa e aprova (HITL).
        
3. **Design (HLD/LLD/API):**
    
    - Tarefa para `@AgenteMentorArquitetoHLD/LLD/API`: "Gerar HLD/LLD/OpenAPI para Módulo X".
        
    - Maestro revisa, solicita ajustes e aprova (HITL).
        
4. **Desenvolvimento (Codificação):**
    
    - Tarefas para `@AgentesMentoresDev` (FastAPI, Flutter, JS): "Implementar endpoint Y / widget Z / funcionalidade da extensão W com base no `[[03_Arquitetura_e_Design/LLD/LLD_Modulo_X.md]]`".
        
    - Maestro fornece contexto adicional via `@AgenteOrquestrador`.
        
    - Código gerado é commitado em branches separadas.
        
5. **Revisão de Código (HITL):**
    
    - Maestro revisa o código gerado.
        
    - `@AgenteMentorSeguranca` pode ser invocado para uma análise de segurança.
        
    - `@AgenteMentorDocumentacao` auxilia na geração de docstrings/comentários.
        
    - Maestro refatora, corrige e integra.
        
6. **Testes:**
    
    - Tarefa para `@AgenteMentorQA`: "Gerar testes unitários/de integração para o código do Módulo X".
        
    - Maestro implementa/supervisiona testes E2E.
        
    - Execução automatizada de testes (CI via Pipedream/GitHub Actions).
        
7. **Documentação:**
    
    - Maestro e `@AgenteMentorDocumentacao` atualizam a "Documentação Viva" no Obsidian (ERS, HLD, LLDs, ADRs) com base nas implementações e decisões.
        
8. **Deploy:**
    
    - Scripts de deploy (automatizados via Pipedream/GitHub Actions, se possível) para Vercel (Frontend), Render (Backend), Supabase (Schema migrations).
        
    - Maestro supervisiona o deploy para staging e produção.
        
9. **Feedback e Iteração:**
    
    - Coleta de feedback do usuário (pós-MVP).
        
    - Novas HUs são criadas, e o ciclo recomeça.
        

### 6.2. Modelo de Human-in-the-Loop (HITL) para o Recoloca.ai

O HITL é fundamental para garantir qualidade, segurança e alinhamento com os objetivos. Ele evoluirá em fases:

- **Fase 1: Supervisão Intensa (MVP Inicial)**
    
    - **Descrição:** O Maestro revisa _todo_ o output significativo dos Agentes de IA (HUs, ACs, diagramas, especificações de API, blocos de código, casos de teste).
        
    - **Pontos de Checagem:** Após cada tarefa principal de um agente.
        
    - **Critérios de Confiança:** Baixa confiança inicial; foco em aprendizado e ajuste dos prompts e personas dos agentes.
        
- **Fase 2: Autonomia Guiada (Pós-MVP, com Agentes Maduros)**
    
    - **Descrição:** O Maestro foca a revisão em áreas críticas, complexas ou de alto risco. Agentes podem ter autonomia para tarefas mais simples ou repetitivas, com revisão por amostragem.
        
    - **Pontos de Checagem:** Definidos para entregas chave ou módulos sensíveis.
        
    - **Critérios de Confiança:** Média confiança; agentes demonstram consistência e qualidade em tarefas específicas. Métricas de qualidade do código e testes são monitoradas.
        
- **Fase 3: Controle Supervisor (Ideal de Longo Prazo)**
    
    - **Descrição:** O Maestro atua mais como um revisor final e tomador de decisões estratégicas. Agentes operam com alta autonomia em áreas bem definidas, com alertas automáticos para anomalias ou baixa confiança.
        
    - **Pontos de Checagem:** Revisões de design de alto nível, aprovações de release.
        
    - **Critérios de Confiança:** Alta confiança; agentes provaram sua capacidade e o sistema de RAG está robusto. Foco do Maestro em inovação e novas funcionalidades.
        

O feedback fornecido pelo Maestro durante as revisões HITL é crucial. Ele não apenas valida o trabalho, mas também serve como dados para o refinamento contínuo dos prompts e das instruções dos Agentes Mentores, melhorando seu desempenho futuro e "treinando-os" implicitamente.

### 6.3. Diagrama Visual do Fluxo de Trabalho

_(Espaço para um diagrama Mermaid.js a ser inserido aqui no Obsidian. O diagrama ilustrará o fluxo da Seção 6.1, mostrando as interações entre Maestro, Agentes de IA, Documentos e o Kanban.)_

**Exemplo Simples de Início (Mermaid.js):**

```
graph TD
    A[ERS/Backlog] --> B{Maestro Prioriza HU};
    B --> C[@AgenteMentorPO Gera HU/AC];
    C --> D{Maestro Revisa HU/AC};
    D -- Aprovado --> E[@AgenteMentorArquitetoHLD/LLD Gera Design];
    E --> F{Maestro Revisa Design};
    F -- Aprovado --> G[@AgenteMentorDev Gera Código];
    G --> H{Maestro Revisa Código};
    H -- Aprovado --> I[Testes por @AgenteMentorQA e Maestro];
    I --> J[Deploy por @AgenteMentorDevOps e Maestro];
    J --> A;
```

## 7. Gestão de Projeto, Tarefas e Comunicação

### 7.1. Configuração e Uso do Obsidian Kanban

O gerenciamento de tarefas será centralizado no **Obsidian** utilizando o plugin **"Kanban"**.

- **Arquivo do Quadro:** `[[KANBAN_Recoloca_AI.md]]` (localizado na raiz da pasta do projeto `Recoloca.ai/` no Obsidian).
    
- **Estrutura de Colunas (Sugestão Inicial):**
    
    - `🧊 Backlog Geral` (Novas ideias, HUs da ERS)
        
    - `✍️ À Fazer - Humano (Revisão/Preparação)`
        
    - `🤖 À Fazer - Agente IA`
        
    - `⚙️ Em Processamento - Humano`
        
    - `⏳ Em Processamento - Agente IA`
        
    - `🧐 Revisão - Humano (HITL)`
        
    - `✅ Feito`
        
- **Cartões (Tarefas):**
    
    - Cada item de lista (`- [ ]`) é um cartão.
        
    - **Links:** Uso intensivo de links para `[[02_Requisitos/ERS.md]]`, `[[02_Requisitos/HU_AC/]]`, `[[03_Arquitetura_e_Design/LLD/]]`, `[[05_Prompts/]]`, etc., para fornecer contexto direto.
        
    - **Tags:**
        
        - `#humano`, `#agente`
            
        - `#agente_po`, `#agente_arquiteto`, `#agente_dev_fastapi`, etc. (para designar o agente)
            
        - `#hitl_fase1`, `#hitl_fase2` (para indicar o nível de revisão necessário)
            
        - `#bug`, `#feature`, `#refactor`
            
        - Prioridade: `#p1_alta`, `#p2_media`, `#p3_baixa`
            
- **Fluxo:** Tarefas movem-se entre as colunas conforme progridem. O Maestro é responsável por mover os cartões e garantir que o contexto (links, descrições) esteja atualizado.
    

### 7.2. Templates de Prompts

A qualidade da interação com os Agentes de IA depende criticamente da qualidade dos prompts.

- **Localização:** `[[05_Prompts/]]` dentro do vault do Obsidian.
    
    - `[[05_Prompts/Templates_Base/]]`: Para templates genéricos reutilizáveis (ex: `TPL_Gerar_HU.md`, `TPL_Gerar_Codigo_FastAPI.md`).
        
    - `[[05_Prompts/Prompts_Especificos/]]`: Para prompts mais elaborados e específicos de uma tarefa complexa, que podem ser construídos com a ajuda do `@AgenteOrquestrador` e baseados nos templates.
        
- **Conteúdo dos Templates:**
    
    - **Contexto:** Seção para injetar informações relevantes (links para ERS, HLD, código existente).
        
    - **Persona do Agente:** Instruções claras sobre o papel e expertise esperados.
        
    - **Tarefa:** Descrição precisa do que deve ser feito.
        
    - **Restrições:** O que o agente NÃO deve fazer, limites, padrões a seguir.
        
    - **Formato de Saída Esperado:** Exemplo de como a resposta deve ser estruturada.
        
    - **Exemplos (Few-shot):** Se aplicável, exemplos de input/output desejados.
        
- **Refinamento Contínuo:** Os templates serão versionados no Git e refinados com base na performance dos agentes.
    

### Exemplo de Estrutura de Template de Prompt (`TPL_Exemplo.md`)

**Nome do Agente Alvo:** `@AgenteExemplo` **Versão do Template:** 1.0 **Objetivo da Tarefa:** [Descrever o que o agente deve alcançar]

**PERSONA DO AGENTE:** Você é um `@AgenteExemplo` especialista em [domínio específico]. Seu tom é [tom de voz] e seu objetivo é [objetivo principal da persona]. Você consulta ativamente o RAG do projeto para obter o contexto mais atualizado sobre `[[ERS.md]]`, `[[HLD.md]]` e outros documentos relevantes antes de responder.

**CONTEXTO FORNECIDO (Além do RAG Geral):**

- Requisito Específico: `[[02_Requisitos/ERS.md#RF-ABC]]`
    
- Seção do LLD: `[[03_Arquitetura_e_Design/LLD/ModuloY/LLD_Especifico.md]]`
    
- Decisão Arquitetural Relacionada: `[[03_Arquitetura_e_Design/ADR/ADR_XYZ.md]]`
    
- [Outras informações contextuais pontuais fornecidas pelo Maestro]
    

**TAREFA DETALHADA:**

1. Com base no RF-ABC, analise o LLD_Especifico.
    
2. Gere [artefato específico A], considerando a decisão em ADR_XYZ.
    
3. Para o [artefato específico A], detalhe [sub-componente B].
    

**RESTRIÇÕES E DIRETRIZES:**

- Não utilize [tecnologia X não aprovada].
    
- Siga o padrão de nomenclatura definido em `[[03_Arquitetura_e_Design/STYLE_GUIDE.md#Nomenclatura]]`.
    
- O código gerado deve incluir documentação no formato [Dartdoc/Google Python Style].
    
- Verifique se a solução é compatível com [requisito não funcional RNF-SEC-005].
    

**FORMATO DE SAÍDA ESPERADO:**

- [Descrever a estrutura da resposta, ex: Bloco de código Python com docstrings, Documento Markdown com seções X, Y, Z e um diagrama Mermaid embutido, Objeto JSON com chaves A, B, C e seus tipos de dados]
    
- **Exemplo (se aplicável):**
    
    ```
    {
      "status": "sucesso",
      "dados": {
        "id_gerado": "123xyz",
        "mensagem_confirmacao": "Operação realizada com sucesso."
      }
    }
    ```
    
## 9. Apêndices

### 9.1. Glossário de Termos Específicos do Projeto e Metodologia

- **Maestro:** O desenvolvedor solo que define a estratégia, orquestra os Agentes de IA, e realiza a validação crítica (HITL) do projeto Recoloca.ai.
    
- **Agente Mentor de IA:** Um agente de IA especializado, configurado com uma persona e conhecimento específico (via prompt e RAG), para assistir o Maestro em uma determinada fase ou tarefa do SDLC (ex: `@AgenteMentorPO`, `@AgenteMentorArquitetoHLD`).
    
- **RAG (Retrieval Augmented Generation):** Geração Aumentada por Recuperação. Técnica que permite a um LLM acessar e utilizar informações de uma base de conhecimento externa (no caso, a "Documentação Viva" do Recoloca.ai) para gerar respostas mais precisas, contextuais e atualizadas.
    
- **MCP (Model Context Protocol):** Protocolo de Contexto de Modelo. Um padrão aberto para permitir que LLMs interajam com ferramentas externas (APIs, sistema de arquivos, etc.) de forma segura e padronizada. Para o Recoloca.ai, o Gemini Function Calling é a abordagem inicial preferida.
    
- **HITL (Human-in-the-Loop):** Humano no Loop. Processo onde um humano (o Maestro) revisa, valida, corrige ou guia o output de um sistema de IA. Essencial para garantir qualidade, segurança e alinhamento.
    
- **SDLC (Software Development Life Cycle):** Ciclo de Vida de Desenvolvimento de Software. As fases tradicionais (Requisitos, Design, Desenvolvimento, Testes, Deploy, Manutenção) adaptadas para a colaboração com Agentes de IA.
    
- **PWA (Progressive Web Application):** Aplicação Web Progressiva. Aplicação web que oferece uma experiência similar a um aplicativo nativo (offline, notificações, etc.).
    
- **BaaS (Backend as a Service):** Backend como Serviço. Plataformas como Supabase que fornecem funcionalidades de backend prontas (autenticação, banco de dados, storage).
    
- **CRUD (Create, Read, Update, Delete):** Operações básicas de manipulação de dados.
    
- **JWT (JSON Web Token):** Padrão aberto para criar tokens de acesso que afirmam um número de "claims" entre duas partes. Usado para autenticação.
    
- **TOTP (Time-based One-Time Password):** Senha de Uso Único Baseada em Tempo. Usada para Autenticação Multifator (MFA).
    
- **OWASP (Open Web Application Security Project):** Projeto Aberto de Segurança em Aplicações Web. Referência para riscos de segurança e melhores práticas.
    
- **YAML (YAML Ain't Markup Language):** Linguagem de serialização de dados legível por humanos, frequentemente usada para arquivos de configuração.
    
- **Markdown:** Linguagem de marcação leve com sintaxe de formatação de texto simples. Usada para a "Documentação Viva".
    
- **Mermaid.js / PlantUML:** Linguagens baseadas em texto para gerar diagramas UML e outros, integráveis em Markdown.
    
- **FAISS (Facebook AI Similarity Search):** Biblioteca para busca eficiente de similaridade e agrupamento de vetores densos. Usada como Vector Store local para o RAG.
    
- **LangChain:** Framework para desenvolver aplicações alimentadas por LLMs, facilitando a criação de cadeias RAG, agentes e interações com ferramentas.
    
- **OpenRouter:** Gateway que permite acesso a múltiplos LLMs (incluindo Gemini) através de uma única API, facilitando a troca de modelos e o gerenciamento de custos.
    
- **Trae IDE:** Ambiente de Desenvolvimento Integrado (IDE) potencializado por IA, usado como plataforma principal para codificação e configuração dos Agentes Mentores.
    
- **Pipedream:** Plataforma de automação de fluxos de trabalho focada em desenvolvedores, usada para CI/CD e outras automações.
    
- **FlutterFlow:** Plataforma low-code para construir aplicações Flutter, podendo ser usada para prototipagem rápida de UI.
    
- **Supabase:** Plataforma BaaS open-source alternativa ao Firebase, oferecendo banco de dados PostgreSQL, autenticação, storage, etc.
    
- **FastAPI:** Framework web Python moderno e de alta performance para construir APIs.
    
- **Vercel:** Plataforma para deploy de frontends e funções serverless, com forte integração Git.
    
- **Render:** Plataforma para deploy de aplicações backend, bancos de dados e outros serviços, com configuração via IaC (`render.yaml`).
    

### 9.2. Referências Chave

- **Documentos Internos do Projeto:**
    
    - `[[GUIA_AVANCADO_V1.md]]` (Guia Avançado para Desenvolvimento Solo com Agentes de IA Mentores v1.0)
        
    - `[[02_Requisitos/ERS.md]]` (Especificação de Requisitos de Software - Recoloca.ai v0.2)
        
    - (Outros documentos a serem criados, como HLD, LLDs, Style Guide, etc.)
        
- **Documentação Oficial das Ferramentas Principais:**
    
    - Obsidian: [https://help.obsidian.md/](https://help.obsidian.md/ "null")
        
    - Git: [https://git-scm.com/doc](https://git-scm.com/doc "null")
        
    - Trae IDE: [https://trae.ai/docs](https://trae.ai/docs "null") (ou link oficial)
        
    - Google Gemini API: [https://ai.google.dev/docs](https://ai.google.dev/docs "null")
        
    - LangChain: [https://python.langchain.com/docs/get_started/introduction](https://python.langchain.com/docs/get_started/introduction "null")
        
    - FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/ "null")
        
    - Flutter: [https://docs.flutter.dev/](https://docs.flutter.dev/ "null")
        
    - Dart: [https://dart.dev/guides](https://dart.dev/guides "null")
        
    - Supabase: [https://supabase.com/docs](https://supabase.com/docs "null")
        
    - Pipedream: [https://pipedream.com/docs/](https://pipedream.com/docs/ "null")
        
    - OpenRouter: [https://openrouter.ai/docs](https://openrouter.ai/docs "null")
        
    - FAISS: [https://faiss.ai/](https://faiss.ai/ "null") (e sua documentação no GitHub)
        
    - FlutterFlow: [https://docs.flutterflow.io/](https://docs.flutterflow.io/ "null")
        
    - Vercel: [https://vercel.com/docs](https://vercel.com/docs "null")
        
    - Render: [https://render.com/docs](https://render.com/docs "null")
        
    - Mermaid.js: [https://mermaid.js.org/](https://mermaid.js.org/ "null")
        
- **Padrões e Guias de Referência:**
    
    - Material Design 3: [https://m3.material.io/](https://m3.material.io/ "null")
        
    - OWASP Top 10: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/ "null")
        
    - OWASP LLM Top 10: [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/ "null")
        
    - PEP 8 (Python Style Guide): [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/ "null")
        
    - Effective Dart: [https://dart.dev/guides/language/effective-dart](https://dart.dev/guides/language/effective-dart "null")
        

**FIM DO PLANO MESTRE RECOLOCA.AI (v1.0)**