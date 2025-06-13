# Termo de Abertura do Projeto (TAP) - Recoloca.AI

---
**Versão:** 1.0 (Pós-Revisão Interativa)  
**Data:** 12 de junho de 2025  
**Responsável:** Bruno S. Rosa (Maestro)  
**Status:** Aprovado  

---

## 1. Identificação do Projeto

**Nome do Projeto:** Recoloca.AI - Plataforma Inteligente de Gestão de Candidaturas  
**Código do Projeto:** RECOL-2025-001  
**Gerente do Projeto:** Bruno S. Rosa (Maestro)  
**Patrocinador:** Bruno S. Rosa  
**Data de Início:** Junho 2025  
**Data Prevista de Conclusão do MVP:** Dezembro 2025  

## 2. Justificativa do Projeto

### 2.1 Problema Identificado
Profissionais de TI enfrentam dificuldades significativas na gestão eficiente de candidaturas a vagas de emprego:
- **Desorganização:** Falta de controle sobre aplicações enviadas
- **Ineficiência:** Processos manuais demorados e propensos a erros
- **Falta de Insights:** Ausência de análise estratégica sobre o mercado
- **Otimização Limitada:** Dificuldade em adaptar CVs para diferentes vagas

### 2.2 Oportunidade de Mercado
- Mercado de TI em crescimento no Brasil
- Demanda por ferramentas de produtividade pessoal
- Potencial de monetização através de modelo freemium
- Diferenciação através de IA aplicada ao recrutamento

## 3. Objetivos do Projeto

### 3.1 Objetivo Geral
Desenvolver uma plataforma web inteligente que atue como **"integrador e cockpit"** para profissionais de TI em recolocação, centralizando o gerenciamento de candidaturas e utilizando IA para otimização de CVs e insights estratégicos, sem competir diretamente com job boards.

### 3.2 Objetivos Específicos
1. **Gestão Centralizada:** Implementar sistema Kanban para organização de candidaturas
2. **Inteligência Artificial:** Integrar IA para análise e otimização de CVs
3. **Automação:** Reduzir trabalho manual através de importação inteligente
4. **Insights:** Fornecer análises estratégicas sobre o mercado
5. **Escalabilidade:** Criar arquitetura preparada para crescimento

## 4. Escopo do Projeto

### 4.1 Escopo Incluído (MVP)

#### 4.1.1 Funcionalidades Core (Baseado em ERS v0.9.1)
- **Landing Page e Marketing**
  - Página inicial atrativa com seção Hero
  - Demonstração clara das funcionalidades
  - CTAs otimizados para conversão
  - Seção de pricing transparente

- **Sistema de Autenticação e Gestão de Contas**
  - Registro com confirmação por email
  - Login seguro e reset de senha
  - Onboarding guiado
  - Gestão de perfil e preferências
  - Diferenciação clara entre tiers (Free/Premium)

- **Kanban de Candidaturas**
  - Colunas fixas: Interessante → Aplicado → Resposta
  - Criação e gestão de cards de vagas
  - Histórico de interações por vaga
  - Dashboard de métricas pessoais
  - Filtros e busca avançada
  - Limites por tier (10 vagas ativas - gratuito)

- **Importação Inteligente de Vagas**
  - Importação via URL com processamento LLM
  - Extração automática de informações relevantes
  - Revisão e validação obrigatória pelo usuário
  - Suporte a múltiplos idiomas (PT, EN, ES)

- **Otimização de CV com IA**
  - Upload e gestão de currículos base
  - Análise de adequação CV-vaga com score IA
  - Sugestões específicas e contextualizadas
  - Estimativa de range salarial
  - Download de CV otimizado (templates ATS-friendly)
  - Versionamento e histórico
  - Limites por tier (3 otimizações/mês - gratuito)

- **Assistente IA para Coaching Básico**
  - Interface chatbot com persona definida
  - Coaching proativo baseado em métricas
  - Orientações sobre soft skills e mercado
  - Respostas baseadas em RAG
  - Limites por tier (15 interações/dia - gratuito)

#### 4.1.2 Aspectos Técnicos
- **Frontend:** Flutter Web (PWA)
- **Backend:** FastAPI (Python)
- **Banco de Dados:** Supabase (PostgreSQL)
- **IA/LLM:** Gemini Pro via OpenRouter
- **Infraestrutura:** Vercel (Frontend) + Render (Backend)

### 4.2 Escopo Excluído (Pós-MVP)
- Aplicativo mobile nativo
- Extensão Chrome avançada
- Integrações com ATSs externos
- Funcionalidades de networking
- Sistema de pagamentos complexo

## 5. Principais Entregas

### 5.1 Fase 1: Estruturação e Validação (Jun - Ago 2025)
- [ ] Sistema RAG operacional
- [ ] Arquitetura de agentes IA configurada
- [ ] Validação técnica (RLS FastAPI/Supabase)
- [ ] Pesquisa com usuários-alvo
- [ ] Documentação técnica detalhada

### 5.2 Fase 2: Desenvolvimento MVP (Set - Nov 2025)
- [ ] Landing page e sistema de autenticação
- [ ] Kanban de candidaturas funcional
- [ ] Importação inteligente de vagas
- [ ] Upload, parsing e otimização de CV com IA
- [ ] Assistente IA para coaching básico
- [ ] Interface web responsiva (PWA)
- [ ] Modelo freemium implementado

### 5.3 Fase 3: Lançamento e Validação (Dez 2025)
- [ ] Deploy em produção
- [ ] Programa de beta testers estruturado
- [ ] Documentação de usuário
- [ ] Estratégia de go-to-market
- [ ] Coleta e análise de métricas de sucesso

## 6. Principais Stakeholders

| Stakeholder | Papel | Responsabilidades | Expectativas |
|-------------|-------|-------------------|---------------|
| **Bruno S. Rosa (Maestro)** | Gerente/Desenvolvedor | Desenvolvimento, arquitetura, gestão | Entrega do MVP funcional |
| **Early Adopters - Dev Sênior** | Beta Testers | Feedback detalhado, casos de uso reais | Ferramenta que acelere recolocação |
| **Early Adopters - QA/Analistas** | Beta Testers | Validação de funcionalidades, UX | Interface intuitiva e eficiente |
| **Mentores/Advisors Tech** | Consultores | Orientação estratégica, networking | Produto com potencial de mercado |
| **Comunidade Tech (LinkedIn/Discord)** | Validadores | Insights, divulgação orgânica | Ferramenta inovadora e útil |
| **Profissionais RH/Recrutamento** | Stakeholders Secundários | Perspectiva do mercado, validação | Candidatos mais bem preparados |

## 7. Principais Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|------------|
| **Complexidade técnica da IA** | Média | Alto | Prototipagem incremental, validação contínua |
| **Custos de APIs de LLM** | Alta | Médio | Monitoramento rigoroso, otimização de prompts |
| **Validação de mercado** | Média | Alto | Pesquisa com usuários, MVP enxuto |
| **Sobrecarga de desenvolvimento solo** | Alta | Alto | Metodologia ágil, agentes IA como suporte |
| **Concorrência** | Baixa | Médio | Diferenciação através de IA e UX |

## 8. Orçamento Estimado

### 8.1 Custos Operacionais (Mensais)
- **APIs de LLM:** $50-100
- **Infraestrutura:** $20-50
- **Ferramentas de desenvolvimento:** $30
- **Total estimado:** $100-180/mês

### 8.2 Investimento em Tempo
- **Desenvolvimento:** 3-4 meses (tempo parcial)
- **Validação e testes:** 1 mês
- **Documentação:** Contínuo

## 9. Critérios de Sucesso

### 9.1 Critérios Técnicos
- [ ] Sistema funcional com todas as features core do MVP
- [ ] Performance adequada (< 2s carregamento inicial)
- [ ] Segurança implementada (RLS, autenticação, LGPD)
- [ ] PWA funcional com responsividade mobile
- [ ] Integração IA estável (< 5% erro rate)
- [ ] Cobertura de testes > 70% (ajustado para desenvolvimento solo)

### 9.2 Critérios de Product-Market Fit (Baseado em METRICAS_SUCESSO_BASE_MERCADO.md)
- [ ] **Sean Ellis PMF Score ≥ 40%** ("Quão decepcionado ficaria sem o Recoloca.ai?")
- [ ] **Day 7 Retention ≥ 15%** (benchmark SaaS B2C: 10-25%)
- [ ] **Onboarding Completion ≥ 70%** (setup inicial + primeira vaga)
- [ ] **Time to First Value < 2 horas** (primeira ação útil)
- [ ] **Core Feature Adoption**: Kanban 90%, CV Optimization 70%, IA Coach 60%

### 9.3 Critérios de Validação de Negócio
- [ ] **Programa Beta**: 15 profissionais qualificados (5 Dev Sênior, 5 QA/Analistas, 5 outros)
- [ ] **Conversion Rate Free→Paid ≥ 3%** (benchmark freemium: 2-5%)
- [ ] **NPS ≥ 40** (indicador de satisfação)
- [ ] **"Momento AHA!" validado**: 70% dos usuários fazem otimização de CV
- [ ] **Métricas de Sucesso do Usuário**: 60% conseguem entrevistas em 90 dias

### 9.4 Critérios de Viabilidade Econômica
- [ ] **CAC ≤ R$50** (custo aquisição orgânico)
- [ ] **LTV:CAC ≥ 10:1** (sustentabilidade econômica)
- [ ] **MRR Growth ≥ 15% MoM** (crescimento saudável)
- [ ] **Monthly Churn ≤ 8%** (retenção adequada para MVP)

## 10. Metodologia de Desenvolvimento

### 10.1 Framework: "Solo Ágil Aumentado por IA"
- **Desenvolvimento iterativo** com sprints de 1-2 semanas
- **Agentes IA Mentores** para suporte especializado
- **Sistema RAG** para gestão de conhecimento
- **Documentação viva** e atualização contínua
- **Validação contínua** com usuários

### 10.2 Ferramentas de Gestão
- **Kanban:** Obsidian com plugin Tasks
- **Versionamento:** Git/GitHub
- **Documentação:** Markdown no Obsidian
- **Comunicação:** Agentes IA via Trae IDE

## 11. Aprovações

**Patrocinador do Projeto:** Bruno S. Rosa  
**Data de Aprovação:** Junho 2025  
**Assinatura:** [Digital - Aprovado via commit inicial]

---

**Próximos Passos Imediatos:**
1. Finalização da operacionalização do sistema RAG
2. Configuração dos agentes IA essenciais no Trae IDE
3. Início da implementação seguindo priorização RICE
4. Estruturação do programa de beta testers
5. Setup de ferramentas de analytics e métricas

**Documentos Relacionados:**
- [[PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica completa
- [[ERS.md]] - Especificação de requisitos (v0.9.1)
- [[PRIORIZACAO_RICE_RF.md]] - Priorização detalhada dos requisitos
- [[METRICAS_SUCESSO_BASE_MERCADO.md]] - Métricas e benchmarks
- [[CAMINHO_CRITICO_MVP.md]] - Roadmap de desenvolvimento
- [[KANBAN_INTERNO_PROJETO.md]] - Backlog detalhado