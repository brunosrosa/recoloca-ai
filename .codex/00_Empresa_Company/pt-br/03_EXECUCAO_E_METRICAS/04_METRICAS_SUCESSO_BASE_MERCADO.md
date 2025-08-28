---
doc_id: "EMP-009"
title: "Métricas de Sucesso com Base no Mercado"
description: "Estabelece métricas de sucesso que são benchmarked contra o mercado e a concorrência, fornecendo um contexto externo para a avaliação de performance."
type: "reference"
status: "published"
owner: "@ArquitetoDoCodex"
tags: ["empresa", "metricas", "benchmark", "mercado", "performance"]
---

# Métricas de Sucesso com Base no Mercado

> **Propósito:** Este documento estabelece um framework para definir e acompanhar métricas de sucesso para `[Nome do Produto/Empresa]`, utilizando benchmarks de mercado como referência. O objetivo é permitir uma avaliação realista da performance e suportar a tomada de decisões baseada em dados, contextualizando os resultados internos com o cenário externo.

> **Instruções:** Substitua os valores de `[Meta da Empresa]` pelos objetivos específicos do seu negócio. As seções de `Benchmark` e `Fonte` devem ser mantidas como referência, mas podem ser adaptadas com dados mais específicos do seu nicho de mercado, se disponíveis.

---

## 1. Metodologia de Benchmarking

As métricas e benchmarks apresentados neste documento são compilados a partir de fontes de mercado confiáveis para modelos de negócio como:

- **SaaS (B2C e B2B)**
- **Plataformas de Marketplace**
- **Produtos com modelo Freemium**
- **Aplicações Mobile**

As fontes primárias incluem, mas não se limitam a: `[Ex: Mixpanel, ChartMogul, OpenView Partners, a16z, Statista, relatórios de mercado específicos do setor]`. É crucial revisitar e atualizar estas fontes periodicamente.

---

## 2. Métricas Fundamentais por Estágio do Funil

### 2.1. Aquisição de Usuários

| Métrica | Benchmark de Mercado | Meta da Empresa | Fonte de Referência |
| :--- | :--- | :--- | :--- |
| **Taxa de Conversão (Visitante → Cadastro)** | `[Ex: 2-5% para SaaS B2C]` | `[Definir Meta]` | `[Ex: Unbounce, WordStream]` |
| **Crescimento de Tráfego Orgânico (MoM)** | `[Ex: 10-20% para Startups]` | `[Definir Meta]` | `[Ex: Ahrefs, SEMrush]` |
| **Custo de Aquisição de Cliente (CAC)** | `[Ex: $100-300 para SaaS B2B]` | `[Definir Meta]` | `[Ex: ProfitWell, ChartMogul]` |
| **Período de Retorno do CAC (Payback)** | `[Ex: 5-12 meses para SaaS]` | `[Definir Meta]` | `[Ex: OpenView Partners]` |

### 2.2. Ativação e Onboarding

| Métrica | Benchmark de Mercado | Meta da Empresa | Fonte de Referência |
| :--- | :--- | :--- | :--- |
| **Time to First Value (TTFV)** | `[Ex: < 24 horas para SaaS]` | `[Definir Meta]` | `[Ex: Mixpanel, Amplitude]` |
| **Taxa de Conclusão do Onboarding** | `[Ex: 60-80% para SaaS]` | `[Definir Meta]` | `[Ex: Userpilot, Appcues]` |
| **Adoção de Features Essenciais (30 dias)** | `[Ex: 60-80% dos usuários ativos]` | `[Definir Meta]` | `[Ex: Mixpanel, Amplitude]` |

### 2.3. Engajamento e Retenção

| Métrica | Benchmark de Mercado | Meta da Empresa | Fonte de Referência |
| :--- | :--- | :--- | :--- |
| **Relação DAU/MAU (Sticky Factor)** | `[Ex: 20-50% para bons produtos]` | `[Definir Meta]` | `[Ex: a16z, Sequoia]` |
| **Retenção Dia 7 (D7 Retention)** | `[Ex: 10-25% para SaaS B2C]` | `[Definir Meta]` | `[Ex: Mixpanel, Amplitude]` |
| **Retenção Mês 1 (M1 Retention)** | `[Ex: 30-50% para SaaS B2B]` | `[Definir Meta]` | `[Ex: ChartMogul, ProfitWell]` |
| **Duração Média da Sessão** | `[Ex: 8-15 minutos para Apps de Carreira]` | `[Definir Meta]` | `[Ex: App Annie, Similar Web]` |

### 2.4. Monetização

| Métrica | Benchmark de Mercado | Meta da Empresa | Fonte de Referência |
| :--- | :--- | :--- | :--- |
| **Taxa de Conversão (Free → Paid)** | `[Ex: 2-5% para Freemium]` | `[Definir Meta]` | `[Ex: ProfitWell, Freemium.org]` |
| **Receita Média por Usuário (ARPU)** | `[Ex: $25-100 para SaaS B2B]` | `[Definir Meta]` | `[Ex: ChartMogul, Recurly]` |
| **Crescimento da Receita Recorrente (MRR Growth)** | `[Ex: 15-20% MoM para Early Stage]` | `[Definir Meta]` | `[Ex: SaaStr, ChartMogul]` |
| **Taxa de Churn Mensal (Monthly Churn)** | `[Ex: 3-7% para SaaS B2C]` | `[Definir Meta]` | `[Ex: ChartMogul, ProfitWell]` |
| **Relação LTV/CAC** | `[Ex: > 3:1]` | `[Definir Meta]` | `[Ex: OpenView, SaaStr]` |

### 2.5. Satisfação e Advocacia

| Métrica | Benchmark de Mercado | Meta da Empresa | Fonte de Referência |
| :--- | :--- | :--- | :--- |
| **Net Promoter Score (NPS)** | `[Ex: > 40 para um bom SaaS]` | `[Definir Meta]` | `[Ex: Delighted, Satmetrix]` |
| **Customer Satisfaction Score (CSAT)** | `[Ex: > 80%]` | `[Definir Meta]` | `[Ex: Zendesk, HubSpot]` |
| **Viralidade (Coeficiente Viral)** | `[Ex: > 0.5 para crescimento viral]` | `[Definir Meta]` | `[Ex: Andrew Chen's Blog]` |

---

## 3. Dashboard e Revisão

- **Ferramenta de Visualização:** `[Ex: Metabase, Looker, Power BI]`
- **Link para o Dashboard:** `[Inserir link para o dashboard de métricas]`
- **Frequência de Revisão:** As métricas de mercado e as metas internas devem ser revisadas `[Ex: trimestralmente]` para garantir o alinhamento contínuo com a estratégia e a realidade do mercado.

**Net Promoter Score (NPS)**
- **Benchmark [CATEGORIA_BENCHMARK]**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_NPS]
- **Fonte**: [FONTE_DADOS]

**Customer Satisfaction Score (CSAT)**
- **Benchmark [CATEGORIA_BENCHMARK]**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_CSAT]
- **Fonte**: [FONTE_DADOS]

**System Usability Scale (SUS)**
- **Benchmark [CATEGORIA_BENCHMARK]**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_SUS]
- **Fonte**: [FONTE_DADOS]

#### 5.2 Product-Market Fit

**Sean Ellis PMF Score**
- **Benchmark para PMF**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_PMF]
- **Pergunta**: "[PERGUNTA_PMF_PERSONALIZADA]"
- **Fonte**: [FONTE_DADOS]

**Organic Growth Rate**
- **Benchmark com PMF**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_CRESCIMENTO_ORGANICO]
- **Fonte**: [FONTE_DADOS]

#### 5.3 Referral e Viral Growth

**Referral Rate**
- **Benchmark [CATEGORIA_BENCHMARK]**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_REFERRAL]
- **Fonte**: [FONTE_DADOS]

**Viral Coefficient (K-factor)**
- **Benchmark [CATEGORIA_BENCHMARK]**: [VALOR_BENCHMARK]
- **Meta [NOME_PROJETO]**: [META_VIRAL_COEFFICIENT]
- **Cálculo**: [FORMULA_CALCULO]
- **Fonte**: [FONTE_DADOS]

---

## 📈 METAS POR FASE DE CRESCIMENTO

### Fase 1: Validação (Nov 2025 - Fev 2026)
**Foco**: Product-Market Fit e Retenção

#### Usuários e Ativação
- **Usuários registrados**: 1.000
- **Usuários ativos mensais**: 700 (70%)
- **Onboarding completion**: 70%
- **Time to first value**: <4 horas

#### Retenção
- **Day 1 retention**: 30%
- **Day 7 retention**: 15%
- **Day 30 retention**: 8%
- **Month 3 retention**: 60%

#### Satisfação
- **NPS**: 40+
- **PMF Score**: 40%+
- **SUS Score**: 70+

#### Monetização
- **Usuários pagantes**: 30 (3% conversion)
- **MRR**: R$1.170
- **Churn mensal**: <8%

### Fase 2: Crescimento Inicial (Mar - Jun 2026)
**Foco**: Escalar Aquisição e Melhorar Conversão

#### Usuários e Ativação
- **Usuários registrados**: 5.000
- **Usuários ativos mensais**: 3.750 (75%)
- **Onboarding completion**: 75%
- **Time to first value**: <2 horas

#### Retenção
- **Day 1 retention**: 35%
- **Day 7 retention**: 20%
- **Day 30 retention**: 12%
- **Month 3 retention**: 70%

#### Satisfação
- **NPS**: 50+
- **PMF Score**: 50%+
- **SUS Score**: 75+

#### Monetização
- **Usuários pagantes**: 200 (4% conversion)
- **MRR**: R$7.800
- **Churn mensal**: <6%
- **CAC**: R$50
- **LTV:CAC**: 10:1+

### Fase 3: Crescimento Acelerado (Jul - Dez 2026)
**Foco**: Otimizar Unit Economics e Escalar

#### Usuários e Ativação
- **Usuários registrados**: 20.000
- **Usuários ativos mensais**: 16.000 (80%)
- **Onboarding completion**: 80%
- **Time to first value**: <1 hora

#### Retenção
- **Day 1 retention**: 40%
- **Day 7 retention**: 25%
- **Day 30 retention**: 15%
- **Month 3 retention**: 75%

#### Satisfação
- **NPS**: 60+
- **PMF Score**: 60%+
- **SUS Score**: 80+

#### Monetização
- **Usuários pagantes**: 1.000 (5% conversion)
- **MRR**: R$39.000
- **Churn mensal**: <5%
- **CAC**: R$40
- **LTV:CAC**: 15:1+

---

## 🎯 MÉTRICAS ESPECÍFICAS DO RECOLOCA.AI

### Métricas de Valor Entregue

#### Success Metrics (Outcome-based)
**Job Interview Rate**
- **Definição**: % de usuários que conseguem entrevistas
- **Meta**: 60% dos usuários ativos em 90 dias
- **Benchmark**: Não disponível (métrica proprietária)

**Job Offer Rate**
- **Definição**: % de usuários que recebem ofertas
- **Meta**: 30% dos usuários ativos em 90 dias
- **Benchmark**: Não disponível (métrica proprietária)

**Salary Improvement**
- **Definição**: Aumento salarial médio dos usuários
- **Meta**: 15% de aumento médio
- **Benchmark**: Mercado TI Brasil ~10-20% ao trocar de emprego

#### Engagement com Features Core
**Kanban Usage**
- **Vagas adicionadas por usuário/mês**: 8-12
- **Atualizações de status por usuário/mês**: 15-25
- **Tempo médio por sessão no Kanban**: 8-12 minutos

**CV Optimization Usage**
- **Otimizações por usuário/mês**: 3-5
- **Taxa de aplicação das sugestões**: 70%+
- **Melhoria no score do CV**: 20%+ em média

**IA Coach Engagement**
- **Perguntas por usuário/mês**: 8-15
- **Taxa de satisfação com respostas**: 80%+
- **Follow-up rate**: 40%+

### Métricas de Mercado Brasileiro

#### Penetração de Mercado
**Total Addressable Market (TAM)**
- **Profissionais de TI no Brasil**: ~1.5M
- **Pleno/Sênior**: ~500k
- **Digitalmente ativos**: ~400k
- **Meta penetração Ano 1**: 0.005% (20 usuários)
- **Meta penetração Ano 3**: 0.1% (400 usuários)

**Serviceable Addressable Market (SAM)**
- **Principais capitais**: ~200k profissionais
- **Dispostos a pagar**: ~80k (40%)
- **Meta penetração**: 2.5% (2k usuários pagantes)

#### Comparação com Concorrentes
**Market Share Estimation**
- **LinkedIn Premium**: ~5% dos profissionais de TI
- **Outras ferramentas**: <1%
- **Meta Recoloca.ai**: 0.5% em 3 anos

---

## 📊 DASHBOARD DE MÉTRICAS

### Métricas Diárias
- **Novos cadastros**
- **DAU / MAU ratio**
- **Feature usage (Kanban, CV, Coach)**
- **Support tickets**

### Métricas Semanais
- **WAU**
- **Onboarding completion rate**
- **Free → Paid conversions**
- **Churn events**
- **NPS responses**

### Métricas Mensais
- **MAU**
- **MRR growth**
- **CAC por canal**
- **LTV:CAC ratio**
- **Retention cohorts**
- **Feature adoption rates**

### Métricas Trimestrais
- **PMF Score**
- **Market penetration**
- **Competitive analysis**
- **User success outcomes**
- **Annual planning metrics**

---

## 🛠️ FERRAMENTAS DE TRACKING

### Analytics Stack
- **Google Analytics 4**: Web analytics, acquisition
- **PostHog**: Product analytics, funnels, retention
- **Mixpanel**: Event tracking, cohort analysis
- **Hotjar**: User behavior, heatmaps

### Business Intelligence
- **Metabase**: Dashboards customizados
- **Google Data Studio**: Relatórios executivos
- **Notion**: Tracking manual de métricas qualitativas

### Customer Feedback
- **Delighted**: NPS tracking
- **Typeform**: Surveys customizados
- **Intercom**: In-app feedback
- **Calendly**: User interviews

### Financial Tracking
- **ChartMogul**: SaaS metrics (MRR, churn, LTV)
- **ProfitWell**: Revenue analytics
- **Stripe**: Payment analytics

---

## 🚨 ALERTAS E THRESHOLDS

### Red Flags (Ação Imediata)
- **Churn mensal >10%**
- **Day 7 retention <10%**
- **NPS <20**
- **Conversion rate <1%**
- **CAC payback >12 meses**

### Yellow Flags (Monitoramento Intensivo)
- **Churn mensal 7-10%**
- **Day 7 retention 10-15%**
- **NPS 20-40**
- **Conversion rate 1-2%**
- **CAC payback 8-12 meses**

### Green Zone (Performance Saudável)
- **Churn mensal <5%**
- **Day 7 retention >20%**
- **NPS >50**
- **Conversion rate >3%**
- **CAC payback <6 meses**

---

## 📋 PROCESSO DE REVISÃO

### Revisão Semanal
- **Métricas de ativação e engajamento**
- **Feedback qualitativo de usuários**
- **Performance de features**
- **Ajustes táticos**

### Revisão Mensal
- **Todas as métricas fundamentais**
- **Análise de coortes**
- **ROI de canais de marketing**
- **Roadmap de produto baseado em dados**

### Revisão Trimestral
- **Benchmarking com mercado**
- **Revisão de metas**
- **Análise competitiva**
- **Planejamento estratégico**

### Revisão Anual
- **Revisão completa de benchmarks**
- **Atualização de metas**
- **Análise de market fit**
- **Planejamento de longo prazo**

---

**Responsável**: Maestro (Bruno S. Rosa)
**Apoio**: @AgenteOrquestrador para análise estratégica
**Ferramentas**: PostHog, Google Analytics, ChartMogul
**Revisão**: Semanal (táticas), Mensal (estratégicas)
**Status**: 🟡 Aguardando implementação de tracking

---

## 🔄 Considerações de Orquestração Inteligente

### Integração com Metodologia v1.1
- **Agentes Especializados**: Utilização de @AgenteOrquestrador para análise estratégica de métricas e @AgenteMentorAnalytics para implementação de tracking
- **RAG Operacional**: Contextualização contínua via base de conhecimento de mercado para benchmarking automático
- **Métricas Contínuas**: Coleta automática de dados de performance integrada com sistema de entregáveis
- **Specialized Intelligence**: Delegação eficiente de análise de dados e geração de insights para agentes especializados

### Critérios de Validação Metodológica
- ✅ **Precisão de Tracking**: 95%+ de precisão na coleta de dados de usuário
- ✅ **Tempo de Insight**: Redução de 80% no tempo para gerar insights acionáveis
- ✅ **Automação de Relatórios**: 100% dos relatórios de métricas automatizados
- ✅ **Benchmarking Contínuo**: Comparação automática com padrões de mercado

### Alinhamento com Documentação Viva
- **Sincronização**: Métricas automaticamente sincronizadas com base RAG
- **Versionamento**: Controle de versão integrado das estratégias de métricas
- **Referências**: Links automáticos para documentos de estratégia e validação
- **Dashboards**: Métricas em tempo real de performance do produto

## 📊 Histórico de Versões

### v1.1 (Junho 2025) - Orquestração Inteligente e Specialized Intelligence
- Atualização de referências para documentos v1.1
- Alinhamento com metodologia de Orquestração Inteligente
- Integração com agentes especializados para analytics
- Adição de métricas de automação e precisão
- Sincronização com base RAG operacional

### v1.0 (Junho 2025) - Versão Inicial
- Definição de métricas baseadas em benchmarks de mercado
- Estrutura de KPIs para SaaS B2C e plataformas de carreira
- Metodologia de tracking e análise
- Plano de implementação e ferramentas

## 📚 Documentos Relacionados

- [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v1.1) - Metodologia base
- [[docs/01_Guias_Centrais/PLANO_MESTRE_RECOLOCA_AI.md]] (v1.1) - Visão e objetivos
- [[ESTRATEGIA_GO_TO_MARKET]] (v1.1) - Estratégia de mercado
- [[docs/01_Guias_Centrais/PLANO_VALIDACAO_PREMISSAS_NEGOCIO.md]] (v1.1) - Validação de premissas
- [[docs/01_Guias_Centrais/VANTAGENS_COMPETITIVAS_SUSTENTAVEIS.md]] (v1.1) - Moats estratégicos
- [[docs/04_Agentes_IA/AGENTES_IA_MENTORES_OVERVIEW.md]] - Agentes especializados
- [[docs/07_Operacoes_e_Deploy/ESTRATEGIA_DEVOPS.md]] (v1.1) - Estratégia de DevOps

**Nota:** Este documento (v1.1) está totalmente alinhado com a metodologia de "Orquestração Inteligente" e "Specialized Intelligence" definida no [[docs/01_Guias_Centrais/GUIA_AVANCADO.md]] (v1.1), incorporando automação de coleta e análise de métricas.

--- FIM DO DOCUMENTO METRICAS_SUCESSO_BASE_MERCADO.md (v1.1) ---