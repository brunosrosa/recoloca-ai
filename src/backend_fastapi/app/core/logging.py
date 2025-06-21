#!/usr/bin/env python3
"""
Recoloca.AI FastAPI Backend Logging Configuration
Structured logging with correlation IDs and observability

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from pythonjsonlogger import jsonlogger

from .config import settings


class CorrelationFilter(logging.Filter):
    """Add correlation ID to log records."""
    
    def filter(self, record: logging.LogRecord) -> bool:
        # Try to get correlation ID from context
        correlation_id = getattr(record, 'correlation_id', None)
        if not correlation_id:
            # Try to get from thread local or other context
            correlation_id = "unknown"
        
        record.correlation_id = correlation_id
        return True


class CustomJSONFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter with additional fields."""
    
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]) -> None:
        super().add_fields(log_record, record, message_dict)
        
        # Add timestamp
        log_record['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        
        # Add service info
        log_record['service'] = 'recoloca-api'
        log_record['version'] = settings.VERSION
        log_record['environment'] = settings.ENVIRONMENT
        
        # Add correlation ID
        log_record['correlation_id'] = getattr(record, 'correlation_id', 'unknown')
        
        # Add request info if available
        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id
        
        if hasattr(record, 'user_id'):
            log_record['user_id'] = record.user_id
        
        if hasattr(record, 'endpoint'):
            log_record['endpoint'] = record.endpoint
        
        if hasattr(record, 'method'):
            log_record['method'] = record.method
        
        if hasattr(record, 'status_code'):
            log_record['status_code'] = record.status_code
        
        if hasattr(record, 'duration_ms'):
            log_record['duration_ms'] = record.duration_ms


class TextFormatter(logging.Formatter):
    """Custom text formatter for development."""
    
    def format(self, record: logging.LogRecord) -> str:
        # Add correlation ID to the record
        correlation_id = getattr(record, 'correlation_id', 'unknown')
        
        # Create formatted message
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        level = record.levelname
        name = record.name
        message = record.getMessage()
        
        formatted = f"[{timestamp}] {level:8} | {correlation_id:12} | {name:20} | {message}"
        
        # Add exception info if present
        if record.exc_info:
            formatted += "\n" + self.formatException(record.exc_info)
        
        return formatted


def setup_logging() -> None:
    """Setup application logging configuration."""
    
    # Clear existing handlers
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    
    # Set log level
    log_level = getattr(logging, settings.LOG_LEVEL)
    root_logger.setLevel(log_level)
    
    # Create correlation filter
    correlation_filter = CorrelationFilter()
    
    # Setup console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.addFilter(correlation_filter)
    
    if settings.LOG_FORMAT == "json":
        # JSON formatter for production
        json_formatter = CustomJSONFormatter(
            fmt='%(timestamp)s %(level)s %(name)s %(message)s'
        )
        console_handler.setFormatter(json_formatter)
    else:
        # Text formatter for development
        text_formatter = TextFormatter()
        console_handler.setFormatter(text_formatter)
    
    root_logger.addHandler(console_handler)
    
    # Setup file handler if specified
    if settings.LOG_FILE:
        log_file_path = Path(settings.LOG_FILE)
        log_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file_path)
        file_handler.addFilter(correlation_filter)
        
        # Always use JSON for file logging
        json_formatter = CustomJSONFormatter(
            fmt='%(timestamp)s %(level)s %(name)s %(message)s'
        )
        file_handler.setFormatter(json_formatter)
        
        root_logger.addHandler(file_handler)
    
    # Configure specific loggers
    
    # Reduce noise from external libraries
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    
    # Set our application loggers
    logging.getLogger("recoloca").setLevel(log_level)
    logging.getLogger("src.backend_fastapi").setLevel(log_level)
    
    # Log startup message
    logger = logging.getLogger(__name__)
    logger.info(
        "Logging configured",
        extra={
            "log_level": settings.LOG_LEVEL,
            "log_format": settings.LOG_FORMAT,
            "log_file": str(settings.LOG_FILE) if settings.LOG_FILE else None,
        }
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger with the specified name."""
    return logging.getLogger(name)


def log_request(logger: logging.Logger, method: str, path: str, status_code: int, 
               duration_ms: float, user_id: Optional[str] = None, 
               request_id: Optional[str] = None) -> None:
    """Log HTTP request with structured data."""
    logger.info(
        f"{method} {path} - {status_code}",
        extra={
            "method": method,
            "endpoint": path,
            "status_code": status_code,
            "duration_ms": duration_ms,
            "user_id": user_id,
            "request_id": request_id,
        }
    )


def log_rag_query(logger: logging.Logger, query: str, results_count: int, 
                 duration_ms: float, cache_hit: bool = False,
                 user_id: Optional[str] = None) -> None:
    """Log RAG query with structured data."""
    logger.info(
        f"RAG query executed: {results_count} results in {duration_ms:.2f}ms",
        extra={
            "query_length": len(query),
            "results_count": results_count,
            "duration_ms": duration_ms,
            "cache_hit": cache_hit,
            "user_id": user_id,
            "operation": "rag_query",
        }
    )


def log_error(logger: logging.Logger, error: Exception, context: Optional[Dict[str, Any]] = None) -> None:
    """Log error with structured context."""
    error_context = {
        "error_type": type(error).__name__,
        "error_message": str(error),
    }
    
    if context:
        error_context.update(context)
    
    logger.error(
        f"Error occurred: {error}",
        extra=error_context,
        exc_info=True
    )