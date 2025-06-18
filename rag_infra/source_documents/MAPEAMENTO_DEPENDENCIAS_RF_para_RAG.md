---
# RAG Metadata
document_type: "requisitos_dependencias"
project: "Recoloca.AI"
version: "1.1"
last_updated: "2025-06-11"
rag_keywords: ["dependencias", "requisitos funcionais", "mapeamento", "mvp", "priorizacao", "desenvolvimento", "componentes nucleo", "desbloqueio"]
related_documents: [
  "ERS_para_RAG.md",
  "PRIORIZACAO_RICE_RF_para_RAG.md",
  "HLD_para_RAG.md",
  "GUIA_AVANCADO_para_RAG.md"
]
cross_references: [
  "RF-AUTH-001", "RF-AUTH-003", "RF-KAN-001", "RF-CV-003", "RF-IMP-001",
  "componentes de nucleo", "dependencias tecnicas", "fluxo usuario"
]
---

# Mapeamento de Dependências dos Requisitos Funcionais - Recoloca.ai

## Informações do Documento
- **Versão**: 1.1 (Orquestração Inteligente e Specialized Intelligence)
- **Data de Criação**: 06 de junho de 2025
- **Data de Última Atualização**: Junho de 2025
- **Baseado em**: ERS v1.1, GUIA_AVANCADO v1.1, HLD v1.1
- **Criado por**: @AgenteOrquestrador em colaboração com Maestro

## 1. Objetivo e Metodologia

### 1.1. Objetivo
Este documento mapeia as **dependências técnicas e de negócio** entre os requisitos funcionais do ERS para:
- Otimizar a sequência de desenvolvimento do MVP
- Identificar "componentes de núcleo" que desbloqueiam múltiplas funcionalidades
- Preparar a aplicação do framework RICE com contexto de dependências
- Minimizar retrabalho e riscos de desenvolvimento

### 1.2. Critérios Aplicados para Identificação de Dependências

**Critérios Explícitos Utilizados:**

1. **Dependência Técnica Direta (Peso: Alto)**
   - RF-B não pode funcionar sem RF-A estar implementado
   - Exemplo: RF-KAN-001 (criar cartões) depende de RF-AUTH-003 (login)

2. **Dependência de Dados/Estado (Peso: Alto)**
   - RF-B precisa de dados/estado criados por RF-A
   - Exemplo: RF-CV-003 (análise CV vs vaga) depende de RF-IMP-001 (importar vaga)

3. **Dependência de UX/Fluxo (Peso: Médio)**
   - RF-B faz mais sentido na jornada do usuário após RF-A
   - Exemplo: RF-AUTH-006 (onboarding) após RF-AUTH-003 (login)

4. **Dependência de Infraestrutura (Peso: Alto)**
   - RF-B usa componentes/serviços estabelecidos por RF-A
   - Exemplo: Todos os RFs dependem da infraestrutura de autenticação

5. **Valor de Desbloqueio (Peso: Médio-Alto)**
   - RF-A "desbloqueia" múltiplos outros RFs (componente de núcleo)
   - Exemplo: RF-AUTH-001/003 desbloqueia praticamente todos os outros

**Por que estes critérios:**
- Baseados na experiência de desenvolvimento de produtos SaaS
- Alinhados com a metodologia "Desenvolvimento Solo Ágil Aumentado por IA"
- Focados na validação rápida do MVP e "Momento AHA!"

## 2. Mapeamento de Dependências por Categoria

### 2.1. Categoria: Autenticação e Onboarding (AUTH)

**RF-AUTH-001: Cadastro de usuário**
- **Dependências**: Nenhuma (Componente de Núcleo)
- **Desbloqueia**: RF-AUTH-003, RF-AUTH-006, todos os demais RFs
- **Tipo**: Infraestrutura fundamental
- **Prioridade**: CRÍTICA

**RF-AUTH-003: Login de usuário**
- **Dependências**: RF-AUTH-001 (cadastro)
- **Desbloqueia**: Todos os RFs autenticados
- **Tipo**: Infraestrutura fundamental
- **Prioridade**: CRÍTICA

**RF-AUTH-006: Onboarding guiado**
- **Dependências**: RF-AUTH-003 (login)
- **Desbloqueia**: Melhor experiência inicial
- **Tipo**: UX/Fluxo
- **Prioridade**: ALTA

### 2.2. Categoria: Kanban de Vagas (KAN)

**RF-KAN-001: Criar cartão de vaga**
- **Dependências**: RF-AUTH-003 (login)
- **Desbloqueia**: RF-KAN-002, RF-KAN-003, RF-KAN-004, RF-CV-003
- **Tipo**: Componente de Núcleo
- **Prioridade**: CRÍTICA

**RF-KAN-002: Editar cartão de vaga**
- **Dependências**: RF-KAN-001 (criar cartão)
- **Desbloqueia**: Gestão completa de vagas
- **Tipo**: Funcionalidade complementar
- **Prioridade**: ALTA

**RF-KAN-003: Mover cartão entre colunas**
- **Dependências**: RF-KAN-001 (criar cartão)
- **Desbloqueia**: Fluxo visual do Kanban
- **Tipo**: Core da proposta de valor
- **Prioridade**: CRÍTICA

**RF-KAN-004: Excluir cartão de vaga**
- **Dependências**: RF-KAN-001 (criar cartão)
- **Desbloqueia**: Gestão completa
- **Tipo**: Funcionalidade complementar
- **Prioridade**: MÉDIA

### 2.3. Categoria: Importação de Vagas (IMP)

**RF-IMP-001: Importar vaga de URL**
- **Dependências**: RF-AUTH-003 (login)
- **Desbloqueia**: RF-CV-003, automação do processo
- **Tipo**: Diferencial competitivo
- **Prioridade**: ALTA

**RF-IMP-002: Importar vaga manual**
- **Dependências**: RF-AUTH-003 (login)
- **Desbloqueia**: RF-CV-003, entrada alternativa
- **Tipo**: Funcionalidade complementar
- **Prioridade**: MÉDIA

### 2.4. Categoria: Otimização de CV (CV)

**RF-CV-001: Upload de CV (PDF)**
- **Dependências**: RF-AUTH-003 (login)
- **Desbloqueia**: RF-CV-002, RF-CV-003
- **Tipo**: Componente de Núcleo
- **Prioridade**: CRÍTICA

**RF-CV-002: Visualizar CV processado**
- **Dependências**: RF-CV-001 (upload)
- **Desbloqueia**: Transparência do processo
- **Tipo**: UX/Confiança
- **Prioridade**: ALTA

**RF-CV-003: Análise CV vs Vaga com IA**
- **Dependências**: RF-CV-001 (upload), RF-KAN-001 ou RF-IMP-001 (ter vaga)
- **Desbloqueia**: "Momento AHA!" principal
- **Tipo**: Core da proposta de valor
- **Prioridade**: CRÍTICA

**RF-CV-004: Sugestões de melhoria**
- **Dependências**: RF-CV-003 (análise)
- **Desbloqueia**: Valor agregado da IA
- **Tipo**: Diferencial competitivo
- **Prioridade**: ALTA

**RF-CV-005: Gerar versão otimizada**
- **Dependências**: RF-CV-003 (análise), RF-CV-004 (sugestões)
- **Desbloqueia**: Entrega tangível
- **Tipo**: Resultado final
- **Prioridade**: CRÍTICA

### 2.5. Categoria: AI Coach (COACH)

**RF-COACH-001: Chat com AI Coach**
- **Dependências**: RF-AUTH-003 (login)
- **Desbloqueia**: Suporte personalizado
- **Tipo**: Diferencial competitivo
- **Prioridade**: MÉDIA

**RF-COACH-002: Sugestões contextuais**
- **Dependências**: RF-COACH-001, dados do usuário
- **Desbloqueia**: IA proativa
- **Tipo**: Valor agregado
- **Prioridade**: BAIXA

## 3. Análise de Componentes de Núcleo

### 3.1. Identificação dos Componentes de Núcleo

**Critérios para Componente de Núcleo:**
- Desbloqueia 3+ outros requisitos funcionais
- Crítico para o "Momento AHA!" do produto
- Infraestrutura fundamental para múltiplas funcionalidades

**Componentes Identificados:**

1. **RF-AUTH-001 + RF-AUTH-003** (Autenticação)
   - Desbloqueia: TODOS os demais RFs
   - Impacto: Infraestrutura fundamental
   - Prioridade: CRÍTICA

2. **RF-KAN-001** (Criar cartão de vaga)
   - Desbloqueia: RF-KAN-002, RF-KAN-003, RF-KAN-004, RF-CV-003
   - Impacto: Base do Kanban
   - Prioridade: CRÍTICA

3. **RF-CV-001** (Upload de CV)
   - Desbloqueia: RF-CV-002, RF-CV-003, RF-CV-004, RF-CV-005
   - Impacto: Base da otimização de CV
   - Prioridade: CRÍTICA

4. **RF-CV-003** (Análise CV vs Vaga)
   - Desbloqueia: RF-CV-004, RF-CV-005
   - Impacto: "Momento AHA!" principal
   - Prioridade: CRÍTICA

### 3.2. Sequência de Desenvolvimento Recomendada

**Fase 1: Infraestrutura (Semanas 1-2)**
1. RF-AUTH-001 (Cadastro)
2. RF-AUTH-003 (Login)
3. RF-AUTH-006 (Onboarding básico)

**Fase 2: Núcleo do Kanban (Semanas 3-4)**
4. RF-KAN-001 (Criar cartão)
5. RF-KAN-003 (Mover cartão)
6. RF-KAN-002 (Editar cartão)

**Fase 3: Núcleo da IA (Semanas 5-7)**
7. RF-CV-001 (Upload CV)
8. RF-CV-003 (Análise IA) - **"Momento AHA!"**
9. RF-CV-002 (Visualizar processado)

**Fase 4: Valor Agregado (Semanas 8-10)**
10. RF-CV-004 (Sugestões)
11. RF-CV-005 (Gerar otimizado)
12. RF-IMP-001 (Importar URL)

**Fase 5: Complementares (Pós-MVP)**
13. RF-IMP-002 (Importar manual)
14. RF-KAN-004 (Excluir cartão)
15. RF-COACH-001 (AI Coach)
16. RF-COACH-002 (Sugestões contextuais)

## 4. Matriz de Dependências

### 4.1. Matriz Visual de Dependências

```
RF-AUTH-001 → RF-AUTH-003 → [Todos os demais]
                ↓
            RF-AUTH-006
                ↓
            RF-KAN-001 → RF-KAN-002
                ↓         RF-KAN-003
                ↓         RF-KAN-004
                ↓
            RF-CV-001 → RF-CV-002
                ↓
            RF-CV-003 ← RF-IMP-001
                ↓         RF-IMP-002
            RF-CV-004
                ↓
            RF-CV-005

            RF-COACH-001 → RF-COACH-002
```

### 4.2. Análise de Riscos de Dependência

**Riscos Identificados:**

1. **Gargalo de Autenticação**
   - Risco: Atraso em AUTH bloqueia todo o desenvolvimento
   - Mitigação: Priorizar AUTH-001 e AUTH-003 no início

2. **Complexidade da IA**
   - Risco: RF-CV-003 pode ser mais complexo que estimado
   - Mitigação: Protótipo rápido, fallback para análise simples

3. **Dependência Externa (Importação)**
   - Risco: Sites podem mudar estrutura, quebrar RF-IMP-001
   - Mitigação: Implementar RF-IMP-002 como backup

## 5. Métricas de Validação

### 5.1. KPIs de Dependências

**Métricas de Desbloqueio:**
- % de RFs desbloqueados por componente de núcleo
- Tempo médio entre implementação de dependência e dependente
- Taxa de retrabalho por dependência mal mapeada

**Métricas de Sequenciamento:**
- Aderência ao cronograma de dependências
- Tempo de ciclo por fase de desenvolvimento
- Eficiência de desenvolvimento (features/semana)

### 5.2. Critérios de Sucesso

**Sucesso do Mapeamento:**
- Zero bloqueios não previstos durante desenvolvimento
- Implementação do "Momento AHA!" até Semana 7
- 90% dos RFs críticos funcionando até Semana 10

## 6. Próximos Passos

### 6.1. Ações Imediatas
1. Validar mapeamento com equipe técnica
2. Aplicar framework RICE usando este contexto
3. Criar backlog priorizado baseado nas dependências
4. Definir critérios de "Definition of Done" para cada RF

### 6.2. Evolução Contínua
- Revisar dependências a cada sprint
- Atualizar mapeamento conforme descobertas técnicas
- Monitorar métricas de desbloqueio
- Ajustar sequenciamento baseado em feedback

## 7. Referências e Documentos Relacionados

### 7.1. Documentos Base
- **ERS_para_RAG.md**: Especificação completa dos requisitos funcionais
- **PRIORIZACAO_RICE_RF_para_RAG.md**: Aplicação do framework RICE
- **HLD_para_RAG.md**: Arquitetura de alto nível
- **GUIA_AVANCADO_para_RAG.md**: Metodologia de desenvolvimento

### 7.2. Documentos Relacionados
- **CAMINHO_CRITICO_MVP_para_RAG.md**: Cronograma detalhado
- **KANBAN_ESTRATEGICO_FASES_para_RAG.md**: Gestão de fases
- **MAESTRO_TASKS_para_RAG.md**: Tarefas específicas do Maestro

---

**Documento**: MAPEAMENTO_DEPENDENCIAS_RF_para_RAG.md (v1.1)
**Otimizado para**: Sistema RAG - Consulta de dependências e sequenciamento
**Palavras-chave RAG**: dependencias, requisitos funcionais, mapeamento, mvp, priorizacao, desenvolvimento, componentes nucleo, desbloqueio, sequenciamento, riscos

--- FIM DO DOCUMENTO MAPEAMENTO_DEPENDENCIAS_RF_para_RAG.md (v1.1) ---