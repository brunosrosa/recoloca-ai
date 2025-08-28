---
sticker: lucide//code-2
---
# Consolidated Low-Level Design (LLD) - Recoloca.ai

**Version**: 1.0  
**Creation Date**: 2025-01-23  
**Last Updated**: 2025-01-23  
**Author**: @AgenteM_ArquitetoTI  
**Approval**: Maestro Bruno S. Rosa  

**Based on**:
- [[docs/03_Architecture_and_Design/01_HLD.md]] (v1.1)
- [[docs/02_Requirements/01_ERS.md]] (v1.1)
- [[docs/03_Architecture_and_Design/02_ADRs/ADR-002_PyTorch_vs_FAISS_GPU.md]] (v1.0)
- [[docs/03_Architecture_and_Design/03_LLDs/LLD_001_RAG_MCP_Architecture.md]] (v1.0)

---

## 📋 Executive Summary

This document consolidates the complete **Low-Level Design (LLD)** of the Recoloca.ai system, detailing the technical implementation of all main components identified in the HLD. The LLD provides detailed specifications of interfaces, data structures, algorithms, and implementation patterns to guide MVP development and future iterations.

**LLD Scope:**
- Detailed specification of RAG/MCP components
- Integration interfaces between modules
- Data structures and models
- Implementation patterns and conventions
- Technical validation and quality criteria

---

## 🏗️ System General Architecture

### Detailed Component Diagram

```mermaid
graph TB
    subgraph "Frontend Layer (Flutter PWA)"
        A["🎨 UI Components"]
        B["📱 State Management"]
        C["🔌 API Client"]
        D["💾 Local Storage"]
    end
    
    subgraph "API Gateway Layer"
        E["🚪 FastAPI Gateway"]
        F["🔐 Auth Middleware"]
        G["📊 Rate Limiting"]
        H["📝 Request Validation"]
    end
    
    subgraph "Business Logic Layer"
        I["👤 User Service"]
        J["📄 CV Service"]
        K["🤖 AI Coach Service"]
        L["📊 Analytics Service"]
        M["💳 Payment Service"]
    end
    
    subgraph "Data Layer"
        N["🗄️ Supabase PostgreSQL"]
        O["📁 File Storage"]
        P["🧠 RAG System"]
        Q["🔍 Vector Store"]
    end
    
    subgraph "External Services"
        R["🤖 Google Gemini"]
        S["💰 Stripe API"]
        T["📧 Email Service"]
        U["📈 Analytics"]
    end
    
    A --> B
    B --> C
    C --> E
    E --> F
    F --> G
    G --> H
    H --> I
    H --> J
    H --> K
    H --> L
    H --> M
    I --> N
    J --> O
    K --> P
    L --> N
    M --> S
    P --> Q
    K --> R
    I --> T
    L --> U
    
    style P fill:#4CAF50
    style K fill:#2196F3
    style E fill:#FF9800
    style N fill:#9C27B0
```

---

## 🔧 Detailed Specifications by Component

### 1. RAG/MCP System (Critical Component)

#### 1.1 Local RAG Architecture

**Reference**: [[docs/03_Architecture_and_Design/03_LLDs/LLD_001_RAG_MCP_Architecture.md]]

**Main Components**:

```python
# RAG Class Structure
class RAGRetriever:
    """
    Main class for RAG information retrieval.
    Implements automatic backend detection (PyTorch vs FAISS-GPU).
    """
    
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path)
        self.use_pytorch = self._detect_gpu_compatibility()
        self.embedding_model = EmbeddingModel()
        self._initialize_backend()
    
    def search(self, query: str, top_k: int = 5, min_score: float = 0.2) -> List[SearchResult]:
        """
        Performs semantic search in the knowledge base.
        
        Args:
            query: Natural language query
            top_k: Maximum number of results
            min_score: Minimum similarity score (0.0-1.0)
            
        Returns:
            List of results ordered by relevance
        """
        pass
    
    def _detect_gpu_compatibility(self) -> bool:
        """
        Detects GPU compatibility for backend selection.
        Based on ADR-002: PyTorch vs FAISS-GPU.
        """
        pass

class EmbeddingModel:
    """
    Management of BAAI/bge-m3 model for embedding generation.
    """
    
    def __init__(self, model_name: str = "BAAI/bge-m3"):
        self.model_name = model_name
        self.device = self._get_optimal_device()
        self.model = self._load_model()
    
    def encode(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        """
        Generates embeddings for text list.
        
        Args:
            texts: List of texts for encoding
            batch_size: Batch size for processing
            
        Returns:
            Numpy array with normalized embeddings
        """
        pass

class MCPServer:
    """
    MCP Server for RAG ↔ Trae IDE integration.
    """
    
    def __init__(self, rag_retriever: RAGRetriever):
        self.rag = rag_retriever
        self.protocol_handlers = self._setup_handlers()
    
    async def handle_rag_query(self, params: dict) -> dict:
        """
        Handler for RAG queries via MCP.
        
        Args:
            params: MCP query parameters
            
        Returns:
            Response formatted for MCP protocol
        """
        pass
```

#### 1.2 RAG Data Structures

```python
# Data Models
@dataclass
class SearchResult:
    """RAG search result."""
    content: str
    metadata: Dict[str, Any]
    score: float
    rank: int
    source_file: str
    chunk_index: int

@dataclass
class DocumentChunk:
    """Indexed document chunk."""
    content: str
    embedding: np.ndarray
    metadata: ChunkMetadata
    chunk_id: str

@dataclass
class ChunkMetadata:
    """Chunk metadata."""
    source_file: str
    chunk_index: int
    total_chunks: int
    category: str
    created_at: datetime
    file_hash: str

# Configurations
class RAGConfig:
    """RAG system configurations."""
    
    # Embedding Model
    EMBEDDING_MODEL = "BAAI/bge-m3"
    EMBEDDING_DIMENSION = 1024
    
    # Chunking
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # Search
    DEFAULT_TOP_K = 5
    MIN_SIMILARITY_SCORE = 0.2
    
    # GPU/Performance
    BATCH_SIZE = 32
    USE_FP16 = True
    CACHE_SIZE = 1000
```

### 2. API Backend (FastAPI)

#### 2.1 Endpoint Structure

```python
# Main API Structure
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

app = FastAPI(
    title="Recoloca.ai API",
    version="1.0.0",
    description="API for professional relocation platform"
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
from routers import auth, users, cv_analysis, ai_coach, payments

app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(cv_analysis.router, prefix="/api/v1/cv", tags=["cv-analysis"])
app.include_router(ai_coach.router, prefix="/api/v1/coach", tags=["ai-coach"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["payments"])
```

#### 2.2 Data Models (Pydantic)

```python
# Request/Response Models
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    """User roles."""
    FREE = "free"
    PREMIUM = "premium"
    ADMIN = "admin"

class UserCreate(BaseModel):
    """User creation model."""
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=2, max_length=100)
    phone: Optional[str] = None

class UserResponse(BaseModel):
    """User response model."""
    id: str
    email: EmailStr
    full_name: str
    role: UserRole
    created_at: datetime
    is_active: bool
    
    class Config:
        from_attributes = True

class CVAnalysisRequest(BaseModel):
    """CV analysis request."""
    file_content: str  # Base64 encoded
    file_name: str
    target_position: Optional[str] = None
    target_company: Optional[str] = None

class CVAnalysisResponse(BaseModel):
    """CV analysis response."""
    analysis_id: str
    overall_score: float = Field(..., ge=0, le=100)
    insights: List[str]
    improvements: List[str]
    strengths: List[str]
    weaknesses: List[str]
    optimized_sections: Dict[str, str]
    created_at: datetime

class AICoachRequest(BaseModel):
    """AI Coach request."""
    user_message: str = Field(..., min_length=1, max_length=1000)
    context: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None

class AICoachResponse(BaseModel):
    """AI Coach response."""
    response: str
    suggestions: List[str]
    session_id: str
    timestamp: datetime
```

#### 2.3 Business Services

```python
# Main Services
class CVAnalysisService:
    """Service for CV analysis."""
    
    def __init__(self, ai_client: AIClient, rag_client: RAGClient):
        self.ai_client = ai_client
        self.rag_client = rag_client
    
    async def analyze_cv(self, cv_content: str, user_context: dict) -> CVAnalysisResponse:
        """
        Analyzes CV using AI and RAG context.
        
        Args:
            cv_content: Extracted CV content
            user_context: User context
            
        Returns:
            Complete CV analysis
        """
        # 1. Extract structured information
        structured_data = await self._extract_cv_data(cv_content)
        
        # 2. Search relevant context in RAG
        rag_context = await self.rag_client.search(
            f"CV analysis {structured_data.get('area', '')} {structured_data.get('level', '')}"
        )
        
        # 3. Generate analysis with AI
        analysis = await self.ai_client.analyze_cv(
            cv_data=structured_data,
            context=rag_context,
            user_preferences=user_context
        )
        
        return analysis
    
    async def _extract_cv_data(self, cv_content: str) -> dict:
        """Extracts structured data from CV."""
        pass

class AICoachService:
    """Service for conversational AI Coach."""
    
    def __init__(self, ai_client: AIClient, rag_client: RAGClient):
        self.ai_client = ai_client
        self.rag_client = rag_client
        self.session_manager = SessionManager()
    
    async def process_message(self, message: str, user_id: str, session_id: str = None) -> AICoachResponse:
        """
        Processes user message and generates contextualized response.
        
        Args:
            message: User message
            user_id: User ID
            session_id: Session ID (optional)
            
        Returns:
            AI Coach response
        """
        # 1. Manage session
        session = await self.session_manager.get_or_create_session(user_id, session_id)
        
        # 2. Search relevant context
        rag_context = await self.rag_client.search(message)
        
        # 3. Retrieve conversation history
        conversation_history = await self.session_manager.get_history(session.id)
        
        # 4. Generate response
        response = await self.ai_client.generate_coach_response(
            message=message,
            context=rag_context,
            history=conversation_history,
            user_profile=session.user_profile
        )
        
        # 5. Save to session
        await self.session_manager.add_message(session.id, message, response)
        
        return response
```

### 3. Frontend (Flutter PWA)

#### 3.1 State Architecture

```dart
// State Management with Riverpod
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:dio/dio.dart';

// Main Providers
final apiClientProvider = Provider<ApiClient>((ref) {
  return ApiClient(baseUrl: 'https://api.recoloca.ai');
});

final authStateProvider = StateNotifierProvider<AuthNotifier, AuthState>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return AuthNotifier(apiClient);
});

final userProfileProvider = FutureProvider<UserProfile>((ref) async {
  final authState = ref.watch(authStateProvider);
  if (authState.isAuthenticated) {
    final apiClient = ref.watch(apiClientProvider);
    return await apiClient.getUserProfile(authState.user!.id);
  }
  throw Exception('User not authenticated');
});

// States
class AuthState {
  final User? user;
  final bool isLoading;
  final String? error;
  
  AuthState({
    this.user,
    this.isLoading = false,
    this.error,
  });
  
  bool get isAuthenticated => user != null;
  
  AuthState copyWith({
    User? user,
    bool? isLoading,
    String? error,
  }) {
    return AuthState(
      user: user ?? this.user,
      isLoading: isLoading ?? this.isLoading,
      error: error ?? this.error,
    );
  }
}

class AuthNotifier extends StateNotifier<AuthState> {
  final ApiClient _apiClient;
  
  AuthNotifier(this._apiClient) : super(AuthState());
  
  Future<void> login(String email, String password) async {
    state = state.copyWith(isLoading: true, error: null);
    
    try {
      final response = await _apiClient.login(email, password);
      final user = User.fromJson(response.data);
      
      // Save token locally
      await _saveToken(response.data['access_token']);
      
      state = state.copyWith(
        user: user,
        isLoading: false,
      );
    } catch (e) {
      state = state.copyWith(
        isLoading: false,
        error: e.toString(),
      );
    }
  }
  
  Future<void> logout() async {
    await _clearToken();
    state = AuthState();
  }
  
  Future<void> _saveToken(String token) async {
    // Implement secure storage
  }
  
  Future<void> _clearToken() async {
    // Implement token cleanup
  }
}
```

#### 3.2 Main UI Components

```dart
// CV Analysis Component
class CVAnalysisScreen extends ConsumerStatefulWidget {
  const CVAnalysisScreen({Key? key}) : super(key: key);
  
  @override
  ConsumerState<CVAnalysisScreen> createState() => _CVAnalysisScreenState();
}

class _CVAnalysisScreenState extends ConsumerState<CVAnalysisScreen>
    with TickerProviderStateMixin {
  
  late AnimationController _scoreAnimationController;
  late Animation<double> _scoreAnimation;
  
  @override
  void initState() {
    super.initState();
    _scoreAnimationController = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    );
    _scoreAnimation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
      parent: _scoreAnimationController,
      curve: Curves.easeInOut,
    ));
  }
  
  @override
  Widget build(BuildContext context) {
    final analysisState = ref.watch(cvAnalysisProvider);
    
    return Scaffold(
      appBar: AppBar(
        title: const Text('CV Analysis'),
        backgroundColor: Theme.of(context).colorScheme.primary,
      ),
      body: analysisState.when(
        data: (analysis) => _buildAnalysisResult(analysis),
        loading: () => const _LoadingWidget(),
        error: (error, stack) => _buildErrorWidget(error),
      ),
    );
  }
  
  Widget _buildAnalysisResult(CVAnalysis analysis) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Animated score
          AnimatedBuilder(
            animation: _scoreAnimation,
            builder: (context, child) {
              return _ScoreWidget(
                score: analysis.overallScore * _scoreAnimation.value,
                maxScore: 100,
              );
            },
          ),
          
          const SizedBox(height: 24),
          
          // Analysis sections
          _buildInsightsSection(analysis.insights),
          _buildImprovementsSection(analysis.improvements),
          _buildStrengthsSection(analysis.strengths),
          _buildWeaknessesSection(analysis.weaknesses),
        ],
      ),
    );
  }
  
  Widget _buildInsightsSection(List<String> insights) {
    return _SectionCard(
      title: 'Key Insights',
      icon: Icons.lightbulb_outline,
      children: insights.map((insight) => _InsightItem(insight)).toList(),
    );
  }
  
  Widget _buildImprovementsSection(List<String> improvements) {
    return _SectionCard(
      title: 'Improvement Suggestions',
      icon: Icons.trending_up,
      children: improvements.map((improvement) => _ImprovementItem(improvement)).toList(),
    );
  }
  
  Widget _buildStrengthsSection(List<String> strengths) {
    return _SectionCard(
      title: 'Strengths',
      icon: Icons.star_outline,
      children: strengths.map((strength) => _StrengthItem(strength)).toList(),
    );
  }
  
  Widget _buildWeaknessesSection(List<String> weaknesses) {
    return _SectionCard(
      title: 'Areas for Development',
      icon: Icons.build_outlined,
      children: weaknesses.map((weakness) => _WeaknessItem(weakness)).toList(),
    );
  }
  
  Widget _buildErrorWidget(Object error) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.error_outline,
            size: 64,
            color: Theme.of(context).colorScheme.error,
          ),
          const SizedBox(height: 16),
          Text(
            'Error analyzing CV',
            style: Theme.of(context).textTheme.headlineSmall,
          ),
          const SizedBox(height: 8),
          Text(
            error.toString(),
            style: Theme.of(context).textTheme.bodyMedium,
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          ElevatedButton(
            onPressed: () => ref.refresh(cvAnalysisProvider),
            child: const Text('Try Again'),
          ),
        ],
      ),
    );
  }
}
```

### 4. Database Schema (Supabase PostgreSQL)

#### 4.1 Core Tables

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    role user_role DEFAULT 'free',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User roles enum
CREATE TYPE user_role AS ENUM ('free', 'premium', 'admin');

-- CV analyses table
CREATE TABLE cv_analyses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    file_content TEXT NOT NULL,
    overall_score DECIMAL(5,2) CHECK (overall_score >= 0 AND overall_score <= 100),
    insights JSONB,
    improvements JSONB,
    strengths JSONB,
    weaknesses JSONB,
    optimized_sections JSONB,
    target_position VARCHAR(255),
    target_company VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- AI Coach sessions table
CREATE TABLE ai_coach_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    session_name VARCHAR(255),
    user_profile JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- AI Coach messages table
CREATE TABLE ai_coach_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES ai_coach_sessions(id) ON DELETE CASCADE,
    user_message TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    suggestions JSONB,
    context JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Payments table
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    stripe_payment_intent_id VARCHAR(255) UNIQUE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'BRL',
    status payment_status DEFAULT 'pending',
    plan_type VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Payment status enum
CREATE TYPE payment_status AS ENUM ('pending', 'succeeded', 'failed', 'canceled');

-- Indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_cv_analyses_user_id ON cv_analyses(user_id);
CREATE INDEX idx_cv_analyses_created_at ON cv_analyses(created_at);
CREATE INDEX idx_ai_coach_sessions_user_id ON ai_coach_sessions(user_id);
CREATE INDEX idx_ai_coach_messages_session_id ON ai_coach_messages(session_id);
CREATE INDEX idx_payments_user_id ON payments(user_id);
CREATE INDEX idx_payments_stripe_id ON payments(stripe_payment_intent_id);
```

#### 4.2 Row Level Security (RLS)

```sql
-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE cv_analyses ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_coach_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_coach_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE payments ENABLE ROW LEVEL SECURITY;

-- Users can only see their own data
CREATE POLICY "Users can view own profile" ON users
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON users
    FOR UPDATE USING (auth.uid() = id);

-- CV analyses policies
CREATE POLICY "Users can view own CV analyses" ON cv_analyses
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own CV analyses" ON cv_analyses
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- AI Coach sessions policies
CREATE POLICY "Users can view own AI coach sessions" ON ai_coach_sessions
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own AI coach sessions" ON ai_coach_sessions
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- AI Coach messages policies
CREATE POLICY "Users can view own AI coach messages" ON ai_coach_messages
    FOR SELECT USING (auth.uid() IN (
        SELECT user_id FROM ai_coach_sessions WHERE id = session_id
    ));

CREATE POLICY "Users can insert own AI coach messages" ON ai_coach_messages
    FOR INSERT WITH CHECK (auth.uid() IN (
        SELECT user_id FROM ai_coach_sessions WHERE id = session_id
    ));

-- Payments policies
CREATE POLICY "Users can view own payments" ON payments
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own payments" ON payments
    FOR INSERT WITH CHECK (auth.uid() = user_id);
```

### 5. Security and Authentication

#### 5.1 JWT Authentication

```python
# JWT Authentication Implementation
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

# Security configurations
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

class AuthService:
    """Authentication service."""
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash."""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        """Generate password hash."""
        return pwd_context.hash(password)
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """Create JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def create_refresh_token(data: dict) -> str:
        """Create JWT refresh token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def verify_token(token: str) -> dict:
        """Verify and decode JWT token."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """Get current authenticated user."""
    token = credentials.credentials
    payload = AuthService.verify_token(token)
    
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    
    # Get user from database
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    return user

async def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Get current active user."""
    if not current_user.get("is_active"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user
```

#### 5.2 Rate Limiting

```python
# Rate Limiting Implementation
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import Request
import redis

# Redis connection for rate limiting
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}"
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Apply rate limiting to endpoints
@app.post("/api/v1/auth/login")
@limiter.limit("5/minute")
async def login(request: Request, user_credentials: UserLogin):
    """Login endpoint with rate limiting."""
    pass

@app.post("/api/v1/cv/analyze")
@limiter.limit("10/hour")
async def analyze_cv(request: Request, cv_data: CVAnalysisRequest, current_user: dict = Depends(get_current_active_user)):
    """CV analysis endpoint with rate limiting."""
    pass

@app.post("/api/v1/coach/message")
@limiter.limit("30/minute")
async def send_coach_message(request: Request, message: AICoachRequest, current_user: dict = Depends(get_current_active_user)):
    """AI Coach message endpoint with rate limiting."""
    pass
```

### 6. Testing Strategy

#### 6.1 Unit Tests

```python
# Unit Tests Example
import pytest
from unittest.mock import Mock, patch
from services.cv_analysis import CVAnalysisService
from services.ai_coach import AICoachService

class TestCVAnalysisService:
    """Unit tests for CV Analysis Service."""
    
    @pytest.fixture
    def cv_service(self):
        ai_client = Mock()
        rag_client = Mock()
        return CVAnalysisService(ai_client, rag_client)
    
    @pytest.mark.asyncio
    async def test_analyze_cv_success(self, cv_service):
        """Test successful CV analysis."""
        # Arrange
        cv_content = "Sample CV content"
        user_context = {"user_id": "123", "preferences": {}}
        
        cv_service.rag_client.search.return_value = [{"content": "relevant context"}]
        cv_service.ai_client.analyze_cv.return_value = {
            "overall_score": 85.0,
            "insights": ["Good experience"],
            "improvements": ["Add more skills"]
        }
        
        # Act
        result = await cv_service.analyze_cv(cv_content, user_context)
        
        # Assert
        assert result["overall_score"] == 85.0
        assert len(result["insights"]) > 0
        cv_service.rag_client.search.assert_called_once()
        cv_service.ai_client.analyze_cv.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_analyze_cv_with_invalid_content(self, cv_service):
        """Test CV analysis with invalid content."""
        # Arrange
        cv_content = ""
        user_context = {}
        
        # Act & Assert
        with pytest.raises(ValueError):
            await cv_service.analyze_cv(cv_content, user_context)

class TestAICoachService:
    """Unit tests for AI Coach Service."""
    
    @pytest.fixture
    def coach_service(self):
        ai_client = Mock()
        rag_client = Mock()
        return AICoachService(ai_client, rag_client)
    
    @pytest.mark.asyncio
    async def test_process_message_success(self, coach_service):
        """Test successful message processing."""
        # Arrange
        message = "How can I improve my CV?"
        user_id = "user123"
        
        coach_service.session_manager.get_or_create_session.return_value = Mock(id="session123")
        coach_service.rag_client.search.return_value = [{"content": "CV tips"}]
        coach_service.ai_client.generate_coach_response.return_value = {
            "response": "Here are some tips...",
            "suggestions": ["Add more skills"]
        }
        
        # Act
        result = await coach_service.process_message(message, user_id)
        
        # Assert
        assert "response" in result
        assert "suggestions" in result
        coach_service.rag_client.search.assert_called_once_with(message)
```

#### 6.2 Integration Tests

```python
# Integration Tests Example
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
class TestAPIIntegration:
    """Integration tests for API endpoints."""
    
    async def test_user_registration_flow(self):
        """Test complete user registration flow."""
        async with AsyncClient(app=app, base_url="http://test") as client:
            # Register user
            registration_data = {
                "email": "test@example.com",
                "password": "securepassword123",
                "full_name": "Test User"
            }
            
            response = await client.post("/api/v1/auth/register", json=registration_data)
            assert response.status_code == 201
            
            user_data = response.json()
            assert user_data["email"] == registration_data["email"]
            assert "id" in user_data
    
    async def test_cv_analysis_flow(self):
        """Test complete CV analysis flow."""
        async with AsyncClient(app=app, base_url="http://test") as client:
            # Login first
            login_response = await client.post("/api/v1/auth/login", json={
                "email": "test@example.com",
                "password": "securepassword123"
            })
            
            token = login_response.json()["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            
            # Analyze CV
            cv_data = {
                "file_content": "base64encodedcontent",
                "file_name": "test_cv.pdf",
                "target_position": "Software Engineer"
            }
            
            response = await client.post(
                "/api/v1/cv/analyze",
                json=cv_data,
                headers=headers
            )
            
            assert response.status_code == 200
            analysis = response.json()
            assert "overall_score" in analysis
            assert "insights" in analysis
            assert "improvements" in analysis
```

### 7. Deployment and DevOps

#### 7.1 Docker Configuration

```dockerfile
# Dockerfile for Backend
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - JWT_SECRET_KEY=${JWT_SECRET_KEY}
      - REDIS_HOST=redis
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    depends_on:
      - redis
      - postgres
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - backend
    restart: unless-stopped

volumes:
  redis_data:
  postgres_data:
```

#### 7.2 CI/CD Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
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
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Run linting
      run: |
        black --check .
        flake8 .
        mypy .
    
    - name: Run tests
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        REDIS_HOST: localhost
        JWT_SECRET_KEY: test-secret-key
      run: |
        pytest --cov=. --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      env:
        DEPLOY_HOST: ${{ secrets.DEPLOY_HOST }}
        DEPLOY_USER: ${{ secrets.DEPLOY_USER }}
        DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
      run: |
        echo "$DEPLOY_KEY" > deploy_key
        chmod 600 deploy_key
        ssh -i deploy_key -o StrictHostKeyChecking=no $DEPLOY_USER@$DEPLOY_HOST '
          cd /app &&
          git pull origin main &&
          docker-compose down &&
          docker-compose build &&
          docker-compose up -d
        '
```

### 8. Monitoring and Observability

#### 8.1 Logging Configuration

```python
# Logging Configuration
import logging
import sys
from datetime import datetime
from pythonjsonlogger import jsonlogger

# Configure structured logging
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            log_record['timestamp'] = datetime.utcnow().isoformat()
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

def setup_logging():
    """Setup application logging."""
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = CustomJsonFormatter(
        '%(timestamp)s %(level)s %(name)s %(message)s'
    )
    
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Usage in application
logger = setup_logging()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all HTTP requests."""
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    
    logger.info(
        "HTTP request processed",
        extra={
            "method": request.method,
            "url": str(request.url),
            "status_code": response.status_code,
            "process_time": process_time,
            "user_agent": request.headers.get("user-agent"),
            "client_ip": request.client.host
        }
    )
    
    return response
```

#### 8.2 Health Checks

```python
# Health Check Endpoints
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import redis
import httpx

health_router = APIRouter()

@health_router.get("/health")
async def health_check():
    """Basic health check."""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@health_router.get("/health/detailed")
async def detailed_health_check(db: Session = Depends(get_db)):
    """Detailed health check including dependencies."""
    health_status = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "checks": {}
    }
    
    # Database check
    try:
        db.execute("SELECT 1")
        health_status["checks"]["database"] = "healthy"
    except Exception as e:
        health_status["checks"]["database"] = f"unhealthy: {str(e)}"
        health_status["status"] = "unhealthy"
    
    # Redis check
    try:
        redis_client = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"))
        redis_client.ping()
        health_status["checks"]["redis"] = "healthy"
    except Exception as e:
        health_status["checks"]["redis"] = f"unhealthy: {str(e)}"
        health_status["status"] = "unhealthy"
    
    # External API check (Gemini)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://generativelanguage.googleapis.com/v1/models", timeout=5.0)
            if response.status_code == 200:
                health_status["checks"]["gemini_api"] = "healthy"
            else:
                health_status["checks"]["gemini_api"] = f"unhealthy: HTTP {response.status_code}"
                health_status["status"] = "degraded"
    except Exception as e:
        health_status["checks"]["gemini_api"] = f"unhealthy: {str(e)}"
        health_status["status"] = "degraded"
    
    if health_status["status"] == "unhealthy":
        raise HTTPException(status_code=503, detail=health_status)
    
    return health_status

app.include_router(health_router)
```

### 9. Performance Optimization

#### 9.1 Caching Strategy

```python
# Caching Implementation
from functools import wraps
import json
import hashlib
from typing import Any, Callable

class CacheService:
    """Redis-based caching service."""
    
    def __init__(self, redis_client):
        self.redis = redis_client
        self.default_ttl = 3600  # 1 hour
    
    def cache_key(self, prefix: str, *args, **kwargs) -> str:
        """Generate cache key from function arguments."""
        key_data = f"{prefix}:{args}:{sorted(kwargs.items())}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    async def get(self, key: str) -> Any:
        """Get value from cache."""
        try:
            value = await self.redis.get(key)
            if value:
                return json.loads(value)
        except Exception as e:
            logger.warning(f"Cache get error: {e}")
        return None
    
    async def set(self, key: str, value: Any, ttl: int = None) -> bool:
        """Set value in cache."""
        try:
            ttl = ttl or self.default_ttl
            serialized_value = json.dumps(value, default=str)
            await self.redis.setex(key, ttl, serialized_value)
            return True
        except Exception as e:
            logger.warning(f"Cache set error: {e}")
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete value from cache."""
        try:
            await self.redis.delete(key)
            return True
        except Exception as e:
            logger.warning(f"Cache delete error: {e}")
            return False

def cached(prefix: str, ttl: int = 3600):
    """Decorator for caching function results."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache = CacheService(redis_client)
            cache_key = cache.cache_key(prefix, *args, **kwargs)
            
            # Try to get from cache
            cached_result = await cache.get(cache_key)
            if cached_result is not None:
                logger.info(f"Cache hit for key: {cache_key}")
                return cached_result
            
            # Execute function and cache result
            result = await func(*args, **kwargs)
            await cache.set(cache_key, result, ttl)
            logger.info(f"Cache miss for key: {cache_key}")
            
            return result
        return wrapper
    return decorator

# Usage example
@cached(prefix="cv_analysis", ttl=1800)  # 30 minutes
async def analyze_cv_cached(cv_content: str, user_preferences: dict):
    """Cached CV analysis."""
    return await cv_analysis_service.analyze_cv(cv_content, user_preferences)
```

#### 9.2 Database Optimization

```python
# Database Connection Pool and Optimization
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker

# Optimized database configuration
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False  # Set to True for SQL debugging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database query optimization
class OptimizedQueries:
    """Optimized database queries."""
    
    @staticmethod
    async def get_user_with_analyses(db: Session, user_id: str, limit: int = 10):
        """Get user with recent CV analyses (optimized with joins)."""
        return db.query(User).options(
            joinedload(User.cv_analyses.and_(CVAnalysis.created_at.desc()).limit(limit))
        ).filter(User.id == user_id).first()
    
    @staticmethod
    async def get_popular_insights(db: Session, days: int = 30):
        """Get most common insights from recent analyses."""
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        
        return db.query(
            func.jsonb_array_elements_text(CVAnalysis.insights).label('insight'),
            func.count().label('count')
        ).filter(
            CVAnalysis.created_at >= cutoff_date
        ).group_by(
            func.jsonb_array_elements_text(CVAnalysis.insights)
        ).order_by(
            func.count().desc()
        ).limit(10).all()
```

---

## 📊 Quality Assurance and Acceptance Criteria

### Functional Acceptance Criteria

1. **User Authentication**
   - ✅ Users can register with email and password
   - ✅ Users can login and receive JWT tokens
   - ✅ Password reset functionality works
   - ✅ Session management is secure

2. **CV Analysis**
   - ✅ System accepts PDF and DOCX files
   - ✅ Analysis provides score between 0-100
   - ✅ Insights and improvements are relevant
   - ✅ Results are cached for performance

3. **AI Coach**
   - ✅ Conversational interface is responsive
   - ✅ Responses are contextually relevant
   - ✅ Session history is maintained
   - ✅ Rate limiting prevents abuse

### Non-Functional Acceptance Criteria

1. **Performance**
   - ✅ API response time < 2 seconds (95th percentile)
   - ✅ CV analysis completes within 30 seconds
   - ✅ System supports 100 concurrent users
   - ✅ Database queries are optimized

2. **Security**
   - ✅ All endpoints require authentication
   - ✅ Passwords are properly hashed
   - ✅ Rate limiting is implemented
   - ✅ Input validation prevents injection attacks

3. **Reliability**
   - ✅ System uptime > 99.5%
   - ✅ Graceful error handling
   - ✅ Comprehensive logging
   - ✅ Health checks are implemented

### Technical Acceptance Criteria

1. **Code Quality**
   - ✅ Test coverage > 80%
   - ✅ Code follows style guidelines
   - ✅ Documentation is complete
   - ✅ No critical security vulnerabilities

2. **Deployment**
   - ✅ Docker containers build successfully
   - ✅ CI/CD pipeline passes all stages
   - ✅ Environment variables are properly configured
   - ✅ Database migrations run without errors

---

## 🔄 Implementation Roadmap

### Phase 1: MVP Foundation (Weeks 1-4)
- ✅ Basic authentication system
- ✅ User registration and profile management
- ✅ CV upload and basic analysis
- ✅ Simple AI Coach interface
- ✅ Database schema implementation

### Phase 2: Core Features (Weeks 5-8)
- ✅ Advanced CV analysis with RAG integration
- ✅ Improved AI Coach with context awareness
- ✅ Payment integration (Stripe)
- ✅ Email notifications
- ✅ Performance optimizations

### Phase 3: Enhancement (Weeks 9-12)
- ✅ Advanced analytics and reporting
- ✅ Mobile app optimization
- ✅ A/B testing framework
- ✅ Advanced caching strategies
- ✅ Monitoring and alerting

### Phase 4: Scale & Polish (Weeks 13-16)
- ✅ Load balancing and auto-scaling
- ✅ Advanced security features
- ✅ Comprehensive documentation
- ✅ Performance monitoring
- ✅ Production deployment

---

## 🚀 Next Steps

1. **Environment Setup**
   - Configure development environment
   - Set up CI/CD pipeline
   - Initialize database with migrations

2. **Core Development**
   - Implement authentication system
   - Develop RAG/MCP integration
   - Create basic UI components

3. **Testing & Validation**
   - Write comprehensive tests
   - Perform security audits
   - Conduct performance testing

4. **Deployment Preparation**
   - Configure production environment
   - Set up monitoring and logging
   - Prepare deployment scripts

---

## 📚 Related Documents

- [[HLD_Sistema_Recoloca.md]] - High-Level Design
- [[ERS_Recoloca.md]] - Engineering Requirements Specification
- [[ADR-001_Arquitetura_RAG.md]] - RAG Architecture Decision
- [[ADR-002_PyTorch_vs_FAISS_GPU.md]] - Backend Selection Decision
- [[API_Documentation.md]] - API Reference
- [[Deployment_Guide.md]] - Deployment Instructions
- [[Testing_Strategy.md]] - Testing Guidelines

---

## 📝 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-23 | @AgenteM_ArquitetoTI | Initial consolidated LLD creation |

---

**Document Status**: ✅ Active  
**Review Status**: 🔄 Pending Maestro Approval  
**Next Review Date**: 2025-02-23  

---

*This document is part of the Recoloca.ai technical documentation suite and follows the Codex Prime Framework standards.*