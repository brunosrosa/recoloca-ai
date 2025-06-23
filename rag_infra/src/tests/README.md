# Testes - Sistema RAG

Esta pasta contém todos os testes do sistema RAG para validação de funcionalidades e performance.

## Testes Disponíveis

### `test_rag_validation.py`
**Descrição:** Validação completa do sistema RAG incluindo performance, qualidade contextual e integração MCP.

**Uso:**
```bash
python tests/test_rag_validation.py
```

**Métricas Validadas:**
- ✅ Performance de conectividade
- ✅ Qualidade contextual
- ✅ Integração MCP
- ✅ Funcionalidades básicas

### `test_rag_system.py`
**Descrição:** Testes básicos do sistema RAG.

**Uso:**
```bash
python tests/test_rag_system.py
```

### `test_embedding.py`
**Descrição:** Testes do modelo de embedding.

**Uso:**
```bash
python tests/test_embedding.py
```

### `test_faiss_gpu.py`
**Descrição:** Testes específicos do FAISS com GPU.

**Uso:**
```bash
python tests/test_faiss_gpu.py
```

### `test_retriever.py`
**Descrição:** Testes do sistema de recuperação de documentos.

**Uso:**
```bash
python tests/test_retriever.py
```

## Como Executar

Todos os testes devem ser executados a partir do diretório raiz do `rag_infra`:

```bash
cd rag_infra
python tests/nome_do_teste.py
```

## Resultados

Os resultados dos testes são salvos em:
- `utils/rag_validation_results.json` - Resultados da validação completa
- `logs/` - Logs detalhados dos testes

## Desenvolvimento

Para adicionar novos testes:

1. Crie o arquivo na pasta `tests/`
2. Siga o padrão de nomenclatura `test_*.py`
3. Adicione documentação neste README
4. Inclua validações adequadas
5. Salve resultados em formato JSON quando apropriado