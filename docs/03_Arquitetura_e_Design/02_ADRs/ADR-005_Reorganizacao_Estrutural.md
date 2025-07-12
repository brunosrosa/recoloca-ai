# ADR-005: Reorganização Estrutural do Projeto

**Status:** Aceito  
**Data:** 2025-06-19  
**Decisores:** @AgenteM_ArquitetoTI, @AgenteM_Orquestrador, @Maestro  
**Tags:** #organizacao #estrutura #documentacao #infraestrutura #kanban

## Contexto

O projeto Recoloca.ai cresceu organicamente durante as fases iniciais de desenvolvimento, resultando em uma estrutura de diretórios e documentação que não reflete adequadamente a maturidade atual do projeto. A metodologia "Solo Agile Development Augmented by AI" requer uma organização clara e eficiente para maximizar a produtividade dos agentes de IA e facilitar a manutenção do código.

### Problemas Identificados

1. **Estrutura de Diretórios Inconsistente**
   - Mistura de lógica core, testes e demos no mesmo diretório
   - Nomenclatura inconsistente (snake_case vs kebab-case)
   - Arquivos de diferentes propósitos agrupados incorretamente

2. **Documentação Fragmentada**
   - ADRs espalhados em múltiplos diretórios
   - Numeração inconsistente de documentos
   - Links quebrados entre documentos

3. **Kanban Desorganizado**
   - Tarefas duplicadas entre diferentes boards
   - Status inconsistentes entre operacional e estratégico
   - Falta de rastreabilidade de progresso

4. **Infraestrutura RAG Confusa**
   - Arquivos de teste misturados com lógica principal
   - Scripts utilitários em locais inadequados
   - Relatórios e resultados sem organização clara

## Decisão

Implementar uma **reorganização estrutural completa** do projeto seguindo princípios de Clean Architecture e boas práticas de organização de projetos de software.

### Estrutura Organizacional Adotada

#### 1. Hierarquia de Documentação

```
docs/
├── 00_Gerenciamento_Projeto/     # Gestão e processos
│   ├── KANBAN/                   # Boards Kanban
│   ├── 10_Maestro_Tasks.md       # Tarefas do Maestro
│   └── METODOLOGIA_MVP.md        # Metodologia do projeto
├── 01_Visao_e_Estrategia/        # Visão estratégica
├── 02_Requisitos/                # Requisitos funcionais/não-funcionais
├── 03_Arquitetura_e_Design/      # Arquitetura e ADRs
│   ├── 02_ADRs/                  # ADRs consolidados
│   └── 00_API_Specs/             # Especificações de API
├── 04_Agentes_IA/                # Configuração de agentes
├── 05_Prompts/                   # Prompts estruturais
├── 06_Implementacao/             # Detalhes de implementação
├── 07_UX_e_Design/               # Design e experiência
└── 08_Deployment/                # Deploy e infraestrutura
```

#### 2. Estrutura RAG Reorganizada

```
rag_infra/
├── core_logic/                   # APENAS lógica principal
│   ├── constants.py              # Constantes do sistema
│   ├── embedding_model.py        # Modelo de embedding
│   ├── mcp_server.py             # Servidor MCP
│   ├── rag_indexer.py            # Indexador RAG
│   ├── rag_retriever.py          # Recuperador RAG
│   ├── pytorch_gpu_retriever.py  # Retriever GPU otimizado
│   ├── pytorch_optimizations.py  # Otimizações PyTorch
│   ├── torch_utils.py            # Utilitários PyTorch
│   ├── rag_metrics_*.py          # Métricas e monitoramento
│   └── cache/                    # Cache do sistema
├── tests/                        # Testes de integração
│   ├── test_gpu_alternatives.py
│   ├── test_pytorch_gpu_retriever.py
│   ├── test_rag_*.py
│   └── verificar_faiss_gpu.py
├── scripts/                      # Scripts e demos
│   ├── benchmark_pytorch_performance.py
│   ├── convert_faiss_to_pytorch.py
│   ├── demo_rag_system.py
│   ├── setup_rtx2060_optimizations.py
│   └── start_rtx2060_optimized.py
├── results_and_reports/          # Relatórios e resultados
│   ├── GPU_OPTIMIZATION_REPORT.md
│   ├── pytorch_performance_benchmark.json
│   ├── rag_final_integration_results.json
│   └── constants.py.backup
├── config/                       # Configurações
├── data_index/                   # Índices e dados
└── docs/                         # Documentação específica
```

#### 3. Consolidação de Kanban

**Estrutura Unificada**:
- **KANBAN_OPERACIONAL.md**: Tarefas de desenvolvimento e implementação
- **KANBAN_ESTRATEGICO.md**: Planejamento e decisões arquiteturais
- **KANBAN_MAESTRO.md**: Coordenação e orquestração de agentes

## Justificativa

### Princípios Aplicados

1. **Separação de Responsabilidades**
   - Lógica core isolada de testes e demos
   - Documentação organizada por domínio
   - Scripts utilitários em diretório dedicado

2. **Convenções de Nomenclatura**
   - Prefixos numéricos para ordenação lógica
   - snake_case para arquivos Python
   - kebab-case para documentação
   - UPPER_CASE para arquivos de configuração

3. **Escalabilidade**
   - Estrutura preparada para crescimento
   - Fácil localização de componentes
   - Manutenção simplificada

4. **Produtividade de Agentes IA**
   - Contexto claro para cada diretório
   - Redução de ambiguidade
   - Facilita navegação e compreensão

### Benefícios Esperados

1. **Manutenibilidade**
   - Localização rápida de arquivos
   - Redução de duplicação
   - Clareza de propósito

2. **Colaboração**
   - Estrutura intuitiva para novos desenvolvedores
   - Documentação centralizada
   - Processos padronizados

3. **Qualidade**
   - Separação clara entre produção e teste
   - Versionamento adequado de documentos
   - Rastreabilidade de decisões

## Implementação

### Fases de Migração

#### Fase 1: Reorganização de Documentação
- ✅ Criação da nova estrutura de diretórios
- ✅ Migração de ADRs para localização centralizada
- ✅ Consolidação de boards Kanban
- ✅ Atualização de links e referências

#### Fase 2: Reestruturação RAG
- 🔄 Separação de lógica core, testes e scripts
- 🔄 Reorganização de arquivos de configuração
- 🔄 Consolidação de relatórios e resultados
- ⏳ Atualização de imports e dependências

#### Fase 3: Validação e Testes
- ⏳ Execução de testes de integração
- ⏳ Validação de funcionalidades
- ⏳ Verificação de performance
- ⏳ Documentação de mudanças

#### Fase 4: Otimização
- ⏳ Refinamento da estrutura
- ⏳ Automação de processos
- ⏳ Implementação de métricas
- ⏳ Treinamento de agentes

### Scripts de Migração

1. **migrate_documentation.py**: Reorganização de documentos
2. **restructure_rag_infra.py**: Reestruturação do RAG
3. **update_imports.py**: Atualização de imports
4. **validate_structure.py**: Validação da nova estrutura

## Consequências

### Positivas

1. **Produtividade Aumentada**
   - Localização rápida de arquivos
   - Redução de tempo de navegação
   - Contexto claro para agentes IA

2. **Qualidade Melhorada**
   - Separação clara de responsabilidades
   - Redução de acoplamento
   - Facilita testes e debugging

3. **Manutenibilidade**
   - Estrutura escalável
   - Convenções consistentes
   - Documentação centralizada

4. **Colaboração**
   - Onboarding simplificado
   - Processos padronizados
   - Comunicação clara

### Riscos e Mitigações

1. **Quebra de Funcionalidades**
   - **Risco**: Imports quebrados após migração
   - **Mitigação**: Scripts automatizados de atualização
   - **Validação**: Testes abrangentes pós-migração

2. **Perda de Histórico**
   - **Risco**: Perda de contexto de arquivos movidos
   - **Mitigação**: Documentação de mapeamento
   - **Backup**: Snapshot completo antes da migração

3. **Resistência à Mudança**
   - **Risco**: Dificuldade de adaptação
   - **Mitigação**: Documentação clara e treinamento
   - **Suporte**: Guias de migração detalhados

## Monitoramento

### Métricas de Sucesso

1. **Produtividade**
   - Tempo médio para localizar arquivos
   - Velocidade de desenvolvimento
   - Eficiência de agentes IA

2. **Qualidade**
   - Redução de bugs relacionados a estrutura
   - Cobertura de testes
   - Consistência de código

3. **Manutenibilidade**
   - Tempo para onboarding
   - Facilidade de navegação
   - Clareza de documentação

### Ferramentas de Monitoramento

- **Scripts de Validação**: Verificação automática de estrutura
- **Métricas de Código**: Análise de qualidade e complexidade
- **Feedback de Agentes**: Avaliação de produtividade

## Próximos Passos

1. **Completar Migração RAG**: Finalizar reestruturação do rag_infra
2. **Atualizar Documentação**: Revisar todos os links e referências
3. **Implementar Automação**: Scripts de validação contínua
4. **Treinar Agentes**: Atualizar contextos e prompts
5. **Monitorar Impacto**: Acompanhar métricas de produtividade

## Validação

### Critérios de Aceitação

- ✅ Estrutura de documentação implementada
- ✅ ADRs consolidados e organizados
- ✅ Kanban unificado e funcional
- 🔄 RAG infra reorganizado
- ⏳ Testes passando após migração
- ⏳ Performance mantida ou melhorada
- ⏳ Documentação atualizada

### Testes de Validação

- ✅ Navegação de documentação
- ✅ Localização de ADRs
- ✅ Funcionalidade de Kanban
- 🔄 Execução de sistema RAG
- ⏳ Performance de consultas
- ⏳ Integração com MCP Server

## Referências

- [Clean Architecture Principles](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Project Structure Best Practices](https://docs.python-guide.org/writing/structure/)
- [Documentation Organization](https://www.divio.com/blog/documentation/)
- [ADR Template](https://github.com/joelparkerhenderson/architecture-decision-record)

---

**Versão:** 1.0  
**Última Atualização:** 2025-06-19  
**Próxima Revisão:** 2025-09-19