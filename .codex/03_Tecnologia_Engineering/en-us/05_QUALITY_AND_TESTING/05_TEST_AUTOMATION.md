---
title: "Test Automation Framework for Recoloca.ai Platform"
doc_id: "TEST-AUTOMATION-RECOLOCA-AI"
version: "1.0"
last_updated: "2025-01-20"
status: "Active"
owner: "@QATeam"
tags: [automation, testing, ci-cd, quality-assurance, frameworks]
description: "Comprehensive test automation framework covering unit tests, integration tests, E2E tests, and continuous testing strategies for the Recoloca.ai platform."
---

# 🤖 Test Automation Framework - Recoloca.ai Platform

## 📋 Overview

This document outlines the comprehensive test automation strategy for the Recoloca.ai platform, covering automated testing frameworks, tools, best practices, and continuous integration workflows.

### Automation Goals

- **Fast Feedback**: Provide rapid feedback on code changes
- **Regression Prevention**: Catch regressions early in the development cycle
- **Quality Gates**: Enforce quality standards before deployment
- **Continuous Testing**: Enable continuous integration and deployment
- **Coverage**: Achieve comprehensive test coverage across all layers
- **Reliability**: Maintain stable and reliable test suites

---

## 🏗️ Test Automation Architecture

### Testing Pyramid

```mermaid
graph TD
    A["🔺 E2E Tests (10%)"] --> B["🔶 Integration Tests (20%)"] 
    B --> C["🔻 Unit Tests (70%)"]
    
    A1["Playwright/Cypress"] --> A
    B1["FastAPI TestClient"] --> B
    B2["React Testing Library"] --> B
    C1["pytest"] --> C
    C2["Jest"] --> C
```

### Test Categories

1. **Unit Tests (70%)**
   - Individual function/component testing
   - Fast execution (< 1 second per test)
   - High coverage (> 90%)

2. **Integration Tests (20%)**
   - API endpoint testing
   - Database integration
   - External service mocking

3. **End-to-End Tests (10%)**
   - Full user journey testing
   - Cross-browser compatibility
   - Critical path validation

---

## 🧪 Backend Test Automation

### pytest Configuration

```python
# pytest.ini
[tool:pytest]
minversion = 6.0
addopts = 
    --strict-markers
    --strict-config
    --verbose
    --tb=short
    --cov=src
    --cov-report=term-missing
    --cov-report=html:htmlcov
    --cov-report=xml
    --cov-fail-under=90
    --asyncio-mode=auto
    --durations=10
testpaths = tests
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
    external: Tests that require external services
    security: Security-related tests
    performance: Performance tests
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
```

### Test Fixtures and Utilities

```python
# tests/conftest.py
import pytest
import asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock

from src.main import app
from src.database.models import Base
from src.database.connection import get_db_session
from src.auth.service import AuthService
from src.config import get_settings

# Test database setup
@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_engine():
    """Create test database engine"""
    settings = get_settings()
    engine = create_async_engine(
        settings.test_database_url,
        echo=False,
        future=True
    )
    
    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # Cleanup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()

@pytest.fixture
async def db_session(test_engine):
    """Create test database session"""
    async_session = async_sessionmaker(
        test_engine, 
        expire_on_commit=False
    )
    
    async with async_session() as session:
        yield session
        await session.rollback()

@pytest.fixture
def override_get_db(db_session):
    """Override database dependency"""
    async def _override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db_session] = _override_get_db
    yield
    app.dependency_overrides.clear()

@pytest.fixture
async def async_client(override_get_db):
    """Create async HTTP client for testing"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture
def sync_client(override_get_db):
    """Create sync HTTP client for testing"""
    with TestClient(app) as client:
        yield client

# User fixtures
@pytest.fixture
async def test_user(db_session):
    """Create test user"""
    from src.users.models import User
    from src.auth.utils import hash_password
    
    user = User(
        email="test@example.com",
        password_hash=hash_password("testpassword123"),
        first_name="Test",
        last_name="User",
        is_active=True,
        is_verified=True
    )
    
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    
    return user

@pytest.fixture
async def authenticated_user(test_user, async_client):
    """Create authenticated user with token"""
    login_data = {
        "email": test_user.email,
        "password": "testpassword123"
    }
    
    response = await async_client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    
    token_data = response.json()
    access_token = token_data["access_token"]
    
    # Set authorization header for future requests
    async_client.headers.update({"Authorization": f"Bearer {access_token}"})
    
    return {
        "user": test_user,
        "token": access_token,
        "client": async_client
    }

# Mock fixtures
@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client"""
    mock_client = AsyncMock()
    mock_client.chat.completions.create.return_value = AsyncMock(
        choices=[
            AsyncMock(
                message=AsyncMock(
                    content="Mocked AI response"
                )
            )
        ]
    )
    return mock_client

@pytest.fixture
def mock_stripe_client():
    """Mock Stripe client"""
    mock_client = MagicMock()
    mock_client.PaymentIntent.create.return_value = {
        "id": "pi_test_123",
        "client_secret": "pi_test_123_secret",
        "status": "requires_payment_method"
    }
    return mock_client

@pytest.fixture
def mock_redis_cache():
    """Mock Redis cache"""
    cache_data = {}
    
    class MockRedis:
        async def get(self, key):
            return cache_data.get(key)
        
        async def set(self, key, value, ex=None):
            cache_data[key] = value
            return True
        
        async def delete(self, key):
            cache_data.pop(key, None)
            return True
    
    return MockRedis()
```

### Unit Test Examples

```python
# tests/unit/test_cv_analysis.py
import pytest
from unittest.mock import AsyncMock, patch
from src.cv_analysis.service import CVAnalysisService
from src.cv_analysis.models import CVAnalysis, AnalysisStatus
from src.cv_analysis.schemas import CVAnalysisCreate

class TestCVAnalysisService:
    
    @pytest.fixture
    def cv_analysis_service(self, db_session, mock_openai_client):
        return CVAnalysisService(
            db_session=db_session,
            ai_client=mock_openai_client
        )
    
    @pytest.mark.unit
    async def test_create_analysis(self, cv_analysis_service, test_user):
        """Test creating a new CV analysis"""
        analysis_data = CVAnalysisCreate(
            user_id=test_user.id,
            cv_content="Sample CV content",
            analysis_type="comprehensive"
        )
        
        analysis = await cv_analysis_service.create_analysis(analysis_data)
        
        assert analysis.user_id == test_user.id
        assert analysis.status == AnalysisStatus.PENDING
        assert analysis.cv_content == "Sample CV content"
    
    @pytest.mark.unit
    async def test_process_analysis_success(self, cv_analysis_service, test_user):
        """Test successful CV analysis processing"""
        # Create analysis
        analysis = CVAnalysis(
            user_id=test_user.id,
            cv_content="Sample CV content",
            status=AnalysisStatus.PENDING
        )
        
        # Mock AI response
        mock_ai_response = {
            "score": 85,
            "suggestions": [
                "Add more technical skills",
                "Improve work experience descriptions"
            ],
            "strengths": ["Good education background"],
            "weaknesses": ["Limited project experience"]
        }
        
        with patch.object(
            cv_analysis_service, 
            '_analyze_with_ai', 
            return_value=mock_ai_response
        ):
            result = await cv_analysis_service.process_analysis(analysis)
        
        assert result.status == AnalysisStatus.COMPLETED
        assert result.score == 85
        assert len(result.suggestions) == 2
    
    @pytest.mark.unit
    async def test_process_analysis_failure(self, cv_analysis_service, test_user):
        """Test CV analysis processing failure"""
        analysis = CVAnalysis(
            user_id=test_user.id,
            cv_content="Sample CV content",
            status=AnalysisStatus.PENDING
        )
        
        # Mock AI failure
        with patch.object(
            cv_analysis_service, 
            '_analyze_with_ai', 
            side_effect=Exception("AI service unavailable")
        ):
            result = await cv_analysis_service.process_analysis(analysis)
        
        assert result.status == AnalysisStatus.FAILED
        assert "AI service unavailable" in result.error_message
    
    @pytest.mark.unit
    async def test_get_user_analyses(self, cv_analysis_service, test_user, db_session):
        """Test retrieving user analyses"""
        # Create multiple analyses
        analyses = [
            CVAnalysis(
                user_id=test_user.id,
                cv_content=f"CV content {i}",
                status=AnalysisStatus.COMPLETED,
                score=80 + i
            )
            for i in range(3)
        ]
        
        for analysis in analyses:
            db_session.add(analysis)
        await db_session.commit()
        
        user_analyses = await cv_analysis_service.get_user_analyses(
            user_id=test_user.id,
            limit=10
        )
        
        assert len(user_analyses) == 3
        assert all(a.user_id == test_user.id for a in user_analyses)
    
    @pytest.mark.unit
    @pytest.mark.parametrize("cv_content,expected_score", [
        ("Excellent CV with 10 years experience", 90),
        ("Good CV with 5 years experience", 75),
        ("Basic CV with 1 year experience", 60),
    ])
    async def test_score_calculation(self, cv_analysis_service, cv_content, expected_score):
        """Test CV score calculation with different inputs"""
        with patch.object(
            cv_analysis_service,
            '_calculate_score',
            return_value=expected_score
        ):
            score = await cv_analysis_service._calculate_score(cv_content)
            assert score == expected_score
```

### Integration Test Examples

```python
# tests/integration/test_cv_analysis_api.py
import pytest
from httpx import AsyncClient
from src.cv_analysis.models import AnalysisStatus

class TestCVAnalysisAPI:
    
    @pytest.mark.integration
    async def test_upload_cv_endpoint(self, authenticated_user):
        """Test CV upload endpoint"""
        client = authenticated_user["client"]
        
        # Prepare file upload
        files = {
            "file": ("test_cv.pdf", b"PDF content", "application/pdf")
        }
        
        response = await client.post("/api/cv/upload", files=files)
        
        assert response.status_code == 201
        data = response.json()
        assert "analysis_id" in data
        assert data["status"] == "pending"
    
    @pytest.mark.integration
    async def test_get_analysis_results(self, authenticated_user, db_session):
        """Test getting analysis results"""
        from src.cv_analysis.models import CVAnalysis
        
        client = authenticated_user["client"]
        user = authenticated_user["user"]
        
        # Create completed analysis
        analysis = CVAnalysis(
            user_id=user.id,
            cv_content="Test CV content",
            status=AnalysisStatus.COMPLETED,
            score=85,
            suggestions=["Improve skills section"]
        )
        
        db_session.add(analysis)
        await db_session.commit()
        await db_session.refresh(analysis)
        
        response = await client.get(f"/api/cv/analysis/{analysis.id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == analysis.id
        assert data["score"] == 85
        assert len(data["suggestions"]) == 1
    
    @pytest.mark.integration
    async def test_list_user_analyses(self, authenticated_user, db_session):
        """Test listing user analyses"""
        from src.cv_analysis.models import CVAnalysis
        
        client = authenticated_user["client"]
        user = authenticated_user["user"]
        
        # Create multiple analyses
        analyses = [
            CVAnalysis(
                user_id=user.id,
                cv_content=f"CV content {i}",
                status=AnalysisStatus.COMPLETED,
                score=80 + i
            )
            for i in range(5)
        ]
        
        for analysis in analyses:
            db_session.add(analysis)
        await db_session.commit()
        
        response = await client.get("/api/cv/analyses")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["analyses"]) == 5
        assert data["total"] == 5
    
    @pytest.mark.integration
    async def test_unauthorized_access(self, async_client):
        """Test unauthorized access to protected endpoints"""
        response = await async_client.get("/api/cv/analyses")
        assert response.status_code == 401
    
    @pytest.mark.integration
    @pytest.mark.slow
    async def test_cv_analysis_workflow(self, authenticated_user, mock_openai_client):
        """Test complete CV analysis workflow"""
        client = authenticated_user["client"]
        
        # 1. Upload CV
        files = {
            "file": ("test_cv.pdf", b"Sample CV content", "application/pdf")
        }
        
        upload_response = await client.post("/api/cv/upload", files=files)
        assert upload_response.status_code == 201
        
        analysis_id = upload_response.json()["analysis_id"]
        
        # 2. Check analysis status (should be pending)
        status_response = await client.get(f"/api/cv/analysis/{analysis_id}")
        assert status_response.status_code == 200
        assert status_response.json()["status"] == "pending"
        
        # 3. Trigger analysis processing (in real scenario, this would be async)
        process_response = await client.post(f"/api/cv/analysis/{analysis_id}/process")
        assert process_response.status_code == 200
        
        # 4. Check completed analysis
        final_response = await client.get(f"/api/cv/analysis/{analysis_id}")
        assert final_response.status_code == 200
        
        final_data = final_response.json()
        assert final_data["status"] == "completed"
        assert "score" in final_data
        assert "suggestions" in final_data
```

---

## 🎭 Frontend Test Automation

### Jest Configuration

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/test/setup.ts'],
  testMatch: [
    '<rootDir>/src/**/__tests__/**/*.{js,jsx,ts,tsx}',
    '<rootDir>/src/**/*.{test,spec}.{js,jsx,ts,tsx}'
  ],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$': '<rootDir>/src/test/__mocks__/fileMock.js'
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/test/**',
    '!src/stories/**',
    '!src/pages/_app.tsx',
    '!src/pages/_document.tsx'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': ['babel-jest', { presets: ['next/babel'] }]
  },
  testTimeout: 10000
};
```

### Test Setup and Utilities

```typescript
// src/test/setup.ts
import '@testing-library/jest-dom';
import { configure } from '@testing-library/react';
import { server } from './mocks/server';

// Configure testing library
configure({ testIdAttribute: 'data-testid' });

// Setup MSW
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

// Mock Next.js router
jest.mock('next/router', () => ({
  useRouter() {
    return {
      route: '/',
      pathname: '/',
      query: {},
      asPath: '/',
      push: jest.fn(),
      replace: jest.fn(),
      reload: jest.fn(),
      back: jest.fn(),
      prefetch: jest.fn().mockResolvedValue(undefined),
      beforePopState: jest.fn(),
      events: {
        on: jest.fn(),
        off: jest.fn(),
        emit: jest.fn(),
      },
    };
  },
}));

// Mock window.matchMedia
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});

// Mock IntersectionObserver
global.IntersectionObserver = class IntersectionObserver {
  constructor() {}
  observe() { return null; }
  disconnect() { return null; }
  unobserve() { return null; }
};
```

### MSW Mock Handlers

```typescript
// src/test/mocks/handlers.ts
import { rest } from 'msw';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const handlers = [
  // Auth endpoints
  rest.post(`${API_BASE_URL}/auth/login`, (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({
        access_token: 'mock-jwt-token',
        token_type: 'bearer',
        expires_in: 3600
      })
    );
  }),

  rest.get(`${API_BASE_URL}/auth/me`, (req, res, ctx) => {
    const authHeader = req.headers.get('Authorization');
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res(ctx.status(401), ctx.json({ detail: 'Unauthorized' }));
    }

    return res(
      ctx.status(200),
      ctx.json({
        id: 1,
        email: 'test@example.com',
        first_name: 'Test',
        last_name: 'User',
        is_active: true
      })
    );
  }),

  // CV Analysis endpoints
  rest.post(`${API_BASE_URL}/api/cv/upload`, (req, res, ctx) => {
    return res(
      ctx.status(201),
      ctx.json({
        analysis_id: 'mock-analysis-id',
        status: 'pending',
        message: 'CV uploaded successfully'
      })
    );
  }),

  rest.get(`${API_BASE_URL}/api/cv/analysis/:id`, (req, res, ctx) => {
    const { id } = req.params;
    
    return res(
      ctx.status(200),
      ctx.json({
        id,
        status: 'completed',
        score: 85,
        suggestions: [
          'Add more technical skills',
          'Improve work experience descriptions'
        ],
        created_at: '2025-01-20T10:00:00Z'
      })
    );
  }),

  rest.get(`${API_BASE_URL}/api/cv/analyses`, (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({
        analyses: [
          {
            id: '1',
            status: 'completed',
            score: 85,
            created_at: '2025-01-20T10:00:00Z'
          },
          {
            id: '2',
            status: 'completed',
            score: 78,
            created_at: '2025-01-19T15:30:00Z'
          }
        ],
        total: 2,
        page: 1,
        per_page: 10
      })
    );
  }),

  // AI Coach endpoints
  rest.post(`${API_BASE_URL}/api/ai-coach/session`, (req, res, ctx) => {
    return res(
      ctx.status(201),
      ctx.json({
        session_id: 'mock-session-id',
        status: 'active'
      })
    );
  }),

  rest.post(`${API_BASE_URL}/api/ai-coach/session/:sessionId/message`, (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({
        message_id: 'mock-message-id',
        response: 'This is a mock AI response for testing purposes.',
        timestamp: new Date().toISOString()
      })
    );
  }),

  // Error handlers
  rest.get(`${API_BASE_URL}/api/error`, (req, res, ctx) => {
    return res(
      ctx.status(500),
      ctx.json({ detail: 'Internal server error' })
    );
  })
];
```

### React Component Tests

```typescript
// src/components/__tests__/CVAnalysisResults.test.tsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import CVAnalysisResults from '../CVAnalysisResults';

// Test wrapper with providers
const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false },
    },
  });

  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('CVAnalysisResults', () => {
  const mockAnalysis = {
    id: '1',
    status: 'completed' as const,
    score: 85,
    suggestions: [
      'Add more technical skills',
      'Improve work experience descriptions'
    ],
    strengths: ['Good education background'],
    weaknesses: ['Limited project experience'],
    created_at: '2025-01-20T10:00:00Z'
  };

  it('renders analysis results correctly', () => {
    render(
      <CVAnalysisResults analysis={mockAnalysis} />,
      { wrapper: createWrapper() }
    );

    expect(screen.getByText('CV Analysis Results')).toBeInTheDocument();
    expect(screen.getByText('Score: 85/100')).toBeInTheDocument();
    expect(screen.getByText('Add more technical skills')).toBeInTheDocument();
    expect(screen.getByText('Improve work experience descriptions')).toBeInTheDocument();
  });

  it('displays loading state when analysis is pending', () => {
    const pendingAnalysis = { ...mockAnalysis, status: 'pending' as const };
    
    render(
      <CVAnalysisResults analysis={pendingAnalysis} />,
      { wrapper: createWrapper() }
    );

    expect(screen.getByText('Analysis in progress...')).toBeInTheDocument();
    expect(screen.getByRole('progressbar')).toBeInTheDocument();
  });

  it('handles error state correctly', () => {
    const errorAnalysis = { 
      ...mockAnalysis, 
      status: 'failed' as const,
      error_message: 'Analysis failed due to invalid file format'
    };
    
    render(
      <CVAnalysisResults analysis={errorAnalysis} />,
      { wrapper: createWrapper() }
    );

    expect(screen.getByText('Analysis Failed')).toBeInTheDocument();
    expect(screen.getByText('Analysis failed due to invalid file format')).toBeInTheDocument();
  });

  it('allows user to download analysis report', async () => {
    const user = userEvent.setup();
    
    // Mock URL.createObjectURL
    global.URL.createObjectURL = jest.fn(() => 'mock-blob-url');
    global.URL.revokeObjectURL = jest.fn();
    
    render(
      <CVAnalysisResults analysis={mockAnalysis} />,
      { wrapper: createWrapper() }
    );

    const downloadButton = screen.getByRole('button', { name: /download report/i });
    await user.click(downloadButton);

    expect(global.URL.createObjectURL).toHaveBeenCalled();
  });

  it('expands and collapses suggestion details', async () => {
    const user = userEvent.setup();
    
    render(
      <CVAnalysisResults analysis={mockAnalysis} />,
      { wrapper: createWrapper() }
    );

    const expandButton = screen.getByRole('button', { name: /show details/i });
    await user.click(expandButton);

    expect(screen.getByText('Strengths')).toBeInTheDocument();
    expect(screen.getByText('Areas for Improvement')).toBeInTheDocument();

    await user.click(expandButton);
    expect(screen.queryByText('Strengths')).not.toBeInTheDocument();
  });
});
```

### Custom Hooks Tests

```typescript
// src/hooks/__tests__/useAuth.test.ts
import { renderHook, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useAuth } from '../useAuth';
import { AuthProvider } from '../../contexts/AuthContext';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false },
    },
  });

  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        {children}
      </AuthProvider>
    </QueryClientProvider>
  );
};

describe('useAuth', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('returns initial unauthenticated state', () => {
    const { result } = renderHook(() => useAuth(), {
      wrapper: createWrapper(),
    });

    expect(result.current.isAuthenticated).toBe(false);
    expect(result.current.user).toBeNull();
    expect(result.current.isLoading).toBe(true);
  });

  it('handles successful login', async () => {
    const { result } = renderHook(() => useAuth(), {
      wrapper: createWrapper(),
    });

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    // Simulate login
    await result.current.login('test@example.com', 'password123');

    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(true);
      expect(result.current.user).toEqual({
        id: 1,
        email: 'test@example.com',
        first_name: 'Test',
        last_name: 'User',
        is_active: true
      });
    });
  });

  it('handles logout correctly', async () => {
    const { result } = renderHook(() => useAuth(), {
      wrapper: createWrapper(),
    });

    // First login
    await result.current.login('test@example.com', 'password123');
    
    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(true);
    });

    // Then logout
    result.current.logout();

    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(false);
      expect(result.current.user).toBeNull();
    });
  });

  it('persists authentication state on page reload', async () => {
    // Set token in localStorage
    localStorage.setItem('access_token', 'mock-jwt-token');

    const { result } = renderHook(() => useAuth(), {
      wrapper: createWrapper(),
    });

    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(true);
      expect(result.current.user).toBeTruthy();
    });
  });
});
```

---

## 🎪 End-to-End Test Automation

### Playwright Configuration

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html'],
    ['json', { outputFile: 'test-results/results.json' }],
    ['junit', { outputFile: 'test-results/results.xml' }]
  ],
  use: {
    baseURL: process.env.E2E_BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

### E2E Test Examples

```typescript
// e2e/cv-analysis-flow.spec.ts
import { test, expect } from '@playwright/test';
import path from 'path';

test.describe('CV Analysis Flow', () => {
  test.beforeEach(async ({ page }) => {
    // Login before each test
    await page.goto('/login');
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    await page.fill('[data-testid="password-input"]', 'password123');
    await page.click('[data-testid="login-button"]');
    
    // Wait for redirect to dashboard
    await expect(page).toHaveURL('/dashboard');
  });

  test('should complete full CV analysis workflow', async ({ page }) => {
    // Navigate to CV upload page
    await page.click('[data-testid="upload-cv-button"]');
    await expect(page).toHaveURL('/cv/upload');

    // Upload CV file
    const fileInput = page.locator('[data-testid="cv-file-input"]');
    const filePath = path.join(__dirname, 'fixtures', 'sample-cv.pdf');
    await fileInput.setInputFiles(filePath);

    // Submit upload
    await page.click('[data-testid="upload-submit-button"]');

    // Wait for upload success message
    await expect(page.locator('[data-testid="upload-success-message"]')).toBeVisible();

    // Navigate to analysis results
    await page.click('[data-testid="view-analysis-button"]');

    // Wait for analysis to complete (with timeout)
    await expect(page.locator('[data-testid="analysis-score"]')).toBeVisible({ timeout: 30000 });

    // Verify analysis results are displayed
    const score = await page.locator('[data-testid="analysis-score"]').textContent();
    expect(score).toMatch(/\d+\/100/);

    // Check suggestions are present
    const suggestions = page.locator('[data-testid="suggestion-item"]');
    await expect(suggestions).toHaveCount.greaterThan(0);

    // Download analysis report
    const downloadPromise = page.waitForDownload();
    await page.click('[data-testid="download-report-button"]');
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toContain('cv-analysis-report');
  });

  test('should handle file upload errors gracefully', async ({ page }) => {
    await page.goto('/cv/upload');

    // Try to upload invalid file type
    const fileInput = page.locator('[data-testid="cv-file-input"]');
    const filePath = path.join(__dirname, 'fixtures', 'invalid-file.txt');
    await fileInput.setInputFiles(filePath);

    await page.click('[data-testid="upload-submit-button"]');

    // Verify error message is displayed
    await expect(page.locator('[data-testid="upload-error-message"]')).toBeVisible();
    await expect(page.locator('[data-testid="upload-error-message"]'))
      .toContainText('Please upload a valid PDF or Word document');
  });

  test('should display analysis history', async ({ page }) => {
    await page.goto('/cv/history');

    // Wait for analyses to load
    await expect(page.locator('[data-testid="analysis-list"]')).toBeVisible();

    // Check that analyses are displayed
    const analysisItems = page.locator('[data-testid="analysis-item"]');
    await expect(analysisItems).toHaveCount.greaterThan(0);

    // Click on first analysis
    await analysisItems.first().click();

    // Verify navigation to analysis details
    await expect(page).toHaveURL(/\/cv\/analysis\/\w+/);
    await expect(page.locator('[data-testid="analysis-details"]')).toBeVisible();
  });
});
```

### Page Object Model

```typescript
// e2e/pages/LoginPage.ts
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;
  readonly forgotPasswordLink: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.locator('[data-testid="email-input"]');
    this.passwordInput = page.locator('[data-testid="password-input"]');
    this.loginButton = page.locator('[data-testid="login-button"]');
    this.errorMessage = page.locator('[data-testid="error-message"]');
    this.forgotPasswordLink = page.locator('[data-testid="forgot-password-link"]');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async getErrorMessage() {
    return await this.errorMessage.textContent();
  }

  async clickForgotPassword() {
    await this.forgotPasswordLink.click();
  }
}

// e2e/pages/CVUploadPage.ts
export class CVUploadPage {
  readonly page: Page;
  readonly fileInput: Locator;
  readonly uploadButton: Locator;
  readonly progressBar: Locator;
  readonly successMessage: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.fileInput = page.locator('[data-testid="cv-file-input"]');
    this.uploadButton = page.locator('[data-testid="upload-submit-button"]');
    this.progressBar = page.locator('[data-testid="upload-progress"]');
    this.successMessage = page.locator('[data-testid="upload-success-message"]');
    this.errorMessage = page.locator('[data-testid="upload-error-message"]');
  }

  async goto() {
    await this.page.goto('/cv/upload');
  }

  async uploadFile(filePath: string) {
    await this.fileInput.setInputFiles(filePath);
    await this.uploadButton.click();
  }

  async waitForUploadComplete() {
    await this.successMessage.waitFor({ state: 'visible', timeout: 30000 });
  }

  async getUploadError() {
    return await this.errorMessage.textContent();
  }
}
```

---

## 🔄 CI/CD Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/test-automation.yml
name: Test Automation

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

env:
  NODE_VERSION: '18'
  PYTHON_VERSION: '3.11'

jobs:
  unit-tests-backend:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}
    
    - name: Cache Python dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-test.txt
    
    - name: Run unit tests
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        REDIS_URL: redis://localhost:6379/0
        SECRET_KEY: test-secret-key
      run: |
        pytest tests/unit/ -v --cov=src --cov-report=xml --cov-report=term-missing
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: backend-unit
        name: backend-unit-tests

  integration-tests-backend:
    runs-on: ubuntu-latest
    needs: unit-tests-backend
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-test.txt
    
    - name: Run integration tests
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        REDIS_URL: redis://localhost:6379/0
        SECRET_KEY: test-secret-key
      run: |
        pytest tests/integration/ -v --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: backend-integration
        name: backend-integration-tests

  unit-tests-frontend:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run unit tests
      run: npm run test:unit -- --coverage --watchAll=false
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage/lcov.info
        flags: frontend-unit
        name: frontend-unit-tests

  e2e-tests:
    runs-on: ubuntu-latest
    needs: [integration-tests-backend, unit-tests-frontend]
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}
    
    - name: Install dependencies
      run: |
        npm ci
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Install Playwright browsers
      run: npx playwright install --with-deps
    
    - name: Start services
      run: |
        # Start backend
        uvicorn main:app --host 0.0.0.0 --port 8000 &
        
        # Start frontend
        npm run build
        npm start &
        
        # Wait for services to be ready
        sleep 30
    
    - name: Run E2E tests
      run: npx playwright test
    
    - name: Upload Playwright report
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: playwright-report
        path: playwright-report/
        retention-days: 30

  test-summary:
    runs-on: ubuntu-latest
    needs: [unit-tests-backend, integration-tests-backend, unit-tests-frontend, e2e-tests]
    if: always()
    
    steps:
    - name: Test Summary
      run: |
        echo "## Test Results Summary" >> $GITHUB_STEP_SUMMARY
        echo "| Test Suite | Status |" >> $GITHUB_STEP_SUMMARY
        echo "|------------|--------|" >> $GITHUB_STEP_SUMMARY
        echo "| Backend Unit Tests | ${{ needs.unit-tests-backend.result }} |" >> $GITHUB_STEP_SUMMARY
        echo "| Backend Integration Tests | ${{ needs.integration-tests-backend.result }} |" >> $GITHUB_STEP_SUMMARY
        echo "| Frontend Unit Tests | ${{ needs.unit-tests-frontend.result }} |" >> $GITHUB_STEP_SUMMARY
        echo "| E2E Tests | ${{ needs.e2e-tests.result }} |" >> $GITHUB_STEP_SUMMARY
```

### Test Reporting and Metrics

```python
# scripts/test_reporter.py
import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Any
from pathlib import Path
import requests

class TestReporter:
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.results = {
            'backend_unit': {},
            'backend_integration': {},
            'frontend_unit': {},
            'e2e': {}
        }
    
    def parse_pytest_xml(self, xml_file: Path) -> Dict[str, Any]:
        """Parse pytest XML results"""
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        total_tests = int(root.get('tests', 0))
        failures = int(root.get('failures', 0))
        errors = int(root.get('errors', 0))
        skipped = int(root.get('skipped', 0))
        time = float(root.get('time', 0))
        
        return {
            'total': total_tests,
            'passed': total_tests - failures - errors - skipped,
            'failed': failures + errors,
            'skipped': skipped,
            'duration': time,
            'success_rate': ((total_tests - failures - errors) / total_tests * 100) if total_tests > 0 else 0
        }
    
    def parse_jest_json(self, json_file: Path) -> Dict[str, Any]:
        """Parse Jest JSON results"""
        with open(json_file) as f:
            data = json.load(f)
        
        return {
            'total': data['numTotalTests'],
            'passed': data['numPassedTests'],
            'failed': data['numFailedTests'],
            'skipped': data['numPendingTests'],
            'duration': data['testResults'][0]['perfStats']['end'] - data['testResults'][0]['perfStats']['start'],
            'success_rate': (data['numPassedTests'] / data['numTotalTests'] * 100) if data['numTotalTests'] > 0 else 0
        }
    
    def parse_playwright_json(self, json_file: Path) -> Dict[str, Any]:
        """Parse Playwright JSON results"""
        with open(json_file) as f:
            data = json.load(f)
        
        total_tests = len(data['suites'][0]['specs'])
        passed_tests = sum(1 for spec in data['suites'][0]['specs'] if spec['ok'])
        
        return {
            'total': total_tests,
            'passed': passed_tests,
            'failed': total_tests - passed_tests,
            'skipped': 0,
            'duration': data['stats']['duration'],
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0
        }
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive test report"""
        # Parse all test results
        if Path('test-results/backend-unit.xml').exists():
            self.results['backend_unit'] = self.parse_pytest_xml(Path('test-results/backend-unit.xml'))
        
        if Path('test-results/backend-integration.xml').exists():
            self.results['backend_integration'] = self.parse_pytest_xml(Path('test-results/backend-integration.xml'))
        
        if Path('test-results/frontend-unit.json').exists():
            self.results['frontend_unit'] = self.parse_jest_json(Path('test-results/frontend-unit.json'))
        
        if Path('test-results/e2e-results.json').exists():
            self.results['e2e'] = self.parse_playwright_json(Path('test-results/e2e-results.json'))
        
        # Calculate overall metrics
        total_tests = sum(result.get('total', 0) for result in self.results.values())
        total_passed = sum(result.get('passed', 0) for result in self.results.values())
        total_failed = sum(result.get('failed', 0) for result in self.results.values())
        total_duration = sum(result.get('duration', 0) for result in self.results.values())
        
        overall_success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        return {
            'project': self.project_name,
            'timestamp': datetime.utcnow().isoformat(),
            'overall': {
                'total_tests': total_tests,
                'passed': total_passed,
                'failed': total_failed,
                'success_rate': overall_success_rate,
                'total_duration': total_duration
            },
            'by_suite': self.results,
            'quality_gates': {
                'min_success_rate': 95,
                'max_duration': 300,  # 5 minutes
                'passed': overall_success_rate >= 95 and total_duration <= 300
            }
        }
    
    def send_to_slack(self, webhook_url: str, report: Dict[str, Any]):
        """Send test report to Slack"""
        overall = report['overall']
        quality_passed = report['quality_gates']['passed']
        
        color = 'good' if quality_passed else 'danger'
        status_emoji = '✅' if quality_passed else '❌'
        
        message = {
            'attachments': [{
                'color': color,
                'title': f'{status_emoji} Test Results - {self.project_name}',
                'fields': [
                    {
                        'title': 'Overall Success Rate',
                        'value': f"{overall['success_rate']:.1f}%",
                        'short': True
                    },
                    {
                        'title': 'Total Tests',
                        'value': str(overall['total_tests']),
                        'short': True
                    },
                    {
                        'title': 'Passed',
                        'value': str(overall['passed']),
                        'short': True
                    },
                    {
                        'title': 'Failed',
                        'value': str(overall['failed']),
                        'short': True
                    }
                ],
                'footer': f"Duration: {overall['total_duration']:.1f}s"
            }]
        }
        
        requests.post(webhook_url, json=message)

# Usage
if __name__ == '__main__':
    reporter = TestReporter('Recoloca.ai')
    report = reporter.generate_report()
    
    # Save report
    with open('test-report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    # Send to Slack if webhook URL is provided
    slack_webhook = os.getenv('SLACK_WEBHOOK_URL')
    if slack_webhook:
        reporter.send_to_slack(slack_webhook, report)
    
    print(f"Test report generated: {report['overall']['success_rate']:.1f}% success rate")
```

---

## 📚 Related Documents

- [Testing Strategy](./01_TESTING_STRATEGY.md)
- [Code Review Checklist](./02_CODE_REVIEW_CHECKLIST.md)
- [Performance Optimization](./04_PERFORMANCE_OPTIMIZATION.md)
- [CI/CD Pipeline](../04_DEVOPS_AND_INFRASTRUCTURE/02_CI_CD_PIPELINE.md)
- [API Specifications](../03_SPECIFICATIONS_AND_CONTRACTS/01_API_SPECIFICATIONS.md)

---

**Document Information:**
- **Created**: 2025-01-20
- **Last Updated**: 2025-01-20
- **Version**: 1.0
- **Status**: Active
- **Owner**: @QATeam