# PROMPT PARA @AgenteM_DevFastAPI - INTEGRAÇÃO RAG PÓS-CORREÇÃO

**Data:** 20 de Junho de 2025  
**Prioridade:** ALTA - DEPENDENTE DA CORREÇÃO ARQUITETURAL  
**Dependência:** Aguardar correção do @AgenteM_ArquitetoTI  
**Contexto:** Implementação robusta de integração RAG no backend

---

## 🎯 OBJETIVO PRINCIPAL

**Implementar integração robusta e eficiente** entre o backend FastAPI e o sistema RAG corrigido, garantindo que todas as funcionalidades do Recoloca.ai tenham acesso confiável à "Documentação Viva" e base de conhecimento.

### 📋 Contexto de Dependência

**Aguardar Conclusão:**
- ✅ Correção do RAGRetriever pelo @AgenteM_ArquitetoTI
- ✅ Unificação das implementações MCP vs. Local
- ✅ Validação da inicialização bem-sucedida

**Então Proceder Com:**
- 🔧 Implementação de interfaces FastAPI para RAG
- 🔧 Integração com endpoints de consulta
- 🔧 Otimização de performance e cache

---

## 🚀 ESCOPO DE IMPLEMENTAÇÃO

### **1. Interface FastAPI para RAG**

**Endpoints Necessários:**
```python
# Consulta semântica básica
POST /api/v1/rag/query
{
    "query": "string",
    "top_k": 5,
    "min_score": 0.2,
    "category_filter": "optional"
}

# Busca por documento específico
GET /api/v1/rag/documents/{document_id}

# Status e health check do RAG
GET /api/v1/rag/status

# Reindexação (admin)
POST /api/v1/rag/reindex
```

### **2. Modelos Pydantic para Validação**

**Estruturas de Dados:**
```python
class RAGQueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)
    top_k: int = Field(default=5, ge=1, le=20)
    min_score: float = Field(default=0.2, ge=0.0, le=1.0)
    category_filter: Optional[str] = None

class RAGQueryResponse(BaseModel):
    results: List[RAGDocument]
    query_time_ms: float
    total_results: int
    
class RAGDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]
    score: float
    source_path: str
```

### **3. Serviço de Integração RAG**

**Classe de Serviço:**
```python
class RAGService:
    def __init__(self):
        # Inicialização com RAG corrigido
        pass
    
    async def query_documents(self, request: RAGQueryRequest) -> RAGQueryResponse:
        # Implementação de consulta assíncrona
        pass
    
    async def get_document_by_id(self, doc_id: str) -> Optional[RAGDocument]:
        # Recuperação de documento específico
        pass
    
    async def health_check(self) -> Dict[str, Any]:
        # Verificação de saúde do sistema
        pass
```

### **4. Middleware e Tratamento de Erros**

**Tratamento Robusto:**
- Timeout handling para consultas RAG
- Retry logic com backoff exponencial
- Fallback para cache local se RAG indisponível
- Logging estruturado para debugging
- Rate limiting para proteção

---

## 🔧 REQUISITOS TÉCNICOS ESPECÍFICOS

### **Performance e Otimização:**

1. **Cache Inteligente**
   - Redis para cache de consultas frequentes
   - TTL configurável por tipo de consulta
   - Invalidação automática em reindexação

2. **Consultas Assíncronas**
   - Uso de `async/await` para todas as operações RAG
   - Connection pooling para otimização
   - Timeout configurável (default: 10s)

3. **Métricas e Observabilidade**
   - Tempo de resposta por consulta
   - Taxa de cache hit/miss
   - Número de consultas por endpoint
   - Logs estruturados com correlation ID

### **Segurança e Validação:**

1. **Autenticação e Autorização**
   - Endpoints protegidos com JWT
   - Rate limiting por usuário
   - Validação de permissões para admin endpoints

2. **Sanitização de Input**
   - Validação rigorosa de queries
   - Prevenção de injection attacks
   - Limitação de tamanho de consulta

---

## 📚 BASE DE CONHECIMENTO OBRIGATÓRIA

**Consulte Prioritariamente:**
- `[[docs/02_Requisitos/01_ERS.md]]` - Requisitos funcionais RAG
- `[[docs/03_Arquitetura_e_Design/01_HLD.md]]` - Arquitetura backend
- `[[docs/03_Arquitetura_e_Design/00_API_Specs/]]` - Especificações de API
- `[[rag_infra/docs/README_RAG_OPERACIONAL.md]]` - Interface operacional

**Documentação Técnica:**
- `[[rag_infra/source_documents/04_Tech_Stack/]]` - FastAPI e Python
- Context7 MCP para documentação FastAPI, Pydantic, SQLAlchemy
- `[[docs/03_Arquitetura_e_Design/03_STYLE_GUIDE.md]]` - Padrões de código

---

## 🧪 TESTES E VALIDAÇÃO

### **Suíte de Testes Obrigatória:**

1. **Testes Unitários**
   ```python
   # test_rag_service.py
   async def test_rag_query_success()
   async def test_rag_query_timeout()
   async def test_rag_query_invalid_input()
   async def test_rag_cache_behavior()
   ```

2. **Testes de Integração**
   ```python
   # test_rag_endpoints.py
   async def test_rag_query_endpoint()
   async def test_rag_status_endpoint()
   async def test_rag_auth_required()
   ```

3. **Testes de Performance**
   - Benchmark de tempo de resposta
   - Teste de carga com múltiplas consultas
   - Validação de cache effectiveness

---

## ⚡ IMPLEMENTAÇÃO FASEADA

### **Fase 1: Core Integration (Imediata)**
- Implementar RAGService básico
- Endpoint de consulta principal
- Tratamento de erros essencial
- Testes unitários básicos

### **Fase 2: Otimização (Seguinte)**
- Sistema de cache Redis
- Métricas e observabilidade
- Rate limiting
- Testes de performance

### **Fase 3: Features Avançadas (Posterior)**
- Endpoints administrativos
- Analytics de uso
- Otimizações específicas
- Documentação OpenAPI completa

---

## 🎯 CRITÉRIOS DE SUCESSO

1. **Funcionalidade:**
   - ✅ Consultas RAG retornam resultados relevantes
   - ✅ Tempo de resposta < 2 segundos para consultas típicas
   - ✅ Taxa de erro < 1% em operação normal

2. **Performance:**
   - ✅ Cache hit rate > 60% para consultas repetidas
   - ✅ Suporte a 100+ consultas simultâneas
   - ✅ Graceful degradation em falhas

3. **Qualidade:**
   - ✅ Cobertura de testes > 80%
   - ✅ Documentação OpenAPI completa
   - ✅ Logs estruturados para debugging

---

## 📞 COORDENAÇÃO COM OUTROS AGENTES

**Colaboração Direta:**
- `@AgenteM_ArquitetoTI`: Validação da implementação com arquitetura
- `@AgenteM_Orquestrador`: Alinhamento estratégico e prioridades

**Comunicação de Progresso:**
- Maestro: Updates sobre implementação
- Equipe: Status de disponibilidade dos endpoints

---

## 🔄 PRÓXIMOS PASSOS

1. **Aguardar Sinal Verde:** Confirmação de correção do @AgenteM_ArquitetoTI
2. **Implementar Fase 1:** Core integration conforme especificado
3. **Validar Integração:** Testes com RAG corrigido
4. **Iterar e Otimizar:** Baseado em feedback e métricas

---

**Maestro, este prompt garante que o @AgenteM_DevFastAPI tenha uma roadmap clara para implementar a integração RAG de forma robusta e eficiente, complementando perfeitamente o trabalho arquitetural do @AgenteM_ArquitetoTI.**

--- FIM DO DOCUMENTO PROMPT_DEV_FASTAPI_RAG_INTEGRATION.md (v1.0) ---