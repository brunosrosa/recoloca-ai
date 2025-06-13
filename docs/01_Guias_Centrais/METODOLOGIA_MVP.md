---
sticker: lucide//lightbulb
---
# METODOLOGIA MVP: DESENVOLVIMENTO SOLO AUMENTADO POR IA

**Versão:** 1.0  
**Data de Criação:** 19 de dezembro de 2024  
**Status:** MVP - Essenciais  
**Baseado em:** [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v1.0)

## Visão Geral

### O Paradigma

O **"Desenvolvimento Solo Ágil Aumentado por IA"** é uma metodologia onde um desenvolvedor experiente (o "Maestro") orquestra múltiplos **Agentes Mentores de IA** especializados para simular e superar as capacidades de uma equipe tradicional.

### Objetivo Central

Criar um **framework replicável** de trabalho com multi-agentes de IA especializados que possam trabalhar de forma integrada e cada vez mais autônoma.

## Princípios Fundamentais

1. **Orquestração Inteligente**: Maestro coordena agentes especializados por domínio
2. **Especialização por Domínio**: Cada agente possui expertise específica e persona definida
3. **Documentação Viva**: Markdown + Obsidian + Git como fonte da verdade
4. **Human-in-the-Loop Evolutivo**: Supervisão diminui gradualmente conforme competência
5. **Iteração Contínua**: Feedback refina produto e metodologia

## Papéis Essenciais

### O Maestro
- **Visionário Estratégico**: Define objetivos e direção
- **Arquiteto de Prompts**: Cria instruções para agentes
- **Curador de Conhecimento**: Mantém documentação viva
- **Supervisor Adaptativo**: Ajusta nível de supervisão
- **Integrador Final**: Revisa e valida outputs

### O @AgenteOrquestrador (Papel Central)
- **PM Mentor Sênior** + **Engenheiro de Prompt**
- Parceiro estratégico principal do Maestro
- **Funções**:
  - Análise estratégica via RAG
  - Geração de perguntas esclarecedoras
  - Co-criação de prompts eficazes
  - Aplicação de frameworks de PM (RICE, MoSCoW)
  - Identificação de "componentes de núcleo"

## Estratégia de Evolução (3 Fases)

### Fase 1: Estruturação & Validação
- ✅ Documentação Viva como fonte da verdade
- ✅ Agentes com personas básicas
- ✅ Sistema RAG para contexto
- ✅ MVP com supervisão intensa

### Fase 2: Especialização & Automação
- 🔄 Refinamento de personas e capacidades
- 🔄 Workflows automatizados
- 🔄 Redução gradual de supervisão
- 🔄 Expansão além do MVP

### Fase 3: Supervisão Avançada
- ⏳ Auto-correção e aprendizado
- ⏳ Supervisão focada em estratégia
- ⏳ Otimização contínua
- ⏳ Replicação para novos projetos

## SDLC Ágil com Agentes

| Fase | Agentes Principais | Maestro |
|------|-------------------|----------|
| **Estratégia** | `@AgenteOrquestrador` | Define visão |
| **Requisitos** | `@AgenteOrquestrador` | Valida e refina |
| **Arquitetura** | `@AgenteM_ArquitetoTI`, `@AgenteMentorAPI` | Revisa decisões |
| **Desenvolvimento** | `@AgenteMentorDevFastAPI`, `@AgenteMentorDevFlutter` | Integra componentes |
| **Testes** | `@AgenteMentorQA`, `@AgenteMentorSeguranca` | Executa integração |
| **Deploy** | `@AgenteM_DevOps` | Supervisiona produção |

## Critérios de Maturidade dos Agentes

### Tier 1 - Básicos (Supervisão Intensa)
- **Precisão**: 70-80% corretos sem revisão
- **Documentação**: 80% dos padrões
- **Autonomia**: Tarefas simples com supervisão constante
- **RAG**: Contexto básico adequado
- **Estratégia**: Compreende objetivos gerais

### Tier 2 - Intermediários (Supervisão Moderada)
- **Precisão**: 85-90% corretos sem revisão
- **Documentação**: 90% dos padrões
- **Autonomia**: Tarefas complexas com supervisão ocasional
- **RAG**: Contexto avançado e conexões relevantes
- **Estratégia**: Questiona e sugere melhorias

### Tier 3 - Avançados (Supervisão Mínima)
- **Precisão**: 95%+ corretos sem revisão
- **Documentação**: 95%+ padrões + sugestões
- **Autonomia**: Auto-correção em tarefas complexas
- **RAG**: Uso criativo e inovador
- **Estratégia**: Contribuição proativa

## Stack Tecnológico RAG

**Status**: Planejado para pós-MVP

- **Framework**: LangChain (Python)
- **Vector Store**: FAISS-GPU (local, CUDA)
- **Embedding**: `BAAI/bge-m3`
- **Ambiente**: Conda + Python 3.10
- **Documentação**: Obsidian + Git + Markdown

## Ferramentas de Apoio

- **Trae IDE**: Ambiente principal para agentes
- **OpenRouter**: Gateway para modelos LLM
- **Obsidian**: Interface para documentação viva
- **Git**: Versionamento e colaboração
- **Pipedream**: Workflows automatizados

## Considerações Especiais

### Perfis Neurodivergentes
A metodologia foi projetada considerando:
- **Estrutura clara** → Reduz sobrecarga cognitiva
- **Delegação inteligente** → Foco em áreas de interesse
- **Flexibilidade** → Diferentes estilos de trabalho
- **Suporte executivo** → Via Agentes Mentores

### IA como Suporte
- **Assistentes executivos** para organização
- **Consultores estratégicos** para decisões
- **Parceiros de brainstorming** para criatividade
- **Sistemas de backup** para memória e contexto

## Recomendações Essenciais

1. **Iteração Contínua**: Refine prompts, personas e processos constantemente
2. **Engenharia de Prompt**: Invista tempo - é o multiplicador de força principal
3. **Curadoria Ativa**: Mantenha documentação viva atualizada
4. **HITL Evolutivo**: Ajuste supervisão conforme confiança aumenta
5. **Considerações Éticas**: Mantenha implicações éticas em mente
6. **Aprendizado Contínuo**: Documente lições aprendidas
7. **Replicabilidade**: Pense sempre em tornar o sistema replicável

## Estrutura de Documentação Mínima

```
Projeto/
├── .trae/rules/
│   ├── user_rules.md
│   └── project_rules.md
├── docs/
│   ├── 01_Guias_Centrais/
│   │   ├── PLANO_MESTRE.md
│   │   ├── METODOLOGIA_MVP.md
│   │   └── GLOSSARIO.md
│   ├── 02_Requisitos/
│   │   └── ERS.md
│   ├── 03_Arquitetura_e_Design/
│   │   ├── HLD.md
│   │   └── API_Specs/
│   ├── 04_Agentes_IA/
│   │   └── AGENTES_OVERVIEW.md
│   └── 05_Prompts/
│       └── 01_Templates_Base/
├── rag_infra/
│   └── source_documents/
└── src/
```

## Próximos Passos

### Para Implementação
1. **Definir personas** dos agentes principais
2. **Criar templates** de prompts básicos
3. **Estruturar documentação** viva inicial
4. **Configurar RAG** básico (pós-MVP)
5. **Estabelecer métricas** de qualidade

### Para Replicação
1. **Adaptar stack** tecnológico ao contexto
2. **Personalizar agentes** para domínio específico
3. **Ajustar critérios** de maturidade
4. **Definir workflows** específicos
5. **Estabelecer governança** de IA

---

**Nota**: Este é um documento vivo que evolui com a experiência prática. A verdadeira inovação vem da aplicação, experimentação e refinamento baseado em resultados reais.

--- FIM DO DOCUMENTO METODOLOGIA_MVP.md (v1.0) ---