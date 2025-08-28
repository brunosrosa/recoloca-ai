---
sticker: lucide//heart-crack
---
# Especificação de Requisitos de Software (ERS): Recoloca. Ai

**Versão**: 1.1 (Orquestração Inteligente e Specialized Intelligence)

**Data de Criação**: 26 de maio de 2025

**Data de atualização**: Janeiro de 2025

**Baseado em**:
- [[PLANO_MESTRE_RECOLOCA_AI]] (v1.0+)
- [[TAP]] (v1.0)
- [[METRICAS_SUCESSO_BASE_MERCADO]] (v1.0)
- Sessões de Pesquisa e Estratégia (Maio/Junho de 2025)
## 1. Introdução

### 1.1. Propósito

Este documento especifica os **requisitos funcionais** (RF) e **não funcionais** (RNF) para a Versão Mínima Viável (MVP) e a evolução inicial da plataforma **Recoloca.AI**. O Recoloca.AI é um Micro-SaaS projetado para auxiliar **profissionais de TI de nível Pleno e Sênior no Brasil** no processo de recolocação profissional, atuando como um **"integrador e cockpit"** que combina gerenciamento de candidaturas, otimização de currículos com Inteligência Artificial (IA) e um assistente de IA para coaching proativo. Esta especificação foi refinada com base em pesquisa de mercado, análise de concorrência, validação de proposta de valor e métricas de sucesso baseadas em benchmarks de mercado, buscando um equilíbrio entre visão estratégica e detalhamento suficiente para guiar o desenvolvimento assistido por IA, alinhado com o [[PLANO_MESTRE_RECOLOCA_AI]] e [[TAP]] v1.0.

Este documento destina-se a:
- Guiar o desenvolvimento do produto pelo "Maestro" (desenvolvedor solo).
- Servir como a especificação primária para os **Agentes de IA Mentores** configurados no Trae IDE, fornecendo contexto e clareza para minimizar suposições.
- Formar a base para o planejamento de testes e validação de qualidade.
- Ser um componente central da "Documentação Viva" do projeto, integrado ao sistema RAG.
### 1.2. Escopo do Produto (MVP e Evolução Inicial)

O escopo do MVP do Recoloca.AI visa entregar valor central através das seguintes funcionalidades principais:
1.  **Gerenciamento de Candidaturas (Kanban):** Sistema visual para organizar e acompanhar aplicações com pipeline estruturado
2.  **Importação Inteligente de Vagas:** Facilidade para adicionar vagas via link com processamento por LLM
3.  **Otimização de Currículo Baseada em IA:** Análise de adequação CV vs. vaga com sugestões contextualizadas (**Momento AHA! Principal**)
4.  **Estimativa de Range Salarial com IA:** Análise da vaga para estimativa de faixa salarial baseada em dados de mercado
5.  **Coach IA Proativo:** Assistente contextual que monitora progresso e oferece orientações personalizadas
6.  **Módulo de Métricas Pessoais:** Dashboard de acompanhamento do funil de candidatura com KPIs
7.  **PWA Responsiva:** Aplicação web progressiva otimizada para desktop e mobile
8.  **Suporte Multilíngue:** Interface em PT-BR com suporte a dados em PT, EN, ES
9.  **Modelo Freemium:** Tiers diferenciados com funcionalidades premium via Stripe

### 1.3. Estratégia de Produto e Priorização
**Diferencial Competitivo Principal:** Coach IA proativo e contextual que atua como "integrador e cockpit" do processo de recolocação.

**Momento AHA! Definido:** Otimização automática do currículo com score de adequação e sugestões específicas para a vaga.

**Abordagem de Desenvolvimento:** "Solo Ágil Aumentado por IA" com foco na jornada completa do usuário e entrega de valor incremental.

**Metodologia de Orquestração Inteligente:** Implementação de "Specialized Intelligence" com métricas objetivas para agentes Production-Ready:

**Métricas de "Specialized Intelligence":**
- **Eficiência de Orquestração:** Tempo médio de resolução de tarefas complexas (< 2h para tarefas padrão)
- **Qualidade do Sistema RAG:** Precisão de recuperação de informações relevantes (> 85%)
- **Satisfação e Produtividade:** Redução de retrabalho e aumento da qualidade das entregas

**Critérios Objetivos para Agentes "Production-Ready":**
- **Tier 1 (Básico):** Precisão > 80%, Tempo de resposta < 30s, Contextualização adequada
- **Tier 2 (Avançado):** Precisão > 90%, Tempo de resposta < 15s, Integração completa com RAG
- **Tier 3 (Expert):** Precisão > 95%, Tempo de resposta < 10s, Autonomia operacional completa

**Cronograma MVP:** Junho - Dezembro 2025 (7 meses)

**Métricas de Sucesso:** Baseadas em benchmarks de mercado SaaS B2C conforme [[METRICAS_SUCESSO_BASE_MERCADO]]

**Escopo Pós-MVP:** Web Clipper avançado (extensão de navegador), simulação de entrevistas detalhadas, gerenciador de networking, biblioteca de recursos, integração com ATS, analytics avançados.

**Público-Alvo Inicial:** Profissionais de TI no Brasil (Desenvolvedores, QAs, Designers, PMs, Analistas) de nível Pleno e Sênior.

**Plataforma Primária:** PWA (Flutter Web) com experiência mobile-first.

**Idiomas Suportados:** Interface em PT-BR, dados em PT/EN/ES.
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
- **Maestro:** O desenvolvedor solo do projeto (Bruno S. Rosa)
- **Agente Mentor de IA:** Agente de IA especializado no Trae IDE
- **PMF Score:** Sean Ellis Product-Market Fit Score
- **CAC:** Customer Acquisition Cost
- **LTV:** Lifetime Value
- **MRR:** Monthly Recurring Revenue
- **ARPU:** Average Revenue Per User
### 1.4. Referências
- [[PLANO_MESTRE_RECOLOCA_AI]] (v1.5+)
- [[TAP]] (v1.0)
- [[METRICAS_SUCESSO_BASE_MERCADO]] (v1.0)
- [[GUIA_AVANCADO]] (v2.0+)
- Documentação das APIs: Google Gemini, Supabase, FastAPI, Stripe
- Benchmarks de mercado SaaS B2C e plataformas de carreira
- Pesquisas salariais da área de TI no Brasil (RAG)
- Sessões de Refinamento e Pesquisa (Maio/Junho 2025)
### 1.5. Visão Geral do Documento
Este documento está organizado da seguinte forma:
- **Seção 1:** Introdução, propósito, escopo, definições e referências.
- **Seção 2:** Descrição geral do produto, funcionalidades, usuários e restrições.
- **Seção 3:** Requisitos Funcionais (RFs) detalhados.
- **Seção 4:** Requisitos Não Funcionais (RNFs) detalhados.
- **Seção 4.X (Nova):** Requisitos Não Funcionais específicos para Pagamentos (Stripe) e Autenticação Social.
- **Seção 5:** Outros Requisitos (Interface, Documentação).
- **Seção 6:** Próximos Passos Críticos para Validação e Mitigação de Riscos.
## 2. Descrição Geral do Produto

### 2.1. Perspectiva do Produto
O Recoloca.AI é uma plataforma SaaS web (PWA robusta construída com Flutter) que se posiciona como **"integrador e cockpit"** do processo de recolocação profissional. Não é um portal de vagas, mas uma ferramenta de produtividade e inteligência que centraliza, organiza e otimiza todo o processo de candidatura, integrando-se ao ecossistema existente (LinkedIn, portais de vagas) e fornecendo insights acionáveis através de IA.
### 2.2. Funções do Produto (Resumo MVP)
1.  **Kanban de Candidaturas:** Gerenciamento visual com pipeline estruturado e métricas
2.  **Importação Inteligente:** Processamento de vagas via link com extração automática de dados
3.  **Otimização de CV com IA:** Score de adequação e sugestões contextualizadas
4.  **Estimativa Salarial:** Range baseado em dados de mercado e análise da vaga
5.  **Coach IA Proativo:** Assistente contextual com monitoramento de progresso
6.  **Dashboard de Métricas:** KPIs pessoais e insights de performance
7.  **PWA Responsiva:** Experiência otimizada para desktop e mobile
8.  **Gestão de Perfil:** Múltiplos CVs base e configurações personalizadas
9.  **Modelo Freemium:** Integração Stripe com tiers diferenciados
10. **Suporte Multilíngue:** Interface PT-BR, dados PT/EN/ES
### 2.3. Características dos Usuários
- **Público Principal (MVP):** Profissionais de TI de **nível Pleno e Sênior** no Brasil (Desenvolvedores, QAs, Designers, Product Managers, Analistas, DevOps, etc.) em processo de recolocação ou transição de carreira.
- **Segmentação Inicial:** 
  - **Early Adopters:** Profissionais tech-savvy em transição ativa
  - **Power Users:** Profissionais que gerenciam múltiplas candidaturas
  - **Career Changers:** Profissionais buscando mudança de área/senioridade
- **Nível de Experiência:** Foco em Pleno/Sênior, com expansão futura para Junior/Especialista.
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
**Módulo: Landing Page e Marketing** `RF-LAND`
---
-   **RF-LAND-001:** O sistema DEVE apresentar uma página inicial (Landing Page) atrativa e informativa para visitantes não autenticados.
    -   _Processo:_ Apresentar proposta de valor clara, benefícios do produto, depoimentos/casos de uso, seções explicativas sobre funcionalidades principais.
    -   _Output:_ Página responsiva e otimizada para conversão.
-   **RF-LAND-002:** A Landing Page DEVE incluir uma seção Hero com headline impactante e call-to-action (CTA) principal para registro.
    -   _Processo:_ Headline focada no problema/solução, subtítulo explicativo, botão CTA destacado direcionando para registro.
    -   _Output:_ Seção Hero otimizada para primeira impressão e conversão.
-   **RF-LAND-003:** A Landing Page DEVE incluir um CTA (Call-to-Action) proeminente para registro de novos usuários.
    -   _Processo:_ Botão/link destacado visualmente, texto persuasivo (ex: "Comece Grátis", "Otimize seu CV Agora"), direcionamento para página de registro.
    -   _Output:_ CTA que maximize a taxa de conversão de visitante para usuário registrado.
-   **RF-LAND-004:** A Landing Page DEVE apresentar as principais funcionalidades do produto de forma clara e visual.
    -   _Processo:_ Seções explicativas sobre Kanban de vagas, Otimização de CV com IA, AI Coach, com ícones/imagens ilustrativas.
    -   _Output:_ Comunicação efetiva do valor do produto.
-   **RF-LAND-005:** A Landing Page DEVE incluir informações sobre os planos (Gratuito vs Premium) e seus benefícios.
    -   _Processo:_ Tabela comparativa ou seções destacando limitações do plano gratuito e vantagens do premium.
    -   _Output:_ Transparência sobre modelo de negócio e incentivo ao upgrade.
-   **RF-LAND-006:** A Landing Page DEVE ser responsiva e otimizada para dispositivos móveis e desktop.
    -   _Processo:_ Design responsivo, tempos de carregamento otimizados, compatibilidade com navegadores modernos.
    -   _Output:_ Experiência consistente em diferentes dispositivos.
-   **RF-LAND-007:** A Landing Page DEVE incluir elementos de credibilidade e confiança (depoimentos, estatísticas, badges de segurança).
    -   _Processo:_ Seções com depoimentos de usuários, estatísticas de sucesso, indicadores de segurança/privacidade.
    -   _Output:_ Aumento da confiança e redução de objeções para conversão.

---
**Módulo: Autenticação e Gerenciamento de Conta** `RF-AUTH`
---
-   **RF-AUTH-001:** O sistema DEVE permitir que novos usuários se cadastrem fornecendo Email e Senha.
    -   **RF-AUTH-001.1 (Sub-Requisito):** O sistema DEVE validar o formato do email e garantir sua unicidade na base de dados.
    -   **RF-AUTH-001.2 (Sub-Requisito):** A senha definida pelo usuário DEVE atender a critérios de complexidade (mínimo de 12 caracteres, contendo letras maiúsculas, minúsculas, números e símbolos).
    -   **RF-AUTH-001.3 (Sub-Requisito):** O sistema DEVE utilizar hashing seguro (ex: Argon2id) para o armazenamento das senhas.
    -   **RF-AUTH-001.4 (Sub-Requisito):** Após o cadastro inicial, o sistema DEVE enviar um email de confirmação para o endereço fornecido.
    -   _Processo: _ Criação de registro no Supabase Auth. Envio de email de confirmação.
    -   _Output: _ Conta criada com status "não confirmado". Mensagem de sucesso.
    -   _Output: _ Conta criada com status "não confirmado". Mensagem de sucesso.
-   **RF-AUTH-002:** O sistema DEVE exigir confirmação de email para ativar a conta.
    -   _Processo: _ Link único e de tempo limitado no email. Atualização do status do usuário para "confirmado" ao clicar.
    -   _Output: _ Acesso pleno às funcionalidades.
-   **RF-AUTH-003:** O sistema DEVE permitir login com Email e Senha.
    -   **RF-AUTH-003.1 (Sub-Requisito):** O sistema DEVE verificar as credenciais fornecidas (email e senha) contra os registros armazenados.
    -   **RF-AUTH-003.2 (Sub-Requisito):** O sistema DEVE implementar mecanismos de proteção contra ataques de força bruta (ex: rate limiting, CAPTCHA após tentativas falhas).
    -   _Processo: _ Verificação de credenciais. Proteção contra brute-force (rate limiting, CAPTCHA).
    -   _Output: _ Sessão autenticada (JWT).
-   **RF-AUTH-004:** O sistema DEVE permitir que usuários se autentiquem utilizando suas contas Google (OAuth 2.0).
    -   _Processo:_ Integração com o sistema de autenticação do Google. Solicitação de permissões mínimas necessárias (email, nome). Criação/vinculação de conta no Recoloca.ai.
    -   _Output:_ Sessão autenticada (JWT).
-   **RF-AUTH-004.1 (Pós-MVP):** O sistema DEVE oferecer Autenticação Multifator (MFA) via TOTP.
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
-   **RF-AUTH-011:** O sistema DEVE permitir ao usuário visualizar o status da sua assinatura (plano atual, data de início, próxima cobrança).
    -   **RF-AUTH-011.1 (Sub-Requisito):** O sistema DEVE redirecionar o usuário para o portal do cliente Stripe para gerenciamento de detalhes de pagamento, histórico de faturas, upgrade, downgrade ou cancelamento da assinatura.
    -   _Processo:_ Integração com Stripe Customer Portal.
    -   _Output:_ Acesso seguro ao portal de gerenciamento de assinaturas do Stripe.
-   **RF-AUTH-012:** O sistema DEVE permitir ao usuário excluir sua conta e dados (conforme LGPD).

---
**Módulo: Kanban (Cockpit de Candidaturas)** `RF-KAN`
---
-   **RF-KAN-001:** O sistema DEVE permitir ao usuário gerenciar cartões de vagas no Kanban.
    -   **RF-KAN-001.1 (Sub-Requisito):** O sistema DEVE permitir a criação de novos cartões de vagas, seja manualmente ou através do processo de importação (RF-IMP-001).
    -   **RF-KAN-001.2 (Sub-Requisito):** O sistema DEVE permitir a visualização dos detalhes de um cartão de vaga.
    -   **RF-KAN-001.3 (Sub-Requisito):** O sistema DEVE permitir a edição dos campos de um cartão de vaga existente.
    -   **RF-KAN-001.4 (Sub-Requisito):** O sistema DEVE permitir a exclusão de cartões de vagas.
    -   **RF-KAN-001.5 (Sub-Requisito):** O sistema DEVE permitir mover cartões entre as colunas do Kanban via drag-and-drop.
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
-   **RF-CV-001:** O sistema DEVE permitir o upload e gerenciamento de currículos base em formato PDF.
    -   **RF-CV-001.1 (Sub-Requisito):** O sistema DEVE aceitar arquivos PDF com tamanho máximo de 10 MB.
    -   **RF-CV-001.2 (Sub-Requisito):** O sistema DEVE permitir que o usuário mantenha múltiplos currículos base, idealmente um para cada idioma principal de candidatura (Português, Inglês, Espanhol no MVP).
    -   **RF-CV-001.3 (Sub-Requisito):** O sistema DEVE extrair o texto do PDF utilizando `pymupdf` como ferramenta primária e `Tesseract OCR` (com suporte a pt-BR, en, es) como fallback para PDFs baseados em imagem.
    -   **RF-CV-001.4 (Sub-Requisito):** O sistema DEVE utilizar um LLM para realizar a categorização semântica das seções do currículo extraído (ex: Contato, Resumo Profissional, Experiência Laboral, Educação, Habilidades, Idiomas, Certificações).
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
-   **RF-CV-008 (Tier Gratuito - Contagem):** Limite de **3 "Otimizações Completas" por mês** (análise IA + score + sugestões + range salarial).

--- 
**Módulo: Pagamentos e Assinaturas (Integração Stripe)** `RF-PAY`
---
-   **RF-PAY-001:** O sistema DEVE integrar-se com o Stripe para processar pagamentos de assinaturas.
    -   _Processo:_ Utilizar Stripe Checkout para a página de pagamento.
    -   _Output:_ Pagamento processado e status da assinatura atualizado no Recoloca.ai.
-   **RF-PAY-002:** O sistema DEVE permitir que o usuário escolha um plano pago e seja redirecionado para o Stripe Checkout para concluir a assinatura.
    -   _Processo:_ Seleção de plano na interface do Recoloca.ai, criação de uma sessão de checkout no Stripe, redirecionamento do usuário.
    -   _Output:_ Usuário completa o pagamento no ambiente seguro do Stripe.
-   **RF-PAY-003:** O sistema DEVE lidar com webhooks do Stripe para atualizar o status das assinaturas.
    -   _Processo:_ Configurar um endpoint seguro para receber eventos do Stripe (ex: `invoice.payment_succeeded`, `customer.subscription.deleted`, `customer.subscription.updated`). Validar a assinatura do webhook.
    -   _Output:_ Atualização do status da assinatura do usuário no banco de dados do Recoloca.ai (Supabase) em tempo real.
-   **RF-PAY-004:** O sistema DEVE redirecionar o usuário para o Stripe Customer Portal para gerenciamento da assinatura (atualizar método de pagamento, ver faturas, cancelar assinatura).
    -   _Processo:_ Gerar um link seguro para o portal do cliente Stripe a partir da interface do Recoloca.ai.
    -   _Output:_ Acesso do usuário ao portal do Stripe para autogerenciamento da assinatura.
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

---
**Módulo: Sistema de Notificações** `RF-NOTIF`
---
-   **RF-NOTIF-001:** O sistema DEVE implementar notificações in-app para eventos importantes.
    -   _Processo:_ Gerar notificações para eventos como: status de vaga alterado, lembretes de follow-up, sugestões do Coach IA, atualizações de assinatura.
    -   _Output:_ Centro de notificações na interface com indicador de não-lidas.
-   **RF-NOTIF-002:** O sistema DEVE permitir configuração granular de preferências de notificação.
    -   _Processo:_ Interface para ativar/desativar categorias específicas de notificações.
    -   _Output:_ Experiência personalizada de notificações.
-   **RF-NOTIF-003:** O sistema DEVE enviar notificações por email para eventos críticos.
    -   _Processo:_ Enviar emails para eventos como: confirmação de conta, alteração de senha, renovação/cancelamento de assinatura, inatividade prolongada.
    -   _Output:_ Emails formatados profissionalmente com links de ação quando aplicável.
-   **RF-NOTIF-004 (Pós-MVP):** O sistema DEVE suportar notificações push via PWA para usuários que optarem.
    -   _Processo:_ Solicitar permissão. Enviar notificações push via API Web Push.
    -   _Output:_ Notificações no desktop/mobile mesmo com o navegador fechado.

---
**Módulo: Analytics e Tracking** `RF-ANALYTICS`
---
-   **RF-ANALYTICS-001:** O sistema DEVE implementar tracking de eventos-chave para análise de produto.
    -   _Processo:_ Capturar eventos como: registro, login, criação de vaga, otimização de CV, interação com Coach IA, conversão para plano pago.
    -   _Output:_ Dados estruturados para análise de funil e comportamento.
-   **RF-ANALYTICS-002:** O sistema DEVE implementar tracking anônimo de uso de features para otimização de produto.
    -   _Processo:_ Capturar métricas agregadas de uso de funcionalidades, tempo em tela, taxas de conclusão de fluxos.
    -   _Output:_ Insights para melhoria contínua da UX.
-   **RF-ANALYTICS-003:** O sistema DEVE fornecer ao usuário transparência sobre dados coletados e opção de opt-out de analytics não-essenciais.
    -   _Processo:_ Página de configurações de privacidade com controles granulares.
    -   _Output:_ Conformidade com LGPD e transparência com usuário.

---
**Módulo: Backup e Exportação de Dados** `RF-DATA`
---
-   **RF-DATA-001:** O sistema DEVE permitir ao usuário exportar seus dados em formato estruturado.
    -   _Processo:_ Gerar arquivo JSON/CSV com dados do usuário: perfil, vagas, currículos, histórico de interações.
    -   _Output:_ Arquivo de download com dados estruturados.
-   **RF-DATA-002:** O sistema DEVE permitir backup e restore de configurações do Kanban.
    -   _Processo:_ Opção para salvar estado atual do Kanban e restaurar posteriormente.
    -   _Output:_ Proteção contra perda acidental de organização.
-   **RF-DATA-003 (Tier Pago):** O sistema DEVE realizar backups automáticos incrementais do Kanban do usuário.
    -   _Processo:_ Salvar snapshots periódicos (diários) com histórico de 30 dias.
    -   _Output:_ Capacidade de restaurar estados anteriores do Kanban.

## 4. Requisitos Não Funcionais (RNF)

Os seguintes RNF são aplicáveis a todo o sistema, salvo indicação contrária. Os IDs são prefixados com `RNF-[CATEGORIA]-[NÚMERO]`.

--- 
**Categoria: Desempenho e Core Web Vitals** `RNF-PER`
---
-   **RNF-PER-001:** A análise de currículo e geração de score de adequação (RF-CV-003) DEVE ser concluída em até **15 segundos** para 90% das requisições.
-   **RNF-PER-002:** As respostas do Coach IA (RF-COACH-001) DEVEM ser apresentadas em até **3-5 segundos** para 90% das interações.
-   **RNF-PER-003:** O carregamento inicial da PWA DEVE ocorrer em até **5 segundos** em conexões de banda larga (>=10Mbps) e até **10 segundos** em conexões 3G rápidas.
-   **RNF-PER-004:** As transições de página e interações comuns na UI (ex: abrir modal, mover card no Kanban) DEVEM responder em menos de **500ms**.
-   **RNF-PER-005:** A PWA DEVE atender aos Core Web Vitals do Google (LCP <2.5s, FID <100ms, CLS <0.1) para garantir boa experiência do usuário e SEO.
-   **RNF-PER-006:** O sistema DEVE implementar rate limiting para proteger APIs contra uso excessivo.
    -   Tier Gratuito: Máximo de 100 requisições/hora para APIs de IA.
    -   Tier Pago: Máximo de 500 requisições/hora para APIs de IA.
    -   Geral: Máximo de 60 requisições/minuto para APIs de CRUD.

--- 
**Categoria: Segurança** `RNF-SEC`
---
-   **RNF-SEC-001:** Todas as senhas de usuário DEVEM ser armazenadas usando hashing forte e salt (ex: Argon2id via Supabase Auth).
-   **RNF-SEC-002:** A comunicação entre o frontend (PWA), backend (FastAPI) e serviços externos (Supabase, Gemini, Stripe) DEVE ser feita exclusivamente sobre HTTPS/TLS.
-   **RNF-SEC-003:** O sistema DEVE implementar proteção contra vulnerabilidades comuns da OWASP Top 10 (ex: XSS, SQL Injection, CSRF).
-   **RNF-SEC-004:** Os JWTs utilizados para autenticação DEVEM ter tempo de expiração curto e mecanismo de refresh seguro.
-   **RNF-SEC-005:** O acesso aos dados do usuário no banco de dados (Supabase) DEVE ser controlado por Row-Level Security (RLS) para garantir que um usuário só possa acessar seus próprios dados.
-   **RNF-SEC-006:** Chaves de API e outros segredos DEVEM ser gerenciados de forma segura (ex: variáveis de ambiente, cofres de segredos) e NUNCA hardcoded no código-fonte.
-   **RNF-SEC-007:** O sistema DEVE estar em conformidade com a LGPD, incluindo mecanismos para consentimento, acesso, retificação e exclusão de dados pessoais.
-   **RNF-SEC-008 (Stripe):** A integração com o Stripe DEVE seguir as melhores práticas de segurança recomendadas pelo Stripe, incluindo o uso de Stripe.js para coleta de dados de pagamento (evitando que dados sensíveis de cartão transitem pelo servidor do Recoloca.ai) e validação de webhooks.
-   **RNF-SEC-009 (Stripe):** NENHUM dado sensível de cartão de crédito (número completo, CVV) DEVE ser armazenado nos servidores ou banco de dados do Recoloca.ai.
-   **RNF-SEC-010:** O sistema DEVE implementar logs de auditoria para ações críticas.
    -   Registrar eventos como: login, alterações de perfil, operações de pagamento, exclusão de dados.
    -   Logs devem incluir timestamp, usuário, ação, IP e resultado.

--- 
**Categoria: Usabilidade** `RNF-USA`
---
-   **RNF-USA-001:** A interface do usuário DEVE ser intuitiva e fácil de aprender, mesmo para usuários com pouca familiaridade com ferramentas similares.
-   **RNF-USA-002:** O sistema DEVE fornecer feedback claro ao usuário sobre o resultado de suas ações (sucesso, erro, processamento).
-   **RNF-USA-003:** A PWA DEVE seguir as diretrizes de acessibilidade WCAG 2.1 Nível AA.
-   **RNF-USA-004:** O design DEVE ser consistente em todas as telas e funcionalidades, seguindo o [[STYLE_GUIDE]].

--- 
**Categoria: Confiabilidade** `RNF-REL`
---
-   **RNF-REL-001:** O sistema DEVE ter uma disponibilidade de **99.5%** (excluindo janelas de manutenção planejadas).
-   **RNF-REL-002:** O sistema DEVE implementar logging detalhado de erros e eventos importantes para facilitar o diagnóstico e a depuração.
-   **RNF-REL-003:** O sistema DEVE ter mecanismos de monitoramento para identificar proativamente falhas e degradação de performance.
-   **RNF-REL-004:** Em caso de falha na comunicação com APIs externas (Gemini, Stripe), o sistema DEVE lidar graciosamente com o erro, informando o usuário e permitindo nova tentativa quando aplicável.
-   **RNF-REL-005 (Stripe):** O processamento de webhooks do Stripe DEVE ser idempotente para evitar duplicidade de ações em caso de reenvios.
-   **RNF-REL-006:** O sistema DEVE implementar estratégia de backup e disaster recovery.
    -   Backups diários completos do banco de dados com retenção de 30 dias.
    -   Backups incrementais a cada 6 horas.
    -   Tempo máximo de recuperação (RTO) de 4 horas.
    -   Ponto de recuperação (RPO) máximo de 6 horas.

--- 
**Categoria: Manutenibilidade** `RNF-MAINT`
---
-   **RNF-MAINT-001:** O código-fonte DEVE ser bem documentado (comentários, docstrings) e seguir os padrões de estilo definidos para cada linguagem (PEP 8 para Python, Effective Dart para Flutter).
-   **RNF-MAINT-002:** A arquitetura DEVE ser modular para facilitar a evolução e a correção de bugs.
-   **RNF-MAINT-003:** A infraestrutura DEVE ser gerenciada como código (IaC) sempre que possível (ex: configurações de deploy no Vercel/Render).

--- 
**Categoria: IA (Específico para funcionalidades de IA)** `RNF-AI`
---
-   **RNF-AI-001 (Precisão):** As sugestões de otimização de CV (RF-CV-004) e o score de adequação (RF-CV-003) DEVEM ser relevantes e úteis para o usuário em pelo menos 75% dos casos, com base em avaliações qualitativas e feedback.
-   **RNF-AI-002 (Engenharia de Prompt):** Os prompts para os LLMs DEVEM ser versionados e refinados continuamente para melhorar a qualidade das respostas.
-   **RNF-AI-003 (Mitigação de Bias):** Esforços DEVEM ser feitos para identificar e mitigar vieses nos outputs da IA, especialmente em relação a gênero, raça ou idade, através de prompts cuidadosamente elaborados e, se necessário, pós-processamento.
-   **RNF-AI-004 (Consistência):** O AI Coach (RF-COACH-001) DEVE manter uma persona consistente em suas interações.
-   **RNF-AI-005 (Explicabilidade):** Sempre que possível, as sugestões da IA DEVEM vir acompanhadas de uma breve justificativa ou lógica por trás da recomendação.
-   **RNF-AI-006 (Governança e Ética):** O uso da IA DEVE seguir princípios éticos, respeitando a privacidade do usuário e a transparência sobre as capacidades e limitações da IA. O usuário DEVE ser informado que as sugestões da IA são para auxílio e não substituem o julgamento profissional.

--- 
**Categoria: Internacionalização e Localização** `RNF-I18N`
---
-   **RNF-I18N-001:** A interface do usuário (PWA) DEVE ser primariamente em Português do Brasil (pt-BR) no MVP.
-   **RNF-I18N-002:** O sistema DEVE ser capaz de processar e armazenar dados (currículos, descrições de vagas) em Português, Inglês e Espanhol.
-   **RNF-I18N-003:** A arquitetura DEVE facilitar a adição de novos idiomas para a interface no futuro.

--- 
**Categoria: Escalabilidade e Métricas de Negócio** `RNF-ESC`
---
-   **RNF-ESC-001:** A arquitetura DEVE ser projetada para suportar um crescimento de até **1.000 usuários ativos diários** no primeiro ano sem degradação significativa de performance, utilizando os recursos de escalabilidade do Supabase e dos serviços de hospedagem (Vercel/Render).
-   **RNF-ESC-002:** O backend (FastAPI) DEVE ser stateless para facilitar a escalabilidade horizontal.
-   **RNF-ESC-003:** O sistema DEVE ser capaz de processar até **100 otimizações de CV simultâneas** sem degradação de performance.
-   **RNF-ESC-004:** O sistema DEVE suportar **crescimento de 15% MoM** em usuários ativos conforme métricas definidas em [[METRICAS_SUCESSO_BASE_MERCADO]].

--- 
**Categoria: Compliance Legal** `RNF-LEGAL`
---
-   **RNF-LEGAL-001:** O sistema DEVE estar em conformidade com a LGPD (Lei Geral de Proteção de Dados).
    -   Implementar mecanismos de consentimento explícito para coleta de dados.
    -   Permitir acesso, correção e exclusão de dados pessoais pelo usuário.
    -   Documentar finalidade de uso de cada dado pessoal coletado.
-   **RNF-LEGAL-002:** O sistema DEVE implementar políticas claras de privacidade e termos de uso.
    -   Linguagem simples e acessível.
    -   Versões em português e inglês.
    -   Histórico de versões disponível.
-   **RNF-LEGAL-003:** O sistema DEVE implementar mecanismos de gestão de consentimento.
    -   Registro de consentimentos obtidos com timestamp.
    -   Interface para gerenciar preferências de privacidade.
    -   Processo para renovação de consentimento quando políticas forem atualizadas.

## 5. Outros Requisitos

### 5.1. Requisitos de Interface Externa
-   **REF-EXT-001:** Integração com API do Google Gemini (Pro e Flash) para funcionalidades de IA.
-   **REF-EXT-002:** Integração com Supabase para autenticação, banco de dados (PostgreSQL) e armazenamento de arquivos (Storage).
-   **REF-EXT-003:** Integração com Stripe para processamento de pagamentos e gerenciamento de assinaturas.

### 5.2. Requisitos de Documentação
-   **REF-DOC-001:** Toda a documentação do projeto (ERS, HLD, LLDs, ADRs, Guias) DEVE ser mantida em formato Markdown no repositório Git, seguindo a estrutura definida no [[PLANO_MESTRE_RECOLOCA_AI]].
-   **REF-DOC-002:** A documentação DEVE utilizar links internos do Obsidian para referenciar outros documentos do projeto (ex: [[PLANO_MESTRE_RECOLOCA_AI]]).
-   **REF-DOC-003:** A documentação DEVE ser considerada "viva", sendo atualizada continuamente conforme o projeto evolui.

## 6. Métricas de Sucesso e KPIs

### 6.1. Métricas de Product-Market Fit
- **Sean Ellis PMF Score:** Meta de 50% (benchmark >40% para PMF)
- **Day 7 Retention:** Meta de 20% (benchmark SaaS B2C: 10-25%)
- **Day 30 Retention:** Meta de 12% (benchmark SaaS B2C: 5-15%)
- **Month 3 Retention:** Meta de 70% (benchmark SaaS: 60-80%)

### 6.2. Métricas de Conversão e Monetização
- **Conversion Rate (Visitante → Cadastro):** Meta de 3% Ano 1, 4% Ano 2
- **Conversion Rate (Free → Paid):** Meta conforme benchmarks freemium
- **Organic Growth Rate:** Meta de 25% MoM (benchmark com PMF: >20%)
- **CAC Payback:** Meta <6 meses

### 6.3. Métricas de Engajamento
- **Core Feature Adoption (30 dias):**
  - Kanban Usage: 90% dos usuários ativos
  - CV Optimization: 70% dos usuários ativos
  - IA Coach: 60% dos usuários ativos
- **Vagas adicionadas por usuário/mês:** 8-12
- **Otimizações por usuário/mês:** 3-5
- **Taxa de aplicação das sugestões:** 70%+

### 6.4. Métricas de Satisfação
- **NPS:** Meta 50+ (Green Zone)
- **CSAT:** Meta 4.5/5
- **SUS Score:** Meta 75+

## 7. Priorização MoSCoW dos Requisitos

A classificação MoSCoW abaixo prioriza os requisitos para o desenvolvimento do MVP e evolução inicial do Recoloca.AI, baseando-se no valor entregue ao usuário, complexidade técnica, dependências e alinhamento estratégico com o "Momento AHA!" e diferencial competitivo definidos.

### 7.1. Must Have (Essencial para o MVP)

**Autenticação e Gerenciamento de Conta:**
- RF-AUTH-001: Cadastro com Email e Senha
- RF-AUTH-002: Confirmação de email
- RF-AUTH-003: Login com Email e Senha
- RF-AUTH-005: Redefinição de senha
- RF-AUTH-006: Onboarding inicial (Nome e CV Base)
- RF-AUTH-007: Diferenciação de tiers

**Kanban (Core do "Cockpit"):**
- RF-KAN-001: Gerenciamento de cartões de vagas
- RF-KAN-002: Colunas fixas do pipeline
- RF-KAN-006: Limite de vagas para tier gratuito

**Otimização de Currículo ("Momento AHA!"):**
- RF-CV-001: Upload e gerenciamento de CVs base
- RF-CV-002: Revisão e validação do conteúdo extraído
- RF-CV-003: Análise de adequação CV vs. vaga
- RF-CV-004: Sugestões de otimização
- RF-CV-006: Download do CV otimizado
- RF-CV-008: Limite de otimizações para tier gratuito

**Importação de Vagas:**
- RF-IMP-001: Importação via URL
- RF-IMP-002: Revisão e edição dos dados extraídos

**Pagamentos:**
- RF-PAY-001: Integração com Stripe
- RF-PAY-002: Checkout para assinatura
- RF-PAY-003: Webhooks para atualização de status

**Landing Page:**
- RF-LAND-001: Landing Page informativa
- RF-LAND-002: Seção Hero com CTA
- RF-LAND-003: CTA para registro
- RF-LAND-005: Informações sobre planos

**Requisitos Não Funcionais Essenciais:**
- RNF-SEC-001 a 009: Segurança (autenticação, HTTPS, RLS, LGPD)
- RNF-PER-001 a 003: Desempenho (tempos de resposta)
- RNF-REL-001 a 004: Confiabilidade básica
- RNF-USA-001 a 004: Usabilidade básica
- RNF-I18N-001 a 002: Suporte a PT-BR e processamento multilíngue
- RNF-LEGAL-001: Conformidade com LGPD

### 7.2. Should Have (Alta Prioridade após MVP Básico)

**Autenticação e Conta:**
- RF-AUTH-004: Login com Google OAuth
- RF-AUTH-008: Edição de perfil
- RF-AUTH-009: Gerenciamento de currículos base
- RF-AUTH-011: Visualização de status da assinatura
- RF-AUTH-012: Exclusão de conta (LGPD)

**Kanban e Métricas:**
- RF-KAN-003: Filtros e ordenação
- RF-KAN-004: Histórico de interações
- RF-KAN-005: Dashboard de métricas pessoais

**Coach IA:**
- RF-COACH-001: Interface de chatbot
- RF-COACH-003: Orientações sobre soft skills e mercado
- RF-COACH-005: Limite de interações para tier gratuito

**Otimização de CV:**
- RF-CV-005: Estimativa de range salarial
- RF-CV-007: Salvamento de versões otimizadas

**Notificações:**
- RF-NOTIF-001: Notificações in-app
- RF-NOTIF-003: Notificações por email para eventos críticos

**Analytics:**
- RF-ANALYTICS-001: Tracking de eventos-chave
- RF-ANALYTICS-003: Transparência e opt-out (LGPD)

**Requisitos Não Funcionais:**
- RNF-AI-001 a 006: Qualidade e ética da IA
- RNF-PER-004 a 005: Core Web Vitals
- RNF-MAINT-001 a 003: Manutenibilidade
- RNF-LEGAL-002 a 003: Políticas e consentimento

### 7.3. Could Have (Desejável, mas não crítico para o MVP)

**Coach IA Avançado:**
- RF-COACH-002: Proatividade do Coach IA
- RF-COACH-004: Uso de métricas para identificar gargalos
- RF-COACH-006: Recursos premium do Coach IA

**Experiência Aprimorada:**
- RF-LAND-004: Apresentação visual das funcionalidades
- RF-LAND-006: Responsividade otimizada
- RF-LAND-007: Elementos de credibilidade

**Gerenciamento de Dados:**
- RF-DATA-001: Exportação de dados
- RF-DATA-002: Backup e restore do Kanban

**Notificações Avançadas:**
- RF-NOTIF-002: Configuração granular de preferências

**Analytics Avançado:**
- RF-ANALYTICS-002: Tracking anônimo para otimização de produto

**Requisitos Não Funcionais:**
- RNF-PER-006: Rate limiting
- RNF-SEC-010: Logs de auditoria
- RNF-ESC-001 a 004: Escalabilidade avançada

### 7.4. Won't Have (Pós-MVP)

**Funcionalidades Avançadas:**
- RF-AUTH-004.1: MFA via TOTP
- RF-IMP-003: Extensão de navegador
- RF-DATA-003: Backups automáticos incrementais
- Simulações de entrevista interativas (mencionado em RF-COACH-006)

**Requisitos Não Funcionais:**
- RNF-REL-006: Estratégia avançada de backup e disaster recovery
- Integrações avançadas com ATS (mencionado no escopo pós-MVP)
- Web Clipper avançado (mencionado no escopo pós-MVP)
- Gerenciador de networking (mencionado no escopo pós-MVP)
- Biblioteca de recursos (mencionado no escopo pós-MVP)

## 8. Próximos Passos Críticos para Validação e Mitigação de Riscos

1.  **Validação da Arquitetura de Autenticação e RLS (FastAPI + Supabase):**
    *   _Ação:_ Desenvolver um protótipo mínimo para testar o fluxo de autenticação JWT entre FastAPI e Supabase, e a correta aplicação de RLS nas queries do FastAPI ao Supabase.
    *   _Risco Mitigado:_ Complexidade inesperada ou inviabilidade da integração de autenticação/autorização.
2.  **Estimativa de Custos de API (Gemini e Stripe) e Infraestrutura (Supabase, Vercel/Render):**
    *   _Ação:_ Modelar cenários de uso (baixo, médio, alto) para estimar os custos mensais com base nos preços atuais das APIs e serviços. Validar a sustentabilidade do modelo Freemium.
    *   _Risco Mitigado:_ Custos operacionais inviáveis ou superiores ao esperado.
3.  **Validação de Product-Market Fit (Protótipo e Early Adopters):**
    *   _Ação:_ Criar um protótipo navegável das principais jornadas do usuário e realizar testes com 10-15 early adopters do público-alvo, medindo Sean Ellis PMF Score e feedback qualitativo.
    *   _Risco Mitigado:_ Baixa adesão ou inadequação do produto ao mercado.
4.  **Prova de Conceito (PoC) do Parsing de PDF e Extração Semântica:**
    *   _Ação:_ Testar `pymupdf` e `Tesseract OCR` com uma variedade de layouts de CVs. Validar a capacidade do LLM (Gemini) de categorizar corretamente as seções do CV.
    *   _Risco Mitigado:_ Dificuldade em processar a diversidade de formatos de CVs, impactando a qualidade da otimização.
5.  **Definição Detalhada do Modelo de Dados no Supabase:**
    *   _Ação:_ Com base nos RFs, detalhar o esquema do banco de dados (tabelas, colunas, relacionamentos, tipos de dados, constraints) no Supabase.
    *   _Risco Mitigado:_ Inconsistências ou falta de dados necessários para as funcionalidades.

---

## Histórico de Versões

### v1.1 (Janeiro 2025) - Orquestração Inteligente e Specialized Intelligence
**Melhorias relacionadas à metodologia de orquestração inteligente:**
- ✅ **Métricas de "Specialized Intelligence"** adicionadas (eficiência de orquestração, qualidade do sistema RAG, satisfação/produtividade)
- ✅ **Critérios objetivos expandidos** para agentes "Production-Ready" em três tiers
- ✅ **Framework de medição** estabelecido para validação da qualidade dos agentes
- ✅ **Indicadores de produtividade** definidos para o desenvolvimento assistido por IA
- ✅ **Alinhamento metodológico** com TAP v1.1 e GUIA_AVANCADO v1.1
- ✅ **Consolidação da metodologia** de "Orquestração Inteligente" e "Specialized Intelligence"

### v1.0 (Junho 2025) - Alinhamento Estratégico e Métricas Refinadas
- Alinhamento com TAP v1.0 e cronograma Junho-Dezembro 2025
- Incorporação de métricas baseadas em benchmarks de mercado SaaS B2C
- Refinamento da visão "integrador e cockpit"
- Especificação detalhada de KPIs e métricas de sucesso
- Atualização de requisitos não funcionais com foco em escalabilidade
- Integração com [[METRICAS_SUCESSO_BASE_MERCADO]] v1.0

---

## Documentos Relacionados

### Gestão e Estratégia
- <mcfile name="TAP.md" path="docs/00_Gerenciamento_Projeto/TAP.md"></mcfile> - Termo de Abertura do Projeto
- <mcfile name="PLANO_MESTRE_RECOLOCA_AI.md" path="docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md"></mcfile> - Plano Mestre e Metodologia
- <mcfile name="GUIA_AVANCADO.md" path="docs/01_Guias_Centrais/GUIA_AVANCADO.md"></mcfile> - Metodologia de Orquestração Inteligente
- <mcfile name="KANBAN_Recoloca_AI.md" path="docs/00_Gerenciamento_Projeto/KANBAN_Recoloca_AI.md"></mcfile> - Gestão de Tarefas

### Documentos Técnicos
- <mcfile name="HLD.md" path="docs/03_Arquitetura_e_Design/HLD.md"></mcfile> - Arquitetura de Alto Nível
- <mcfile name="AGENTES_IA_MENTORES_OVERVIEW.md" path="docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md"></mcfile> - Visão Geral dos Agentes

### Perfis de Agentes
- <mcfolder name="Perfis" path="docs/04_Agentes_IA/Perfis"></mcfolder> - Perfis detalhados dos Agentes Mentores

---

**FIM DO DOCUMENTO ERS.md (v1.1) - RECOLOCA.AI**

---

**Próximas atualizações previstas:**
- Detalhamento de Histórias de Usuário (HU) e Critérios de Aceitação (AC)
- Especificação técnica detalhada da arquitetura (HLD/LLD)
- Refinamento de prompts para IA baseado em testes iniciais
- Validação de métricas com early adopters
- Implementação do dashboard de métricas de "Specialized Intelligence"

**Nota:** Este documento integra a metodologia de "Orquestração Inteligente" e "Specialized Intelligence" estabelecida no <mcfile name="GUIA_AVANCADO.md" path="docs/01_Guias_Centrais/GUIA_AVANCADO.md"></mcfile>, servindo como especificação técnica detalhada para o desenvolvimento assistido por Agentes de IA Mentores.