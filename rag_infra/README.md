# 🧠 Sistema RAG - Recoloca.ai

## 📋 Visão Geral

Sistema de Retrieval-Augmented Generation (RAG) completo para o projeto Recoloca.ai, implementando busca semântica inteligente em toda a documentação do projeto através de um MCP Server integrado ao Trae IDE.

### 🎯 Funcionalidades Principais

- **Indexação Automática**: Processa e indexa documentos MD, TXT, PDF, DOCX e HTML
- **Busca Semântica**: Utiliza modelo BGE-M3 para embeddings de alta qualidade
- **MCP Server**: Integração nativa com Trae IDE via protocolo MCP
- **Cache Inteligente**: Sistema de cache para otimização de performance
- **Categorização**: Organização automática por categorias (arquitetura, requisitos, etc.)
- **Monitoramento**: Logs estruturados e métricas de performance

## 🏗️ Arquitetura

```
rag_infra/
├── core_logic/              # Lógica principal do RAG
│   ├── constants.py         # Constantes e configurações
│   ├── embedding_model.py   # Gerenciamento do modelo BGE-M3
│   ├── rag_indexer.py      # Indexação de documentos
│   └── rag_retriever.py    # Sistema de recuperação
├── data_index/             # Índices FAISS e metadados
├── source_documents/       # Documentos para indexação
├── logs/                   # Logs do sistema
├── mcp_server.py          # Servidor MCP
├── setup_rag.py           # Script de configuração
├── test_rag_system.py     # Testes do sistema
├── trae_mcp_config.json   # Configuração para Trae IDE
└── environment.yml        # Dependências Conda
```

## 🚀 Instalação e Configuração

### 1. Pré-requisitos

- **Python 3.8+**
- **CUDA 11.8+** (opcional, para GPU)
- **16GB+ RAM** (recomendado)
- **5GB+ espaço livre** (para modelos e índices)

### 2. Configuração do Ambiente

```bash
# Criar ambiente Conda
conda env create -f rag_infra/environment.yml
conda activate rag_env

# Ou instalar via pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install sentence-transformers langchain faiss-cpu pymupdf python-dotenv unstructured
```

### 3. Setup Automático

```bash
# Setup completo (recomendado)
python rag_infra/setup_rag.py

# Opções avançadas
python rag_infra/setup_rag.py --force-cpu      # Forçar CPU
python rag_infra/setup_rag.py --skip-indexing  # Pular indexação
python rag_infra/setup_rag.py --verbose        # Modo debug
```

### 4. Verificação da Instalação

```bash
# Testar sistema completo
python rag_infra/test_rag_system.py

# Testar componentes individuais
python rag_infra/core_logic/rag_indexer.py
python rag_infra/core_logic/rag_retriever.py
```

## 🔧 Uso do Sistema

### Indexação de Documentos

```python
from rag_infra.core_logic.rag_indexer import RAGIndexer

# Indexar todos os documentos
indexer = RAGIndexer()
success = indexer.index_documents()

# Forçar reindexação
indexer.index_documents(force_reindex=True)
```

### Consultas RAG

```python
from rag_infra.core_logic.rag_retriever import RAGRetriever

# Inicializar retriever
retriever = RAGRetriever()

# Busca semântica
results = retriever.search(
    query="como implementar autenticação FastAPI",
    top_k=5,
    min_score=0.3
)

# Busca por documento específico
docs = retriever.search_by_document_pattern("arquitetura")

# Listar documentos indexados
all_docs = retriever.get_document_list()
```

### MCP Server

```bash
# Iniciar servidor MCP
python rag_infra/mcp_server.py

# Servidor estará disponível via stdio para integração com Trae
```

## 🎮 Integração com Trae IDE

### 1. Configuração do MCP Server

Adicione ao arquivo de configuração do Trae:

```json
{
  "mcpServers": {
    "recoloca-rag": {
      "command": "python",
      "args": ["rag_infra/mcp_server.py"],
      "cwd": ".",
      "env": {
        "PYTHONPATH": "rag_infra:rag_infra/core_logic"
      }
    }
  }
}
```

### 2. Ferramentas Disponíveis

| Ferramenta | Descrição | Uso |
|------------|-----------|-----|
| `rag_query` | Consulta semântica | Buscar informações por conceito |
| `rag_search_by_document` | Busca por documento | Encontrar documentos específicos |
| `rag_get_document_list` | Listar documentos | Ver todos os documentos indexados |
| `rag_reindex` | Reindexar | Atualizar índice após mudanças |
| `rag_get_status` | Status do sistema | Verificar saúde do RAG |

### 3. Configuração por Agente

Cada agente tem configurações otimizadas:

- **@AgenteM_DevFastAPI**: Foco em documentação técnica
- **@AgenteM_Orquestrador**: Prioriza documentos de gestão
- **@AgenteM_ArquitetoTI**: Enfatiza arquitetura e design
- **@AgenteM_UXDesigner**: Concentra em requisitos e UX

## 📊 Documentos Indexados

O sistema indexa automaticamente:

### 📁 Categorias de Documentos

| Categoria | Padrões | Prioridade |
|-----------|---------|------------|
| **Arquitetura** | `**/03_Arquitetura/**`, `**/*arquitetura*` | Alta |
| **Requisitos** | `**/02_Requisitos/**`, `**/ERS.md` | Alta |
| **Guias** | `**/01_Guias_Centrais/**`, `**/README.md` | Média |
| **Kanban** | `**/00_Gerenciamento_Projeto/**`, `**/KANBAN/**` | Média |
| **Agentes** | `**/04_Agentes_IA/**`, `**/*agente*` | Média |
| **Tech Stack** | `**/Tech_Stack/**`, `**/*fastapi*` | Alta |

### 📄 Formatos Suportados

- **Markdown** (`.md`) - Documentação principal
- **Texto** (`.txt`) - Notas e especificações
- **PDF** (`.pdf`) - Documentos formais
- **Word** (`.docx`) - Documentos colaborativos
- **HTML** (`.html`) - Documentação web

## 🔄 Manutenção e Atualizações

### Indexação Automática

O sistema suporta:

- **Reindexação Diária**: Automática às 02:00
- **Watch de Arquivos**: Detecta mudanças em tempo real
- **Debounce**: Evita reindexações desnecessárias (5s)

### Comandos de Manutenção

```bash
# Reindexar manualmente
python rag_infra/core_logic/rag_indexer.py --force-reindex

# Limpar cache
python -c "from rag_infra.core_logic.rag_retriever import clear_cache; clear_cache()"

# Verificar status
python -c "from rag_infra.core_logic.rag_retriever import get_global_retriever; print(get_global_retriever().get_index_info())"

# Backup do índice
cp -r rag_infra/data_index rag_infra/data_index_backup_$(date +%Y%m%d)
```

### Rotinas Automáticas

Para configurar rotinas automáticas:

```bash
# Crontab (Linux/Mac)
0 2 * * * cd /path/to/project && python rag_infra/core_logic/rag_indexer.py

# Task Scheduler (Windows)
schtasks /create /tn "RAG Reindex" /tr "python rag_infra/core_logic/rag_indexer.py" /sc daily /st 02:00
```

## 📈 Monitoramento e Métricas

### Logs Estruturados

```bash
# Logs principais
tail -f rag_infra/logs/rag_indexer.log    # Indexação
tail -f rag_infra/logs/rag_retriever.log  # Consultas
tail -f rag_infra/logs/mcp_server.log     # Servidor MCP
```

### Métricas de Performance

- **Tempo de Indexação**: < 5min para 1000 documentos
- **Tempo de Consulta**: < 500ms para busca semântica
- **Precisão**: > 85% para consultas relevantes
- **Cobertura**: 100% dos documentos do projeto

### Health Checks

```python
# Via MCP
rag_get_status()

# Via código
from rag_infra.core_logic.rag_retriever import get_global_retriever
retriever = get_global_retriever()
status = retriever.get_index_info()
print(f"Documentos indexados: {status['total_documents']}")
```

## 🛠️ Troubleshooting

### Problemas Comuns

| Problema | Causa | Solução |
|----------|-------|----------|
| GPU não detectada | Drivers CUDA | Instalar CUDA 11.8+ ou usar `--force-cpu` |
| Índice não encontrado | Primeira execução | Executar `python setup_rag.py` |
| Modelo não carrega | Sem internet/espaço | Verificar conexão e espaço em disco |
| Consultas lentas | CPU/RAM limitados | Usar GPU ou aumentar RAM |
| Documentos não indexados | Formato não suportado | Verificar extensões suportadas |

### Comandos de Diagnóstico

```bash
# Verificar ambiente
python rag_infra/setup_rag.py --verbose

# Testar GPU
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# Verificar modelo
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('BAAI/bge-m3')"

# Testar FAISS
python -c "import faiss; print(f'FAISS: {faiss.__version__}')"
```

## 🔒 Segurança e Privacidade

- **Dados Locais**: Todos os dados permanecem no ambiente local
- **Sem Telemetria**: Nenhum dado é enviado para serviços externos
- **Controle de Acesso**: Integração com sistema de permissões do Trae
- **Backup Seguro**: Índices podem ser criptografados para backup

## 🚀 Roadmap

### Fase Atual (v1.0)
- ✅ RAG Core funcional
- ✅ MCP Server integrado
- ✅ Indexação automática
- ✅ Categorização de documentos

### Próximas Fases
- 🔄 **v1.1**: Busca híbrida (semântica + keyword)
- 🔄 **v1.2**: Suporte a imagens e diagramas
- 🔄 **v1.3**: RAG multimodal completo
- 🔄 **v2.0**: Integração com agentes de IA

## 📞 Suporte

Para problemas ou dúvidas:

1. **Verificar logs**: `rag_infra/logs/`
2. **Executar diagnósticos**: `python setup_rag.py --verbose`
3. **Consultar troubleshooting**: Seção acima
4. **Reportar issues**: Via sistema de gestão do projeto

---

**Sistema RAG - Recoloca.ai** | Desenvolvido por @AgenteM_DevFastAPI

*Última atualização: $(date +"%Y-%m-%d")*