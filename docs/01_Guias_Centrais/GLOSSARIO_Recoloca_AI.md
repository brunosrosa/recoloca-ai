# GLOSSÁRIO DO PROJETO RECOLOCA.AI

Versão: 1.0

**Data de Criação**: 30 de maio de 2025

**Data de Última Atualização**: 30 de maio de 2025

**Baseado em**: [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.4), [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.2)
## 1. Introdução

Este glossário define os termos chave, acrônimos e conceitos específicos utilizados no contexto do projeto **Recoloca.ai** e na metodologia de "Desenvolvimento Solo Ágil Aumentado por IA". O objetivo é promover um entendimento comum e consistente entre o "Maestro" (desenvolvedor solo) e os Agentes de IA Mentores, facilitando a comunicação e a colaboração.

Este é um documento vivo e será atualizado continuamente à medida que o projeto evolui e novos termos são introduzidos.
## 2. Termos da Metodologia de Desenvolvimento com IA

- **Maestro:**
    
    - **Definição:** O desenvolvedor solo (Bruno S. Rosa) que lidera, orquestra e supervisiona o desenvolvimento do projeto Recoloca.ai, utilizando Agentes de IA como "Mentores" e assistentes. Atua como o principal tomador de decisões estratégicas, de design e de produto.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 2.2)
        
- **Agente de IA Mentor (ou Agente Mentor):**
    
    - **Definição:** Um agente de Inteligência Artificial especializado, configurado no Trae IDE, projetado para auxiliar o Maestro em tarefas específicas dentro do ciclo de vida de desenvolvimento de software (SDLC). Cada agente possui uma persona e um conjunto de habilidades definidas.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 4)
        
- **`@AgenteOrquestrador` (PM Mentor):**
    
    - **Definição:** O principal Agente de IA Mentor, que atua como um "Product Manager Mentor Sênior e Engenheiro de Prompt Especialista". Auxilia o Maestro a refinar o pensamento estratégico de Product Management, validar a estratégia de features, e a formular prompts claros e contextualmente ricos para os outros Agentes Mentores.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 3)
        
- **Desenvolvimento Solo Ágil Aumentado por IA:**
    
    - **Definição:** A metodologia de desenvolvimento adotada para o Recoloca.ai, onde o desenvolvedor solo ("Maestro") colabora intensivamente com uma orquestra de Agentes de IA Mentores para amplificar suas capacidades e construir o produto.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 2)
        
- **Documentação Viva:**
    
    - **Definição:** O conjunto de documentos do projeto (Plano Mestre, ERS, Guia Avançado, HLD, LLDs, etc.), mantidos no Obsidian, versionados com Git, e continuamente atualizados para refletir o estado atual do projeto. Serve como a principal fonte de verdade e contexto.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (Seção 5.2)
        
- **RAG (Retrieval Augmented Generation):**
    
    - **Definição:** Uma técnica de IA onde um modelo de linguagem amplo (LLM) tem sua capacidade de geração aumentada pela recuperação de informações relevantes de uma base de conhecimento externa (no caso do Recoloca.ai, a "Documentação Viva"). Isso melhora a precisão, reduz alucinações e fornece contexto específico do projeto aos Agentes de IA.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 5.1)
        
- **HITL (Human-in-the-Loop):**
    
    - **Definição:** O processo pelo qual o "Maestro" supervisiona, valida, corrige e refina o output gerado pelos Agentes de IA. É um componente essencial para garantir qualidade, segurança, alinhamento ético e aprendizado contínuo.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 6)
        
- **Engenharia de Prompt:**
    
    - **Definição:** A arte e ciência de projetar e refinar instruções (prompts) eficazes para guiar os modelos de linguagem ampla (LLMs) a gerar os outputs desejados.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (Seção 7.2)
        
## 3. Termos do Projeto Recoloca.ai

- **Recoloca.ai:**
    
    - **Definição:** O Micro-SaaS que é o objeto deste projeto, focado em auxiliar profissionais brasileiros no processo de recolocação profissional.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (Seção 1.1)
        
- **Cockpit do Candidato:**
    
    - **Definição:** A metáfora central para descrever a proposta de valor do Recoloca.ai – uma plataforma integrada que dá ao profissional controle e visibilidade sobre seu processo de recolocação.
        
    - **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (Seção 2.1)
        
- **Kanban (Recoloca.ai):**
    
    - **Definição:** A funcionalidade central de gerenciamento visual de candidaturas dentro do Recoloca.ai, onde os usuários organizam vagas em colunas que representam etapas do processo seletivo.
        
    - **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (RF-KAN)
        
- **Currículo Base Ativo:**
    
    - **Definição:** A versão principal e validada pelo usuário do seu currículo, armazenada no sistema Recoloca.ai, que serve como base para as otimizações de IA para vagas específicas. Pode haver um currículo base ativo por idioma suportado.
        
    - **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (RF-CV-002, RF-CV-003)
        
- **Score de Adequação (IA):**
    
    - **Definição:** Uma pontuação gerada pela IA do Recoloca.ai que indica o quão bem o "Currículo Base Ativo" do usuário se alinha com a descrição de uma vaga específica.
        
    - **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (RF-CV-003)
        
- **PM Mentor:**
    
    - **Definição:** Um papel estratégico assumido pelo `@AgenteOrquestrador`, focado em auxiliar o Maestro a aplicar consistentemente os princípios de Product Management, validar a estratégia de features e garantir o alinhamento com os objetivos do produto.
        
    - **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (Seção 3)
        
## 4. Termos Técnicos Gerais e Acrônimos

- **ADR (Architecture Decision Record):**
    
    - **Definição:** Um documento que captura uma decisão arquitetural importante, seu contexto e consequências.
        
    - **Localização:** [[docs/03_Arquitetura_e_Design/ADR/]]
        
- **API (Application Programming Interface):**
    
    - **Definição:** Uma interface que permite que diferentes sistemas de software se comuniquem.
        
- **ATS (Applicant Tracking System):**
    
    - **Definição:** Software usado por empresas para gerenciar o processo de recrutamento e filtrar currículos.
        
- **BaaS (Backend as a Service):**
    
    - **Definição:** Um modelo de serviço em nuvem que fornece aos desenvolvedores uma forma de conectar suas aplicações web e mobile a um backend na nuvem, gerenciando infraestrutura, bancos de dados, autenticação, etc. (Ex: Supabase).
        
- **CI/CD (Continuous Integration/Continuous Deployment ou Delivery):**
    
    - **Definição:** Práticas de DevOps para automatizar a construção, teste e deploy de software.
        
- **ERS (Especificação de Requisitos de Software):**
    
    - **Definição:** Documento que descreve o que o software deve fazer (requisitos funcionais) e quão bem (requisitos não funcionais). No projeto, é o [[docs/02_Requisitos/ERS.md]].
        
- **FAISS (Facebook AI Similarity Search):**
    
    - **Definição:** Uma biblioteca para busca eficiente de similaridade e agrupamento de vetores densos. Usada no Recoloca.ai para o Vector Store do RAG.
        
- **HLD (High-Level Design):**
    
    - **Definição:** Documento que descreve a arquitetura de alto nível do sistema, seus principais componentes e suas interações. No projeto, é o [[docs/03_Arquitetura_e_Design/HLD.md]].
        
- **HU/AC (História de Usuário / Critérios de Aceite):**
    
    - **Definição:** Artefatos ágeis para descrever funcionalidades da perspectiva do usuário e definir as condições para sua aceitação.
        
    - **Localização:** [[docs/02_Requisitos/HU_AC/]]
        
- **JWT (JSON Web Token):**
    
    - **Definição:** Um padrão aberto para criar tokens de acesso que afirmam um certo número de claims. Usado para autenticação.
        
- **LangChain:**
    
    - **Definição:** Um framework para desenvolver aplicações alimentadas por modelos de linguagem. Usado no Recoloca.ai para o sistema RAG.
        
- **LGPD (Lei Geral de Proteção de Dados Pessoais):**
    
    - **Definição:** A legislação brasileira de proteção de dados.
        
- **LLD (Low-Level Design):**
    
    - **Definição:** Documento que detalha o design interno de componentes específicos do software.
        
    - **Localização:** [[docs/03_Arquitetura_e_Design/LLD/]]
        
- **LLM (Large Language Model):**
    
    - **Definição:** Um modelo de IA treinado em grandes quantidades de texto, capaz de entender e gerar linguagem humana (Ex: Google Gemini).
        
- **MVP (Minimum Viable Product / Produto Mínimo Viável):**
    
    - **Definição:** A versão de um novo produto que permite a uma equipe coletar a quantidade máxima de aprendizado validado sobre os clientes com o mínimo esforço.
        
- **OpenRouter:**
    
    - **Definição:** Um gateway que permite acesso a múltiplos modelos de LLM de diferentes provedores através de uma API unificada.
        
- **PWA (Progressive Web Application):**
    
    - **Definição:** Uma aplicação web que utiliza tecnologias web modernas para oferecer uma experiência de usuário similar a de um aplicativo nativo.
        
- **RLS (Row-Level Security):**
    
    - **Definição:** Uma funcionalidade de banco de dados (como no PostgreSQL/Supabase) que permite controlar o acesso a linhas específicas em uma tabela com base nas características do usuário que está fazendo a consulta.
        
- **SaaS (Software as a Service):**
    
    - **Definição:** Um modelo de licenciamento e entrega de software no qual o software é licenciado por assinatura e hospedado centralmente.
        
- **SDLC (Software Development Life Cycle):**
    
    - **Definição:** O processo de planejamento, criação, teste e deploy de um sistema de informação.
        
- **Trae IDE:**
    
    - **Definição:** O Ambiente de Desenvolvimento Integrado com IA que será utilizado pelo Maestro para codificar e interagir com os Agentes de IA Mentores.
        
- **UVP (Unique Value Proposition / Proposta Única de Valor):**
    
    - **Definição:** Uma declaração clara que descreve o benefício de sua oferta, como você resolve as necessidades do seu cliente e o que o distingue da concorrência.
        
- **UX (User Experience / Experiência do Usuário):**
    
    - **Definição:** As percepções e respostas de uma pessoa que resultam do uso ou da antecipação do uso de um produto, sistema ou serviço.
        
- **UI (User Interface / Interface do Usuário):**
    
    - **Definição:** O meio pelo qual um usuário interage com uma máquina, sistema ou aplicação.
        
## FIM DO DOCUMENTO GLOSSARIO_Recoloca_AI.md (v1.0)