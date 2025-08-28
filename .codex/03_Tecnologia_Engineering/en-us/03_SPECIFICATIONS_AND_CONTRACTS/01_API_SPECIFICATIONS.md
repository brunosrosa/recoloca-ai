---
title: "API Specifications - Recoloca.ai"
doc_id: "API-SPECIFICATIONS-RECOLOCA"
version: "1.0"
last_updated: "2025-01-20 15:35:00"
timezone: "America/Sao_Paulo"
status: "Active"
owner: "@BackendTeam"
tags: [api, specifications, rest, openapi, swagger, endpoints]
description: "Complete API specifications for the Recoloca.ai platform, including authentication, CV analysis, AI coaching, and payment endpoints."
---

# API Specifications - Recoloca.ai

## 📋 Overview

This document provides comprehensive API specifications for the **Recoloca.ai** platform. All APIs follow RESTful principles and use JSON for data exchange.

## 🔧 Base Configuration

### Base URL
```
Production:  https://api.recoloca.ai/v1
Staging:     https://staging-api.recoloca.ai/v1
Development: http://localhost:8000/api/v1
```

### Authentication
```http
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

### Common Headers
```http
Content-Type: application/json
Accept: application/json
X-Request-ID: <uuid>
X-Client-Version: <version>
```

---

## 🔐 Authentication Endpoints

### POST /auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!",
  "full_name": "John Doe",
  "phone": "+5511999999999"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": 123,
      "email": "user@example.com",
      "full_name": "John Doe",
      "phone": "+5511999999999",
      "is_verified": false,
      "created_at": "2025-01-20T15:30:00Z"
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 3600
  },
  "meta": {
    "timestamp": "2025-01-20T15:30:00Z",
    "request_id": "req_123456789"
  }
}
```

**Error Response (400 Bad Request):**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "email": ["Invalid email format"],
      "password": ["Password must be at least 8 characters"]
    }
  },
  "meta": {
    "timestamp": "2025-01-20T15:30:00Z",
    "request_id": "req_123456789"
  }
}
```

### POST /auth/login
Authenticate user and obtain access token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": 123,
      "email": "user@example.com",
      "full_name": "John Doe",
      "subscription_tier": "premium",
      "is_verified": true
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 3600
  }
}
```

### POST /auth/refresh
Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 3600
  }
}
```

### POST /auth/logout
Logout user and invalidate tokens.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (204 No Content)**

---

## 👤 User Management Endpoints

### GET /users/me
Get current user profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 123,
    "email": "user@example.com",
    "full_name": "John Doe",
    "phone": "+5511999999999",
    "subscription_tier": "premium",
    "subscription_status": "active",
    "cv_analyses_used": 5,
    "cv_analyses_limit": 50,
    "is_verified": true,
    "created_at": "2025-01-20T15:30:00Z",
    "updated_at": "2025-01-20T15:30:00Z"
  }
}
```

### PUT /users/me
Update current user profile.

**Request Body:**
```json
{
  "full_name": "John Smith",
  "phone": "+5511888888888"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 123,
    "email": "user@example.com",
    "full_name": "John Smith",
    "phone": "+5511888888888",
    "updated_at": "2025-01-20T16:00:00Z"
  }
}
```

### POST /users/me/change-password
Change user password.

**Request Body:**
```json
{
  "current_password": "OldPassword123!",
  "new_password": "NewSecurePassword456!"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "message": "Password changed successfully"
  }
}
```

---

## 📄 CV Analysis Endpoints

### POST /cv/upload
Upload CV file for analysis.

**Request (multipart/form-data):**
```
file: <cv_file.pdf>
analysis_type: "comprehensive" | "quick" | "detailed"
job_description: "Optional job description for targeted analysis"
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "analysis_id": "cv_analysis_456789",
    "status": "processing",
    "file_name": "john_doe_cv.pdf",
    "file_size": 1024000,
    "analysis_type": "comprehensive",
    "estimated_completion": "2025-01-20T15:35:00Z",
    "created_at": "2025-01-20T15:30:00Z"
  }
}
```

### GET /cv/analysis/{analysis_id}
Get CV analysis results.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "cv_analysis_456789",
    "status": "completed",
    "file_name": "john_doe_cv.pdf",
    "analysis_type": "comprehensive",
    "results": {
      "overall_score": 85.5,
      "sections": {
        "personal_info": {
          "score": 90,
          "feedback": "Complete and well-formatted contact information"
        },
        "experience": {
          "score": 88,
          "feedback": "Strong professional experience with clear progression",
          "years_of_experience": 8,
          "positions_count": 4
        },
        "skills": {
          "score": 82,
          "feedback": "Good technical skills, could benefit from more soft skills",
          "technical_skills": ["Python", "JavaScript", "React", "PostgreSQL"],
          "soft_skills": ["Leadership", "Communication"]
        },
        "education": {
          "score": 85,
          "feedback": "Relevant educational background",
          "degrees": [
            {
              "degree": "Bachelor of Computer Science",
              "institution": "University of São Paulo",
              "year": 2015
            }
          ]
        }
      },
      "recommendations": [
        {
          "category": "skills",
          "priority": "high",
          "suggestion": "Add more soft skills like project management and team collaboration"
        },
        {
          "category": "formatting",
          "priority": "medium",
          "suggestion": "Consider using bullet points for better readability"
        }
      ],
      "ats_compatibility": {
        "score": 78,
        "issues": [
          "Some formatting may not be ATS-friendly",
          "Consider using standard section headers"
        ]
      }
    },
    "created_at": "2025-01-20T15:30:00Z",
    "completed_at": "2025-01-20T15:32:00Z"
  }
}
```

### GET /cv/analysis/history
Get user's CV analysis history.

**Query Parameters:**
```
page: 1
limit: 10
status: "completed" | "processing" | "failed"
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": "cv_analysis_456789",
      "file_name": "john_doe_cv.pdf",
      "status": "completed",
      "overall_score": 85.5,
      "analysis_type": "comprehensive",
      "created_at": "2025-01-20T15:30:00Z",
      "completed_at": "2025-01-20T15:32:00Z"
    }
  ],
  "meta": {
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 25,
      "pages": 3
    }
  }
}
```

### POST /cv/analysis/{analysis_id}/optimize
Generate CV optimization suggestions.

**Request Body:**
```json
{
  "target_role": "Senior Software Engineer",
  "target_company": "Tech Startup",
  "focus_areas": ["technical_skills", "experience", "ats_optimization"]
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "optimization_id": "opt_789123",
    "suggestions": [
      {
        "section": "skills",
        "type": "addition",
        "priority": "high",
        "suggestion": "Add Docker and Kubernetes to technical skills",
        "reasoning": "These skills are commonly required for Senior Software Engineer roles"
      },
      {
        "section": "experience",
        "type": "enhancement",
        "priority": "medium",
        "suggestion": "Quantify achievements with specific metrics",
        "example": "Led team of 5 developers → Led team of 5 developers, increasing delivery speed by 40%"
      }
    ],
    "estimated_score_improvement": 8.5,
    "created_at": "2025-01-20T15:35:00Z"
  }
}
```

---

## 🤖 AI Coach Endpoints

### POST /coach/sessions
Start a new AI coaching session.

**Request Body:**
```json
{
  "topic": "interview_preparation",
  "context": {
    "target_role": "Senior Software Engineer",
    "interview_type": "technical",
    "company_info": "Tech startup focused on fintech"
  }
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "session_id": "coach_session_987654",
    "topic": "interview_preparation",
    "status": "active",
    "context": {
      "target_role": "Senior Software Engineer",
      "interview_type": "technical",
      "company_info": "Tech startup focused on fintech"
    },
    "created_at": "2025-01-20T15:40:00Z"
  }
}
```

### POST /coach/sessions/{session_id}/messages
Send message to AI coach.

**Request Body:**
```json
{
  "message": "I'm nervous about the technical interview. What should I focus on?",
  "message_type": "question"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "message_id": "msg_123456",
    "user_message": "I'm nervous about the technical interview. What should I focus on?",
    "ai_response": "It's natural to feel nervous! For a Senior Software Engineer technical interview at a fintech startup, I'd recommend focusing on: 1) System design fundamentals, 2) Data structures and algorithms, 3) Financial domain knowledge, 4) Scalability considerations. Would you like me to dive deeper into any of these areas?",
    "suggestions": [
      "Practice system design problems",
      "Review common algorithms",
      "Learn about financial systems"
    ],
    "created_at": "2025-01-20T15:41:00Z"
  }
}
```

### GET /coach/sessions/{session_id}/messages
Get coaching session message history.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "session_id": "coach_session_987654",
    "messages": [
      {
        "id": "msg_123456",
        "user_message": "I'm nervous about the technical interview. What should I focus on?",
        "ai_response": "It's natural to feel nervous! For a Senior Software Engineer...",
        "created_at": "2025-01-20T15:41:00Z"
      }
    ],
    "message_count": 1
  }
}
```

### GET /coach/sessions
Get user's coaching session history.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "session_id": "coach_session_987654",
      "topic": "interview_preparation",
      "status": "active",
      "message_count": 5,
      "created_at": "2025-01-20T15:40:00Z",
      "last_activity": "2025-01-20T15:45:00Z"
    }
  ]
}
```

---

## 💳 Payment Endpoints

### GET /payments/plans
Get available subscription plans.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": "plan_basic",
      "name": "Basic",
      "description": "Perfect for job seekers starting their journey",
      "price_cents": 2990,
      "currency": "BRL",
      "billing_cycle": "monthly",
      "features": {
        "cv_analyses_per_month": 5,
        "ai_coach_sessions": 10,
        "optimization_suggestions": true,
        "ats_compatibility_check": true,
        "priority_support": false
      },
      "is_popular": false
    },
    {
      "id": "plan_premium",
      "name": "Premium",
      "description": "For serious professionals seeking career advancement",
      "price_cents": 4990,
      "currency": "BRL",
      "billing_cycle": "monthly",
      "features": {
        "cv_analyses_per_month": 20,
        "ai_coach_sessions": 50,
        "optimization_suggestions": true,
        "ats_compatibility_check": true,
        "priority_support": true,
        "interview_simulation": true,
        "salary_insights": true
      },
      "is_popular": true
    }
  ]
}
```

### POST /payments/subscriptions
Create new subscription.

**Request Body:**
```json
{
  "plan_id": "plan_premium",
  "payment_method_id": "pm_1234567890",
  "billing_cycle": "monthly"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "subscription_id": "sub_abc123",
    "plan_id": "plan_premium",
    "status": "active",
    "current_period_start": "2025-01-20T15:50:00Z",
    "current_period_end": "2025-02-20T15:50:00Z",
    "next_billing_date": "2025-02-20T15:50:00Z",
    "amount_cents": 4990,
    "currency": "BRL"
  }
}
```

### GET /payments/subscriptions/current
Get current user subscription.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "subscription_id": "sub_abc123",
    "plan": {
      "id": "plan_premium",
      "name": "Premium",
      "features": {
        "cv_analyses_per_month": 20,
        "ai_coach_sessions": 50
      }
    },
    "status": "active",
    "current_period_start": "2025-01-20T15:50:00Z",
    "current_period_end": "2025-02-20T15:50:00Z",
    "usage": {
      "cv_analyses_used": 5,
      "ai_coach_sessions_used": 12
    }
  }
}
```

### POST /payments/subscriptions/{subscription_id}/cancel
Cancel subscription.

**Request Body:**
```json
{
  "reason": "no_longer_needed",
  "feedback": "Found a job, no longer need the service"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "subscription_id": "sub_abc123",
    "status": "canceled",
    "canceled_at": "2025-01-20T16:00:00Z",
    "end_of_service": "2025-02-20T15:50:00Z"
  }
}
```

### GET /payments/invoices
Get user's invoice history.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "invoice_id": "inv_789123",
      "subscription_id": "sub_abc123",
      "amount_cents": 4990,
      "currency": "BRL",
      "status": "paid",
      "invoice_date": "2025-01-20T15:50:00Z",
      "due_date": "2025-01-27T15:50:00Z",
      "paid_date": "2025-01-20T15:51:00Z",
      "download_url": "https://api.recoloca.ai/v1/payments/invoices/inv_789123/download"
    }
  ]
}
```

---

## 📊 Analytics Endpoints

### GET /analytics/dashboard
Get user dashboard analytics.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "cv_analyses": {
      "total": 25,
      "this_month": 5,
      "average_score": 82.3,
      "improvement_trend": "+5.2"
    },
    "ai_coach": {
      "total_sessions": 12,
      "this_month": 3,
      "total_messages": 156,
      "favorite_topics": ["interview_preparation", "salary_negotiation"]
    },
    "achievements": [
      {
        "id": "first_analysis",
        "title": "First CV Analysis",
        "description": "Completed your first CV analysis",
        "earned_at": "2025-01-15T10:00:00Z"
      }
    ]
  }
}
```

---

## 🔔 Notification Endpoints

### GET /notifications
Get user notifications.

**Query Parameters:**
```
read: true | false
type: "cv_analysis" | "subscription" | "coach" | "system"
limit: 20
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": "notif_123",
      "type": "cv_analysis",
      "title": "CV Analysis Complete",
      "message": "Your CV analysis is ready! Score: 85.5/100",
      "is_read": false,
      "created_at": "2025-01-20T15:32:00Z",
      "action_url": "/cv/analysis/cv_analysis_456789"
    }
  ],
  "meta": {
    "unread_count": 3
  }
}
```

### PUT /notifications/{notification_id}/read
Mark notification as read.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "notif_123",
    "is_read": true,
    "read_at": "2025-01-20T16:00:00Z"
  }
}
```

---

## 🚨 Error Codes

### Authentication Errors
- `AUTH_INVALID_CREDENTIALS` - Invalid email or password
- `AUTH_TOKEN_EXPIRED` - Access token has expired
- `AUTH_TOKEN_INVALID` - Invalid or malformed token
- `AUTH_REFRESH_TOKEN_INVALID` - Invalid refresh token
- `AUTH_USER_NOT_VERIFIED` - User email not verified

### Validation Errors
- `VALIDATION_ERROR` - General validation error
- `VALIDATION_EMAIL_INVALID` - Invalid email format
- `VALIDATION_PASSWORD_WEAK` - Password doesn't meet requirements
- `VALIDATION_FILE_TOO_LARGE` - Uploaded file exceeds size limit
- `VALIDATION_FILE_TYPE_INVALID` - Unsupported file type

### Business Logic Errors
- `SUBSCRIPTION_REQUIRED` - Feature requires active subscription
- `USAGE_LIMIT_EXCEEDED` - Monthly usage limit exceeded
- `CV_ANALYSIS_FAILED` - CV analysis processing failed
- `PAYMENT_FAILED` - Payment processing failed
- `SUBSCRIPTION_ALREADY_EXISTS` - User already has active subscription

### System Errors
- `INTERNAL_SERVER_ERROR` - Unexpected server error
- `SERVICE_UNAVAILABLE` - External service unavailable
- `RATE_LIMIT_EXCEEDED` - Too many requests
- `MAINTENANCE_MODE` - System under maintenance

---

## 📈 Rate Limiting

### Rate Limits by Endpoint Category

| Category | Limit | Window |
|----------|-------|--------|
| Authentication | 10 requests | 1 minute |
| CV Upload | 5 requests | 1 hour |
| CV Analysis | 100 requests | 1 hour |
| AI Coach | 200 requests | 1 hour |
| Payments | 20 requests | 1 minute |
| General API | 1000 requests | 1 hour |

### Rate Limit Headers
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642694400
X-RateLimit-Window: 3600
```

### Rate Limit Exceeded Response
```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again later.",
    "details": {
      "limit": 1000,
      "window": 3600,
      "reset_at": "2025-01-20T17:00:00Z"
    }
  }
}
```

---

## 🔍 Webhook Events

### Webhook Configuration
```http
POST https://your-app.com/webhooks/recoloca
Content-Type: application/json
X-Recoloca-Signature: sha256=<signature>
```

### Event Types

#### cv.analysis.completed
```json
{
  "event": "cv.analysis.completed",
  "data": {
    "analysis_id": "cv_analysis_456789",
    "user_id": 123,
    "overall_score": 85.5,
    "status": "completed"
  },
  "timestamp": "2025-01-20T15:32:00Z"
}
```

#### subscription.created
```json
{
  "event": "subscription.created",
  "data": {
    "subscription_id": "sub_abc123",
    "user_id": 123,
    "plan_id": "plan_premium",
    "status": "active"
  },
  "timestamp": "2025-01-20T15:50:00Z"
}
```

#### payment.succeeded
```json
{
  "event": "payment.succeeded",
  "data": {
    "payment_id": "pay_xyz789",
    "subscription_id": "sub_abc123",
    "amount_cents": 4990,
    "currency": "BRL"
  },
  "timestamp": "2025-01-20T15:51:00Z"
}
```

---

## 📚 OpenAPI Specification

### Swagger Documentation
```yaml
openapi: 3.0.3
info:
  title: Recoloca.ai API
  description: API for CV analysis and AI career coaching platform
  version: 1.0.0
  contact:
    name: API Support
    email: api-support@recoloca.ai
    url: https://docs.recoloca.ai
servers:
  - url: https://api.recoloca.ai/v1
    description: Production server
  - url: https://staging-api.recoloca.ai/v1
    description: Staging server
paths:
  /auth/register:
    post:
      summary: Register new user
      tags: [Authentication]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRegistration'
      responses:
        '201':
          description: User registered successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthResponse'
components:
  schemas:
    UserRegistration:
      type: object
      required: [email, password, full_name]
      properties:
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 8
        full_name:
          type: string
        phone:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

---

## 🔗 Related Documents

- [[Authentication_Module.md]] - Authentication Implementation
- [[CV_Analysis_Module.md]] - CV Analysis System
- [[AI_Coach_Module.md]] - AI Coaching System
- [[Payment_Module.md]] - Payment Processing
- [[Security_Guidelines.md]] - API Security Standards
- [[Testing_Strategy.md]] - API Testing Approach

---

**Document Status**: Active  
**Next Review Date**: 2025-03-20  
**Maintained By**: @BackendTeam