#!/usr/bin/env python3
"""
Recoloca.AI API v1 Router
Main router configuration for API version 1

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

from fastapi import APIRouter

from .endpoints import rag

# Create API v1 router
api_router = APIRouter()

# Include endpoint routers
api_router.include_router(
    rag.router,
    prefix="/rag",
    tags=["RAG"]
)

# TODO: Add other endpoint routers as they are implemented
# api_router.include_router(
#     auth.router,
#     prefix="/auth",
#     tags=["Authentication"]
# )
# 
# api_router.include_router(
#     jobs.router,
#     prefix="/jobs",
#     tags=["Jobs"]
# )
# 
# api_router.include_router(
#     profile.router,
#     prefix="/profile",
#     tags=["Profile"]
# )
# 
# api_router.include_router(
#     kanban.router,
#     prefix="/kanban",
#     tags=["Kanban"]
# )
# 
# api_router.include_router(
#     coach.router,
#     prefix="/coach",
#     tags=["AI Coach"]
# )