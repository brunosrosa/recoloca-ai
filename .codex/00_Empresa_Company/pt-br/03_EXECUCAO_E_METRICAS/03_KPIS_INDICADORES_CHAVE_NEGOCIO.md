---
doc_id: "EMP-008"
title: "KPIs e Indicadores-Chave de Negócio"
description: "Define os Key Performance Indicators (KPIs) e outras métricas vitais para monitorar a saúde e o progresso do negócio em relação aos seus objetivos estratégicos."
type: "reference"
status: "published"
owner: "@ArquitetoDoCodex"
tags: ["empresa", "metricas", "kpis", "indicadores", "performance"]
---

# KPIs e Indicadores-Chave de Negócio

> **Propósito:** Este documento estabelece os Key Performance Indicators (KPIs) e as métricas essenciais para `[Nome da Empresa]`. O objetivo é criar um sistema de monitoramento consistente que permita avaliar a performance, tomar decisões baseadas em dados e garantir o alinhamento com os objetivos estratégicos definidos no artefato `Diretrizes Estratégicas`.

---

## 1. Visão Geral e Filosofia de Métricas

Nossa abordagem para métricas é focada em **simplicidade, acionabilidade e alinhamento**. Cada KPI deve estar diretamente ligado a um objetivo de negócio e deve ser claro o suficiente para que toda a equipe entenda sua importância e como pode impactá-lo.

Priorizamos **Métricas que Importam (North Star Metric)** sobre métricas de vaidade.

---

## 2. North Star Metric (Métrica Estrela do Norte)

*   **Definição:** A North Star Metric é a medida que melhor captura o valor principal que entregamos aos nossos clientes.

| Métrica Estrela do Norte | Descrição | Justificativa | Frequência de Medição |
| :--- | :--- | :--- | :--- |
| **`[Definir a Métrica]`** | `[Descrição clara e concisa da métrica]` | `[Por que esta métrica representa o valor central para o cliente e o sucesso do negócio?]` | `[Diária, Semanal, Mensal]` |

---

## 3. KPIs por Área de Negócio

A seguir, detalhamos os KPIs primários e secundários para cada área funcional da empresa.

### 3.1. KPIs Financeiros

| KPI | Descrição | Fórmula / Cálculo | Meta (Ex: Trimestral) | Status Atual |
| :--- | :--- | :--- | :--- | :--- |
| **Receita Recorrente Mensal (MRR)** | Receita total gerada por assinaturas em um mês. | `Soma de todas as receitas de assinatura do mês` | `[Ex: Aumentar 20%]` | `[Valor]` |
| **Custo de Aquisição de Cliente (CAC)** | Custo total para adquirir um novo cliente. | `(Custos de Marketing + Vendas) / Nº de Novos Clientes` | `[Ex: Reduzir 10%]` | `[Valor]` |
| **Lifetime Value (LTV)** | Receita total esperada de um cliente durante seu ciclo de vida. | `(Ticket Médio * Média de Compras) * Tempo de Retenção` | `[Ex: Aumentar 15%]` | `[Valor]` |
| **LTV/CAC Ratio** | Relação entre o valor do ciclo de vida do cliente e o custo para adquiri-lo. | `LTV / CAC` | `[Ex: Manter > 3]` | `[Valor]` |
| **Runway** | Tempo (em meses) que a empresa pode operar com o caixa atual. | `Caixa Atual / Burn Rate Mensal` | `[Ex: Manter > 12 meses]` | `[Valor]` |

### 3.2. KPIs de Produto e Engajamento

| KPI | Descrição | Fórmula / Cálculo | Meta (Ex: Trimestral) | Status Atual |
| :--- | :--- | :--- | :--- | :--- |
| **Usuários Ativos (DAU/MAU)** | Número de usuários únicos ativos diária e mensalmente. | `Contagem de usuários únicos` | `[Ex: Atingir 10k MAU]` | `[Valor]` |
| **Taxa de Retenção (Retention Rate)** | Percentual de usuários que retornam ao produto após um período. | `(Nº de usuários ativos no período N) / (Nº de usuários no período N-1)` | `[Ex: 40% em 30 dias]` | `[Valor]` |
| **Taxa de Churn (Churn Rate)** | Percentual de clientes que cancelam o serviço em um período. | `(Nº de clientes perdidos) / (Nº total de clientes no início do período)` | `[Ex: Manter < 2%]` | `[Valor]` |
| **NPS (Net Promoter Score)** | Medida de lealdade e satisfação do cliente. | `(% Promotores) - (% Detratores)` | `[Ex: Atingir > 50]` | `[Valor]` |
| **Adoção de Features Chave** | Percentual de usuários que utilizam as funcionalidades principais do produto. | `(Nº de usuários da feature) / (Nº total de usuários ativos)` | `[Ex: 70% de adoção da feature X]` | `[Valor]` |

### 3.3. KPIs de Marketing e Vendas

| KPI | Descrição | Fórmula / Cálculo | Meta (Ex: Trimestral) | Status Atual |
| :--- | :--- | :--- | :--- | :--- |
| **Leads Gerados (MQL/SQL)** | Número de leads qualificados por marketing e por vendas. | `Contagem de leads que atendem aos critérios` | `[Ex: Gerar 500 MQLs]` | `[Valor]` |
| **Taxa de Conversão (Funil)** | Percentual de usuários que avançam em cada etapa do funil de vendas. | `(Conversões na Etapa N) / (Total na Etapa N-1)` | `[Ex: 10% de MQL para SQL]` | `[Valor]` |
| **Ciclo de Vendas (Sales Cycle)** | Tempo médio para fechar um negócio. | `Soma do tempo de todas as vendas / Nº de vendas` | `[Ex: Reduzir para 30 dias]` | `[Valor]` |
| **Ticket Médio** | Valor médio de cada venda. | `Receita Total / Nº de Vendas` | `[Ex: Aumentar para R$X]` | `[Valor]` |

---

## 4. Dashboard e Ferramentas de Monitoramento

*   **Ferramenta Principal:** `[Ex: Google Analytics, Mixpanel, Metabase, Power BI]`
*   **Dashboard Central:** `[Link para o dashboard onde os KPIs são visualizados]`
*   **Frequência de Revisão:** As métricas serão revisadas em `[Ex: reuniões semanais de performance, reuniões mensais de estratégia]`.