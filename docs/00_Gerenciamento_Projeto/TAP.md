# Termo de Abertura do Projeto (TAP) - Recoloca.AI

---
**Versão:** 0.9 (Pré-Revisão Interativa)  
**Data:** Dezembro 2024  
**Responsável:** Bruno S. Rosa (Maestro)  
**Status:** Aprovado  

---

## 1. Identificação do Projeto

**Nome do Projeto:** Recoloca.AI - Plataforma Inteligente de Gestão de Candidaturas  
**Código do Projeto:** RECOL-2024-001  
**Gerente do Projeto:** Bruno S. Rosa (Maestro)  
**Patrocinador:** Bruno S. Rosa  
**Data de Início:** Dezembro 2024  
**Data Prevista de Conclusão do MVP:** Março 2025  

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
Desenvolver uma plataforma web inteligente que revolucione a forma como profissionais de TI gerenciam suas candidaturas, utilizando IA para otimização de CVs e insights estratégicos.

### 3.2 Objetivos Específicos
1. **Gestão Centralizada:** Implementar sistema Kanban para organização de candidaturas
2. **Inteligência Artificial:** Integrar IA para análise e otimização de CVs
3. **Automação:** Reduzir trabalho manual através de importação inteligente
4. **Insights:** Fornecer análises estratégicas sobre o mercado
5. **Escalabilidade:** Criar arquitetura preparada para crescimento

## 4. Escopo do Projeto

### 4.1 Escopo Incluído (MVP)

#### 4.1.1 Funcionalidades Core
- **Sistema de Autenticação e Contas**
  - Registro e login de usuários
  - Gestão de perfis
  - Controle de acesso baseado em roles

- **Kanban de Candidaturas**
  - Criação e gestão de cards de vagas
  - Movimentação entre colunas (Interessante, Aplicado, Resposta)
  - Filtros e busca avançada

- **Otimização de CV com IA**
  - Upload e parsing de CVs em PDF
  - Análise de compatibilidade vaga-CV
  - Sugestões de otimização
  - Estimativa salarial

- **Importação Inteligente de Vagas**
  - Importação via texto/URL
  - Parsing automático com IA
  - Criação automática de cards

- **Coach IA Proativo**
  - Chatbot para orientações
  - Sugestões proativas
  - Análise de tendências

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

### 5.1 Fase 1: Estruturação e Validação (Dez 2024 - Jan 2025)
- [ ] Sistema RAG operacional
- [ ] Arquitetura de agentes IA configurada
- [ ] Validação técnica (RLS FastAPI/Supabase)
- [ ] Pesquisa com usuários-alvo
- [ ] Documentação técnica detalhada

### 5.2 Fase 2: Desenvolvimento MVP (Jan - Mar 2025)
- [ ] Sistema de autenticação funcional
- [ ] Kanban básico operacional
- [ ] Upload e parsing de CV
- [ ] Integração com IA para análise
- [ ] Interface web responsiva
- [ ] Testes de integração

### 5.3 Fase 3: Lançamento e Validação (Mar 2025)
- [ ] Deploy em produção
- [ ] Testes com usuários beta
- [ ] Documentação de usuário
- [ ] Estratégia de go-to-market

## 6. Principais Stakeholders

| Stakeholder | Papel | Responsabilidades | Expectativas |
|-------------|-------|-------------------|---------------|
| **Bruno S. Rosa (Maestro)** | Gerente/Desenvolvedor | Desenvolvimento, arquitetura, gestão | Entrega do MVP funcional |
| **Usuários-Alvo** | Beneficiários | Feedback, validação | Solução eficaz para gestão de candidaturas |
| **Comunidade Tech** | Validadores | Insights, networking | Ferramenta inovadora e útil |

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
- [ ] Sistema funcional com todas as features do MVP
- [ ] Performance adequada (< 2s carregamento)
- [ ] Segurança implementada (RLS, autenticação)
- [ ] Cobertura de testes > 80%

### 9.2 Critérios de Negócio
- [ ] Validação positiva com 5+ usuários beta
- [ ] Feedback qualitativo favorável
- [ ] Métricas de engajamento satisfatórias
- [ ] Viabilidade econômica demonstrada

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
**Data de Aprovação:** Dezembro 2024  
**Assinatura:** [Digital - Aprovado via commit inicial]

---

**Próximos Passos:**
1. Operacionalização do sistema RAG
2. Configuração dos agentes IA no Trae IDE
3. Início da Fase 1: Estruturação e Validação

**Documentos Relacionados:**
- [[PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica completa
- [[ERS.md]] - Especificação de requisitos
- [[KANBAN_INTERNO_PROJETO.md]] - Backlog detalhado
- [[Maestro_Tasks.md]] - Dashboard de tarefas