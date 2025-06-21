#!/usr/bin/env python3
"""
Recoloca.AI FastAPI Backend
Main application entry point

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.api.v1.api import api_router
from app.core.config_simple import settings
from app.core.logging import setup_logging
from app.core.middleware import setup_middleware
from app.services.rag_service import RAGService

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    
    try:
        # Initialize RAG service
        if settings.RAG_ENABLED:
            logger.info("Initializing RAG service...")
            rag_service = RAGService()
            await rag_service.initialize()
            app.state.rag_service = rag_service
            logger.info("RAG service initialized successfully")
        else:
            logger.info("RAG service disabled")
            app.state.rag_service = None
        
        logger.info("Application startup completed")
        
    except Exception as e:
        logger.error(f"Failed to initialize application: {e}")
        raise
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")
    
    try:
        # Cleanup RAG service
        if hasattr(app.state, 'rag_service') and app.state.rag_service:
            logger.info("Cleaning up RAG service...")
            await app.state.rag_service.cleanup()
            logger.info("RAG service cleanup completed")
        
        logger.info("Application shutdown completed")
        
    except Exception as e:
        logger.error(f"Error during application shutdown: {e}")


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered job search and career coaching platform",
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    openapi_url="/openapi.json" if settings.DEBUG else None,
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add trusted host middleware
if settings.ALLOWED_HOSTS:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )

# Setup all custom middleware
setup_middleware(app)

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
async def root(request: Request) -> JSONResponse:
    """
    Root endpoint - Health check with RAG status.
    """
    rag_status = "unknown"
    
    # Check RAG service status
    if hasattr(request.app.state, 'rag_service') and request.app.state.rag_service:
        try:
            health = await request.app.state.rag_service.health_check()
            rag_status = health.status
        except Exception:
            rag_status = "error"
    elif not settings.RAG_ENABLED:
        rag_status = "disabled"
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": f"Welcome to {settings.APP_NAME}",
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "status": "healthy",
            "rag_status": rag_status,
            "timestamp": settings.get_current_timestamp()
        }
    )


@app.get("/health", tags=["Health"])
async def health_check(request: Request) -> JSONResponse:
    """
    Detailed health check endpoint.
    """
    health_data = {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": settings.get_current_timestamp(),
        "services": {
            "api": "healthy"
        }
    }
    
    # Check RAG service health
    if settings.RAG_ENABLED and hasattr(request.app.state, 'rag_service'):
        rag_service = request.app.state.rag_service
        if rag_service:
            try:
                rag_health = await rag_service.health_check()
                health_data["services"]["rag"] = rag_health.status
                health_data["rag_details"] = {
                    "initialized": rag_health.initialized,
                    "document_count": rag_health.document_count,
                    "last_error": rag_health.last_error
                }
            except Exception as e:
                health_data["services"]["rag"] = "error"
                health_data["rag_details"] = {"error": str(e)}
        else:
            health_data["services"]["rag"] = "not_initialized"
    else:
        health_data["services"]["rag"] = "disabled"
    
    # Determine overall status
    service_statuses = list(health_data["services"].values())
    if "error" in service_statuses:
        health_data["status"] = "degraded"
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    elif "not_initialized" in service_statuses:
        health_data["status"] = "starting"
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    else:
        status_code = status.HTTP_200_OK
    
    return JSONResponse(
        status_code=status_code,
        content=health_data
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info" if not settings.DEBUG else "debug"
    )