#!/usr/bin/env python3
"""
Recoloca.AI Authentication Dependencies
JWT-based authentication and authorization for FastAPI endpoints

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import logging
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWTError

from ...core.config import settings
from ...core.logging import log_error

security = HTTPBearer()
logger = logging.getLogger(__name__)


class JWTError(Exception):
    """Custom JWT error for better error handling."""
    pass


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.
    
    Args:
        data: Payload data to encode in the token
        expires_delta: Token expiration time (default: 30 minutes)
    
    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    try:
        encoded_jwt = jwt.encode(
            to_encode,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error creating JWT token: {e}")
        raise JWTError("Failed to create access token")


def create_refresh_token(data: Dict[str, Any]) -> str:
    """
    Create a JWT refresh token.
    
    Args:
        data: Payload data to encode in the token
    
    Returns:
        Encoded JWT refresh token string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    
    try:
        encoded_jwt = jwt.encode(
            to_encode,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error creating JWT refresh token: {e}")
        raise JWTError("Failed to create refresh token")


def verify_token(token: str) -> Dict[str, Any]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT token string to verify
    
    Returns:
        Decoded token payload
    
    Raises:
        JWTError: If token is invalid or expired
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        
        # Check if token has expired
        exp = payload.get("exp")
        if exp and datetime.utcnow().timestamp() > exp:
            raise JWTError("Token has expired")
        
        return payload
        
    except PyJWTError as e:
        logger.warning(f"JWT verification failed: {e}")
        raise JWTError(f"Invalid token: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during token verification: {e}")
        raise JWTError("Token verification failed")


async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> Dict[str, Any]:
    """
    Get current authenticated user from JWT token.
    
    Args:
        request: FastAPI request object
        credentials: HTTP Bearer credentials
    
    Returns:
        User information dictionary
    
    Raises:
        HTTPException: If authentication fails
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Verify the token
        payload = verify_token(credentials.credentials)
        
        # Extract user information
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        
        # Check token type (should not be refresh token)
        token_type = payload.get("type")
        if token_type == "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type for this operation",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # TODO: In a real implementation, you would fetch user data from database
        # For now, we'll use the payload data
        user_data = {
            "id": user_id,
            "email": payload.get("email"),
            "tier": payload.get("tier", "free"),
            "role": payload.get("role", "user"),
            "is_active": payload.get("is_active", True),
            "permissions": payload.get("permissions", []),
            "exp": payload.get("exp")
        }
        
        # Check if user is active
        if not user_data.get("is_active"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Inactive user",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Add user info to request state for logging
        request.state.user_id = user_id
        request.state.user_tier = user_data.get("tier")
        
        return user_data
        
    except JWTError as e:
        log_error(logger, e, {
            "operation": "get_current_user",
            "token_prefix": credentials.credentials[:10] if credentials.credentials else None
        })
        raise credentials_exception
    except HTTPException:
        raise
    except Exception as e:
        log_error(logger, e, {
            "operation": "get_current_user",
            "unexpected_error": True
        })
        raise credentials_exception


async def get_current_admin_user(
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Get current authenticated admin user.
    
    Args:
        current_user: Current authenticated user
    
    Returns:
        Admin user information dictionary
    
    Raises:
        HTTPException: If user is not an admin
    """
    user_role = current_user.get("role")
    user_permissions = current_user.get("permissions", [])
    
    # Check if user has admin role or admin permissions
    is_admin = (
        user_role == "admin" or
        user_role == "super_admin" or
        "admin" in user_permissions or
        "rag_admin" in user_permissions
    )
    
    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    
    return current_user


async def get_current_premium_user(
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Get current authenticated premium user.
    
    Args:
        current_user: Current authenticated user
    
    Returns:
        Premium user information dictionary
    
    Raises:
        HTTPException: If user is not premium
    """
    user_tier = current_user.get("tier", "free")
    
    if user_tier not in ["premium", "enterprise"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Premium subscription required"
        )
    
    return current_user


async def get_optional_user(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False))
) -> Optional[Dict[str, Any]]:
    """
    Get current user if authenticated, otherwise return None.
    Useful for endpoints that work for both authenticated and anonymous users.
    
    Args:
        request: FastAPI request object
        credentials: Optional HTTP Bearer credentials
    
    Returns:
        User information dictionary or None if not authenticated
    """
    if not credentials:
        return None
    
    try:
        return await get_current_user(request, credentials)
    except HTTPException:
        return None


def check_permission(required_permission: str):
    """
    Dependency factory to check if user has specific permission.
    
    Args:
        required_permission: Permission string to check
    
    Returns:
        Dependency function that validates permission
    """
    async def permission_checker(
        current_user: Dict[str, Any] = Depends(get_current_user)
    ) -> Dict[str, Any]:
        user_permissions = current_user.get("permissions", [])
        user_role = current_user.get("role")
        
        # Super admin has all permissions
        if user_role == "super_admin":
            return current_user
        
        # Check if user has the required permission
        if required_permission not in user_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission '{required_permission}' required"
            )
        
        return current_user
    
    return permission_checker


def check_tier(required_tier: str):
    """
    Dependency factory to check if user has required subscription tier.
    
    Args:
        required_tier: Minimum tier required (free, premium, enterprise)
    
    Returns:
        Dependency function that validates tier
    """
    tier_hierarchy = {"free": 0, "premium": 1, "enterprise": 2}
    
    async def tier_checker(
        current_user: Dict[str, Any] = Depends(get_current_user)
    ) -> Dict[str, Any]:
        user_tier = current_user.get("tier", "free")
        
        required_level = tier_hierarchy.get(required_tier, 0)
        user_level = tier_hierarchy.get(user_tier, 0)
        
        if user_level < required_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Subscription tier '{required_tier}' or higher required"
            )
        
        return current_user
    
    return tier_checker