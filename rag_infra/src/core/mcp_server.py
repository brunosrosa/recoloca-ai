#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP Server para Sistema RAG - Recoloca.ai

Este servidor MCP expõe as funcionalidades do sistema RAG para integração
com o Trae IDE e outros clientes MCP.

Autor: @AgenteM_DevFastAPI
Versão: 1.0
Data: Junho 2025
"""

import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

# Força a codificação UTF-8 para stdout e stderr
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Imports do MCP
try:
    from mcp.server.fastmcp import FastMCP
    from mcp.server.models import InitializationOptions
    from mcp.server.stdio import stdio_server
    from mcp.types import (
        Resource,
        Tool,
        TextContent,
        ImageContent,
        EmbeddedResource,
        LoggingLevel
    )
except ImportError as e:
    # Adiciona um log mais claro para o host MCP, que espera JSON
    error_msg = json.dumps({"jsonrpc": "2.0", "error": {"code": -32001, "message": f"Dependência MCP não encontrada: {e}. Execute 'pip install mcp-client'."}})
    print(error_msg, flush=True)
    sys.exit(1)

# Imports dos módulos RAG (agora locais)
project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root / "rag_infra" / "src"))

from core.rag_indexer import RAGIndexer
from core.rag_retriever import (
    RAGRetriever,
    initialize_retriever,
    get_retriever,
    search_documents
)
from core.constants import (
    MCP_SERVER_NAME,
    MCP_SERVER_VERSION,
    MCP_TOOLS,
    DEFAULT_TOP_K,
    MIN_SIMILARITY_SCORE,
    SOURCE_DOCUMENTS_DIR,
    FAISS_INDEX_DIR,
    LOGS_DIR,
    create_directories
)
from core.rag_optimization_config import RAGOptimizationConfig

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

# Criar servidor MCP
server = FastMCP(MCP_SERVER_NAME)

# Estado global do servidor
server_state = {
    "initialized": False,
    "indexer": None,
    "retriever": None,
    "last_error": None
}



async def _ensure_initialized(tool_name: str):
    """Garante que o sistema RAG esteja inicializado antes de executar uma ferramenta."""
    if not server_state["initialized"]:
        error_message = {
            "status": "error",
            "message": f"Falha ao executar '{tool_name}': O sistema RAG não foi inicializado com sucesso.",
            "details": server_state.get("last_error", "Nenhum detalhe de erro disponível.")
        }
        # Usar RuntimeError para sinalizar um erro interno grave para o host MCP
        raise RuntimeError(json.dumps(error_message, ensure_ascii=False, indent=2))

async def _initialize_rag_system():
    """
    Inicializa o sistema RAG com lógica de fallback (GPU -> CPU).
    """
    global server_state
    logger.info("Iniciando inicialização do sistema RAG...")

    try:
        create_directories()
        logger.info("Diretórios essenciais verificados/criados.")

        # Tenta inicializar o retriever
        retriever = initialize_retriever()

        if retriever and retriever.is_initialized and retriever.is_loaded:
            server_state["retriever"] = retriever
            server_state["initialized"] = True
            server_state["last_error"] = None
            backend_info = retriever.get_backend_info()
            logger.info(f"[OK] Sistema RAG inicializado com sucesso. Backend: {backend_info.get('backend', 'N/A')}, Dispositivo: {backend_info.get('device', 'N/A')}")
            return
        
        # Se a inicialização falhar
        error_msg = "Falha crítica ao inicializar o RAG Retriever."
        if retriever:
            backend_info = retriever.get_backend_info()
            error_msg += f" Detalhes: Backend: {backend_info.get('backend')}, Device: {backend_info.get('device')}, Initialized: {retriever.is_initialized}, Loaded: {retriever.is_loaded}"
        
        server_state["initialized"] = False
        server_state["last_error"] = error_msg
        logger.error(error_msg)

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        error_msg = f"Erro crítico e inesperado durante a inicialização do sistema RAG: {e}"
        server_state["initialized"] = False
        server_state["last_error"] = f"{error_msg}\n{error_details}"
        logger.critical(error_msg, exc_info=True)

@server.tool("rag_query")
async def rag_query(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    min_score: float = MIN_SIMILARITY_SCORE,
    category_filter: Optional[str] = None
) -> Sequence[TextContent]:
    """
    Realiza consulta semântica no sistema RAG.

    Busca documentos relevantes baseado na similaridade semântica da consulta.

    Args:
        query: Consulta de busca semântica.
        top_k: Número de resultados a retornar (padrão: 5, máximo: 20).
        min_score: Score mínimo de similaridade (0.0 a 1.0).
        category_filter: Filtro por categoria de documento (opcional).
    """
    
    await _ensure_initialized("rag_query")

    if not query.strip():
        return [TextContent(type="text", text="Erro: Consulta vazia")]

    try:
        retriever = get_retriever()
        results = retriever.search(query, top_k, min_score, category_filter)

        if not results:
            return [TextContent(type="text", text=f"Nenhum resultado encontrado para: {query}")]

        response_data = {
            "query": query,
            "total_results": len(results),
            "parameters": {"top_k": top_k, "min_score": min_score, "category_filter": category_filter},
            "results": [result.to_dict() for result in results]
        }
        return [TextContent(type="text", text=json.dumps(response_data, ensure_ascii=False, indent=2))]

    except Exception as e:
        logger.error(f"Erro na consulta RAG: {e}", exc_info=True)
        return [TextContent(type="text", text=f"Erro na consulta: {e}")]

@server.tool("rag_search_by_document")
async def rag_search_by_document(document_pattern: str, top_k: int = DEFAULT_TOP_K) -> Sequence[TextContent]:
    """
    Busca documentos por padrão no nome ou caminho do arquivo.

    Args:
        document_pattern: Padrão para buscar no nome/caminho do documento.
        top_k: Número máximo de resultados.
    """
    
    await _ensure_initialized("rag_search_by_document")

    if not document_pattern.strip():
        return [TextContent(type="text", text="Erro: Padrão de documento vazio")]

    try:
        retriever = get_retriever()
        results = retriever.search_by_document(document_pattern, top_k)

        response_data = {
            "document_pattern": document_pattern,
            "total_results": len(results),
            "results": [result.to_dict() for result in results]
        }
        return [TextContent(type="text", text=json.dumps(response_data, ensure_ascii=False, indent=2))]

    except Exception as e:
        logger.error(f"Erro na busca por documento: {e}", exc_info=True)
        return [TextContent(type="text", text=f"Erro na busca: {e}")]

@server.tool("rag_get_document_list")
async def rag_get_document_list(category: Optional[str] = None) -> Sequence[TextContent]:
    """
    Retorna lista de todos os documentos indexados no sistema RAG.

    Args:
        category: Filtro por categoria (opcional).
    """
    
    await _ensure_initialized("rag_get_document_list")

    try:
        retriever = get_retriever()
        documents = retriever.get_document_list(category)

        response_data = {
            "category_filter": category,
            "total_documents": len(documents),
            "documents": documents
        }
        return [TextContent(type="text", text=json.dumps(response_data, ensure_ascii=False, indent=2))]

    except Exception as e:
        logger.error(f"Erro ao listar documentos: {e}", exc_info=True)
        return [TextContent(type="text", text=f"Erro na listagem: {e}")]

@server.tool("rag_reindex")
async def rag_reindex(force_cpu: bool = False, clear_cache: bool = True) -> Sequence[TextContent]:
    """
    Força a reindexação de todos os documentos. Use apenas quando necessário.

    Args:
        force_cpu: Força o uso de CPU em vez de GPU.
        clear_cache: Limpa o cache antes da reindexação.
    """
    
    await _ensure_initialized("rag_reindex")

    try:
        logger.info(f"Iniciando processo de reindexação com force_cpu={force_cpu}...")

        async def reindex_and_restart():
            try:
                indexer = RAGIndexer(force_cpu=force_cpu)
                # O método reindex_all já é síncrono, então o to_thread é bom
                await asyncio.to_thread(indexer.reindex_all, clear_cache=clear_cache)
                logger.info("Reindexação em background concluída. Disparando reinicialização do sistema RAG.")
                await _initialize_rag_system()
            except Exception as e:
                logger.error(f"Erro no processo de reindexação em background: {e}", exc_info=True)

        asyncio.create_task(reindex_and_restart())

        response_data = {
            "status": "pending",
            "message": "Processo de reindexação iniciado em background. O sistema será reinicializado automaticamente. Verifique o status em alguns instantes.",
            "parameters": {"force_cpu": force_cpu, "clear_cache": clear_cache}
        }
        return [TextContent(type="text", text=json.dumps(response_data, ensure_ascii=False, indent=2))]

    except Exception as e:
        logger.critical(f"Erro ao disparar a reindexação: {e}", exc_info=True)
        return [TextContent(type="text", text=json.dumps({"status": "error", "message": f"Erro ao disparar a reindexação: {e}"}, ensure_ascii=False, indent=2))]

@server.tool("rag_get_status")
async def rag_get_status() -> Sequence[TextContent]:
    """
    Retorna informações sobre o status do sistema RAG.
    """
    try:
        # Aguardar um pouco para dar tempo à inicialização assíncrona, se estiver em progresso
        await asyncio.sleep(1)

        # Status básico
        status_data = {
            "server_name": MCP_SERVER_NAME,
            "server_version": MCP_SERVER_VERSION,
            "initialized": server_state["initialized"],
            "last_error": server_state["last_error"]
        }
        
        # Informações do retriever se disponível
        retriever = get_retriever()
        if retriever:
            try:
                index_info = await asyncio.to_thread(retriever.get_index_info)
                backend_info = await asyncio.to_thread(retriever.get_backend_info)
                status_data["retriever_info"] = {
                    "index": index_info,
                    "backend": backend_info
                }
            except Exception as e:
                logger.warning(f"Não foi possível obter informações do retriever: {e}")
                status_data["retriever_info"] = {"error": f"Não foi possível obter informações do retriever: {e}"}
        else:
            status_data["retriever_info"] = "Retriever não instanciado."

        # Verificar diretórios
        status_data["directories"] = {
            "source_documents": {
                "path": str(SOURCE_DOCUMENTS_DIR),
                "exists": SOURCE_DOCUMENTS_DIR.exists()
            },
            "faiss_index": {
                "path": str(FAISS_INDEX_DIR),
                "exists": FAISS_INDEX_DIR.exists()
            }
        }
        
        return [TextContent(
            type="text",
            text=json.dumps(status_data, ensure_ascii=False, indent=2)
        )]
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        logger.error(f"Erro ao obter status: {e}\n{error_details}")
        return [TextContent(
            type="text",
            text=json.dumps({"status": "error", "message": f"Erro ao obter status: {e}"}, ensure_ascii=False, indent=2)
        )]

async def _initialize_rag_system_async():
    """Inicializa o sistema RAG de forma assíncrona."""
    await _initialize_rag_system()
    logger.info("MCP Server iniciado e aguardando comandos...")

if __name__ == "__main__":
    # Inicializar o sistema RAG antes de executar o servidor
    asyncio.run(_initialize_rag_system_async())
    # Executar o servidor MCP
    server.run()