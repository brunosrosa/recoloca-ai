---
rag_metadata:
  document_type: "technical_guide"
  category: "development_tools"
  priority: "high"
  last_updated: "2025-06-12"
  version: "2.0"
  tags: ["trae_ide", "ai_agents", "rag", "orchestration", "best_practices", "configuration"]
  cross_references:
    - "AGENTES_IA_MENTORES_OVERVIEW_para_RAG.md"
    - "PLANO_MESTRE_RECOLOCA_AI_para_RAG.md"
    - "HLD_para_RAG.md"
    - "KANBAN_ESTRATEGICO_FASES_para_RAG.md"
  search_keywords: ["trae ide", "agentes ia", "configuração", "orquestração", "rag integration", "testing", "debugging", "prompts", "context management"]
---

# TRAE IDE BEST PRACTICES - GUIA COMPLETO

**Versão:** 2.0 (Integrada)  
**Data:** Junho 2025  
**Projeto:** Recoloca.ai  
**Escopo:** Configuração, Teste, Orquestração e Integração RAG de Agentes IA no Trae IDE

## 📋 VISÃO GERAL

### Propósito
Este documento fornece diretrizes abrangentes para configuração, teste e orquestração de agentes IA no Trae IDE, com foco especial na integração RAG para o projeto Recoloca.ai.

### Objetivos Estratégicos
- **Operacionalização Eficiente:** Configurar agentes IA de forma sistemática e reproduzível
- **Qualidade Assegurada:** Implementar estratégias de teste robustas para validação de capacidades
- **Orquestração Inteligente:** Estabelecer workflows eficientes entre agentes especializados
- **Integração RAG:** Maximizar o aproveitamento do sistema RAG para contexto e conhecimento
- **Produtividade Maximizada:** Otimizar o desenvolvimento através de melhores práticas

### Escopo de Aplicação
- Configuração de agentes Tier 1 do projeto Recoloca.ai
- Estratégias de teste em múltiplos níveis
- Workflows de orquestração entre agentes
- Integração com sistema RAG local
- Debugging e troubleshooting
- Métricas e avaliação de performance

## 🤖 CONFIGURAÇÃO DE AGENTES

### Hierarquia de Agentes Recoloca.ai

```
@AgenteM_Orquestrador (Tier 0 - Master)
├── @AgenteM_DevFastAPI (Tier 1 - Backend)
├── @AgenteM_DevFlutter (Tier 1 - Frontend)
├── @AgenteM_UXDesigner (Tier 1 - UX Design)
├── @AgenteM_UIDesigner (Tier 1 - UI Design)
├── @AgenteM_ArquitetoTI (Tier 1 - Arquitetura)
└── @AgenteM_QA (Tier 2 - Qualidade)
```

### Sequência de Configuração Recomendada

1. **@AgenteM_Orquestrador** (Master - Primeiro)
2. **@AgenteM_ArquitetoTI** (Arquitetura Core)
3. **@AgenteM_DevFastAPI** (Backend Core)
4. **@AgenteM_UXDesigner** (UX Foundation)
5. **@AgenteM_UIDesigner** (UI Implementation)
6. **@AgenteM_DevFlutter** (Frontend)
7. **@AgenteM_QA** (Qualidade - Último)

### Checklist de Configuração por Agente

#### ✅ Pré-Configuração
- [ ] Perfil do agente atualizado (`docs/04_Agentes_IA/Perfis/`)
- [ ] Documentação RAG relevante identificada
- [ ] Dependências técnicas verificadas
- [ ] Prompt de teste preparado
- [ ] Custom Instructions validadas

#### ✅ Durante a Configuração
- [ ] Custom Instructions aplicadas corretamente
- [ ] Contexto inicial fornecido via RAG
- [ ] Teste básico executado
- [ ] Capacidades RAG validadas
- [ ] Integração com outros agentes testada

#### ✅ Pós-Configuração
- [ ] Teste de orquestração realizado
- [ ] Integração com outros agentes verificada
- [ ] Documentação de setup atualizada
- [ ] Métricas de baseline estabelecidas
- [ ] Feedback loop configurado

## 🧪 ESTRATÉGIA DE TESTES

### Níveis de Teste (Pirâmide)

```
    🎯 Teste de Orquestração Real (Nível 3)
         ↑ Mais Valor, Menos Frequente
    
    📊 Teste de Capacidades RAG (Nível 2)
         ↑ Validação Contextual
    
    ⚡ Teste de Configuração Básica (Nível 1)
         ↑ Mais Frequente, Setup Rápido
```

### Quando Usar Cada Nível

#### 🎯 Nível 3 - Orquestração Real
- **Quando:** Configuração inicial, mudanças significativas
- **Objetivo:** Validar capacidades práticas e integração
- **Duração:** 15-30 minutos
- **Valor:** Alto - simula uso real
- **Exemplo:** Desenvolvimento completo de uma feature

#### 📊 Nível 2 - Capacidades RAG
- **Quando:** Validação de conhecimento específico
- **Objetivo:** Testar recuperação e aplicação de contexto
- **Duração:** 5-10 minutos
- **Valor:** Médio - valida integração RAG
- **Exemplo:** Consulta a documentação técnica específica

#### ⚡ Nível 1 - Configuração Básica
- **Quando:** Setup inicial, verificações rápidas
- **Objetivo:** Confirmar funcionamento básico
- **Duração:** 1-3 minutos
- **Valor:** Baixo - verificação de sanidade
- **Exemplo:** Resposta a prompt simples

### Templates de Teste por Agente

#### @AgenteM_DevFastAPI
```
# Nível 1 - Básico
"Crie um endpoint FastAPI simples para health check"

# Nível 2 - RAG
"Consulte a arquitetura do projeto e implemente um endpoint seguindo os padrões estabelecidos"

# Nível 3 - Orquestração
"Desenvolva um módulo completo de autenticação seguindo a arquitetura do projeto, incluindo testes e documentação"
```

#### @AgenteM_UXDesigner
```
# Nível 1 - Básico
"Descreva os princípios de UX para uma aplicação web"

# Nível 2 - RAG
"Baseado no style guide do projeto, proponha melhorias para a experiência do usuário na tela de login"

# Nível 3 - Orquestração
"Conduza uma pesquisa UX completa para uma nova funcionalidade, incluindo personas, jornada do usuário e wireframes"
```

## 🔄 ORQUESTRAÇÃO E WORKFLOW

### Padrões de Orquestração

#### 1. Desenvolvimento de Feature Completa
```
@AgenteM_Orquestrador → @AgenteM_UXDesigner → @AgenteM_UIDesigner → @AgenteM_DevFastAPI → @AgenteM_DevFlutter → @AgenteM_QA
```

#### 2. Resolução de Problema Técnico
```
@AgenteM_Orquestrador → @AgenteM_ArquitetoTI → @AgenteM_DevFastAPI → @AgenteM_QA
```

#### 3. Melhoria de UX/UI
```
@AgenteM_Orquestrador → @AgenteM_UXDesigner → @AgenteM_UIDesigner → @AgenteM_DevFlutter
```

### Handoffs Eficientes

#### Estrutura de Handoff
1. **Contexto:** Resumo da tarefa e objetivos
2. **Entregáveis:** O que foi produzido pelo agente anterior
3. **Próximos Passos:** O que o próximo agente deve fazer
4. **Dependências:** Recursos ou informações necessárias
5. **Critérios de Sucesso:** Como validar o resultado

#### Template de Handoff
```markdown
## Handoff: [Agente Origem] → [Agente Destino]

### Contexto
[Descrição da tarefa e objetivos]

### Entregáveis do Agente Anterior
- [Item 1]
- [Item 2]

### Próximos Passos
[O que o próximo agente deve fazer]

### Dependências
- [Recurso 1]
- [Recurso 2]

### Critérios de Sucesso
- [ ] [Critério 1]
- [ ] [Critério 2]
```

## 💡 MELHORES PRÁTICAS DE PROMPTS

### Estrutura de Prompt Eficaz

#### 1. Contexto e Papel
```
Você é um [PAPEL] especializado em [DOMÍNIO] trabalhando no projeto Recoloca.ai.
```

#### 2. Tarefa Específica
```
Sua tarefa é [AÇÃO ESPECÍFICA] para [OBJETIVO].
```

#### 3. Contexto RAG
```
Consulte a documentação do projeto para [INFORMAÇÃO ESPECÍFICA].
```

#### 4. Formato de Saída
```
Forneça a resposta no formato:
- [ITEM 1]
- [ITEM 2]
```

#### 5. Critérios de Qualidade
```
Garanta que a solução:
- [CRITÉRIO 1]
- [CRITÉRIO 2]
```

### Prompts por Tipo de Tarefa

#### Desenvolvimento
```
Como desenvolvedor [TECNOLOGIA] sênior do projeto Recoloca.ai, implemente [FUNCIONALIDADE] seguindo:
- Arquitetura definida no HLD
- Padrões de código do projeto
- Práticas de segurança
- Testes automatizados

Consulte a documentação técnica via RAG para detalhes específicos.
```

#### Design
```
Como UX/UI Designer do projeto Recoloca.ai, desenvolva [ELEMENTO DE DESIGN] considerando:
- Style Guide do projeto
- Personas definidas
- Princípios de acessibilidade
- Responsividade

Base-se na pesquisa UX existente via RAG.
```

#### Arquitetura
```
Como Arquiteto de TI do projeto Recoloca.ai, defina [COMPONENTE ARQUITETURAL] garantindo:
- Escalabilidade
- Segurança
- Performance
- Manutenibilidade

Consulte as decisões arquiteturais anteriores via RAG.
```

## 🧠 GESTÃO DE CONTEXTO E RAG

### Estratégias de Contexto

#### 1. Contexto Inicial (Setup)
- Fornecer visão geral do projeto
- Definir papel e responsabilidades
- Estabelecer padrões e diretrizes
- Configurar acesso ao RAG

#### 2. Contexto Incremental (Durante Trabalho)
- Adicionar informações específicas conforme necessário
- Referenciar decisões anteriores
- Manter histórico de conversas relevantes
- Atualizar conhecimento sobre mudanças

#### 3. Contexto de Handoff (Entre Agentes)
- Transferir conhecimento acumulado
- Destacar decisões importantes
- Fornecer contexto sobre limitações
- Estabelecer continuidade

### Otimização do RAG

#### Consultas Eficazes
- **Específicas:** "Como implementar autenticação JWT no FastAPI"
- **Contextuais:** "Padrões de API definidos para o projeto Recoloca.ai"
- **Evolutivas:** "Decisões arquiteturais sobre banco de dados"

#### Validação de Resultados RAG
- Verificar relevância da informação recuperada
- Confirmar atualidade dos dados
- Validar aplicabilidade ao contexto atual
- Complementar com conhecimento específico

## 🐛 DEBUGGING E TROUBLESHOOTING

### Problemas Comuns e Soluções

#### 1. Agente Não Responde Adequadamente
**Sintomas:**
- Respostas genéricas
- Ignorar contexto do projeto
- Não usar informações RAG

**Soluções:**
- Verificar Custom Instructions
- Reforçar contexto do projeto
- Testar consultas RAG específicas
- Reiniciar conversa com contexto completo

#### 2. RAG Não Retorna Informações Relevantes
**Sintomas:**
- Informações desatualizadas
- Contexto irrelevante
- Falha na recuperação

**Soluções:**
- Reformular consulta RAG
- Verificar indexação de documentos
- Usar termos mais específicos
- Combinar múltiplas consultas

#### 3. Orquestração Ineficiente
**Sintomas:**
- Handoffs confusos
- Perda de contexto
- Retrabalho desnecessário

**Soluções:**
- Melhorar estrutura de handoff
- Documentar decisões importantes
- Usar templates padronizados
- Validar entendimento antes de prosseguir

### Checklist de Debugging

#### ✅ Verificações Básicas
- [ ] Custom Instructions aplicadas corretamente
- [ ] Contexto inicial fornecido
- [ ] RAG funcionando adequadamente
- [ ] Prompt claro e específico

#### ✅ Verificações Avançadas
- [ ] Histórico de conversa relevante
- [ ] Integração entre agentes funcionando
- [ ] Documentação atualizada
- [ ] Métricas de qualidade dentro do esperado

## 📊 MÉTRICAS E AVALIAÇÃO

### KPIs de Agentes

#### Eficiência
- **Tempo de Resposta:** < 2 minutos para tarefas simples
- **Taxa de Acerto:** > 80% nas primeiras tentativas
- **Retrabalho:** < 20% das tarefas

#### Qualidade
- **Aderência aos Padrões:** 100% seguindo guidelines
- **Uso de RAG:** > 70% das respostas com contexto RAG
- **Completude:** > 90% das tarefas entregues completas

#### Colaboração
- **Handoffs Eficazes:** > 85% sem necessidade de esclarecimentos
- **Integração:** Trabalho conjunto sem conflitos
- **Comunicação:** Clara e objetiva

### Ferramentas de Medição

#### 1. Logs de Conversa
- Tempo de resposta
- Qualidade das respostas
- Uso de contexto RAG
- Eficácia de handoffs

#### 2. Feedback do Maestro
- Satisfação com resultados
- Produtividade percebida
- Qualidade do trabalho
- Facilidade de uso

#### 3. Métricas de Projeto
- Velocidade de desenvolvimento
- Qualidade do código
- Redução de bugs
- Tempo de entrega

## 🔒 SEGURANÇA E COMPLIANCE

### Diretrizes de Segurança

#### 1. Proteção de Dados
- Não compartilhar informações sensíveis
- Usar dados fictícios em exemplos
- Proteger credenciais e tokens
- Seguir LGPD/GDPR

#### 2. Controle de Acesso
- Validar permissões de agentes
- Limitar acesso a recursos sensíveis
- Monitorar atividades suspeitas
- Implementar logs de auditoria

#### 3. Qualidade de Código
- Seguir práticas de secure coding
- Implementar validações adequadas
- Usar ferramentas de análise estática
- Realizar code reviews

### Compliance

#### Padrões Técnicos
- Clean Code principles
- SOLID principles
- Design patterns apropriados
- Documentação adequada

#### Padrões de Projeto
- Seguir arquitetura definida
- Usar tecnologias aprovadas
- Implementar testes automatizados
- Manter versionamento adequado

## 🚀 EVOLUÇÃO CONTÍNUA

### Ciclo de Melhoria

#### 1. Coleta de Feedback
- Feedback do Maestro
- Métricas de performance
- Análise de logs
- Identificação de padrões

#### 2. Análise e Planejamento
- Identificar oportunidades de melhoria
- Priorizar mudanças
- Planejar implementação
- Definir métricas de sucesso

#### 3. Implementação
- Atualizar Custom Instructions
- Melhorar prompts
- Otimizar workflows
- Treinar agentes

#### 4. Validação
- Testar melhorias
- Medir impacto
- Coletar feedback
- Ajustar conforme necessário

### Roadmap de Melhorias

#### Curto Prazo (1-2 semanas)
- Otimizar prompts existentes
- Melhorar handoffs entre agentes
- Implementar métricas básicas
- Documentar lições aprendidas

#### Médio Prazo (1-2 meses)
- Desenvolver agentes especializados adicionais
- Implementar automações avançadas
- Criar dashboards de métricas
- Estabelecer processos de qualidade

#### Longo Prazo (3-6 meses)
- Integrar com ferramentas externas
- Implementar IA para otimização automática
- Desenvolver capacidades avançadas
- Escalar para outros projetos

## 📚 REFERÊNCIAS E RECURSOS

### Documentação do Projeto
- [[PLANO_MESTRE_RECOLOCA_AI_para_RAG.md]] - Visão geral e estratégia
- [[AGENTES_IA_MENTORES_OVERVIEW_para_RAG.md]] - Especificações dos agentes
- [[HLD_para_RAG.md]] - Arquitetura técnica
- [[KANBAN_ESTRATEGICO_FASES_para_RAG.md]] - Fases e prioridades

### Recursos Técnicos
- Trae IDE Documentation
- RAG System Implementation Guide
- FastAPI Best Practices
- Flutter Development Guidelines

### Ferramentas e Tecnologias
- **IDE:** Trae IDE
- **RAG:** Sistema local com MCP
- **Backend:** FastAPI + Python
- **Frontend:** Flutter Web
- **Database:** Supabase
- **AI/LLM:** Google Gemini via OpenRouter

---

**Última Atualização:** Junho 2025  
**Próxima Revisão:** Julho 2025  
**Responsável:** @AgenteM_Orquestrador  
**Status:** Ativo - Versão de Produção