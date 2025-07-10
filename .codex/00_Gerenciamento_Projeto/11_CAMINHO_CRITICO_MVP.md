---
sticker: lucide//route
---
# CAMINHO CRÍTICO MVP - RECOLOCA.AI

**Data de Criação**: 10 de junho de 2025
**Versão**: 1.0
**Status**: Aprovado - Versão Final
**Autor**: @AgenteM_Orquestrador
**Baseado em**: 
- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.0)
- [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v1.0)
- [[docs/03_Arquitetura_e_Design/02_FLUXO_TRABALHO_GERAL.md]] (v1.0)
- [[docs/04_Agentes_IA/02_AGENTES_IA_MENTORES_OVERVIEW.md]] (v1.0)
- Metodologia "Intelligent Orchestration with Domain Specialization"
- Feedback do Maestro sobre foco em aprendizado e experimentação

---

## 🎯 VISÃO ESTRATÉGICA REFINADA

### Posicionamento Corrigido
**Recoloca.ai** é um **integrador e cockpit** para profissionais de TI em recolocação, não um competidor direto de job boards. O foco principal é:

1. **Aprendizado e Experimentação** com agentes de IA especializados
2. **Orquestração inteligente** de múltiplas fontes de vagas
3. **RAG especializado** para análise de mercado e CVs
4. **Validação de conceitos** de IA aplicada à recolocação profissional

### Agentes Prioritários Identificados

Baseado na análise do [[docs/04_Agentes_IA/02_AGENTES_IA_MENTORES_OVERVIEW.md]], os agentes críticos para o MVP são:

**TIER 1 - Essenciais para MVP:**
- `@AgenteM_Orquestrador` - PM Mentor e Engenheiro de Prompt (Validação Estratégica Central)
- `@AgenteM_UXDesigner` - UX Designer e Pesquisador Mentor Sênior
- `@AgenteM_UIDesigner` - UI Designer e Visual Mentor Sênior
- `@AgenteM_DevFastAPI` - Desenvolvedor Backend Python Sênior
- `@AgenteM_DevFlutter` - Desenvolvedor Flutter/Dart Mentor Sênior

**TIER 2 - Importantes para Qualidade:**
- `@AgenteM_API` - Arquiteto de APIs Mentor
- `@AgenteM_QA` - Analista de QA e Testes Mentor Sênior
- `@AgenteM_Seguranca` - Analista de Segurança Mentor Sênior

---

## 🛤️ CAMINHO CRÍTICO DETALHADO

### FASE 0: FUNDAÇÃO RAG E AGENTES (IMEDIATO)
**Período**: 10-23 Jun 2025 (2 semanas)
**Status**: 🔥 **CRÍTICO - EM ANDAMENTO**

#### Semana 1 (10-16 Jun 2025)
**Prioridade Máxima:**

1. **[CRÍTICO]** Operacionalização RAG Completa
   - ✅ Ambiente Conda configurado (`Agents_RAG_Env`)
   - 🔄 Implementação `rag_indexer.py` funcional
   - 🔄 Indexação documentos core do projeto
   - 🔄 Testes de recuperação semântica
   - **Entregável**: RAG operacional com documentação indexada
   - **Agentes**: `@Maestro` + ferramentas técnicas

2. **[CRÍTICO]** Configuração Agentes Prioritários
   - 🔄 Setup `@AgenteM_UXDesigner` no Trae IDE
   - 🔄 Setup `@AgenteM_UIDesigner` no Trae IDE
   - 🔄 Validação integração RAG com agentes
   - **Entregável**: Agentes UX/UI operacionais
   - **Validação Estratégica**: `@AgenteM_Orquestrador`
   - **Execução**: `@AgenteM_UXDesigner`, `@AgenteM_UIDesigner`

#### Semana 2 (17-23 Jun 2025)
**Consolidação da Base:**

3. **[ALTA]** Servidor MCP RAG
   - 🔄 Implementação servidor MCP para Trae IDE
   - 🔄 Testes de integração com agentes
   - **Entregável**: MCP Server funcional
   - **Agentes**: `@Maestro` + ferramentas técnicas

4. **[ALTA]** Definição UX/UI Foundations
   - 🔄 Pesquisa UX inicial com `@AgenteM_UXDesigner`
   - 🔄 Style Guide base com `@AgenteM_UIDesigner`
   - 🔄 Wireframes principais telas MVP
   - **Entregável**: Fundações de design definidas
   - **Validação Estratégica**: `@AgenteM_Orquestrador` (alinhamento com visão do produto)
   - **Execução**: `@AgenteM_UXDesigner`, `@AgenteM_UIDesigner`

**Marco Fase 0**: ✅ RAG operacional + Agentes UX/UI configurados + Fundações de design

---

### FASE 1: VALIDAÇÃO TÉCNICA E ESTRATÉGICA
**Período**: 24 Jun - 14 Jul 2025 (3 semanas)
**Objetivo**: Validar viabilidade técnica e refinar estratégia

#### Semana 3 (24-30 Jun 2025)
**Validações Críticas:**

5. **[CRÍTICO]** Prototipagem Autenticação (Supabase RLS)
   - 🔄 Setup Supabase com políticas RLS
   - 🔄 Protótipo FastAPI com autenticação
   - 🔄 Testes de segurança básicos
   - **Entregável**: Prova de conceito validada
   - **Agentes**: `@AgenteM_DevFastAPI`, `@AgenteM_Seguranca`

6. **[ALTA]** Análise Competitiva Executada
   - 🔄 Execução prompt análise competitiva com Gemini Pro
   - 🔄 Mapeamento de gaps e oportunidades
   - 🔄 Refinamento posicionamento como "integrador"
   - **Entregável**: Relatório competitivo completo
   - **Validação Estratégica**: `@AgenteM_Orquestrador` (frameworks de análise competitiva)
   - **Execução**: `@Maestro` + ferramentas de pesquisa

#### Semana 4-5 (01-14 Jul 2025)
**Definições Arquiteturais:**

7. **[ALTA]** Arquitetura API Definida
   - 🔄 Especificação OpenAPI 3.0 detalhada
   - 🔄 Definição contratos entre componentes
   - 🔄 Validação com agentes de desenvolvimento
   - **Entregável**: API Spec v1.0 aprovada
   - **Agentes**: `@AgenteM_API`, `@AgenteM_DevFastAPI`

8. **[MÉDIA]** Validação Premissas de Negócio
   - 🔄 Entrevistas com 5-8 profissionais de TI
   - 🔄 Validação disposição para pagar
   - 🔄 Teste conceito "cockpit de recolocação"
   - **Entregável**: Insights de validação documentados
   - **Validação Estratégica**: `@AgenteM_Orquestrador` (frameworks de validação de premissas)
   - **Execução**: `@Maestro` + metodologias de pesquisa

**Marco Fase 1**: ✅ Viabilidade técnica comprovada + Estratégia refinada + API definida

---

### FASE 2: MVP KANBAN + MOMENTO AHA!
**Período**: 15 Jul - 25 Ago 2025 (6 semanas)
**Objetivo**: Desenvolver core funcional com foco no "Momento AHA!"

#### Semana 6-7 (15-28 Jul 2025)
**MVP Kanban (Base):**

9. **[CRÍTICO]** Backend Kanban Funcional
   - 🔄 Modelos de dados (Vaga, Status, Candidatura)
   - 🔄 APIs CRUD completas
   - 🔄 Integração com autenticação Supabase
   - **Entregável**: Backend Kanban operacional
   - **Agentes**: `@AgenteM_DevFastAPI`

10. **[CRÍTICO]** Frontend Kanban (Flutter PWA)
    - 🔄 Interface drag-and-drop entre colunas
    - 🔄 Gestão visual de candidaturas
    - 🔄 Responsividade mobile-first
    - **Entregável**: Kanban UI funcional
    - **Agentes**: `@AgenteM_DevFlutter`, `@AgenteM_UIDesigner`

#### Semana 8-9 (29 Jul - 11 Ago 2025)
**Importação Inteligente (Diferencial):**

11. **[CRÍTICO]** Importação de Vagas com IA
    - 🔄 Parser de URLs com LLM (Gemini)
    - 🔄 Extração automática de dados de vagas
    - 🔄 Categorização inteligente
    - **Entregável**: Importação automática funcionando
    - **Agentes**: `@AgenteM_DevFastAPI`, `@AgenteM_DevFlutter`

#### Semana 10-11 (12-25 Ago 2025)
**MOMENTO AHA! - Análise de CV com IA:**

12. **[CRÍTICO]** Upload e Parsing de CV
    - 🔄 Sistema upload PDF seguro
    - 🔄 Extração com pymupdf + Tesseract (pt-BR)
    - 🔄 Estruturação de dados extraídos
    - **Entregável**: Sistema de upload e extração
    - **Agentes**: `@AgenteM_DevFastAPI`

13. **[CRÍTICO]** Análise Vaga-CV com IA (MOMENTO AHA!)
    - 🔄 Score de adequação CV x Vaga
    - 🔄 Sugestões de otimização personalizadas
    - 🔄 Insights sobre gaps de competências
    - 🔄 **Vídeo explicativo** do processo de análise
    - **Entregável**: Feature que gera o "WOW!" no usuário
   - **Validação Estratégica**: `@AgenteM_Orquestrador` (alinhamento com "Momento AHA!")
   - **Execução**: `@AgenteM_DevFastAPI`, `@AgenteM_UXDesigner`

**Marco Fase 2**: ✅ MVP funcional com Kanban + Importação IA + Análise CV (Momento AHA!)

---

### FASE 3: REFINAMENTO E VALIDAÇÃO
**Período**: 26 Ago - 30 Set 2025 (5 semanas)
**Objetivo**: Polir experiência e validar com usuários reais

#### Semana 12-13 (26 Ago - 08 Set 2025)
**Polimento e QA:**

14. **[ALTA]** Assistente IA Coach (Básico)
    - 🔄 Interface de chat integrada
    - 🔄 Orientações contextuais baseadas no perfil
    - 🔄 Proatividade baseada em ações do usuário
    - **Entregável**: Coach básico funcional
    - **Agentes**: `@AgenteM_DevFastAPI`, `@AgenteM_DevFlutter`

15. **[ALTA]** Testes e QA Completos
    - 🔄 Testes automatizados críticos
    - 🔄 Testes de usabilidade internos
    - 🔄 Correção de bugs e otimizações
    - **Entregável**: MVP estável para testes externos
    - **Agentes**: `@AgenteM_QA`, `@AgenteM_Seguranca`

#### Semana 14-16 (09-30 Set 2025)
**Validação com Usuários:**

16. **[CRÍTICO]** Testes com Usuários Reais
    - 🔄 Recrutamento 10-15 profissionais de TI
    - 🔄 Sessões de teste do "Momento AHA!"
    - 🔄 Coleta de feedback sobre valor percebido
    - 🔄 Métricas de engajamento e retenção
    - **Entregável**: Dados de validação do produto
   - **Validação Estratégica**: `@AgenteM_Orquestrador` (métricas e KPIs de validação)
   - **Execução**: `@Maestro`, `@AgenteM_UXDesigner`

17. **[ALTA]** Implementação de Melhorias Críticas
    - 🔄 Ajustes baseados no feedback
    - 🔄 Otimizações de UX prioritárias
    - 🔄 Refinamento do "Momento AHA!"
    - **Entregável**: MVP refinado v1.1
   - **Validação Estratégica**: `@AgenteM_Orquestrador` (priorização de melhorias)
   - **Execução**: Agentes especializados conforme necessário

**Marco Fase 3**: ✅ Produto validado com usuários + Melhorias implementadas

---

## 🎯 MOMENTOS AHA! REFINADOS

### Opção A: AHA! Precoce (Recomendada)
**Quando**: Logo após upload do CV
**O que**: Análise instantânea mostra score de adequação + 3-5 insights acionáveis
**Impacto**: Valor imediato, engajamento alto, demonstração clara da IA

### Opção B: AHA! Demonstrativo (Complementar)
**Quando**: Durante onboarding
**O que**: **Vídeo interativo** (2-3 min) mostrando análise de CV exemplo
**Impacto**: Educação sobre valor, reduz abandono, mais envolvente que texto

### Opção C: AHA! Progressivo (Retenção)
**Quando**: Ao longo do uso
**O que**: Insights crescentes conforme mais dados são adicionados
**Impacto**: Retenção de longo prazo, valor composto

**Estratégia Recomendada**: Implementar A + B para maximizar conversão e retenção

---

## 📊 QUESTÕES ESTRATÉGICAS RESPONDIDAS

### 1. Dados para Estimativa Salarial
**Solução**: Utilizar pesquisas anuais de salários existentes (Catho, Robert Half, etc.)
- Demonstrar que é análise baseada em período específico
- Incluir disclaimers sobre variações regionais
- Atualizar base anualmente

### 2. Modelo de Aprendizado dos Agentes
**Proposta**: Criar pasta `docs/05_Agentes_Learning/`
- Logs de interações bem-sucedidas
- Padrões de prompts eficazes
- Feedback loops estruturados
- Templates de melhoria contínua

### 3. Escalabilidade da Arquitetura
**Abordagem**: Arquitetura modular desde o início
- Microserviços preparados para escala
- APIs stateless
- Cache inteligente para LLM calls
- Monitoramento de performance desde MVP

### 4. Modelo de Monetização
**Posição**: Manter recorrência com freemium
- Freemium: 5 análises de CV/mês
- Pro: Análises ilimitadas + Coach avançado + Insights premium
- Enterprise: Funcionalidades para empresas (futuro)

---

## 🚨 RISCOS CRÍTICOS E MITIGAÇÕES

### Risco 1: Dependência de APIs Externas
**Mitigação**: 
- Múltiplos provedores LLM (Gemini + OpenRouter)
- Fallbacks para parsing de PDF
- Cache agressivo de resultados

### Risco 2: Qualidade da Análise de CV
**Mitigação**:
- Testes extensivos com CVs reais
- Feedback loop com usuários
- Refinamento contínuo de prompts

### Risco 3: Complexidade dos Agentes
**Mitigação**:
- Foco nos 5 agentes essenciais primeiro
- Documentação detalhada de cada agente
- Testes de integração entre agentes

---

## 📈 MÉTRICAS DE SUCESSO DO CAMINHO CRÍTICO

### Métricas Técnicas (Por Fase)
- **Fase 0**: RAG retrieval accuracy > 85%
- **Fase 1**: API response time < 200ms
- **Fase 2**: CV analysis completion rate > 90%
- **Fase 3**: User satisfaction score > 4.0/5.0

### Métricas de Produto
- **Momento AHA!**: 70% dos usuários completam primeira análise CV
- **Engajamento**: 40% retornam em 7 dias
- **Valor Percebido**: 60% consideram "muito útil" ou "extremamente útil"

### Métricas de Aprendizado (Agentes)
- **Eficácia de Prompts**: Redução de 30% em iterações para tarefas repetitivas
- **Qualidade de Output**: 85% dos outputs de agentes aprovados sem modificação
- **Tempo de Desenvolvimento**: 40% redução vs desenvolvimento tradicional

---

## 🎯 PRÓXIMOS PASSOS IMEDIATOS

### Esta Semana (Atualizar Datas Conforme Cronograma Atual)
1. **[PRIORIDADE 1]** Finalizar configuração RAG operacional
2. **[PRIORIDADE 2]** Setup `@AgenteM_UXDesigner` e `@AgenteM_UIDesigner` com validação estratégica do `@AgenteM_Orquestrador`
3. **[PRIORIDADE 3]** Primeira sessão de UX research (validada estrategicamente)
4. **[PRIORIDADE 4]** Wireframes iniciais das telas principais
5. **[PRIORIDADE 5]** Style Guide base definido

### Próxima Semana (17-23 Jun 2025)
1. Implementar servidor MCP RAG
2. Validar integração agentes com RAG
3. Iniciar prototipagem autenticação Supabase
4. Executar análise competitiva com Gemini Pro

### Decisões Pendentes (Para o Maestro)
1. **Priorização UX/UI**: Confirmar se UX/UI são realmente primários?
2. **Escopo Fase 0**: Incluir mais agentes ou focar nos 5 essenciais?
3. **Momento AHA!**: Qual combinação de opções implementar?
4. **Cronograma**: Ajustar datas baseado na capacidade real?

---

**Próxima Revisão**: A ser definida pelo Maestro
**Responsável**: @AgenteM_Orquestrador + Maestro
**Critério de Sucesso**: RAG operacional + Agentes UX/UI configurados + Primeiros wireframes validados estrategicamente

## 🔄 METODOLOGIA APLICADA

### Intelligent Orchestration with Domain Specialization
Conforme [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] e [[docs/03_Arquitetura_e_Design/02_FLUXO_TRABALHO_GERAL.md]], este caminho crítico segue os princípios:

1. **Validação Estratégica Central**: `@AgenteM_Orquestrador` valida TODAS as tarefas antes da execução
2. **Especialização por Domínio**: Cada agente atua em sua área de expertise
3. **RAG como Fundação**: Decisões baseadas na "Documentação Viva"
4. **Agile SDLC Adaptado**: Fases alinhadas com Discovery → Design → Development → Testing → Deployment

### Processo de Validação Estratégica
Antes de cada tarefa crítica:
1. `@AgenteM_Orquestrador` analisa alinhamento com objetivos do produto
2. Questiona premissas e explora alternativas
3. Define critérios de sucesso mensuráveis
4. Aprova execução ou sugere refinamentos

--- FIM DO DOCUMENTO CAMINHO_CRITICO_MVP.md (v0.9.1) ---