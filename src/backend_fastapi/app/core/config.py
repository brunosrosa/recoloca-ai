#!/usr/bin/env python3
"""
Recoloca.AI FastAPI Backend Configuration
Centralized configuration management with environment variables

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    model_config = {
        "extra": "ignore",
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True
    }
    
    # Application
    APP_NAME: str = "Recoloca.AI API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    DEBUG: bool = Field(default=True, env="DEBUG")
    
    # Server
    HOST: str = Field(default="0.0.0.0", env="HOST")
    PORT: int = Field(default=8000, env="PORT")
    
    # Security
    SECRET_KEY: str = Field(env="SECRET_KEY")
    ALLOWED_ORIGINS: List[str] = Field(
        default="http://localhost:3000,http://localhost:8080,https://recoloca.ai,https://*.recoloca.ai",
        env="ALLOWED_ORIGINS"
    )
    ALLOWED_HOSTS: List[str] = Field(
        default="localhost,127.0.0.1,recoloca.ai,*.recoloca.ai",
        env="ALLOWED_HOSTS"
    )
    
    # Database (Supabase)
    SUPABASE_URL: str = Field(env="SUPABASE_URL")
    SUPABASE_ANON_KEY: str = Field(env="SUPABASE_ANON_KEY")
    SUPABASE_SERVICE_ROLE_KEY: str = Field(env="SUPABASE_SERVICE_ROLE_KEY")
    DATABASE_URL: Optional[str] = Field(default=None, env="DATABASE_URL")
    
    # JWT
    JWT_SECRET_KEY: str = Field(env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field(default="HS256", env="JWT_ALGORITHM")
    JWT_EXPIRE_MINUTES: int = Field(default=30, env="JWT_EXPIRE_MINUTES")
    
    # Redis (Cache)
    REDIS_URL: Optional[str] = Field(default=None, env="REDIS_URL")
    REDIS_HOST: str = Field(default="localhost", env="REDIS_HOST")
    REDIS_PORT: int = Field(default=6379, env="REDIS_PORT")
    REDIS_DB: int = Field(default=0, env="REDIS_DB")
    REDIS_PASSWORD: Optional[str] = Field(default=None, env="REDIS_PASSWORD")
    
    # RAG Configuration
    RAG_ENABLED: bool = Field(default=True, env="RAG_ENABLED")
    RAG_TIMEOUT_SECONDS: int = Field(default=10, env="RAG_TIMEOUT_SECONDS")
    RAG_CACHE_TTL_SECONDS: int = Field(default=3600, env="RAG_CACHE_TTL_SECONDS")
    RAG_MAX_RESULTS: int = Field(default=20, env="RAG_MAX_RESULTS")
    RAG_MIN_SCORE: float = Field(default=0.2, env="RAG_MIN_SCORE")
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = Field(default=True, env="RATE_LIMIT_ENABLED")
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = Field(default=60, env="RATE_LIMIT_REQUESTS_PER_MINUTE")
    RATE_LIMIT_BURST: int = Field(default=10, env="RATE_LIMIT_BURST")
    
    # Logging
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    LOG_FORMAT: str = Field(default="json", env="LOG_FORMAT")  # json or text
    LOG_FILE: Optional[str] = Field(default=None, env="LOG_FILE")
    
    # External APIs
    OPENROUTER_API_KEY: Optional[str] = Field(default=None, env="OPENROUTER_API_KEY")
    GEMINI_API_KEY: Optional[str] = Field(default=None, env="GEMINI_API_KEY")
    
    # Stripe
    STRIPE_PUBLISHABLE_KEY: Optional[str] = Field(default=None, env="STRIPE_PUBLISHABLE_KEY")
    STRIPE_SECRET_KEY: Optional[str] = Field(default=None, env="STRIPE_SECRET_KEY")
    STRIPE_WEBHOOK_SECRET: Optional[str] = Field(default=None, env="STRIPE_WEBHOOK_SECRET")
    
    # Monitoring
    SENTRY_DSN: Optional[str] = Field(default=None, env="SENTRY_DSN")
    ENABLE_METRICS: bool = Field(default=True, env="ENABLE_METRICS")
    
    # File paths
    PROJECT_ROOT: Path = Field(default_factory=lambda: Path(__file__).parent.parent.parent.parent.parent)
    RAG_DATA_PATH: Optional[Path] = Field(default=None)
    
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    @field_validator("ALLOWED_HOSTS", mode="before")
    @classmethod
    def parse_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v
    
    @field_validator("RAG_DATA_PATH", mode="before")
    @classmethod
    def set_rag_data_path(cls, v):
        if v is None:
            project_root = Path(__file__).parent.parent.parent.parent.parent
            return project_root / "rag_infra" / "data"
        return Path(v)
    
    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, v):
        allowed = ["development", "staging", "production"]
        if v not in allowed:
            raise ValueError(f"Environment must be one of {allowed}")
        return v
    
    @field_validator("LOG_LEVEL")
    @classmethod
    def validate_log_level(cls, v):
        allowed = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in allowed:
            raise ValueError(f"Log level must be one of {allowed}")
        return v.upper()
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.ENVIRONMENT == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.ENVIRONMENT == "production"
    
    @property
    def redis_url_full(self) -> str:
        """Get full Redis URL."""
        if self.REDIS_URL:
            return self.REDIS_URL
        
        auth = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"redis://{auth}{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
    
    @staticmethod
    def get_current_timestamp() -> str:
        """Get current timestamp in ISO format."""
        return datetime.utcnow().isoformat() + "Z"
    



# Global settings instance
settings = Settings()


# Environment-specific configurations
if settings.ENVIRONMENT == "production":
    # Production overrides
    settings.DEBUG = False
    settings.LOG_LEVEL = "WARNING"
elif settings.ENVIRONMENT == "staging":
    # Staging overrides
    settings.DEBUG = False
    settings.LOG_LEVEL = "INFO"
else:
    # Development defaults
    settings.DEBUG = True
    settings.LOG_LEVEL = "DEBUG"