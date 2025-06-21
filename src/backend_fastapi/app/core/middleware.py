#!/usr/bin/env python3
"""
Recoloca.AI Middleware
Custom middleware for FastAPI application

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import logging
import time
import uuid
from typing import Callable

from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import RequestResponseEndpoint

from .config import settings
from .logging import log_error, log_request

logger = logging.getLogger(__name__)


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add unique request ID to each request.
    """
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        
        # Add request ID to request state
        request.state.request_id = request_id
        
        # Process request
        response = await call_next(request)
        
        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id
        
        return response


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for request/response logging.
    """
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        
        # Get request info
        method = request.method
        url = str(request.url)
        client_ip = request.client.host if request.client else "unknown"
        user_agent = request.headers.get("user-agent", "unknown")
        request_id = getattr(request.state, 'request_id', 'unknown')
        
        # Handle forwarded headers
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            client_ip = forwarded_for.split(",")[0].strip()
        
        try:
            # Process request
            response = await call_next(request)
            
            # Calculate processing time
            process_time = time.time() - start_time
            
            # Log request
            log_request(
                logger=logger,
                method=method,
                url=url,
                status_code=response.status_code,
                process_time=process_time,
                client_ip=client_ip,
                user_agent=user_agent,
                request_id=request_id,
                user_id=getattr(request.state, 'user_id', None)
            )
            
            # Add processing time to response headers
            response.headers["X-Process-Time"] = str(process_time)
            
            return response
            
        except Exception as e:
            # Calculate processing time for error case
            process_time = time.time() - start_time
            
            # Log error
            log_error(logger, e, {
                "operation": "request_processing",
                "method": method,
                "url": url,
                "client_ip": client_ip,
                "user_agent": user_agent,
                "request_id": request_id,
                "process_time": process_time
            })
            
            # Return error response
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error": "Internal server error",
                    "request_id": request_id,
                    "timestamp": settings.get_current_timestamp()
                },
                headers={
                    "X-Request-ID": request_id,
                    "X-Process-Time": str(process_time)
                }
            )


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for global error handling.
    """
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response = await call_next(request)
            return response
            
        except Exception as e:
            request_id = getattr(request.state, 'request_id', 'unknown')
            
            # Log the error
            log_error(logger, e, {
                "operation": "global_error_handler",
                "method": request.method,
                "url": str(request.url),
                "request_id": request_id
            })
            
            # Return appropriate error response
            if settings.DEBUG:
                # In debug mode, return detailed error information
                error_detail = {
                    "error": "Internal server error",
                    "detail": str(e),
                    "type": type(e).__name__,
                    "request_id": request_id,
                    "timestamp": settings.get_current_timestamp()
                }
            else:
                # In production, return generic error message
                error_detail = {
                    "error": "Internal server error",
                    "request_id": request_id,
                    "timestamp": settings.get_current_timestamp()
                }
            
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=error_detail,
                headers={
                    "X-Request-ID": request_id
                }
            )


class RateLimitHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add rate limit headers to responses.
    """
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        
        # Add rate limit headers if they were set by rate limiting dependency
        rate_limit_headers = getattr(request.state, 'rate_limit_headers', {})
        for header_name, header_value in rate_limit_headers.items():
            response.headers[header_name] = header_value
        
        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add security headers to responses.
    """
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        
        # Add security headers
        security_headers = {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Content-Security-Policy": (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline'; "
                "style-src 'self' 'unsafe-inline'; "
                "img-src 'self' data: https:; "
                "font-src 'self'; "
                "connect-src 'self' https:; "
                "frame-ancestors 'none';"
            )
        }
        
        # Add HSTS header for HTTPS
        if request.url.scheme == "https":
            security_headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        
        for header_name, header_value in security_headers.items():
            response.headers[header_name] = header_value
        
        return response


class CacheControlMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add appropriate cache control headers.
    """
    
    def __init__(self, app, cache_config: dict = None):
        super().__init__(app)
        self.cache_config = cache_config or {
            "/api/v1/rag/status": "no-cache",
            "/api/v1/rag/query": "private, max-age=300",  # 5 minutes
            "/api/v1/rag/documents": "private, max-age=3600",  # 1 hour
            "/health": "no-cache",
            "/": "no-cache"
        }
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        
        # Get cache control for this path
        path = request.url.path
        cache_control = None
        
        # Find matching cache config
        for config_path, config_value in self.cache_config.items():
            if path.startswith(config_path):
                cache_control = config_value
                break
        
        # Default cache control for API endpoints
        if not cache_control and path.startswith("/api/"):
            cache_control = "private, no-cache"
        
        # Add cache control header
        if cache_control:
            response.headers["Cache-Control"] = cache_control
        
        return response


class HealthCheckMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle health check requests efficiently.
    """
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Handle health check requests quickly
        if request.url.path in ["/health", "/healthz", "/ping"]:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "status": "healthy",
                    "timestamp": settings.get_current_timestamp(),
                    "version": settings.APP_VERSION
                }
            )
        
        return await call_next(request)


def setup_middleware(app):
    """
    Setup all middleware for the FastAPI application.
    
    Args:
        app: FastAPI application instance
    """
    # Add middleware in reverse order (last added is executed first)
    
    # Health check middleware (should be first to handle quickly)
    app.add_middleware(HealthCheckMiddleware)
    
    # Security headers
    app.add_middleware(SecurityHeadersMiddleware)
    
    # Cache control
    app.add_middleware(CacheControlMiddleware)
    
    # Rate limit headers
    app.add_middleware(RateLimitHeadersMiddleware)
    
    # Error handling
    app.add_middleware(ErrorHandlingMiddleware)
    
    # Request logging
    app.add_middleware(LoggingMiddleware)
    
    # Request ID (should be last to ensure all other middleware can access it)
    app.add_middleware(RequestIDMiddleware)
    
    logger.info("All middleware configured successfully")