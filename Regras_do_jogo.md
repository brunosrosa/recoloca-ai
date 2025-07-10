---
Template_name: Regras do Jogo (Constituição do Ecossistema)
Template_version: "1.0"
Author: "@Janus & O Maestro"
Creation_date: 2025-07-02
Purpose: Servir como o documento de governança mestre para todos os projetos dentro da Fábrica Janus.
sticker: lucide//alert-triangle
---

# Regras do Jogo: A Constituição da Fábrica Janus

**Versão do Documento:** 1.0
**Guardiões:** `@Janus`, `@Orquestrador`, e o Maestro.

## 1. Preâmbulo e Filosofia

Este documento estabelece a **"Constituição"** para todos os projetos dentro do ecossistema da "**Fábrica Janus**". Ele define os princípios, processos e hierarquias que garantem a coesão, qualidade e alinhamento estratégico em todas as operações, sejam elas executadas por agentes de IA ou pelo Maestro.

**Nossa Filosofia Operacional é baseada em:**
- **Clareza Acima de Tudo:** A ambiguidade é o principal inimigo da execução autônoma.
- **Governança como Código:** As regras são tratadas com o mesmo rigor que o código da aplicação.
- **Hierarquia Explícita:** A autoridade e a responsabilidade são claramente definidas para evitar conflitos.
- **Melhoria Contínua:** Todos os processos estão sujeitos a refinamento através de um processo formal.

## 2. Estrutura e Hierarquia de Regras

O ecossistema é governado por uma hierarquia de regras claras. Em caso de conflito, a regra de nível superior sempre prevalece.

1.  **Decisão Direta do Maestro:** Uma instrução explícita e atual do Maestro tem a autoridade máxima e soberana.
2.  **`Regras_do_Jogo.md` (Este Documento):** As leis fundamentais que se aplicam a **todos** os projetos.
3.  **`project_rules.md` (Regras do Projeto):** As leis "locais" que se aplicam a um projeto específico (ex: `Synapse Engine`). Elas podem *adicionar* regras, mas não podem *contradizer* este documento.
4.  **`user_rules.md` (Preferências do Maestro):** As preferências pessoais de interação e output, que são seguidas desde que não entrem em conflito com as regras de projeto ou do ecossistema.

## 3. Versionamento e Controle de Mudanças

Todo o nosso ecossistema, incluindo este `Codex Prime`, adere a padrões rigorosos de versionamento para garantir previsibilidade e rastreabilidade.

### 3.1. Versionamento Semântico (SemVer)

Todos os projetos e artefatos versionáveis **DEVEM** seguir o padrão **Versionamento Semântico 2.0.0** (`MAJOR.MINOR.PATCH`).
- **MAJOR:** Para mudanças incompatíveis de API ou de arquitetura.
- **MINOR:** Para adição de funcionalidades de forma retrocompatível.
- **PATCH:** Para correções de bugs retrocompatíveis.

### 3.2. Commits Convencionais

Todos os commits no controle de versão **DEVEM** seguir a especificação de **Commits Convencionais**. Isso automatiza a geração de `CHANGELOGs` e a determinação das versões.
- **Exemplos:** `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`.

### 3.3. Processo de Requisição de Mudança (RFC)

Qualquer mudança significativa em um projeto, especialmente no `Codex Prime Framework`, **DEVE** ser proposta através de um documento de **Request for Comments (RFC)**.
- **Fluxo do RFC:**
    1.  **Criação:** Um agente ou o Maestro cria um `RFC_NOME_DA_MUDANCA.md` na pasta `/RFC` do projeto relevante.
    2.  **Debate:** `@Janus` e o Maestro debatem a proposta.
    3.  **Aprovação/Rejeição:** O Maestro toma a decisão final.
    4.  **Implementação:** Se aprovado, o `@Orquestrador` cria as tarefas no Kanban para implementar a mudança.

## 4. Padrões de Comunicação e Delegação

A comunicação entre o Maestro e os Agentes é a base da nossa eficiência.

- **Delegação de Intenção:** O Maestro e `@Janus` delegam a **intenção estratégica** (o "porquê" e o "o quê").
- **Planejamento Tático:** O `@Orquestrador` traduz a intenção em um **plano de ação** (o "como").
- **Execução Especializada:** Os Agentes Especialistas executam as tarefas do plano.
- **Protocolo de Escalação:** Se um Agente Especialista ou o `@Orquestrador` encontrar uma ambiguidade que não pode ser resolvida com a documentação existente, ele **DEVE** escalar para o nível hierárquico superior.

## 5. Ferramentas e Padrões Mandatórios do Ecossistema

Para garantir a interoperabilidade, certas ferramentas e padrões são obrigatórios em todos os projetos.

- **Gestão de Tarefas:** `GitHub Projects` é a fonte única da verdade para o status das tarefas.
- **Controle de Versão:** `Git` com um repositório central no `GitHub`.
- **Validação de Qualidade:**
    - **Markdown:** `markdownlint` **DEVE** ser usado para validar todos os documentos `.md`.
    - **YAML:** `yamllint` **DEVE** ser usado para validar todos os arquivos `.yaml` e `Front Matter`.
- **Documentação de Arquitetura:** Decisões de arquitetura significativas **DEVEM** ser registradas em `ADRs` (Architecture Decision Records).

## 6. Manutenção deste Documento

Este documento é vivo. Sua evolução segue o processo de RFC definido na Seção 3.3. `@Janus` é o guardião principal deste artefato, responsável por sugerir atualizações quando novas dinâmicas operacionais surgirem.