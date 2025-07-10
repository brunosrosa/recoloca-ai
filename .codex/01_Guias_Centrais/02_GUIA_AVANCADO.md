---
sticker: lucide//check
---
# GUIA AVANÇADO PARA DESENVOLVIMENTO SOLO COM AGENTES DE IA MENTORES (Aplicado ao Projeto Recoloca.ai)

**Versão:** 1.1
**Data de Criação:** 28 de maio de 2025
**Data de Última Atualização:** Janeiro de 2025
**Status:** Aprovado
**Baseado em:**
- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.0)
- [[docs/02_Requisitos/01_ERS.md]] (v0.5)
- [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v0.9 - versão anterior)

## Introdução

Este documento apresenta o **"Guia Avançado para Desenvolvimento Solo com Agentes de IA Mentores"**, aplicado especificamente ao projeto **Recoloca.ai**. Representa a evolução de uma metodologia inovadora que combina desenvolvimento ágil solo com orquestração inteligente de Agentes de IA especializados.

### Paradigma do Desenvolvimento Solo Aumentado por IA

O desenvolvimento de software tradicionalmente depende de equipes multidisciplinares. Este guia propõe um paradigma alternativo: o **"Desenvolvimento Solo Ágil Aumentado por IA"**, onde um desenvolvedor experiente (o "Maestro") orquestra múltiplos **Agentes Mentores de IA** especializados para simular e superar as capacidades de uma equipe tradicional.

### Propósito e Escopo

Este guia serve como:
- **Manual metodológico** para implementação do paradigma de desenvolvimento solo aumentado por IA
- **Documentação viva** das práticas, ferramentas e processos específicos do Recoloca.ai
- **Framework replicável** para futuros projetos que adotem esta abordagem

### O Projeto Recoloca.ai como Testbed

O **Recoloca.ai** funciona como um laboratório prático para validar e refinar esta metodologia. É importante destacar que **este projeto é o output completo de um projeto anterior focado na "Metodologia"**, onde o objetivo principal é criar um **sistema replicável** de trabalho com multi-agentes de IA especializados que possam trabalhar de forma integrada e cada vez mais autônoma.

## Princípios Fundamentais

O framework "Desenvolvimento Solo Aumentado por IA" baseia-se em cinco princípios fundamentais:

1. **Orquestração Inteligente**: O Maestro atua como regente, coordenando Agentes de IA especializados em diferentes domínios (arquitetura, desenvolvimento, testes, documentação).

2. **Especialização por Domínio**: Cada Agente Mentor de IA possui expertise específica, persona definida e acesso contextual relevante via RAG (Retrieval-Augmented Generation).

3. **Documentação Viva**: Toda a documentação é mantida como "fonte da verdade" em formato Markdown no Obsidian, versionada com Git e integrada ao sistema RAG.

4. **Human-in-the-Loop (HITL) Evolutivo**: O nível de supervisão humana diminui gradualmente conforme os agentes demonstram competência e confiabilidade.

5. **Iteração Contínua**: Feedback constante refina tanto o produto quanto a metodologia, criando um ciclo de melhoria contínua.

## O Papel do "Maestro"

O **Maestro** (desenvolvedor principal) assume múltiplas responsabilidades:

- **Visionário Estratégico**: Define objetivos, prioridades e direção do produto
- **Arquiteto de Prompts**: Cria e refina instruções para os Agentes Mentores de IA
- **Curador de Conhecimento**: Mantém e evolui a "Documentação Viva" e a base RAG
- **Supervisor Adaptativo**: Ajusta o nível de supervisão conforme a maturidade dos agentes
- **Integrador Final**: Revisa, integra e valida todas as saídas dos agentes

## Estratégia de Evolução Gradual

A implementação segue uma abordagem de três fases:

### Fase 1: Estruturação & Validação (Atual)
- Estabelecimento da "Documentação Viva" como fonte da verdade
- Configuração inicial dos Agentes Mentores de IA com personas básicas
- Implementação do sistema RAG para contexto inteligente
- Validação do MVP com supervisão intensa

### Fase 2: Especialização & Automação
- Refinamento das personas e capacidades dos agentes
- Implementação de workflows automatizados
- Redução gradual da supervisão para tarefas validadas
- Expansão das funcionalidades além do MVP

### Fase 3: Supervisão Avançada
- Agentes capazes de auto-correção e aprendizado
- Supervisão focada em decisões estratégicas
- Otimização contínua baseada em métricas de performance
- Replicação da metodologia para novos projetos

## SDLC Ágil Adaptado com Agentes Mentores de IA

O ciclo de desenvolvimento integra Agentes de IA em cada fase:

### Concepção e Estratégia
- **`@AgenteM_Orquestrador`**: Atua como PM Mentor, validando estratégia e criando prompts eficazes
- **Maestro**: Define visão e objetivos estratégicos

### Análise e Requisitos
- **`@AgenteM_Orquestrador`**: Gera Histórias de Usuário e Critérios de Aceite
- **Maestro**: Valida e refina requisitos

### Design e Arquitetura
- **`@AgenteM_ArquitetoTI`**: Cria HLD, LLD e diagramas arquiteturais
- **`@AgenteMentorAPI`**: Especifica APIs em OpenAPI 3.0
- **Maestro**: Revisa e aprova decisões arquiteturais

### Implementação
- **`@AgenteMentorDevFastAPI`**: Desenvolve backend Python/FastAPI
- **`@AgenteMentorDevFlutter`**: Desenvolve frontend Flutter/Dart
- **`@AgenteMentorDevJS`**: Desenvolve extensão Chrome (Pós-MVP)
- **Maestro**: Integra e testa componentes

### Testes e Qualidade
- **`@AgenteMentorQA`**: Gera planos e casos de teste
- **`@AgenteMentorSeguranca`**: Revisa segurança e conformidade
- **Maestro**: Executa testes de integração

### Deploy e Monitoramento
- **`@AgenteM_DevOps`**: Automatiza deploy e monitoramento
- **Maestro**: Supervisiona produção

### Documentação e Manutenção
- **`@AgenteMentorDocumentacao`**: Mantém documentação técnica
- **Todos os Agentes**: Contribuem para a "Documentação Viva"

## O `@AgenteM_Orquestrador`: PM Mentor e Orquestrador de Prompts

O **`@AgenteM_Orquestrador`** possui papel central e expandido:

### Persona e Objetivos
- **Product Manager Mentor Sênior** e **Engenheiro de Prompt Especialista**
- Parceiro estratégico principal do Maestro
- Foco duplo: mentoria em PM + engenharia de prompts

### Funcionalidades Principais

#### 1. Análise Estratégica via RAG
- Consulta ativa à "Documentação Viva" para embasar análises
- Acesso a materiais de Product Management em `[[rag_infra/source_documents/PM_Knowledge/]]`
- Validação de alinhamento com objetivos do produto

#### 2. Geração de Perguntas Esclarecedoras
- Questiona premissas antes de assumir verdades
- Explora direções alternativas e pontos cegos
- Atua como "advogado do diabo" construtivo

#### 3. Criação Assistida de Prompts Eficazes
- Co-criação de prompts contextualizados para outros agentes
- Aplicação de melhores práticas de engenharia de prompt
- Utilização de templates em `[[docs/05_Prompts/01_Templates_Base/]]`

#### 4. Frameworks de Product Management
- Aplicação de RICE, ICE, MoSCoW para priorização
- Análise de valor para usuário e alinhamento estratégico
- Identificação de "componentes de núcleo" do projeto

## Critérios Objetivos para Agentes "Production-Ready" e Métricas de "Specialized Intelligence"

Para definir quando um Agente Mentor de IA está pronto para produção, estabelecemos critérios objetivos organizados em três tiers, complementados por métricas específicas de "Specialized Intelligence":

### Tier 1 - Agentes Básicos (Supervisão Intensa)
- **Precisão Técnica**: 70-80% de outputs corretos sem revisão
- **Consistência de Documentação**: Segue 80% dos padrões estabelecidos
- **Autonomia Operacional**: Executa tarefas simples com supervisão constante
- **Integração RAG**: Utiliza contexto básico adequadamente
- **Alinhamento Estratégico**: Compreende objetivos gerais do projeto

### Tier 2 - Agentes Intermediários (Supervisão Moderada)
- **Precisão Técnica**: 85-90% de outputs corretos sem revisão
- **Consistência de Documentação**: Segue 90% dos padrões estabelecidos
- **Autonomia Operacional**: Executa tarefas complexas com supervisão ocasional
- **Integração RAG**: Utiliza contexto avançado e faz conexões relevantes
- **Alinhamento Estratégico**: Questiona e sugere melhorias alinhadas

### Tier 3 - Agentes Avançados (Supervisão Mínima)
- **Precisão Técnica**: 95%+ de outputs corretos sem revisão
- **Consistência de Documentação**: Segue 95%+ dos padrões e sugere melhorias
- **Autonomia Operacional**: Executa tarefas complexas com auto-correção
- **Integração RAG**: Utiliza contexto de forma criativa e inovadora
- **Alinhamento Estratégico**: Contribui proativamente para estratégia

### Métricas de "Specialized Intelligence" para Orquestração

#### Eficiência de Orquestração
- **Tempo de Resposta dos Agentes**: < 30 segundos para consultas simples, < 2 minutos para análises complexas
- **Taxa de Automação**: % de tarefas executadas sem intervenção manual (Meta: 70% Tier 1, 85% Tier 2, 95% Tier 3)
- **Precisão de Handoffs**: % de transferências bem-sucedidas entre agentes (Meta: >90%)

#### Qualidade do Sistema RAG
- **Precisão de Retrieval**: % de documentos relevantes recuperados (Meta: >85%)
- **Cobertura da Base RAG**: % da documentação indexada e atualizada (Meta: >95%)
- **Tempo de Indexação**: Tempo para processar novos documentos (Meta: < 5 minutos)

#### Satisfação e Produtividade
- **Satisfação do Maestro**: Escala 1-10 com feedback sobre utilidade dos agentes (Meta: >8)
- **Redução de Context Switching**: % de redução em mudanças de ferramenta (Meta: >60%)
- **Aceleração de Desenvolvimento**: Fator de multiplicação da produtividade (Meta: 2-3x)

## Estratégia RAG (Retrieval-Augmented Generation)

**Nota**: A implementação completa do sistema RAG está planejada para **pós-MVP**, priorizando inicialmente a estruturação da "Documentação Viva" e validação dos agentes.

### Tecnologias e Arquitetura
- **Framework**: LangChain (Python)
- **Vector Store**: FAISS-GPU (local, utilizando CUDA)
- **Modelo de Embedding**: `BAAI/bge-m3` (via Sentence Transformers)
- **Ambiente**: Conda com Python 3.10

### Processo de Indexação
1. **Curadoria**: Seleção manual de documentos relevantes
2. **Processamento**: Chunking inteligente preservando contexto
3. **Embedding**: Geração de vetores semânticos
4. **Indexação**: Armazenamento otimizado no FAISS

### Processo de Query
1. **Análise da Query**: Compreensão da intenção do usuário
2. **Retrieval**: Busca por similaridade semântica
3. **Ranking**: Ordenação por relevância e contexto
4. **Augmentation**: Enriquecimento do prompt com contexto recuperado

### "Documentação Viva" com Obsidian e Git
- **Obsidian**: Interface rica para criação e navegação
- **Git**: Versionamento e colaboração
- **Markdown**: Formato padrão para máxima compatibilidade
- **Links Internos**: Conectividade semântica entre documentos

## Ferramentas de Apoio

### Trae IDE
- **Ambiente principal** para interação com Agentes Mentores de IA
- **Integração nativa** com modelos via OpenRouter
- **Contexto inteligente** via `#Context` e MCPs

### OpenRouter
- **Gateway unificado** para múltiplos modelos LLM
- **Google Gemini Pro/Flash** como modelos primários
- **Fallbacks** para garantir disponibilidade

### Pipedream
- **Automação de workflows** entre ferramentas
- **Integrações** com Supabase, GitHub, etc.
- **Triggers** baseados em eventos do projeto

### FlutterFlow (Opcional)
- **Prototipagem rápida** de interfaces
- **Geração de código** Flutter inicial
- **Validação visual** com stakeholders

## Convenções de Gerenciamento de Tarefas (Kanban)

### Formato de ID de Tarefa
`[ATIVIDADE]-[DOMINIO]-[NUMERO]`

**Exemplos:**
- `DEV-KAN-001`: Desenvolvimento do módulo Kanban
- `API-AUTH-002`: Especificação da API de autenticação
- `TST-CV-003`: Testes do módulo de CV

### Tipos de Atividade
- **API**: Especificação de APIs
- **ARQ**: Arquitetura e design
- **DEV**: Desenvolvimento/implementação
- **DOC**: Documentação
- **INF**: Infraestrutura e DevOps
- **PRO**: Prototipagem
- **TST**: Testes e QA

### Domínios de Aplicação
- **GER**: Gerenciamento geral
- **KAN**: Módulo Kanban
- **AUTH**: Autenticação
- **CV**: Análise de CV
- **COA**: Coach IA
- **PAY**: Pagamentos
- **IMP**: Importação de dados
- **RAG**: Sistema RAG
- **AGT**: Agentes de IA

### Estados de Tarefa
- `[ ]` **A Fazer**: Tarefa identificada, não iniciada
- `[x]` **Concluída**: Tarefa finalizada e validada

### Workflow
1. **Identificação**: Maestro ou `@AgenteM_Orquestrador` identifica necessidade
2. **Priorização**: Aplicação de frameworks (RICE, MoSCoW)
3. **Atribuição**: Delegação para Agente Mentor apropriado
4. **Execução**: Desenvolvimento com supervisão adequada
5. **Validação**: Revisão e aprovação pelo Maestro
6. **Integração**: Incorporação ao projeto principal

### Critérios de Priorização
- **Dependências**: Tarefas bloqueantes têm prioridade
- **Valor MVP**: Alinhamento com objetivos do MVP
- **Risco**: Tarefas de alto risco são priorizadas
- **Esforço vs. Impacto**: Análise custo-benefício

### Organização no Arquivo
- **Seções por Estado**: Agrupamento visual claro
- **Tags de Prioridade**: `#alta`, `#media`, `#baixa`
- **Links para Documentos**: Rastreabilidade completa

### Integração com Agentes de IA
- **Referência em Prompts**: IDs de tarefa em contexto
- **Consulta pelo `@AgenteM_Orquestrador`**: Análise de prioridades
- **Atualização Automática**: Via Pipedream quando possível

### Sincronização com Obsidian Kanban Plugin
- **Plugin nativo** para visualização kanban
- **Sincronização bidirecional** com arquivo Markdown
- **Filtros e views** customizáveis

### Evolução e Refinamento
As convenções evoluem baseadas em:
- **Feedback do uso prático**
- **Necessidades emergentes do projeto**
- **Melhores práticas identificadas**
- **Integração com novas ferramentas**

## Human-in-the-Loop (HITL) Evolutivo

O processo HITL evolui em três fases distintas:

### Fase 1: Supervisão Intensa
- **Revisão de 100%** dos outputs dos agentes
- **Feedback detalhado** para refinamento
- **Ajustes frequentes** de prompts e personas
- **Validação manual** de todas as decisões

### Fase 2: Autonomia Guiada
- **Revisão seletiva** baseada em confiança
- **Delegação de tarefas** de baixo risco
- **Monitoramento de métricas** de qualidade
- **Intervenção quando necessário**

### Fase 3: Controle Supervisório
- **Supervisão estratégica** apenas
- **Auto-correção** dos agentes
- **Foco em inovação** e direção
- **Escalabilidade** para novos projetos

## Considerações para Desenvolvedores Neurodivergentes

Esta metodologia foi especialmente projetada considerando perfis neurodivergentes:

### Alinhamento com ADHD
- **Estrutura clara** reduz sobrecarga cognitiva
- **Delegação inteligente** permite foco em áreas de interesse
- **Feedback imediato** mantém engajamento
- **Flexibilidade** para diferentes estilos de trabalho

### Alinhamento com Superdotação
- **Complexidade intelectual** através da orquestração
- **Múltiplas perspectivas** via diferentes agentes
- **Aprendizado contínuo** através da iteração
- **Autonomia criativa** com suporte estruturado

### Ferramentas e Técnicas de Apoio

#### Obsidian
- **Pensamento não-linear** através de links
- **Visualização de conexões** entre conceitos
- **Organização flexível** adaptável ao estilo pessoal

#### Trae IDE
- **Interface unificada** reduz context switching
- **Agentes especializados** para diferentes necessidades
- **Automação** de tarefas repetitivas

#### Pipedream
- **Workflows automatizados** reduzem carga mental
- **Integrações** seamless entre ferramentas
- **Triggers** baseados em eventos

#### Técnicas de Gestão de Tempo
- **Pomodoro adaptado** com pausas flexíveis
- **Time-boxing** para tarefas específicas
- **Batching** de atividades similares

### IA como Suporte Executivo e Estratégico

Os Agentes Mentores de IA funcionam como:
- **Assistentes executivos** para organização
- **Consultores estratégicos** para decisões
- **Parceiros de brainstorming** para criatividade
- **Sistemas de backup** para memória e contexto

## Conclusão

Este guia representa a evolução de uma metodologia inovadora que combina as melhores práticas do desenvolvimento ágil com o poder transformador da IA. O **Recoloca.ai** serve como laboratório para validar e refinar esta abordagem, mas o objetivo maior é criar um **framework replicável** para futuros projetos.

### Origem e Propósito

É importante reforçar que **este projeto é o output completo de um projeto anterior focado na "Metodologia"**. O objetivo principal não é apenas desenvolver o Recoloca.ai, mas criar e validar um **sistema replicável** de trabalho com multi-agentes de IA especializados que possam trabalhar de forma integrada e cada vez mais autônoma.

### Alinhamento com Perfis Neurodivergentes

A metodologia foi especialmente projetada considerando as necessidades e fortalezas de desenvolvedores neurodivergentes, oferecendo:
- **Estrutura clara** que reduz sobrecarga cognitiva
- **Delegação inteligente** que permite foco em áreas de interesse
- **Flexibilidade** para diferentes estilos de trabalho
- **Suporte executivo** através dos Agentes Mentores de IA

### Recomendações Chave para o Maestro

1. **Iteração Contínua**: Refine constantemente prompts, personas e processos baseado no feedback prático

2. **Engenharia de Prompt**: Invista tempo na criação de prompts eficazes - é o multiplicador de força mais importante

3. **Curadoria Ativa**: Mantenha a "Documentação Viva" atualizada e relevante - é a base de todo o sistema

4. **HITL Evolutivo**: Ajuste gradualmente o nível de supervisão conforme a confiança nos agentes aumenta

5. **Considerações Éticas**: Mantenha sempre em mente as implicações éticas do uso de IA, especialmente em decisões que afetam usuários

6. **Aprendizado Contínuo**: Documente lições aprendidas e evolua a metodologia baseado na experiência prática

7. **Replicabilidade**: Pense sempre em como tornar o sistema mais replicável para futuros projetos

A jornada do desenvolvimento solo aumentado por IA está apenas começando. Este guia fornece a base sólida, mas a verdadeira inovação virá da aplicação prática, experimentação contínua e refinamento baseado em resultados reais.

## Apêndice A: Estrutura de Pastas do Projeto

```
Recoloca.AI/
├── .git/ # Diretório do Git (gerenciado pelo sistema)
├── .obsidian/ # Configurações do Obsidian (gerenciado pelo Obsidian)
├── .trae/ # Configurações do Trae IDE
│ └── rules/
│ ├── user_rules.md # Regras de IA de nível de usuário/preferências
│ └── project_rules.md # Regras de IA específicas do projeto Recoloca.ai
├── docs/ # Documentação principal do projeto
│ ├── 00_Gerenciamento_Projeto/
│ │ ├── 01_TAP.md # Termo de Abertura do Projeto
│ │ ├── 02_ROADMAP_TEMPORAL_RECOLOCA_AI.md # Roadmap temporal
│ │ ├── 03_PGE.md # Plano de Gerenciamento do Escopo
│ │ ├── 04_PGC.md # Plano de Gerenciamento de Custos
│ │ ├── 05_PGP.md # Plano de Gerenciamento do Projeto
│ │ ├── 06_PGQ.md # Plano de Gerenciamento da Qualidade
│ │ ├── 07_PGR.md # Plano de Gerenciamento de Riscos
│ │ ├── 08_PCom.md # Plano de Gerenciamento das Comunicações
│ │ ├── 09_PStakeholders.md # Plano de Gerenciamento dos Stakeholders
│ │ ├── 10_Maestro_Tasks.md # Tarefas específicas do Maestro
│ │ ├── 11_CAMINHO_CRITICO_MVP.md # Caminho crítico do MVP
│ │ ├── KANBAN/ # Pasta com arquivos Kanban
│ │ └── TEMPLATE_PRD_ClaudeTaskMaster.txt # Template PRD
│ ├── 01_Guias_Centrais/
│ │ ├── 01_PLANO_MESTRE_RECOLOCA_AI.md # Documento estratégico central
│ │ ├── 02_GUIA_AVANCADO.md # Metodologia de Dev Solo com IA (este doc)
│ │ ├── 03_METODOLOGIA_MVP.md # Metodologia específica do MVP
│ │ ├── 04_TRAE_IDE_BEST_PRACTICES.md # Melhores práticas Trae IDE
│ │ ├── 05_PLANO_VALIDACAO_PREMISSAS_NEGOCIO.md # Validação de premissas
│ │ ├── 06_VANTAGENS_COMPETITIVAS_SUSTENTAVEIS.md # Vantagens competitivas
│ │ └── 07_GLOSSARIO_Recoloca_AI.md # Termos e definições do projeto
│ ├── 02_Requisitos/
│ │ ├── 01_ERS.md # Especificação de Requisitos de Software
│ │ ├── 02_HU_AC/ # Histórias de Usuário e Critérios de Aceite
│ │ ├── 03_MAPEAMENTO_DEPENDENCIAS_RF.md # Mapeamento de dependências
│ │ └── 04_PRIORIZACAO_RICE_RF.md # Priorização RICE
│ ├── 03_Arquitetura_e_Design/
│ │ ├── 02_ADRs/ # Registros de Decisão Arquitetural
│ │ ├── 00_API_Specs/ # Especificações de API
│ │ ├── 01_HLD.md # High-Level Design da Arquitetura
│ │ ├── 03_LLDs/ # Low-Level Design por módulo
│ │ ├── 03_STYLE_GUIDE.md # Guia de Estilo Visual e de UX Writing
│ │ ├── 04_FLUXO_TRABALHO_GERAL.md # Diagrama do fluxo de desenvolvimento
│ │ ├── 05_SISTEMA_ENTREGAVEIS_GATILHOS.md # Sistema de entregáveis
│ │ └── 06_ESTRATEGIA_MOMENTO_AHA.md # Estratégia momento Aha
│ ├── 04_Agentes_IA/
│ │ ├── 00_Templates_Modelos/ # Templates e modelos
│ │ ├── 01_Perfis/ # Perfis individuais dos agentes
│ │ ├── 02_AGENTES_IA_MENTORES_OVERVIEW.md # Visão geral dos agentes
│ │ ├── 03_FLUXO_ORQUESTRACAO_AGENTES.md # Fluxo de orquestração
│ │ └── 04_EVOLUCAO_FUTURA_AGENTE_ORQUESTRADOR.md # Evolução futura
│ ├── 05_Prompts/
│ │ ├── 00_Prompts_Estruturais_Agentes/ # Prompts estruturais
│ │ ├── 01_Templates_Base/ # Templates genéricos de prompts
│ │ └── 02_Prompts_Especificos/ # Prompts complexos e reutilizáveis
│ ├── 06_Qualidade_e_Testes/
│ │ └── Casos_de_Teste/ # Casos de teste
│ ├── 07_Metricas_e_Analytics/
│ │ └── METRICAS_SUCESSO_BASE_MERCADO.md # Métricas de sucesso
│ ├── 07_Operacoes_e_Deploy/
│ │ ├── ESTRATEGIA_DEVOPS.md # Estratégia DevOps
│ │ ├── GUIA_DEPLOY_BACKEND.md # Deploy backend
│ │ ├── GUIA_DEPLOY_EXTENSAO.md # Deploy extensão
│ │ └── GUIA_DEPLOY_FRONTEND.md # Deploy frontend
│ ├── 08_Marketing_e_Vendas/
│ │ └── ESTRATEGIA_GO_TO_MARKET.md # Estratégia Go-to-Market
│ ├── 09_Pesquisa_e_Insights/ # Notas de pesquisa, artigos, etc.
│ └── 10_Agentes_Learning/ # Aprendizado dos agentes
├── rag_infra/ # Arquivos base da infra do RAG para Agentes
│ └── core_logic/ # Scripts base da infra do RAG
│ │ └── rag_indexer.py
│ │ └── rag_retriever.py
│ │ └── verifica_faiss_gpu.py
│ └── index_store/ # Index criado para o RAG
│ │ └── Index (?)
│ └── notebooks/ # ???
│ │ └── (arquivos de notebooks?)
│ └── source_documents/ # Documentos base para o RAG
│ │ └── GUIA_AVANCADO_para_RAG.md 
│ │ └── API_Specs_Sumario_para_RAG.md
│ │ └── ERS_para_RAG.md
│ │ └── HLD_para_RAG.md
│ │ └── STYLE_GUIDE_para_RAG.md
│ │ └── PM_Knowledge/ # Pasta com documentos para o Agente PM (Product Manager)
│ │ │ └── (arquivos diversos)
│ └── environment.yml # Definição do Ambiente de RAG exportado do Conda
├── logs/ # Logs gerados por scripts ou processos (se aplicável localmente)
│ └── (arquivos de log)
├── scripts/ # Scripts de automação do projeto
│ └── (arquivos de scripts)
├── src/ # Código-fonte da aplicação
│ ├── backend_fastapi/ # Código do backend em FastAPI
│ ├── frontend_flutter/ # Código do frontend PWA em Flutter
│ └── chrome_extension_js/ # Código da extensão Chrome (Pós-MVP)
└── README.md # README principal do projeto (no Git)
```

## Apêndice B: Tabela Essencial - Papéis dos Agentes Mentores de IA

Esta tabela resume os Agentes de IA Mentores. A principal mudança é o papel expandido do `@AgenteM_Orquestrador`.

| **Fase do SDLC Ágil** | **Agente Mentor de IA (Trae IDE)** | **Principais Tarefas Assistidas para Recoloca.ai** | **Ferramentas/Modelos de IA Chave** | **Contexto RAG Primário** |
| -------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Estratégia e Orquestração** | `@AgenteM_Orquestrador`              | **Atuar como PM Mentor:** Auxiliar o Maestro a validar estratégia de features, alinhar com objetivos, usar frameworks de PM. **Engenharia de Prompt:** Analisar docs (RAG), gerar perguntas, criar prompts eficazes. | Google Gemini (Pro via OpenRouter), Trae IDE, LangChain/FAISS (via RAG)                       | Toda a "Documentação Viva" (ERS, Plano Mestre, etc.), Materiais de PM em [[rag_infra/source_documents/PM_Knowledge/]]                        |
| **Definição de Requisitos** | `@AgenteM_Orquestrador`              | Gerar Histórias de Usuário e Critérios de Aceite (em [[docs/02_Requisitos/02_HU_AC/]]) a partir da [[docs/02_Requisitos/01_ERS.md]] (v0.5), **considerando o alinhamento estratégico e validação de PM**.                        | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/02_Requisitos/01_ERS.md]] (v0.5), [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5), Base de conhecimento PM_Knowledge                     |
| **Arquitetura Completa (HLD + LLD)** | `@AgenteM_ArquitetoTI`        | Criar/refinar [[docs/03_Arquitetura_e_Design/01_HLD.md]], diagramas de arquitetura (Mermaid.js), definir interações entre módulos, detalhar classes, funções, modelos de dados para módulos em [[docs/03_Arquitetura_e_Design/03_LLDs/]], diagramas de sequência/classes (Mermaid.js).                                                                                           | Google Gemini (Pro via OpenRouter), Trae IDE, Mermaid.js                                      | [[docs/02_Requisitos/01_ERS.md]] (v0.5), [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.5)                                                       |
| **Especificação de API** | `@AgenteMentorAPI`                 | Gerar/manter especificações OpenAPI 3.0 (ex: [[docs/03_Arquitetura_e_Design/00_API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]).                                                                                                     | Google Gemini (Pro via OpenRouter), Trae IDE                                                  | [[docs/02_Requisitos/01_ERS.md]] (v0.5), [[docs/03_Arquitetura_e_Design/01_HLD.md]]                                                                             |
| **Desenvolvimento Backend** | `@AgenteMentorDevFastAPI`          | Gerar código Python/FastAPI para endpoints, lógica de negócios, interação com Supabase, testes unitários (pytest).                                                                                                   | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/03_Arquitetura_e_Design/00_API_Specs/RecolocaAPI_v1_OpenAPI.yaml]], [[docs/03_Arquitetura_e_Design/03_LLDs/]], Padrões Seguros                            |
| **Desenvolvimento Frontend** | `@AgenteMentorDevFlutter`          | Criar widgets Flutter/Dart, lógica de UI, gerenciamento de estado (Provider/Riverpod), chamadas à API, testes.                                                                                                       | Google Gemini (Pro/Flash via OpenRouter), Trae IDE, (Opcional: FlutterFlow para prototipagem) | [[docs/03_Arquitetura_e_Design/00_API_Specs/RecolocaAPI_v1_OpenAPI.yaml]], [[docs/03_Arquitetura_e_Design/03_LLDs/]], [[docs/03_Arquitetura_e_Design/03_STYLE_GUIDE.md]] |
| **Desenvolvimento Extensão (Pós-MVP)** | `@AgenteMentorDevJS`               | Implementar lógica de extração de dados (JS), comunicação com backend, UI da extensão.                                                                                                                               | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/02_Requisitos/01_ERS.md]] (v0.5 - seção da extensão), [[docs/03_Arquitetura_e_Design/00_API_Specs/RecolocaAPI_v1_OpenAPI.yaml]]                          |
| **Testes e QA** | `@AgenteMentorQA`                  | Gerar planos de teste ([[docs/06_Qualidade_e_Testes/01_PGQ.md]]), casos de teste (Gherkin em [[docs/06_Qualidade_e_Testes/Casos_de_Teste/]]), scripts de testes unitários/integração.                                             | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | [[docs/02_Requisitos/01_ERS.md]] (v0.5), [[docs/02_Requisitos/02_HU_AC/]], [[docs/03_Arquitetura_e_Design/03_LLDs/]]                                                     |
| **Documentação** | `@AgenteMentorDocumentacao`        | Gerar comentários/docstrings, explicar algoritmos, auxiliar na manutenção da "Documentação Viva" e curadoria da base RAG ([[rag_infra/source_documents/]]).                                                       | Google Gemini (Pro/Flash via OpenRouter), Trae IDE                                            | Código-fonte, [[docs/02_Requisitos/01_ERS.md]] (v0.5), [[docs/03_Arquitetura_e_Design/01_HLD.md]], [[docs/03_Arquitetura_e_Design/03_LLDs/]]                             |
| **Segurança** | `@AgenteMentorSeguranca`           | Revisar código e design (OWASP Top 10, OWASP LLM Top 10, LGPD), instruir sobre práticas seguras.                                                                                                                     | Google Gemini (Pro via OpenRouter), Trae IDE                                                  | [[docs/02_Requisitos/01_ERS.md]] (v0.5 - seção de segurança), Padrões de Código Seguro, Documentação OWASP                                              |

## Apêndice C: Exemplos de Prompts Base para Agentes

Os templates de prompts detalhados e específicos para cada agente e tarefa são gerenciados na pasta [[docs/05_Prompts/01_Templates_Base/]] e [[docs/05_Prompts/02_Prompts_Especificos/]] dentro do vault do Obsidian.

A estrutura geral de um template de prompt (conforme [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] v1.5, Seção 7.2) inclui:

1.  **Metadados:** Agente Alvo, Versão, Objetivo.
2.  **PERSONA DO AGENTE:** Instruções sobre papel, expertise, tom de voz, interação com RAG.
3.  **CONTEXTO FORNECIDO:** Placeholders para links (`[[Arquivo.md#Cabeçalho]]`) e input do Maestro.
4.  **TAREFA DETALHADA:** Descrição passo a passo.
5.  **RESTRIÇÕES E DIRETRIZES:** O que NÃO fazer, padrões, segurança.
6.  **FORMATO DE SAÍDA ESPERADO:** Estrutura, exemplos (few-shot), tipo de artefato.

**Exemplo Conceitual de Interação (Maestro para `@AgenteM_Orquestrador` com foco em PM):**

**Maestro:** "`@AgenteM_Orquestrador`, estou considerando o `RF-KAN-005` (Dashboard de Métricas Pessoais) da [[docs/02_Requisitos/01_ERS.md]] v0.5 para a próxima sprint. Ajude-me a validar a estratégia e depois criar as HUs e ACs."

`@AgenteM_Orquestrador` (como PM Mentor e PO, após consulta RAG): "Ótimo, Maestro! O `RF-KAN-005` parece alinhar-se com a dor do usuário sobre 'falta de visibilidade do progresso'. Antes de detalharmos as HUs:

1.  Qual o **principal Job-To-Be-Done** que este dashboard resolve para o nosso profissional de TI? É 'ajudar-me a entender onde estou falhando para melhorar' ou 'dar-me uma sensação de controle e progresso'? A clareza aqui impactará as métricas prioritárias.
2.  Considerando nossos concorrentes (conforme pesquisa), qual seria o **diferencial chave** do nosso dashboard de métricas? Seria a simplicidade, a profundidade dos insights ou a integração com o Coach IA?
3.  Quais **1-2 métricas de sucesso** para _esta feature específica_ nos indicariam que ela está entregando valor? (Ex: % de usuários que acessam o dashboard semanalmente, ou uma melhoria na taxa de conversão do funil do usuário após X tempo de uso).
4.  Pensando em MVP para este dashboard, quais são as 2-3 métricas absolutamente essenciais que precisamos exibir para validar a hipótese de valor, versus métricas 'nice-to-have' que podem vir depois? (Podemos usar MoSCoW aqui).
    Após alinharmos esses pontos estratégicos, posso criar as HUs e ACs detalhadas para o MVP deste dashboard, garantindo rastreabilidade e testabilidade."

## Histórico de Versões

### v1.1 - Janeiro 2025 (Orquestração Inteligente e Specialized Intelligence)
**Melhorias Implementadas:**
- **Métricas de "Specialized Intelligence"**: Adicionadas métricas específicas para orquestração de agentes IA, qualidade do sistema RAG e produtividade
- **Critérios Objetivos Expandidos**: Complementados os tiers de agentes com métricas quantificáveis de eficiência e qualidade
- **Framework de Medição**: Estabelecidas metas específicas para tempo de resposta, taxa de automação e precisão de handoffs
- **Indicadores de Produtividade**: Definidas métricas para satisfação do Maestro, redução de context switching e aceleração de desenvolvimento
- **Alinhamento Metodológico**: Sincronização com outros documentos chave do projeto (KANBAN_INTERNO_PROJETO.md, TAP.md, PStakeholders.md)
- **Consolidação da Metodologia**: Reforço dos conceitos de "Orquestração Inteligente" e "Specialized Intelligence" como pilares centrais

### v1.0 - Dezembro 2024 (Versão Base)
**Características Principais:**
- Framework "Desenvolvimento Solo Ágil Aumentado por IA"
- Definição de papéis dos Agentes Mentores de IA
- Estratégia RAG e "Documentação Viva"
- Processo HITL (Human-in-the-Loop) Evolutivo
- Considerações para desenvolvedores neurodivergentes
- Estrutura de pastas e convenções do projeto

## Documentos Relacionados

### Documentos de Gestão
- [[docs/00_Gerenciamento_Projeto/KANBAN/]] - Kanban principal com metodologia de orquestração
- [[docs/00_Gerenciamento_Projeto/01_TAP.md]] - Termo de Abertura com agentes IA integrados
- [[docs/00_Gerenciamento_Projeto/09_PStakeholders.md]] - Gestão de stakeholders com IA
- [[docs/00_Gerenciamento_Projeto/10_Maestro_Tasks.md]] - Tarefas específicas do Maestro

### Documentos Técnicos
- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica e objetivos
- [[docs/02_Requisitos/01_ERS.md]] - Especificação de requisitos
- [[docs/03_Arquitetura_e_Design/01_HLD.md]] - Arquitetura de alto nível
- [[docs/04_Agentes_IA/02_AGENTES_IA_MENTORES_OVERVIEW.md]] - Visão geral dos agentes

### Perfis de Agentes
- [[docs/04_Agentes_IA/01_Perfis/]] - Perfis individuais dos agentes especializados
- [[docs/05_Prompts/01_Templates_Base/]] - Templates de prompts para agentes

---

**Nota de Atualização:** Este documento foi atualizado para integrar completamente a metodologia de "Orquestração Inteligente" e "Specialized Intelligence", estabelecendo métricas quantificáveis para avaliar a eficácia dos agentes IA e do sistema RAG no contexto do projeto Recoloca.ai.

--- FIM DO DOCUMENTO GUIA_AVANCADO.md (v1.1) ---