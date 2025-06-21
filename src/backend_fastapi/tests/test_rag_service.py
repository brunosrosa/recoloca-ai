# -*- coding: utf-8 -*-
"""
Recoloca.AI RAG Service Tests
Comprehensive test suite for RAG service functionality

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import pytest
import asyncio
import time
from typing import Dict, Any, List
from unittest.mock import AsyncMock, MagicMock, patch

from app.services.rag_service import (
    RAGService,
    RAGQueryRequest,
    RAGQueryResponse,
    RAGDocument,
    RAGHealthStatus
)


class TestRAGService:
    """Test suite for RAGService class."""
    
    @pytest.fixture
    def rag_service(self):
        """Create a RAGService instance for testing."""
        return RAGService()
    
    @pytest.mark.asyncio
    async def test_rag_service_initialization(self, rag_service: RAGService):
        """Test RAG service initialization."""
        # Initially not initialized
        assert not rag_service.is_initialized
        assert rag_service.cache is None
        assert rag_service.rag_retriever is None
        
        # Initialize service
        await rag_service.initialize()
        
        # Should be initialized now
        assert rag_service.is_initialized
        # Note: In test environment, cache and rag_retriever might still be None
        # due to missing dependencies, but initialization should complete
    
    @pytest.mark.asyncio
    async def test_rag_service_cache_initialization(self, rag_service: RAGService):
        """Test Redis cache initialization."""
        with patch('redis.asyncio.from_url') as mock_redis:
            mock_redis_instance = AsyncMock()
            mock_redis.return_value = mock_redis_instance
            mock_redis_instance.ping.return_value = True
            
            await rag_service._initialize_cache()
            
            assert rag_service.cache is not None
            mock_redis_instance.ping.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_rag_service_cache_initialization_failure(self, rag_service: RAGService):
        """Test Redis cache initialization failure."""
        with patch('redis.asyncio.from_url') as mock_redis:
            mock_redis.side_effect = Exception("Redis connection failed")
            
            await rag_service._initialize_cache()
            
            # Should handle failure gracefully
            assert rag_service.cache is None
    
    @pytest.mark.asyncio
    async def test_rag_service_rag_initialization(self, rag_service: RAGService):
        """Test RAG retriever initialization."""
        with patch('app.services.rag_service.RAGRetriever') as mock_retriever_class:
            mock_retriever = AsyncMock()
            mock_retriever_class.return_value = mock_retriever
            mock_retriever.initialize.return_value = None
            
            await rag_service._initialize_rag()
            
            assert rag_service.rag_retriever is not None
            mock_retriever.initialize.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_rag_service_rag_initialization_failure(self, rag_service: RAGService):
        """Test RAG retriever initialization failure."""
        with patch('app.services.rag_service.RAGRetriever') as mock_retriever_class:
            mock_retriever_class.side_effect = Exception("RAG initialization failed")
            
            await rag_service._initialize_rag()
            
            # Should handle failure gracefully
            assert rag_service.rag_retriever is None


class TestRAGServiceQueries:
    """Test suite for RAG service query functionality."""
    
    @pytest.fixture
    def initialized_rag_service(self):
        """Create an initialized RAGService instance for testing."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock RAG retriever
        service.rag_retriever = AsyncMock()
        service.rag_retriever.query.return_value = [
            {
                "content": "Test document content 1",
                "metadata": {"id": "doc1", "category": "test"},
                "score": 0.95,
                "source_path": "/test/doc1.md"
            },
            {
                "content": "Test document content 2",
                "metadata": {"id": "doc2", "category": "test"},
                "score": 0.85,
                "source_path": "/test/doc2.md"
            }
        ]
        
        # Mock Redis cache
        service.cache = AsyncMock()
        service.cache.get.return_value = None  # Cache miss by default
        service.cache.setex.return_value = True
        
        return service
    
    @pytest.mark.asyncio
    async def test_query_documents_success(self, initialized_rag_service: RAGService):
        """Test successful document query."""
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3,
            use_cache=True
        )
        
        response = await initialized_rag_service.query_documents(request)
        
        assert isinstance(response, RAGQueryResponse)
        assert len(response.results) == 2
        assert response.total_results == 2
        assert response.query_time_ms > 0
        assert not response.cache_hit  # First query should be cache miss
        assert response.query_hash is not None
        
        # Validate document structure
        doc = response.results[0]
        assert isinstance(doc, RAGDocument)
        assert doc.content == "Test document content 1"
        assert doc.metadata["id"] == "doc1"
        assert doc.score == 0.95
        assert doc.source_path == "/test/doc1.md"
    
    @pytest.mark.asyncio
    async def test_query_documents_cache_hit(self, initialized_rag_service: RAGService):
        """Test document query with cache hit."""
        # Mock cache hit
        cached_response = {
            "results": [
                {
                    "content": "Cached content",
                    "metadata": {"id": "cached_doc"},
                    "score": 0.9,
                    "source_path": "/cached/doc.md"
                }
            ],
            "total_results": 1,
            "query_time_ms": 50,
            "cache_hit": True,
            "query_hash": "cached_hash"
        }
        
        import json
        initialized_rag_service.cache.get.return_value = json.dumps(cached_response)
        
        request = RAGQueryRequest(
            query="cached query",
            top_k=5,
            min_score=0.3,
            use_cache=True
        )
        
        response = await initialized_rag_service.query_documents(request)
        
        assert response.cache_hit
        assert response.total_results == 1
        assert response.results[0].content == "Cached content"
        
        # RAG retriever should not be called for cache hit
        initialized_rag_service.rag_retriever.query.assert_not_called()
    
    @pytest.mark.asyncio
    async def test_query_documents_no_cache(self, initialized_rag_service: RAGService):
        """Test document query without cache."""
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3,
            use_cache=False
        )
        
        response = await initialized_rag_service.query_documents(request)
        
        assert not response.cache_hit
        assert len(response.results) == 2
        
        # Cache should not be checked or updated
        initialized_rag_service.cache.get.assert_not_called()
        initialized_rag_service.cache.setex.assert_not_called()
    
    @pytest.mark.asyncio
    async def test_query_documents_filter_by_score(self, initialized_rag_service: RAGService):
        """Test document query with score filtering."""
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.9,  # High threshold
            use_cache=False
        )
        
        response = await initialized_rag_service.query_documents(request)
        
        # Only documents with score >= 0.9 should be returned
        assert len(response.results) == 1
        assert response.results[0].score >= 0.9
    
    @pytest.mark.asyncio
    async def test_query_documents_limit_results(self, initialized_rag_service: RAGService):
        """Test document query with result limiting."""
        request = RAGQueryRequest(
            query="test query",
            top_k=1,  # Limit to 1 result
            min_score=0.3,
            use_cache=False
        )
        
        response = await initialized_rag_service.query_documents(request)
        
        # Should return only 1 result (the highest scoring one)
        assert len(response.results) == 1
        assert response.results[0].score == 0.95  # Highest score
    
    @pytest.mark.asyncio
    async def test_query_documents_service_not_initialized(self):
        """Test document query when service is not initialized."""
        service = RAGService()
        # Service is not initialized
        
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3,
            use_cache=True
        )
        
        with pytest.raises(Exception) as exc_info:
            await service.query_documents(request)
        
        assert "not initialized" in str(exc_info.value).lower()
    
    @pytest.mark.asyncio
    async def test_query_documents_rag_retriever_error(self, initialized_rag_service: RAGService):
        """Test document query when RAG retriever throws an error."""
        # Mock RAG retriever to throw an exception
        initialized_rag_service.rag_retriever.query.side_effect = Exception("RAG query failed")
        
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3,
            use_cache=False
        )
        
        with pytest.raises(Exception) as exc_info:
            await initialized_rag_service.query_documents(request)
        
        assert "RAG query failed" in str(exc_info.value)
    
    @pytest.mark.asyncio
    async def test_query_documents_timeout(self, initialized_rag_service: RAGService):
        """Test document query timeout."""
        # Mock RAG retriever to take too long
        async def slow_query(*args, **kwargs):
            await asyncio.sleep(2)  # Longer than timeout
            return []
        
        initialized_rag_service.rag_retriever.query.side_effect = slow_query
        
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3,
            use_cache=False
        )
        
        with pytest.raises(asyncio.TimeoutError):
            await initialized_rag_service.query_documents(request)


class TestRAGServiceHealthCheck:
    """Test suite for RAG service health check functionality."""
    
    @pytest.fixture
    def healthy_rag_service(self):
        """Create a healthy RAGService instance for testing."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock healthy RAG retriever
        service.rag_retriever = AsyncMock()
        service.rag_retriever.get_document_count.return_value = 100
        service.rag_retriever.query.return_value = [
            {
                "content": "Health check content",
                "metadata": {"id": "health_doc"},
                "score": 0.9,
                "source_path": "/health/doc.md"
            }
        ]
        
        # Mock healthy Redis cache
        service.cache = AsyncMock()
        service.cache.ping.return_value = True
        
        return service
    
    @pytest.mark.asyncio
    async def test_health_check_success(self, healthy_rag_service: RAGService):
        """Test successful health check."""
        status = await healthy_rag_service.health_check()
        
        assert isinstance(status, RAGHealthStatus)
        assert status.status == "operational"
        assert status.initialized
        assert status.total_documents == 100
        assert status.index_loaded
        assert status.response_time_ms > 0
        assert status.cache_status == "connected"
        assert status.last_error is None
    
    @pytest.mark.asyncio
    async def test_health_check_not_initialized(self):
        """Test health check when service is not initialized."""
        service = RAGService()
        # Service is not initialized
        
        status = await service.health_check()
        
        assert status.status == "down"
        assert not status.initialized
        assert status.total_documents == 0
        assert not status.index_loaded
        assert status.cache_status == "disconnected"
        assert "not initialized" in status.last_error.lower()
    
    @pytest.mark.asyncio
    async def test_health_check_rag_retriever_error(self, healthy_rag_service: RAGService):
        """Test health check when RAG retriever has issues."""
        # Mock RAG retriever to throw an exception
        healthy_rag_service.rag_retriever.get_document_count.side_effect = Exception("RAG error")
        
        status = await healthy_rag_service.health_check()
        
        assert status.status == "degraded"
        assert status.initialized
        assert status.total_documents == 0
        assert not status.index_loaded
        assert "RAG error" in status.last_error
    
    @pytest.mark.asyncio
    async def test_health_check_cache_error(self, healthy_rag_service: RAGService):
        """Test health check when cache has issues."""
        # Mock cache to throw an exception
        healthy_rag_service.cache.ping.side_effect = Exception("Cache error")
        
        status = await healthy_rag_service.health_check()
        
        assert status.cache_status == "error"
        # Service should still be operational if only cache has issues
        assert status.status in ["operational", "degraded"]
    
    @pytest.mark.asyncio
    async def test_health_check_test_query_failure(self, healthy_rag_service: RAGService):
        """Test health check when test query fails."""
        # Mock test query to fail
        healthy_rag_service.rag_retriever.query.side_effect = Exception("Query test failed")
        
        status = await healthy_rag_service.health_check()
        
        assert status.status == "degraded"
        assert "Query test failed" in status.last_error


class TestRAGServiceDocumentRetrieval:
    """Test suite for RAG service document retrieval functionality."""
    
    @pytest.fixture
    def document_rag_service(self):
        """Create a RAGService instance with document retrieval capability."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock RAG retriever with document retrieval
        service.rag_retriever = AsyncMock()
        service.rag_retriever.get_document_by_id.return_value = {
            "content": "Document content by ID",
            "metadata": {"id": "test-doc-1", "category": "test"},
            "score": 1.0,
            "source_path": "/test/doc1.md"
        }
        
        return service
    
    @pytest.mark.asyncio
    async def test_get_document_by_id_success(self, document_rag_service: RAGService):
        """Test successful document retrieval by ID."""
        document = await document_rag_service.get_document_by_id("test-doc-1")
        
        assert isinstance(document, RAGDocument)
        assert document.content == "Document content by ID"
        assert document.metadata["id"] == "test-doc-1"
        assert document.score == 1.0
        assert document.source_path == "/test/doc1.md"
    
    @pytest.mark.asyncio
    async def test_get_document_by_id_not_found(self, document_rag_service: RAGService):
        """Test document retrieval for non-existent document."""
        # Mock retriever to return None for non-existent document
        document_rag_service.rag_retriever.get_document_by_id.return_value = None
        
        document = await document_rag_service.get_document_by_id("non-existent")
        
        assert document is None
    
    @pytest.mark.asyncio
    async def test_get_document_by_id_service_not_initialized(self):
        """Test document retrieval when service is not initialized."""
        service = RAGService()
        # Service is not initialized
        
        with pytest.raises(Exception) as exc_info:
            await service.get_document_by_id("test-doc-1")
        
        assert "not initialized" in str(exc_info.value).lower()


class TestRAGServiceReindexing:
    """Test suite for RAG service reindexing functionality."""
    
    @pytest.fixture
    def reindex_rag_service(self):
        """Create a RAGService instance with reindexing capability."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock RAG retriever with reindexing
        service.rag_retriever = AsyncMock()
        service.rag_retriever.reindex.return_value = None
        
        # Mock Redis cache
        service.cache = AsyncMock()
        service.cache.flushdb.return_value = True
        
        return service
    
    @pytest.mark.asyncio
    async def test_reindex_success(self, reindex_rag_service: RAGService):
        """Test successful reindexing."""
        result = await reindex_rag_service.reindex(force_cpu=False, clear_cache=True)
        
        assert result["status"] == "completed"
        assert result["cache_cleared"] is True
        assert "timestamp" in result
        assert "message" in result
        
        # Verify reindex was called
        reindex_rag_service.rag_retriever.reindex.assert_called_once_with(force_cpu=False)
        
        # Verify cache was cleared
        reindex_rag_service.cache.flushdb.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_reindex_without_cache_clear(self, reindex_rag_service: RAGService):
        """Test reindexing without clearing cache."""
        result = await reindex_rag_service.reindex(force_cpu=True, clear_cache=False)
        
        assert result["status"] == "completed"
        assert result["cache_cleared"] is False
        
        # Verify reindex was called with force_cpu=True
        reindex_rag_service.rag_retriever.reindex.assert_called_once_with(force_cpu=True)
        
        # Verify cache was not cleared
        reindex_rag_service.cache.flushdb.assert_not_called()
    
    @pytest.mark.asyncio
    async def test_reindex_service_not_initialized(self):
        """Test reindexing when service is not initialized."""
        service = RAGService()
        # Service is not initialized
        
        with pytest.raises(Exception) as exc_info:
            await service.reindex()
        
        assert "not initialized" in str(exc_info.value).lower()
    
    @pytest.mark.asyncio
    async def test_reindex_rag_retriever_error(self, reindex_rag_service: RAGService):
        """Test reindexing when RAG retriever throws an error."""
        # Mock RAG retriever to throw an exception
        reindex_rag_service.rag_retriever.reindex.side_effect = Exception("Reindex failed")
        
        with pytest.raises(Exception) as exc_info:
            await reindex_rag_service.reindex()
        
        assert "Reindex failed" in str(exc_info.value)


class TestRAGServiceCacheOperations:
    """Test suite for RAG service cache operations."""
    
    @pytest.fixture
    def cache_rag_service(self):
        """Create a RAGService instance with cache operations."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock Redis cache
        service.cache = AsyncMock()
        service.cache.get.return_value = None
        service.cache.setex.return_value = True
        
        return service
    
    def test_generate_cache_key(self, cache_rag_service: RAGService):
        """Test cache key generation."""
        request = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3,
            category_filter="test"
        )
        
        key = cache_rag_service._generate_cache_key(request)
        
        assert key.startswith("rag_query:")
        assert len(key) > 20  # Should be a reasonable length hash
    
    def test_generate_cache_key_consistency(self, cache_rag_service: RAGService):
        """Test cache key generation consistency."""
        request1 = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3
        )
        
        request2 = RAGQueryRequest(
            query="test query",
            top_k=5,
            min_score=0.3
        )
        
        key1 = cache_rag_service._generate_cache_key(request1)
        key2 = cache_rag_service._generate_cache_key(request2)
        
        # Same requests should generate same cache key
        assert key1 == key2
    
    def test_generate_cache_key_different_requests(self, cache_rag_service: RAGService):
        """Test cache key generation for different requests."""
        request1 = RAGQueryRequest(
            query="test query 1",
            top_k=5,
            min_score=0.3
        )
        
        request2 = RAGQueryRequest(
            query="test query 2",
            top_k=5,
            min_score=0.3
        )
        
        key1 = cache_rag_service._generate_cache_key(request1)
        key2 = cache_rag_service._generate_cache_key(request2)
        
        # Different requests should generate different cache keys
        assert key1 != key2
    
    @pytest.mark.asyncio
    async def test_get_cached_response_hit(self, cache_rag_service: RAGService):
        """Test getting cached response (cache hit)."""
        cached_data = {
            "results": [{"content": "cached", "metadata": {}, "score": 0.9, "source_path": "/cached.md"}],
            "total_results": 1,
            "query_time_ms": 50,
            "cache_hit": True,
            "query_hash": "cached_hash"
        }
        
        import json
        cache_rag_service.cache.get.return_value = json.dumps(cached_data)
        
        cache_key = "test_cache_key"
        response = await cache_rag_service._get_cached_response(cache_key)
        
        assert response is not None
        assert isinstance(response, RAGQueryResponse)
        assert response.cache_hit
        assert response.total_results == 1
    
    @pytest.mark.asyncio
    async def test_get_cached_response_miss(self, cache_rag_service: RAGService):
        """Test getting cached response (cache miss)."""
        cache_rag_service.cache.get.return_value = None
        
        cache_key = "test_cache_key"
        response = await cache_rag_service._get_cached_response(cache_key)
        
        assert response is None
    
    @pytest.mark.asyncio
    async def test_store_response_in_cache(self, cache_rag_service: RAGService):
        """Test storing response in cache."""
        response = RAGQueryResponse(
            results=[],
            total_results=0,
            query_time_ms=100,
            cache_hit=False,
            query_hash="test_hash"
        )
        
        cache_key = "test_cache_key"
        await cache_rag_service._store_response_in_cache(cache_key, response)
        
        # Verify cache.setex was called
        cache_rag_service.cache.setex.assert_called_once()
        
        # Verify the stored response has cache_hit=True
        call_args = cache_rag_service.cache.setex.call_args
        stored_data = json.loads(call_args[0][2])  # Third argument is the JSON data
        assert stored_data["cache_hit"] is True


class TestRAGServiceCleanup:
    """Test suite for RAG service cleanup functionality."""
    
    @pytest.fixture
    def cleanup_rag_service(self):
        """Create a RAGService instance for cleanup testing."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock Redis cache
        service.cache = AsyncMock()
        service.cache.close.return_value = None
        
        return service
    
    @pytest.mark.asyncio
    async def test_cleanup_success(self, cleanup_rag_service: RAGService):
        """Test successful service cleanup."""
        await cleanup_rag_service.cleanup()
        
        # Verify cache was closed
        cleanup_rag_service.cache.close.assert_called_once()
        
        # Verify service state was reset
        assert not cleanup_rag_service.is_initialized
        assert cleanup_rag_service.cache is None
        assert cleanup_rag_service.rag_retriever is None
    
    @pytest.mark.asyncio
    async def test_cleanup_no_cache(self):
        """Test cleanup when no cache is present."""
        service = RAGService()
        service.is_initialized = True
        service.cache = None
        
        # Should not raise an exception
        await service.cleanup()
        
        assert not service.is_initialized
    
    @pytest.mark.asyncio
    async def test_cleanup_cache_error(self, cleanup_rag_service: RAGService):
        """Test cleanup when cache close throws an error."""
        cleanup_rag_service.cache.close.side_effect = Exception("Cache close error")
        
        # Should handle error gracefully
        await cleanup_rag_service.cleanup()
        
        # Service should still be cleaned up
        assert not cleanup_rag_service.is_initialized
        assert cleanup_rag_service.cache is None


class TestRAGServicePerformance:
    """Performance tests for RAG service."""
    
    @pytest.fixture
    def performance_rag_service(self):
        """Create a RAGService instance for performance testing."""
        service = RAGService()
        service.is_initialized = True
        
        # Mock fast RAG retriever
        service.rag_retriever = AsyncMock()
        service.rag_retriever.query.return_value = [
            {
                "content": f"Performance test content {i}",
                "metadata": {"id": f"perf_doc_{i}"},
                "score": 0.9 - (i * 0.1),
                "source_path": f"/perf/doc{i}.md"
            }
            for i in range(10)
        ]
        
        # Mock fast cache
        service.cache = AsyncMock()
        service.cache.get.return_value = None
        service.cache.setex.return_value = True
        
        return service
    
    @pytest.mark.asyncio
    async def test_query_performance(self, performance_rag_service: RAGService):
        """Test query performance."""
        request = RAGQueryRequest(
            query="performance test query",
            top_k=10,
            min_score=0.1,
            use_cache=False
        )
        
        start_time = time.time()
        response = await performance_rag_service.query_documents(request)
        end_time = time.time()
        
        query_time = end_time - start_time
        
        # Query should complete quickly (under 1 second for mocked service)
        assert query_time < 1.0
        assert response.query_time_ms < 1000
        assert len(response.results) == 10
    
    @pytest.mark.asyncio
    async def test_concurrent_queries_performance(self, performance_rag_service: RAGService):
        """Test concurrent query performance."""
        requests = [
            RAGQueryRequest(
                query=f"concurrent test query {i}",
                top_k=5,
                min_score=0.3,
                use_cache=False
            )
            for i in range(5)
        ]
        
        start_time = time.time()
        
        # Execute concurrent queries
        tasks = [
            performance_rag_service.query_documents(request)
            for request in requests
        ]
        responses = await asyncio.gather(*tasks)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Concurrent queries should not take much longer than sequential
        assert total_time < 2.0
        assert len(responses) == 5
        
        # All responses should be valid
        for response in responses:
            assert isinstance(response, RAGQueryResponse)
            assert len(response.results) <= 5
    
    @pytest.mark.asyncio
    async def test_health_check_performance(self, performance_rag_service: RAGService):
        """Test health check performance."""
        # Mock document count retrieval
        performance_rag_service.rag_retriever.get_document_count.return_value = 1000
        
        start_time = time.time()
        status = await performance_rag_service.health_check()
        end_time = time.time()
        
        health_check_time = end_time - start_time
        
        # Health check should be fast
        assert health_check_time < 0.5
        assert status.response_time_ms < 500
        assert status.status == "operational"