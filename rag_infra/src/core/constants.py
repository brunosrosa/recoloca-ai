# -*- coding: utf-8 -*-
"""
Constantes para o Sistema RAG do Recoloca.ai

Este módulo define todas as constantes utilizadas pelo sistema RAG,
incluindo caminhos, configurações de modelos e parâmetros de indexação.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import os
from pathlib import Path

# =============================================================================
# CAMINHOS E DIRETÓRIOS
# =============================================================================

# Diretório raiz do projeto RAG
RAG_ROOT_DIR = Path(__file__).resolve().parents[2]  # rag_infra/

# Diretórios de dados
SOURCE_DOCUMENTS_DIR = RAG_ROOT_DIR / "knowledge_base_for_rag" # Caminho corrigido
DATA_INDEX_DIR = RAG_ROOT_DIR / "data" / "indexes" / "data_index"
FAISS_INDEX_DIR = DATA_INDEX_DIR / "faiss_index_bge_m3"
PYTORCH_INDEX_DIR = DATA_INDEX_DIR / "pytorch_index_bge_m3"
LOGS_DIR = RAG_ROOT_DIR / "logs"
CACHE_DIR = RAG_ROOT_DIR / "cache"
METRICS_DIR = RAG_ROOT_DIR / "metrics"

# Subdiretórios de documentos (estrutura reorganizada)
DOCUMENTACAO_CENTRAL_DIR = SOURCE_DOCUMENTS_DIR / "00_Documentacao_Central"
GESTAO_PROCESSOS_DIR = SOURCE_DOCUMENTS_DIR / "01_Gestao_e_Processos"
REQUISITOS_ESPECIFICACOES_DIR = SOURCE_DOCUMENTS_DIR / "02_Requisitos_e_Especificacoes"
ARQUITETURA_DESIGN_DIR = SOURCE_DOCUMENTS_DIR / "03_Arquitetura_e_Design"
PADROES_GUIAS_DIR = SOURCE_DOCUMENTS_DIR / "04_Padroes_e_Guias"
TECH_STACK_DIR = SOURCE_DOCUMENTS_DIR / "05_Tech_Stack"
AGENTES_IA_DIR = SOURCE_DOCUMENTS_DIR / "06_Agentes_e_IA"
UX_DESIGN_DIR = SOURCE_DOCUMENTS_DIR / "07_UX_e_Design"
CONHECIMENTO_ESPECIALIZADO_DIR = SOURCE_DOCUMENTS_DIR / "08_Conhecimento_Especializado"

# =============================================================================
# CONFIGURAÇÕES DO MODELO DE EMBEDDING
# =============================================================================

# Modelo de embedding principal
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"

# Configurações do modelo
EMBEDDING_MODEL_CONFIG = {
    "model_name": EMBEDDING_MODEL_NAME,
    "model_kwargs": {
        "device": "cuda",  # Usar GPU se disponível
        "trust_remote_code": True
    },
    "encode_kwargs": {
        "normalize_embeddings": True,
        "batch_size": 32
    }
}

# =============================================================================
# CONFIGURAÇÕES DE CHUNKING
# =============================================================================

# Configurações para divisão de documentos
CHUNK_SIZE = 1000  # Tamanho do chunk em caracteres
CHUNK_OVERLAP = 200  # Sobreposição entre chunks
MIN_CHUNK_SIZE = 100  # Tamanho mínimo dos chunks em caracteres
SEPARATORS = ["\n\n", "\n", ".", "!", "?", ",", " ", ""]  # Separadores para chunking

# =============================================================================
# CONFIGURAÇÕES DO FAISS
# =============================================================================

# Configurações do índice FAISS
FAISS_INDEX_TYPE = "IndexFlatIP"  # Inner Product para embeddings normalizados
FAISS_METRIC_TYPE = "METRIC_INNER_PRODUCT"
FAISS_NPROBE = 32  # Número de clusters a serem pesquisados
FAISS_NLIST = 100  # Número de clusters para IVF
FAISS_FACTORY_STRING = "Flat"  # String de configuração do índice
FAISS_TRAIN_SIZE = 10000  # Tamanho mínimo para treinamento
FAISS_EF_SEARCH = 64  # Parâmetro de busca para HNSW

# Nomes dos arquivos do índice
FAISS_INDEX_FILE = "faiss_index.bin"
FAISS_METADATA_FILE = "metadata.json"
FAISS_DOCUMENTS_FILE = "documents.json"
FAISS_EMBEDDINGS_FILE = "embeddings.npy"

# Nomes dos arquivos PyTorch
PYTORCH_INDEX_FILE = "pytorch_index.pt"
PYTORCH_EMBEDDINGS_FILE = "embeddings.pt"
PYTORCH_METADATA_FILE = "metadata.json"
PYTORCH_DOCUMENTS_FILE = "documents.json"
PYTORCH_MAPPING_FILE = "mapping.json"

# Arquivo de mapeamento FAISS
FAISS_MAPPING_FILE = "mapping.json"

# =============================================================================
# CONFIGURAÇÕES DE BUSCA
# =============================================================================

# Parâmetros padrão para busca
DEFAULT_TOP_K = 5  # Número padrão de resultados retornados
MAX_TOP_K = 20     # Número máximo de resultados permitidos
MIN_SIMILARITY_SCORE = 0.2  # Threshold ajustado para permitir mais resultados  # Score mínimo de similaridade

# =============================================================================
# CONFIGURAÇÕES DE LOGGING
# =============================================================================

# Configurações de log
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Arquivos de log
INDEXER_LOG_FILE = LOGS_DIR / "rag_indexer.log"
RETRIEVER_LOG_FILE = LOGS_DIR / "rag_retriever.log"
MCP_SERVER_LOG_FILE = LOGS_DIR / "mcp_server.log"
PERFORMANCE_LOG_FILE = LOGS_DIR / "performance.log"

# =============================================================================
# CONFIGURAÇÕES DE PERFORMANCE
# =============================================================================

# Timeouts e limites
QUERY_TIMEOUT = 30  # Timeout para consultas em segundos
MAX_BATCH_SIZE = 100  # Tamanho máximo do batch para processamento
CACHE_SIZE = 1000  # Tamanho do cache de consultas

# Configurações específicas do PyTorch
PYTORCH_BATCH_SIZE = 32  # Tamanho do batch para PyTorch
PYTORCH_MAX_MEMORY_GB = 4  # Memória máxima em GB para PyTorch

# Configurações de funcionalidades
ENABLE_METRICS = True  # Habilitar coleta de métricas
ENABLE_CACHING = True  # Habilitar cache de resultados
ENABLE_PYTORCH_OPTIMIZATION = True  # Habilitar otimizações PyTorch

# =============================================================================
# EXTENSÕES DE ARQUIVO SUPORTADAS
# =============================================================================

SUPPORTED_EXTENSIONS = [
    '.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml', '.yaml', '.yml',
    '.csv', '.tsv', '.log', '.ini', '.cfg', '.conf', '.sh', '.bat', '.ps1',
    '.sql', '.r', '.scala', '.go', '.rust', '.cpp', '.c', '.h', '.hpp',
    '.java', '.kt', '.swift', '.php', '.rb', '.pl', '.lua', '.dart'
]

# Configurações de encoding
ENCODING_FALLBACKS = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']

# Mensagens de status
STATUS_MESSAGES = {
    'indexing': 'Indexando documentos...',
    'searching': 'Buscando documentos...',
    'complete': 'Operação concluída',
    'error': 'Erro na operação'
}

# Template de resultado
RESULT_TEMPLATE = {
    'query': '',
    'results': [],
    'total_results': 0,
    'processing_time': 0.0,
    'status': 'success'
}

# =============================================================================
# METADADOS PADRÃO
# =============================================================================

# Campos de metadados para documentos
METADATA_FIELDS = [
    "source",      # Caminho do arquivo fonte
    "title",       # Título do documento
    "section",     # Seção do documento
    "chunk_id",    # ID único do chunk
    "timestamp",   # Timestamp de indexação
    "file_type",   # Tipo do arquivo
    "file_size",   # Tamanho do arquivo
    "category",    # Categoria do documento (PM, UX, Tech, etc.)
    "language",    # Idioma do documento
    "version"      # Versão do documento
]

# Categorias de documentos
DOCUMENT_CATEGORIES = {
    "PM_Knowledge": "product_management",
    "UX_Knowledge": "user_experience",
    "Tech_Stack": "technical",
    "API_Specs": "api_specification",
    "ERS": "requirements",
    "HLD": "architecture",
    "STYLE_GUIDE": "design_system",
    "GUIA_AVANCADO": "methodology"
}

# =============================================================================
# CONFIGURAÇÕES DO MCP SERVER
# =============================================================================

# Configurações do servidor MCP
MCP_SERVER_NAME = "rag_recoloca"
MCP_SERVER_VERSION = "1.0.0"
MCP_SERVER_DESCRIPTION = "RAG Server para Recoloca.ai - Acesso à base de conhecimento"

# Tools disponíveis via MCP
MCP_TOOLS = [
    "rag_query",
    "rag_search_by_document", 
    "rag_get_document_list",
    "rag_reindex"
]

# =============================================================================
# CONFIGURAÇÕES DE AMBIENTE
# =============================================================================

# Variáveis de ambiente
CUDA_VISIBLE_DEVICES = os.getenv("CUDA_VISIBLE_DEVICES", "0")
HUGGINGFACE_HUB_CACHE = os.getenv("HUGGINGFACE_HUB_CACHE", str(RAG_ROOT_DIR / ".cache"))

# Verificação de GPU
USE_GPU = True  # Será verificado dinamicamente no embedding_model.py

# =============================================================================
# MENSAGENS E TEMPLATES
# =============================================================================

# Mensagens de status
STATUS_MESSAGES = {
    "indexing_start": "Iniciando indexação da base de conhecimento...",
    "indexing_complete": "Indexação concluída com sucesso!",
    "indexing_error": "Erro durante a indexação: {error}",
    "query_start": "Processando consulta: {query}",
    "query_complete": "Consulta processada. {count} resultados encontrados.",
    "query_error": "Erro durante a consulta: {error}",
    "gpu_available": "GPU detectada e disponível para FAISS",
    "gpu_unavailable": "GPU não disponível, usando CPU",
    "model_loading": "Carregando modelo de embedding: {model}",
    "model_loaded": "Modelo carregado com sucesso",
    "index_loading_start": "Carregando índice...",
    "loading_faiss_index": "   - Carregando índice FAISS...",
    "loading_pytorch_index": "   - Carregando índice PyTorch...",
    "index_loaded_success": "Índice carregado com sucesso.",
    "index_loaded_error": "Erro ao carregar índice: {error}"
}

# Template para formatação de resultados
RESULT_TEMPLATE = """
**Documento:** {source}
**Seção:** {section}
**Relevância:** {score:.3f}
**Conteúdo:**
{content}
---
"""

# =============================================================================
# VALIDAÇÕES E VERIFICAÇÕES
# =============================================================================

def create_directories():
    """Cria os diretórios necessários se não existirem."""
    directories = [
        DATA_INDEX_DIR,
        FAISS_INDEX_DIR,
        PYTORCH_INDEX_DIR,
        LOGS_DIR,
        CACHE_DIR,
        METRICS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

def validate_environment():
    """Valida se o ambiente está configurado corretamente."""
    errors = []
    
    # Verificar se o diretório de documentos existe
    if not SOURCE_DOCUMENTS_DIR.exists():
        errors.append(f"Diretório de documentos não encontrado: {SOURCE_DOCUMENTS_DIR}")
    
    # Verificar se há documentos para indexar
    if SOURCE_DOCUMENTS_DIR.exists():
        md_files = list(SOURCE_DOCUMENTS_DIR.rglob("*.md"))
        if not md_files:
            errors.append("Nenhum arquivo Markdown encontrado para indexação")
    
    return errors

if __name__ == "__main__":
    # Criar diretórios necessários
    create_directories()
    
    # Validar ambiente
    errors = validate_environment()
    if errors:
        print("[ERROR] Erros de configuração encontrados:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("[OK] Ambiente configurado corretamente!")