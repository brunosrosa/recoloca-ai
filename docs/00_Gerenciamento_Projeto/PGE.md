# Plano de Gerenciamento do Escopo (PGE) - Recoloca.AI

---
**Versão:** 0.9 (Pré-Revisão Interativa)  
**Data:** Dezembro 2024  
**Responsável:** Bruno S. Rosa (Maestro)  
**Próxima Revisão:** Janeiro 2025  

---

## 1. Introdução

### 1.1 Objetivo
Este documento define como o escopo do projeto Recoloca.AI será planejado, definido, controlado e validado ao longo do ciclo de vida do projeto, garantindo que todo o trabalho necessário (e apenas o trabalho necessário) seja incluído para completar o projeto com sucesso.

### 1.2 Escopo do Documento
O plano abrange:
- Definição e documentação do escopo do projeto e do produto
- Criação da Estrutura Analítica do Projeto (EAP)
- Processo de controle de mudanças de escopo
- Validação e aceitação de entregas
- Gestão de requisitos

## 2. Metodologia de Gerenciamento do Escopo

### 2.1 Abordagem "Solo Ágil Aumentado por IA"
O gerenciamento do escopo segue a metodologia do projeto:
- **Iterativo e Incremental:** Desenvolvimento em fases com validação contínua
- **Orientado por Valor:** Priorização baseada no valor para o usuário
- **Flexível:** Adaptação baseada em feedback e aprendizados
- **Aumentado por IA:** Uso de agentes IA para análise e refinamento de requisitos

### 2.2 Processo de Definição do Escopo
1. **Coleta de Requisitos:** Via pesquisa com usuários e análise de mercado
2. **Análise com @AgenteMentorPO:** Refinamento e priorização de requisitos
3. **Validação com Maestro:** Aprovação final e alinhamento estratégico
4. **Documentação:** Registro na [[ERS.md]] e atualização do backlog
5. **Comunicação:** Divulgação via [[PCom.md]]

## 3. Escopo do Projeto

### 3.1 Objetivo do Projeto
Desenvolver o **Recoloca.AI**, um Micro-SaaS para auxiliar profissionais brasileiros de TI na recolocação profissional, utilizando inteligência artificial para análise de currículos e matching com oportunidades.

### 3.2 Objetivos Específicos
- Criar uma plataforma web (PWA) para upload e análise de currículos
- Implementar sistema de IA para extração e análise de informações profissionais
- Desenvolver algoritmo de matching entre perfis e vagas
- Fornecer sugestões personalizadas de melhoria de perfil
- Estabelecer dashboard para acompanhamento do progresso

### 3.3 Critérios de Sucesso
- **Técnicos:**
  - Precisão da análise de CV ≥ 85%
  - Tempo de processamento ≤ 30 segundos
  - Disponibilidade do sistema ≥ 99%
  - Compatibilidade com principais navegadores

- **Negócio:**
  - Satisfação do usuário ≥ 4.0/5.0
  - Taxa de conversão ≥ 15%
  - 100+ usuários beta registrados
  - Validação da proposta de valor

### 3.4 Principais Entregas

#### 3.4.1 MVP (Minimum Viable Product)
- **Frontend PWA (Flutter)**
  - Interface de upload de CV
  - Dashboard do usuário
  - Visualização de análises e sugestões
  - Sistema de autenticação

- **Backend API (FastAPI)**
  - Endpoints para upload e processamento
  - Sistema de análise com IA
  - Integração com Supabase
  - Sistema de matching básico

- **Sistema RAG**
  - Processamento de PDFs
  - Extração de informações
  - Análise semântica
  - Base de conhecimento

#### 3.4.2 Pós-MVP (Roadmap Futuro)
- **Extensão Chrome**
  - Captura automática de vagas
  - Análise de compatibilidade em tempo real
  - Notificações de oportunidades

- **Funcionalidades Avançadas**
  - Sistema de recomendações ML
  - Integração com LinkedIn
  - Análise de mercado de trabalho
  - Relatórios avançados

## 4. Escopo do Produto

### 4.1 Funcionalidades Incluídas (MVP)

#### 4.1.1 Gestão de Currículos
- **RF-CV-001:** Upload de arquivos PDF
- **RF-CV-002:** Validação de formato e conteúdo
- **RF-CV-003:** Extração automática de informações
- **RF-CV-004:** Armazenamento seguro de dados

#### 4.1.2 Análise Inteligente
- **RF-AN-001:** Análise de compatibilidade com vagas
- **RF-AN-002:** Geração de sugestões de melhoria
- **RF-AN-003:** Identificação de gaps de competências
- **RF-AN-004:** Pontuação de perfil profissional

#### 4.1.3 Interface do Usuário
- **RF-UI-001:** Dashboard personalizado
- **RF-UI-002:** Visualização de análises
- **RF-UI-003:** Sistema de notificações
- **RF-UI-004:** Perfil do usuário

#### 4.1.4 Segurança e Autenticação
- **RF-SE-001:** Autenticação via Supabase
- **RF-SE-002:** Controle de acesso
- **RF-SE-003:** Criptografia de dados sensíveis
- **RF-SE-004:** Conformidade com LGPD

### 4.2 Funcionalidades Excluídas (MVP)
- Integração com redes sociais (exceto autenticação)
- Sistema de pagamentos
- Funcionalidades de recrutador/empresa
- Análise de vídeo ou áudio
- Aplicativo mobile nativo
- Integração com ATS externos

### 4.3 Restrições

#### 4.3.1 Técnicas
- **Linguagens:** Python (backend), Dart/Flutter (frontend)
- **Banco de Dados:** PostgreSQL via Supabase
- **IA/LLM:** Google Gemini Pro/Flash
- **Hospedagem:** Plataformas compatíveis com stack escolhida

#### 4.3.2 Regulamentares
- Conformidade com LGPD
- Proteção de dados pessoais
- Termos de uso e política de privacidade

#### 4.3.3 Orçamentárias
- Desenvolvimento solo com suporte de IA
- Uso de ferramentas gratuitas/freemium quando possível
- Foco em MVP para validação antes de investimentos maiores

## 5. Estrutura Analítica do Projeto (EAP)

### 5.1 EAP - Nível 1
```
Recoloca.AI
├── 1. Gestão do Projeto
├── 2. Análise e Design
├── 3. Desenvolvimento
├── 4. Testes e Qualidade
├── 5. Deploy e Operações
└── 6. Validação e Entrega
```

### 5.2 EAP - Nível 2 (Detalhado)

#### 1. Gestão do Projeto
- 1.1 Planejamento inicial
- 1.2 Documentação de requisitos
- 1.3 Gestão de riscos
- 1.4 Controle de mudanças
- 1.5 Comunicação e relatórios

#### 2. Análise e Design
- 2.1 Pesquisa com usuários
- 2.2 Definição de requisitos
- 2.3 Arquitetura do sistema
- 2.4 Design de interface
- 2.5 Modelagem de dados

#### 3. Desenvolvimento
- 3.1 Setup do ambiente
- 3.2 Backend (FastAPI)
  - 3.2.1 APIs de autenticação
  - 3.2.2 APIs de upload
  - 3.2.3 Sistema RAG
  - 3.2.4 Análise com IA
- 3.3 Frontend (Flutter PWA)
  - 3.3.1 Autenticação
  - 3.3.2 Upload de CV
  - 3.3.3 Dashboard
  - 3.3.4 Visualizações
- 3.4 Integração de sistemas

#### 4. Testes e Qualidade
- 4.1 Testes unitários
- 4.2 Testes de integração
- 4.3 Testes de usabilidade
- 4.4 Testes de performance
- 4.5 Testes de segurança

#### 5. Deploy e Operações
- 5.1 Configuração de infraestrutura
- 5.2 Deploy de produção
- 5.3 Monitoramento
- 5.4 Backup e recuperação

#### 6. Validação e Entrega
- 6.1 Testes beta
- 6.2 Coleta de feedback
- 6.3 Ajustes finais
- 6.4 Entrega do MVP

## 6. Processo de Controle de Mudanças

### 6.1 Tipos de Mudanças

#### 6.1.1 Mudanças Menores (Aprovação Automática)
- Correções de bugs
- Melhorias de UX sem impacto funcional
- Otimizações de performance
- Atualizações de documentação

#### 6.1.2 Mudanças Moderadas (Aprovação do Maestro)
- Novos requisitos não-funcionais
- Alterações de design significativas
- Mudanças de tecnologia secundária
- Ajustes de cronograma < 1 semana

#### 6.1.3 Mudanças Maiores (Análise Completa)
- Novos requisitos funcionais
- Mudanças de arquitetura
- Alterações de tecnologia core
- Impacto no cronograma > 1 semana
- Mudanças de escopo do MVP

### 6.2 Processo de Solicitação de Mudança

1. **Identificação:** Detecção da necessidade de mudança
2. **Documentação:** Registro formal da solicitação
3. **Análise de Impacto:** Avaliação com @AgenteOrquestrador
   - Impacto no cronograma
   - Impacto no orçamento
   - Impacto técnico
   - Impacto nos objetivos
4. **Decisão:** Aprovação/rejeição pelo Maestro
5. **Implementação:** Execução da mudança aprovada
6. **Comunicação:** Atualização de stakeholders
7. **Documentação:** Atualização da documentação

### 6.3 Comitê de Controle de Mudanças
- **Maestro (Bruno S. Rosa):** Decisor final
- **@AgenteOrquestrador:** Análise de impacto e recomendações
- **Agentes Especializados:** Consulta técnica conforme necessário

## 7. Validação e Aceitação de Entregas

### 7.1 Critérios de Aceitação

#### 7.1.1 Critérios Técnicos
- Todos os testes unitários passando
- Cobertura de testes ≥ 80%
- Performance dentro dos parâmetros definidos
- Segurança validada
- Documentação técnica completa

#### 7.1.2 Critérios Funcionais
- Todos os requisitos funcionais implementados
- Casos de teste de aceitação passando
- Interface de usuário conforme design aprovado
- Fluxos de trabalho funcionando corretamente

#### 7.1.3 Critérios de Qualidade
- Usabilidade validada com usuários
- Acessibilidade básica implementada
- Compatibilidade com navegadores testada
- Responsividade verificada

### 7.2 Processo de Validação

1. **Validação Técnica:** Testes automatizados e revisão de código
2. **Validação Funcional:** Testes manuais e casos de uso
3. **Validação de Usuário:** Testes com usuários beta
4. **Validação de Negócio:** Verificação de objetivos e métricas
5. **Aprovação Final:** Sign-off do Maestro

### 7.3 Documentação de Aceitação
- **Checklist de Aceitação:** Para cada entrega
- **Relatório de Testes:** Resultados detalhados
- **Feedback de Usuários:** Compilação de comentários
- **Termo de Aceitação:** Documento formal de aprovação

## 8. Gestão de Requisitos

### 8.1 Categorização de Requisitos

#### 8.1.1 Por Prioridade (MoSCoW)
- **Must Have:** Essenciais para o MVP
- **Should Have:** Importantes mas não críticos
- **Could Have:** Desejáveis se houver tempo
- **Won't Have:** Fora do escopo atual

#### 8.1.2 Por Tipo
- **Funcionais:** O que o sistema deve fazer
- **Não-Funcionais:** Como o sistema deve se comportar
- **Técnicos:** Restrições de implementação
- **Negócio:** Objetivos e métricas

### 8.2 Rastreabilidade de Requisitos

#### 8.2.1 Matriz de Rastreabilidade
| Requisito | Origem | Prioridade | Status | Teste | Entrega |
|-----------|--------|------------|--------|-------|----------|
| RF-CV-001 | Pesquisa Usuário | Must | Em Desenvolvimento | TC-001 | Sprint 2 |
| RF-AN-001 | Análise Mercado | Must | Planejado | TC-015 | Sprint 3 |

#### 8.2.2 Ferramentas de Rastreabilidade
- **[[ERS.md]]:** Especificação completa
- **[[KANBAN_INTERNO_PROJETO.md]]:** Status de desenvolvimento
- **Casos de Teste:** Validação de implementação
- **Git Issues:** Tracking de implementação

### 8.3 Processo de Mudança de Requisitos

1. **Solicitação:** Via stakeholder ou descoberta técnica
2. **Análise:** Impacto no escopo, cronograma e recursos
3. **Priorização:** Usando framework MoSCoW
4. **Aprovação:** Decisão do Maestro
5. **Atualização:** Documentação e comunicação
6. **Implementação:** Inclusão no backlog

## 9. Métricas de Controle do Escopo

### 9.1 Indicadores de Performance

#### 9.1.1 Métricas de Escopo
- **Estabilidade do Escopo:** % de mudanças aprovadas vs solicitadas
- **Completude:** % de requisitos implementados vs planejados
- **Qualidade:** % de entregas aceitas na primeira tentativa
- **Satisfação:** Feedback dos usuários beta

#### 9.1.2 Métricas de Processo
- **Tempo de Análise:** Tempo médio para avaliar mudanças
- **Taxa de Aprovação:** % de mudanças aprovadas
- **Impacto Médio:** Impacto médio das mudanças no cronograma
- **Eficiência:** Velocidade de implementação de requisitos

### 9.2 Relatórios de Acompanhamento

#### 9.2.1 Relatório Semanal
- Status dos requisitos em desenvolvimento
- Mudanças solicitadas e aprovadas
- Riscos identificados relacionados ao escopo
- Próximas entregas planejadas

#### 9.2.2 Relatório Mensal
- Análise de tendências de mudanças
- Avaliação da estabilidade do escopo
- Impacto cumulativo das mudanças
- Recomendações de ajustes

## 10. Riscos Relacionados ao Escopo

### 10.1 Principais Riscos

#### 10.1.1 Scope Creep
- **Descrição:** Expansão não controlada do escopo
- **Probabilidade:** Média
- **Impacto:** Alto
- **Mitigação:** Processo rigoroso de controle de mudanças

#### 10.1.2 Requisitos Mal Definidos
- **Descrição:** Ambiguidade ou incompletude nos requisitos
- **Probabilidade:** Média
- **Impacto:** Alto
- **Mitigação:** Validação contínua com usuários e @AgenteMentorPO

#### 10.1.3 Mudanças de Prioridade
- **Descrição:** Alterações frequentes nas prioridades
- **Probabilidade:** Baixa
- **Impacto:** Médio
- **Mitigação:** Framework claro de priorização (MoSCoW)

### 10.2 Plano de Contingência
- **Scope Creep:** Congelamento temporário de mudanças
- **Requisitos Mal Definidos:** Sessões de refinamento com stakeholders
- **Mudanças de Prioridade:** Revisão do business case

## 11. Lições Aprendidas e Melhoria Contínua

### 11.1 Processo de Captura
- **Retrospectivas de Sprint:** Identificação de problemas de escopo
- **Feedback de Usuários:** Validação de requisitos
- **Análise de Métricas:** Avaliação da eficácia do processo
- **Documentação:** Registro de aprendizados

### 11.2 Aplicação de Melhorias
- **Refinamento de Processos:** Baseado em lições aprendidas
- **Atualização de Templates:** Melhoria de documentação
- **Treinamento:** Capacitação em gestão de escopo
- **Ferramentas:** Adoção de novas tecnologias de apoio

---

## 12. Aprovação e Controle de Versões

**Aprovado por:** Bruno S. Rosa (Maestro)  
**Data de Aprovação:** Dezembro 2024  
**Próxima Revisão:** Janeiro 2025  

**Histórico de Versões:**
- v1.0 (Dez 2024): Versão inicial

**Documentos Relacionados:**
- [[TAP.md]] - Termo de Abertura do Projeto
- [[ERS.md]] - Especificação de Requisitos de Software
- [[PLANO_MESTRE_RECOLOCA_AI.md]] - Visão estratégica
- [[KANBAN_INTERNO_PROJETO.md]] - Backlog e priorização
- [[PCom.md]] - Plano de Gerenciamento das Comunicações
- [[PGR.md]] - Plano de Gerenciamento de Riscos

**Anexos:**
- Matriz de rastreabilidade de requisitos
- Templates de solicitação de mudança
- Checklists de aceitação
- Formulários de validação

--- FIM DO DOCUMENTO PGE.md (v1.0) ---