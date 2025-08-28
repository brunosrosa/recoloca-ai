# ADR-007: Correção do RAGRetriever Local e Otimização de Performance

## Status
**IMPLEMENTADO** - 19/06/2025

## Contexto

Durante a auditoria técnica do sistema RAG (COR-RAG-001), foram identificados problemas específicos com o RAGRetriever local que resultavam em:

1. **Retorno de 0 resultados** em consultas válidas devido a threshold de similaridade muito alto
2. **Seleção inadequada de backend** entre FAISS e PyTorch
3. **Problemas de compatibilidade** com GPU RTX 2060 e FAISS-GPU
4. **Inconsistências** na integração com o MCP Server

### Problemas Identificados

- `MIN_SIMILARITY_SCORE = 0.7` estava muito alto, rejeitando resultados relevantes
- Detecção de GPU funcionando corretamente, mas threshold impedindo retorno de resultados
- Sistema estava usando PyTorch corretamente devido à incompatibilidade da RTX 2060 com FAISS-GPU
- MCP Server funcionando, mas retornando poucos resultados devido ao threshold

## Decisão

### 1. Otimização do Threshold de Similaridade

**Decisão**: Reduzir `MIN_SIMILARITY_SCORE` de `0.7` para `0.2`

**Justificativa**:
- Testes mostraram que scores entre 0.2-0.7 contêm resultados relevantes
- Threshold 0.7 era muito restritivo para o modelo BGE-M3
- Threshold 0.2 mantém qualidade enquanto aumenta recall

### 2. Validação da Seleção de Backend

**Decisão**: Manter lógica atual de detecção de GPU

**Justificativa**:
- Sistema corretamente detecta RTX 2060 como incompatível com FAISS-GPU
- PyTorch backend está funcionando adequadamente
- Performance satisfatória (busca em ~60-170ms)

### 3. Melhorias na Integração MCP

**Decisão**: Validar e documentar funções do MCP Server

**Justificativa**:
- `search_documents()` e `get_retriever()` funcionando corretamente
- Integração com Trae IDE operacional
- Necessário apenas ajuste de threshold

## Implementação

### Alterações Realizadas

1. **constants.py**:
   ```python
   # Antes
   MIN_SIMILARITY_SCORE = 0.7
   
   # Depois  
   MIN_SIMILARITY_SCORE = 0.2
   ```

2. **Testes de Validação**:
   - Criado `diagnostico_rag.py` para diagnóstico completo
   - Criado `correcao_rag.py` para aplicação de correções
   - Validação com múltiplas queries de teste

### Resultados dos Testes

**Antes da Correção**:
- Query "Recoloca.ai MVP desenvolvimento": 0 resultados
- Threshold 0.7: Muito restritivo

**Após a Correção**:
- Query "Recoloca.ai MVP desenvolvimento": 5 resultados
- Scores típicos: 0.2 - 0.7
- Performance: 12-170ms por consulta

### Configuração do Sistema

**Hardware Detectado**:
- GPU: NVIDIA GeForce RTX 2060
- CUDA: Disponível
- FAISS-GPU: Não compatível (conforme esperado)

**Backend Selecionado**:
- PyTorch com GPU acceleration
- Modelo: BAAI/bge-m3
- Documentos indexados: 281

## Consequências

### Positivas

1. **Melhoria Significativa no Recall**:
   - Consultas que retornavam 0 resultados agora retornam 3-5 resultados relevantes
   - Mantém precisão adequada com scores > 0.2

2. **Performance Otimizada**:
   - Busca rápida (12-170ms)
   - Cache funcionando adequadamente
   - Cleanup de memória GPU eficiente

3. **Integração MCP Estável**:
   - `search_documents()` funcionando
   - `get_retriever()` operacional
   - Compatibilidade com Trae IDE mantida

### Riscos Mitigados

1. **Falsos Positivos**: Threshold 0.2 ainda filtra resultados irrelevantes
2. **Performance**: Sistema mantém velocidade adequada
3. **Qualidade**: Scores disponíveis para ranking adicional

## Monitoramento

### Métricas a Acompanhar

1. **Qualidade dos Resultados**:
   - Distribuição de scores retornados
   - Feedback de relevância dos usuários
   - Taxa de cliques nos resultados

2. **Performance**:
   - Tempo de resposta das consultas
   - Uso de memória GPU
   - Taxa de cache hit

3. **Integração**:
   - Estabilidade do MCP Server
   - Logs de erro do Trae IDE
   - Disponibilidade do sistema

### Alertas Configurados

- Tempo de resposta > 500ms
- Taxa de erro > 5%
- Uso de memória GPU > 80%
- Falhas na inicialização do retriever

## Próximos Passos

1. **Fase Imediata** (Concluída):
   - ✅ Aplicar correção do threshold
   - ✅ Validar funcionamento
   - ✅ Documentar alterações

2. **Fase de Monitoramento** (Em andamento):
   - Acompanhar métricas de qualidade
   - Coletar feedback de uso
   - Ajustar threshold se necessário

3. **Fase de Otimização** (Planejada):
   - Implementar threshold dinâmico
   - Adicionar métricas de relevância
   - Otimizar cache de consultas

## Referências

- **Tarefa**: COR-RAG-001 - Correção RAGRetriever Local
- **Documentos**: 
  - `diagnostico_rag.py` - Script de diagnóstico
  - `correcao_rag.py` - Script de correção
  - `test_rag_quick.py` - Testes de validação
- **Logs**: `rag_infra/logs/` - Logs de execução
- **Backup**: `constants.py.backup` - Backup da configuração anterior

## Aprovação

- **Arquiteto**: @AgenteM_ArquitetoTI ✅
- **Data**: 19/06/2025
- **Revisão**: Aprovada para produção

---

**Nota**: Esta correção resolve o problema crítico identificado na auditoria técnica e estabelece uma base sólida para o sistema RAG do Recoloca.ai.