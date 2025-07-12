# ADR-002: Seleção de Backend para Retrieval - PyTorch vs FAISS-GPU

## Status
**APROVADO** - 19/06/2025

## Contexto

O sistema RAG do Recoloca.ai requer um backend eficiente para busca semântica em documentos indexados. Durante o desenvolvimento e otimização do sistema, foi necessário escolher entre duas abordagens principais:

1. **FAISS-GPU**: Framework especializado do Facebook para busca de similaridade com aceleração GPU
2. **PyTorch**: Framework de deep learning com capacidades de busca semântica

### Problema Identificado

Durante a implementação inicial, foram identificados problemas de compatibilidade específicos:

- **Hardware Target**: NVIDIA GeForce RTX 2060 (arquitetura Turing)
- **Sistema Operacional**: Windows 11 com WDDM (Windows Display Driver Model)
- **Limitações FAISS-GPU**: Incompatibilidade conhecida com GPUs GeForce em modo WDDM
- **Requisitos de Performance**: Busca semântica em ~280 documentos com latência < 200ms

### Contexto Técnico

O sistema utiliza:
- **Modelo de Embedding**: BAAI/bge-m3 (1024 dimensões)
- **Documentos Indexados**: 281 documentos técnicos
- **Threshold de Similaridade**: 0.2 (otimizado)
- **Volume de Consultas**: Baixo a médio (desenvolvimento/uso pessoal)

## Decisão

### Implementação de Backend Híbrido com Detecção Automática

**Decisão Principal**: Implementar sistema de detecção automática de compatibilidade GPU que seleciona o backend mais adequado:

1. **Detecção de Compatibilidade**:
   ```python
   def _detect_gpu_compatibility(self):
       if not torch.cuda.is_available():
           return False
       
       gpu_name = torch.cuda.get_device_name(0).lower()
       incompatible_gpus = ['rtx 2060', 'gtx 1660', 'gtx 1650']
       
       if any(gpu in gpu_name for gpu in incompatible_gpus):
           return False
   ```

2. **Seleção de Backend**:
   - **PyTorch**: Para GPUs incompatíveis com FAISS-GPU (RTX 2060, GTX 1660, GTX 1650)
   - **FAISS-GPU**: Para GPUs compatíveis (RTX 3000+, RTX 4000+, Tesla, Quadro)

### Justificativas Técnicas

#### Para PyTorch (RTX 2060 e similares)

**Vantagens**:
- **Compatibilidade Total**: Funciona nativamente com CUDA em GPUs GeForce
- **Flexibilidade**: Permite implementações customizadas de busca
- **Integração**: Melhor integração com pipeline de ML existente
- **Debugging**: Mais fácil de debugar e otimizar
- **Performance Adequada**: 12-170ms para consultas típicas

**Desvantagens**:
- **Overhead**: Maior uso de memória comparado ao FAISS otimizado
- **Complexidade**: Requer implementação manual de algoritmos de busca
- **Escalabilidade**: Menos otimizado para grandes volumes

#### Para FAISS-GPU (GPUs Compatíveis)

**Vantagens**:
- **Performance Superior**: Altamente otimizado para busca de similaridade
- **Escalabilidade**: Excelente para grandes volumes de dados
- **Memória Eficiente**: Uso otimizado de memória GPU
- **Maturidade**: Framework maduro e testado

**Desvantagens**:
- **Compatibilidade Limitada**: Problemas com GPUs GeForce em WDDM
- **Flexibilidade Reduzida**: Menos customizável
- **Debugging Complexo**: Mais difícil de debugar problemas

## Implementação

### Arquitetura da Solução

```python
class RAGRetriever:
    def __init__(self):
        self.use_pytorch = not self._detect_gpu_compatibility()
        
        if self.use_pytorch:
            self.pytorch_retriever = PyTorchGPURetriever()
        else:
            self.faiss_index = self._load_faiss_index()
    
    def search(self, query, top_k=5, min_score=0.2):
        if self.use_pytorch:
            return self.pytorch_retriever.search(query, top_k, min_score)
        else:
            return self._search_faiss(query, top_k, min_score)
```

### Configuração Específica RTX 2060

**Otimizações Implementadas**:
- **Batch Size**: 32 (otimizado para 6GB VRAM)
- **Precision**: FP16 para reduzir uso de memória
- **Cache Management**: Limpeza automática de cache CUDA
- **Memory Monitoring**: Monitoramento de uso de VRAM

### Métricas de Performance

**PyTorch Backend (RTX 2060)**:
- **Latência Média**: 60-120ms
- **Latência P95**: 170ms
- **Uso de VRAM**: ~2GB
- **Throughput**: 15-20 consultas/segundo
- **Precisão**: Mantida (scores 0.2-0.7)

**FAISS-GPU Backend (GPUs Compatíveis)**:
- **Latência Média**: 10-30ms
- **Latência P95**: 50ms
- **Uso de VRAM**: ~1GB
- **Throughput**: 50+ consultas/segundo
- **Precisão**: Equivalente

## Consequências

### Positivas

1. **Compatibilidade Universal**:
   - Sistema funciona em qualquer GPU CUDA
   - Detecção automática elimina configuração manual
   - Fallback graceful para CPU se necessário

2. **Performance Otimizada**:
   - Cada GPU utiliza o backend mais adequado
   - Performance satisfatória em ambos os casos
   - Escalabilidade preservada para GPUs compatíveis

3. **Manutenibilidade**:
   - Código unificado com abstração clara
   - Testes automatizados para ambos os backends
   - Logs detalhados para debugging

4. **Experiência do Usuário**:
   - Funcionamento transparente
   - Performance consistente
   - Sem necessidade de configuração técnica

### Riscos e Mitigações

1. **Complexidade de Código**:
   - **Risco**: Manutenção de dois backends
   - **Mitigação**: Interface unificada e testes abrangentes

2. **Inconsistências de Resultado**:
   - **Risco**: Pequenas diferenças entre backends
   - **Mitigação**: Testes de paridade e normalização de scores

3. **Performance Variável**:
   - **Risco**: Performance diferente entre GPUs
   - **Mitigação**: Benchmarks e otimizações específicas

## Monitoramento

### Métricas Acompanhadas

1. **Performance por Backend**:
   - Latência de consultas
   - Uso de memória GPU
   - Taxa de erro
   - Distribuição de scores

2. **Compatibilidade**:
   - Taxa de detecção correta
   - Fallbacks para CPU
   - Erros de inicialização

3. **Qualidade dos Resultados**:
   - Consistência entre backends
   - Relevância dos resultados
   - Feedback de usuários

### Alertas Configurados

- Latência > 500ms
- Uso de VRAM > 80%
- Taxa de erro > 5%
- Inconsistências entre backends

## Evolução Futura

### Próximas Otimizações

1. **Fase Imediata**:
   - Benchmark detalhado de GPUs adicionais
   - Otimização de cache entre consultas
   - Implementação de métricas de qualidade

2. **Fase Intermediária**:
   - Suporte para backends adicionais (Qdrant, Weaviate)
   - Otimizações específicas por arquitetura GPU
   - Cache distribuído para múltiplas instâncias

3. **Fase Avançada**:
   - Auto-tuning de parâmetros por hardware
   - Balanceamento de carga entre backends
   - Integração com serviços cloud de embedding

### Critérios para Revisão

- **Performance**: Se latência média > 200ms
- **Compatibilidade**: Novos problemas com GPUs
- **Escala**: Volume > 10k documentos
- **Tecnologia**: Novos frameworks de busca

## Referências

- **Implementação**: `rag_infra/core_logic/rag_retriever.py`
- **Backend PyTorch**: `rag_infra/core_logic/pytorch_gpu_retriever.py`
- **Utilitários**: `rag_infra/core_logic/torch_utils.py`
- **Testes**: `rag_infra/diagnostico_rag.py`
- **Benchmarks**: `rag_infra/results_and_reports/`
- **Documentação FAISS**: https://github.com/facebookresearch/faiss
- **Documentação PyTorch**: https://pytorch.org/docs/

## Aprovação

- **Arquiteto**: @AgenteM_ArquitetoTI ✅
- **Data**: 19/06/2025
- **Revisão**: Aprovada com base em testes práticos
- **Próxima Revisão**: Dezembro 2025 ou quando volume > 1k documentos

---

**Nota**: Esta decisão foi validada através de implementação prática e testes extensivos, demonstrando eficácia em ambiente real de desenvolvimento.