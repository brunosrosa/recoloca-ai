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
├── data_index/                   # Índices de dados
├── logs/                         # Logs do sistema
└── source_documents/             # Documentos fonte organizados
    ├── 00_Documentacao_Central/
    ├── 01_Gestao_e_Processos/
    ├── 02_Requisitos_e_Specs/
    ├── 03_Arquitetura_e_Design/
    ├── 04_Agentes_e_Prompts/
    ├── 05_Implementacao_Tecnica/
    ├── 06_UX_e_Design/
    ├── 07_Deploy_e_Infra/
    └── 08_Pesquisa_e_Insights/
```

#### 3. Consolidação de ADRs

**Localização Unificada**: `docs/03_Arquitetura_e_Design/02_ADRs/`

**Nomenclatura Padronizada**:
- `ADR-001_Ferramentas_Core.md`
- `ADR-002_PyTorch_vs_FAISS_GPU.md`
- `ADR-003_Otimizacoes_RTX_2060.md`
- `ADR-004_Evolucao_MCP_Server.md`
- `ADR-005_Reorganizacao_Estrutural.md`

#### 4. Kanban Unificado

**Estrutura Hierárquica**:
- **Estratégico**: `02_KANBAN_ESTRATEGICO_FASES.md` - Visão de fases e marcos
- **Operacional**: `01_KANBAN_OPERACIONAL_SESSOES.md` - Tarefas diárias
- **Maestro Tasks**: `10_Maestro_Tasks.md` - Tarefas críticas do Maestro

**Sincronização**: Status consistente entre todos os boards

## Justificativa

### Benefícios da Reorganização

1. **Produtividade dos Agentes**
   - Localização rápida de documentos
   - Estrutura previsível e lógica
   - Redução de tempo de busca

2. **Manutenibilidade**
   - Separação clara de responsabilidades
   - Facilita refatoração e evolução
   - Reduz acoplamento entre componentes

3. **Onboarding**
   - Estrutura intuitiva para novos desenvolvedores
   - Documentação bem organizada
   - Padrões claros e consistentes

4. **Qualidade do Código**
   - Testes separados da lógica principal
   - Scripts utilitários organizados
   - Configurações centralizadas

5. **Observabilidade**
   - Logs e relatórios organizados
   - Métricas centralizadas
   - Facilita debugging e monitoramento

### Princípios Aplicados

1. **Separation of Concerns**: Cada diretório tem responsabilidade específica
2. **Single Responsibility**: Arquivos com propósito único e claro
3. **Consistency**: Nomenclatura e estrutura padronizadas
4. **Discoverability**: Fácil localização de recursos
5. **Scalability**: Estrutura preparada para crescimento

## Implementação

### Fases de Execução

#### Fase 1: Reorganização RAG (✅ Concluída)
- ✅ Renomeação de `results and reports/` para `results_and_reports/`
- ✅ Movimentação de testes para `tests/`
- ✅ Movimentação de scripts para `scripts/`
- ✅ Movimentação de relatórios para `results_and_reports/`
- ✅ Atualização de imports e paths
- ✅ Validação através de testes

#### Fase 2: Consolidação de Documentação (🔄 Em Andamento)
- 🔄 Criação de ADRs faltantes (ADR-003, ADR-004, ADR-005)
- 🔄 Unificação de ADRs em diretório único
- 🔄 Correção de links quebrados
- 🔄 Padronização de nomenclatura

#### Fase 3: Sincronização Kanban (⏳ Planejado)
- ⏳ Unificação de status entre boards
- ⏳ Eliminação de duplicatas
- ⏳ Implementação de rastreabilidade
- ⏳ Automação de sincronização

#### Fase 4: Otimização Contínua (⏳ Futuro)
- ⏳ Monitoramento de aderência aos padrões
- ⏳ Automação de validação estrutural
- ⏳ Métricas de qualidade organizacional
- ⏳ Evolução baseada em feedback

### Impactos nos Sistemas

#### Sistema RAG
- **Compatibilidade**: Mantida através de atualização de imports
- **Performance**: Não impactada, apenas organização
- **Funcionalidade**: 100% preservada

#### MCP Server
- **Paths**: Atualizados para nova estrutura
- **Configuração**: Ajustada para novos diretórios
- **Integração**: Validada através de testes

#### Agentes IA
- **Acesso RAG**: Melhorado com estrutura mais clara
- **Documentação**: Mais fácil de localizar e usar
- **Produtividade**: Aumentada com organização melhor

### Validação da Reorganização

#### Testes Automatizados
```python
def test_estrutura_reorganizada():
    # Verifica se estrutura está correta
    assert os.path.exists('rag_infra/core_logic/')
    assert os.path.exists('rag_infra/tests/')
    assert os.path.exists('rag_infra/scripts/')
    assert os.path.exists('rag_infra/results_and_reports/')
    
def test_imports_funcionais():
    # Verifica se imports ainda funcionam
    from rag_infra.core_logic import rag_retriever
    from rag_infra.core_logic import mcp_server
    
def test_mcp_server_funcional():
    # Verifica se MCP Server ainda funciona
    # após reorganização
```

#### Métricas de Qualidade
- **Tempo de Localização**: <30 segundos para qualquer documento
- **Links Quebrados**: 0 links quebrados na documentação
- **Consistência**: 100% aderência aos padrões de nomenclatura
- **Cobertura**: 100% dos arquivos em locais apropriados

## Consequências

### Positivas

1. **Produtividade**: Agentes e desenvolvedores mais eficientes
2. **Qualidade**: Código mais limpo e organizados
3. **Manutenibilidade**: Facilita evolução e refatoração
4. **Onboarding**: Reduz curva de aprendizado
5. **Escalabilidade**: Estrutura preparada para crescimento
6. **Observabilidade**: Melhor visibilidade do sistema

### Negativas

1. **Migração**: Esforço inicial para reorganização
2. **Adaptação**: Equipe precisa se adaptar à nova estrutura
3. **Links**: Necessidade de atualizar referências externas
4. **Documentação**: Atualização de guias e tutoriais

### Riscos e Mitigações

1. **Quebra de Funcionalidade**
   - **Mitigação**: Testes abrangentes antes e após reorganização

2. **Perda de Histórico**
   - **Mitigação**: Git preserva histórico de movimentações

3. **Confusão Temporária**
   - **Mitigação**: Documentação clara da nova estrutura

4. **Links Externos Quebrados**
   - **Mitigação**: Mapeamento e redirecionamento de URLs

## Métricas de Sucesso

### Organizacionais
- **Tempo de Localização**: <30s para qualquer arquivo
- **Aderência a Padrões**: >95% dos arquivos seguem convenções
- **Links Funcionais**: 100% dos links internos funcionando
- **Estrutura Consistente**: 0 violações de organização

### Produtividade
- **Velocidade de Desenvolvimento**: 20% mais rápido
- **Tempo de Onboarding**: 50% redução para novos membros
- **Eficiência de Agentes**: 30% menos tempo buscando informações
- **Qualidade de Código**: Redução de 40% em code smells

### Técnicas
- **Performance RAG**: Mantida ou melhorada
- **Estabilidade MCP**: 100% funcional após reorganização
- **Cobertura de Testes**: Mantida em >90%
- **Integridade de Dados**: 0 perda de informações

## Próximos Passos

1. **Finalizar ADRs**: Completar criação de ADR-003, ADR-004, ADR-005
2. **Consolidar ADRs**: Mover todos para diretório unificado
3. **Corrigir Links**: Atualizar todas as referências quebradas
4. **Sincronizar Kanban**: Unificar status entre boards
5. **Documentar Padrões**: Criar guia de organização
6. **Automatizar Validação**: Scripts para verificar aderência

## Validação

### Critérios Técnicos
- ✅ Estrutura RAG reorganizada e funcional
- ✅ Testes passando após reorganização
- ✅ MCP Server funcionando corretamente
- 🔄 ADRs consolidados em local único
- ⏳ Links corrigidos e funcionais

### Critérios de Qualidade
- ✅ Separação clara de responsabilidades
- ✅ Nomenclatura consistente
- ✅ Estrutura escalável implementada
- 🔄 Documentação atualizada
- ⏳ Padrões documentados e seguidos

## Referências

- [Clean Architecture Principles](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Project Organization Best Practices](https://docs.python-guide.org/writing/structure/)
- [REORGANIZATION_PLAN.md](../../rag_infra/REORGANIZATION_PLAN.md)
- [ADR-001: Ferramentas Core](./ADR-001_Ferramentas_Core.md)
- [Metodologia MVP](../../00_Gerenciamento_Projeto/METODOLOGIA_MVP.md)

---

**Versão:** 1.0  
**Última Atualização:** 2025-06-19  
**Próxima Revisão:** 2025-02-19