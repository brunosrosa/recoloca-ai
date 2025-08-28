---
sticker: lucide//shield-question
---
# 📋 COMO USAR O KANBAN NO OBSIDIAN (RECOLOCA.AI)

Este documento visa esclarecer o uso e os padrões do Kanban no Obsidian para o projeto Recoloca.ai, com foco na compatibilidade e nas melhores práticas para os plugins Obsidian Kanban e Obsidian Tasks.

## 💡 Entendendo o Kanban no Obsidian

O Obsidian, através do plugin Kanban, permite criar quadros Kanban diretamente em arquivos Markdown. No entanto, é crucial entender como a estrutura do Markdown interage com a visualização do Kanban para evitar problemas.

### ❌ O Problema com Títulos `##` (H2) e Colunas

Um ponto de atenção fundamental é o uso de títulos de segundo nível (`##`). No plugin Kanban do Obsidian, **cada título `##` é interpretado como uma nova coluna do Kanban**. <mcreference link="https://www.reddit.com/r/ObsidianMD/comments/rk45ig/help_previewing_linked_kanban_boards_as_boards/" index="3">3</mcreference>

**Exemplo de Problema:**

```markdown
# Meu Kanban

## Coluna 1
- Tarefa A
- Tarefa B

## Coluna 2
- Tarefa C

## Subseção Dentro da Coluna 2
Isso criaria uma nova coluna indesejada no Kanban, em vez de ser uma subseção da Coluna 2.
```

**Impacto:** Se você usar `##` para organizar subseções dentro de uma coluna (por exemplo, para agrupar tarefas por tipo ou subtópico), o plugin Kanban irá criar uma nova coluna para cada `##`, desorganizando completamente o quadro e dificultando a visualização e o gerenciamento.

### ✅ Solução: Use Títulos `###` (H3) ou Níveis Inferiores para Subseções

Para organizar o conteúdo dentro de uma coluna Kanban sem criar novas colunas, utilize títulos de terceiro nível (`###`) ou inferiores (`####`, etc.). Estes são interpretados como subtítulos dentro da coluna existente. <mcreference link="https://www.reddit.com/r/ObsidianMD/comments/rk45ig/help_previewing_linked_kanban_boards_as_boards/" index="3">3</mcreference>

**Exemplo de Solução Correta:**

```markdown
# Meu Kanban

## Coluna de Tarefas

### Tarefas Prioritárias
- [ ] Tarefa Importante 1
- [ ] Tarefa Importante 2

### Tarefas de Baixa Prioridade
- [ ] Tarefa Menor 1
- [ ] Tarefa Menor 2

## Coluna Concluído
- [x] Tarefa Finalizada
```

Neste exemplo, "Tarefas Prioritárias" e "Tarefas de Baixa Prioridade" aparecerão como subtítulos dentro da "Coluna de Tarefas", mantendo a estrutura do Kanban intacta.

## 🎯 Padrões e Entendimentos para o Projeto Recoloca.ai

Para garantir a consistência e a funcionalidade dos nossos Kanbans, seguiremos os seguintes padrões:

### 1. Estrutura de Colunas (Títulos `##`)

As colunas principais do Kanban (e, portanto, os títulos `##`) devem representar os estágios do fluxo de trabalho ou as fases do projeto:

- `## SESSÃO ATUAL (Em Progresso)`
- `## FASE 0: FUNDAÇÃO RAG + AGENTES`
- `## FASE 1: VALIDAÇÃO TÉCNICA E ESTRATÉGICA`
- `## BACKLOG (Não Priorizado)`
- `## CONCLUÍDO`

### 2. Organização Interna das Colunas (Títulos `###` ou `####`)

Para organizar tarefas ou informações dentro de uma coluna, utilize `###` (títulos de terceiro nível) ou `####` (títulos de quarto nível). **Nunca use `##` dentro de uma coluna existente.**

Exemplos:
```markdown
## FASE 0: FUNDAÇÃO RAG + AGENTES

### Configuração RAG
- [ ] Configurar ChromaDB
- [ ] Implementar pipeline de ingestão

### Agentes Tier 1
- [ ] Configurar Agent Mentor PM
- [ ] Configurar Agent Mentor UX/UI
```

### 3. Integração com Obsidian Tasks Plugin

O Obsidian Tasks Plugin oferece funcionalidades avançadas para gerenciamento de tarefas: <mcreference link="https://publish.obsidian.md/tasks/Introduction" index="1">1</mcreference>

#### Sintaxe de Tarefas:
- **Tarefas abertas:** `- [ ] Minha tarefa`
- **Tarefas concluídas:** `- [x] Minha tarefa`
- **Tarefas canceladas:** `- [-] Minha tarefa`

#### Metadados de Tarefas:
- **Datas de vencimento:** `📅 YYYY-MM-DD`
- **Datas de início:** `🛫 YYYY-MM-DD`
- **Datas de agendamento:** `⏳ YYYY-MM-DD`
- **Tarefas recorrentes:** `🔁 every week`
- **Prioridade:** `🔺` (alta), `⏫` (média), `🔽` (baixa)

#### Exemplo Completo:
```markdown
- [ ] Implementar autenticação JWT 📅 2024-01-15 🔺 #desenvolvimento #MVP
- [ ] Criar mockups da tela de login ⏳ 2024-01-10 ⏫ #design #UX
- [x] Configurar banco de dados ✅ 2024-01-05 #infraestrutura
```

### 4. Tags e Categorização

Utilize tags (`#`) de forma consistente para categorizar tarefas:

- **Por área:** `#desenvolvimento`, `#design`, `#arquitetura`, `#testes`
- **Por fase:** `#Fase0`, `#Fase1`, `#MVP`
- **Por componente:** `#RAG`, `#agentes`, `#frontend`, `#backend`
- **Por prioridade:** `#critico`, `#importante`, `#nice-to-have`

### 5. Links Internos e Referências

Sempre que referenciar outros documentos do projeto, utilize links internos do Obsidian:

```markdown
- [ ] Revisar [[docs/02_Requisitos/01_ERS.md|ERS]] para validar requisitos
- [ ] Implementar conforme [[docs/03_Arquitetura_e_Design/01_HLD.md|HLD]]
```

### 6. Transclusion e Embedding

O plugin Kanban permite transcluir colunas de outros quadros Kanban: <mcreference link="https://www.reddit.com/r/ObsidianMD/comments/rk45ig/help_previewing_linked_kanban_boards_as_boards/" index="3">3</mcreference>

```markdown
## Tarefas de Desenvolvimento
![[KANBAN_INTERNO_PROJETO#SESSÃO ATUAL (Em Progresso)]]
```

### 7. Visualização e Edição

O plugin Kanban oferece múltiplas formas de visualização: <mcreference link="https://www.xda-developers.com/how-i-use-kanban-boards-in-obsidian-to-manage-my-personal-projects/" index="5">5</mcreference>

- **Visualização Kanban:** Interface visual com colunas e cartões
- **Visualização Markdown:** Edição direta do código Markdown
- **Visualização Tabela:** Formato tabular para análise
- **Visualização Lista:** Formato de lista simples

## 🚀 Melhores Práticas

### ✅ Faça:
- Use `##` apenas para colunas principais
- Use `###` ou `####` para subseções dentro de colunas
- Mantenha tags consistentes em todo o projeto
- Utilize metadados do Tasks Plugin para rastreamento avançado
- Referencie documentos relacionados com links internos
- Mantenha a estrutura simples e funcional

### ❌ Evite:
- Usar `##` para subseções dentro de colunas
- Criar muitas colunas (máximo 6-8 para boa visualização)
- Tags inconsistentes ou muito específicas
- Estruturas muito complexas que dificultem a navegação
- Misturar diferentes padrões de organização no mesmo quadro

## 🔧 Configuração Recomendada

Para o projeto Recoloca.ai, utilizamos um sistema de **5 Kanbans especializados**:

### 📋 Kanbans Principais (Sempre Ativos):

1. **Kanban Operacional** (`01_KANBAN_OPERACIONAL_SESSOES.md`):
   - **Propósito:** Gestão diária de tarefas e sessões de trabalho
   - **Foco:** Tarefas da sessão atual e próximas ações
   - **Colunas:** Máximo 6 colunas para boa visualização
   - **Atualização:** Diária, a cada sessão de trabalho
   - **Responsáveis:** @Maestro, @AgenteM_Orquestrador

2. **Kanban Estratégico** (`02_KANBAN_ESTRATEGICO_FASES.md`):
   - **Propósito:** Visão de longo prazo organizada por fases do projeto
   - **Foco:** Objetivos estratégicos e marcos principais
   - **Organização:** Por fases (Fase 0, Fase 1, Fase 2, etc.)
   - **Atualização:** Semanal/quinzenal
   - **Responsáveis:** @Maestro, @AgenteM_Orquestrador

### 🎯 Kanbans Especializados (Ativados Conforme Demanda):

3. **Kanban Bugs & Issues** (`03_KANBAN_BUGS_ISSUES.md`):
   - **Quando usar:** Quando o volume de bugs justificar um quadro dedicado (pós-MVP)
   - **Propósito:** Gestão específica de bugs, issues técnicas e correções
   - **Organização:** Por prioridade (P0-P3) e status de resolução
   - **Responsáveis:** @AgenteM_DevFastAPI, @AgenteM_DevFlutter, @AgenteM_ArquitetoTI

4. **Kanban Research & Insights** (`04_KANBAN_RESEARCH_INSIGHTS.md`):
   - **Quando usar:** Para demanda contínua de pesquisas e validações (pós-MVP)
   - **Propósito:** Gestão de pesquisas de mercado, insights de usuário e descobertas estratégicas
   - **Organização:** Do backlog de pesquisas até insights implementados
   - **Responsáveis:** @AgenteM_Orquestrador, @AgenteM_UXDesigner, @Maestro

5. **Kanban Marketing & GTM** (`05_KANBAN_MARKETING_GTM.md`):
   - **Quando usar:** Pós-MVP, quando iniciar atividades de marketing e aquisição
   - **Propósito:** Gestão de atividades de marketing, go-to-market e crescimento
   - **Organização:** Do planejamento de campanhas até resultados implementados
   - **Responsáveis:** @Maestro, @AgenteM_Orquestrador, Marketing Team (futuro)

### 🔄 Diretrizes de Uso por Fase:

#### **Fase 0-1 (Atual):** 
- **Ativos:** Operacional + Estratégico
- **Foco:** Fundação RAG, configuração de agentes, validação técnica

#### **Fase 2 (MVP):**
- **Ativos:** Operacional + Estratégico + Bugs & Issues
- **Foco:** Desenvolvimento, testes, correções

#### **Fase 3+ (Pós-MVP):**
- **Ativos:** Todos os 5 Kanbans conforme demanda
- **Foco:** Crescimento, pesquisa contínua, marketing

### 🔗 Sincronização entre Kanbans:

- **Tags Consistentes:** Use o mesmo sistema de tags em todos os quadros
- **Transclusion:** Conecte quadros relacionados quando necessário
- **Cross-Reference:** Referencie tarefas entre quadros quando há dependências
- **Rotina de Sincronização:** Defina rotina regular de alinhamento entre quadros
- **Responsabilidade Compartilhada:** @AgenteM_Orquestrador mantém visão geral de todos os quadros

Ao seguir estas diretrizes, garantimos que nossos Kanbans sejam funcionais, organizados e compatíveis com as ferramentas do Obsidian, facilitando a gestão eficiente do projeto Recoloca.ai.

---

**Referências:**
- Obsidian Tasks Plugin Documentation
- Obsidian Kanban Plugin Documentation
- Comunidade Obsidian no Reddit

--- FIM DO DOCUMENTO COMO_USAR_KANBAN.md ---