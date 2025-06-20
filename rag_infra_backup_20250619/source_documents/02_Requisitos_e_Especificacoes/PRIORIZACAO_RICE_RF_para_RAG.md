---
# RAG Metadata
document_type: "requisitos_priorizacao"
project: "Recoloca.AI"
version: "1.1"
last_updated: "2025-06-11"
rag_keywords: ["RICE", "priorizacao", "requisitos funcionais", "reach", "impact", "confidence", "effort", "mvp", "momento aha", "score"]
related_documents: [
  "ERS_para_RAG.md",
  "MAPEAMENTO_DEPENDENCIAS_RF_para_RAG.md",
  "HLD_para_RAG.md",
  "GUIA_AVANCADO_para_RAG.md"
]
cross_references: [
  "framework RICE", "reach impact confidence effort", "priorizacao mvp",
  "momento aha", "componentes nucleo", "score rice", "validacao rapida"
]
---

# Priorização RICE dos Requisitos Funcionais - Recoloca.ai

## Informações do Documento
- **Versão**: 1.1 (Orquestração Inteligente e Specialized Intelligence)
- **Data de Criação**: 11 de junho de 2025
- **Data de Última Atualização**: Junho de 2025
- **Baseado em**: MAPEAMENTO_DEPENDENCIAS_RF v1.1, ERS v1.1, GUIA_AVANCADO v1.1
- **Criado por**: @AgenteOrquestrador + Maestro
- **Status**: Validado e Alinhado

## 1. Objetivo e Metodologia

### 1.1 Propósito
Este documento aplica o **framework RICE (Reach, Impact, Confidence, Effort)** aos requisitos funcionais do Recoloca.ai, utilizando o contexto das dependências mapeadas para otimizar a sequência de desenvolvimento do MVP.

### 1.2 Metodologia RICE Adaptada

**Fórmula Base:** `RICE Score = (Reach × Impact × Confidence) / Effort`

**Adaptações para o Projeto:**
- **Bônus de Desbloqueio:** +20% no score para features que desbloqueiam outras
- **Ajuste de Probabilidade:** Confidence baseado em dependências mapeadas
- **Contexto MVP:** Foco em validação rápida e "Momento AHA!"

### 1.3 Critérios de Avaliação

#### Reach (Alcance) - Escala 1-10
- **10:** Todos os usuários do MVP (100%)
- **8:** Maioria dos usuários (70-90%)
- **6:** Metade dos usuários (40-70%)
- **4:** Minoria significativa (20-40%)
- **2:** Nicho específico (5-20%)
- **1:** Casos extremos (<5%)

#### Impact (Impacto) - Escala 1-10
- **10:** Crítico para o "Momento AHA!" - sem isso, produto não funciona
- **8:** Alto impacto na proposta de valor principal
- **6:** Melhora significativa na experiência
- **4:** Melhoria moderada, mas perceptível
- **2:** Pequena melhoria
- **1:** Impacto mínimo

#### Confidence (Probabilidade) - Escala 0-100%
Baseado nos critérios detalhados do mapeamento de dependências:

- **Complexidade Técnica (40%):**
  - 90-100%: Implementação simples, tecnologias conhecidas
  - 70-89%: Complexidade moderada, algumas incertezas
  - 50-69%: Complexidade alta, muitas incertezas
  - 30-49%: Muito complexo, alto risco técnico
  - 10-29%: Extremamente complexo, risco muito alto

- **Dependências Mapeadas (30%):**
  - 90-100%: Sem dependências ou dependências já implementadas
  - 70-89%: Dependências claras e simples
  - 50-69%: Dependências moderadas
  - 30-49%: Dependências complexas
  - 10-29%: Dependências críticas não resolvidas

- **Conhecimento da Equipe (20%):**
  - 90-100%: Domínio completo da tecnologia/domínio
  - 70-89%: Bom conhecimento, pequena curva de aprendizado
  - 50-69%: Conhecimento moderado
  - 30-49%: Conhecimento limitado
  - 10-29%: Tecnologia/domínio novo

- **Riscos Externos (10%):**
  - 90-100%: Sem riscos externos
  - 70-89%: Riscos mínimos e controláveis
  - 50-69%: Alguns riscos externos
  - 30-49%: Riscos significativos
  - 10-29%: Altos riscos externos

#### Effort (Esforço) - Escala 1-10
- **1:** 1-2 dias de desenvolvimento
- **2:** 3-5 dias de desenvolvimento
- **3:** 1 semana de desenvolvimento
- **4:** 1.5 semanas de desenvolvimento
- **5:** 2 semanas de desenvolvimento
- **6:** 3 semanas de desenvolvimento
- **7:** 4 semanas de desenvolvimento
- **8:** 5-6 semanas de desenvolvimento
- **9:** 7-8 semanas de desenvolvimento
- **10:** 9+ semanas de desenvolvimento

## 2. Avaliação RICE por Categoria

### 2.1. Categoria: Autenticação e Onboarding (AUTH)

#### RF-AUTH-001: Cadastro de usuário
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - sem isso não há produto)
- **Confidence:** 95% (Tecnologia conhecida, sem dependências)
- **Effort:** 3 (1 semana)
- **Bônus Desbloqueio:** +20% (desbloqueia todos os RFs)
- **RICE Score:** (10 × 10 × 0.95) / 3 × 1.2 = **38.0**
- **Prioridade:** CRÍTICA

#### RF-AUTH-003: Login de usuário
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - acesso ao sistema)
- **Confidence:** 95% (Tecnologia conhecida, depende de AUTH-001)
- **Effort:** 2 (3-5 dias)
- **Bônus Desbloqueio:** +20% (desbloqueia funcionalidades autenticadas)
- **RICE Score:** (10 × 10 × 0.95) / 2 × 1.2 = **57.0**
- **Prioridade:** CRÍTICA

#### RF-AUTH-006: Onboarding guiado
- **Reach:** 10 (100% dos novos usuários)
- **Impact:** 6 (Melhora significativa na experiência)
- **Confidence:** 85% (UX design, depende de AUTH-003)
- **Effort:** 4 (1.5 semanas)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (10 × 6 × 0.85) / 4 = **12.8**
- **Prioridade:** ALTA

### 2.2. Categoria: Kanban de Vagas (KAN)

#### RF-KAN-001: Criar cartão de vaga
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - base do Kanban)
- **Confidence:** 90% (CRUD simples, depende de AUTH-003)
- **Effort:** 3 (1 semana)
- **Bônus Desbloqueio:** +20% (desbloqueia outros KAN e CV-003)
- **RICE Score:** (10 × 10 × 0.90) / 3 × 1.2 = **36.0**
- **Prioridade:** CRÍTICA

#### RF-KAN-003: Mover cartão entre colunas
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - essência do Kanban)
- **Confidence:** 85% (Drag & drop, depende de KAN-001)
- **Effort:** 4 (1.5 semanas)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (10 × 10 × 0.85) / 4 = **21.3**
- **Prioridade:** CRÍTICA

#### RF-KAN-002: Editar cartão de vaga
- **Reach:** 8 (70-90% dos usuários)
- **Impact:** 6 (Melhora significativa na experiência)
- **Confidence:** 90% (CRUD simples, depende de KAN-001)
- **Effort:** 2 (3-5 dias)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (8 × 6 × 0.90) / 2 = **21.6**
- **Prioridade:** ALTA

#### RF-KAN-004: Excluir cartão de vaga
- **Reach:** 6 (40-70% dos usuários)
- **Impact:** 4 (Melhoria moderada)
- **Confidence:** 95% (CRUD simples, depende de KAN-001)
- **Effort:** 1 (1-2 dias)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (6 × 4 × 0.95) / 1 = **22.8**
- **Prioridade:** MÉDIA

### 2.3. Categoria: Otimização de CV (CV)

#### RF-CV-001: Upload de CV (PDF)
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - base da otimização)
- **Confidence:** 80% (Parsing PDF, OCR, depende de AUTH-003)
- **Effort:** 5 (2 semanas)
- **Bônus Desbloqueio:** +20% (desbloqueia toda categoria CV)
- **RICE Score:** (10 × 10 × 0.80) / 5 × 1.2 = **19.2**
- **Prioridade:** CRÍTICA

#### RF-CV-003: Análise CV vs Vaga com IA
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - "Momento AHA!" principal)
- **Confidence:** 70% (Integração LLM, depende de CV-001 e KAN-001)
- **Effort:** 6 (3 semanas)
- **Bônus Desbloqueio:** +20% (desbloqueia CV-004 e CV-005)
- **RICE Score:** (10 × 10 × 0.70) / 6 × 1.2 = **14.0**
- **Prioridade:** CRÍTICA

#### RF-CV-002: Visualizar CV processado
- **Reach:** 8 (70-90% dos usuários)
- **Impact:** 6 (Melhora confiança no processo)
- **Confidence:** 85% (Visualização simples, depende de CV-001)
- **Effort:** 3 (1 semana)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (8 × 6 × 0.85) / 3 = **13.6**
- **Prioridade:** ALTA

#### RF-CV-004: Sugestões de melhoria
- **Reach:** 10 (100% dos usuários)
- **Impact:** 8 (Alto impacto na proposta de valor)
- **Confidence:** 75% (Lógica de IA, depende de CV-003)
- **Effort:** 4 (1.5 semanas)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (10 × 8 × 0.75) / 4 = **15.0**
- **Prioridade:** ALTA

#### RF-CV-005: Gerar versão otimizada
- **Reach:** 10 (100% dos usuários)
- **Impact:** 10 (Crítico - entrega tangível)
- **Confidence:** 65% (Geração de PDF, depende de CV-003 e CV-004)
- **Effort:** 5 (2 semanas)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (10 × 10 × 0.65) / 5 = **13.0**
- **Prioridade:** CRÍTICA

### 2.4. Categoria: Importação de Vagas (IMP)

#### RF-IMP-001: Importar vaga de URL
- **Reach:** 8 (70-90% dos usuários)
- **Impact:** 8 (Alto impacto - automação)
- **Confidence:** 60% (Web scraping, riscos externos)
- **Effort:** 6 (3 semanas)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (8 × 8 × 0.60) / 6 = **6.4**
- **Prioridade:** ALTA

#### RF-IMP-002: Importar vaga manual
- **Reach:** 6 (40-70% dos usuários)
- **Impact:** 4 (Melhoria moderada - backup)
- **Confidence:** 90% (Formulário simples)
- **Effort:** 2 (3-5 dias)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (6 × 4 × 0.90) / 2 = **10.8**
- **Prioridade:** MÉDIA

### 2.5. Categoria: AI Coach (COACH)

#### RF-COACH-001: Chat com AI Coach
- **Reach:** 6 (40-70% dos usuários)
- **Impact:** 6 (Melhora significativa na experiência)
- **Confidence:** 70% (Integração LLM, contexto do usuário)
- **Effort:** 7 (4 semanas)
- **Bônus Desbloqueio:** +20% (desbloqueia COACH-002)
- **RICE Score:** (6 × 6 × 0.70) / 7 × 1.2 = **3.6**
- **Prioridade:** MÉDIA

#### RF-COACH-002: Sugestões contextuais
- **Reach:** 4 (20-40% dos usuários)
- **Impact:** 4 (Melhoria moderada)
- **Confidence:** 60% (IA proativa, depende de COACH-001)
- **Effort:** 5 (2 semanas)
- **Bônus Desbloqueio:** 0% (não desbloqueia outros RFs)
- **RICE Score:** (4 × 4 × 0.60) / 5 = **1.9**
- **Prioridade:** BAIXA

## 3. Ranking Final RICE

### 3.1. Ranking por Score RICE

| Posição | RF | Descrição | Score RICE | Prioridade |
|---------|----|-----------|-----------|-----------|
| 1 | RF-AUTH-003 | Login de usuário | 57.0 | CRÍTICA |
| 2 | RF-AUTH-001 | Cadastro de usuário | 38.0 | CRÍTICA |
| 3 | RF-KAN-001 | Criar cartão de vaga | 36.0 | CRÍTICA |
| 4 | RF-KAN-004 | Excluir cartão de vaga | 22.8 | MÉDIA |
| 5 | RF-KAN-002 | Editar cartão de vaga | 21.6 | ALTA |
| 6 | RF-KAN-003 | Mover cartão entre colunas | 21.3 | CRÍTICA |
| 7 | RF-CV-001 | Upload de CV (PDF) | 19.2 | CRÍTICA |
| 8 | RF-CV-004 | Sugestões de melhoria | 15.0 | ALTA |
| 9 | RF-CV-003 | Análise CV vs Vaga com IA | 14.0 | CRÍTICA |
| 10 | RF-CV-002 | Visualizar CV processado | 13.6 | ALTA |
| 11 | RF-CV-005 | Gerar versão otimizada | 13.0 | CRÍTICA |
| 12 | RF-AUTH-006 | Onboarding guiado | 12.8 | ALTA |
| 13 | RF-IMP-002 | Importar vaga manual | 10.8 | MÉDIA |
| 14 | RF-IMP-001 | Importar vaga de URL | 6.4 | ALTA |
| 15 | RF-COACH-001 | Chat com AI Coach | 3.6 | MÉDIA |
| 16 | RF-COACH-002 | Sugestões contextuais | 1.9 | BAIXA |

### 3.2. Agrupamento por Prioridade

**CRÍTICAS (Score > 13.0):**
- RF-AUTH-003: Login de usuário (57.0)
- RF-AUTH-001: Cadastro de usuário (38.0)
- RF-KAN-001: Criar cartão de vaga (36.0)
- RF-KAN-003: Mover cartão entre colunas (21.3)
- RF-CV-001: Upload de CV (PDF) (19.2)
- RF-CV-003: Análise CV vs Vaga com IA (14.0)
- RF-CV-005: Gerar versão otimizada (13.0)

**ALTAS (Score 10.0-13.0):**
- RF-KAN-002: Editar cartão de vaga (21.6)
- RF-CV-004: Sugestões de melhoria (15.0)
- RF-CV-002: Visualizar CV processado (13.6)
- RF-AUTH-006: Onboarding guiado (12.8)

**MÉDIAS (Score 5.0-10.0):**
- RF-KAN-004: Excluir cartão de vaga (22.8)
- RF-IMP-002: Importar vaga manual (10.8)
- RF-IMP-001: Importar vaga de URL (6.4)
- RF-COACH-001: Chat com AI Coach (3.6)

**BAIXAS (Score < 5.0):**
- RF-COACH-002: Sugestões contextuais (1.9)

## 4. Sequência de Desenvolvimento Otimizada

### 4.1. Sequência Baseada em RICE + Dependências

**Sprint 1 (Semanas 1-2): Infraestrutura**
1. RF-AUTH-001: Cadastro de usuário (Score: 38.0)
2. RF-AUTH-003: Login de usuário (Score: 57.0)
3. RF-AUTH-006: Onboarding guiado (Score: 12.8)

**Sprint 2 (Semanas 3-4): Núcleo Kanban**
4. RF-KAN-001: Criar cartão de vaga (Score: 36.0)
5. RF-KAN-003: Mover cartão entre colunas (Score: 21.3)
6. RF-KAN-002: Editar cartão de vaga (Score: 21.6)

**Sprint 3 (Semanas 5-7): Núcleo IA - "Momento AHA!"**
7. RF-CV-001: Upload de CV (PDF) (Score: 19.2)
8. RF-CV-003: Análise CV vs Vaga com IA (Score: 14.0)
9. RF-CV-002: Visualizar CV processado (Score: 13.6)

**Sprint 4 (Semanas 8-10): Valor Agregado**
10. RF-CV-004: Sugestões de melhoria (Score: 15.0)
11. RF-CV-005: Gerar versão otimizada (Score: 13.0)
12. RF-IMP-001: Importar vaga de URL (Score: 6.4)

**Pós-MVP: Complementares**
13. RF-KAN-004: Excluir cartão de vaga (Score: 22.8)
14. RF-IMP-002: Importar vaga manual (Score: 10.8)
15. RF-COACH-001: Chat com AI Coach (Score: 3.6)
16. RF-COACH-002: Sugestões contextuais (Score: 1.9)

### 4.2. Marcos de Validação

**Marco 1 (Fim Sprint 1): Usuário Autenticado**
- Usuário pode se cadastrar e fazer login
- Onboarding básico funcional
- Validação: Taxa de conversão cadastro → login

**Marco 2 (Fim Sprint 2): Kanban Funcional**
- Usuário pode criar e gerenciar vagas no Kanban
- Fluxo visual básico funcionando
- Validação: Engajamento com o Kanban

**Marco 3 (Fim Sprint 3): "Momento AHA!"**
- Usuário pode fazer upload de CV e receber análise IA
- Proposta de valor principal demonstrada
- Validação: Taxa de "AHA!" (usuários que completam análise)

**Marco 4 (Fim Sprint 4): MVP Completo**
- Usuário pode gerar CV otimizado
- Fluxo completo end-to-end funcionando
- Validação: Taxa de conversão para CV otimizado

## 5. Análise de Sensibilidade

### 5.1. Cenários de Ajuste

**Cenário 1: Redução de Escopo (MVP Mínimo)**
Se precisar reduzir escopo, remover nesta ordem:
1. RF-COACH-002 (Score: 1.9)
2. RF-COACH-001 (Score: 3.6)
3. RF-IMP-001 (Score: 6.4)
4. RF-IMP-002 (Score: 10.8)

**Cenário 2: Aceleração (Recursos Extras)**
Se tiver recursos extras, paralelizar:
1. RF-CV-002 com RF-CV-003 (dependência fraca)
2. RF-IMP-001 com RF-CV-004 (independentes)
3. RF-KAN-004 antecipado (score alto, esforço baixo)

**Cenário 3: Risco Técnico Alto**
Se RF-CV-003 for muito complexo:
1. Implementar versão simplificada primeiro
2. Antecipar RF-CV-002 para ganhar confiança
3. Considerar RF-IMP-002 como alternativa rápida

### 5.2. Fatores de Ajuste

**Fatores que podem alterar scores:**
- Feedback de usuários beta
- Descobertas técnicas durante desenvolvimento
- Mudanças no mercado/competição
- Limitações de recursos ou tempo

## 6. Métricas de Acompanhamento

### 6.1. KPIs por RF

**Autenticação:**
- Taxa de conversão cadastro → login
- Tempo médio de onboarding
- Taxa de abandono no cadastro

**Kanban:**
- Número médio de vagas por usuário
- Frequência de uso do Kanban
- Taxa de movimentação entre colunas

**Otimização CV:**
- Taxa de upload de CV
- Taxa de conclusão da análise IA
- Taxa de geração de CV otimizado
- NPS da funcionalidade de IA

**Importação:**
- Taxa de sucesso da importação por URL
- Tempo médio de importação
- Taxa de uso vs criação manual

### 6.2. Métricas de Validação do RICE

**Validação de Reach:**
- % real de usuários que usam cada feature
- Comparação com estimativas iniciais

**Validação de Impact:**
- Correlação entre uso da feature e retenção
- NPS por feature
- Tempo até "Momento AHA!"

**Validação de Confidence:**
- Aderência aos prazos estimados
- Número de bugs/retrabalho por feature
- Taxa de sucesso técnico

**Validação de Effort:**
- Tempo real vs estimado por feature
- Complexidade real vs estimada
- Recursos consumidos vs planejados

## 7. Próximos Passos

### 7.1. Ações Imediatas
1. Validar scores RICE com stakeholders
2. Criar backlog detalhado baseado na sequência
3. Definir critérios de aceitação para cada RF
4. Estabelecer métricas de acompanhamento

### 7.2. Evolução Contínua
- Revisar scores RICE a cada sprint
- Ajustar sequência baseada em aprendizados
- Monitorar métricas de validação
- Atualizar estimativas de esforço

## 8. Referências e Documentos Relacionados

### 8.1. Documentos Base
- **ERS_para_RAG.md**: Especificação completa dos requisitos funcionais
- **MAPEAMENTO_DEPENDENCIAS_RF_para_RAG.md**: Análise detalhada de dependências
- **HLD_para_RAG.md**: Arquitetura de alto nível
- **GUIA_AVANCADO_para_RAG.md**: Metodologia de desenvolvimento

### 8.2. Documentos Relacionados
- **CAMINHO_CRITICO_MVP_para_RAG.md**: Cronograma detalhado
- **KANBAN_ESTRATEGICO_FASES_para_RAG.md**: Gestão de fases
- **MAESTRO_TASKS_para_RAG.md**: Tarefas específicas do Maestro

---

**Documento**: PRIORIZACAO_RICE_RF_para_RAG.md (v1.1)
**Otimizado para**: Sistema RAG - Consulta de priorização e scores RICE
**Palavras-chave RAG**: RICE, priorizacao, requisitos funcionais, reach, impact, confidence, effort, mvp, momento aha, score, ranking, sequencia desenvolvimento

--- FIM DO DOCUMENTO PRIORIZACAO_RICE_RF_para_RAG.md (v1.1) ---