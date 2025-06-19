# Scripts Utilitários - Sistema RAG

Esta pasta contém scripts utilitários para manutenção e diagnóstico do sistema RAG.

## Scripts Disponíveis

### `check_backend.py`
**Descrição:** Verifica qual backend RAG está sendo usado (PyTorch ou FAISS) e detecta a GPU disponível.

**Uso:**
```bash
python scripts/check_backend.py
```

**Saída:**
- Backend em uso (PyTorch/FAISS)
- GPU detectada
- Configurações do retriever

### `create_dirs.py`
**Descrição:** Script para criar diretórios necessários para o sistema RAG.

**Uso:**
```bash
python scripts/create_dirs.py
```

### `debug_paths.py`
**Descrição:** Script de diagnóstico para verificar caminhos e configurações do sistema.

**Uso:**
```bash
python scripts/debug_paths.py
```

## Como Usar

Todos os scripts devem ser executados a partir do diretório raiz do `rag_infra`:

```bash
cd rag_infra
python scripts/nome_do_script.py
```

## Desenvolvimento

Para adicionar novos scripts utilitários:

1. Crie o arquivo na pasta `scripts/`
2. Adicione documentação neste README
3. Certifique-se de que o script funciona a partir do diretório raiz
4. Inclua tratamento de erros adequado