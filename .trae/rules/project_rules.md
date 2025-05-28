# Project Rules for Recoloca.ai

## 1. Diretrizes Gerais do Projeto

* **Objetivo Principal:** Desenvolver o MVP do Recoloca.ai, um Micro-SaaS para auxiliar profissionais brasileiros na recolocação profissional, conforme definido em `[[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]]` e `[[docs/02_Requisitos/ERS.md]]`. [cite: 11, 353, 354, 356, 357, 358]
* **Metodologia:** Aplicar o "Desenvolvimento Solo Ágil Aumentado por IA", com o "Maestro" orquestrando "Agentes Mentores de IA", conforme `[[docs/01_Guias_Centrais/GUIA_AVANCADO_V1.md]]`. [cite: 5, 6, 17]
* **Público-Alvo:** Focar nas necessidades de profissionais de tecnologia brasileiros em busca de recolocação. [cite: 1, 378]
* **Fonte da Verdade:** A "Documentação Viva" mantida no Obsidian e versionada com Git é a fonte primária da verdade. Agentes devem priorizar informações de documentos linkados e do RAG.

## 2. Padrões Técnicos Mandatórios

* **Stack Tecnológica:**
    * **Frontend (PWA):** **Flutter (Dart)**. [cite: 13, 381]
    * **Backend:** **Python com FastAPI**. [cite: 13, 382]
    * **Banco de Dados & Autenticação:** **Supabase (PostgreSQL)**. [cite: 13, 383]
    * **Extensão de Navegador:** **JavaScript, HTML, CSS** (Chrome). [cite: 13, 381]
    * **IA LLM:** **Google Gemini Pro & Flash** (via OpenRouter). [cite: 13, 384]
    * **Parsing de PDF:** **pymupdf (Fitz)** primário, **Tesseract OCR (pt-BR)** como fallback, e **LLM** para categorização semântica. [cite: 15, 385, 386]
* **Especificação de API:** **OpenAPI 3.0** em formato **YAML**, localizada em `[[docs/03_Arquitetura_e_Design/API_Specs/]]`. [cite: 82, 161]
* **Controle de Versão:** **Git** é obrigatório. Mensagens de commit devem ser claras e seguir um padrão (ex: Conventional Commits).
* **Guia de Estilo:** Seguir **TODAS** as diretrizes definidas em `[[docs/03_Arquitetura_e_Design/STYLE_GUIDE.md]]` (cores, fontes, espaçamento, componentes, tom de voz, etc.). [cite: 460]

## 3. Diretrizes para Agentes de IA

* **Consulta à Base de Conhecimento (RAG):** **SEMPRE** consulte a base de conhecimento RAG (via ferramenta configurada ou `#Context` aprofundado) antes de gerar código, design ou documentação complexa para garantir alinhamento com `[[docs/02_Requisitos/ERS.md]]`, `[[docs/03_Arquitetura_e_Design/HLD.md]]`, LLDs e ADRs. [cite: 309, 326, 327]
* **Documentação Viva:**
    * Gere docstrings (Google Style para Python, Dartdoc para Dart) e comentários em Português do Brasil para todo código produzido. [cite: 242, 253]
    * Gere diagramas UML e de fluxo em **Mermaid.js**. [cite: 142]
    * Refira-se a outros documentos usando links `[[...]]`.
* **Segurança (Security by Design):**
    * Implemente práticas seguras em todo o código (validação de inputs, sanitização, controle de acesso).
    * Considere os riscos **OWASP Top 10** e **OWASP LLM Top 10**. [cite: 468]
    * Siga as diretrizes da **LGPD** ao lidar com dados do usuário. [cite: 465]
* **Testes:**
    * Gere **testes unitários** (pytest para Python, flutter\_test para Dart) para o código produzido. [cite: 284]
    * Gere **casos de teste** em formato **Gherkin** a partir de HUs e ACs quando solicitado. [cite: 266, 278]
* **HITL (Human-in-the-Loop):** Esteja ciente de que **TODAS** as saídas significativas serão revisadas pelo "Maestro". Gere código claro, modular e fácil de revisar. Explique suas decisões quando solicitado ou quando a lógica for complexa.
* **Parsing de PDF (RF-CV-002):** Ao lidar com esta funcionalidade, siga a abordagem de múltiplos estágios (pymupdf -> Tesseract -> LLM) e lembre-se da necessidade de validação pelo usuário (RF-CV-004). [cite: 15, 191, 419, 420, 425]

## 4. Comunicação e Formato de Saída

* **Linguagem:** **Português do Brasil**.
* **Clareza:** Seja claro e conciso, mas forneça detalhes quando necessário.
* **Formato:**
    * Código: Blocos de código formatados corretamente com a linguagem especificada.
    * Documentação: Markdown.
    * APIs: YAML (OpenAPI 3.0).
    * Diagramas: Código Mermaid.js.
* **Referências:** Sempre que possível, indique as fontes de informação ou os requisitos que basearam sua resposta (ex: "Com base no RF-AUTH-001...").