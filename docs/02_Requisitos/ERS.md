---
sticker: lucide//heart-crack
---
# Especificação de Requisitos de Software (ERS): Recoloca. Ai

**Versão**: 0.9 (Pré-Revisão Interativa)

**Data de Criação**: 26 de maio de 2025

**Data de atualização**: 03 de junho de 2025

**Baseado em**:
- [[PLANO_MESTRE_RECOLOCA_AI]] (v 1.5)
- ERS Recoloca.Ai (v 0.5)
- Sessões de Pesquisa e Estratégia (Maio/Junho de 2025)
## 1. Introdução

### 1.1. Propósito

Este documento especifica os **requisitos funcionais** (RF) e **não funcionais** (RNF) para a Versão Mínima Viável (MVP) e a evolução inicial da plataforma **Recoloca. Ai**. O Recoloca. Ai é um Micro-SaaS projetado para auxiliar **profissionais de TI de nível Pleno e Sênior no Brasil** no processo de recolocação profissional, atuando como um "cockpit" que combina gerenciamento de candidaturas, otimização de currículos com Inteligência Artificial (IA) e um assistente de IA para coaching. Esta especificação foi refinada com base em pesquisa de mercado, análise de concorrência e validação de proposta de valor, buscando um equilíbrio entre visão estratégica e detalhamento suficiente para guiar o desenvolvimento assistido por IA, alinhado com a versão 1.5 do [[PLANO_MESTRE_RECOLOCA_AI]].

Este documento destina-se a:
- Guiar o desenvolvimento do produto pelo "Maestro" (desenvolvedor solo).
- Servir como a especificação primária para os **Agentes de IA Mentores** configurados no Trae IDE, fornecendo contexto e clareza para minimizar suposições.
- Formar a base para o planejamento de testes e validação de qualidade.
- Ser um componente central da "Documentação Viva" do projeto, integrado ao sistema RAG.
### 1.2. Escopo do Produto (MVP e Evolução Inicial)

O escopo do MVP do Recoloca. Ai visa entregar valor central através das seguintes funcionalidades principais:
1.  **Gerenciamento de Candidaturas (Kanban):** Um sistema visual para o usuário organizar e acompanhar suas aplicações a vagas.
2.  **Importação Inteligente de Vagas:** Facilidade para adicionar vagas à plataforma, inicialmente via link com processamento por LLM.
3.  **Otimização de Currículo Baseada em IA:** Análise de currículo do usuário em relação a descrições de vagas, com sugestões de melhoria e score de adequação (**Momento AHA! Principal**).
4.  **Estimativa de Range Salarial com IA:** Análise da descrição da vaga para fornecer uma estimativa de faixa salarial.
5.  **Assistente de IA para Coaching Básico:** Suporte inicial para dúvidas e orientações sobre o processo de recolocação.
6.  **Módulo de Métricas Pessoais:** Para acompanhamento do funil de candidatura.

### 1.3. Estratégia de Produto e Priorização
**Diferencial Competitivo Principal:** Assistente/Coach de IA contextual que analisa vagas e perfil do usuário.

**Momento AHA! Definido:** Edição do currículo base com IA para combinar perfeitamente com a descrição da vaga específica.

**Abordagem de Desenvolvimento:** Wizard-style focado na jornada completa do usuário, priorizando fluxo de valor sobre complexidade técnica.

**Jornada Detalhada:** Documentada em [[docs/02_Requisitos/HU_AC/HU_MVP_Jornada_Usuario.md]]

Funcionalidades como Web Clipper avançado (extensão de navegador para múltiplos sites), simulação de entrevistas detalhadas, gerenciador de networking aprofundado e biblioteca de recursos extensa são consideradas para evoluções futuras (Pós-MVP) ou como parte de tiers premium. O foco inicial é em profissionais de TI no Brasil, com currículos e vagas primariamente em Português, Inglês e Espanhol. A PWA será a plataforma primária, com a extensão de navegador (para captura de vagas do LinkedIn) sendo Pós-MVP.
### 1.3. Definições, Acrônimos e Abreviações
- **IA:** Inteligência Artificial
- **LLM:** Large Language Model (Modelo de Linguagem Amplo)
- **MVP:** Minimum Viable Product (Produto Mínimo Viável)
- **RF:** Requisito Funcional
- **RNF:** Requisito Não Funcional
- **ATS:** Applicant Tracking System (Sistema de Rastreamento de Candidatos)
- **RAG:** Retrieval-Augmented Generation
- **UX:** User Experience (Experiência do Usuário)
- **UI:** User Interface (Interface do Usuário)
- **RLS:** Row-Level Security (Segurança em Nível de Linha)
- **JWT:** JSON Web Token
- **API:** Application Programming Interface (Interface de Programação de Aplicações)
- **BaaS:** Backend as a Service
- **SaaS:** Software as a Service
- **PWA:** Progressive Web Application
- **LGPD:** Lei Geral de Proteção de Dados Pessoais
- **HLD:** High-Level Design
- **LLD:** Low-Level Design
- **ADR:** Architecture Decision Record
- **Maestro:** O desenvolvedor solo do projeto.
- **Agente Mentor de IA:** Agente de IA especializado no Trae IDE.
### 1.4. Referências
- [[PLANO_MESTRE_RECOLOCA_AI]] (v 1.2 ou mais recente)
- [[GUIA_AVANCADO]] (v 2.0 ou mais recente)
- Documentação das APIs: Google Gemini, Supabase, FastAPI.
- Pesquisas de mercado e salariais da área de TI no Brasil (a serem compiladas para o RAG).
- Discussões de Refinamento e Pesquisa (Maio de 2025).
### 1.5. Visão Geral do Documento
Este documento está organizado da seguinte forma:
- **Seção 1:** Introdução, propósito, escopo, definições e referências.
- **Seção 2:** Descrição geral do produto, funcionalidades, usuários e restrições.
- **Seção 3:** Requisitos Funcionais (RFs) detalhados.
- **Seção 4:** Requisitos Não Funcionais (RNFs) detalhados.
- **Seção 5:** Outros Requisitos (Interface, Documentação).
- **Seção 6:** Próximos Passos Críticos para Validação e Mitigação de Riscos.
## 2. Descrição Geral do Produto

### 2.1. Perspectiva do Produto
O Recoloca. Ai é uma plataforma SaaS web (PWA robusta construída com Flutter) que se posiciona como o **"cockpit do candidato"**. Ele não é um portal de vagas, mas uma ferramenta de produtividade e inteligência que auxilia o profissional a gerenciar suas candidaturas, otimizar seus materiais e se preparar melhor para os desafios da recolocação, integrando-se ao ecossistema de busca de vagas existente.
### 2.2. Funções do Produto (Resumo MVP)
1.  Gerenciamento Visual e Enriquecido de Candidaturas (Kanban).
2.  Importação de Vagas via Link com Processamento LLM.
3.  Análise de Currículo vs. Vaga e Score de Adequação por IA.
4.  Sugestões de Otimização de Currículo por IA.
5.  Estimativa de Range Salarial da Vaga por IA.
6.  Módulo de Métricas Pessoais de Candidatura.
7.  Assistente IA para Coaching Básico e Proativo.
8.  Gerenciamento de Conta e Currículos Base (Multi-idioma PT, EN, ES).
9.  Modelo Freemium com Tiers de Funcionalidades.
### 2.3. Características dos Usuários
- **Público Principal (MVP):** Profissionais de Tecnologia da Informação de **nível Pleno e Sênior** (Desenvolvedores, Analistas, QAs, Designers, Product Managers, etc.) no Brasil, buscando recolocação ou novas oportunidades.
- **Nível de Experiência:** Desde juniores buscando o primeiro emprego até seniores e especialistas.
- **Necessidades:** Organização, eficiência, destaque em processos seletivos, insights sobre o mercado, redução da ansiedade e frustração.
- **Habilidades Técnicas Esperadas:** Confortáveis com ferramentas digitais e SaaS.
### 2.4. Restrições Gerais e Tecnológicas
- **Desenvolvimento Solo:** O escopo do MVP deve ser gerenciável por um único desenvolvedor ("Maestro") com auxílio de Agentes de IA.
- **Orçamento:** Custos de APIs (Gemini) e infraestrutura (Supabase, Vercel/Render) devem ser considerados para a sustentabilidade do modelo Freemium.
- **LGPD:** Conformidade estrita com a Lei Geral de Proteção de Dados Pessoais.
- **Limitações de IA:** O usuário deve ser informado sobre as limitações das sugestões da IA e que elas não substituem o julgamento profissional.
- **Idioma (MVP):** Português do Brasil para interface. Suporte a dados (CVs, vagas) em Português, Inglês, Espanhol.
- **Plataforma (MVP):** PWA (Flutter Web) acessível em navegadores modernos.
- **Stack Tecnológica Principal (Conforme Plano Mestre):**
    - Frontend (PWA): **Flutter (Dart)**.
    - Backend: **Python com FastAPI**.
    - Banco de Dados: **PostgreSQL (Via Supabase)**.
    - Autenticação & Storage: **Supabase**.
    - IA LLM: APIs **Google Gemini Pro e Flash**.
    - Parsing de PDF: `pymupdf` (Fitz) primário; OCR (`Tesseract`) como fallback; LLM para categorização semântica.
    - Hospedagem: Frontend PWA em **Vercel** (ou similar); Backend FastAPI em **Render** (ou similar); Supabase para BaaS.
    - Vector DB (para RAG): **FAISS** para implementação local inicial; considerar Supabase pgvector (Pós-MVP).
- **Importação de Vagas (MVP):** Foco na importação via link com processamento LLM. Extensão de navegador para captura direta (ex: LinkedIn) é Pós-MVP.
### 2.5. Premissas e Dependências
- Disponibilidade e funcionalidade das APIs do Google Gemini e serviços do Supabase.
- O usuário fornecerá informações precisas em seu currículo base e nos links das vagas.
- Acesso a pesquisas e dados de mercado para treinar/alimentar o RAG da IA de estimativa salarial.
- A arquitetura RLS entre FastAPI e Supabase será validada via protótipo.
## 3. Requisitos Funcionais (RF)

A seguir, os IDs dos requisitos são prefixados com `RF-[MÓDULO]-[NÚMERO]`. Detalhes de processo e output são fornecidos para clareza dos Agentes de IA.

---
**Módulo: Autenticação e Gerenciamento de Conta** `RF-AUTH`
---
-   **RF-AUTH-001:** O sistema DEVE permitir que novos usuários se cadastrem fornecendo Email e Senha.
    -   _Processo: _ Validar formato do email e unicidade. Senha deve atender critérios de complexidade (mín. 12 caracteres, maiúsculas, minúsculas, números, símbolos). Hashing seguro (Argon 2 id). Criação de registro no Supabase Auth. Envio de email de confirmação.
    -   _Output: _ Conta criada com status "não confirmado". Mensagem de sucesso.
-   **RF-AUTH-002:** O sistema DEVE exigir confirmação de email para ativar a conta.
    -   _Processo: _ Link único e de tempo limitado no email. Atualização do status do usuário para "confirmado" ao clicar.
    -   _Output: _ Acesso pleno às funcionalidades.
-   **RF-AUTH-003:** O sistema DEVE permitir login com Email e Senha.
    -   _Processo: _ Verificação de credenciais. Proteção contra brute-force (rate limiting, CAPTCHA).
    -   _Output: _ Sessão autenticada (JWT).
-   **RF-AUTH-004 (Pós-MVP):** O sistema DEVE oferecer Autenticação Multifator (MFA) via TOTP.
-   **RF-AUTH-005:** O sistema DEVE permitir redefinição de senha.
    -   _Processo: _ Usuário informa email. Envio de link seguro e de tempo limitado. Usuário define nova senha (mesma complexidade). Notificação de segurança por email.
    -   _Output: _ Senha redefinida.
-   **RF-AUTH-006:** O sistema DEVE guiar o usuário no onboarding inicial (após 1º login), solicitando Nome Completo e upload do "Currículo Base" (PDF).
    -   _Processo: _ Explicar importância. Permitir pular, informando limitações.
    -   _Output: _ Perfil inicial e currículo base armazenados.
-   **RF-AUTH-007:** O sistema DEVE diferenciar tiers (gratuito/premium) e aplicar limitações/benefícios.
-   **RF-AUTH-008:** O sistema DEVE permitir ao usuário visualizar e editar Nome e Email no perfil.
-   **RF-AUTH-009:** O sistema DEVE permitir ao usuário gerenciar seus currículos base (upload de novos, exclusão, definir padrão por idioma PT/EN/ES no MVP).
-   **RF-AUTH-010:** O sistema DEVE permitir ao usuário configurar preferências de notificação.
-   **RF-AUTH-011:** O sistema DEVE permitir ao usuário visualizar e gerenciar o status da assinatura (plano, pagamentos, upgrade/downgrade/cancelamento).
-   **RF-AUTH-012:** O sistema DEVE permitir ao usuário excluir sua conta e dados (conforme LGPD).

---
**Módulo: Kanban (Cockpit de Candidaturas)** `RF-KAN`
---
-   **RF-KAN-001:** O sistema DEVE permitir ao usuário criar, visualizar, editar e excluir cartões de vagas no Kanban.
    -   _Processo: _ Criação manual ou via importação (RF-IMP-001). Campos do cartão: Título da Vaga, Empresa, Link Original, Status (coluna), Data de Adição, Prioridade, Anotações (Markdown), Localização, Modalidade, Data de Publicação/Captura, Origem, Score de Adequação (se calculado), Prazo.
    -   _Output: _ Cartão de vaga gerenciável no Kanban.
-   **RF-KAN-002:** O sistema DEVE apresentar as vagas em colunas fixas e ordenadas: "Salvas", "Radar de Interesse", "Aplicadas", "Entrevista (s)", "Teste (s)", "Proposta", "Recusada/Fechada".
    -   _Processo: _ Usuário move cartões entre colunas (drag-and-drop).
    -   _Output: _ Visualização do pipeline de candidatura.
-   **RF-KAN-003:** O sistema DEVE permitir filtros e ordenação dos cartões (Empresa, Data, Prioridade, Status, Idioma, etc.).
-   **RF-KAN-004:** O sistema DEVE permitir registrar um histórico de interações para cada vaga (data da aplicação, contatos, feedbacks, etc.).
-   **RF-KAN-005:** O sistema DEVE fornecer um dashboard de métricas pessoais (funil de candidatura):
    -   _Processo: _ Coleta dados dos status das vagas e interações. Apresenta visualmente: Nº de aplicações/período, Taxas de conversão entre etapas (ex: Salvas -> Aplicadas, Aplicadas -> Entrevistas), Tempo médio em cada etapa.
    -   _Output: _ Gráficos e números resumindo o progresso do usuário.
- **RF-KAN-006 (Tier Gratuito):** Limite de **10 vagas ativas** (não em "Recusada/Fechada").
-   **RF-KAN-007 (Tier Pago):** Vagas ativas ilimitadas.

---
**Módulo: Importação de Vagas** `RF-IMP`
---
-   **RF-IMP-001 (MVP):** O sistema DEVE permitir importar uma vaga colando a URL.
    -   _Processo: _ Usuário fornece URL. IA (LLM) tenta extrair: Título, Empresa, Descrição, Requisitos, Localização, Modalidade, Idioma. Suporte inicial para PT, EN, ES.
    -   _Output: _ Campos pré-preenchidos para revisão do usuário (RF-IMP-002).
-   **RF-IMP-002:** O sistema DEVE permitir ao usuário revisar, editar e complementar os dados extraídos pela IA antes de salvar a vaga no Kanban.
-   **RF-IMP-003 (Pós-MVP):** Extensão de navegador (Chrome) para captura de vagas do LinkedIn.

---
**Módulo: Otimização de Currículo com IA** `RF-CV`
---
-   **RF-CV-001:** O sistema DEVE permitir upload e gerenciamento de múltiplos currículos base (PDF, até 10 MB), um para cada idioma (PT, EN, ES no MVP).
    -   _Processo: _ Extração de texto via `pymupdf` (primário) ou OCR `Tesseract` (fallback). Categorização semântica das seções (Contato, Experiência, Formação, Habilidades, etc.) via LLM.
    -   _Output: _ Conteúdo do CV estruturado para validação do usuário.
-   **RF-CV-002:** O sistema DEVE apresentar o conteúdo extraído e estruturado para **revisão, edição e validação obrigatória pelo usuário**, formando o "Currículo Base Ativo" para um idioma.
-   **RF-CV-003:** Para uma vaga selecionada, a IA DEVE analisar a adequação do "Currículo Base Ativo" (do idioma correspondente à vaga) com a descrição da vaga.
    -   _Processo IA: _ Identificar palavras-chave, requisitos técnicos/comportamentais, habilidades, tom da vaga. Comparar com o currículo. Consultar RAG (Glassdoor, etc.) para contexto da empresa/vaga.
    -   _Output IA (Score de Adequação): _ Pontuação (0-100%) e relatório detalhado (pontos fortes, gaps, áreas de melhoria).
-   **RF-CV-004:** A IA DEVE fornecer sugestões específicas e contextualizadas para otimizar o currículo para a vaga.
    -   _Processo IA: _ Sugerir edições, adições, reformulações focadas em ATS e impacto humano.
    -   _Output IA: _ Sugestões interativas (antes/depois), permitindo aceitar, editar ou rejeitar.
-   **RF-CV-005:** O sistema DEVE, usando IA e RAG (pesquisas salariais), fornecer uma estimativa de range salarial para a vaga.
    -   _Processo IA: _ Analisar descrição da vaga, localidade, senioridade inferida, e cruzar com dados de mercado.
    -   _Output IA: _ Range salarial estimado (ex: R $X.XXX - R$Y.YYY), com aviso de que é uma estimativa.
-   **RF-CV-006:** O sistema DEVE permitir download do currículo otimizado em PDF (usando templates profissionais e ATS-friendly).
-   **RF-CV-007:** O sistema DEVE permitir salvar versões otimizadas e que o usuário escolha se elas atualizam o "Currículo Base Ativo".
- **RF-CV-008 (Tier Gratuito - Contagem):** Limite de **3 "Otimizações Completas" por mês** (análise IA + score + sugestões + range salarial).
-   **RF-CV-009 (Tier Pago):** Otimizações "ilimitadas" (sujeito a política de uso justo, ex: 100/mês). Acesso a templates de CV avançados e análises mais detalhadas da IA (conforme ERS v 0.3, RF-CV-012).

---
**Módulo: Assistente de IA para Coaching** `RF-COACH`
---
-   **RF-COACH-001:** Interface de chatbot acessível para coaching.
    -   _Processo: _ Usuário interage com LLM (Gemini Flash para gratuito, Pro para pago) com persona definida (Animado, inspirador, empático, prático, especialista em recolocação BR).
    -   _Output: _ Respostas e orientações baseadas em RAG (base de conhecimento curada) e contexto do usuário.
-   **RF-COACH-002:** IA Coach DEVE atuar proativamente.
    -   _Processo: _ Monitorar atividades no Kanban (com consentimento). Após X tempo de uma vaga adicionada ou em certo status, IA pergunta sobre progresso, dificuldades, oferece dicas, incentiva atualização.
    -   _Output: _ Notificações/mensagens no chat.
-   **RF-COACH-003:** IA Coach DEVE fornecer orientações sobre soft skills, tendências de mercado e preparação para entrevistas.
-   **RF-COACH-004:** IA Coach DEVE usar métricas do usuário (RF-KAN-005) para identificar gargalos e sugerir foco.
- **RF-COACH-005 (Tier Gratuito):** Limite de **15 interações/dia**. Respostas mais genéricas.
-   **RF-COACH-006 (Tier Pago):** Interações "ilimitadas". Respostas mais elaboradas (Gemini Pro). Simulações de entrevista interativas com feedback (Pós-MVP).

## 4. Requisitos Não Funcionais (RNF)

**Performance** `RNF-PERF` (Core Web Vitals)
---
-   **RNF-PERF-002 (Otimização de Currículo - P 90):** Análise de CV vs Vaga e sugestões iniciais pela IA DEVE ser **≤ 15 segundos**.
-   **RNF-PERF-003 (Chatbot - P 90):** Resposta do chatbot DEVE ser **≤ 3-5 segundos**.

---
**Segurança** `RNF-SEC` (Incluindo LGPD, RLS, OWASP)
---
-   **RNF-SEC-00 X (Validação de Senha):** Senha DEVE ter no mínimo 12 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos. DEVE ser verificada contra listas de senhas vazadas conhecidas (ex: API "Have I Been Pwned" ou similar) durante o cadastro.

---
**Usabilidade** `RNF-USAB` (UX superior, responsividade)
---
-   **RNF-USAB-00 X (Acessibilidade):** Meta WCAG 2.1 Nível AA.

---
**Confiabilidade** `RNF-REL` (Disponibilidade 99.9%, tratamento de falhas)
---
-   **RNF-REL-00 X (Monitoramento e Logging):** Utilizar Sentry. Io (ou Datadog) para erros, Better Uptime (ou UptimeRobot) para disponibilidade, e logging centralizado. Monitorar ativamente APIs LLM.
-   **RNF-REL-00 Y (Suporte ao Usuário):** FAQ buscável, chatbot para suporte básico, canal de email/ticket com SLAs definidos.

---
**Manutenibilidade** `RNF-MAINT` (Código modular, documentado)
---
-   **RNF-MAINT-00 X (Configuração como Código):** Infraestrutura (ex: `render` `Yaml`) e CI/CD DEVEM ser gerenciados como código.

---
**IA: Precisão, Ética e Relevância** `RNF-IA` (Consolidado e Detalhado)
---
-   **RNF-IA-001 (Precisão e Relevância):**
    -   Sugestões da IA (CV, coach) DEVEM ser relevantes e úteis.
    -   Score de Adequação e Range Salarial DEVEM ser consistentes e baseados em lógica defensável.
    -   **Precisão Parsing PDF + Categorização IA (Meta):** Extração de texto bruto > 98% para PDFs textuais. Categorização semântica das seções do CV pela IA > 90% ANTES da validação do usuário. A etapa de validação pelo usuário (RF-CV-002) é crucial.
-   **RNF-IA-002 (Engenharia de Prompt):** Processo contínuo de desenvolvimento, teste e refinamento de prompts eficazes e robustos para PT-BR, EN, ES. Templates gerenciados em [[05_Prompts/]].
-   **RNF-IA-003 (Mitigação de Vieses e Ética):**
    -   Utilizar LLMs de provedores com foco em mitigação de vieses.
    -   Prompts explícitos para evitar vieses (gênero, raça, etc.) e focar em qualificações objetivas.
    -   Auditoria humana regular das sugestões da IA.
    -   Mecanismo para usuários reportarem sugestões inadequadas.
    -   Transparência sobre uso e limitações da IA.
-   **RNF-IA-004 (Consistência da Persona do Chatbot):** Persona (RF-COACH-001) DEVE ser mantida consistentemente.
- **RNF-IA-005 (Rastreabilidade e Explicabilidade - XAI):** O sistema DEVE fornecer justificativas claras e compreensíveis para as principais sugestões e análises da IA (especialmente em otimização de CV e score de adequação), permitindo ao usuário entender o "porquê" das recomendações. Isso pode incluir destacar as seções do CV ou da vaga que mais influenciaram o resultado.
- **RNF-IA-006 (Governança de IA e Conformidade Ética):**
    - O sistema DEVE seguir os princípios de IA Responsável definidos no [[PLANO_MESTRE_RECOLOCA_AI]] (Transparência, Mitigação de Vieses, Privacidade, Controle Humano, Módulo Educativo).
    - O sistema DEVE estar em conformidade com a LGPD e preparado para adaptações futuras relacionadas a regulações de IA (como o PL 2.338/2023, se aprovado e aplicável).
    - Auditorias e monitoramento contínuo dos modelos e sugestões da IA DEVEM ser planejados para garantir a conformidade e a ética.

---
**Internacionalização (i 18 n) e Localização (l 10 n)** `RNF-I 18 N` 
---
## 5. Outros Requisitos

### 5.1. Requisitos de Interface Externa
-   Google Gemini API, Supabase, Gateway de Pagamento.
### 5.2. Requisitos de Documentação
-   **RNF-DOC-001 (Manutenibilidade para RAG):** Toda a documentação do projeto (ERS, HLD, LLDs, ADRs, Plano Mestre) DEVE ser escrita e mantida em Markdown, utilizando links internos (` [[Arquivo.md]] `) e uma estrutura clara de cabeçalhos para facilitar o processamento, indexação e recuperação eficiente pelo sistema RAG, fornecendo contexto preciso aos Agentes de IA.
-   **RNF-DOC-002 (Atualização Contínua):** A documentação DEVE ser tratada como um artefato vivo e atualizada continuamente.
-   **RNF-DOC-003 (Documentação do Usuário - Pós-MVP):** FAQ ou base de conhecimento simples.
## 6. Próximos Passos Críticos para Validação e Mitigação de Riscos

1.  **Validação Técnica da Arquitetura de Autenticação (Protótipo RLS FastAPI/Supabase)**
2.  **Estimativa Detalhada de Custos Operacionais (API Gemini, Infraestrutura)**
3.  **Validação Qualitativa com Usuários-Alvo (Protótipos de Baixa Fidelidade e Entrevistas)**

---
**Fim do Documento ERS v 0.5**
