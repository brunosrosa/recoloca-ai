# Especificação de Requisitos de Software (ERS): Recoloca.ai

**Versão**: 0.3 (Revisada e Alinhada com o Plano Mestre v1.2)

**Data de Criação**: 26 de maio de 2025

**Data de atualização**: 28 de maio de 2025

**Baseado em**:

- `[[PLANO_MESTRE_RECOLOCA_AI.md]]` (v1.2)
    
- ERS Recoloca.ai (v0.2)
    
## 1. Introdução

### 1.1. Propósito

Este documento especifica os **requisitos funcionais** (RF) e **não funcionais** (RNF) para a Versão Mínima Viável (MVP) e a evolução inicial da plataforma **Recoloca.ai**. O Recoloca.ai é um Micro-SaaS projetado para auxiliar profissionais no Brasil no processo de recolocação profissional, combinando gerenciamento de candidaturas, otimização de currículos com Inteligência Artificial (IA) e um assistente de IA para coaching.

Este documento destina-se a:

- Guiar o desenvolvimento do produto pelo "Maestro" (desenvolvedor solo).
    
- Servir como a especificação primária para os **Agentes de IA Mentores** configurados no Trae IDE.
    
- Formar a base para o planejamento de testes e validação de qualidade.
    
- Ser um componente central da "Documentação Viva" do projeto, integrado ao sistema RAG.
    

### 1.2. Escopo do Produto (MVP e Evolução Inicial)

O escopo do produto está detalhado no `[[PLANO_MESTRE_RECOLOCA_AI.md#1.3. Objetivos e Escopo do MVP (Produto Mínimo Viável)]]`. Este ERS focará nos requisitos para atingir o MVP e as primeiras funcionalidades de evolução planejadas.

**Funcionalidades Centrais do MVP:**

1. **Gerenciamento de Candidaturas (Kanban):** Permitir que usuários salvem e organizem vagas de emprego com captura de dados enriquecida.
    
2. **Otimização de Currículo com IA:** Analisar descrições de vagas e currículos base (com parsing robusto e validação do usuário) para gerar versões customizadas, pontuações de aderência detalhadas e sugestões avançadas.
    
3. **Acompanhamento e "Coaching" com IA (Chatbot):** Oferecer dicas, suporte contextualizado e treino básico para entrevistas, com base de conhecimento curada e persona definida.
    

A plataforma será acessível via Web (PWA robusto construído com Flutter) e uma extensão de navegador para Chrome. O idioma principal será Português do Brasil.

**Funcionalidades Fora do Escopo do MVP (conforme `[[PLANO_MESTRE_RECOLOCA_AI.md]]`):**

- Integração direta com API do LinkedIn para importação de perfil ou aplicação.
    
- Análise avançada de perfil comportamental.
    
- Geração automática completa de cartas de apresentação (a IA pode auxiliar em trechos).
    
- Múltiplos idiomas (além do Português do Brasil).
    
- Funcionalidades de networking ou comunidade dentro da plataforma.
    
- Aplicativos nativos dedicados para Android/iOS (foco em PWA de alta qualidade).
    
- Matching proativo de vagas com IA.
    
- Dashboard de analytics de carreira muito avançado (além de métricas básicas de uso).
    
- Módulos de testes de competências (hard/soft skills).
    
- Gamificação complexa.
    
- Integração com agendas externas (Google Calendar, Outlook).
    
- Importação de perfil de outras plataformas além de PDF.
    

### 1.3. Definições, Acrônimos e Abreviações

- **IA:** Inteligência Artificial
    
- **LLM:** Large Language Model (Modelo de Linguagem Amplo)
    
- **PWA:** Progressive Web Application
    
- **ATS:** Applicant Tracking System (Sistema de Rastreamento de Candidatos)
    
- **MVP:** Minimum Viable Product (Produto Mínimo Viável)
    
- **PRD:** Product Requirements Document (Documento de Requisitos do Produto)
    
- **ERS/SRS:** Especificação de Requisitos de Software / Software Requirements Specification
    
- **UI:** User Interface (Interface do Usuário)
    
- **UX:** User Experience (Experiência do Usuário)
    
- **API:** Application Programming Interface (Interface de Programação de Aplicações)
    
- **LGPD:** Lei Geral de Proteção de Dados Pessoais
    
- **DB:** Banco de Dados
    
- **CRUD:** Create, Read, Update, Delete
    
- **MFA:** Multi-Factor Authentication (Autenticação Multifator)
    
- **OWASP:** Open Web Application Security Project
    
- **RAG:** Retrieval Augmented Generation
    
- **FCM:** Firebase Cloud Messaging
    
- **LCP:** Largest Contentful Paint
    
- **FID:** First Input Delay
    
- **INP:** Interaction to Next Paint
    
- **CLS:** Cumulative Layout Shift
    
- **Maestro:** O desenvolvedor solo do projeto.
    
- **Agente Mentor de IA:** Agente de IA especializado no Trae IDE.
    
- **Trae IDE:** Ambiente de Desenvolvimento Integrado com IA.
    
- **OpenRouter:** Gateway para acesso a múltiplos LLMs.
    
- **ADR:** Architecture Decision Record (Registro de Decisão Arquitetural)
    

### 1.4. Referências

- `[[01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]]` (v1.2)
    
- `[[01_Guias_Centrais/GUIA_AVANCADO_V1.md]]`
    
- Discussões de Refinamento e Sugestões Finais (documentadas internamente no Obsidian e no histórico Git).
    

### 1.5. Visão Geral do Documento

Este documento está organizado da seguinte forma: Seção 1 (Introdução), Seção 2 (Descrição Geral), Seção 3 (Requisitos Específicos), Seção 4 (Questões Abertas - minimizadas por refinamentos).

## 2. Descrição Geral

### 2.1. Perspectiva do Produto

O Recoloca.ai será um novo produto independente. Ele interagirá com APIs externas de LLMs (Google Gemini via OpenRouter) e com job boards (LinkedIn, Gupy) através de uma extensão de navegador. A arquitetura completa está detalhada no `[[03_Arquitetura_e_Design/HLD.md]]`.

### 2.2. Funções do Produto (Resumo)

1. **Gerenciamento Visual e Enriquecido de Candidaturas.**
    
2. **Otimização Profunda e Inteligente de Currículos com validação do usuário.**
    
3. **Suporte e Coaching por IA com Base de Conhecimento Curada.**
    

### 2.3. Características dos Usuários

- **Primário:** Profissionais brasileiros (foco inicial do MVP: profissionais de tecnologia) buscando nova oportunidade de emprego ou em transição de carreira.
    
- **Secundário:** Profissionais que desejam se manter preparados para futuras oportunidades.
    
- **Habilidades Técnicas Esperadas:** Familiaridade com navegação na web, uso de aplicativos online.
    

### 2.4. Restrições Gerais

- **Idioma:** Português do Brasil (MVP).
    
- **Navegador (Extensão):** Google Chrome (versão mais recente estável).
    
- **Plataforma (PWA):** Acessível em navegadores web modernos (desktops e mobile - iOS/Android) via Flutter Web.
    
- **Legislação:** Conformidade total com a LGPD.
    
- **Stack Tecnológica Decidida (conforme `[[PLANO_MESTRE_RECOLOCA_AI.md#4.1. Stack Tecnológica Principal]]`):**
    
    - Frontend (PWA): **Flutter (Dart)**.
        
    - Backend: **Python com FastAPI**.
        
    - Banco de Dados: **PostgreSQL (Via Supabase)**.
        
    - Autenticação & Storage de Arquivos: **Supabase**.
        
    - Extensão de Navegador: **JavaScript, HTML, CSS**.
        
    - IA LLM: APIs **Google Gemini Pro e Flash** (via OpenRouter).
        
    - Parsing de PDF: **`pymupdf` (Fitz)** primário; **`Tesseract OCR`** (com modelos pt-BR de alta qualidade) como fallback; **IA (LLM)** para categorização semântica do texto extraído.
        
    - Infraestrutura/Hospedagem: Frontend PWA em **Vercel**; Backend FastAPI em **Render**; Banco de Dados e Auth com **Supabase**.
        
- **Vector DB (para RAG):** **FAISS** para implementação local inicial.
    

### 2.5. Suposições e Dependências

- Suposições do PRD (demanda, disposição a pagar, maturidade IA, viabilidade da extensão) são mantidas.
    
- Dependência das APIs do Google Gemini (via OpenRouter), estrutura DOM dos job boards (para a extensão), e serviços de hospedagem (Vercel, Render, Supabase).
    
- Disponibilidade e funcionalidade do Trae IDE e OpenRouter.
    

## 3. Requisitos Específicos

### 3.1. Requisitos Funcionais

#### 3.1.1. Autenticação e Gerenciamento de Conta

- **RF-AUTH-001:** O sistema DEVE permitir que novos usuários se cadastrem fornecendo Email e Senha.
    
    - _Input:_ Email (formato de email válido, unicidade verificada), Senha (string).
        
    - _Processo:_ Validação dos dados de entrada. Senha DEVE ter no mínimo 12 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos (conforme recomendações OWASP). Senha DEVE ser verificada contra listas de senhas vazadas conhecidas (ex: integração com API "Have I Been Pwned" ou similar). Hashing seguro da senha com Argon2id antes da persistência. Criação de registro de usuário no Supabase Auth.
        
    - _Output:_ Conta de usuário criada com status "não confirmado". Envio de email de confirmação. Mensagem de sucesso para o usuário.
        
    - _Considerações para Agentes de IA:_ `@AgenteMentorDevFastAPI` deve implementar a lógica de validação e hashing. `@AgenteMentorSeguranca` deve revisar a implementação.
        
- **RF-AUTH-002:** O sistema DEVE exigir confirmação de email para ativar completamente a conta do usuário.
    
    - _Processo:_ Um email com um link de confirmação único e de tempo limitado (ex: 24 horas) DEVE ser enviado ao email cadastrado. Ao clicar no link, o status do usuário é atualizado para "confirmado".
        
    - _Output:_ Acesso pleno às funcionalidades da plataforma após confirmação.
        
- **RF-AUTH-003:** O sistema DEVE permitir que usuários existentes façam login usando Email e Senha.
    
    - _Input:_ Email, Senha.
        
    - _Processo:_ Verificação das credenciais contra os dados armazenados (comparando o hash da senha fornecida com o hash armazenado). O sistema DEVE implementar proteção contra ataques de brute-force (ex: rate limiting por IP e por conta, CAPTCHA após X falhas consecutivas).
        
    - _Output:_ Sessão de usuário autenticada (ex: retorno de token JWT). Acesso à plataforma.
        
- **RF-AUTH-004 (Pós-MVP):** O sistema DEVE oferecer Autenticação Multifator (MFA), preferencialmente TOTP (ex: Google Authenticator, Authy).
    
    - _Nota:_ Prioridade alta para implementação logo após o MVP.
        
- **RF-AUTH-005:** O sistema DEVE permitir que usuários redefinam sua senha caso a esqueçam.
    
    - _Processo:_ Usuário informa o email cadastrado. Se o email existir, um link seguro, único e de tempo limitado (ex: 15-30 minutos) para redefinição de senha é enviado ao email. Ao acessar o link, o usuário define uma nova senha, que DEVE seguir os mesmos critérios de complexidade de RF-AUTH-001. Uma notificação de segurança (email) DEVE ser enviada ao usuário após a alteração da senha.
        
    - _Output:_ Senha redefinida.
        
- **RF-AUTH-006:** No primeiro login bem-sucedido (após confirmação de email), o sistema DEVE guiar o usuário por um processo de onboarding inicial, solicitando que forneça seu Nome Completo e faça o upload do seu "Currículo Base" em formato PDF.
    
    - _Processo:_ Explicar a importância dessas informações para a funcionalidade completa da plataforma. O usuário DEVE poder pular esta etapa, mas será informado que as funcionalidades de otimização de currículo e coaching contextualizado pela IA permanecerão limitadas ou bloqueadas até que o currículo base seja fornecido.
        
    - _Output:_ Dados de perfil inicial e currículo base armazenados.
        
- **RF-AUTH-007:** O sistema DEVE diferenciar usuários do tier gratuito e premium, aplicando as respectivas limitações e benefícios de funcionalidade conforme definido para cada tier.
    
    - _Considerações para Agentes de IA:_ A lógica de verificação de tier deve ser implementada no backend e consultada antes de permitir acesso a funcionalidades pagas.
        

#### 3.1.2. Gerenciamento de Candidaturas (Kanban)

- **RF-KAN-001:** O sistema DEVE permitir a captura de informações de vagas de emprego através de uma extensão de navegador (Google Chrome) a partir de sites pré-definidos (MVP: LinkedIn, Gupy).
    
    - _Processo Extensão:_ `@AgenteMentorDevJS` implementará a extensão. A extensão, quando ativada em uma página de vaga compatível, DEVE tentar extrair automaticamente: Título da Vaga, Nome da Empresa, Link da Vaga, Descrição Completa da Vaga, **Localização** (Cidade/Estado/Remoto/Híbrido), **Modalidade** (Remoto/Híbrido/Presencial), **Data da Publicação da Vaga** (se disponível, caso contrário, data de captura), e **Nome da Plataforma de Origem**.
        
    - _Feedback e Edição:_ Se a extração automática de campos chave falhar ou for incompleta, o usuário DEVE ser claramente informado na interface da extensão e ter a opção de editar ou preencher manualmente os campos antes de salvar a vaga no Kanban do PWA.
        
    - _Output:_ Dados da vaga enviados ao backend e adicionados ao Kanban do usuário.
        
- **RF-KAN-002:** O sistema DEVE permitir que o usuário adicione manualmente vagas de emprego ao seu Kanban através da interface do PWA, preenchendo todos os campos listados em RF-KAN-001.
    
- **RF-KAN-003:** O Kanban DEVE possuir as seguintes colunas fixas e ordenadas para representar o fluxo de candidatura: "Salvas", "Aplicadas", "Entrevista Agendada", "Proposta Recebida", "Recusadas/Fechadas".
    
- **RF-KAN-004:** O sistema DEVE permitir que o usuário mova os cards (representando vagas) entre as colunas do Kanban utilizando uma interface de arrastar e soltar (drag-and-drop) fluida.
    
- **RF-KAN-005:** O sistema DEVE permitir que os cards de vagas sejam movidos para colunas anteriores no fluxo, se necessário (ex: de "Entrevista Agendada" de volta para "Aplicadas").
    
- **RF-KAN-006:** Cada card de vaga DEVE permitir a adição de notas textuais pelo usuário. As notas DEVEM suportar formatação **Markdown simples** (negrito, itálico, listas) e ter um limite de, no mínimo, 5000 caracteres.
    
- **RF-KAN-007:** O sistema DEVE permitir que o usuário adicione uma data de prazo (deadline) a cada card/vaga.
    
- **RF-KAN-008:** Os cards de vagas exibidos no Kanban DEVEM apresentar, no mínimo, as seguintes informações de forma clara: Título da Vaga, Nome da Empresa, Data de Publicação/Captura, Ícone representando a Origem da Vaga (LinkedIn, Gupy, Manual), Score de Aderência do Currículo (se >0 e calculado), e Prazo (se definido e não expirado).
    
- **RF-KAN-009:** O sistema DEVE fornecer funcionalidades de busca e filtro para as vagas no Kanban do usuário:
    
    - _Busca Textual:_ Busca textual avançada (case-insensitive, com suporte a correspondência parcial) nos campos: Título da Vaga, Nome da Empresa e Descrição Completa da Vaga.
        
    - _Filtros Combináveis:_ Os usuários DEVEM poder aplicar múltiplos filtros simultaneamente: por Coluna do Kanban, por Data de Adição (intervalo de datas), por Data de Prazo (intervalo de datas), por Origem da Vaga, e por Vagas com Score de Aderência (sim/não, ou faixa de score).
        
- **RF-KAN-010 (Tier Gratuito):** Usuários do tier gratuito terão um limite de **10 vagas ativas** (não arquivadas/fechadas) em seu Kanban. Ao atingir o limite, o sistema deve informar o usuário e impedir a adição de novas vagas, sugerindo um upgrade.
    
- **RF-KAN-011 (Tier Pago):** Usuários do tier pago terão vagas ativas **ilimitadas** em seu Kanban.
    

#### 3.1.3. Otimização de Currículo com Inteligência Artificial (IA)

- **RF-CV-001:** O sistema DEVE permitir que o usuário faça upload do seu "Currículo Base" no formato PDF, com um limite de tamanho de arquivo de **10MB**.
    
- **RF-CV-002:** O sistema DEVE realizar um parsing robusto do currículo em PDF para extrair seu conteúdo textual e estrutural.
    
    - _Processo:_
        
        1. Utilizar a biblioteca **`pymupdf` (Fitz)** como primeira tentativa para extração de texto e metadados de layout.
            
        2. Se a extração via `pymupdf` for insuficiente (ex: PDF baseado em imagem, texto ilegível, baixa quantidade de texto recuperado), o sistema DEVE recorrer à biblioteca **`Tesseract OCR`** (com modelos de linguagem pt-BR de alta qualidade) como fallback para extrair o texto.
            
        3. O texto bruto extraído (por qualquer um dos métodos) DEVE ser então processado por um **LLM (Google Gemini Pro)** para categorizar semanticamente os blocos de texto nas seções padrão de um currículo (conforme RF-CV-003).
            
    - _Considerações para Agentes de IA:_ `@AgenteMentorDevFastAPI` implementará essa lógica de parsing e orquestração. O prompt para o LLM de categorização deve ser cuidadosamente elaborado para lidar com a variabilidade de formatos de currículo.
        
- **RF-CV-003:** O sistema DEVE tentar extrair e/ou categorizar (via LLM) as seguintes seções e campos do currículo, que serão posteriormente validados e editados pelo usuário:
    
    - Dados de Contato (Nome Completo, Email, Telefone, Link do LinkedIn, Cidade/Estado).
        
    - Resumo/Objetivo Profissional.
        
    - Experiência Profissional (Cargo/Título, Nome da Empresa, Local (Cidade/País), Período (Data de Início - Data de Fim), Descrição detalhada das responsabilidades, conquistas e tecnologias utilizadas).
        
    - Formação Acadêmica (Nome do Curso/Grau, Nome da Instituição de Ensino, Local, Período (Data de Início - Data de Conclusão), principais projetos ou teses, se relevante).
        
    - Habilidades Técnicas (Hard Skills, Ferramentas, Linguagens de Programação, Nível de Proficiência se informado).
        
    - Habilidades Comportamentais (Soft Skills).
        
    - Idiomas (Língua, Nível de Proficiência).
        
    - Certificações e Cursos Complementares (Nome da Certificação/Curso, Instituição Emissora, Data de Emissão/Conclusão).
        
    - Projetos/Portfólio (Nome do Projeto, Descrição, Link se disponível, Tecnologias utilizadas).
        
- **RF-CV-004:** Após o parsing e a categorização inicial pela IA, o sistema DEVE apresentar o conteúdo extraído e estruturado de forma clara para **revisão, edição e validação obrigatória pelo usuário**. Esta etapa é crucial para garantir a precisão dos dados que alimentarão as análises subsequentes da IA. O usuário deve poder adicionar, remover ou modificar qualquer informação. O resultado desta etapa é o "Currículo Ativo".
    
- **RF-CV-005:** O sistema DEVE realizar uma análise por IA (LLM **Google Gemini Pro**) comparando a descrição de uma vaga (colada pelo usuário ou capturada pela extensão) com o "Currículo Ativo" validado pelo usuário.
    
    - _Input:_ Texto da descrição da vaga, dados estruturados do "Currículo Ativo".
        
    - _Processo IA:_ O LLM DEVE ser instruído a:
        
        1. Identificar palavras-chave semânticas, requisitos técnicos e comportamentais, habilidades obrigatórias e desejáveis, e o tom de voz da descrição da vaga.
            
        2. Comparar essas informações com os dados do "Currículo Ativo".
            
        3. Avaliar a congruência em múltiplos aspectos.
            
    - _Output IA (apresentado ao usuário de forma clara e acionável):_
        
        1. **Score de Congruência Geral (0-100%):** Uma pontuação geral indicando o quão bem o currículo se alinha com a vaga, baseada em fatores como: correspondência semântica de palavras-chave e termos técnicos, profundidade e relevância da experiência profissional, alinhamento de competências e habilidades, adequação de senioridade (tentativa), e presença de resultados quantificáveis no currículo.
            
        2. **Relatório Detalhado do Score:** Uma explicação textual dos principais pontos fortes do currículo em relação à vaga, os gaps identificados (habilidades ou experiências importantes mencionadas na vaga mas ausentes ou pouco destacadas no currículo) e áreas gerais de melhoria no currículo para aquela vaga específica.
            
        3. **Sub-Scores Visuais e Textuais (Opcional para MVP, desejável):** Pontuações ou indicadores visuais (ex: barras de progresso, cores) para seções principais do currículo (ex: cada Experiência Profissional, Habilidades Técnicas) mostrando seu alinhamento com a vaga.
            
        4. **Sugestões de Adaptações Contextualizadas:** Recomendações específicas de edições, adições ou reformulações no "Currículo Ativo" para melhorar seu alinhamento com a vaga. As sugestões devem focar tanto na otimização para Sistemas de Rastreamento de Candidatos (ATS) quanto no impacto para recrutadores humanos, com exemplos práticos.
            
- **RF-CV-006:** O sistema DEVE apresentar as sugestões de adaptação do currículo de forma interativa, idealmente mostrando o "antes e depois" de trechos específicos. O usuário DEVE poder aceitar, editar ou rejeitar cada sugestão individualmente. O sistema DEVE permitir que o usuário forneça input adicional (texto livre ou seleção de opções pré-definidas baseadas nos gaps identificados) para que a IA re-gere ou refine as sugestões.
    
- **RF-CV-007:** O sistema DEVE permitir que o usuário faça o download do currículo otimizado (após aplicar as sugestões) em formato PDF. O sistema DEVE fornecer um ou mais layouts de currículo padronizados, profissionais e testados para boa legibilidade por ATS.
    
- **RF-CV-008:** O sistema DEVE permitir o gerenciamento do "Currículo Ativo":
    
    - O usuário mantém um único "Currículo Ativo" principal, que é a versão mais atualizada e validada dos seus dados curriculares no sistema.
        
    - Ao realizar uma otimização para uma vaga específica, as alterações sugeridas e aceitas pelo usuário são aplicadas a uma versão de "rascunho" ou "otimizada para a vaga X".
        
    - Após baixar o PDF otimizado para uma vaga, o usuário DEVE ter a opção explícita de: "Salvar estas alterações no meu Currículo Ativo principal" ou "Descartar alterações (manter Currículo Ativo original)".
        
- **RF-CV-009 (Contagem de "Otimização" - Tier Gratuito):** Uma "otimização" é contada sempre que o sistema realiza uma análise completa pela IA (LLM Google Gemini Pro) entre o "Currículo Ativo" e uma Descrição de Vaga, resultando na apresentação de score e sugestões detalhadas. Re-gerações de sugestões dentro de uma mesma sessão de edição para a mesma combinação vaga/currículo (ex: dentro de 30 minutos) NÃO contam como uma nova otimização. Limite de **3 otimizações/mês** para usuários do tier gratuito.
    
- **RF-CV-010 (Tier Pago):** Usuários do tier pago terão otimizações "ilimitadas", sujeitas a uma política de uso justo (ex: **100 otimizações/mês**) para prevenir abusos.
    
- **RF-CV-011 (Tier Pago - Templates Avançados):** Usuários do tier pago terão acesso a um mínimo de **7-10 templates de currículo PDF distintos**, visualmente atraentes e testados para compatibilidade com ATS. DEVE haver opções de customização para esses templates, como: escolha de cores primárias (dentro de uma paleta curada), seleção de fontes (lista curada de fontes profissionais), reordenação de seções principais do currículo, e a capacidade de ligar/desligar seções opcionais (ex: Projetos, Habilidades Comportamentais).
    
- **RF-CV-012 (Tier Pago - Análises Mais Detalhadas):** Usuários do tier pago terão acesso a insights e sugestões mais aprofundados pela IA, incluindo:
    
    1. **Análise de Sentimento/Tom da Descrição da Vaga:** Para ajudar o usuário a adaptar o tom do seu currículo e carta de apresentação.
        
    2. **Benchmarking de Habilidades:** Comparar as habilidades do usuário com as N habilidades mais demandadas para o cargo/área (com base em dados de mercado, se possível, ou análise da vaga), sugerindo habilidades adjacentes ou em alta para desenvolvimento.
        
    3. **Identificação Explícita de Gaps de Habilidades/Experiência:** Apontar claramente quais habilidades ou tipos de experiência mencionados na vaga estão faltando ou pouco evidentes no currículo, com sugestões de como abordar esses gaps (ex: cursos, projetos pessoais, ou como reformular experiências existentes).
        
    4. **Otimização de Impacto/Resultados:** Sugestões específicas para reescrever os bullet points das experiências profissionais focando em resultados mensuráveis e conquistas, utilizando técnicas como STAR (Situação, Tarefa, Ação, Resultado) ou CAR (Contexto, Ação, Resultado).
        
    5. **Previsão de Perguntas de Entrevista Personalizadas:** Geração de 5-7 perguntas de entrevista (comportamentais e técnicas) personalizadas com base na descrição da vaga e no currículo do usuário, acompanhadas de dicas e estruturas sugeridas para as respostas.
        
    6. **Análise de Palavras-Chave da Indústria:** Sugerir termos técnicos e palavras-chave relevantes adicionais, específicos da indústria ou do cargo, que podem aumentar a visibilidade do currículo para ATS e recrutadores.
        

#### 3.1.4. Acompanhamento e "Coaching" com IA (Chatbot)

- **RF-CHAT-001:** O sistema DEVE fornecer uma interface de chatbot acessível e fácil de usar (ex: um balão flutuante no canto inferior direito da interface do PWA).
    
- **RF-CHAT-002 (Base de Conhecimento - RAG):** O chatbot DEVE utilizar um sistema RAG para acessar uma base de conhecimento extensa, curada e continuamente atualizada pelo Maestro. Esta base DEVE ser focada em informações relevantes para o mercado de trabalho brasileiro, incluindo: dicas para processos seletivos, etiqueta profissional, informações básicas sobre legislação trabalhista, técnicas de negociação salarial, como se preparar para diferentes tipos de entrevista, etc. O conteúdo será armazenado em `[[08_Knowledge_Base_RAG_Sources/]]`.
    
- **RF-CHAT-003 (Persona do LLM):** O LLM do chatbot (Google Gemini, via OpenRouter) DEVE operar com uma persona pré-definida e consistente: **Animado, inspirador, empático, prático e especialista em recolocação profissional no Brasil**. Esta persona será definida através de um "system prompt" detalhado e, se necessário, "few-shot prompting". O Maestro DEVE monitorar e ajustar continuamente a persona e os prompts para garantir a qualidade e adequação das interações.
    
- **RF-CHAT-004:** O chatbot DEVE ser capaz de fornecer dicas contextuais baseadas no status da(s) vaga(s) do usuário no Kanban (ex: se uma vaga está na coluna "Entrevista Agendada", o chatbot pode proativamente oferecer dicas para preparação de entrevista relacionadas àquela vaga).
    
- **RF-CHAT-005:** O sistema DEVE poder enviar notificações ao usuário dentro da plataforma PWA (e, se permitido, notificações push no PWA via FCM) para lembretes importantes (ex: prazos de vagas, follow-ups sugeridos) e para engajamento com o chatbot (ex: "Vi que você aplicou para X vagas hoje, quer algumas dicas para o próximo passo?").
    
- **RF-CHAT-006 (Tier Gratuito - Gemini Flash):** Usuários do tier gratuito terão um limite de **30 interações (mensagens de pergunta/resposta) por dia** com o chatbot. Funcionalidades avançadas como "Treino Aprofundado para Entrevistas" ou "Análise de Carreira Personalizada" NÃO estarão disponíveis. As respostas podem ter um delay ligeiramente maior (o usuário deve ser informado disso sutilmente, se aplicável) e as sugestões serão mais genéricas, baseadas primariamente no RAG.
    
- **RF-CHAT-007 (Tier Pago - Gemini Pro):** Usuários do tier pago terão acesso completo e interações "ilimitadas" (sujeito a política de uso justo) com o chatbot, utilizando o modelo Gemini Pro para respostas mais elaboradas e capacidades avançadas, incluindo:
    
    - **Treino Aprofundado para Entrevistas:** O chatbot atuará como um entrevistador, realizando simulações interativas. Fará perguntas comportamentais (incentivando respostas no formato STAR), perguntas técnicas (baseadas na área de atuação inferida do usuário ou em uma vaga específica que o usuário queira focar), e perguntas sobre o currículo. O usuário responderá por texto. A IA analisará as respostas em termos de adequação, clareza, uso de exemplos concretos, e (tentativamente) confiança inferida, fornecendo feedback detalhado, construtivo e acionável para cada resposta.
        

### 3.2. Requisitos Não Funcionais

#### 3.2.1. Desempenho (Core Web Vitals e IA)

- **RNF-PERF-001 (PWA - Core Web Vitals):**
    
    - Largest Contentful Paint (LCP): DEVE ser **≤ 2.0 segundos**.
        
    - First Input Delay (FID): DEVE ser **≤ 100 milissegundos** (ou Interaction to Next Paint (INP) DEVE ser **≤ 200 milissegundos**).
        
    - Cumulative Layout Shift (CLS): DEVE ser **≤ 0.1**.
        
- **RNF-PERF-002 (Otimização de Currículo - Tier Premium - P90):** O tempo total para análise de CV vs Vaga e apresentação das sugestões iniciais pela IA DEVE ser **≤ 15 segundos** para 90% das requisições.
    
- **RNF-PERF-003 (Chatbot - Tier Premium - P90):** O tempo de resposta do chatbot para uma consulta do usuário DEVE ser **≤ 3 segundos** para 90% das interações.
    
- **RNF-PERF-004 (Kanban Drag-and-Drop):** A resposta visual ao arrastar e soltar um card no Kanban DEVE ser percebida como instantânea (idealmente **< 100ms**, máximo **< 200ms**).
    

#### 3.2.2. Usabilidade (UX/UI)

- **RNF-USAB-001:** A interface do usuário (UI) DEVE ser **simples, intuitiva, e fácil de aprender e usar**, minimizando a carga cognitiva, especialmente considerando o público-alvo que pode estar sob estresse. O design DEVE seguir os princípios de UX estabelecidos no `[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]`. Consistência visual e de interação será garantida pelo uso do Flutter.
    
- **RNF-USAB-002 (PWA - Responsividade):** A PWA DEVE ser **totalmente responsiva**, adaptando-se de forma fluida a diferentes tamanhos de tela (desktops, tablets e smartphones iOS/Android) e orientações, sem perda de funcionalidade ou usabilidade.
    
- **RNF-USAB-003 (Feedback ao Usuário):** O sistema DEVE fornecer **feedback visual contínuo e apropriado** para as ações do usuário (ex: indicadores de carregamento, mensagens de sucesso/erro, transições suaves).
    
- **RNF-USAB-004 (Guia de Estilo):** Um **Guia de Estilo Abrangente e Documentado** (`[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]`) DEVE ser criado, mantido e rigorosamente seguido em todo o desenvolvimento da UI. Este guia incluirá: paleta de cores, tipografia, sistema de grid e espaçamento, iconografia, estilo e estados de botões e inputs, componentes básicos reutilizáveis, tom de voz e diretrizes de UX Writing, e princípios de acessibilidade (WCAG 2.1 Nível AA como meta).
    
- **RNF-USAB-005 (Acessibilidade):** A plataforma DEVE ser projetada e desenvolvida para ser acessível a pessoas com deficiência, seguindo as diretrizes WCAG 2.1 Nível AA como meta. Isso inclui contraste de cores adequado, navegação por teclado, texto alternativo para imagens, e semântica HTML correta.
    

#### 3.2.3. Confiabilidade

- **RNF-REL-001 (Disponibilidade):** A disponibilidade da plataforma Recoloca.ai DEVE ter uma meta de **99.9%** (excluindo janelas de manutenção planejadas e comunicadas).
    
- **RNF-REL-002 (Tratamento de Falhas):** O sistema DEVE tratar de forma elegante as falhas de comunicação com APIs externas (LLMs, Supabase, etc.), fornecendo feedback claro ao usuário sobre o problema e, quando apropriado, oferecendo a opção de tentar novamente a ação. Não deve haver perda de dados do usuário devido a essas falhas.
    
- **RNF-REL-003 (Monitoramento e Logging):**
    
    - Utilizar **Sentry.io** (ou Datadog) para monitoramento de erros de frontend e backend em tempo real.
        
    - Utilizar **Better Uptime** (ou UptimeRobot) para monitoramento da disponibilidade dos principais serviços.
        
    - Implementar logging centralizado e estruturado (ex: Logtail, ou logs no Supabase/Render) para operações críticas, erros e atividades importantes do sistema.
        
    - Monitorar ativamente o uso, latência e taxas de erro das APIs dos LLMs (via OpenRouter ou painel do provedor Gemini).
        
- **RNF-REL-004 (Suporte ao Usuário):**
    
    - Uma seção de **FAQ detalhada e buscável** DEVE estar disponível na plataforma.
        
    - O chatbot (`@AgenteChatbot`) DEVE ser capaz de fornecer suporte básico e direcionar para a FAQ.
        
    - Um canal de **email de suporte** (`suporte@recoloca.ai`) ou um sistema de tickets simples (ex: Zendesk Lite, Crisp, Tidio) DEVE ser implementado, com os seguintes SLAs de primeira resposta: Tier Premium - **12 horas úteis**; Tier Gratuito - **24-48 horas úteis**.
        

#### 3.2.4. Segurança (Conforme PRD 4.4 e Plano Mestre)

- **RNF-SEC-001 (LGPD):** Conformidade total com a Lei Geral de Proteção de Dados Pessoais (LGPD) do Brasil em todas as coletas, processamentos e armazenamentos de dados pessoais.
    
- **RNF-SEC-002 (Criptografia):** Todos os dados sensíveis (PII, conteúdo de currículos, senhas) DEVEM ser criptografados em trânsito (HTTPS/TLS 1.2+) e em repouso (ex: AES-256 para arquivos de currículo no Supabase Storage e para campos sensíveis no banco de dados PostgreSQL).
    
- **RNF-SEC-003 (Políticas Legais):** Uma Política de Privacidade e Termos de Uso claros, abrangentes, facilmente acessíveis e validados juridicamente DEVEM ser apresentados ao usuário durante o cadastro e estar disponíveis permanentemente na plataforma.
    
- **RNF-SEC-004 (Consentimento):** O sistema DEVE obter consentimento explícito e granular do usuário para a coleta e processamento de seus dados pessoais, especialmente para o conteúdo dos currículos e para as análises realizadas pela IA. O usuário DEVE poder gerenciar e revogar seu consentimento.
    
- **RNF-SEC-005 (Proteção OWASP):** O sistema DEVE ser desenvolvido com proteção contra as vulnerabilidades mais críticas do OWASP Top 10 (ex: Injection, Broken Authentication, XSS, CSRF, Security Misconfiguration, etc.) e do OWASP LLM Top 10 (ex: Prompt Injection, Data Leakage).
    
- **RNF-SEC-006 (Senhas):** As senhas dos usuários DEVEM ser armazenadas utilizando hashing forte e moderno, como Argon2id (preferencial) ou bcrypt.
    
- **RNF-SEC-007 (MFA):** A implementação de Autenticação Multifator (MFA) via TOTP (ex: Google Authenticator) é fortemente recomendada. Se não incluída no MVP, deve ser uma prioridade máxima pós-lançamento.
    
- **RNF-SEC-008 (Controle de Acesso):** Implementar controle de acesso baseado em roles (RBAC) para diferenciar funcionalidades e acesso a dados entre usuários (ex: tier gratuito vs. premium) e administradores do sistema.
    
- **RNF-SEC-009 (Segurança da Extensão):** A extensão de navegador DEVE ser desenvolvida seguindo as melhores práticas de segurança para extensões, minimizando permissões solicitadas e validando todas as comunicações com o backend.
    

#### 3.2.5. Manutenibilidade

- **RNF-MAINT-001 (Código):** O código-fonte (Flutter/Dart, Python/FastAPI, JavaScript) DEVE ser modular, bem organizado, seguindo os princípios de design (ex: SOLID onde aplicável), e extensivamente documentado (comentários, docstrings) para facilitar a compreensão, manutenção e evolução pelo Maestro e pelos Agentes de IA.
    
- **RNF-MAINT-002 (Stack Tecnológica):** As decisões de stack (Python/FastAPI, Flutter/Dart, Supabase) foram tomadas considerando a disponibilidade de talentos (para eventual colaboração futura), a robustez dos ecossistemas, a qualidade da documentação e o suporte da comunidade.
    
- **RNF-MAINT-003 (Configuração como Código):** Sempre que possível, a configuração da infraestrutura (ex: Render via `render.yaml`) e dos processos de CI/CD (ex: Pipedream workflows, GitHub Actions) DEVE ser gerenciada como código e versionada.
    

#### 3.2.6. Requisitos de IA Específicos

- **RNF-AI-001 (Engenharia de Prompt):** Um processo contínuo de desenvolvimento, teste e refinamento de prompts eficazes e robustos DEVE ser implementado para todas as funcionalidades de IA, com foco em resultados de alta qualidade em Português do Brasil. Os templates de prompts serão gerenciados em `[[05_Prompts/]]`.
    
- **RNF-AI-002 (Mitigação de Vieses e Ética):**
    
    1. Utilizar LLMs de provedores que demonstrem esforços em pesquisa e mitigação de vieses.
        
    2. Aplicar técnicas de Prompt Engineering explícitas para instruir os LLMs a evitar vieses de gênero, raça, idade, etc., e a focar em habilidades, experiências e qualificações objetivas.
        
    3. Realizar testes com uma gama diversificada de exemplos de currículos e descrições de vagas (se possível, com dados sintéticos ou anonimizados que representem diferentes perfis).
        
    4. Implementar auditoria humana regular (pelo Maestro) das sugestões e análises geradas pela IA, especialmente em áreas sensíveis.
        
    5. Fornecer um mecanismo claro para que os usuários reportem sugestões ou comportamentos da IA que considerem enviesados ou inadequados.
        
    6. Manter transparência com o usuário sobre o uso de IA, suas capacidades e limitações.
        
- **RNF-AI-003 (Precisão Parsing PDF + Categorização IA):**
    
    - Para PDFs textuais e bem estruturados, a taxa de extração de texto bruto pelas ferramentas de parsing (pymupdf) DEVE ser **> 98%**.
        
    - A taxa de sucesso da categorização semântica dos blocos de texto extraídos pela IA (LLM) nas seções corretas do currículo (conforme RF-CV-003) DEVE ser **> 90%** ANTES da validação do usuário. A etapa de **revisão e correção obrigatória pelo usuário (RF-CV-004)** é fundamental para alcançar a precisão final dos dados.
        
- **RNF-AI-004 (Consistência da Persona do Chatbot):** A persona do chatbot (RF-CHAT-003) DEVE ser mantida de forma consistente em todas as interações, evitando respostas que contradigam o tom ou o nível de expertise definidos.
    
- **RNF-AI-005 (Rastreabilidade e Explicabilidade - XAI):** Embora a explicabilidade total de LLMs seja um desafio, o sistema DEVE, sempre que possível, fornecer justificativas ou destacar as evidências (ex: trechos da vaga ou do currículo) que levaram a IA a uma determinada sugestão ou análise, especialmente no módulo de otimização de currículo.
    

#### 3.2.7. Documentação (Nova Seção)

- **RNF-DOC-001 (Manutenibilidade para RAG):** Toda a documentação do projeto (ERS, HLD, LLDs, ADRs, este Plano Mestre) DEVE ser escrita e mantida em Markdown, utilizando links internos (`[[Arquivo.md]]`) e uma estrutura clara de cabeçalhos para facilitar o processamento, indexação e recuperação eficiente pelo sistema RAG, fornecendo contexto preciso aos Agentes de IA.
    
- **RNF-DOC-002 (Atualização Contínua):** A documentação DEVE ser tratada como um artefato vivo e atualizada continuamente para refletir o estado atual do software, das decisões de design e dos processos. O `@AgenteMentorDocumentacao` auxiliará nesta tarefa.
    

### 3.3. Requisitos de Interface Externa

#### 3.3.1. Interface do Usuário (UI)

- **RI-UI-001:** A PWA DEVE ser desenvolvida em Flutter Web, aderindo estritamente ao `[[03_Arquitetura_e_Design/STYLE_GUIDE.md]]` para garantir consistência visual e de experiência do usuário.
    
- **RI-UI-002:** A extensão de navegador (JavaScript, HTML, CSS) DEVE ter uma interface de usuário minimalista, intuitiva e focada na tarefa de captura e edição rápida de informações de vagas.
    

#### 3.3.2. Interfaces de Software (API)

- **RI-API-001:** A interação com as APIs do Google Gemini (via OpenRouter) DEVE ser realizada de forma segura, utilizando HTTPS e gerenciamento seguro de chaves de API.
    
- **RI-API-002:** A comunicação entre a extensão de navegador e o backend Recoloca.ai DEVE ser realizada exclusivamente via HTTPS, com autenticação e validação adequadas das requisições.
    
- **RI-API-003 (API Interna):** A API backend do Recoloca.ai DEVE ser documentada usando o padrão OpenAPI 3.0 (arquivo `[[03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]`).
    

#### 3.3.3. Interfaces de Comunicação

- **RI-COMM-001 (Email Transacional):** Para emails transacionais (confirmação de conta, redefinição de senha, notificações importantes), o sistema DEVE utilizar um serviço de alta entregabilidade como **Postmark** ou **Amazon SES**. O Supabase Auth pode ser usado para emails básicos de autenticação, mas serviços dedicados são preferíveis para outros tipos de comunicação.
    
- **RI-COMM-002 (Notificações Push PWA):** Se implementadas, as notificações push para a PWA DEVEM utilizar **Firebase Cloud Messaging (FCM)** ou um serviço similar compatível com PWAs.
    

## 4. Questões Abertas e Pontos para Definição Futura

Com os refinamentos e o alinhamento com o `[[PLANO_MESTRE_RECOLOCA_AI.md]]`, a maioria das questões técnicas e funcionais para o MVP foram abordadas. As questões primariamente em aberto ou que requerem definição contínua são:

- **Estratégia de Precificação Detalhada do Tier Premium:** (Valores como R$ 19,90/semana ou R$ 59,90/mês necessitam de validação final com análise de custos completa, pesquisa de mercado aprofundada e testes A/B).
    
- **Roadmap de Benefícios Premium Adicionais:** (Além dos já definidos para evolução inicial, explorar continuamente novas funcionalidades de valor para o tier pago com base no feedback do usuário, análise competitiva e estratégia de negócio).
    
- **Pesquisa Contínua sobre ATS e Práticas de Recrutamento:** O funcionamento dos ATS e as tendências de recrutamento evoluem; a pesquisa e adaptação das sugestões de IA e da base de conhecimento do RAG DEVEM ser contínuas.
    
- **Estratégia de Marketing e Aquisição de Usuários Detalhada:** (A ser desenvolvida e refinada continuamente, possivelmente com auxílio de um `@AgenteMentorMarketing` futuro).
    
- **Mecanismos e Ferramentas para Coleta de Feedback de Satisfação (NPS/CSAT):** Escolha final de ferramentas (ex: Sprig, Hotjar, Delighted, Typeform) e implementação dos fluxos de coleta de feedback do usuário na plataforma.
    
- **Validação Jurídica Final dos Documentos:** A Política de Privacidade e os Termos de Uso DEVEM ser revisados e validados por um profissional jurídico especializado em LGPD e direito digital antes do lançamento.
    
- **Métricas de Sucesso Detalhadas (KPIs):** Definir KPIs específicos para o MVP e para as fases subsequentes de evolução do produto (ex: taxa de conversão para tier pago, taxa de retenção, engajamento com funcionalidades chave, NPS).