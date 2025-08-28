---
sticker: lucide//check
---
# GLOSSÁRIO DO PROJETO RECOLOCA. AI

**Versão:** 1.2 (Orquestração Inteligente e Specialized Intelligence)
**Data de Criação:** 30 de maio de 2025
**Data de Última Atualização:** Janeiro de 2025
**Baseado em:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v 1.5), [[docs/02_Requisitos/ERS.md]] (v 0.5), [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3)
## 1. Introdução

Este glossário define os termos chave, acrônimos e conceitos específicos utilizados no contexto do projeto **Recoloca. Ai** e na metodologia de "Desenvolvimento Solo Ágil Aumentado por IA". O objetivo é promover um entendimento comum e consistente entre o "Maestro" (desenvolvedor solo) e os Agentes de IA Mentores, facilitando a comunicação e a colaboração.

Este é um documento vivo e será atualizado continuamente à medida que o projeto evolui e novos termos são introduzidos.
## 2. Termos da Metodologia de Desenvolvimento com IA

-   **Maestro:**
    -   **Definição:** O desenvolvedor solo (Bruno S. Rosa) que lidera, orquestra e supervisiona o desenvolvimento do projeto Recoloca. Ai, utilizando Agentes de IA como "Mentores" e assistentes. Atua como o principal tomador de decisões estratégicas, de design e de produto.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 2.2)

-   **Agente de IA Mentor (ou Agente Mentor):**
    -   **Definição:** Um agente de Inteligência Artificial especializado, configurado no Trae IDE, projetado para auxiliar o Maestro em tarefas específicas dentro do ciclo de vida de desenvolvimento de software (SDLC). Cada agente possui uma persona e um conjunto de habilidades definidas.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 4)

-   **`@AgenteM_Orquestrador` (PM Mentor):**
    -   **Definição:** O principal Agente de IA Mentor, que atua como um "Product Manager (e Product Owner) Mentor Sênior e Engenheiro de Prompt Especialista". Auxilia o Maestro a refinar o pensamento estratégico de Product Management, validar a estratégia de features, e a formular prompts claros e contextualmente ricos para os outros Agentes Mentores.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 3)

-   **Desenvolvimento Solo Ágil Aumentado por IA:**
    -   **Definição:** A metodologia de desenvolvimento adotada para o Recoloca. Ai, onde o desenvolvedor solo ("Maestro") colabora intensivamente com uma orquestra de Agentes de IA Mentores para amplificar suas capacidades e construir o produto.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 2)

-   **Documentação Viva:**
    -   **Definição:** O conjunto de documentos do projeto (Plano Mestre, ERS, Guia Avançado, HLD, LLDs, etc.), mantidos no Obsidian, versionados com Git, e continuamente atualizados para refletir o estado atual do projeto. Serve como a principal fonte de verdade e contexto.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v 1.5, Seção 5.2)

-   **RAG (Retrieval Augmented Generation):**
    -   **Definição:** Uma técnica de IA onde um modelo de linguagem amplo (LLM) tem sua capacidade de geração aumentada pela recuperação de informações relevantes de uma base de conhecimento externa (no caso do Recoloca. Ai, a "Documentação Viva" e outros materiais curados). Isso melhora a precisão, reduz alucinações e fornece contexto específico do projeto aos Agentes de IA. No Recoloca. Ai, é implementado com LangChain, FAISS-GPU e o modelo de embedding `BAAI/bge-m3`.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 5.1), [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v 1.5, Seção 5.1)

-   **HITL (Human-in-the-Loop):**
    -   **Definição:** O processo pelo qual o "Maestro" supervisiona, valida, corrige e refina o output gerado pelos Agentes de IA. É um componente essencial para garantir qualidade, segurança, alinhamento ético e aprendizado contínuo.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 6)

-   **Engenharia de Prompt:**
    -   **Definição:** A arte e ciência de projetar e refinar instruções (prompts) eficazes para guiar os modelos de linguagem ampla (LLMs) a gerar os outputs desejados.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v 1.5, Seção 7.2), [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 5.4)
## 3. Termos do Projeto Recoloca. Ai

-   **Recoloca. Ai:**
    -   **Definição:** O Micro-SaaS que é o objeto deste projeto, focado em auxiliar profissionais brasileiros no processo de recolocação profissional.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v 1.5, Seção 1.1)

-   **Cockpit do Candidato:**
    -   **Definição:** A metáfora central para descrever a proposta de valor do Recoloca. Ai – uma plataforma integrada que dá ao profissional controle e visibilidade sobre seu processo de recolocação.
    -   **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (v 0.5, Seção 2.1)

-   **Kanban (Recoloca. Ai):**
    -   **Definição:** A funcionalidade central de gerenciamento visual de candidaturas dentro do Recoloca. Ai, onde os usuários organizam vagas em colunas que representam etapas do processo seletivo.
    -   **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (v 0.5, RF-KAN)

-   **Currículo Base Ativo:**
    -   **Definição:** A versão principal e validada pelo usuário do seu currículo, armazenada no sistema Recoloca. Ai, que serve como base para as otimizações de IA para vagas específicas. Pode haver um currículo base ativo por idioma suportado.
    -   **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (v 0.5, RF-CV-002, RF-CV-003)

-   **Score de Adequação (IA):**
    -   **Definição:** Uma pontuação gerada pela IA do Recoloca. Ai que indica o quão bem o "Currículo Base Ativo" do usuário se alinha com a descrição de uma vaga específica.
    -   **Referência Principal:** [[docs/02_Requisitos/ERS.md]] (v 0.5, RF-CV-003)

-   **PM Mentor:**
    -   **Definição:** Um papel estratégico assumido pelo `@AgenteM_Orquestrador`, focado em auxiliar o Maestro a aplicar consistentemente os princípios de Product Management, validar a estratégia de features e garantir o alinhamento com os objetivos do produto.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.3, Seção 3)

-   **Orquestração Inteligente:**
    -   **Definição:** Metodologia avançada de coordenação e gestão de múltiplos Agentes de IA Mentores, onde o `@AgenteM_Orquestrador` atua como maestro estratégico, otimizando a colaboração entre agentes especializados para maximizar a eficiência e qualidade das entregas do projeto.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.4), [[docs/01_Guias_Centrais/TAP.md]] (v 1.1)

-   **Specialized Intelligence:**
    -   **Definição:** Conceito que define a capacidade de cada Agente de IA Mentor de atuar como um especialista de alto nível em sua área específica (UX, Arquitetura, Desenvolvimento, etc.), combinando conhecimento técnico profundo com contexto específico do projeto através do sistema RAG.
    -   **Referência Principal:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v 2.4), [[docs/03_Arquitetura_e_Design/HLD.md]] (v 1.1)

-   **Agente Production-Ready:**
    -   **Definição:** Um Agente de IA Mentor que atende aos critérios objetivos de qualidade e performance estabelecidos, incluindo precisão ≥85%, tempo de resposta ≤30s, contextualização adequada via RAG, e autonomia operacional para tarefas de sua especialidade.
    -   **Referência Principal:** [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]] (v 3.1), [[docs/03_Arquitetura_e_Design/HLD.md]] (v 1.1)

-   **Métricas de Specialized Intelligence:**
    -   **Definição:** Conjunto de indicadores quantitativos e qualitativos para medir a eficácia da orquestração de agentes, incluindo: Eficiência de Orquestração (tempo de resolução, taxa de sucesso), Qualidade do Sistema RAG (precisão de recuperação, relevância contextual), e Satisfação/Produtividade (qualidade percebida, redução de retrabalho).
    -   **Referência Principal:** [[docs/03_Arquitetura_e_Design/HLD.md]] (v 1.1), [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]] (v 3.1)
## 4. Termos Técnicos Gerais e Acrônimos

-   **ADR (Architecture Decision Record):**
    -   **Definição:** Um documento que captura uma decisão arquitetural importante, seu contexto e consequências.
    -   **Localização:** [[docs/03_Arquitetura_e_Design/02_ADRs/]]

-   **API (Application Programming Interface):**
    -   **Definição:** Uma interface que permite que diferentes sistemas de software se comuniquem.

-   **ATS (Applicant Tracking System):**
    -   **Definição:** Software usado por empresas para gerenciar o processo de recrutamento e filtrar currículos.

-   **`BAAI/bge-m3`:**
    -   **Definição:** O modelo de embedding de texto escolhido para o projeto Recoloca. Ai. É um modelo multilíngue de alto desempenho usado para converter texto em vetores numéricos para o sistema RAG.
    -   **Referência:** [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v 1.5, Seção 5.1)

-   **BaaS (Backend as a Service):**
    -   **Definição:** Um modelo de serviço em nuvem que fornece aos desenvolvedores uma forma de conectar suas aplicações web e mobile a um backend na nuvem, gerenciando infraestrutura, bancos de dados, autenticação, etc. (Ex: Supabase).

-   **Chunking:**
    -   **Definição:** No contexto de RAG, é o processo de dividir documentos longos em pedaços menores (chunks) de texto. Isso é feito para que os embeddings possam ser gerados para cada chunk e para que apenas os chunks mais relevantes sejam passados para o LLM, respeitando os limites de contexto do modelo.

-   **CI/CD (Continuous Integration/Continuous Deployment ou Delivery):**
    -   **Definição:** Práticas de DevOps para automatizar a construção, teste e deploy de software.

-   **Conda:**
    -   **Definição:** Um sistema de gerenciamento de pacotes e ambientes de código aberto e multiplataforma. Utilizado no Recoloca. Ai para criar e gerenciar o ambiente Python e suas dependências complexas, como PyTorch com CUDA e FAISS-GPU.

-   **CUDA Toolkit:**
    -   **Definição:** Uma plataforma de computação paralela e modelo de programação criado pela NVIDIA. Permite que desenvolvedores usem GPUs NVIDIA para computação de propósito geral (GPGPU). Necessário para FAISS-GPU.

-   **cuDNN (CUDA Deep Neural Network library):**
    -   **Definição:** Uma biblioteca da NVIDIA que fornece primitivas aceleradas por GPU para redes neurais profundas. É uma dependência para frameworks de deep learning como o PyTorch ao rodar em GPUs NVIDIA.

-   **Embedding:**
    -   **Definição:** Uma representação vetorial de baixa dimensionalidade de dados de alta dimensionalidade, como texto. No RAG, embeddings são usados para representar semanticamente o texto dos documentos e das consultas dos usuários, permitindo a busca por similaridade.

-   **`environment.yml`:**
    -   **Definição:** Um arquivo de configuração usado pelo Conda para definir e recriar um ambiente Conda específico, listando os pacotes, suas versões e os canais de origem. Essencial para a reprodutibilidade do ambiente de desenvolvimento do Recoloca. Ai.
    -   **Localização:** [[rag_infra/environment.yml]] (proposta)

-   **ERS (Especificação de Requisitos de Software):**
    -   **Definição:** Documento que descreve o que o software deve fazer (requisitos funcionais) e quão bem (requisitos não funcionais). No projeto, é o [[docs/02_Requisitos/ERS.md]].

-   **FAISS-GPU (Facebook AI Similarity Search - GPU version):**
    -   **Definição:** Uma biblioteca para busca eficiente de similaridade e agrupamento de vetores densos, otimizada para rodar em GPUs NVIDIA (via CUDA). Usada no Recoloca. Ai para o Vector Store do sistema RAG.

-   **HLD (High-Level Design):**
    -   **Definição:** Documento que descreve a arquitetura de alto nível do sistema, seus principais componentes e suas interações. No projeto, é o [[docs/03_Arquitetura_e_Design/HLD.md]].

-   **HU/AC (História de Usuário / Critérios de Aceite):**
    -   **Definição:** Artefatos ágeis para descrever funcionalidades da perspectiva do usuário e definir as condições para sua aceitação.
    -   **Localização:** [[docs/02_Requisitos/HU_AC/]]

-   **JWT (JSON Web Token):**
    -   **Definição:** Um padrão aberto para criar tokens de acesso que afirmam um certo número de claims. Usado para autenticação.

-   **LangChain:**
    -   **Definição:** Um framework para desenvolver aplicações alimentadas por modelos de linguagem. Usado no Recoloca. Ai para orquestrar o sistema RAG e potencialmente para os Agentes de IA.

-   **LGPD (Lei Geral de Proteção de Dados Pessoais):**
    -   **Definição:** A legislação brasileira de proteção de dados.

-   **LLD (Low-Level Design):**
    -   **Definição:** Documento que detalha o design interno de componentes específicos do software.
    -   **Localização:** [[docs/03_Arquitetura_e_Design/03_LLDs/]]

-   **LLM (Large Language Model):**
    -   **Definição:** Um modelo de IA treinado em grandes quantidades de texto, capaz de entender e gerar linguagem humana (Ex: Google Gemini).

-   **MVP (Minimum Viable Product / Produto Mínimo Viável):**
    -   **Definição:** A versão de um novo produto que permite a uma equipe coletar a quantidade máxima de aprendizado validado sobre os clientes com o mínimo esforço.

-   **NVIDIA Drivers:**
    -   **Definição:** Software que permite ao sistema operacional comunicar-se com a GPU NVIDIA. São um pré-requisito para usar CUDA e, consequentemente, FAISS-GPU e PyTorch com aceleração de GPU.

-   **OpenRouter:**
    -   **Definição:** Um gateway que permite acesso a múltiplos modelos de LLM de diferentes provedores através de uma API unificada.

-   **PyMuPDF (fitz):**
    -   **Definição:** Uma biblioteca Python para acessar e manipular arquivos PDF. Usada no Recoloca. Ai para extrair texto de currículos em PDF para o sistema RAG e para a funcionalidade de otimização de CV.

-   **PWA (Progressive Web Application):**
    -   **Definição:** Uma aplicação web que utiliza tecnologias web modernas para oferecer uma experiência de usuário similar a de um aplicativo nativo.

-   **RLS (Row-Level Security):**
    -   **Definição:** Uma funcionalidade de banco de dados (como no PostgreSQL/Supabase) que permite controlar o acesso a linhas específicas em uma tabela com base nas características do usuário que está fazendo a consulta.

-   **SaaS (Software as a Service):**
    -   **Definição:** Um modelo de licenciamento e entrega de software no qual o software é licenciado por assinatura e hospedado centralmente.

-   **SDLC (Software Development Life Cycle):**
    -   **Definição:** O processo de planejamento, criação, teste e deploy de um sistema de informação.

-   **Sentence Transformers:**
    -   **Definição:** Uma biblioteca Python que fornece uma maneira fácil de calcular embeddings para sentenças, parágrafos e imagens. Usada no Recoloca. Ai para carregar e utilizar o modelo `BAAI/bge-m3`.

-   **Trae IDE:**
    -   **Definição:** O Ambiente de Desenvolvimento Integrado com IA que será utilizado pelo Maestro para codificar e interagir com os Agentes de IA Mentores.

-   **`unstructured`:**
    -   **Definição:** Uma biblioteca Python para pré-processar texto e extrair dados de diversos tipos de arquivos não estruturados (como Markdown, HTML, PDF, etc.), preparando-os para ingestão em sistemas de IA como RAG.

-   **UVP (Unique Value Proposition / Proposta Única de Valor):**
    -   **Definição:** Uma declaração clara que descreve o benefício de sua oferta, como você resolve as necessidades do seu cliente e o que o distingue da concorrência.

-   **UX (User Experience / Experiência do Usuário):**
    -   **Definição:** As percepções e respostas de uma pessoa que resultam do uso ou da antecipação do uso de um produto, sistema ou serviço.

-   **UI (User Interface / Interface do Usuário):**
    -   **Definição:** O meio pelo qual um usuário interage com uma máquina, sistema ou aplicação.

-   **Vector Store (Banco de Dados Vetorial):**
    -   **Definição:** Um tipo de banco de dados otimizado para armazenar e buscar vetores de embeddings. No Recoloca. Ai, o FAISS-GPU é a implementação inicial do Vector Store.

## 5. Histórico de Versões

### v1.2 (Janeiro 2025) - Orquestração Inteligente e Specialized Intelligence
- **Adição de Novos Termos:** Orquestração Inteligente, Specialized Intelligence, Agente Production-Ready, Métricas de Specialized Intelligence
- **Atualização de Referências:** Alinhamento com versões atualizadas dos documentos centrais (TAP v1.1, GUIA_AVANCADO v2.4, HLD v1.1, AGENTES_IA_MENTORES_OVERVIEW v3.1)
- **Consolidação Metodológica:** Integração dos conceitos avançados de orquestração de agentes e métricas de qualidade
- **Expansão Conceitual:** Definições detalhadas dos critérios objetivos para agentes "Production-Ready"

### v1.1 (Junho 2025)
- Versão inicial do glossário
- Definições básicas dos termos da metodologia e do projeto
- Estruturação das seções principais

## 6. Documentos Relacionados

### Documentos de Gestão
- [[docs/01_Guias_Centrais/TAP.md]] (v1.1) - Termo de Abertura do Projeto
- [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5) - Plano Mestre
- [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.4) - Metodologia Avançada
- [[docs/00_Gerenciamento_Projeto/KANBAN_Recoloca_AI.md]] - Gestão de Tarefas

### Documentos Técnicos
- [[docs/02_Requisitos/ERS.md]] (v0.5) - Especificação de Requisitos
- [[docs/03_Arquitetura_e_Design/HLD.md]] (v1.1) - Arquitetura de Alto Nível
- [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]] (v3.1) - Visão Geral dos Agentes

### Perfis de Agentes
- [[docs/04_Agentes_IA/Perfis/]] - Perfis detalhados de cada Agente de IA Mentor

---

**Nota:** Este glossário é um documento vivo que evolui continuamente com o projeto. A metodologia de "Orquestração Inteligente" e "Specialized Intelligence" representa um marco na maturidade do projeto, estabelecendo critérios objetivos para qualidade e performance dos agentes de IA.

--- FIM DO DOCUMENTO GLOSSARIO_Recoloca_AI.md (v 1.2) ---