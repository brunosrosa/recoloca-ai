---
sticker: lucide//heart-crack
---
# High-Level Design (HLD) do Projeto Recoloca.ai

**Versão**: 0.9 (Pré-Revisão Interativa)

**Data de Criação**: 03 de junho de 2025

**Data de Última Atualização**: 03 de junho de 2025

**Autor**: @AgenteM_ArquitetoHLD (com supervisão do Maestro Bruno S. Rosa)

**Baseado em**:
- [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5)
    
- [[docs/02_Requisitos/ERS.md]] (v0.5)
    
- [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.3)
    
- [[docs/03_Arquitetura_e_Design/ADR/ADR_001_Ferramentas_Core.md]] (v1.0)
    
## 1. Introdução

### 1.1. Propósito

Este documento descreve a arquitetura de alto nível (High-Level Design - HLD) do sistema **Recoloca.ai**. O objetivo é fornecer uma visão geral dos principais componentes do sistema, suas responsabilidades, interações e as tecnologias chave empregadas. Este HLD servirá como guia para o desenvolvimento do MVP e futuras iterações, garantindo que as decisões de design estejam alinhadas com os requisitos funcionais (RFs) e não funcionais (RNFs) definidos na [[docs/02_Requisitos/ERS.md]] e com as escolhas tecnológicas registradas no [[docs/03_Arquitetura_e_Design/ADR/ADR_001_Ferramentas_Core.md]].
### 1.2. Escopo

O escopo deste HLD abrange os principais subsistemas do Recoloca.ai, incluindo:

- A aplicação Frontend (PWA).
    
- A API Backend.
    
- Os serviços de Backend as a Service (BaaS) para autenticação e persistência de dados.
    
- A integração com Modelos de Linguagem Ampla (LLMs).
    
- O sistema de Retrieval Augmented Generation (RAG) para contextualização da IA.
    
- As ferramentas de automação e CI/CD.
    
- A futura Extensão de Navegador (Pós-MVP).
    

Detalhes de design de baixo nível (LLD) para módulos específicos serão documentados separadamente em [[docs/03_Arquitetura_e_Design/LLD/]].
### 1.3. Siglas e Termos

Consulte o [[docs/01_Guias_Centrais/GLOSSARIO_Recoloca_AI.md]] (v1.1) para definições de termos e siglas utilizados neste documento.
## 2. Visão Geral da Arquitetura

O Recoloca.ai é projetado como um sistema distribuído, composto por uma aplicação frontend (PWA), uma API backend, serviços de BaaS, e integrações com serviços de IA e automação. A arquitetura visa ser modular, escalável e manutenível, suportando a metodologia de "Desenvolvimento Solo Ágil Aumentado por IA".

**Principais Componentes:**

1. **Frontend (PWA - Flutter):** Interface com o usuário, lógica de apresentação, gerenciamento de estado local e comunicação com a API Backend.
    
2. **API Backend (Python/FastAPI):** Lógica de negócios principal, orquestração de chamadas para LLMs, interação com o Supabase e o sistema RAG.
    
3. **Supabase (BaaS):** Gerencia autenticação de usuários, banco de dados PostgreSQL (dados da aplicação, metadados de CVs) e armazenamento de arquivos (ex: PDFs de currículos).
    
4. **Google Gemini LLMs (via OpenRouter):** Fornece as capacidades de processamento de linguagem natural para otimização de CV, coaching, importação de vagas, etc.
    
5. **Sistema RAG Local (LangChain + FAISS-GPU + `BAAI/bge-m3`):** Indexa a "Documentação Viva" e outros materiais de referência para fornecer contexto dinâmico aos LLMs e Agentes de IA.
    
6. **Agentes de IA (Trae IDE):** Não são um componente de runtime da aplicação do _usuário final_, mas sim do ambiente de _desenvolvimento e metodologia_. Interagem com o sistema RAG e os LLMs para auxiliar o Maestro.
    
7. **Pipedream (Automação):** Orquestra fluxos de CI/CD e outras automações (ex: gatilhos para reindexar o RAG).
    
8. **Extensão** de **Navegador (Chrome - Pós-MVP):** Coleta dados de vagas de portais de emprego.
    
## 3. Diagrama da Arquitetura de Alto Nível

O diagrama abaixo ilustra os principais componentes do sistema Recoloca.ai e suas interações.

```mermaid
graph RL
    subgraph "Usuário Final"
        U["👤 Usuário (Profissional)"]
    end

    subgraph "Ambiente de Desenvolvimento e Metodologia"
        Maestro["🧑‍💻 Maestro (Bruno S. Rosa)"]
        TraeIDE["🛠️ Trae IDE"]
        AgentesIA["🤖 Agentes de IA Mentores<br>(Inclui @AgenteM_Documentacao)"]
        RAG_Dev["📚 Sistema RAG Local<br>(LangChain, FAISS-GPU, BAAI/bge-m3)"]
        Obsidian["📓 Obsidian (Documentação Viva)"]
        GitRepo_Dev["📦 Repositório Git<br>(Fonte da Verdade)"]

        Maestro -- "Interage com" --> TraeIDE
        TraeIDE -- "Orquestra" --> AgentesIA
        AgentesIA -- "Utiliza para Contexto" --> RAG_Dev
        AgentesIA -- "Consultam" --> GeminiAPI_Dev["🌐 Google Gemini APIs<br>(via OpenRouter)"]
        AgentesIA -- "Cria/Atualiza Documentos" --> Obsidian
        Maestro -- "Revisa e Cura Documentos" --> Obsidian
        Obsidian -- "Fonte para" --> RAG_Dev
        Obsidian -- "Sincroniza com" --> GitRepo_Dev
        Maestro -- "Commits/Pushes para" --> GitRepo_Dev
    end

    subgraph "Sistema Recoloca.ai (Produção)"
        Frontend_PWA["📱 Frontend PWA<br>(Flutter Web)<br>Hospedado: Vercel"]
        Backend_API["⚙️ API Backend<br>(Python/FastAPI)<br>Hospedado: Render"]
        Supabase["☁️ Supabase (BaaS)<br>- Autenticação<br>- PostgreSQL DB<br>- Storage (PDFs CVs)"]
        GeminiAPI_Prod["🌐 Google Gemini APIs<br>(via OpenRouter)<br>Para: Otimização CV, Coach, Importação Vagas"]
        RAG_Prod_Context_Source["(Lógica de acesso ao RAG<br>para contexto em runtime)"]

        U -- "Interage via HTTPS" --> Frontend_PWA
        Frontend_PWA -- "Chamadas API (HTTPS/REST)" --> Backend_API
        Backend_API -- "Consultas SQL, Auth, Storage" --> Supabase
        Backend_API -- "Chamadas API" --> GeminiAPI_Prod
        Backend_API -- "Consulta (Interna)" --> RAG_Prod_Context_Source
        RAG_Prod_Context_Source -. "Contexto injetado no prompt" .-> GeminiAPI_Prod

        %% Extensão Pós-MVP
        Extensao["🌐 Extensão Chrome (Pós-MVP)"]
        U -- "Usa" --> Extensao
        Extensao -- "Chamadas API (HTTPS/REST)" --> Backend_API
    end

    subgraph "Ferramentas de Operação e Automação"
        Pipedream["🚀 Pipedream<br>(CI/CD, Automações)"]

        GitRepo_Dev -- "Gatilho para (CI/CD)" --> Pipedream
        Pipedream -- "Deploy" --> Frontend_PWA
        Pipedream -- "Deploy" --> Backend_API
        Pipedream -- "Pode acionar<br>Reindexação RAG" --> RAG_Dev
    end

    %% Estilização para clareza
    classDef user fill:#D6EAF8,stroke:#2E86C1,stroke-width:2px;
    classDef devEnv fill:#E8DAEF,stroke:#8E44AD,stroke-width:2px;
    classDef prodSys fill:#D5F5E3,stroke:#28B463,stroke-width:2px;
    classDef opsTools fill:#FCF3CF,stroke:#F39C12,stroke-width:2px;

    class U user;
    class Maestro,TraeIDE,AgentesIA,RAG_Dev,Obsidian,GeminiAPI_Dev,GitRepo_Dev devEnv;
    class Frontend_PWA,Backend_API,Supabase,GeminiAPI_Prod,RAG_Prod_Context_Source,Extensao prodSys;
    class Pipedream opsTools;
```

**Nota sobre o Diagrama:**

- O "Sistema RAG Local" no ambiente de desenvolvimento é a infraestrutura (`rag_infra/`) que indexa a "Documentação Viva".
    
- O nó "Lógica de acesso ao RAG para contexto em runtime" no sistema de produção representa a funcionalidade pela qual o Backend API acessa e utiliza os _resultados_ do processo de RAG (os chunks de texto relevantes) para enriquecer os prompts enviados aos LLMs em runtime, quando necessário para funcionalidades como o Coach IA. A implementação exata de como o índice RAG (criado no ambiente de dev) é disponibilizado ou consultado pelo backend em produção (seja por uma cópia do índice, uma API interna, ou outro mecanismo) será detalhada no LLD.
    
## 4. Descrição dos Componentes

### 4.1. Frontend (PWA - Flutter)

- **Tecnologia:** Flutter (Dart), compilado para Web (PWA).
    
- **Hospedagem:** Vercel (ou similar).
    
- **Responsabilidades:**
    
    - Renderizar a interface do usuário (UI) e gerenciar a experiência do usuário (UX).
        
    - Gerenciar o estado da aplicação no lado do cliente (ex: Provider, Riverpod).
        
    - Realizar chamadas HTTPS/REST para a API Backend para obter e enviar dados.
        
    - Lidar com a entrada do usuário e validações no lado do cliente.
        
    - Implementar a lógica de apresentação das funcionalidades (Kanban, formulários de CV, Chatbot UI, etc.).
        
    - Armazenamento local (ex: SharedPreferences) para preferências do usuário ou cache leve.
        
- **Interações Chave:**
    
    - Com o Usuário: Recebe inputs, exibe informações.
        
    - Com a API Backend: Envia requisições para todas as operações de dados e lógica de negócios.
        
### 4.2. API Backend (Python/FastAPI)

- **Tecnologia:** Python 3.10+, FastAPI.
    
- **Hospedagem:** Render (ou similar).
    
- **Responsabilidades:**
    
    - Expor endpoints RESTful seguros para o Frontend PWA e a Extensão de Navegador.
        
    - Implementar a lógica de negócios principal da aplicação (regras de validação, processamento de dados).
        
    - Orquestrar chamadas para os serviços do Supabase (autenticação, banco de dados, storage).
        
    - Orquestrar chamadas para as APIs do Google Gemini (via OpenRouter) para funcionalidades de IA.
        
    - Integrar-se com o sistema RAG para fornecer contexto aos LLMs quando necessário em runtime (ex: para o Coach IA).
        
    - Gerenciar a lógica de parsing de PDFs de currículos (usando `pymupdf`, `Tesseract`, e LLMs).
        
    - Implementar a lógica de tiers (Freemium/Premium) e controle de acesso a funcionalidades.
        
- **Interações Chave:**
    
    - Com o Frontend PWA/Extensão: Recebe requisições, envia respostas JSON.
        
    - Com o Supabase: Autentica usuários (validação de JWT), realiza operações CRUD no banco de dados PostgreSQL, gerencia uploads/downloads de arquivos.
        
    - Com Google Gemini APIs: Envia prompts (potencialmente enriquecidos com contexto RAG) e recebe respostas geradas.
        
    - Com o Sistema RAG (em runtime): Acessa o índice vetorial (ou uma representação dele) para buscar chunks de texto relevantes para contextualizar prompts para os LLMs.
        
### 4.3. Supabase (BaaS)

- **Tecnologia:** Plataforma BaaS utilizando PostgreSQL.
    
- **Responsabilidades:**
    
    - **Autenticação:** Gerenciamento de identidades de usuários (cadastro, login, JWTs, RLS).
        
    - **Banco de Dados (PostgreSQL):** Persistência de todos os dados da aplicação (dados de usuários, vagas, currículos estruturados, histórico de interações, etc.).
        
    - **Storage:** Armazenamento seguro de arquivos enviados pelos usuários (ex: PDFs de currículos originais).
        
    - **Realtime (Opcional, Pós-MVP):** Para funcionalidades que exigem atualizações em tempo real (ex: notificações no Kanban).
        
- **Interações Chave:**
    
    - Com a API Backend: Principal consumidor dos serviços do Supabase.
        
    - Com o Frontend PWA (limitado): Pode interagir diretamente para autenticação ou upload de arquivos, se a arquitetura permitir e for seguro.
        
### 4.4. Google Gemini LLMs (via OpenRouter)

- **Tecnologia:** Modelos Gemini Pro e Flash da Google.
    
- **Acesso:** Primariamente via OpenRouter para flexibilidade e gerenciamento.
    
- **Responsabilidades:**
    
    - Fornecer as capacidades de Processamento de Linguagem Natural (PLN) para:
        
        - Importação inteligente de vagas (extração de dados de URLs).
            
        - Categorização semântica de seções de currículos.
            
        - Análise de adequação CV vs. Vaga (Score de Adequação).
            
        - Geração de sugestões de otimização de CV.
            
        - Estimativa de range salarial.
            
        - Respostas e interações do Coach IA.
            
- **Interações Chave:**
    
    - Com a API Backend: Recebe prompts (enriquecidos com contexto RAG quando aplicável) e retorna texto gerado ou análises.
        
### 4.5. Sistema RAG Local (Infraestrutura em `rag_infra/`)

- **Tecnologias:** LangChain, FAISS-GPU, `BAAI/bge-m3` (via Sentence Transformers), Python, Conda.
    
- **Responsabilidades (Ambiente de Desenvolvimento/Manutenção):**
    
    - Indexar a "Documentação Viva" (Markdown do Obsidian) e outros materiais de referência (ex: artigos de PM, pesquisas salariais) da pasta `rag_infra/source_documents/`.
        
    - Processo: Carregar documentos, dividir em chunks, gerar embeddings vetoriais usando `BAAI/bge-m3`, e armazenar esses vetores em um índice FAISS-GPU (`rag_infra/data_index/faiss_index_bge_m3/`).
        
    - Fornecer uma maneira para os Agentes de IA (durante o desenvolvimento) e para o Backend API (em runtime, para certas funcionalidades) consultarem este índice para obter contexto relevante.
        
- **Interações Chave:**
    
    - Com a "Documentação Viva" (Obsidian): Lê os documentos fonte.
        
    - Com os Agentes de IA (via Trae IDE/scripts): Permite que os agentes obtenham contexto específico do projeto.
        
    - Com a API Backend (em runtime): A API Backend precisará de um mecanismo para consultar este índice (ou uma cópia/serviço derivado dele) para enriquecer prompts para os LLMs (ex: o Coach IA usando a base de conhecimento curada).
        
### 4.6. Agentes de IA (Trae IDE)

- **Tecnologia:** Configurações e prompts customizados no Trae IDE, utilizando os LLMs Gemini.
    
- **Responsabilidades (Ambiente de Desenvolvimento e Metodologia):**
    
    - Auxiliar o Maestro em todas as fases do SDLC, conforme definido no [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]].
        
    - Utilizar o Sistema RAG para obter contexto do projeto.
        
    - Gerar artefatos (código, documentação, designs, HUs, casos de teste, etc.) sob a supervisão do Maestro (HITL).
        
- **Interações Chave:**
    
    - Com o Maestro (via Trae IDE): Recebe instruções, fornece outputs.
        
    - Com o Sistema RAG Local: Obtém contexto.
        
    - Com os LLMs Gemini: Para suas capacidades de geração e raciocínio.
        
### 4.7. Pipedream (Automação)

- **Tecnologia:** Plataforma de automação baseada em nuvem.
    
- **Responsabilidades:**
    
    - **CI/CD:** Automatizar os processos de build, teste e deploy do Frontend PWA (para Vercel) e da API Backend (para Render) a partir de gatilhos do repositório Git.
        
    - **Automação de Tarefas:** Potencialmente, acionar a reindexação do RAG em commits na documentação, enviar notificações, etc.
        
- **Interações Chave:**
    
    - Com o Repositório Git: Monitora pushes/merges.
        
    - Com Vercel/Render: Realiza deploys.
        
    - Com o Sistema RAG Local: Pode acionar scripts de reindexação.
        
### 4.8. Extensão de Navegador (Chrome - Pós-MVP)

- **Tecnologia:** JavaScript, HTML, CSS.
    
- **Responsabilidades:**
    
    - Permitir ao usuário capturar facilmente informações de vagas de portais de emprego (inicialmente LinkedIn).
        
    - Comunicar-se com a API Backend para enviar os dados capturados.
        
- **Interações Chave:**
    
    - Com o Usuário: Interface para captura e confirmação.
        
    - Com Portais de Emprego: Extrai dados do DOM (requer cuidado com seletores e termos de uso).
        
    - Com a API Backend: Envia os dados da vaga capturada.
        
## 5. Fluxos de Dados Chave (Exemplos)

### 5.1. Fluxo de Autenticação de Usuário

1. Usuário insere credenciais no Frontend PWA.
    
2. Frontend PWA envia credenciais para a API Backend.
    
3. API Backend encaminha para o serviço de Autenticação do Supabase.
    
4. Supabase valida, retorna JWT para a API Backend.
    
5. API Backend retorna JWT para o Frontend PWA.
    
6. Frontend PWA armazena JWT e o inclui em chamadas subsequentes.
    
### 5.2. Fluxo de Otimização de CV

1. Usuário seleciona uma vaga e um "Currículo Base Ativo" no Frontend PWA.
    
2. Frontend PWA envia ID da vaga e ID do currículo para a API Backend.
    
3. API Backend recupera a descrição da vaga e o conteúdo estruturado do currículo do Supabase.
    
4. API Backend envia a descrição da vaga e o currículo para o LLM Gemini (via OpenRouter), possivelmente com contexto adicional do RAG (ex: melhores práticas de CV para aquela área).
    
5. LLM Gemini analisa e retorna Score de Adequação, sugestões de otimização e estimativa salarial.
    
6. API Backend processa a resposta do LLM e a envia para o Frontend PWA.
    
7. Frontend PWA exibe as informações ao usuário.
    
### 5.3. Fluxo de Consulta ao RAG por um Agente de IA (Desenvolvimento)

1. Maestro interage com um Agente de IA no Trae IDE (ex: `@AgenteM_ArquitetoHLD` para discutir uma decisão de design).
    
2. O Trae IDE (ou a lógica do `@AgenteOrquestrador`) formula uma consulta para o Sistema RAG Local com base na pergunta do Maestro.
    
3. O Sistema RAG Local (`rag_retriever.py`) busca no índice FAISS-GPU os chunks de texto mais relevantes da "Documentação Viva" (ex: ADRs existentes, HLD, ERS).
    
4. Os chunks recuperados são injetados no prompt enviado ao LLM Gemini que motoriza o `@AgenteM_ArquitetoHLD`.
    
5. O `@AgenteM_ArquitetoHLD` utiliza esse contexto para gerar uma resposta mais informada e específica para o projeto.
    
## 6. Considerações Arquiteturais Chave

### 6.1. Escalabilidade

- **Frontend (Vercel) e Backend (Render):** Plataformas PaaS que oferecem escalabilidade automática ou gerenciada.
    
- **Supabase:** Projetado para escalar, com planos que suportam maior carga.
    
- **LLMs (OpenRouter):** Gerencia a escalabilidade das chamadas às APIs dos LLMs.
    
- **Sistema RAG Local:** Para o MVP, o RAG local com FAISS-GPU é suficiente. Para escalar o RAG em produção para um grande número de usuários ou uma base de conhecimento muito dinâmica, pode ser necessário considerar soluções de Vector DB gerenciadas na nuvem (ex: Supabase pgvector, Pinecone, Weaviate) e uma arquitetura de atualização do índice mais robusta.
    
### 6.2. Segurança

- **Autenticação e Autorização:** Supabase Auth com JWTs e RLS no PostgreSQL.
    
- **Comunicação:** HTTPS/TLS para todas as comunicações entre componentes.
    
- **Validação de Dados:** Validação rigorosa de inputs no Frontend e, crucialmente, no Backend API (usando Pydantic).
    
- **Segurança de APIs LLM:** Gerenciamento seguro de chaves de API (ex: via variáveis de ambiente, `python-dotenv`).
    
- **OWASP Top 10 e OWASP LLM Top 10:** Considerar estas diretrizes no desenvolvimento.
    
- **LGPD:** Conformidade com a Lei Geral de Proteção de Dados (ex: exclusão de dados do usuário, consentimento).
    
### 6.3. Performance

- **Frontend:** Otimizações do Flutter Web, lazy loading, code splitting. Core Web Vitals como meta.
    
- **Backend:** FastAPI é altamente performático. Otimização de consultas ao banco de dados.
    
- **LLM:** Escolha entre Gemini Flash (mais rápido, menor custo) e Pro (mais capaz) conforme a necessidade da tarefa.
    
- **RAG:** FAISS-GPU para buscas vetoriais rápidas. Otimização do tamanho dos chunks e da qualidade dos embeddings.
    
### 6.4. Manutenibilidade e Evolução

- **Modularidade:** Componentes bem definidos com responsabilidades claras.
    
- **"Documentação Viva":** Essencial para o entendimento e evolução do sistema.
    
- **Testes Automatizados:** Cobertura de testes unitários e de integração.
    
- **CI/CD:** Automação de builds e deploys via Pipedream.
    
- **Stack Tecnológica Moderna:** Escolha de tecnologias com boas comunidades e perspectivas de futuro.
    
### 6.5. Custos

- Monitorar os custos de API dos LLMs, Supabase, Vercel, Render e Pipedream, especialmente para o modelo Freemium.
    
- Otimizar o uso de LLMs (ex: usar Gemini Flash sempre que possível) e recursos de infraestrutura.
    
## 7. Implicações para o LLD (Low-Level Design)

Este HLD estabelece a estrutura geral. Os LLDs para cada módulo principal (Autenticação, Kanban, Otimização de CV, Coach IA, etc.) precisarão detalhar:

- Modelos de dados específicos (esquemas PostgreSQL).
    
- Estrutura detalhada dos endpoints da API Backend.
    
- Interações específicas com os LLMs e o sistema RAG para cada funcionalidade de IA.
    
- Design de componentes de UI no Flutter.
    
- Algoritmos e lógica de negócios complexa.
    
## 8. Riscos Arquiteturais e Estratégias de Mitigação

- **Dependência de APIs Externas (LLMs, Supabase):**
    
    - _Mitigação:_ Design para resiliência (circuit breakers, retries), monitoramento, ter planos de contingência ou abstrações caso seja necessário trocar de provedor (OpenRouter ajuda com LLMs).
        
- **Complexidade da Integração RAG em Runtime:**
    
    - _Mitigação:_ Começar com um escopo limitado para o RAG em runtime (ex: apenas para o Coach IA), prototipar e testar exaustivamente.
        
- **Performance do Parsing de PDF e Análise de CV:**
    
    - _Mitigação:_ Otimizar o pipeline de parsing, usar LLMs eficientes (Gemini Flash), fornecer feedback ao usuário durante processos longos.
        
- **Gerenciamento de Custos de IA:**
    
    - _Mitigação:_ Implementar limites de uso (tiers), otimizar prompts, usar modelos mais baratos quando apropriado, monitorar custos de perto.
        

--- FIM DO DOCUMENTO HLD_Recoloca.ai (v1.0) ---