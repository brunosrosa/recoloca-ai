# Especificação de Requisitos de Software (ERS): Recoloca.ai
**Versão:** 0.2 (Refinada)
**Data:** 23 de maio de 2025
**Baseado no PRD:** Recoloca.AI - PRD - MVP (inicial) - Versão 0.1 e Refinamentos Posteriores

## 1. Introdução

### 1.1. Propósito
Este documento especifica os requisitos funcionais e não funcionais para a Versão Mínima Viável (MVP) da plataforma Recoloca.ai. O Recoloca.ai é um Micro-SaaS projetado para auxiliar profissionais no Brasil no processo de recolocação profissional, combinando gerenciamento de candidaturas, otimização de currículos com Inteligência Artificial (IA) e um assistente de IA para coaching. Este documento destina-se a guiar o desenvolvimento do produto por equipes de engenharia, incluindo Agentes de IA, e servir como base para testes e validação.

### 1.2. Escopo do Produto (MVP)
O MVP do Recoloca.ai se concentrará em:
1.  **Gerenciamento de Candidaturas (Kanban):** Permitir que usuários salvem e organizem vagas de emprego com captura de dados enriquecida.
2.  **Otimização de Currículo com IA:** Analisar descrições de vagas e currículos base (com parsing robusto e validação do usuário) para gerar versões customizadas, pontuações de aderência detalhadas e sugestões avançadas.
3.  **Acompanhamento e "Coaching" com IA (Chatbot):** Oferecer dicas, suporte contextualizado e treino básico para entrevistas, com base de conhecimento curada e persona definida.
A plataforma será acessível via Web (PWA robusto construído com Flutter) e uma extensão de navegador para Chrome. O idioma principal será Português do Brasil.

**Funcionalidades Fora do Escopo do MVP (conforme refinamentos):**
*   Integração direta com API do LinkedIn para importação de perfil ou aplicação.
*   Análise avançada de perfil comportamental.
*   Geração automática completa de cartas de apresentação (a IA pode auxiliar em trechos).
*   Múltiplos idiomas (além do Português do Brasil).
*   Funcionalidades de networking ou comunidade dentro da plataforma.
*   Aplicativos nativos dedicados para Android/iOS (foco em PWA de alta qualidade).
*   Matching proativo de vagas com IA.
*   Dashboard de analytics de carreira muito avançado (além de métricas básicas de uso).
*   Módulos de testes de competências (hard/soft skills).
*   Gamificação complexa.
*   Integração com agendas externas (Google Calendar, Outlook).
*   Importação de perfil de outras plataformas além de PDF.

### 1.3. Definições, Acrônimos e Abreviações
*   **IA:** Inteligência Artificial
*   **LLM:** Large Language Model (Modelo de Linguagem Amplo)
*   **PWA:** Progressive Web Application
*   **ATS:** Applicant Tracking System (Sistema de Rastreamento de Candidatos)
*   **MVP:** Minimum Viable Product (Produto Mínimo Viável)
*   **PRD:** Product Requirements Document (Documento de Requisitos do Produto)
*   **ERS/SRS:** Especificação de Requisitos de Software / Software Requirements Specification
*   **UI:** User Interface (Interface do Usuário)
*   **UX:** User Experience (Experiência do Usuário)
*   **API:** Application Programming Interface (Interface de Programação de Aplicações)
*   **LGPD:** Lei Geral de Proteção de Dados Pessoais
*   **DB:** Banco de Dados
*   **CRUD:** Create, Read, Update, Delete
*   **MFA:** Multi-Factor Authentication (Autenticação Multifator)
*   **OWASP:** Open Web Application Security Project
*   **RAG:** Retrieval Augmented Generation
*   **FCM:** Firebase Cloud Messaging
*   **LCP:** Largest Contentful Paint
*   **FID:** First Input Delay
*   **INP:** Interaction to Next Paint
*   **CLS:** Cumulative Layout Shift

### 1.4. Referências
*   Recoloca.AI - PRD - MVP (inicial) - Versão 0.1, Data: 15 de maio de 2025, Autor: Bruno Sant’Ana de Rosa.
*   Discussões de Refinamento e Sugestões Finais (documentadas internamente).

### 1.5. Visão Geral do Documento
Este documento está organizado da seguinte forma: Seção 1 (Introdução), Seção 2 (Descrição Geral), Seção 3 (Requisitos Específicos), Seção 4 (Questões Abertas – minimizadas por refinamentos).

## 2. Descrição Geral

### 2.1. Perspectiva do Produto
O Recoloca.ai será um novo produto independente. Ele interagirá com APIs externas de LLMs (Google Gemini) e com job boards (LinkedIn, Gupy) através de uma extensão de navegador.

### 2.2. Funções do Produto (Resumo)
1.  **Gerenciamento Visual e Enriquecido de Candidaturas.**
2.  **Otimização Profunda e Inteligente de Currículos com validação do usuário.**
3.  **Suporte e Coaching por IA com Base de Conhecimento Curada.**

### 2.3. Características dos Usuários
*   **Primário:** Profissionais brasileiros (foco inicial do MVP: profissionais de tecnologia) buscando nova oportunidade de emprego ou em transição de carreira.
*   **Secundário:** Profissionais que desejam se manter preparados para futuras oportunidades.
*   **Habilidades Técnicas Esperadas:** Familiaridade com navegação na web, uso de aplicativos online.

### 2.4. Restrições Gerais
*   **Idioma:** Português do Brasil (MVP).
*   **Navegador (Extensão):** Google Chrome (versão mais recente estável).
*   **Plataforma (PWA):** Acessível em navegadores web modernos (desktops e mobile - iOS/Android) via Flutter Web.
*   **Legislação:** Conformidade total com a LGPD.
*   **Stack Tecnológica Decidida:**
    *   Frontend (PWA): **Flutter (Dart)**.
    *   Backend: **Python com FastAPI**.
    *   Banco de Dados: **PostgreSQL (Via Supabase)**.
    *   Autenticação & Storage de Arquivos: **Supabase**.
    *   Extensão de Navegador: JavaScript, HTML, CSS.
    *   IA LLM: APIs **Google Gemini 2.5 Flash** (para tarefas mais simples/rápidas) e **Gemini 2.5 Pro** ou superior (para análises complexas e geração de alta qualidade).
    *   Parsing de PDF: **`pymupdf` (Fitz)** primário; **`Tesseract OCR`** (com modelos pt-BR de alta qualidade) como fallback; **IA (LLM)** para categorização semântica do texto extraído.
    *   Infraestrutura/Hospedagem: Frontend PWA em **Vercel** ou **Netlify**; Backend FastAPI em **Render** ou **Google Cloud Run**; Banco de Dados e Auth com **Supabase**.
*   **Vector DB:** **Adiado para Pós-MVP**. Reavaliar quando funcionalidades de matching proativo forem consideradas.

### 2.5. Suposições e Dependências
*   Suposições do PRD (demanda, disposição a pagar, maturidade IA, viabilidade da extensão) são mantidas.
*   Dependência das APIs do Google Gemini, estrutura DOM dos job boards, e serviços de hospedagem.

## 3. Requisitos Específicos

### 3.1. Requisitos Funcionais

#### 3.1.1. Autenticação e Gerenciamento de Conta
*   **RF-AUTH-001:** O sistema DEVE permitir que novos usuários se cadastrem fornecendo Email e Senha.
    *   *Input:* Email (formato de email válido), Senha.
    *   *Processo:* Validação dos dados. Senha DEVE ter no mínimo 12 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos (OWASP). Senha DEVE ser verificada contra listas de senhas vazadas (ex: Have I Been Pwned API). Hashing seguro com Argon2id. Criação de registro de usuário.
    *   *Output:* Conta de usuário criada. Solicitação de confirmação de email.
*   **RF-AUTH-002:** O sistema DEVE exigir confirmação de email para acesso pleno. Um email com link de confirmação único e de tempo limitado DEVE ser enviado.
*   **RF-AUTH-003:** O sistema DEVE permitir que usuários existentes façam login usando Email e Senha. O sistema DEVE implementar proteção contra brute-force (ex: rate limiting, CAPTCHA após falhas).
*   **RF-AUTH-004 (Fortemente Recomendado Pós-MVP, se não no MVP):** O sistema DEVE oferecer Autenticação Multifator (MFA), preferencialmente TOTP (ex: Google Authenticator).
*   **RF-AUTH-005:** O sistema DEVE permitir que usuários redefinam sua senha. O fluxo DEVE envolver envio de link seguro, único e de tempo limitado (expiração: 15-30 minutos) ao email cadastrado. Nova senha DEVE seguir os mesmos critérios de complexidade. Notificação de segurança DEVE ser enviada após alteração.
*   **RF-AUTH-006:** No primeiro login bem-sucedido (após confirmação de email), o sistema DEVE solicitar ao usuário que forneça seu Nome Completo e faça o upload do "Currículo Base" em PDF, explicando a importância para a funcionalidade da plataforma. O usuário poderá pular esta etapa, mas as funcionalidades de otimização de currículo e IA contextual permanecerão limitadas/bloqueadas.
*   **RF-AUTH-007:** O sistema DEVE diferenciar usuários do tier gratuito e premium, aplicando as limitações/benefícios.

#### 3.1.2. Gerenciamento de Candidaturas (Kanban) - (PRD 3.1.1)
*   **RF-KAN-001:** O sistema DEVE permitir a captura de vagas via extensão de navegador (Chrome) para LinkedIn e Gupy.
    *   *Processo Extensão:* A extensão DEVE extrair automaticamente: Título da Vaga, Empresa, Link da Vaga, Descrição Completa, **Localização** (Cidade/Estado/Remoto/Híbrido), **Modalidade** (Remoto/Híbrido/Presencial), **Data da Publicação da Vaga** (se disponível, senão data de captura), **Nome da Plataforma de Origem**. Se a extração de campos chave falhar, o usuário DEVE ser informado e poder editar manualmente na extensão ou no PWA.
*   **RF-KAN-002:** O sistema DEVE permitir o input manual de vagas com todos os campos acima.
*   **RF-KAN-003:** O Kanban DEVE ter as colunas fixas (PRD 3.1.1).
*   **RF-KAN-004:** Drag-and-drop DEVE ser fluido para mover cards.
*   **RF-KAN-005:** Cards podem ser movidos para colunas anteriores.
*   **RF-KAN-006:** Notas nos cards/vagas DEVEM suportar **Markdown simples** (negrito, itálico, listas) com limite de 5000 caracteres.
*   **RF-KAN-007:** Permitir adicionar prazo (data) a cada card/vaga.
*   **RF-KAN-008:** Cards DEVEM exibir: Título da Vaga, Empresa, Data Publicação/Captura, Origem (ícone), Score de Aderência (se >0), Prazo (se definido).
*   **RF-KAN-009:** Busca e filtro de vagas no Kanban:
    *   **Busca textual avançada (case-insensitive, parcial):** Em Título, Empresa, Descrição Completa.
    *   **Filtros Combináveis:** Por Coluna, Data de Adição (intervalo), Data de Prazo (intervalo), Origem da Vaga, Vagas com Score de Aderência (sim/não, ou faixa de score).
*   **RF-KAN-010 (Tier Gratuito):** Limite de 10 vagas ativas.
*   **RF-KAN-011 (Tier Pago):** Vagas ativas ilimitadas.

#### 3.1.3. Otimização de Currículo com Inteligência Artificial (IA) - (PRD 3.1.2)
*   **RF-CV-001:** Upload do currículo base em PDF (limite **10MB**).
*   **RF-CV-002:** Parsing robusto do currículo PDF:
    *   *Processo:* Usar **`pymupdf` (Fitz)** para extração de texto/estrutura. Se necessário (PDF de imagem ou seção ilegível), usar **`Tesseract OCR`** (modelos pt-BR alta qualidade). Em seguida, **IA (LLM)** para categorizar semanticamente os blocos de texto extraídos nas seções padrão (ver RF-CV-003).
*   **RF-CV-003:** Campos a serem extraídos/categorizados pela IA e validados pelo usuário:
    *   Dados de Contato (Nome, Email, Telefone, LinkedIn, Cidade/Estado).
    *   Resumo/Objetivo Profissional.
    *   Experiência Profissional (Cargo, Empresa, Local, Período, Descrição detalhada incluindo responsabilidades, conquistas, tecnologias).
    *   Formação Acadêmica (Curso, Instituição, Local, Período, projetos).
    *   Habilidades Técnicas (Hard Skills, Ferramentas).
    *   Habilidades Comportamentais (Soft Skills).
    *   Idiomas (com nível).
    *   Certificações/Cursos.
    *   Projetos/Portfólio.
*   **RF-CV-004:** O sistema DEVE apresentar o conteúdo extraído e categorizado para **revisão e edição obrigatória pelo usuário** antes de prosseguir para a otimização, garantindo a precisão dos dados de entrada para a IA.
*   **RF-CV-005:** Análise IA (LLM Gemini 1.5 Pro) da descrição da vaga (colada ou capturada) e do "Currículo Ativo" validado:
    *   *Processo IA:* Identificar palavras-chave (semântica), requisitos, habilidades (obrigatórias/desejáveis), tom de voz. Comparar com o currículo.
    *   *Output IA:*
        1.  **Score de Congruência Geral (0-100):** Baseado em: correspondência semântica de palavras-chave/termos técnicos, profundidade/relevância da experiência, alinhamento de competências, adequação de senioridade (tentativa), presença de resultados quantificáveis.
        2.  **Relatório Detalhado do Score:** Explicando pontos fortes, gaps e áreas de melhoria.
        3.  **Sub-Scores Visuais e Textuais:** Para seções principais do currículo (ex: cada Experiência Profissional).
        4.  **Sugestões de Adaptações Contextualizadas (edições/adições):** Foco em otimização para ATS e impacto humano, com exemplos.
*   **RF-CV-006:** Apresentação das sugestões com "antes e depois", permitindo aceitar/editar/rejeitar. Input adicional do usuário para re-gerar sugestões (texto livre e opções pré-definidas baseadas em gaps).
*   **RF-CV-007:** Download do currículo otimizado em PDF (layout padronizado e profissional fornecido pelo sistema).
*   **RF-CV-008:** Gerenciamento do "Currículo Ativo":
    *   O usuário mantém um único "Currículo Ativo" editável.
    *   Ao otimizar, as alterações são um rascunho. Após baixar o PDF otimizado, o usuário DEVE ter a opção de "Salvar Alterações no Meu Currículo Ativo" ou "Descartar".
*   **RF-CV-009 (Contagem de "Otimização" - Tier Gratuito):** Cada análise completa pela IA (LLM) entre o Currículo Ativo e uma Descrição de Vaga, resultando em score e sugestões detalhadas. Re-gerações dentro de uma sessão de edição curta (ex: 30 min) para a mesma vaga/currículo NÃO contam adicionalmente. Limite de **3 otimizações/mês**.
*   **RF-CV-010 (Tier Pago):** Otimizações "ilimitadas" (com política de uso justo de **100 otimizações/mês**).
*   **RF-CV-011 (Tier Pago - Templates Avançados):** Mínimo de **7-10 templates** distintos, testados para ATS. Customização de cores, fontes (lista curada), ordem das seções, ligar/desligar seções opcionais.
*   **RF-CV-012 (Tier Pago - Análises Mais Detalhadas):**
    1.  Análise de Sentimento/Tom da Descrição da Vaga.
    2.  Benchmarking de Habilidades (comparar com N mais demandadas para o cargo/área, sugerir adjacentes).
    3.  Identificação Explícita de Gaps de Habilidades/Experiência com sugestões de como abordá-los.
    4.  Otimização de Impacto/Resultados (sugestões para reescrever bullet points focando em resultados mensuráveis - técnica STAR/CAR).
    5.  Previsão de 5-7 Perguntas de Entrevista Personalizadas (baseado na vaga/currículo) com dicas de resposta.
    6.  Análise de Palavras-Chave da Indústria (sugerir termos relevantes adicionais).

#### 3.1.4. Acompanhamento e "Coaching" com IA (Chatbot) - (PRD 3.1.3)
*   **RF-CHAT-001:** Interface de chatbot acessível (balão canto inferior direito).
*   **RF-CHAT-002 (Base de Conhecimento - RAG):** Extensa, continuamente atualizada (curadoria humana rigorosa), focada no mercado brasileiro (processos seletivos, legislação básica, negociação salarial, etiqueta).
*   **RF-CHAT-003 (Persona):** LLM DEVE operar com persona: Animado, inspirador, empático, especialista em recolocação no Brasil (via "system prompt" detalhado e "few-shot prompting"). Monitoramento e ajuste contínuos.
*   **RF-CHAT-004:** Dicas contextuais baseadas no status da vaga no Kanban.
*   **RF-CHAT-005:** Notificações na plataforma (e push no PWA) para lembretes e follow-ups.
*   **RF-CHAT-006 (Tier Gratuito - Gemini 2.5 Flash):** Limite de **30 interações/dia**. Sem "Treino Aprofundado para Entrevistas" ou "Análise de Carreira Personalizada". Respostas podem ter delay ligeiramente maior (informar). Sugestões mais genéricas.
*   **RF-CHAT-007 (Tier Pago - Gemini 2.5 Pro):** Acesso completo, incluindo:
    *   **Treino Aprofundado para Entrevistas:** Simulação interativa (chatbot como entrevistador), perguntas comportamentais (STAR), técnicas (baseadas na vaga). Usuário responde por texto. IA analisa resposta (adequação, clareza, exemplos, confiança inferida) e fornece feedback detalhado e acionável.

### 3.2. Requisitos Não Funcionais

#### 3.2.1. Desempenho (Core Web Vitals e IA)
*   **RNF-PERF-001 (PWA):** LCP ≤ 2.0s; FID ≤ 100ms (ou INP ≤ 200ms); CLS ≤ 0.1.
*   **RNF-PERF-002 (Otimização Currículo - Tier Premium):** ≤ 15 segundos (P90).
*   **RNF-PERF-003 (Chatbot - Tier Premium):** ≤ 3 segundos por resposta.
*   **RNF-PERF-004 (Kanban Drag-and-Drop):** Reflexo visual < 200ms.

#### 3.2.2. Usabilidade (UX/UI)
*   **RNF-USAB-001:** Interface simples, intuitiva (PRD 5.1). Flutter para consistência.
*   **RNF-USAB-002 (PWA):** Totalmente responsivo (desktops, tablets, smartphones).
*   **RNF-USAB-003:** Feedback visual contínuo.
*   **RNF-USAB-004 (Guia de Estilo):** Um **Guia de Estilo Abrangente e Documentado** DEVE ser criado e seguido, incluindo: paleta de cores, tipografia, grid/espaçamento, iconografia, estilo de botões/inputs, componentes básicos, tom de voz (UX Writing), princípios de acessibilidade (WCAG).

#### 3.2.3. Confiabilidade
*   **RNF-REL-001:** Disponibilidade da plataforma: Meta de **99.9%**.
*   **RNF-REL-002:** Tratamento de falhas de API (LLM, etc.) com feedback claro ao usuário e opção de nova tentativa.
*   **RNF-REL-003 (Monitoramento):** Utilizar Sentry.io (ou Datadog) para erros, Better Uptime (ou UptimeRobot) para disponibilidade, Logtail (ou similar) para logging centralizado. Monitorar uso/latência/erros de APIs LLM.
*   **RNF-REL-004 (Suporte):** FAQ detalhada e buscável. Chatbot para suporte básico. Email de suporte/sistema de tickets (Zendesk lite, Crisp) com SLA (Premium: 12h úteis, Gratuito: 24-48h úteis).

#### 3.2.4. Segurança (PRD 4.4)
*   **RNF-SEC-001:** Conformidade total com LGPD.
*   **RNF-SEC-002:** Criptografia para dados sensíveis em trânsito (HTTPS/TLS) e em repouso (AES-256 para currículos e PII no DB).
*   **RNF-SEC-003:** Política de Privacidade e Termos de Uso claros, acessíveis e validados juridicamente.
*   **RNF-SEC-004:** Consentimento explícito para coleta/processamento de dados (especialmente currículos e análise IA).
*   **RNF-SEC-005:** Proteção contra OWASP Top 10 (XSS, CSRF, SQLi, etc.).
*   **RNF-SEC-006 (Senhas):** Hashing com Argon2id.
*   **RNF-SEC-007 (MFA):** Implementação de MFA (TOTP) fortemente recomendada (se não no MVP, prioridade máxima pós-lançamento).

#### 3.2.5. Manutenibilidade
*   **RNF-MAINT-001:** Código modular, bem documentado. Flutter e FastAPI facilitam isso.
*   **RNF-MAINT-002:** Decisões de stack (Python/FastAPI, Flutter) consideram disponibilidade de talentos e ecossistemas robustos.

#### 3.2.6. Requisitos de IA Específicos
*   **RNF-AI-001 (Prompt Engineering):** Desenvolvimento e refinamento contínuo de prompts eficazes para todas as funcionalidades de IA em Português do Brasil.
*   **RNF-AI-002 (Mitigação de Vieses):**
    1.  Uso de LLMs com esforços declarados em redução de viés.
    2.  Prompt Engineering explícito para evitar vieses e focar em habilidades/experiência.
    3.  Testes com dados diversificados.
    4.  Auditoria humana regular das sugestões.
    5.  Mecanismo de feedback do usuário para reportar vieses.
    6.  Transparência sobre o uso e limitações da IA.
*   **RNF-AI-003 (Precisão Parsing PDF + Categorização IA):**
    *   Extração de Texto Bruto (PDFs textuais): **> 98%**.
    *   Categorização Semântica dos Blocos de Texto pela IA nas seções corretas: **> 90%**, com **revisão e correção obrigatória pelo usuário (RF-CV-004)**.

### 3.3. Requisitos de Interface Externa

#### 3.3.1. Interface do Usuário (UI)
*   **RI-UI-001:** PWA em Flutter Web, seguindo o Guia de Estilo.
*   **RI-UI-002:** Extensão de navegador (JS, HTML, CSS) com UI simples e intuitiva.

#### 3.3.2. Interfaces de Software (API)
*   **RI-API-001:** Interação segura (HTTPS, chaves de API seguras) com APIs Google Gemini.
*   **RI-API-002:** Comunicação segura (HTTPS) entre extensão e backend Recoloca.ai.

#### 3.3.3. Interfaces de Comunicação
*   **RI-COMM-001 (Email Transacional):** **Postmark** ou **Amazon SES** para alta entregabilidade (Supabase Auth para emails básicos de autenticação, se aplicável).
*   **RI-COMM-002 (Notificações Push PWA):** **Firebase Cloud Messaging (FCM)**.

## 4. Questões Abertas e Pontos para Definição Futura

Com os refinamentos, a maioria das questões técnicas e funcionais para o MVP foram abordadas. As questões primariamente em aberto são de natureza de negócio ou pesquisa de mercado contínua:

*   **Precificação Final do Tier Premium:** (R$ 19,90/semana ou R$ 59,90/mês – necessita validação final com análise de custos completa e pesquisa de mercado).
*   **Benefícios Premium Adicionais:** (Além dos já definidos, explorar continuamente com base no feedback do usuário e estratégia de negócio).
*   **Pesquisa Contínua sobre ATS:** O funcionamento dos ATS evolui; a pesquisa e adaptação das sugestões de IA devem ser contínuas.
*   **Estratégia de Marketing e Aquisição de Usuários Detalhada:** (Desenvolver e refinar continuamente).
*   **Coleta de Feedback de Satisfação (NPS/CSAT):** Escolha final de ferramentas (Sprig, Hotjar, Delighted) e implementação dos fluxos de coleta.
*   **Validação Jurídica Final:** Política de Privacidade e Termos de Uso.