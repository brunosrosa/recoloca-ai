# 🏗️ Arquitetura e Design

## 🎯 Propósito

Esta pasta contém toda a **documentação técnica de arquitetura, design e padrões** do projeto Recoloca.ai, essencial para decisões de desenvolvimento e implementação.

## 📋 Tipos de Documentos

### ✅ Incluir Aqui:
- **HLD (High Level Design)** - Arquitetura geral do sistema
- **LLD (Low Level Design)** - Especificações técnicas detalhadas
- **ADRs (Architecture Decision Records)** - Decisões arquiteturais
- **Style Guides** - Padrões de código e design
- **Diagramas de Arquitetura** - Representações visuais do sistema
- **Padrões de Design** - Patterns e convenções
- **Especificações de API** - Contratos e interfaces
- **Modelos de Dados** - Estruturas e relacionamentos

### ❌ Não Incluir:
- Requisitos funcionais (usar 02_Requisitos_e_Especificacoes)
- Processos de gestão (usar 01_Gestao_e_Processos)
- Documentação de usuário (usar 00_Documentacao_Central)

## 🔍 Prioridade RAG

**Alta Prioridade** - Estes documentos são fundamentais para:
- @AgenteM_ArquitetoTI - Decisões arquiteturais
- @AgenteM_DevFastAPI - Implementação backend
- @AgenteM_DevOps - Deploy e infraestrutura
- Todos os agentes técnicos para manter consistência

## 📝 Convenções de Nomenclatura

```
[TIPO]_[COMPONENTE]_para_RAG.md

Exemplos:
- HLD_SISTEMA_GERAL_para_RAG.md
- LLD_API_BACKEND_para_RAG.md
- ADR_001_ESCOLHA_FRAMEWORK_para_RAG.md
- STYLE_GUIDE_PYTHON_para_RAG.md
- API_SPEC_AUTENTICACAO_para_RAG.md
```

## 🏷️ Categorias

### 🎨 Design System
- Style guides
- Padrões visuais
- Componentes reutilizáveis

### 🏛️ Arquitetura
- HLD e LLD
- Diagramas de sistema
- Padrões arquiteturais

### 📡 APIs e Interfaces
- Especificações OpenAPI
- Contratos de interface
- Documentação de endpoints

### 🗄️ Dados
- Modelos de dados
- Esquemas de banco
- Fluxos de informação

## 🔄 Manutenção

- **Frequência de Atualização**: A cada sprint ou mudança arquitetural
- **Responsável**: @AgenteM_ArquitetoTI
- **Revisão**: Semanal com equipe técnica
- **Versionamento**: Manter histórico de decisões

## 🔗 Integração

Esses documentos devem estar sincronizados com:
- Código fonte no repositório
- Documentação de deploy
- Especificações de requisitos
- Testes de arquitetura

---

*Última atualização: $(date +"%Y-%m-%d")*