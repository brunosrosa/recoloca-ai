# Project Rules for Recoloca.ai

**Versão**: 1.3
**Data de Última Atualização**: 03 de junho de 2025
**Baseado em**: [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5), [[docs/02_Requisitos/ERS.md]] (v0.5), [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.3), [[docs/03_Arquitetura_e_Design/ADR/ADR_001_Ferramentas_Core.md]] (v1.0)

## 1. Diretrizes Gerais do Projeto

- **Objetivo Principal do Projeto:** Desenvolver o Recoloca.ai, um Micro-SaaS para auxiliar profissionais brasileiros na recolocação profissional, com um foco inicial no MVP para validar a proposta de valor e evoluir continuamente com base no feedback e na visão de longo prazo. Conforme definido em [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5, Seção 1.1 e 1.3) e [[docs/02_Requisitos/ERS.md]] (v0.5).
- **Metodologia:** Aplicar o "Desenvolvimento Solo Ágil Aumentado por IA", com o "Maestro" orquestrando "Agentes Mentores de IA", conforme [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v2.3). O `@AgenteOrquestrador` atua como um PM Mentor chave, auxiliando o Maestro na validação estratégica antes da delegação de tarefas.
- **Público-Alvo:** Focar nas necessidades de profissionais de tecnologia brasileiros em busca de recolocação, conforme detalhado na [[docs/02_Requisitos/ERS.md]] (v0.5).
- **Fonte da Verdade:** A "Documentação Viva" mantida no Obsidian e versionada com Git é a fonte primária da verdade. Agentes DEVEM priorizar informações de documentos linkados e do RAG. Todos os links para documentos internos DEVEM usar o caminho relativo a partir da raiz do vault (ex: [[docs/02_Requisitos/ERS.md]]).
    
## 2. Padrões Técnicos Mandatórios

- **Stack Tecnológica (Conforme [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] v1.5, Seção 4.1 e [[docs/03_Arquitetura_e_Design/ADR/ADR_001_Ferramentas_Core.md]] v1.0):**
    - **Frontend (PWA):** Flutter (Dart).
    - **Backend:** Python com FastAPI.
    - **Banco de Dados & Autenticação:** Supabase (PostgreSQL).
    - **IA LLM:** Google Gemini Pro & Flash (via OpenRouter ou diretamente).
    - **Parsing de PDF:** `pymupdf` (Fitz) primário, `Tesseract OCR` (pt-BR) como fallback, e LLM para categorização semântica.
    - **Framework de Orquestração RAG:** LangChain (Python).
    - **Vector Store (RAG):** FAISS-GPU (local inicial, utilizando CUDA).
    - **Embedding Model (RAG):** `BAAI/bge-m3` (via Sentence Transformers).
    - **Ambiente de Desenvolvimento RAG:** Conda (com Python 3.10).
    - **Extensão de Navegador (Pós-MVP):** JavaScript, HTML, CSS (Chrome).
- **Especificação de API:** OpenAPI 3.0 em formato YAML, localizada em [[docs/03_Arquitetura_e_Design/API_Specs/RecolocaAPI_v1_OpenAPI.yaml]].
- **Controle de Versão:** Git é obrigatório. Mensagens de commit DEVEM ser claras e seguir o padrão Conventional Commits.
- **Guia de Estilo:** Seguir **TODAS** as diretrizes definidas em [[docs/03_Arquitetura_e_Design/STYLE_GUIDE.md]] (cores, fontes, espaçamento, componentes, tom de voz, etc.).
    
## 3. Diretrizes para Agentes de IA

- **Consulta à Base de Conhecimento (RAG) e Ferramentas de Contexto:**
    - **SEMPRE** consulte a base de conhecimento RAG (via ferramenta configurada ou `#Context` aprofundado) antes de gerar código, design ou documentação complexa para garantir alinhamento com [[docs/02_Requisitos/ERS.md]], [[docs/03_Arquitetura_e_Design/HLD.md]], LLDs e ADRs.
    - O `@AgenteOrquestrador` DEVE utilizar o RAG para acessar materiais de Product Management (em [[rag_infra/source_documents/PM_Knowledge/]]) para embasar suas perguntas estratégicas ao Maestro.
    - **Agentes de Desenvolvimento (Builders):** Ao gerar ou verificar código que utilize bibliotecas, frameworks ou SDKs externos, DEVEM utilizar ativamente funcionalidades como MCP/Context7 (se disponíveis no Trae IDE) em conjunto com o RAG. O RAG fornecerá o contexto específico do projeto e da "Documentação Viva", enquanto o MCP/Context7 (ou consulta direta à documentação oficial da ferramenta) fornecerá a sintaxe mais atualizada e melhores práticas da ferramenta externa. Em caso de conflito ou dúvida, priorize a documentação oficial da ferramenta externa e sinalize ao `@AgenteOrquestrador`/Maestro.
- **Documentação Viva:**
    - Gere docstrings (Google Style para Python, Dartdoc para Dart) e comentários em Português do Brasil para todo código produzido.
    - Gere diagramas UML e de fluxo em **Mermaid.js**.
    - Ao referenciar outros documentos do projeto, utilize **ESTRITAMENTE** o formato de link interno do Obsidian: [[docs/Caminho/Para/Arquivo.md]], [[docs/Arquivo.md#Cabeçalho Específico]], ou [[rag_infra/source_documents/Arquivo_RAG.md]] (ajustando o caminho base conforme a localização do arquivo referenciado). **NÃO** envolva esses links com crases (`) ou qualquer outra formatação que os transforme em texto literal, a menos que o objetivo seja demonstrar o código do link em si.
- **Segurança (Security by Design):**
    - Implemente práticas seguras em todo o código (validação de inputs, sanitização, controle de acesso).
    - Considere os riscos **OWASP Top 10** e **OWASP LLM Top 10**.
    - Siga as diretrizes da **LGPD** ao lidar com dados do usuário. 
- **Testes:**
    - Gere **testes unitários** (pytest para Python, flutter_test para Dart) para o código produzido.
    - Gere **casos de teste** em formato **Gherkin** a partir de HUs e ACs quando solicitado.
- **HITL (Human-in-the-Loop):**
    - Esteja ciente de que **TODAS** as saídas significativas serão revisadas pelo "Maestro". Gere código claro, modular e fácil de revisar.
    - Explique suas decisões quando solicitado ou quando a lógica for complexa, especialmente se houver desvios de padrões ou alternativas consideradas.
- **Parsing de PDF (Conforme `RF-CV-001`, `RF-CV-002` da [[docs/02_Requisitos/ERS.md]]):** Ao lidar com esta funcionalidade, siga a abordagem de múltiplos estágios (pymupdf -> Tesseract -> LLM) e lembre-se da necessidade de validação pelo usuário.
    
## 4. Comunicação e Formato de Saída

- **Linguagem:** **Português do Brasil** para toda comunicação e documentação gerada (exceto onde a linguagem de programação exija inglês, como nomes de variáveis/funções).
- **Clareza e Contexto:** Seja claro e conciso, mas forneça detalhes suficientes para evitar ambiguidades. Ao responder a uma solicitação, sempre referencie os documentos ou requisitos que basearam sua resposta (ex: "Com base no `RF-AUTH-001` da [[docs/02_Requisitos/ERS.md]] v0.5...").
    
- **Formato de Saída:**
    - **Código:** Blocos de código formatados corretamente com a linguagem especificada.
    - **Documentação e Textos Longos:** Markdown. O Agente DEVE gerar o documento completo, sem abreviar seções, mesmo que resulte em uma resposta longa, a menos que explicitamente instruído a resumir pelo Maestro.
    - **Finalização de Documentos:** Ao gerar um documento completo, o Agente DEVE incluir uma linha de finalização clara, como: `--- FIM DO DOCUMENTO [NOME_DO_ARQUIVO] (vX.X) ---` (substituindo NOME_DO_ARQUIVO e vX.X conforme apropriado).
    - **APIs:** YAML (OpenAPI 3.0).
    - **Diagramas:** Código Mermaid.js (sem indentação inicial e com textos de nós entre aspas, escapando aspas internas com `&quot;` se necessário).
- **Referências:** Sempre que possível, indique as fontes de informação ou os requisitos que basearam sua resposta.
    
## 5. Interação com o `@AgenteOrquestrador` (PM Mentor)

- O `@AgenteOrquestrador` é o **ponto de partida** para a maioria das novas tarefas ou features que envolvam estratégia de produto ou refinamento de requisitos.
    
- Agentes especializados (Dev, QA, etc.) devem esperar prompts que foram co-criados ou validados pelo Maestro em conjunto com o `@AgenteOrquestrador`, garantindo que o contexto estratégico e os requisitos de Product Management tenham sido considerados.
    
- Se um Agente especializado receber um prompt diretamente do Maestro que pareça carecer de clareza estratégica ou desalinhado com os objetivos do produto (conforme RAG), ele PODE sugerir uma consulta prévia ao `@AgenteOrquestrador`.

--- FIM DO DOCUMENTO project_rules.md (v1.3) ---