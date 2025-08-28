# Plano de Gerenciamento do Escopo (PGP) - Recoloca.AI

---
**Versão:** 1.0  
**Data:** Junho 2025  
**Responsável:** Bruno S. Rosa (Maestro)  
**Próxima Revisão:** Setembro 2025  

---

## 1. Introdução

### 1.1 Objetivo
Este documento define como o escopo do projeto Recoloca.AI será planejado, definido, controlado e validado ao longo de todo o ciclo de vida do projeto, garantindo que todas as entregas necessárias sejam incluídas e que o trabalho desnecessário seja evitado.

### 1.2 Escopo do Documento
O plano abrange:
- Metodologia de gerenciamento do escopo
- Definição do escopo do projeto e do produto
- Estrutura Analítica do Projeto (EAP)
- Processo de controle de mudanças
- Validação e aceitação de entregas
- Gestão de requisitos
- Métricas de controle do escopo

### 1.3 Metodologia
Utilizamos a metodologia **"Solo Ágil Aumentado por IA"** adaptada para gerenciamento de escopo, com:
- **Iterações curtas** com validação contínua
- **Agentes IA Mentores** para suporte especializado
- **@AgenteM_Orquestrador** como mentor estratégico
- **Documentação Viva** para rastreabilidade
- **Feedback loops** constantes com stakeholders

## 2. Escopo do Projeto

### 2.1 Objetivos do Projeto

#### 2.1.1 Objetivo Geral
Desenvolver o **Recoloca.AI**, um Micro-SaaS para auxiliar profissionais brasileiros de tecnologia na recolocação profissional, utilizando IA para análise de CVs e insights de mercado.

#### 2.1.2 Objetivos Específicos
- **MVP (Mês 1-3):** Validar proposta de valor com funcionalidades core
- **Expansão (Mês 4-6):** Adicionar funcionalidades avançadas baseadas em feedback
- **Escala (Mês 7+):** Preparar para crescimento e monetização sustentável

### 2.2 Critérios de Sucesso

#### 2.2.1 Critérios Técnicos
- **Performance:** Análise de CV em < 30 segundos
- **Precisão:** ≥ 85% de precisão na extração de dados
- **Disponibilidade:** ≥ 99% uptime
- **Segurança:** Conformidade total com LGPD
- **Usabilidade:** SUS Score ≥ 70

#### 2.2.2 Critérios de Negócio
- **Validação:** 50+ usuários beta com feedback positivo
- **Engajamento:** ≥ 70% taxa de retenção semanal
- **Product-Market Fit:** NPS ≥ 50
- **Viabilidade:** Modelo de receita validado

### 2.3 Principais Entregas

#### 2.3.1 Entregas MVP (Fase 1)
- **Backend FastAPI** com APIs core
- **Frontend PWA Flutter** responsivo
- **Sistema de Análise de CV** com IA
- **Autenticação e Segurança** via Supabase
- **Dashboard de Insights** básico
- **Documentação Técnica** completa

#### 2.3.2 Entregas Pós-MVP (Fase 2)
- **Extensão de Navegador** Chrome
- **Análise de Mercado** avançada
- **Recomendações Personalizadas** de carreira
- **Integração com Plataformas** de emprego
- **Sistema de Notificações** inteligente
- **Analytics Avançado** para usuários

#### 2.3.3 Entregas de Escala (Fase 3)
- **API Pública** para parceiros
- **Dashboard Administrativo** completo
- **Sistema de Pagamentos** integrado
- **Funcionalidades B2B** para empresas
- **Mobile App Nativo** (iOS/Android)
- **Infraestrutura Escalável** em cloud

## 3. Escopo do Produto

### 3.1 Funcionalidades Incluídas no MVP

#### 3.1.1 Core Features
- **RF-CV-001:** Upload e parsing de CV (PDF/DOCX)
- **RF-CV-002:** Extração automática de dados estruturados
- **RF-CV-003:** Análise de competências técnicas
- **RF-CV-004:** Identificação de gaps de habilidades
- **RF-CV-005:** Sugestões básicas de melhoria

#### 3.1.2 Features de Suporte
- **RF-AUTH-001:** Autenticação segura de usuários
- **RF-AUTH-002:** Gestão de perfis e preferências
- **RF-DASH-001:** Dashboard com métricas pessoais
- **RF-DASH-002:** Histórico de análises
- **RF-SEC-001:** Conformidade com LGPD

### 3.2 Funcionalidades Excluídas do MVP

#### 3.2.1 Funcionalidades Avançadas (Pós-MVP)
- Análise de mercado em tempo real
- Recomendações de vagas específicas
- Integração com LinkedIn/outras plataformas
- Sistema de coaching personalizado
- Análise comparativa com outros profissionais

#### 3.2.2 Funcionalidades B2B (Fase 3)
- Dashboard para recrutadores
- API para integração corporativa
- Análise de equipes/departamentos
- Relatórios executivos
- White-label solutions

### 3.3 Restrições do Escopo

#### 3.3.1 Restrições Técnicas
- **Linguagens:** Português brasileiro apenas (MVP)
- **Formatos:** PDF e DOCX apenas (MVP)
- **Plataformas:** Web PWA apenas (MVP)
- **IA:** Google Gemini como LLM principal
- **Infraestrutura:** Supabase como backend principal

#### 3.3.2 Restrições de Negócio
- **Mercado:** Brasil apenas (MVP)
- **Segmento:** Profissionais de TI (MVP)
- **Modelo:** Freemium (MVP gratuito)
- **Compliance:** LGPD obrigatória
- **Orçamento:** Autofinanciado (MVP)

#### 3.3.3 Restrições de Tempo
- **MVP:** 3 meses máximo
- **Iterações:** Sprints de 1-2 semanas
- **Validação:** Feedback semanal obrigatório
- **Lançamento:** Beta em 2.5 meses

## 4. Estrutura Analítica do Projeto (EAP)

### 4.1 EAP Nível 1 - Fases Principais

```
Recoloca.AI
├── 1. Planejamento e Setup
├── 2. Desenvolvimento MVP
├── 3. Testes e Validação
├── 4. Lançamento Beta
├── 5. Expansão Pós-MVP
└── 6. Preparação para Escala
```

### 4.2 EAP Nível 2 - Componentes Detalhados

#### 4.2.1 Fase 1: Planejamento e Setup (Semana 1-2)
```
1. Planejamento e Setup
├── 1.1 Documentação Estratégica
│   ├── 1.1.1 Plano Mestre
│   ├── 1.1.2 ERS (Especificação de Requisitos)
│   ├── 1.1.3 HLD (High Level Design)
│   └── 1.1.4 Planos de Gerenciamento
├── 1.2 Setup Técnico
│   ├── 1.2.1 Ambiente de Desenvolvimento
│   ├── 1.2.2 Repositórios Git
│   ├── 1.2.3 Infraestrutura Supabase
│   └── 1.2.4 Configuração RAG/IA
└── 1.3 Setup de Agentes IA
    ├── 1.3.1 Configuração @AgenteM_Orquestrador
    ├── 1.3.2 Agentes Mentores Especializados
    └── 1.3.3 Templates e Prompts
```

#### 4.2.2 Fase 2: Desenvolvimento MVP (Semana 3-10)
```
2. Desenvolvimento MVP
├── 2.1 Backend Core
│   ├── 2.1.1 APIs de Autenticação
│   ├── 2.1.2 APIs de Upload/Parsing
│   ├── 2.1.3 Sistema de Análise IA
│   └── 2.1.4 APIs de Dashboard
├── 2.2 Frontend PWA
│   ├── 2.2.1 Interface de Login
│   ├── 2.2.2 Upload de CV
│   ├── 2.2.3 Dashboard de Resultados
│   └── 2.2.4 Perfil do Usuário
├── 2.3 Integração e Testes
│   ├── 2.3.1 Testes Unitários
│   ├── 2.3.2 Testes de Integração
│   ├── 2.3.3 Testes de Performance
│   └── 2.3.4 Testes de Segurança
└── 2.4 Infraestrutura
    ├── 2.4.1 Deploy Automatizado
    ├── 2.4.2 Monitoramento
    ├── 2.4.3 Backup e Recovery
    └── 2.4.4 Conformidade LGPD
```

#### 4.2.3 Fase 3: Testes e Validação (Semana 9-11)
```
3. Testes e Validação
├── 3.1 Testes Internos
│   ├── 3.1.1 Testes de Usabilidade
│   ├── 3.1.2 Testes de Performance
│   ├── 3.1.3 Testes de Segurança
│   └── 3.1.4 Testes de Conformidade
├── 3.2 Validação com Usuários
│   ├── 3.2.1 Recrutamento Beta Testers
│   ├── 3.2.2 Testes de Usabilidade
│   ├── 3.2.3 Coleta de Feedback
│   └── 3.2.4 Iterações Baseadas em Feedback
└── 3.3 Preparação para Lançamento
    ├── 3.3.1 Documentação de Usuário
    ├── 3.3.2 Material de Marketing
    ├── 3.3.3 Estratégia de Comunicação
    └── 3.3.4 Plano de Suporte
```

### 4.3 Pacotes de Trabalho (Work Packages)

Cada componente da EAP é detalhado em:
- **Descrição:** O que será entregue
- **Critérios de Aceitação:** Como validar a conclusão
- **Responsável:** Maestro + Agente Mentor específico
- **Duração Estimada:** Tempo necessário
- **Dependências:** Pré-requisitos
- **Riscos:** Potenciais problemas

## 5. Processo de Controle de Mudanças

### 5.1 Tipos de Mudanças

#### 5.1.1 Mudanças Menores (Aprovação Automática)
- **Critérios:** Impacto < 4 horas de trabalho, sem afetar arquitetura
- **Exemplos:** Ajustes de UI, correções de bugs, melhorias de performance
- **Processo:** Documentação no commit Git + atualização da documentação
- **Responsável:** Maestro

#### 5.1.2 Mudanças Médias (Aprovação do @AgenteM_Orquestrador)
- **Critérios:** Impacto 4-16 horas, pode afetar múltiplos componentes
- **Exemplos:** Novos endpoints, mudanças de fluxo, integrações adicionais
- **Processo:** Discussão estratégica + análise de impacto + aprovação
- **Responsável:** Maestro + @AgenteM_Orquestrador

#### 5.1.3 Mudanças Maiores (Revisão Completa)
- **Critérios:** Impacto > 16 horas, afeta arquitetura ou escopo core
- **Exemplos:** Mudança de stack, novos requisitos funcionais, pivots
- **Processo:** Análise completa + atualização de documentação + validação
- **Responsável:** Maestro + @AgenteM_Orquestrador + Stakeholders

### 5.2 Processo de Solicitação de Mudança

#### 5.2.1 Fluxo de Aprovação
1. **Identificação:** Necessidade de mudança identificada
2. **Análise:** Impacto em escopo, tempo, custo, qualidade
3. **Categorização:** Menor, média ou maior
4. **Aprovação:** Conforme categoria
5. **Implementação:** Execução da mudança
6. **Documentação:** Atualização da documentação viva
7. **Comunicação:** Informar stakeholders relevantes

#### 5.2.2 Critérios de Avaliação
- **Alinhamento Estratégico:** Contribui para objetivos do projeto?
- **Viabilidade Técnica:** É tecnicamente possível?
- **Impacto no Cronograma:** Afeta marcos críticos?
- **Impacto no Orçamento:** Requer recursos adicionais?
- **Valor para o Usuário:** Melhora a proposta de valor?
- **Riscos:** Introduz novos riscos significativos?

### 5.3 Registro de Mudanças

Todas as mudanças são registradas em:
- **Git Commits:** Para mudanças de código
- **Documentação Viva:** Para mudanças de escopo/requisitos
- **KANBAN_INTERNO_PROJETO.md:** Para mudanças de prioridades
- **Log de Mudanças:** Registro centralizado de decisões

## 6. Validação e Aceitação de Entregas

### 6.1 Critérios de Aceitação

#### 6.1.1 Critérios Técnicos
- **Funcionalidade:** Atende aos requisitos funcionais
- **Performance:** Atende aos requisitos não-funcionais
- **Qualidade:** Passa em todos os testes automatizados
- **Segurança:** Atende aos requisitos de segurança
- **Documentação:** Documentação técnica completa

#### 6.1.2 Critérios de Negócio
- **Valor:** Entrega valor mensurável ao usuário
- **Usabilidade:** Interface intuitiva e responsiva
- **Conformidade:** Atende à LGPD e regulamentações
- **Escalabilidade:** Suporta crescimento esperado
- **Manutenibilidade:** Código limpo e bem estruturado

### 6.2 Processo de Validação

#### 6.2.1 Validação Interna
1. **Auto-validação:** Maestro verifica critérios básicos
2. **Validação por Agente:** Agente Mentor especializado revisa
3. **Validação Cruzada:** @AgenteM_Orquestrador valida alinhamento estratégico
4. **Testes Automatizados:** Execução de suíte de testes
5. **Testes Manuais:** Validação de fluxos críticos

#### 6.2.2 Validação Externa
1. **Beta Testing:** Usuários reais testam funcionalidades
2. **Feedback Collection:** Coleta estruturada de feedback
3. **Análise de Métricas:** Avaliação de KPIs de uso
4. **Iteração:** Ajustes baseados em feedback
5. **Aprovação Final:** Confirmação de aceitação

### 6.3 Marcos de Validação

#### 6.3.1 Marcos Técnicos
- **M1:** Backend APIs funcionais (Semana 6)
- **M2:** Frontend PWA básico (Semana 8)
- **M3:** Integração completa (Semana 10)
- **M4:** Testes de aceitação (Semana 11)
- **M5:** Beta release (Semana 12)

#### 6.3.2 Marcos de Negócio
- **B1:** Validação de conceito (Semana 4)
- **B2:** Protótipo funcional (Semana 8)
- **B3:** MVP completo (Semana 10)
- **B4:** Validação de usuários (Semana 12)
- **B5:** Product-market fit (Semana 16)

## 7. Gestão de Requisitos

### 7.1 Categorização de Requisitos

#### 7.1.1 Por Tipo
- **Funcionais (RF):** O que o sistema deve fazer
- **Não-Funcionais (RNF):** Como o sistema deve se comportar
- **Negócio (RN):** Regras de negócio específicas
- **Interface (RI):** Requisitos de interface e usabilidade
- **Dados (RD):** Requisitos de dados e informação

#### 7.1.2 Por Prioridade (MoSCoW)
- **Must Have:** Críticos para MVP
- **Should Have:** Importantes mas não críticos
- **Could Have:** Desejáveis se houver tempo
- **Won't Have:** Fora do escopo atual

#### 7.1.3 Por Fase
- **MVP (Fase 1):** Requisitos essenciais
- **Expansão (Fase 2):** Funcionalidades avançadas
- **Escala (Fase 3):** Requisitos de crescimento

### 7.2 Rastreabilidade de Requisitos

#### 7.2.1 Matriz de Rastreabilidade
| ID Requisito | Descrição | Prioridade | Fase | Componente | Status | Testes |
|--------------|-----------|------------|------|------------|--------|---------|
| RF-CV-001 | Upload de CV | Must | MVP | Backend | Em Desenvolvimento | TC-001 |
| RF-CV-002 | Parsing de CV | Must | MVP | Backend | Planejado | TC-002 |
| ... | ... | ... | ... | ... | ... | ... |

#### 7.2.2 Relacionamentos
- **Requisito → Componente:** Onde é implementado
- **Requisito → Teste:** Como é validado
- **Requisito → História de Usuário:** Contexto de uso
- **Requisito → Critério de Aceitação:** Como aceitar

### 7.3 Processo de Mudança de Requisitos

#### 7.3.1 Solicitação de Mudança
1. **Origem:** Feedback de usuários, mudança de negócio, descoberta técnica
2. **Análise:** Impacto em outros requisitos e componentes
3. **Aprovação:** Conforme processo de controle de mudanças
4. **Atualização:** Documentação e matriz de rastreabilidade
5. **Comunicação:** Informar equipe e stakeholders

#### 7.3.2 Versionamento
- **ERS.md:** Documento principal de requisitos
- **Controle de Versão:** Git para histórico completo
- **Tags:** Marcos importantes marcados
- **Changelog:** Registro de mudanças significativas

## 8. Métricas de Controle do Escopo

### 8.1 Métricas de Progresso

#### 8.1.1 Métricas de Entrega
- **Percentual de Conclusão:** Entregas concluídas / Total planejado
- **Velocity:** Pontos de história entregues por sprint
- **Burn-down:** Trabalho restante ao longo do tempo
- **Burn-up:** Trabalho concluído ao longo do tempo
- **Eficiência de Entrega:** Entregas aceitas / Entregas desenvolvidas

#### 8.1.2 Métricas de Qualidade
- **Taxa de Defeitos:** Bugs encontrados / Funcionalidades entregues
- **Cobertura de Testes:** Linhas testadas / Total de linhas
- **Tempo de Correção:** Tempo médio para corrigir bugs
- **Satisfação do Usuário:** NPS e feedback qualitativo
- **Performance:** Tempo de resposta e disponibilidade

### 8.2 Métricas de Controle de Mudanças

#### 8.2.1 Volume de Mudanças
- **Taxa de Mudanças:** Mudanças solicitadas / Período
- **Taxa de Aprovação:** Mudanças aprovadas / Solicitadas
- **Impacto Médio:** Horas de trabalho por mudança
- **Origem das Mudanças:** Distribuição por fonte

#### 8.2.2 Impacto das Mudanças
- **Desvio de Cronograma:** Atraso causado por mudanças
- **Desvio de Orçamento:** Custo adicional por mudanças
- **Scope Creep:** Crescimento não controlado do escopo
- **Retrabalho:** Trabalho descartado por mudanças

### 8.3 Dashboard de Métricas

#### 8.3.1 Métricas em Tempo Real
- **Status das Entregas:** Verde/Amarelo/Vermelho
- **Progresso Geral:** Percentual de conclusão
- **Próximos Marcos:** Datas e status
- **Riscos Ativos:** Riscos que podem afetar escopo

#### 8.3.2 Relatórios Periódicos
- **Semanal:** Progresso e impedimentos
- **Mensal:** Análise de tendências e métricas
- **Por Marco:** Avaliação completa de entrega
- **Final:** Lições aprendidas e métricas finais

## 9. Riscos Relacionados ao Escopo

### 9.1 Identificação de Riscos

#### 9.1.1 Riscos de Scope Creep
- **R-ESC-001:** Solicitações constantes de novas funcionalidades
- **R-ESC-002:** Mudanças de requisitos por feedback de usuários
- **R-ESC-003:** Descobertas técnicas que exigem retrabalho
- **R-ESC-004:** Pressão de stakeholders por funcionalidades adicionais

#### 9.1.2 Riscos de Entrega
- **R-ENT-001:** Subestimação de complexidade técnica
- **R-ENT-002:** Dependências externas não controladas
- **R-ENT-003:** Problemas de integração entre componentes
- **R-ENT-004:** Mudanças em APIs ou serviços externos

### 9.2 Estratégias de Mitigação

#### 9.2.1 Prevenção de Scope Creep
- **Documentação Clara:** Requisitos bem definidos e comunicados
- **Processo Rigoroso:** Controle de mudanças estruturado
- **Educação de Stakeholders:** Comunicação sobre impactos
- **Foco no MVP:** Manter foco nas funcionalidades essenciais

#### 9.2.2 Garantia de Entregas
- **Planejamento Conservador:** Estimativas com margem de segurança
- **Validação Contínua:** Testes e feedback frequentes
- **Alternativas Técnicas:** Planos B para componentes críticos
- **Monitoramento Ativo:** Acompanhamento de progresso e riscos

### 9.3 Planos de Contingência

#### 9.3.1 Cenário: Scope Creep Significativo
- **Gatilho:** > 20% de aumento no escopo original
- **Resposta:** Revisão completa de prioridades e cronograma
- **Ações:** Renegociação de marcos, possível descarte de funcionalidades
- **Responsável:** Maestro + @AgenteM_Orquestrador

#### 9.3.2 Cenário: Atraso Crítico em Entrega
- **Gatilho:** > 2 semanas de atraso em marco crítico
- **Resposta:** Análise de causa raiz e replanejamento
- **Ações:** Priorização de funcionalidades, recursos adicionais
- **Responsável:** Maestro

## 10. Lições Aprendidas

### 10.1 Processo de Captura

#### 10.1.1 Momentos de Captura
- **Fim de Sprint:** Retrospectivas de desenvolvimento
- **Marcos Principais:** Análise de entregas significativas
- **Mudanças Importantes:** Aprendizados de mudanças de escopo
- **Fim de Fase:** Avaliação completa da fase
- **Fim de Projeto:** Consolidação de todos os aprendizados

#### 10.1.2 Categorias de Lições
- **Planejamento:** Estimativas, definição de escopo, priorização
- **Execução:** Desenvolvimento, testes, integração
- **Controle:** Mudanças, qualidade, riscos
- **Comunicação:** Stakeholders, equipe, documentação
- **Ferramentas:** Tecnologias, processos, metodologias

### 10.2 Aplicação Futura

#### 10.2.1 Melhorias de Processo
- **Templates Atualizados:** Incorporar aprendizados em templates
- **Checklists Melhorados:** Adicionar verificações baseadas em lições
- **Estimativas Refinadas:** Usar dados históricos para melhor precisão
- **Riscos Identificados:** Atualizar registro de riscos conhecidos

#### 10.2.2 Capacitação
- **Documentação:** Registrar melhores práticas identificadas
- **Treinamento:** Incorporar lições em processos de onboarding
- **Mentoria:** Compartilhar experiências com outros projetos
- **Comunidade:** Contribuir para conhecimento da comunidade tech

---

## 11. Aprovação e Controle de Versões

**Aprovado por:** Bruno S. Rosa (Maestro)  
**Data de Aprovação:** Junho 2025  
**Próxima Revisão:** Setembro 2025  

**Histórico de Versões:**
- v0.9 (Mai 2025): Versão inicial com metodologia Solo Ágil Aumentado por IA
- v1.0 (Jun 2025): Revisão interativa com correções de nomenclatura e estrutura

**Documentos Relacionados:**
- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica
- [[docs/02_Requisitos/01_ERS.md]] - Especificação de Requisitos
- [[docs/03_Arquitetura_e_Design/01_HLD.md]] - Arquitetura de Alto Nível
- [[docs/00_Gerenciamento_Projeto/00_TAP.md]] - Termo de Abertura
- [[docs/00_Gerenciamento_Projeto/04_PGR.md]] - Gestão de Riscos
- [[docs/00_Gerenciamento_Projeto/06_PGQ.md]] - Gestão de Qualidade
- [[docs/00_Gerenciamento_Projeto/01_KANBAN_INTERNO_PROJETO.md]] - Prioridades

**Anexos:**
- Matriz de Rastreabilidade de Requisitos
- Templates de Solicitação de Mudança
- Checklists de Validação
- Formulários de Lições Aprendidas

--- FIM DO DOCUMENTO PGP.md (v1.0) ---