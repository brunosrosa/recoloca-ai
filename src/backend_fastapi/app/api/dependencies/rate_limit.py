#!/usr/bin/env python3
"""
Recoloca.AI Rate Limiting Dependencies
Redis-based rate limiting for FastAPI endpoints

Author: @AgenteM_DevFastAPI
Date: 2025-06-20
Version: 1.0.0
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, Optional

import redis.asyncio as redis
from fastapi import HTTPException, Request, status

from ...core.config import settings
from ...core.logging import log_error

logger = logging.getLogger(__name__)


class RateLimiter:
    """
    Redis-based rate limiter with sliding window algorithm.
    """
    
    def __init__(self, redis_client: Optional[redis.Redis] = None):
        self.redis_client = redis_client
        self._local_cache: Dict[str, Dict[str, Any]] = {}
        self._cache_ttl = 60  # Local cache TTL in seconds
    
    async def get_redis_client(self) -> Optional[redis.Redis]:
        """Get Redis client, create if not exists."""
        if not self.redis_client and settings.REDIS_URL:
            try:
                self.redis_client = redis.from_url(
                    settings.REDIS_URL,
                    encoding="utf-8",
                    decode_responses=True,
                    socket_connect_timeout=5,
                    socket_timeout=5
                )
                # Test connection
                await self.redis_client.ping()
                logger.info("Redis connection established for rate limiting")
            except Exception as e:
                logger.warning(f"Failed to connect to Redis for rate limiting: {e}")
                self.redis_client = None
        
        return self.redis_client
    
    def _get_local_cache_key(self, identifier: str, window: str) -> str:
        """Generate local cache key."""
        return f"{identifier}:{window}"
    
    def _is_local_cache_valid(self, cache_entry: Dict[str, Any]) -> bool:
        """Check if local cache entry is still valid."""
        return (
            cache_entry and
            datetime.utcnow().timestamp() - cache_entry.get("timestamp", 0) < self._cache_ttl
        )
    
    async def _check_rate_limit_redis(
        self,
        identifier: str,
        limit: int,
        window_seconds: int
    ) -> Dict[str, Any]:
        """Check rate limit using Redis sliding window."""
        redis_client = await self.get_redis_client()
        if not redis_client:
            # Fallback to local cache if Redis is not available
            return await self._check_rate_limit_local(identifier, limit, window_seconds)
        
        current_time = datetime.utcnow().timestamp()
        window_start = current_time - window_seconds
        
        # Redis key for this identifier
        key = f"rate_limit:{identifier}"
        
        try:
            # Use Redis pipeline for atomic operations
            pipe = redis_client.pipeline()
            
            # Remove expired entries
            pipe.zremrangebyscore(key, 0, window_start)
            
            # Count current requests in window
            pipe.zcard(key)
            
            # Add current request
            pipe.zadd(key, {str(current_time): current_time})
            
            # Set expiration
            pipe.expire(key, window_seconds + 1)
            
            results = await pipe.execute()
            current_count = results[1]  # Count after removing expired entries
            
            # Check if limit exceeded
            if current_count >= limit:
                # Remove the request we just added since it's over the limit
                await redis_client.zrem(key, str(current_time))
                
                # Get the oldest request time to calculate reset time
                oldest_requests = await redis_client.zrange(key, 0, 0, withscores=True)
                if oldest_requests:
                    oldest_time = oldest_requests[0][1]
                    reset_time = oldest_time + window_seconds
                else:
                    reset_time = current_time + window_seconds
                
                return {
                    "allowed": False,
                    "limit": limit,
                    "remaining": 0,
                    "reset_time": reset_time,
                    "retry_after": max(1, int(reset_time - current_time))
                }
            
            return {
                "allowed": True,
                "limit": limit,
                "remaining": limit - current_count - 1,
                "reset_time": current_time + window_seconds,
                "retry_after": 0
            }
            
        except Exception as e:
            logger.error(f"Redis rate limiting error: {e}")
            # Fallback to local cache
            return await self._check_rate_limit_local(identifier, limit, window_seconds)
    
    async def _check_rate_limit_local(
        self,
        identifier: str,
        limit: int,
        window_seconds: int
    ) -> Dict[str, Any]:
        """Fallback rate limiting using local memory cache."""
        current_time = datetime.utcnow().timestamp()
        window_start = current_time - window_seconds
        
        cache_key = self._get_local_cache_key(identifier, str(window_seconds))
        
        # Get or create cache entry
        if cache_key not in self._local_cache:
            self._local_cache[cache_key] = {
                "requests": [],
                "timestamp": current_time
            }
        
        cache_entry = self._local_cache[cache_key]
        
        # Clean expired requests
        cache_entry["requests"] = [
            req_time for req_time in cache_entry["requests"]
            if req_time > window_start
        ]
        
        current_count = len(cache_entry["requests"])
        
        if current_count >= limit:
            # Find reset time
            if cache_entry["requests"]:
                oldest_time = min(cache_entry["requests"])
                reset_time = oldest_time + window_seconds
            else:
                reset_time = current_time + window_seconds
            
            return {
                "allowed": False,
                "limit": limit,
                "remaining": 0,
                "reset_time": reset_time,
                "retry_after": max(1, int(reset_time - current_time))
            }
        
        # Add current request
        cache_entry["requests"].append(current_time)
        cache_entry["timestamp"] = current_time
        
        return {
            "allowed": True,
            "limit": limit,
            "remaining": limit - current_count - 1,
            "reset_time": current_time + window_seconds,
            "retry_after": 0
        }
    
    async def check_rate_limit(
        self,
        identifier: str,
        limit: int,
        window_seconds: int = 60
    ) -> Dict[str, Any]:
        """
        Check if request is within rate limit.
        
        Args:
            identifier: Unique identifier for rate limiting (e.g., user_id, IP)
            limit: Maximum number of requests allowed
            window_seconds: Time window in seconds
        
        Returns:
            Dictionary with rate limit status
        """
        try:
            return await self._check_rate_limit_redis(identifier, limit, window_seconds)
        except Exception as e:
            logger.error(f"Rate limiting error: {e}")
            # In case of error, allow the request but log the issue
            return {
                "allowed": True,
                "limit": limit,
                "remaining": limit - 1,
                "reset_time": datetime.utcnow().timestamp() + window_seconds,
                "retry_after": 0,
                "error": str(e)
            }


# Global rate limiter instance
_rate_limiter = RateLimiter()


def rate_limit(
    requests_per_minute: int = 60,
    per_user: bool = True,
    per_ip: bool = False,
    tier_multipliers: Optional[Dict[str, float]] = None
) -> Callable:
    """
    Rate limiting dependency factory.
    
    Args:
        requests_per_minute: Base number of requests per minute
        per_user: Apply rate limit per authenticated user
        per_ip: Apply rate limit per IP address
        tier_multipliers: Multipliers for different user tiers
    
    Returns:
        FastAPI dependency function
    """
    if tier_multipliers is None:
        tier_multipliers = {
            "free": 1.0,
            "premium": 2.0,
            "enterprise": 5.0
        }
    
    async def rate_limit_dependency(request: Request) -> None:
        """
        Rate limiting dependency function.
        
        Raises:
            HTTPException: If rate limit is exceeded
        """
        try:
            # Determine identifier for rate limiting
            identifier_parts = []
            
            if per_user:
                user_id = getattr(request.state, 'user_id', None)
                if user_id:
                    identifier_parts.append(f"user:{user_id}")
                    
                    # Apply tier multiplier
                    user_tier = getattr(request.state, 'user_tier', 'free')
                    tier_multiplier = tier_multipliers.get(user_tier, 1.0)
                    effective_limit = int(requests_per_minute * tier_multiplier)
                else:
                    # For unauthenticated users, fall back to IP-based limiting
                    per_ip_fallback = True
                    effective_limit = requests_per_minute
            else:
                effective_limit = requests_per_minute
            
            if per_ip or (per_user and not getattr(request.state, 'user_id', None)):
                client_ip = request.client.host if request.client else "unknown"
                # Handle forwarded headers
                forwarded_for = request.headers.get("X-Forwarded-For")
                if forwarded_for:
                    client_ip = forwarded_for.split(",")[0].strip()
                identifier_parts.append(f"ip:{client_ip}")
            
            if not identifier_parts:
                # No valid identifier, skip rate limiting
                return
            
            identifier = ":".join(identifier_parts)
            
            # Add endpoint to identifier for more granular control
            endpoint = f"{request.method}:{request.url.path}"
            full_identifier = f"{identifier}:{endpoint}"
            
            # Check rate limit
            result = await _rate_limiter.check_rate_limit(
                identifier=full_identifier,
                limit=effective_limit,
                window_seconds=60  # 1 minute window
            )
            
            # Add rate limit headers to response
            if hasattr(request.state, 'rate_limit_headers'):
                request.state.rate_limit_headers.update({
                    "X-RateLimit-Limit": str(result["limit"]),
                    "X-RateLimit-Remaining": str(result["remaining"]),
                    "X-RateLimit-Reset": str(int(result["reset_time"]))
                })
            else:
                request.state.rate_limit_headers = {
                    "X-RateLimit-Limit": str(result["limit"]),
                    "X-RateLimit-Remaining": str(result["remaining"]),
                    "X-RateLimit-Reset": str(int(result["reset_time"]))
                }
            
            if not result["allowed"]:
                # Log rate limit exceeded
                logger.warning(
                    f"Rate limit exceeded for {identifier}",
                    extra={
                        "identifier": identifier,
                        "endpoint": endpoint,
                        "limit": result["limit"],
                        "retry_after": result["retry_after"]
                    }
                )
                
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail={
                        "error": "Rate limit exceeded",
                        "limit": result["limit"],
                        "retry_after": result["retry_after"],
                        "reset_time": result["reset_time"]
                    },
                    headers={
                        "Retry-After": str(result["retry_after"]),
                        "X-RateLimit-Limit": str(result["limit"]),
                        "X-RateLimit-Remaining": "0",
                        "X-RateLimit-Reset": str(int(result["reset_time"]))
                    }
                )
            
        except HTTPException:
            raise
        except Exception as e:
            log_error(logger, e, {
                "operation": "rate_limit_dependency",
                "endpoint": f"{request.method}:{request.url.path}"
            })
            # In case of error, allow the request to proceed
            pass
    
    return rate_limit_dependency


# Predefined rate limit configurations
def rag_query_rate_limit() -> Callable:
    """Rate limit for RAG query endpoints."""
    return rate_limit(
        requests_per_minute=30,
        per_user=True,
        tier_multipliers={
            "free": 1.0,
            "premium": 3.0,
            "enterprise": 10.0
        }
    )


def rag_admin_rate_limit() -> Callable:
    """Rate limit for RAG admin endpoints."""
    return rate_limit(
        requests_per_minute=10,
        per_user=True,
        tier_multipliers={
            "free": 1.0,
            "premium": 1.0,
            "enterprise": 2.0
        }
    )


def general_api_rate_limit() -> Callable:
    """General rate limit for API endpoints."""
    return rate_limit(
        requests_per_minute=100,
        per_user=True,
        tier_multipliers={
            "free": 1.0,
            "premium": 2.0,
            "enterprise": 5.0
        }
    )