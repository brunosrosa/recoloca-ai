---
title: "Style Guide - Standards and Patterns"
doc_id: "STYLE-GUIDE-STANDARDS-PATTERNS"
version: "1.0"
last_updated: "2025-01-20 15:30:00"
timezone: "America/Sao_Paulo"
status: "Active"
owner: "@DevelopmentTeam"
tags: [style-guide, standards, patterns, code-quality, best-practices]
description: "Comprehensive style guide defining coding standards, naming conventions, and architectural patterns for the Recoloca.ai project."
---

# Style Guide - Standards and Patterns

## 📋 Overview

This document establishes the coding standards, naming conventions, and architectural patterns for the **Recoloca.ai** project. Adherence to these guidelines ensures code consistency, maintainability, and team collaboration efficiency.

## 🎯 Objectives

- **Consistency**: Uniform code style across all team members
- **Readability**: Clear and self-documenting code
- **Maintainability**: Easy to understand and modify code
- **Quality**: Reduced bugs and improved code reliability
- **Collaboration**: Smooth team development workflow

---

## 🐍 Python Standards

### Code Formatting

#### Formatter: Black
```bash
# Install Black
pip install black

# Format code
black .

# Check formatting
black --check .
```

#### Configuration (.pyproject.toml)
```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  migrations
  | venv
  | .venv
)/
'''
```

### Import Organization

```python
# 1. Standard library imports
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# 2. Third-party imports
import fastapi
import pydantic
from sqlalchemy import Column, Integer, String

# 3. Local application imports
from app.core.config import settings
from app.models.user import User
from app.services.auth import AuthService
```

### Naming Conventions

#### Variables and Functions
```python
# Use snake_case for variables and functions
user_name = "john_doe"
max_retry_count = 3

def calculate_cv_score(cv_content: str) -> float:
    """Calculate CV score based on content analysis."""
    pass

def get_user_by_id(user_id: int) -> Optional[User]:
    """Retrieve user by ID from database."""
    pass
```

#### Classes
```python
# Use PascalCase for classes
class UserService:
    """Service for user-related operations."""
    pass

class CVAnalysisResult:
    """Result of CV analysis operation."""
    pass

class PaymentProcessor:
    """Handles payment processing logic."""
    pass
```

#### Constants
```python
# Use UPPER_SNAKE_CASE for constants
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
DEFAULT_TIMEOUT = 30
API_VERSION = "v1"
SUPPORTED_FILE_TYPES = [".pdf", ".doc", ".docx"]
```

#### Private Members
```python
class UserService:
    def __init__(self):
        self._db_connection = None  # Protected member
        self.__secret_key = "..."   # Private member
    
    def _validate_user_data(self, data: dict) -> bool:
        """Protected method for internal validation."""
        pass
    
    def __encrypt_password(self, password: str) -> str:
        """Private method for password encryption."""
        pass
```

### Type Hints

```python
from typing import Dict, List, Optional, Union, Any
from pydantic import BaseModel

# Always use type hints for function parameters and return values
def process_cv_analysis(
    cv_content: str,
    user_id: int,
    options: Optional[Dict[str, Any]] = None
) -> CVAnalysisResult:
    """Process CV analysis with type safety."""
    pass

# Use Pydantic models for data validation
class UserCreateRequest(BaseModel):
    email: str
    password: str
    full_name: str
    phone: Optional[str] = None
```

### Documentation

#### Docstring Format (Google Style)
```python
def analyze_cv_content(
    cv_text: str,
    analysis_type: str = "comprehensive"
) -> CVAnalysisResult:
    """
    Analyze CV content using AI-powered analysis.
    
    Args:
        cv_text: The extracted text content from CV
        analysis_type: Type of analysis to perform (comprehensive, quick, detailed)
        
    Returns:
        CVAnalysisResult containing analysis results and recommendations
        
    Raises:
        ValueError: If cv_text is empty or invalid
        AnalysisError: If AI analysis fails
        
    Example:
        >>> result = analyze_cv_content("John Doe Software Engineer...")
        >>> print(result.score)
        85.5
    """
    pass
```

### Error Handling

```python
# Use specific exception types
class CVAnalysisError(Exception):
    """Base exception for CV analysis operations."""
    pass

class InvalidCVFormatError(CVAnalysisError):
    """Raised when CV format is not supported."""
    pass

# Proper exception handling
def process_cv_upload(file_path: str) -> CVAnalysisResult:
    try:
        cv_content = extract_cv_content(file_path)
        return analyze_cv_content(cv_content)
    except FileNotFoundError:
        logger.error(f"CV file not found: {file_path}")
        raise InvalidCVFormatError(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"Unexpected error processing CV: {e}")
        raise CVAnalysisError(f"Failed to process CV: {e}")
```

---

## 🌐 TypeScript/JavaScript Standards

### Code Formatting

#### Formatter: Prettier
```json
// .prettierrc
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}
```

#### ESLint Configuration
```json
// .eslintrc.json
{
  "extends": [
    "@next/next/recommended",
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "prefer-const": "error",
    "no-var": "error"
  }
}
```

### Naming Conventions

#### Variables and Functions
```typescript
// Use camelCase for variables and functions
const userName = 'john_doe';
const maxRetryCount = 3;

function calculateCvScore(cvContent: string): number {
  // Implementation
  return 0;
}

const getUserById = async (userId: number): Promise<User | null> => {
  // Implementation
  return null;
};
```

#### Interfaces and Types
```typescript
// Use PascalCase for interfaces and types
interface UserProfile {
  id: number;
  email: string;
  fullName: string;
  createdAt: Date;
}

type CVAnalysisStatus = 'pending' | 'processing' | 'completed' | 'failed';

interface CVAnalysisResult {
  score: number;
  recommendations: string[];
  status: CVAnalysisStatus;
}
```

#### Constants
```typescript
// Use UPPER_SNAKE_CASE for constants
const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
const DEFAULT_TIMEOUT = 30000;
const API_BASE_URL = '/api/v1';
const SUPPORTED_FILE_TYPES = ['.pdf', '.doc', '.docx'] as const;
```

### Component Structure (React)

```typescript
// components/CVAnalysisCard.tsx
import React, { useState, useEffect } from 'react';
import { Card, Button, Progress } from '@/components/ui';
import { CVAnalysisResult } from '@/types/cv';

interface CVAnalysisCardProps {
  analysisResult: CVAnalysisResult;
  onRetry?: () => void;
  className?: string;
}

export const CVAnalysisCard: React.FC<CVAnalysisCardProps> = ({
  analysisResult,
  onRetry,
  className,
}) => {
  const [isExpanded, setIsExpanded] = useState(false);

  useEffect(() => {
    // Component logic
  }, [analysisResult]);

  const handleExpand = (): void => {
    setIsExpanded(!isExpanded);
  };

  return (
    <Card className={className}>
      {/* Component JSX */}
    </Card>
  );
};

export default CVAnalysisCard;
```

### API Client Structure

```typescript
// services/api/cvAnalysis.ts
import { ApiClient } from './base';
import { CVAnalysisRequest, CVAnalysisResult } from '@/types/cv';

export class CVAnalysisService extends ApiClient {
  async analyzeCv(request: CVAnalysisRequest): Promise<CVAnalysisResult> {
    return this.post<CVAnalysisResult>('/cv/analyze', request);
  }

  async getCvAnalysis(analysisId: string): Promise<CVAnalysisResult> {
    return this.get<CVAnalysisResult>(`/cv/analysis/${analysisId}`);
  }

  async getCvAnalysisHistory(userId: number): Promise<CVAnalysisResult[]> {
    return this.get<CVAnalysisResult[]>(`/cv/analysis/history/${userId}`);
  }
}

export const cvAnalysisService = new CVAnalysisService();
```

---

## 🗄️ Database Standards

### Table Naming
```sql
-- Use snake_case for table names (plural)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cv_analyses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    file_path VARCHAR(500) NOT NULL,
    analysis_result JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Column Naming
```sql
-- Use snake_case for column names
-- Use descriptive names
-- Include units in names when applicable
CREATE TABLE subscription_plans (
    id SERIAL PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    price_cents INTEGER NOT NULL,  -- Price in cents
    billing_cycle_days INTEGER NOT NULL,  -- Billing cycle in days
    max_cv_analyses_per_month INTEGER,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Index Naming
```sql
-- Format: idx_{table}_{column(s)}_{type}
CREATE INDEX idx_users_email_unique ON users(email);
CREATE INDEX idx_cv_analyses_user_id ON cv_analyses(user_id);
CREATE INDEX idx_cv_analyses_created_at ON cv_analyses(created_at);
```

---

## 📁 File and Directory Structure

### Project Structure
```
recoloca-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── users.py
│   │   │   │   │   └── cv_analysis.py
│   │   │   │   └── api.py
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── cv_analysis.py
│   │   │   └── base.py
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── cv_service.py
│   │   │   └── ai_service.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── ui/
    │   │   ├── forms/
    │   │   └── layout/
    │   ├── pages/
    │   ├── services/
    │   ├── types/
    │   ├── utils/
    │   └── hooks/
    ├── public/
    ├── package.json
    └── next.config.js
```

### File Naming Conventions

#### Python Files
```
# Use snake_case for Python files
user_service.py
cv_analysis_service.py
auth_middleware.py
test_user_service.py
```

#### TypeScript/JavaScript Files
```
# Use camelCase for TypeScript/JavaScript files
userService.ts
cvAnalysisService.ts
AuthProvider.tsx
UserProfile.component.tsx
```

#### Configuration Files
```
# Use kebab-case for configuration files
docker-compose.yml
.env.example
eslint.config.js
prettier.config.js
```

---

## 🔧 API Design Standards

### RESTful Endpoints

```
# Resource naming (plural nouns)
GET    /api/v1/users              # List users
POST   /api/v1/users              # Create user
GET    /api/v1/users/{id}         # Get user by ID
PUT    /api/v1/users/{id}         # Update user
DELETE /api/v1/users/{id}         # Delete user

# Nested resources
GET    /api/v1/users/{id}/cv-analyses     # Get user's CV analyses
POST   /api/v1/users/{id}/cv-analyses     # Create CV analysis for user

# Actions on resources
POST   /api/v1/cv-analyses/{id}/reanalyze # Reanalyze CV
POST   /api/v1/users/{id}/reset-password  # Reset user password
```

### Request/Response Format

```typescript
// Request format
interface CreateUserRequest {
  email: string;
  password: string;
  fullName: string;
  phone?: string;
}

// Response format
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: any;
  };
  meta?: {
    timestamp: string;
    requestId: string;
    pagination?: {
      page: number;
      limit: number;
      total: number;
    };
  };
}
```

### HTTP Status Codes

```
200 OK           - Successful GET, PUT, PATCH
201 Created      - Successful POST
204 No Content   - Successful DELETE
400 Bad Request  - Invalid request data
401 Unauthorized - Authentication required
403 Forbidden    - Insufficient permissions
404 Not Found    - Resource not found
409 Conflict     - Resource conflict
422 Unprocessable Entity - Validation errors
500 Internal Server Error - Server error
```

---

## 🧪 Testing Standards

### Test File Naming

```python
# Python tests
test_user_service.py
test_cv_analysis_service.py
test_auth_middleware.py
```

```typescript
// TypeScript tests
userService.test.ts
cvAnalysisService.test.ts
AuthProvider.test.tsx
```

### Test Structure

```python
# Python test structure
import pytest
from app.services.user_service import UserService
from app.models.user import User

class TestUserService:
    """Test suite for UserService."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.user_service = UserService()
    
    def test_create_user_success(self):
        """Test successful user creation."""
        # Arrange
        user_data = {
            "email": "test@example.com",
            "password": "secure_password",
            "full_name": "Test User"
        }
        
        # Act
        result = self.user_service.create_user(user_data)
        
        # Assert
        assert result.success is True
        assert result.data.email == user_data["email"]
    
    def test_create_user_duplicate_email(self):
        """Test user creation with duplicate email."""
        # Test implementation
        pass
```

---

## 📝 Documentation Standards

### README Structure

```markdown
# Project Name

## Overview
Brief description of the project

## Features
- Feature 1
- Feature 2

## Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+

## Installation
### Backend Setup
```bash
# Installation steps
```

### Frontend Setup
```bash
# Installation steps
```

## Usage
### Development
```bash
# Development commands
```

### Production
```bash
# Production commands
```

## API Documentation
Link to API documentation

## Contributing
Contribution guidelines

## License
License information
```

### Code Comments

```python
# Good comments explain WHY, not WHAT
def calculate_cv_score(cv_content: str) -> float:
    """
    Calculate CV score using weighted algorithm.
    
    We use a weighted scoring system because different sections
    of a CV have varying importance for job matching.
    """
    # Weight experience section higher for senior positions
    experience_weight = 0.4
    skills_weight = 0.3
    education_weight = 0.2
    other_weight = 0.1
    
    # Calculate individual section scores
    experience_score = analyze_experience_section(cv_content)
    skills_score = analyze_skills_section(cv_content)
    
    return (
        experience_score * experience_weight +
        skills_score * skills_weight +
        # ... other calculations
    )
```

---

## 🔍 Code Review Guidelines

### Review Checklist

#### Functionality
- [ ] Code works as intended
- [ ] Edge cases are handled
- [ ] Error handling is appropriate
- [ ] Performance considerations are addressed

#### Code Quality
- [ ] Code follows style guide
- [ ] Names are descriptive and clear
- [ ] Functions are focused and single-purpose
- [ ] Code is DRY (Don't Repeat Yourself)

#### Testing
- [ ] Tests are included for new functionality
- [ ] Tests cover edge cases
- [ ] Tests are clear and maintainable
- [ ] All tests pass

#### Documentation
- [ ] Code is self-documenting
- [ ] Complex logic is commented
- [ ] API changes are documented
- [ ] README is updated if needed

#### Security
- [ ] No sensitive data in code
- [ ] Input validation is present
- [ ] Authentication/authorization is correct
- [ ] SQL injection prevention

### Review Process

1. **Self Review**: Author reviews their own code first
2. **Peer Review**: At least one team member reviews
3. **Testing**: All tests must pass
4. **Approval**: Code is approved before merging
5. **Merge**: Code is merged to main branch

---

## 🚀 Deployment Standards

### Environment Variables

```bash
# Use descriptive names with prefixes
RECOLOCA_DATABASE_URL=postgresql://...
RECOLOCA_REDIS_URL=redis://...
RECOLOCA_SECRET_KEY=...
RECOLOCA_AI_API_KEY=...

# Use different prefixes for different environments
DEV_DATABASE_URL=...
STAGING_DATABASE_URL=...
PROD_DATABASE_URL=...
```

### Docker Standards

```dockerfile
# Use specific version tags
FROM python:3.11-slim

# Create non-root user
RUN useradd -m -u 1000 appuser

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change ownership and switch to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Start application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📊 Monitoring and Logging

### Logging Format

```python
import logging
import json
from datetime import datetime

# Structured logging format
class StructuredFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if hasattr(record, 'user_id'):
            log_entry['user_id'] = record.user_id
        
        if hasattr(record, 'request_id'):
            log_entry['request_id'] = record.request_id
            
        return json.dumps(log_entry)

# Usage
logger = logging.getLogger(__name__)
logger.info("User created successfully", extra={"user_id": 123})
```

### Metrics Collection

```python
from prometheus_client import Counter, Histogram, Gauge

# Define metrics
api_requests_total = Counter(
    'api_requests_total',
    'Total API requests',
    ['method', 'endpoint', 'status']
)

api_request_duration = Histogram(
    'api_request_duration_seconds',
    'API request duration',
    ['method', 'endpoint']
)

active_users = Gauge(
    'active_users_total',
    'Number of active users'
)

# Usage in code
api_requests_total.labels(method='POST', endpoint='/api/v1/users', status='201').inc()
api_request_duration.labels(method='POST', endpoint='/api/v1/users').observe(0.5)
```

---

## 🔗 Related Documents

- [[Best_Practices.md]] - Development Best Practices
- [[API_Documentation.md]] - API Specifications
- [[Security_Guidelines.md]] - Security Standards
- [[Testing_Strategy.md]] - Testing Guidelines
- [[Deployment_Guide.md]] - Deployment Procedures

---

**Document Status**: Active  
**Next Review Date**: 2025-03-20  
**Maintained By**: @DevelopmentTeam