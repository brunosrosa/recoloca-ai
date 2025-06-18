# 📚 RAG Source Documents - Recoloca.ai

## 🎯 Visão Geral

Esta pasta contém toda a **documentação organizada para o sistema RAG** (Retrieval Augmented Generation) do projeto Recoloca.ai. A estrutura foi otimizada para maximizar a eficiência das consultas dos agentes de IA e garantir acesso rápido ao conhecimento relevante.

## 🗂️ Estrutura Organizacional

### 📋 Categorias Principais

```
source_documents/
├── 01_Documentacao_Central/     # 📚 Guias mestres e documentação fundamental
├── 02_Arquitetura_e_Design/     # 🏗️ Especificações técnicas e padrões
├── 03_Requisitos_e_Especificacoes/ # 📋 ERS, APIs e critérios de aceitação
├── 04_Gestao_e_Processos/       # 📊 KANBAN, metodologias e workflows
├── 05_Agentes_e_IA/             # 🤖 Configurações e prompts dos agentes
├── 06_Tech_Stack/               # 💻 Documentação de tecnologias utilizadas
├── 07_UX_e_Design/              # 🎨 Design system e pesquisa de usuário
└── 08_Conhecimento_Especializado/ # 🧠 Expertise de domínio e mercado
```

### 🎯 Prioridades RAG

**🔴 Crítica (Consulta Frequente)**
- `01_Documentacao_Central` - Visão estratégica e metodologias
- `05_Agentes_e_IA` - Auto-referência e coordenação
- `08_Conhecimento_Especializado` - Expertise de domínio

**🟡 Alta (Desenvolvimento Ativo)**
- `02_Arquitetura_e_Design` - Decisões técnicas
- `03_Requisitos_e_Especificacoes` - Implementação de features
- `06_Tech_Stack` - Referência técnica

**🟢 Média-Alta (Gestão e UX)**
- `04_Gestao_e_Processos` - Coordenação de projeto
- `07_UX_e_Design` - Interface e experiência

## 📝 Convenções de Nomenclatura

### 🏷️ Padrão Geral
```
[TIPO]_[COMPONENTE/AREA]_para_RAG.md

Exemplos:
- PLANO_MESTRE_para_RAG.md
- HLD_SISTEMA_GERAL_para_RAG.md
- ERS_COMPLETO_para_RAG.md
- AGENTE_ORQUESTRADOR_SPEC_para_RAG.md
```

### 📂 Organização por Pasta
Cada pasta possui seu próprio `README.md` com:
- Propósito específico
- Tipos de documentos aceitos
- Convenções de nomenclatura
- Critérios de qualidade
- Responsáveis pela manutenção

## 🔍 Como Usar o Sistema RAG

### 👤 Para o Maestro
1. **Consulta Direta**: Use `#Context` no Trae IDE para buscar informações específicas
2. **Validação**: Verifique se documentos estão atualizados antes de tomar decisões
3. **Atualização**: Mantenha documentos sincronizados com mudanças do projeto

### 🤖 Para Agentes de IA
1. **Consulta Obrigatória**: SEMPRE consulte o RAG antes de gerar código/documentação
2. **Priorização**: Use a hierarquia de prioridades para otimizar consultas
3. **Contextualização**: Combine informações de múltiplas categorias quando necessário
4. **Atualização**: Sinalize quando encontrar informações desatualizadas

## 🎯 Agentes e Suas Prioridades

### 🎭 @AgenteM_Orquestrador
**Prioridade**: `01_Documentacao_Central` → `04_Gestao_e_Processos` → `08_Conhecimento_Especializado`

### 🛠️ @AgenteM_DevFastAPI
**Prioridade**: `02_Arquitetura_e_Design` → `03_Requisitos_e_Especificacoes` → `06_Tech_Stack`

### 🏗️ @AgenteM_ArquitetoTI
**Prioridade**: `02_Arquitetura_e_Design` → `06_Tech_Stack` → `03_Requisitos_e_Especificacoes`

### 🎨 @AgenteM_UXDesigner
**Prioridade**: `07_UX_e_Design` → `03_Requisitos_e_Especificacoes` → `08_Conhecimento_Especializado`

### ⚙️ @AgenteM_DevOps
**Prioridade**: `06_Tech_Stack` → `02_Arquitetura_e_Design` → `04_Gestao_e_Processos`

## 📊 Métricas de Qualidade

### ✅ Indicadores de Sucesso
- **Cobertura**: Todos os tópicos principais documentados
- **Atualidade**: Documentos sincronizados com desenvolvimento
- **Acessibilidade**: Tempo de resposta < 2s para consultas RAG
- **Relevância**: Taxa de acerto > 85% nas consultas dos agentes

### 🔄 Processo de Manutenção
- **Diário**: Atualização de KANBAN e status
- **Semanal**: Revisão de documentos críticos
- **Mensal**: Auditoria completa e otimização
- **Trimestral**: Reestruturação se necessário

## 🚀 Otimizações Implementadas

### 📈 Melhorias na Organização
1. **Categorização Semântica**: Documentos agrupados por contexto de uso
2. **Hierarquia de Prioridades**: Acesso otimizado por frequência de consulta
3. **Nomenclatura Padronizada**: Facilita busca e identificação
4. **READMEs Específicos**: Orientação clara para cada categoria

### 🎯 Benefícios para Agentes
- **Consultas Mais Rápidas**: Estrutura otimizada reduz tempo de busca
- **Contexto Melhorado**: Informações relacionadas agrupadas
- **Qualidade Superior**: Documentação padronizada e atualizada
- **Especialização**: Cada agente sabe onde encontrar seu conhecimento

## 🔧 Configuração Técnica

### 📋 Requisitos
- **Embedding Model**: `BAAI/bge-m3` (via Sentence Transformers)
- **Vector Store**: FAISS-GPU (CUDA)
- **Framework**: LangChain (Python)
- **Ambiente**: Conda (Python 3.10)

### ⚙️ Configuração RAG
```python
# Configuração otimizada para consultas
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RESULTS = 5
SIMILARITY_THRESHOLD = 0.7
```

## 📚 Documentos Migrados

### ✅ Reorganização Concluída
- `HLD_para_RAG.md` → `02_Arquitetura_e_Design/`
- `STYLE_GUIDE_para_RAG.md` → `02_Arquitetura_e_Design/`
- `ERS_para_RAG.md` → `03_Requisitos_e_Especificacoes/`
- `API_Specs_Sumario_para_RAG.md` → `03_Requisitos_e_Especificacoes/`
- `GUIA_AVANCADO_para_RAG.md` → `01_Documentacao_Central/`
- `PM_Knowledge/` → `08_Conhecimento_Especializado/`
- `UX_Knowledge/` → `07_UX_e_Design/`

## 🎯 Próximos Passos

### 🔄 Melhorias Contínuas
1. **Monitoramento**: Implementar métricas de uso por categoria
2. **Feedback Loop**: Coletar feedback dos agentes sobre qualidade
3. **Automação**: Scripts para validação de nomenclatura
4. **Expansão**: Adicionar novas categorias conforme necessário

### 📈 Evolução do Sistema
- **Indexação Automática**: Reindexação automática quando documentos mudam
- **Versionamento**: Controle de versões para documentos críticos
- **Analytics**: Dashboard de uso e performance do RAG
- **Integração**: Conexão direta com ferramentas de desenvolvimento

---

## 📞 Suporte

**Responsável Geral**: @AgenteM_Orquestrador  
**Manutenção Técnica**: @AgenteM_DevFastAPI  
**Coordenação**: Maestro (Bruno S. Rosa)

**Última Atualização**: Junho 2025  
**Versão**: 2.0 (Estrutura Otimizada)

---

*Este sistema RAG foi projetado para evoluir continuamente, garantindo que os agentes de IA do Recoloca.ai tenham acesso ao conhecimento mais relevante e atualizado para suas funções específicas.*