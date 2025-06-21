#!/usr/bin/env python3
"""
Recoloca.AI RAG API Endpoints
RESTful endpoints for RAG system integration

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import logging
from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer

from ....core.config import settings
from ....core.logging import log_error
from ....services.rag_service import (
    RAGDocument,
    RAGHealthStatus,
    RAGQueryRequest,
    RAGQueryResponse,
    RAGService
)
from ...dependencies.auth import get_current_user, get_current_admin_user
from ...dependencies.rate_limit import rate_limit

router = APIRouter(prefix="/rag", tags=["RAG"])
security = HTTPBearer()
logger = logging.getLogger(__name__)


def get_rag_service(request: Request) -> RAGService:
    """Get RAG service from application state."""
    rag_service = getattr(request.app.state, 'rag_service', None)
    if not rag_service:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="RAG service is not available"
        )
    return rag_service


@router.post(
    "/query",
    response_model=RAGQueryResponse,
    summary="Query RAG System",
    description="Perform semantic search on the RAG knowledge base"
)
async def query_rag(
    request: RAGQueryRequest,
    http_request: Request,
    current_user: Dict[str, Any] = Depends(get_current_user),
    rag_service: RAGService = Depends(get_rag_service),
    _: None = Depends(rate_limit(requests_per_minute=30))
) -> RAGQueryResponse:
    """
    Query the RAG system for relevant documents.
    
    **Parameters:**
    - **query**: Search query string (1-1000 characters)
    - **top_k**: Number of results to return (1-20, default: 5)
    - **min_score**: Minimum similarity score (0.0-1.0, default: 0.2)
    - **category_filter**: Optional category filter
    - **use_cache**: Whether to use cached results (default: true)
    
    **Returns:**
    - List of relevant documents with similarity scores
    - Query execution time and metadata
    
    **Rate Limit:** 30 requests per minute per user
    """
    try:
        user_id = current_user.get("id")
        
        # Validate query length for user tier
        user_tier = current_user.get("tier", "free")
        if user_tier == "free" and len(request.query) > 500:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Query too long for free tier. Upgrade to premium for longer queries."
            )
        
        # Execute RAG query
        response = await rag_service.query_documents(request, user_id=user_id)
        
        # Filter results for free tier
        if user_tier == "free" and len(response.results) > 3:
            response.results = response.results[:3]
            response.total_results = len(response.results)
        
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        log_error(logger, e, {
            "operation": "rag_query_endpoint",
            "user_id": current_user.get("id"),
            "query_length": len(request.query)
        })
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during RAG query"
        )


@router.get(
    "/documents/{document_id}",
    response_model=Optional[RAGDocument],
    summary="Get Document by ID",
    description="Retrieve a specific document by its ID"
)
async def get_document(
    document_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user),
    rag_service: RAGService = Depends(get_rag_service),
    _: None = Depends(rate_limit(requests_per_minute=60))
) -> Optional[RAGDocument]:
    """
    Retrieve a specific document by its ID.
    
    **Parameters:**
    - **document_id**: Unique document identifier
    
    **Returns:**
    - Document content and metadata if found
    - null if document not found
    
    **Rate Limit:** 60 requests per minute per user
    """
    try:
        document = await rag_service.get_document_by_id(document_id)
        
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Document with ID '{document_id}' not found"
            )
        
        return document
        
    except HTTPException:
        raise
    except Exception as e:
        log_error(logger, e, {
            "operation": "get_document_endpoint",
            "user_id": current_user.get("id"),
            "document_id": document_id
        })
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while retrieving document"
        )


@router.get(
    "/status",
    response_model=RAGHealthStatus,
    summary="RAG System Status",
    description="Get health status and metrics of the RAG system"
)
async def get_rag_status(
    current_user: Dict[str, Any] = Depends(get_current_user),
    rag_service: RAGService = Depends(get_rag_service),
    _: None = Depends(rate_limit(requests_per_minute=10))
) -> RAGHealthStatus:
    """
    Get comprehensive health status of the RAG system.
    
    **Returns:**
    - System status (operational/degraded/down)
    - Initialization status
    - Document count and index status
    - Cache status
    - Response time metrics
    - Last error information
    
    **Rate Limit:** 10 requests per minute per user
    """
    try:
        health_status = await rag_service.health_check()
        return health_status
        
    except Exception as e:
        log_error(logger, e, {
            "operation": "rag_status_endpoint",
            "user_id": current_user.get("id")
        })
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while checking RAG status"
        )


@router.post(
    "/reindex",
    response_model=Dict[str, Any],
    summary="Reindex RAG System",
    description="Trigger reindexing of the RAG knowledge base (Admin only)"
)
async def reindex_rag(
    force_cpu: bool = False,
    clear_cache: bool = True,
    current_admin: Dict[str, Any] = Depends(get_current_admin_user),
    rag_service: RAGService = Depends(get_rag_service),
    _: None = Depends(rate_limit(requests_per_minute=2))
) -> Dict[str, Any]:
    """
    Trigger reindexing of the RAG knowledge base.
    
    **Admin Only Endpoint**
    
    **Parameters:**
    - **force_cpu**: Force CPU usage instead of GPU (default: false)
    - **clear_cache**: Clear existing cache before reindexing (default: true)
    
    **Returns:**
    - Reindexing status and completion information
    
    **Rate Limit:** 2 requests per minute per admin
    """
    try:
        logger.info(
            "RAG reindexing triggered by admin",
            extra={
                "admin_id": current_admin.get("id"),
                "force_cpu": force_cpu,
                "clear_cache": clear_cache
            }
        )
        
        result = await rag_service.reindex(
            force_cpu=force_cpu,
            clear_cache=clear_cache
        )
        
        return result
        
    except Exception as e:
        log_error(logger, e, {
            "operation": "rag_reindex_endpoint",
            "admin_id": current_admin.get("id"),
            "force_cpu": force_cpu,
            "clear_cache": clear_cache
        })
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during RAG reindexing"
        )


# Additional endpoints for advanced RAG operations

@router.get(
    "/categories",
    response_model=Dict[str, Any],
    summary="Get Available Categories",
    description="Get list of available document categories for filtering"
)
async def get_categories(
    current_user: Dict[str, Any] = Depends(get_current_user),
    _: None = Depends(rate_limit(requests_per_minute=20))
) -> Dict[str, Any]:
    """
    Get list of available document categories for filtering.
    
    **Returns:**
    - List of available categories
    - Category descriptions and document counts
    
    **Rate Limit:** 20 requests per minute per user
    """
    # TODO: Implement category listing from RAG system
    return {
        "categories": [
            {
                "name": "arquitetura",
                "description": "Architecture and design documents",
                "document_count": 0
            },
            {
                "name": "requisitos",
                "description": "Requirements and specifications",
                "document_count": 0
            },
            {
                "name": "guias",
                "description": "Guides and tutorials",
                "document_count": 0
            },
            {
                "name": "kanban",
                "description": "Project management and kanban",
                "document_count": 0
            },
            {
                "name": "agentes",
                "description": "AI agents documentation",
                "document_count": 0
            },
            {
                "name": "tech_stack",
                "description": "Technical stack documentation",
                "document_count": 0
            }
        ],
        "total_categories": 6,
        "last_updated": settings.get_current_timestamp()
    }


@router.get(
    "/metrics",
    response_model=Dict[str, Any],
    summary="RAG System Metrics",
    description="Get detailed metrics about RAG system usage (Admin only)"
)
async def get_rag_metrics(
    current_admin: Dict[str, Any] = Depends(get_current_admin_user),
    _: None = Depends(rate_limit(requests_per_minute=10))
) -> Dict[str, Any]:
    """
    Get detailed metrics about RAG system usage and performance.
    
    **Admin Only Endpoint**
    
    **Returns:**
    - Query statistics
    - Performance metrics
    - Cache hit rates
    - Error rates
    
    **Rate Limit:** 10 requests per minute per admin
    """
    # TODO: Implement actual metrics collection
    return {
        "query_stats": {
            "total_queries": 0,
            "queries_last_24h": 0,
            "average_response_time_ms": 0.0,
            "cache_hit_rate": 0.0
        },
        "performance": {
            "average_query_time_ms": 0.0,
            "p95_query_time_ms": 0.0,
            "p99_query_time_ms": 0.0
        },
        "errors": {
            "error_rate": 0.0,
            "errors_last_24h": 0,
            "common_errors": []
        },
        "system": {
            "uptime_seconds": 0,
            "memory_usage_mb": 0,
            "cpu_usage_percent": 0.0
        },
        "timestamp": settings.get_current_timestamp()
    }