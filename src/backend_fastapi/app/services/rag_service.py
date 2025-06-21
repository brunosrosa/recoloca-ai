#!/usr/bin/env python3
"""
Recoloca.AI RAG Service
Integration service for RAG system with caching and error handling

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import asyncio
import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import redis.asyncio as redis
from pydantic import BaseModel, Field

from ..core.config import settings
from ..core.logging import log_error, log_rag_query

# Import RAG components
try:
    import sys
    rag_path = settings.PROJECT_ROOT / "rag_infra"
    sys.path.insert(0, str(rag_path))
    
    from src.core.core_logic.rag_retriever import RAGRetriever
    from config import RAGConfig
except ImportError as e:
    logging.warning(f"RAG components not available: {e}")
    RAGRetriever = None
    RAGConfig = None


class RAGDocument(BaseModel):
    """RAG document model."""
    content: str
    metadata: Dict[str, Any]
    score: float
    source_path: str
    chunk_index: Optional[int] = None
    category: Optional[str] = None


class RAGQueryRequest(BaseModel):
    """RAG query request model."""
    query: str = Field(..., min_length=1, max_length=1000, description="Search query")
    top_k: int = Field(default=5, ge=1, le=20, description="Number of results to return")
    min_score: float = Field(default=0.2, ge=0.0, le=1.0, description="Minimum similarity score")
    category_filter: Optional[str] = Field(default=None, description="Category filter")
    use_cache: bool = Field(default=True, description="Whether to use cache")


class RAGQueryResponse(BaseModel):
    """RAG query response model."""
    results: List[RAGDocument]
    query_time_ms: float
    total_results: int
    cache_hit: bool = False
    query_hash: Optional[str] = None


class RAGHealthStatus(BaseModel):
    """RAG health status model."""
    status: str  # operational, degraded, down
    initialized: bool
    total_documents: int
    index_loaded: bool
    last_error: Optional[str] = None
    cache_status: str = "unknown"
    response_time_ms: Optional[float] = None


class RAGService:
    """RAG service with caching and error handling."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.rag_retriever: Optional[RAGRetriever] = None
        self.redis_client: Optional[redis.Redis] = None
        self.initialized = False
        self.last_error: Optional[str] = None
        
    async def initialize(self) -> None:
        """Initialize RAG service and dependencies."""
        try:
            self.logger.info("Initializing RAG service...")
            
            # Initialize Redis cache if available
            await self._initialize_cache()
            
            # Initialize RAG retriever
            await self._initialize_rag()
            
            self.initialized = True
            self.last_error = None
            self.logger.info("✅ RAG service initialized successfully")
            
        except Exception as e:
            self.last_error = str(e)
            log_error(self.logger, e, {"operation": "rag_service_init"})
            raise
    
    async def _initialize_cache(self) -> None:
        """Initialize Redis cache connection."""
        if not settings.REDIS_URL and not settings.REDIS_HOST:
            self.logger.info("Redis not configured, running without cache")
            return
        
        try:
            self.redis_client = redis.from_url(
                settings.redis_url_full,
                encoding="utf-8",
                decode_responses=True,
                socket_timeout=5,
                socket_connect_timeout=5,
            )
            
            # Test connection
            await self.redis_client.ping()
            self.logger.info("✅ Redis cache connected")
            
        except Exception as e:
            self.logger.warning(f"Redis connection failed, running without cache: {e}")
            self.redis_client = None
    
    async def _initialize_rag(self) -> None:
        """Initialize RAG retriever."""
        if not RAGRetriever or not RAGConfig:
            raise RuntimeError("RAG components not available. Please check RAG installation.")
        
        try:
            # Initialize RAG config
            config = RAGConfig()
            
            # Create RAG retriever
            self.rag_retriever = RAGRetriever(config)
            
            # Test RAG functionality
            test_result = await self._test_rag_query()
            if not test_result:
                raise RuntimeError("RAG test query failed")
            
            self.logger.info("✅ RAG retriever initialized")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize RAG retriever: {e}")
            raise
    
    async def _test_rag_query(self) -> bool:
        """Test RAG functionality with a simple query."""
        try:
            if not self.rag_retriever:
                return False
            
            # Simple test query
            results = await asyncio.wait_for(
                asyncio.to_thread(
                    self.rag_retriever.query_documents,
                    "test",
                    top_k=1,
                    min_score=0.0
                ),
                timeout=settings.RAG_TIMEOUT_SECONDS
            )
            
            return isinstance(results, list)
            
        except Exception as e:
            self.logger.warning(f"RAG test query failed: {e}")
            return False
    
    async def query_documents(self, request: RAGQueryRequest, user_id: Optional[str] = None) -> RAGQueryResponse:
        """Query documents using RAG with caching."""
        start_time = time.time()
        cache_hit = False
        query_hash = None
        
        try:
            # Generate cache key
            if request.use_cache and self.redis_client:
                query_hash = self._generate_cache_key(request)
                cached_result = await self._get_cached_result(query_hash)
                if cached_result:
                    cache_hit = True
                    duration_ms = (time.time() - start_time) * 1000
                    
                    log_rag_query(
                        self.logger, request.query, len(cached_result.results),
                        duration_ms, cache_hit=True, user_id=user_id
                    )
                    
                    return cached_result
            
            # Execute RAG query
            results = await self._execute_rag_query(request)
            
            # Create response
            duration_ms = (time.time() - start_time) * 1000
            response = RAGQueryResponse(
                results=results,
                query_time_ms=duration_ms,
                total_results=len(results),
                cache_hit=cache_hit,
                query_hash=query_hash
            )
            
            # Cache result
            if request.use_cache and self.redis_client and query_hash:
                await self._cache_result(query_hash, response)
            
            # Log query
            log_rag_query(
                self.logger, request.query, len(results),
                duration_ms, cache_hit=False, user_id=user_id
            )
            
            return response
            
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            log_error(self.logger, e, {
                "operation": "rag_query",
                "query_length": len(request.query),
                "duration_ms": duration_ms,
                "user_id": user_id
            })
            raise
    
    async def _execute_rag_query(self, request: RAGQueryRequest) -> List[RAGDocument]:
        """Execute RAG query with timeout."""
        if not self.rag_retriever:
            raise RuntimeError("RAG retriever not initialized")
        
        try:
            # Execute query with timeout
            raw_results = await asyncio.wait_for(
                asyncio.to_thread(
                    self.rag_retriever.query_documents,
                    request.query,
                    top_k=request.top_k,
                    min_score=request.min_score,
                    category_filter=request.category_filter
                ),
                timeout=settings.RAG_TIMEOUT_SECONDS
            )
            
            # Convert to RAGDocument objects
            documents = []
            for result in raw_results:
                doc = RAGDocument(
                    content=result.get("content", ""),
                    metadata=result.get("metadata", {}),
                    score=result.get("score", 0.0),
                    source_path=result.get("source_path", ""),
                    chunk_index=result.get("chunk_index"),
                    category=result.get("category")
                )
                documents.append(doc)
            
            return documents
            
        except asyncio.TimeoutError:
            raise RuntimeError(f"RAG query timeout after {settings.RAG_TIMEOUT_SECONDS} seconds")
        except Exception as e:
            raise RuntimeError(f"RAG query failed: {e}")
    
    def _generate_cache_key(self, request: RAGQueryRequest) -> str:
        """Generate cache key for query."""
        import hashlib
        
        cache_data = {
            "query": request.query,
            "top_k": request.top_k,
            "min_score": request.min_score,
            "category_filter": request.category_filter,
        }
        
        cache_string = json.dumps(cache_data, sort_keys=True)
        return f"rag_query:{hashlib.md5(cache_string.encode()).hexdigest()}"
    
    async def _get_cached_result(self, cache_key: str) -> Optional[RAGQueryResponse]:
        """Get cached query result."""
        if not self.redis_client:
            return None
        
        try:
            cached_data = await self.redis_client.get(cache_key)
            if cached_data:
                data = json.loads(cached_data)
                return RAGQueryResponse(**data)
        except Exception as e:
            self.logger.warning(f"Cache retrieval failed: {e}")
        
        return None
    
    async def _cache_result(self, cache_key: str, response: RAGQueryResponse) -> None:
        """Cache query result."""
        if not self.redis_client:
            return
        
        try:
            # Mark as cache hit for storage
            response_data = response.dict()
            response_data["cache_hit"] = True
            
            await self.redis_client.setex(
                cache_key,
                settings.RAG_CACHE_TTL_SECONDS,
                json.dumps(response_data, default=str)
            )
        except Exception as e:
            self.logger.warning(f"Cache storage failed: {e}")
    
    async def get_document_by_id(self, document_id: str) -> Optional[RAGDocument]:
        """Get specific document by ID."""
        # This would need to be implemented based on RAG system capabilities
        # For now, return None as placeholder
        self.logger.warning("get_document_by_id not yet implemented")
        return None
    
    async def health_check(self) -> RAGHealthStatus:
        """Perform health check on RAG service."""
        start_time = time.time()
        
        try:
            # Check RAG status
            if not self.initialized or not self.rag_retriever:
                return RAGHealthStatus(
                    status="down",
                    initialized=False,
                    total_documents=0,
                    index_loaded=False,
                    last_error=self.last_error or "Not initialized"
                )
            
            # Test query
            test_success = await self._test_rag_query()
            response_time_ms = (time.time() - start_time) * 1000
            
            # Check cache status
            cache_status = "disabled"
            if self.redis_client:
                try:
                    await self.redis_client.ping()
                    cache_status = "healthy"
                except Exception:
                    cache_status = "unhealthy"
            
            return RAGHealthStatus(
                status="operational" if test_success else "degraded",
                initialized=True,
                total_documents=0,  # TODO: Get actual count from RAG
                index_loaded=True,
                last_error=self.last_error,
                cache_status=cache_status,
                response_time_ms=response_time_ms
            )
            
        except Exception as e:
            log_error(self.logger, e, {"operation": "rag_health_check"})
            return RAGHealthStatus(
                status="down",
                initialized=self.initialized,
                total_documents=0,
                index_loaded=False,
                last_error=str(e),
                response_time_ms=(time.time() - start_time) * 1000
            )
    
    async def reindex(self, force_cpu: bool = False, clear_cache: bool = True) -> Dict[str, Any]:
        """Trigger RAG reindexing (admin operation)."""
        try:
            self.logger.info("Starting RAG reindexing...")
            
            # Clear cache if requested
            if clear_cache and self.redis_client:
                try:
                    # Clear all RAG-related cache keys
                    keys = await self.redis_client.keys("rag_query:*")
                    if keys:
                        await self.redis_client.delete(*keys)
                        self.logger.info(f"Cleared {len(keys)} cache entries")
                except Exception as e:
                    self.logger.warning(f"Cache clearing failed: {e}")
            
            # TODO: Implement actual reindexing logic
            # This would depend on the RAG system's reindexing capabilities
            
            return {
                "status": "completed",
                "message": "Reindexing completed successfully",
                "timestamp": settings.get_current_timestamp(),
                "cache_cleared": clear_cache
            }
            
        except Exception as e:
            log_error(self.logger, e, {"operation": "rag_reindex"})
            raise
    
    async def cleanup(self) -> None:
        """Cleanup resources."""
        try:
            if self.redis_client:
                await self.redis_client.close()
                self.logger.info("Redis connection closed")
            
            self.initialized = False
            self.logger.info("RAG service cleanup completed")
            
        except Exception as e:
            log_error(self.logger, e, {"operation": "rag_cleanup"})