# Plano de Gerenciamento da Qualidade (PGQ) - Recoloca.AI

---
**Versão:** 1.0 (Aprovado)  
**Data:** Junho 2025  
**Responsável:** Bruno S. Rosa (Maestro)  
**Próxima Revisão:** Setembro 2025  

---

## 1. Introdução

### 1.1 Objetivo
Este documento define como a qualidade será planejada, gerenciada e controlada no projeto Recoloca.AI, estabelecendo padrões, processos, métricas e responsabilidades para garantir que o produto final atenda aos requisitos de qualidade e às expectativas dos usuários.

### 1.2 Escopo do Documento
O plano abrange:
- Política e objetivos de qualidade
- Padrões e métricas de qualidade
- Processos de garantia e controle de qualidade
- **Orquestração de Agentes IA para Qualidade**
- **Sistema RAG para Gestão de Conhecimento de Qualidade**
- Planos de teste e validação
- Gestão de defeitos e melhorias
- Revisões e auditorias de qualidade
- **Métricas de "Specialized Intelligence" para Qualidade**

## 2. Política de Qualidade

### 2.1 Declaração de Política
**"O Recoloca.AI compromete-se a entregar uma solução de alta qualidade que atenda às necessidades dos profissionais de TI brasileiros, priorizando usabilidade, confiabilidade, segurança e performance, através de processos contínuos de validação, teste e melhoria."**

### 2.2 Princípios de Qualidade

#### 2.2.1 Foco no Usuário
- Experiência do usuário como prioridade máxima
- Validação contínua com usuários reais
- Feedback incorporado em todas as iterações
- Acessibilidade e inclusão

#### 2.2.2 Excelência Técnica
- Código limpo e bem documentado
- Arquitetura robusta e escalável
- Testes automatizados abrangentes
- Performance otimizada

#### 2.2.3 Melhoria Contínua
- Retrospectivas regulares
- Métricas de qualidade monitoradas
- Processo de lições aprendidas
- Evolução baseada em dados

#### 2.2.4 Transparência
- Documentação completa e atualizada
- Comunicação clara de problemas
- Rastreabilidade de decisões
- Visibilidade de métricas

#### 2.2.5 Inteligência Especializada ("Specialized Intelligence")
- **Orquestração de Agentes IA:** Especialização por domínio de qualidade
- **Sistema RAG Integrado:** Base de conhecimento viva para padrões e melhores práticas
- **Automação Inteligente:** Detecção proativa de problemas de qualidade
- **Aprendizado Contínuo:** Evolução baseada em feedback e métricas

## 3. Objetivos de Qualidade

### 3.1 Objetivos Funcionais

#### 3.1.1 Precisão da Análise
- **Meta:** ≥ 85% de precisão na extração de informações de CV
- **Medição:** Comparação com análise manual de amostra
- **Frequência:** Semanal durante desenvolvimento, diária em produção

#### 3.1.2 Completude Funcional
- **Meta:** 100% dos requisitos Must Have implementados
- **Medição:** Checklist de requisitos vs funcionalidades entregues
- **Frequência:** A cada entrega/sprint

#### 3.1.3 Usabilidade
- **Meta:** ≥ 4.0/5.0 em pesquisas de satisfação
- **Medição:** Surveys com usuários beta
- **Frequência:** Mensal durante testes beta

### 3.2 Objetivos Não-Funcionais

#### 3.2.1 Performance
- **Tempo de Resposta:** ≤ 3 segundos para análise de CV
- **Throughput:** ≥ 10 análises simultâneas
- **Disponibilidade:** ≥ 99% uptime
- **Escalabilidade:** Suporte a 1000+ usuários simultâneos

#### 3.2.2 Segurança
- **Conformidade LGPD:** 100% dos requisitos atendidos
- **Criptografia:** Dados sensíveis sempre criptografados
- **Autenticação:** Sistema robusto de controle de acesso
- **Vulnerabilidades:** Zero vulnerabilidades críticas

#### 3.2.3 Confiabilidade
- **Taxa de Erro:** ≤ 0.1% de falhas em operações críticas
- **Recuperação:** ≤ 5 minutos para recuperação de falhas
- **Consistência:** 100% de consistência de dados
- **Backup:** Backup automático diário com teste de restauração

### 3.3 Objetivos de Processo

#### 3.3.1 Cobertura de Testes
- **Testes Unitários:** ≥ 80% de cobertura de código
- **Testes de Integração:** 100% dos fluxos críticos
- **Testes E2E:** 100% dos casos de uso principais

#### 3.3.2 Orquestração de Agentes IA para Qualidade
- **Eficiência de Orquestração:** ≥ 90% de tarefas de qualidade executadas com sucesso pelos agentes
- **Tempo de Resposta de Agentes:** ≤ 30 segundos para análises de qualidade
- **Cobertura de Especialização:** 100% dos domínios de qualidade cobertos por agentes especializados
- **Qualidade das Análises:** ≥ 85% de precisão nas recomendações de agentes

#### 3.3.3 Sistema RAG para Gestão de Conhecimento
- **Performance de Recuperação:** ≤ 2 segundos para consultas à base de conhecimento
- **Relevância de Resultados:** ≥ 90% de consultas retornam informações relevantes
- **Cobertura da Base:** 100% dos padrões e processos de qualidade indexados
- **Atualização Contínua:** Base de conhecimento atualizada semanalmente
- **Testes de Performance:** 100% dos endpoints críticos

#### 3.3.2 Qualidade de Código
- **Code Review:** 100% do código revisado
- **Padrões:** Conformidade com style guides
- **Complexidade:** Complexidade ciclomática ≤ 10
- **Duplicação:** ≤ 3% de código duplicado

## 4. Padrões de Qualidade

### 4.1 Padrões de Desenvolvimento

#### 4.1.1 Padrões de Código
- **Python (Backend):**
  - PEP 8 para style guide
  - Type hints obrigatórios
  - Docstrings para funções públicas
  - Pylint score ≥ 8.0

- **Dart/Flutter (Frontend):**
  - Effective Dart guidelines
  - Análise estática com dart analyze
  - Documentação de widgets customizados
  - Flutter lints configurado

#### 4.1.2 Padrões de Arquitetura
- **Clean Architecture:** Separação clara de responsabilidades
- **SOLID Principles:** Aplicação consistente
- **Design Patterns:** Uso apropriado e documentado
- **API Design:** RESTful com OpenAPI/Swagger

#### 4.1.3 Padrões de Documentação
- **Código:** Comentários claros e concisos
- **APIs:** Documentação OpenAPI completa
- **Arquitetura:** Diagramas atualizados
- **Processos:** Runbooks e guias operacionais

### 4.2 Padrões de Interface

#### 4.2.1 Design System
- **Consistência Visual:** Componentes padronizados
- **Acessibilidade:** WCAG 2.1 AA compliance
- **Responsividade:** Design mobile-first
- **Performance:** Otimização de assets

#### 4.2.2 Experiência do Usuário
- **Usabilidade:** Heurísticas de Nielsen
- **Feedback:** Indicadores visuais claros
- **Navegação:** Fluxos intuitivos
- **Erro Handling:** Mensagens amigáveis

### 4.3 Padrões de Segurança

#### 4.3.1 Desenvolvimento Seguro
- **OWASP Top 10:** Mitigação de vulnerabilidades
- **Input Validation:** Sanitização de entradas
- **Authentication:** JWT com refresh tokens
- **Authorization:** RBAC implementado

#### 4.3.2 Proteção de Dados
- **Criptografia:** AES-256 para dados em repouso
- **Transmissão:** TLS 1.3 para dados em trânsito
- **Logs:** Não exposição de dados sensíveis
- **Backup:** Criptografia de backups

## 5. Processos de Qualidade

### 5.1 Garantia de Qualidade (QA)

#### 5.1.1 Planejamento de Qualidade
- **Definição de Critérios:** Para cada funcionalidade
- **Estratégia de Testes:** Baseada em riscos
- **Recursos Necessários:** Ferramentas e ambiente
- **Cronograma:** Integrado ao desenvolvimento

#### 5.1.2 Revisões de Qualidade
- **Code Reviews:** Obrigatórias para todo código
- **Design Reviews:** Validação de arquitetura
- **Requirements Reviews:** Clareza e completude
- **Test Plan Reviews:** Cobertura adequada

#### 5.1.3 Auditorias de Processo
- **Frequência:** Mensal
- **Escopo:** Aderência aos padrões definidos
- **Responsável:** @AgenteM_Orquestrador + Maestro
- **Ações:** Planos de melhoria quando necessário

#### 5.1.4 Orquestração de Agentes IA para Qualidade
- **@AgenteM_QualityAssurance:** Análise automatizada de padrões de qualidade
- **@AgenteM_TestingSpecialist:** Geração e execução de casos de teste
- **@AgenteM_SecurityAuditor:** Auditoria contínua de segurança
- **@AgenteM_PerformanceAnalyst:** Monitoramento e otimização de performance
- **Sistema RAG:** Base de conhecimento para melhores práticas e padrões

### 5.2 Controle de Qualidade (QC)

#### 5.2.1 Testes de Software

**Testes Unitários**
- **Responsabilidade:** Desenvolvedor (Maestro)
- **Cobertura:** ≥ 80% do código
- **Ferramentas:** pytest (Python), test (Dart)
- **Execução:** Automática no CI/CD

**Testes de Integração**
- **Responsabilidade:** Maestro
- **Escopo:** APIs e integrações externas
- **Ferramentas:** pytest + requests, integration_test (Flutter)
- **Execução:** A cada build

**Testes End-to-End**
- **Responsabilidade:** Maestro
- **Escopo:** Fluxos críticos de usuário
- **Ferramentas:** Playwright ou Selenium
- **Execução:** Antes de cada release

**Testes de Performance**
- **Responsabilidade:** Maestro
- **Escopo:** APIs críticas e frontend
- **Ferramentas:** Locust, Lighthouse
- **Execução:** Semanal e antes de releases

**Testes de Segurança**
- **Responsabilidade:** Maestro + Consultoria externa
- **Escopo:** Vulnerabilidades e conformidade
- **Ferramentas:** OWASP ZAP, Bandit
- **Execução:** Mensal e antes de releases

#### 5.2.2 Testes de Usabilidade

**Testes com Usuários**
- **Frequência:** Quinzenal durante desenvolvimento
- **Participantes:** 5-8 usuários por sessão
- **Método:** Think-aloud protocol
- **Métricas:** Task completion rate, time on task, satisfaction

**Testes de Acessibilidade**
- **Ferramentas:** axe-core, WAVE
- **Padrão:** WCAG 2.1 AA
- **Frequência:** A cada nova funcionalidade
- **Validação:** Testes com screen readers

### 5.3 Gestão de Defeitos

#### 5.3.1 Classificação de Defeitos

**Por Severidade:**
- **Crítica:** Sistema inutilizável ou perda de dados
- **Alta:** Funcionalidade principal não funciona
- **Média:** Funcionalidade secundária com problemas
- **Baixa:** Problemas cosméticos ou de usabilidade

**Por Prioridade:**
- **P1:** Correção imediata (< 24h)
- **P2:** Correção urgente (< 72h)
- **P3:** Correção na próxima release
- **P4:** Correção quando possível

#### 5.3.2 Processo de Resolução

1. **Detecção:** Identificação do defeito
2. **Registro:** Documentação no sistema de tracking
3. **Triagem:** Classificação e priorização
4. **Atribuição:** Designação para correção
5. **Correção:** Implementação da solução
6. **Verificação:** Teste da correção
7. **Fechamento:** Confirmação da resolução

#### 5.3.3 Métricas de Defeitos
- **Densidade:** Defeitos por KLOC (mil linhas de código)
- **Taxa de Detecção:** % de defeitos encontrados em testes
- **Tempo de Resolução:** Tempo médio por severidade
- **Taxa de Reincidência:** % de defeitos que retornam

## 6. Ferramentas de Qualidade

### 6.1 Ferramentas de Desenvolvimento

#### 6.1.1 Análise Estática
- **Python:** pylint, black, mypy, bandit
- **Dart:** dart analyze, dart format
- **Geral:** SonarQube (futuro)

#### 6.1.2 Testes Automatizados
- **Backend:** pytest, coverage.py, factory_boy
- **Frontend:** test (Dart), mockito, integration_test
- **E2E:** Playwright ou Selenium
- **Performance:** Locust, k6

#### 6.1.3 CI/CD
- **GitHub Actions:** Pipeline automatizado
- **Quality Gates:** Critérios de qualidade obrigatórios
- **Deployment:** Automático após aprovação
- **Rollback:** Processo automatizado

### 6.2 Ferramentas de Monitoramento

#### 6.2.1 Aplicação
- **Logs:** Estruturados com correlação
- **Métricas:** Prometheus + Grafana (futuro)
- **APM:** Sentry para error tracking
- **Uptime:** UptimeRobot ou similar

#### 6.2.2 Usuário
- **Analytics:** Google Analytics 4
- **Heatmaps:** Hotjar
- **Feedback:** Sistema integrado na aplicação
- **Surveys:** Typeform ou similar

### 6.3 Ferramentas de Gestão

#### 6.3.1 Tracking
- **Issues:** GitHub Issues
- **Projeto:** GitHub Projects
- **Documentação:** Obsidian + Git
- **Comunicação:** Slack (futuro)

#### 6.3.2 Qualidade
- **Code Review:** GitHub Pull Requests
- **Testing:** Relatórios automatizados
- **Metrics:** Dashboards customizados
- **Compliance:** Checklists e auditorias

#### 6.3.3 Orquestração de Agentes IA
- **Trae IDE:** Ambiente integrado para orquestração
- **Sistema RAG:** Base de conhecimento viva (MCP Server)
- **Agentes Especializados:** Tier 1 para domínios específicos de qualidade
- **Dashboard de Orquestração:** Monitoramento de performance dos agentes
- **Métricas de "Specialized Intelligence":** KPIs específicos por agente

## 7. Métricas de Qualidade

### 7.1 Métricas de Produto

#### 7.1.1 Funcionalidade
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Precisão da análise de CV | ≥ 85% | Comparação manual | Semanal |
| Completude de features | 100% Must Have | Checklist | Por sprint |
| Taxa de sucesso de upload | ≥ 95% | Logs de sistema | Diária |
| Tempo de processamento | ≤ 30s | Métricas de API | Contínua |

#### 7.1.2 Usabilidade
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Satisfação do usuário | ≥ 4.0/5.0 | Surveys | Mensal |
| Task completion rate | ≥ 90% | Testes de usabilidade | Quinzenal |
| Time on task | Baseline -20% | Observação | Quinzenal |
| Error rate | ≤ 5% | Analytics | Semanal |

#### 7.1.3 Performance
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Page load time | ≤ 3s | Lighthouse | Diária |
| API response time | ≤ 500ms | APM | Contínua |
| Uptime | ≥ 99% | Monitoring | Contínua |
| Error rate | ≤ 0.1% | Logs | Contínua |

### 7.2 Métricas de Processo

#### 7.2.1 Desenvolvimento
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Code coverage | ≥ 80% | Coverage tools | Por commit |
| Code review coverage | 100% | GitHub | Por PR |
| Build success rate | ≥ 95% | CI/CD | Contínua |
| Deployment frequency | 2x/semana | Git logs | Semanal |

#### 7.2.2 Qualidade
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Defect density | ≤ 1/KLOC | Issue tracking | Mensal |
| Defect resolution time | ≤ 48h (P1-P2) | Issue tracking | Semanal |
| Test execution rate | 100% | Test reports | Por release |
| Customer satisfaction | ≥ 4.0/5.0 | Feedback | Mensal |

#### 7.2.3 Orquestração de Agentes IA
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Eficiência de Orquestração | ≥ 90% | Dashboard Agentes | Diária |
| Tempo Resposta Agentes | ≤ 30s | Logs de Performance | Contínua |
| Precisão Análises IA | ≥ 85% | Validação Manual | Semanal |
| Cobertura Especialização | 100% | Mapeamento Domínios | Mensal |

#### 7.2.4 Sistema RAG
| Métrica | Meta | Medição | Frequência |
|---------|------|---------|------------|
| Performance Recuperação | ≤ 2s | Logs RAG | Contínua |
| Relevância Resultados | ≥ 90% | Feedback Usuários | Semanal |
| Cobertura Base Conhecimento | 100% | Auditoria Conteúdo | Mensal |
| Taxa Atualização | Semanal | Logs Sistema | Contínua |

### 7.3 Dashboards de Qualidade

#### 7.3.1 Dashboard Executivo
- **Visão Geral:** Status de qualidade consolidado
- **Tendências:** Evolução das métricas principais
- **Alertas:** Problemas que requerem atenção
- **Ações:** Próximos passos recomendados

#### 7.3.2 Dashboard Técnico
- **Code Quality:** Métricas de código e testes
- **Performance:** Tempos de resposta e throughput
- **Errors:** Taxa de erros e incidentes
- **Deployment:** Status e frequência de releases

#### 7.3.3 Dashboard de Usuário
- **Satisfaction:** Pesquisas e feedback
- **Usage:** Padrões de uso e adoção
- **Issues:** Problemas reportados pelos usuários
- **Features:** Solicitações e sugestões

#### 7.3.4 Dashboard de Orquestração IA
- **Performance Agentes:** Métricas de eficiência por agente especializado
- **Sistema RAG:** Status e performance da base de conhecimento
- **"Specialized Intelligence":** KPIs de inteligência especializada
- **Orquestração:** Fluxos de trabalho e automação

## 8. Plano de Testes

### 8.1 Estratégia de Testes

#### 8.1.1 Pirâmide de Testes
```
        E2E Tests (10%)
      ─────────────────
    Integration Tests (20%)
   ─────────────────────────
     Unit Tests (70%)
  ───────────────────────────
```

#### 8.1.2 Tipos de Teste por Fase

**Desenvolvimento (Contínuo):**
- Testes unitários
- Testes de integração
- Análise estática de código
- Code review

**Pré-Release (Semanal):**
- Testes end-to-end
- Testes de performance
- Testes de segurança
- Testes de usabilidade

**Release (Por versão):**
- Testes de aceitação
- Testes de regressão
- Testes de carga
- Validação de produção

### 8.2 Casos de Teste Críticos

#### 8.2.1 Fluxo Principal
1. **Cadastro de Usuário**
   - Registro com email válido
   - Confirmação de email
   - Login inicial

2. **Upload de CV**
   - Upload de PDF válido
   - Validação de formato
   - Processamento bem-sucedido

3. **Análise de CV**
   - Extração de informações
   - Geração de insights
   - Exibição de resultados

4. **Dashboard**
   - Visualização de dados
   - Navegação entre seções
   - Atualização de informações

#### 8.2.2 Cenários de Erro
1. **Upload Inválido**
   - Arquivo corrompido
   - Formato não suportado
   - Tamanho excessivo

2. **Falhas de Sistema**
   - Indisponibilidade de API
   - Timeout de processamento
   - Erro de banco de dados

3. **Problemas de Rede**
   - Conexão instável
   - Latência alta
   - Perda de conectividade

### 8.3 Ambiente de Testes

#### 8.3.1 Ambientes
- **Development:** Desenvolvimento local
- **Staging:** Ambiente de homologação
- **Production:** Ambiente de produção

#### 8.3.2 Dados de Teste
- **Sintéticos:** Gerados automaticamente
- **Anonimizados:** Baseados em dados reais
- **Específicos:** Para cenários particulares

## 9. Gestão de Riscos de Qualidade

### 9.1 Riscos Identificados

#### 9.1.1 Riscos Técnicos
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|----------|
| Baixa precisão da IA | Média | Alto | Testes extensivos, fine-tuning |
| Performance inadequada | Baixa | Alto | Testes de carga, otimização |
| Problemas de segurança | Baixa | Crítico | Auditorias, testes de penetração |
| Bugs críticos | Média | Alto | Code review, testes automatizados |

#### 9.1.2 Riscos de Processo
| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|----------|
| Falta de testes | Baixa | Alto | Processo obrigatório, métricas |
| Documentação inadequada | Média | Médio | Templates, revisões |
| Feedback tardio | Média | Médio | Testes frequentes com usuários |
| Scope creep | Média | Médio | Controle rigoroso de mudanças |

### 9.2 Planos de Contingência

#### 9.2.1 Problemas de Qualidade
- **Detecção Precoce:** Métricas e alertas
- **Resposta Rápida:** Processo de escalação
- **Correção:** Hotfixes quando necessário
- **Prevenção:** Análise de causa raiz

#### 9.2.2 Falhas de Processo
- **Identificação:** Auditorias regulares
- **Correção:** Planos de ação imediatos
- **Melhoria:** Atualização de processos
- **Treinamento:** Capacitação quando necessário

## 10. Melhoria Contínua

### 10.1 Processo de Melhoria

#### 10.1.1 Ciclo PDCA
- **Plan:** Identificação de oportunidades
- **Do:** Implementação de melhorias
- **Check:** Verificação de resultados
- **Act:** Padronização de melhorias

#### 10.1.2 Fontes de Melhoria
- **Métricas:** Análise de tendências
- **Feedback:** Usuários e stakeholders
- **Retrospectivas:** Lições aprendidas
- **Benchmarking:** Melhores práticas do mercado

### 10.2 Lições Aprendidas

#### 10.2.1 Captura
- **Retrospectivas:** Semanais/quinzenais
- **Post-mortems:** Após incidentes
- **Feedback:** Contínuo de usuários
- **Métricas:** Análise de dados

#### 10.2.2 Aplicação
- **Processos:** Atualização baseada em aprendizados
- **Ferramentas:** Adoção de novas tecnologias
- **Treinamento:** Capacitação da equipe
- **Documentação:** Atualização de guias

### 10.3 Inovação em Qualidade

#### 10.3.1 Novas Tecnologias
- **AI/ML:** Para detecção automática de problemas
- **Automation:** Expansão de testes automatizados
- **Monitoring:** Observabilidade avançada
- **Analytics:** Insights baseados em dados
- **Orquestração de Agentes IA:** Especialização por domínio de qualidade
- **Sistema RAG:** Base de conhecimento viva e contextual

#### 10.3.2 Metodologias
- **Shift-Left:** Qualidade desde o início
- **DevOps:** Integração contínua de qualidade
- **User-Centric:** Foco na experiência do usuário
- **Data-Driven:** Decisões baseadas em métricas
- **"Specialized Intelligence":** Inteligência especializada por agente
- **Orquestração Inteligente:** Coordenação automatizada de processos de qualidade

---

## 11. Aprovação e Controle de Versões

**Aprovado por:** Bruno S. Rosa (Maestro)  
**Data de Aprovação:** Junho 2025

---

## 12. Histórico de Versões

| Versão | Data | Autor | Descrição |
|--------|------|-------|----------|
| 1.0 | Junho 2025 | Bruno S. Rosa | Versão inicial do Plano de Gestão de Qualidade |
| 1.1 | Janeiro 2025 | Bruno S. Rosa | Integração da Orquestração de Agentes IA e Sistema RAG para Qualidade |

### Principais Melhorias v1.1:
- **Orquestração de Agentes IA:** Adição de agentes especializados para qualidade (@AgenteM_QualityAssurance, @AgenteM_TestingSpecialist, @AgenteM_SecurityAuditor, @AgenteM_PerformanceAnalyst)
- **Sistema RAG:** Integração de base de conhecimento viva para padrões e melhores práticas
- **Métricas de "Specialized Intelligence":** KPIs específicos para performance de agentes IA
- **Dashboard de Orquestração:** Monitoramento de eficiência e performance dos agentes
- **Metodologia Inovadora:** Incorporação de "Specialized Intelligence" e Orquestração Inteligente

---

## 13. Documentos Relacionados

- **[[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]]** - Visão geral e objetivos do projeto
- **[[docs/00_Gerenciamento_Projeto/03_PGE.md]]** - Plano de Gestão de Escopo
- **[[docs/00_Gerenciamento_Projeto/01_KANBAN_INTERNO_PROJETO.md]]** - Gestão de tarefas e prioridades
- **[[docs/04_Agentes_IA/03_FLUXO_ORQUESTRACAO_AGENTES.md]]** - Metodologia de orquestração
- **[[docs/04_Agentes_IA/02_AGENTES_IA_MENTORES_OVERVIEW.md]]** - Visão geral dos agentes especializados
- **[[docs/02_Requisitos/01_ERS.md]]** - Especificação de requisitos
- **[[docs/03_Arquitetura_e_Design/01_HLD.md]]** - Arquitetura de alto nível  
**Próxima Revisão:** Setembro 2025  

**Histórico de Versões:**
- v0.9 (Maio 2025): Versão inicial para revisão
- v1.0 (Jun 2025): Versão aprovada - Alinhamento com cronograma MVP 16 semanas (Jun-Dez 2025), padronização nomenclatura agentes, integração metodologia "Orquestração Inteligente"

**Documentos Relacionados:**
- [[TAP.md]] - Termo de Abertura do Projeto
- [[PGE.md]] - Plano de Gerenciamento do Escopo
- [[PGC.md]] - Plano de Gerenciamento de Custos
- [[PGR.md]] - Plano de Gerenciamento de Riscos
- [[PCom.md]] - Plano de Gerenciamento das Comunicações
- [[ERS.md]] - Especificação de Requisitos de Software
- [[PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica

**Anexos:**
- Checklists de qualidade
- Templates de casos de teste
- Relatórios de métricas
- Procedimentos de auditoria

--- FIM DO DOCUMENTO PGQ.md (v1.0) ---