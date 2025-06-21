# -*- coding: utf-8 -*-
"""
Recoloca.AI Backend Test Configuration
Pytest fixtures and test configuration

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import asyncio
import os
import pytest
from typing import AsyncGenerator, Generator
from unittest.mock import AsyncMock, MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

# Set test environment variables
os.environ["ENVIRONMENT"] = "testing"
os.environ["DEBUG"] = "true"
os.environ["TESTING"] = "true"
os.environ["RAG_ENABLED"] = "false"  # Disable RAG for most tests
os.environ["REDIS_URL"] = "redis://localhost:6379/15"  # Test database
os.environ["SECRET_KEY"] = "test-secret-key-for-testing-only"
os.environ["JWT_SECRET_KEY"] = "test-jwt-secret-key-for-testing-only"
os.environ["SUPABASE_URL"] = "https://test.supabase.co"
os.environ["SUPABASE_ANON_KEY"] = "test-anon-key"
os.environ["SUPABASE_SERVICE_ROLE_KEY"] = "test-service-role-key"

from main import app
from app.core.config import settings
from app.services.rag_service import RAGService, RAGQueryRequest, RAGQueryResponse, RAGDocument


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def test_app() -> FastAPI:
    """Create a test FastAPI application."""
    return app


@pytest.fixture
def client(test_app: FastAPI) -> TestClient:
    """Create a test client for synchronous tests."""
    return TestClient(test_app)


@pytest.fixture
async def async_client(test_app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create an async test client for asynchronous tests."""
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def mock_rag_service() -> MagicMock:
    """Create a mock RAG service for testing."""
    mock_service = MagicMock(spec=RAGService)
    mock_service.initialized = True
    mock_service.last_error = None
    
    # Mock query_documents method
    async def mock_query_documents(request: RAGQueryRequest, user_id: str = None) -> RAGQueryResponse:
        return RAGQueryResponse(
            results=[
                RAGDocument(
                    content="Test document content",
                    metadata={"source": "test"},
                    score=0.95,
                    source_path="test/document.md",
                    chunk_index=0,
                    category="test"
                )
            ],
            query_time_ms=50.0,
            total_results=1,
            cache_hit=False,
            query_hash="test-hash"
        )
    
    mock_service.query_documents = AsyncMock(side_effect=mock_query_documents)
    
    # Mock health_check method
    from app.services.rag_service import RAGHealthStatus
    async def mock_health_check() -> RAGHealthStatus:
        return RAGHealthStatus(
            status="operational",
            initialized=True,
            total_documents=10,
            index_loaded=True,
            last_error=None,
            cache_status="healthy",
            response_time_ms=25.0
        )
    
    mock_service.health_check = AsyncMock(side_effect=mock_health_check)
    
    # Mock get_document_by_id method
    async def mock_get_document_by_id(document_id: str) -> RAGDocument:
        if document_id == "test-doc-1":
            return RAGDocument(
                content="Test document content",
                metadata={"id": document_id},
                score=1.0,
                source_path="test/document.md",
                chunk_index=0,
                category="test"
            )
        return None
    
    mock_service.get_document_by_id = AsyncMock(side_effect=mock_get_document_by_id)
    
    # Mock reindex method
    async def mock_reindex(force_cpu: bool = False, clear_cache: bool = True) -> dict:
        return {
            "status": "completed",
            "message": "Reindexing completed successfully",
            "timestamp": "2025-06-20T10:00:00Z",
            "cache_cleared": clear_cache
        }
    
    mock_service.reindex = AsyncMock(side_effect=mock_reindex)
    
    return mock_service


@pytest.fixture
def mock_user_token() -> str:
    """Create a mock JWT token for testing."""
    from app.api.dependencies.auth import create_access_token
    from datetime import timedelta
    
    user_data = {
        "sub": "test-user-id",
        "id": "test-user-id",
        "email": "test@example.com",
        "tier": "premium",
        "role": "user"
    }
    
    return create_access_token(
        data=user_data,
        expires_delta=timedelta(hours=1)
    )


@pytest.fixture
def mock_admin_token() -> str:
    """Create a mock admin JWT token for testing."""
    from app.api.dependencies.auth import create_access_token
    from datetime import timedelta
    
    admin_data = {
        "sub": "test-admin-id",
        "id": "test-admin-id",
        "email": "admin@example.com",
        "tier": "admin",
        "role": "admin"
    }
    
    return create_access_token(
        data=admin_data,
        expires_delta=timedelta(hours=1)
    )


@pytest.fixture
def mock_free_user_token() -> str:
    """Create a mock free tier user JWT token for testing."""
    from app.api.dependencies.auth import create_access_token
    from datetime import timedelta
    
    user_data = {
        "sub": "test-free-user-id",
        "id": "test-free-user-id",
        "email": "free@example.com",
        "tier": "free",
        "role": "user"
    }
    
    return create_access_token(
        data=user_data,
        expires_delta=timedelta(hours=1)
    )


@pytest.fixture
def auth_headers(mock_user_token: str) -> dict:
    """Create authorization headers for testing."""
    return {"Authorization": f"Bearer {mock_user_token}"}


@pytest.fixture
def admin_auth_headers(mock_admin_token: str) -> dict:
    """Create admin authorization headers for testing."""
    return {"Authorization": f"Bearer {mock_admin_token}"}


@pytest.fixture
def free_user_auth_headers(mock_free_user_token: str) -> dict:
    """Create free user authorization headers for testing."""
    return {"Authorization": f"Bearer {mock_free_user_token}"}


@pytest.fixture(autouse=True)
def setup_test_environment(test_app: FastAPI, mock_rag_service: MagicMock):
    """Setup test environment before each test."""
    # Inject mock RAG service into app state
    test_app.state.rag_service = mock_rag_service
    
    yield
    
    # Cleanup after test
    if hasattr(test_app.state, 'rag_service'):
        delattr(test_app.state, 'rag_service')


# Test data fixtures
@pytest.fixture
def sample_rag_query() -> dict:
    """Sample RAG query data for testing."""
    return {
        "query": "Como implementar autenticação JWT no FastAPI?",
        "top_k": 5,
        "min_score": 0.3,
        "category_filter": None,
        "use_cache": True
    }


@pytest.fixture
def sample_long_query() -> dict:
    """Sample long RAG query for testing free tier limits."""
    long_text = "Como implementar autenticação JWT no FastAPI? " * 50  # ~2500 chars
    return {
        "query": long_text,
        "top_k": 5,
        "min_score": 0.3,
        "category_filter": None,
        "use_cache": True
    }


@pytest.fixture
def sample_invalid_query() -> dict:
    """Sample invalid RAG query for testing validation."""
    return {
        "query": "",  # Empty query
        "top_k": 25,  # Too many results
        "min_score": 1.5,  # Invalid score
        "category_filter": "invalid_category",
        "use_cache": True
    }