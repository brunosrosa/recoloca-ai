# ADR-004: Evolução do MCP Server

**Status:** Aceito  
**Data:** 2025-06-19  
**Decisores:** @AgenteM_ArquitetoTI, @Maestro  
**Tags:** #mcp #server #integracao #trae #rag #evolucao

## Contexto

O projeto Recoloca.ai adota uma metodologia de "Solo Agile Development Augmented by AI" que requer integração eficiente entre agentes de IA especializados e a base de conhecimento do projeto. O MCP (Model Context Protocol) Server é o componente crítico que viabiliza essa integração, permitindo que agentes no Trae IDE acessem o sistema RAG de forma transparente.

### Necessidades Identificadas

1. **Integração RAG-Agentes**: Agentes precisam acessar documentação contextualizada
2. **Performance**: Consultas devem ser respondidas em <2 segundos
3. **Escalabilidade**: Suporte a múltiplos agentes simultâneos
4. **Confiabilidade**: Sistema deve ser robusto e auto-recuperável
5. **Observabilidade**: Monitoramento e logging detalhados

### Estado Atual

O MCP Server foi implementado como prova de conceito com funcionalidades básicas:
- Protocolo MCP implementado
- Interface com sistema RAG local
- Configuração básica no Trae IDE
- Testes de conectividade funcionais

## Decisão

Evoluir o MCP Server para uma **arquitetura robusta e escalável** que suporte as necessidades de produção do projeto Recoloca.ai.

### Arquitetura Evolutiva

#### 1. Core MCP Server (`mcp_server.py`)
```python
class RecolocaRAGServer:
    def __init__(self):
        self.server = Server("rag_recoloca")
        self.rag_retriever = None
        self.metrics_monitor = None
        self.health_checker = None
    
    async def initialize(self):
        # Inicialização assíncrona
        # Carregamento de modelos
        # Setup de monitoramento
```

#### 2. Funcionalidades Principais

**Consulta RAG Semântica**
```python
@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    return [
        Tool(
            name="rag_query",
            description="Consulta semântica no sistema RAG",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "top_k": {"type": "integer", "default": 5},
                    "min_score": {"type": "number", "default": 0.7}
                }
            }
        )
    ]
```

**Busca por Documento**
```python
@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "rag_search_by_document":
        return await search_documents(arguments)
```

#### 3. Sistema de Monitoramento

**Métricas de Performance**
- Tempo de resposta por consulta
- Throughput de requisições
- Uso de memória e CPU
- Qualidade das respostas (score médio)

**Health Checks**
- Status do modelo de embedding
- Conectividade com índices
- Disponibilidade de GPU
- Integridade dos dados

#### 4. Configuração Avançada

**Arquivo de Configuração**
```python
MCP_SERVER_CONFIG = {
    "name": "rag_recoloca",
    "version": "2.0.0",
    "description": "RAG Server para Recoloca.ai - Acesso à base de conhecimento",
    "max_concurrent_requests": 10,
    "request_timeout": 30,
    "cache_enabled": True,
    "cache_ttl": 3600,
    "logging_level": "INFO"
}
```

**Configuração Trae IDE**
```json
{
  "mcpServers": {
    "recoloca-rag": {
      "command": "python",
      "args": ["rag_infra/mcp_server.py"],
      "env": {
        "RAG_CONFIG_PATH": "rag_infra/config/rag_config.json"
      }
    }
  }
}
```

## Justificativa

### Vantagens da Evolução

1. **Produtividade dos Agentes**
   - Acesso instantâneo à documentação
   - Respostas contextualizadas
   - Redução de tempo de pesquisa

2. **Qualidade das Respostas**
   - Busca semântica avançada
   - Filtragem por relevância
   - Metadados estruturados

3. **Escalabilidade**
   - Suporte a múltiplos agentes
   - Cache inteligente
   - Balanceamento de carga

4. **Confiabilidade**
   - Auto-recuperação de falhas
   - Fallbacks automáticos
   - Monitoramento proativo

5. **Observabilidade**
   - Logs estruturados
   - Métricas detalhadas
   - Alertas automáticos

### Alternativas Consideradas

1. **API REST Simples**: Rejeitado por não integrar nativamente com Trae IDE
2. **WebSocket Server**: Complexidade desnecessária para o caso de uso
3. **gRPC Server**: Overhead de configuração muito alto
4. **Plugin Trae Nativo**: Limitações de flexibilidade e manutenção

## Implementação

### Fases de Evolução

#### Fase 1: Estabilização (Atual)
- ✅ Protocolo MCP básico implementado
- ✅ Integração com RAG funcional
- ✅ Testes de conectividade
- ✅ Configuração no Trae IDE

#### Fase 2: Robustez (Em Andamento)
- 🔄 Sistema de monitoramento
- 🔄 Cache inteligente
- 🔄 Error handling robusto
- 🔄 Logging estruturado

#### Fase 3: Otimização (Planejado)
- ⏳ Performance tuning
- ⏳ Balanceamento de carga
- ⏳ Compressão de respostas
- ⏳ Métricas avançadas

#### Fase 4: Escalabilidade (Futuro)
- ⏳ Clustering
- ⏳ Replicação
- ⏳ Auto-scaling
- ⏳ Multi-tenancy

### Estrutura de Arquivos

```
rag_infra/
├── mcp_server.py                 # Servidor principal
├── core_logic/
│   ├── rag_retriever.py         # Interface RAG
│   ├── rag_metrics_monitor.py   # Monitoramento
│   └── pytorch_gpu_retriever.py # Backend otimizado
├── config/
│   ├── mcp_config.json          # Configuração MCP
│   └── trae_mcp_config.json     # Config Trae IDE
├── logs/
│   └── mcp_server.log           # Logs do servidor
└── tests/
    └── test_mcp_server.py       # Testes de integração
```

### APIs Disponíveis

#### 1. Consulta RAG
```python
rag_query(
    query: str,           # Consulta semântica
    top_k: int = 5,       # Número de resultados
    min_score: float = 0.7, # Score mínimo
    category_filter: str = None # Filtro por categoria
) -> List[Document]
```

#### 2. Busca por Documento
```python
rag_search_by_document(
    document_pattern: str, # Padrão de busca
    top_k: int = 5        # Máximo de resultados
) -> List[Document]
```

#### 3. Lista de Documentos
```python
rag_get_document_list(
    category: str = None  # Filtro opcional
) -> List[DocumentInfo]
```

#### 4. Status do Sistema
```python
rag_get_status() -> SystemStatus
```

## Consequências

### Positivas

1. **Produtividade**: Agentes mais eficientes com acesso contextualizado
2. **Qualidade**: Respostas mais precisas e relevantes
3. **Escalabilidade**: Sistema preparado para crescimento
4. **Manutenibilidade**: Código bem estruturado e monitorado
5. **Confiabilidade**: Sistema robusto com auto-recuperação

### Negativas

1. **Complexidade**: Sistema mais complexo para manter
2. **Recursos**: Maior uso de CPU/memória para monitoramento
3. **Dependências**: Mais dependências externas
4. **Curva de Aprendizado**: Equipe precisa entender MCP

### Riscos e Mitigações

1. **Falha do Servidor MCP**
   - **Mitigação**: Auto-restart e fallback para consulta direta

2. **Performance Degradada**
   - **Mitigação**: Cache inteligente e otimizações de consulta

3. **Incompatibilidade Trae IDE**
   - **Mitigação**: Testes de integração contínuos

4. **Sobrecarga de Monitoramento**
   - **Mitigação**: Configuração ajustável de logging

## Métricas de Sucesso

### Performance
- **Tempo de Resposta**: <2 segundos para 95% das consultas
- **Throughput**: >100 consultas/minuto
- **Disponibilidade**: >99.5% uptime
- **Precisão**: Score médio >0.8 nas respostas

### Qualidade
- **Relevância**: >90% das respostas consideradas úteis
- **Cobertura**: Acesso a 100% da documentação indexada
- **Atualização**: Índice atualizado em <5 minutos

### Operacional
- **Facilidade de Uso**: Agentes conseguem usar sem treinamento
- **Estabilidade**: <1 falha por semana
- **Observabilidade**: 100% das operações logadas

## Próximos Passos

1. **Implementar Monitoramento**: Sistema de métricas e alertas
2. **Otimizar Cache**: Implementar cache inteligente de consultas
3. **Expandir APIs**: Adicionar funcionalidades avançadas
4. **Documentar Uso**: Guias para agentes e desenvolvedores
5. **Testes de Carga**: Validar performance sob stress

## Validação

### Critérios Técnicos
- ✅ Protocolo MCP implementado corretamente
- ✅ Integração com RAG funcional
- ✅ Performance adequada (<2s)
- 🔄 Monitoramento implementado
- ⏳ Cache otimizado

### Critérios de Negócio
- ✅ Agentes conseguem acessar documentação
- ✅ Respostas são relevantes e úteis
- 🔄 Produtividade dos agentes melhorou
- ⏳ Sistema é confiável em produção

## Referências

- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Trae IDE MCP Integration](https://docs.trae.ai/mcp)
- [Sistema RAG Recoloca.ai](../../rag_infra/README.md)
- [ADR-001: Ferramentas Core](./ADR-001_Ferramentas_Core.md)
- [ADR-003: Otimizações RTX 2060](./ADR-003_Otimizacoes_RTX_2060.md)

---

**Versão:** 1.0  
**Última Atualização:** 2025-06-19  
**Próxima Revisão:** 2025-02-19