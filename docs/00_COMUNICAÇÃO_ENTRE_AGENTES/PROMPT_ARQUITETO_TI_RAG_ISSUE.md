# PROMPT PARA @AgenteM_ArquitetoTI - CORREÇÃO CRÍTICA RAG

**Data:** 20 de Junho de 2025  
**Prioridade:** CRÍTICA - AÇÃO IMEDIATA  
**Prazo:** 24-48 horas  
**Contexto:** Falha recorrente na inicialização do RAGRetriever

---

## 🚨 PROBLEMA CRÍTICO IDENTIFICADO

**Erro Recorrente:** `'NoneType' object has no attribute 'search'`  
**Status RAG:** `"initialized": false`  
**Mensagem:** "Falha na inicialização do retriever"

### 📋 Contexto Técnico Atual

**Situação Identificada:**
- ✅ **MCP Server:** Funcional e operacional
- ❌ **RAGRetriever Local:** Falha consistente (retorna 0 resultados)
- ⚠️ **Inconsistência:** Duas implementações divergentes para o mesmo sistema
- 🔍 **Impacto:** Agentes não conseguem consultar a "Documentação Viva"

**Evidências Documentadas:**
- `[[docs/00_COMUNICAÇÃO_ENTRE_AGENTES/RELATORIO_AUDITORIA_RAG_MCP_TECNICA.md]]`
- `[[rag_infra/docs/CORREÇÃO_MCP_CONNECTION_ERROR.md]]`
- Status atual via `rag_get_status`: inicialização falhando

---

## 🎯 SOLICITAÇÃO ESPECÍFICA

### **Análise Arquitetural Urgente:**

1. **Investigar Método `search()` na Classe `RAGRetriever`**
   - Localizar: `rag_infra/src/core/core_logic/rag_retriever.py`
   - Analisar: Por que retorna `NoneType` em vez de objeto inicializado
   - Verificar: Compatibilidade com backend PyTorch

2. **Alinhar Implementações Divergentes**
   - **MCP Server:** Funcional (usar como referência)
   - **Implementação Local:** Corrigir para espelhar funcionalidade MCP
   - **Objetivo:** Unificar comportamento entre interfaces

3. **Validar Arquitetura de Inicialização**
   - Verificar sequência de inicialização do retriever
   - Analisar dependências (FAISS, embeddings, metadados)
   - Identificar ponto de falha na cadeia de inicialização

### **Entregáveis Esperados:**

1. **Diagnóstico Técnico Detalhado**
   - Causa raiz da falha de inicialização
   - Análise comparativa MCP vs. Local
   - Identificação de inconsistências arquiteturais

2. **Plano de Correção Estruturado**
   - Passos específicos para correção
   - Modificações necessárias no código
   - Estratégia de validação pós-correção

3. **Arquitetura Unificada**
   - Design para interface única de acesso RAG
   - Padrão arquitetural para evitar divergências futuras
   - Documentação de decisões (ADR se necessário)

---

## 📚 BASE DE CONHECIMENTO OBRIGATÓRIA

**Consulte Prioritariamente:**
- `[[docs/00_Gerenciamento_Projeto/KANBAN/]]` - Contexto da fase atual
- `[[docs/03_Arquitetura_e_Design/01_HLD.md]]` - Arquitetura atual
- `[[rag_infra/docs/README_RAG_OPERACIONAL.md]]` - Especificações operacionais
- `[[rag_infra/docs/CORREÇÃO_MCP_CONNECTION_ERROR.md]]` - Correções anteriores

**Documentação Técnica:**
- `[[rag_infra/source_documents/04_Tech_Stack/]]` - Stack tecnológico
- `[[docs/03_Arquitetura_e_Design/02_ADRs/]]` - Decisões arquiteturais

---

## 🔧 FERRAMENTAS DISPONÍVEIS

- **RAG MCP:** Para consulta da documentação técnica
- **Filesystem MCP:** Análise de código e estrutura
- **Context7 MCP:** Documentação oficial de bibliotecas
- **Deepview MCP:** Análise semântica do codebase
- **Web Search:** Melhores práticas e soluções técnicas

---

## ⚡ SOLUÇÃO TEMPORÁRIA RECOMENDADA

**Enquanto a correção não é implementada:**
- Orientar todos os agentes a usar **exclusivamente MCP Server** para consultas RAG
- Deprecar temporariamente implementação local problemática
- Documentar mudança de arquitetura temporária

---

## 🎯 CRITÉRIOS DE SUCESSO

1. **RAGRetriever Local:** Inicialização bem-sucedida
2. **Consultas RAG:** Retorno consistente de resultados relevantes
3. **Unificação:** Comportamento idêntico entre MCP e implementação local
4. **Validação:** Testes automatizados confirmando funcionalidade
5. **Documentação:** ADR ou documentação técnica atualizada

---

## 📞 COMUNICAÇÃO

**Reporte Progresso Para:**
- Maestro (Bruno S. Rosa)
- `@AgenteM_Orquestrador` (para coordenação estratégica)

**Escalação Se Necessário:**
- `@AgenteM_DevFastAPI` (para implementação específica)
- `@AgenteM_DevOps` (se houver questões de infraestrutura)

---

**Maestro, este prompt estruturado fornece ao @AgenteM_ArquitetoTI todo o contexto necessário para diagnosticar e corrigir o problema de inicialização do RAG de forma eficiente e alinhada com suas responsabilidades arquiteturais.**

--- FIM DO DOCUMENTO PROMPT_ARQUITETO_TI_RAG_ISSUE.md (v1.0) ---