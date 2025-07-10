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
| **Falha na orquestração de agentes IA** | Média | Alto | Monitoramento contínuo, fallback manual |
| **Degradação da base RAG** | Média | Médio | Backup automático, versionamento |
| **Dependência excessiva de IA** | Baixa | Alto | Manter capacidade de operação manual |

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

### 9.1.1 Critérios de "Specialized Intelligence"
- [ ] **Eficiência de Orquestração ≥ 85%** (tarefas completadas com sucesso pelos agentes)
- [ ] **Tempo de Resposta dos Agentes ≤ 30s** (média de processamento)
- [ ] **Precisão de Insights RAG ≥ 90%** (relevância das informações recuperadas)
- [ ] **Taxa de Automação ≥ 60%** (tarefas automatizadas vs manuais)
- [ ] **Cobertura da Base RAG ≥ 95%** (documentos indexados e atualizados)
- [ ] **Satisfação com Agentes IA ≥ 4.5/5** (feedback do Maestro)

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
- **"Orquestração Inteligente":** Coordenação estratégica entre Maestro e Agentes IA Mentores
- **"Specialized Intelligence":** Agentes IA especializados por domínio técnico
- **Sistema RAG Integrado** para gestão de conhecimento e base de decisões
- **Documentação viva** e atualização contínua
- **Validação contínua** com usuários
- **Automação de tarefas repetitivas** via agentes especializados

### 10.2 Agentes IA Mentores Especializados
- **@AgenteOrquestrador:** PM Mentor e Engenheiro de Prompt principal
- **@AgenteM_DevFastAPI:** Especialista em desenvolvimento backend
- **@AgenteM_DevFlutter:** Especialista em desenvolvimento frontend
- **@AgenteM_QualityAssurance:** Especialista em testes e qualidade
- **@AgenteM_StakeholderManager:** Especialista em gestão de relacionamentos
- **@AgenteM_SecurityAuditor:** Especialista em segurança e compliance

### 10.3 Ferramentas de Gestão e Orquestração
- **Kanban Inteligente:** Obsidian com plugin Tasks + análise IA
- **Versionamento:** Git/GitHub com automação de commits
- **Documentação:** Markdown no Obsidian com sistema RAG
- **Orquestração:** Agentes IA via Trae IDE
- **Dashboard de Métricas:** Monitoramento de "Specialized Intelligence"
- **Base RAG:** Gestão de conhecimento técnico e de negócio

## 11. Aprovações

**Patrocinador do Projeto:** Bruno S. Rosa  
**Data de Aprovação:** Junho 2025  
**Assinatura:** [Digital - Aprovado via commit inicial]

---

**Próximos Passos Imediatos:**
1. Finalização da operacionalização do sistema RAG
2. Configuração dos agentes IA essenciais no Trae IDE
3. Implementação do dashboard de métricas de "Specialized Intelligence"
4. Testes piloto da orquestração inteligente

---

## 12. Histórico de Versões

### Versão 1.1 - Janeiro 2025
**Melhorias de Orquestração Inteligente e Specialized Intelligence:**
- Integração da metodologia "Orquestração Inteligente" na gestão do projeto
- Adição de agentes IA especializados por domínio técnico
- Implementação de sistema RAG integrado para gestão de conhecimento
- Definição de métricas de "Specialized Intelligence" para orquestração de agentes IA
- Expansão dos critérios de sucesso com métricas de automação e eficiência IA
- Inclusão de riscos específicos de orquestração de agentes IA
- Atualização das ferramentas de gestão com dashboard de métricas
- Consolidação da metodologia "Solo Ágil Aumentado por IA"

### Versão 1.0 - Junho 2025
- Versão inicial aprovada
- Definição completa do escopo MVP
- Estabelecimento de critérios de sucesso
- Aprovação do orçamento e cronograma

---

## 13. Documentos Relacionados

- **[[PLANO_MESTRE_RECOLOCA_AI.md]]** - Visão geral e objetivos estratégicos
- **[[ERS.md]]** - Especificação de Requisitos do Sistema
- **[[KANBAN_INTERNO_PROJETO.md]]** - Gestão de tarefas e prioridades
- **[[PGQ.md]]** - Plano de Gestão da Qualidade
- **[[PStakeholders.md]]** - Plano de Gestão de Stakeholders
- **[[Maestro_Tasks.md]]** - Tarefas específicas do Maestro
- **[[HLD.md]]** - Arquitetura de Alto Nível
- **[[AGENTES_IA_MENTORES_OVERVIEW.md]]** - Visão geral dos agentes IA
- **[[GUIA_AVANCADO.md]]** - Metodologia e engenharia de prompt

---

*Documento atualizado com metodologia de "Orquestração Inteligente" e "Specialized Intelligence" - Janeiro 2025*