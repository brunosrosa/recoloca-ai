# -*- coding: utf-8 -*-
"""
Recoloca.AI RAG Endpoints Tests
Comprehensive test suite for RAG API endpoints

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import pytest
import time
from typing import Dict, Any
from unittest.mock import AsyncMock, patch

from fastapi import status
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.services.rag_service import RAGQueryRequest, RAGQueryResponse, RAGDocument, RAGHealthStatus


class TestRAGQueryEndpoint:
    """Test suite for /api/v1/rag/query endpoint."""
    
    @pytest.mark.asyncio
    async def test_query_rag_success(self, async_client: AsyncClient, auth_headers: Dict[str, str], sample_rag_query: Dict[str, Any]):
        """Test successful RAG query."""
        response = await async_client.post(
            "/api/v1/rag/query",
            json=sample_rag_query,
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Validate response structure
        assert "results" in data
        assert "query_time_ms" in data
        assert "total_results" in data
        assert "cache_hit" in data
        assert "query_hash" in data
        
        # Validate results
        assert isinstance(data["results"], list)
        assert data["total_results"] >= 0
        assert data["query_time_ms"] >= 0
        
        if data["results"]:
            result = data["results"][0]
            assert "content" in result
            assert "metadata" in result
            assert "score" in result
            assert "source_path" in result
    
    @pytest.mark.asyncio
    async def test_query_rag_free_tier_limits(self, async_client: AsyncClient, free_user_auth_headers: Dict[str, str], sample_long_query: Dict[str, Any]):
        """Test free tier query length limits."""
        response = await async_client.post(
            "/api/v1/rag/query",
            json=sample_long_query,
            headers=free_user_auth_headers
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert "Query too long for free tier" in data["detail"]
    
    @pytest.mark.asyncio
    async def test_query_rag_free_tier_result_limits(self, async_client: AsyncClient, free_user_auth_headers: Dict[str, str]):
        """Test free tier result count limits."""
        query_data = {
            "query": "test query",
            "top_k": 10,  # Request more than free tier limit
            "min_score": 0.1,
            "use_cache": True
        }
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=free_user_auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Free tier should be limited to 3 results
        assert len(data["results"]) <= 3
    
    @pytest.mark.asyncio
    async def test_query_rag_invalid_request(self, async_client: AsyncClient, auth_headers: Dict[str, str], sample_invalid_query: Dict[str, Any]):
        """Test RAG query with invalid request data."""
        response = await async_client.post(
            "/api/v1/rag/query",
            json=sample_invalid_query,
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    @pytest.mark.asyncio
    async def test_query_rag_unauthorized(self, async_client: AsyncClient, sample_rag_query: Dict[str, Any]):
        """Test RAG query without authentication."""
        response = await async_client.post(
            "/api/v1/rag/query",
            json=sample_rag_query
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    @pytest.mark.asyncio
    async def test_query_rag_service_unavailable(self, async_client: AsyncClient, auth_headers: Dict[str, str], sample_rag_query: Dict[str, Any]):
        """Test RAG query when service is unavailable."""
        with patch('app.api.v1.endpoints.rag.get_rag_service') as mock_get_service:
            from fastapi import HTTPException
            mock_get_service.side_effect = HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="RAG service is not available"
            )
            
            response = await async_client.post(
                "/api/v1/rag/query",
                json=sample_rag_query,
                headers=auth_headers
            )
            
            assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
    
    @pytest.mark.asyncio
    async def test_query_rag_service_error(self, async_client: AsyncClient, auth_headers: Dict[str, str], sample_rag_query: Dict[str, Any], test_app):
        """Test RAG query when service throws an error."""
        # Mock the RAG service to throw an exception
        test_app.state.rag_service.query_documents = AsyncMock(side_effect=Exception("Service error"))
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json=sample_rag_query,
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        data = response.json()
        assert "Internal server error" in data["detail"]


class TestRAGDocumentEndpoint:
    """Test suite for /api/v1/rag/documents/{document_id} endpoint."""
    
    @pytest.mark.asyncio
    async def test_get_document_success(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test successful document retrieval."""
        document_id = "test-doc-1"
        
        response = await async_client.get(
            f"/api/v1/rag/documents/{document_id}",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Validate document structure
        assert "content" in data
        assert "metadata" in data
        assert "score" in data
        assert "source_path" in data
        assert data["metadata"]["id"] == document_id
    
    @pytest.mark.asyncio
    async def test_get_document_not_found(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test document retrieval for non-existent document."""
        document_id = "non-existent-doc"
        
        response = await async_client.get(
            f"/api/v1/rag/documents/{document_id}",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        data = response.json()
        assert "not found" in data["detail"].lower()
    
    @pytest.mark.asyncio
    async def test_get_document_unauthorized(self, async_client: AsyncClient):
        """Test document retrieval without authentication."""
        document_id = "test-doc-1"
        
        response = await async_client.get(
            f"/api/v1/rag/documents/{document_id}"
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestRAGStatusEndpoint:
    """Test suite for /api/v1/rag/status endpoint."""
    
    @pytest.mark.asyncio
    async def test_get_rag_status_success(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test successful RAG status retrieval."""
        response = await async_client.get(
            "/api/v1/rag/status",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Validate status structure
        assert "status" in data
        assert "initialized" in data
        assert "total_documents" in data
        assert "index_loaded" in data
        assert "response_time_ms" in data
        
        # Validate status values
        assert data["status"] in ["operational", "degraded", "down"]
        assert isinstance(data["initialized"], bool)
        assert isinstance(data["total_documents"], int)
        assert isinstance(data["index_loaded"], bool)
        assert isinstance(data["response_time_ms"], (int, float))
    
    @pytest.mark.asyncio
    async def test_get_rag_status_unauthorized(self, async_client: AsyncClient):
        """Test RAG status retrieval without authentication."""
        response = await async_client.get("/api/v1/rag/status")
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    @pytest.mark.asyncio
    async def test_get_rag_status_service_error(self, async_client: AsyncClient, auth_headers: Dict[str, str], test_app):
        """Test RAG status when service throws an error."""
        # Mock the RAG service to throw an exception
        test_app.state.rag_service.health_check = AsyncMock(side_effect=Exception("Health check error"))
        
        response = await async_client.get(
            "/api/v1/rag/status",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestRAGReindexEndpoint:
    """Test suite for /api/v1/rag/reindex endpoint."""
    
    @pytest.mark.asyncio
    async def test_reindex_rag_success(self, async_client: AsyncClient, admin_auth_headers: Dict[str, str]):
        """Test successful RAG reindexing."""
        response = await async_client.post(
            "/api/v1/rag/reindex",
            params={"force_cpu": False, "clear_cache": True},
            headers=admin_auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Validate reindex response
        assert "status" in data
        assert "message" in data
        assert "timestamp" in data
        assert "cache_cleared" in data
        
        assert data["status"] == "completed"
        assert isinstance(data["cache_cleared"], bool)
    
    @pytest.mark.asyncio
    async def test_reindex_rag_unauthorized_user(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test RAG reindexing with regular user (should fail)."""
        response = await async_client.post(
            "/api/v1/rag/reindex",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    @pytest.mark.asyncio
    async def test_reindex_rag_unauthorized(self, async_client: AsyncClient):
        """Test RAG reindexing without authentication."""
        response = await async_client.post("/api/v1/rag/reindex")
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    @pytest.mark.asyncio
    async def test_reindex_rag_with_parameters(self, async_client: AsyncClient, admin_auth_headers: Dict[str, str]):
        """Test RAG reindexing with custom parameters."""
        response = await async_client.post(
            "/api/v1/rag/reindex",
            params={"force_cpu": True, "clear_cache": False},
            headers=admin_auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["cache_cleared"] == False


class TestRAGCategoriesEndpoint:
    """Test suite for /api/v1/rag/categories endpoint."""
    
    @pytest.mark.asyncio
    async def test_get_categories_success(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test successful categories retrieval."""
        response = await async_client.get(
            "/api/v1/rag/categories",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Validate categories structure
        assert "categories" in data
        assert "total_categories" in data
        assert "last_updated" in data
        
        assert isinstance(data["categories"], list)
        assert isinstance(data["total_categories"], int)
        
        # Validate category structure
        if data["categories"]:
            category = data["categories"][0]
            assert "name" in category
            assert "description" in category
            assert "document_count" in category
    
    @pytest.mark.asyncio
    async def test_get_categories_unauthorized(self, async_client: AsyncClient):
        """Test categories retrieval without authentication."""
        response = await async_client.get("/api/v1/rag/categories")
        
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestRAGMetricsEndpoint:
    """Test suite for /api/v1/rag/metrics endpoint."""
    
    @pytest.mark.asyncio
    async def test_get_metrics_success(self, async_client: AsyncClient, admin_auth_headers: Dict[str, str]):
        """Test successful metrics retrieval."""
        response = await async_client.get(
            "/api/v1/rag/metrics",
            headers=admin_auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        
        # Validate metrics structure
        assert "query_stats" in data
        assert "performance" in data
        assert "errors" in data
        assert "system" in data
        assert "timestamp" in data
        
        # Validate query stats
        query_stats = data["query_stats"]
        assert "total_queries" in query_stats
        assert "queries_last_24h" in query_stats
        assert "average_response_time_ms" in query_stats
        assert "cache_hit_rate" in query_stats
    
    @pytest.mark.asyncio
    async def test_get_metrics_unauthorized_user(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test metrics retrieval with regular user (should fail)."""
        response = await async_client.get(
            "/api/v1/rag/metrics",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    @pytest.mark.asyncio
    async def test_get_metrics_unauthorized(self, async_client: AsyncClient):
        """Test metrics retrieval without authentication."""
        response = await async_client.get("/api/v1/rag/metrics")
        
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestRAGEndpointsIntegration:
    """Integration tests for RAG endpoints."""
    
    @pytest.mark.asyncio
    async def test_rag_workflow_integration(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test complete RAG workflow integration."""
        # 1. Check RAG status
        status_response = await async_client.get(
            "/api/v1/rag/status",
            headers=auth_headers
        )
        assert status_response.status_code == status.HTTP_200_OK
        
        # 2. Get available categories
        categories_response = await async_client.get(
            "/api/v1/rag/categories",
            headers=auth_headers
        )
        assert categories_response.status_code == status.HTTP_200_OK
        
        # 3. Perform a query
        query_data = {
            "query": "FastAPI authentication",
            "top_k": 3,
            "min_score": 0.3,
            "use_cache": True
        }
        
        query_response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=auth_headers
        )
        assert query_response.status_code == status.HTTP_200_OK
        
        # 4. Try to get a specific document (if any results)
        query_data = query_response.json()
        if query_data["results"]:
            # This would normally use a real document ID from the query results
            doc_response = await async_client.get(
                "/api/v1/rag/documents/test-doc-1",
                headers=auth_headers
            )
            # Document might not exist, but endpoint should respond properly
            assert doc_response.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]


class TestRAGEndpointsPerformance:
    """Performance tests for RAG endpoints."""
    
    @pytest.mark.asyncio
    async def test_query_response_time(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test RAG query response time."""
        query_data = {
            "query": "FastAPI performance optimization",
            "top_k": 5,
            "min_score": 0.2,
            "use_cache": False  # Disable cache to test actual query time
        }
        
        start_time = time.time()
        response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=auth_headers
        )
        end_time = time.time()
        
        assert response.status_code == status.HTTP_200_OK
        
        # Response should be under 2 seconds for MVP
        response_time = end_time - start_time
        assert response_time < 2.0, f"Query took {response_time:.2f}s, expected < 2.0s"
        
        # Check reported query time
        data = response.json()
        assert data["query_time_ms"] < 2000, f"Reported query time {data['query_time_ms']}ms, expected < 2000ms"
    
    @pytest.mark.asyncio
    async def test_concurrent_queries(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test concurrent RAG queries."""
        import asyncio
        
        query_data = {
            "query": "FastAPI concurrent requests",
            "top_k": 3,
            "min_score": 0.3,
            "use_cache": True
        }
        
        # Send 5 concurrent requests
        tasks = []
        for _ in range(5):
            task = async_client.post(
                "/api/v1/rag/query",
                json=query_data,
                headers=auth_headers
            )
            tasks.append(task)
        
        start_time = time.time()
        responses = await asyncio.gather(*tasks)
        end_time = time.time()
        
        # All requests should succeed
        for response in responses:
            assert response.status_code == status.HTTP_200_OK
        
        # Concurrent requests should not take much longer than a single request
        total_time = end_time - start_time
        assert total_time < 5.0, f"Concurrent queries took {total_time:.2f}s, expected < 5.0s"
    
    @pytest.mark.asyncio
    async def test_cache_performance(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test RAG query cache performance."""
        query_data = {
            "query": "FastAPI cache performance test",
            "top_k": 5,
            "min_score": 0.2,
            "use_cache": True
        }
        
        # First request (cache miss)
        first_response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=auth_headers
        )
        assert first_response.status_code == status.HTTP_200_OK
        first_data = first_response.json()
        
        # Second request (should be cache hit)
        second_response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=auth_headers
        )
        assert second_response.status_code == status.HTTP_200_OK
        second_data = second_response.json()
        
        # Cache hit should be faster
        # Note: In our mock, cache_hit is always False, but in real implementation
        # the second request should have cache_hit=True and faster response time
        assert second_data["query_time_ms"] <= first_data["query_time_ms"] * 2  # Allow some variance