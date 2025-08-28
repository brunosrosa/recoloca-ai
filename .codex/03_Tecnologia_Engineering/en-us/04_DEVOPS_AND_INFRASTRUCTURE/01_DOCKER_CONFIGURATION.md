---
title: "Docker Configuration - Recoloca.ai"
doc_id: "DOCKER-CONFIGURATION-RECOLOCA"
version: "1.0"
last_updated: "2025-01-20 15:40:00"
timezone: "America/Sao_Paulo"
status: "Active"
owner: "@DevOpsTeam"
tags: [docker, containers, infrastructure, deployment, microservices]
description: "Complete Docker configuration for the Recoloca.ai platform, including Dockerfiles, docker-compose, and container orchestration setup."
---

# Docker Configuration - Recoloca.ai

## 📋 Overview

This document provides comprehensive Docker configuration for the **Recoloca.ai** platform, including containerization strategies, multi-stage builds, and orchestration setup for development, staging, and production environments.

## 🎯 Objectives

- **Consistency**: Identical environments across development, staging, and production
- **Scalability**: Easy horizontal scaling of services
- **Isolation**: Proper service isolation and resource management
- **Security**: Secure container configurations and best practices
- **Performance**: Optimized container images and resource usage

---

## 🐳 Backend Service (FastAPI)

### Dockerfile

```dockerfile
# Multi-stage build for Python backend
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim as production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/home/appuser/.local/bin:$PATH

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

# Copy Python packages from builder stage
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Set working directory and switch to non-root user
WORKDIR /app
USER appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Start application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### .dockerignore

```dockerignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
.venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Git
.git/
.gitignore

# Documentation
*.md
docs/

# Tests
tests/
.pytest_cache/
.coverage
htmlcov/

# Environment files
.env
.env.local
.env.*.local

# Logs
logs/
*.log

# Docker
Dockerfile*
docker-compose*.yml
.dockerignore
```

---

## 🌐 Frontend Service (Next.js)

### Dockerfile

```dockerfile
# Multi-stage build for Next.js frontend
FROM node:18-alpine AS base

# Install dependencies only when needed
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./
RUN npm ci --only=production

# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Set build-time environment variables
ARG NEXT_PUBLIC_API_URL
ARG NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=$NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY

# Build application
RUN npm run build

# Production image, copy all the files and run next
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production

# Create non-root user
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copy built application
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

# Switch to non-root user
USER nextjs

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/api/health || exit 1

# Expose port
EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

# Start application
CMD ["node", "server.js"]
```

### next.config.js (for standalone build)

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  experimental: {
    outputFileTracingRoot: undefined,
  },
  // Other Next.js configurations
}

module.exports = nextConfig
```

---

## 🗄️ Database Services

### PostgreSQL Configuration

```dockerfile
# Custom PostgreSQL with extensions
FROM postgres:15-alpine

# Install additional extensions
RUN apk add --no-cache postgresql-contrib

# Copy initialization scripts
COPY ./docker/postgres/init/ /docker-entrypoint-initdb.d/

# Set custom configuration
COPY ./docker/postgres/postgresql.conf /etc/postgresql/postgresql.conf
COPY ./docker/postgres/pg_hba.conf /etc/postgresql/pg_hba.conf

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD pg_isready -U $POSTGRES_USER -d $POSTGRES_DB || exit 1

EXPOSE 5432
```

### Redis Configuration

```dockerfile
# Custom Redis configuration
FROM redis:7-alpine

# Copy custom configuration
COPY ./docker/redis/redis.conf /usr/local/etc/redis/redis.conf

# Create non-root user
RUN addgroup -g 1001 -S redis && \
    adduser -S -D -H -u 1001 -h /var/empty -s /sbin/nologin -G redis -g redis redis

# Set ownership
RUN chown redis:redis /usr/local/etc/redis/redis.conf

# Switch to non-root user
USER redis

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD redis-cli ping || exit 1

EXPOSE 6379

# Start Redis with custom config
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
```

---

## 🔧 Docker Compose Configurations

### Development Environment

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
      target: builder  # Use builder stage for development
    container_name: recoloca-backend-dev
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=development
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/recoloca_dev
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=dev-secret-key-change-in-production
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - STRIPE_SECRET_KEY=${STRIPE_SECRET_KEY}
    volumes:
      - ./backend:/app
      - backend_cache:/home/appuser/.cache
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - recoloca-network
    restart: unless-stopped
    command: [
      "uvicorn", "app.main:app", 
      "--host", "0.0.0.0", 
      "--port", "8000", 
      "--reload", 
      "--log-level", "debug"
    ]

  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: deps  # Use deps stage for development
    container_name: recoloca-frontend-dev
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
      - NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=${NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY}
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - frontend_cache:/app/.next
    depends_on:
      - backend
    networks:
      - recoloca-network
    restart: unless-stopped
    command: ["npm", "run", "dev"]

  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    container_name: recoloca-postgres-dev
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_DB=recoloca_dev
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_INITDB_ARGS=--encoding=UTF-8 --lc-collate=C --lc-ctype=C
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/postgres/init:/docker-entrypoint-initdb.d
    networks:
      - recoloca-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d recoloca_dev"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: recoloca-redis-dev
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
      - ./docker/redis/redis.conf:/usr/local/etc/redis/redis.conf
    networks:
      - recoloca-network
    restart: unless-stopped
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s

  # Monitoring - Prometheus
  prometheus:
    image: prom/prometheus:latest
    container_name: recoloca-prometheus-dev
    ports:
      - "9090:9090"
    volumes:
      - ./docker/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    networks:
      - recoloca-network
    restart: unless-stopped
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'

  # Monitoring - Grafana
  grafana:
    image: grafana/grafana:latest
    container_name: recoloca-grafana-dev
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
      - ./docker/grafana/provisioning:/etc/grafana/provisioning
    networks:
      - recoloca-network
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
  backend_cache:
  frontend_cache:

networks:
  recoloca-network:
    driver: bridge
```

### Production Environment

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  # Reverse Proxy - Nginx
  nginx:
    image: nginx:alpine
    container_name: recoloca-nginx-prod
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./docker/nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./docker/nginx/conf.d:/etc/nginx/conf.d
      - ./docker/ssl:/etc/nginx/ssl
      - nginx_logs:/var/log/nginx
    depends_on:
      - backend
      - frontend
    networks:
      - recoloca-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 5s
      retries: 3

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
      target: production
    container_name: recoloca-backend-prod
    environment:
      - ENVIRONMENT=production
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
      - SECRET_KEY=${SECRET_KEY}
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - STRIPE_SECRET_KEY=${STRIPE_SECRET_KEY}
      - SENTRY_DSN=${SENTRY_DSN}
    volumes:
      - backend_logs:/app/logs
      - uploaded_files:/app/uploads
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - recoloca-network
    restart: unless-stopped
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: runner
      args:
        - NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
        - NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=${NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY}
    container_name: recoloca-frontend-prod
    environment:
      - NODE_ENV=production
    networks:
      - recoloca-network
    restart: unless-stopped
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    container_name: recoloca-postgres-prod
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - postgres_backups:/backups
      - ./docker/postgres/init:/docker-entrypoint-initdb.d
    networks:
      - recoloca-network
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 2G
        reservations:
          cpus: '1.0'
          memory: 1G
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: recoloca-redis-prod
    volumes:
      - redis_data:/data
      - ./docker/redis/redis.conf:/usr/local/etc/redis/redis.conf
    networks:
      - recoloca-network
    restart: unless-stopped
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s

  # Backup Service
  backup:
    build:
      context: ./docker/backup
      dockerfile: Dockerfile
    container_name: recoloca-backup-prod
    environment:
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
      - AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
      - S3_BUCKET=${BACKUP_S3_BUCKET}
    volumes:
      - postgres_backups:/backups
    depends_on:
      - postgres
    networks:
      - recoloca-network
    restart: unless-stopped

volumes:
  postgres_data:
  postgres_backups:
  redis_data:
  nginx_logs:
  backend_logs:
  uploaded_files:

networks:
  recoloca-network:
    driver: bridge
```

---

## 🔧 Configuration Files

### Nginx Configuration

```nginx
# docker/nginx/nginx.conf
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 1024;
    use epoll;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging format
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for" '
                    'rt=$request_time uct="$upstream_connect_time" '
                    'uht="$upstream_header_time" urt="$upstream_response_time"';

    access_log /var/log/nginx/access.log main;

    # Performance settings
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    client_max_body_size 10M;

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/json
        application/javascript
        application/xml+rss
        application/atom+xml
        image/svg+xml;

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;

    # Include server configurations
    include /etc/nginx/conf.d/*.conf;
}
```

```nginx
# docker/nginx/conf.d/default.conf
upstream backend {
    least_conn;
    server backend:8000 max_fails=3 fail_timeout=30s;
}

upstream frontend {
    least_conn;
    server frontend:3000 max_fails=3 fail_timeout=30s;
}

server {
    listen 80;
    server_name recoloca.ai www.recoloca.ai;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self' https://api.stripe.com;" always;

    # API routes
    location /api/ {
        limit_req zone=api burst=20 nodelay;
        
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
        
        # Buffer settings
        proxy_buffering on;
        proxy_buffer_size 4k;
        proxy_buffers 8 4k;
    }

    # Authentication endpoints with stricter rate limiting
    location /api/v1/auth/ {
        limit_req zone=login burst=5 nodelay;
        
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Frontend routes
    location / {
        proxy_pass http://frontend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support for Next.js dev
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # Health check endpoint
    location /health {
        access_log off;
        return 200 "healthy\n";
        add_header Content-Type text/plain;
    }

    # Static files caching
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        add_header Vary Accept-Encoding;
    }
}
```

### Redis Configuration

```conf
# docker/redis/redis.conf
# Network
bind 0.0.0.0
port 6379
protected-mode yes

# General
daemonize no
supervised no
pidfile /var/run/redis_6379.pid
loglevel notice
logfile ""
databases 16

# Snapshotting
save 900 1
save 300 10
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb
dir /data

# Replication
# replica-serve-stale-data yes
# replica-read-only yes

# Security
# requirepass your_redis_password_here

# Memory management
maxmemory 256mb
maxmemory-policy allkeys-lru

# Append only file
appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

# Slow log
slowlog-log-slower-than 10000
slowlog-max-len 128

# Client output buffer limits
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit replica 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60

# TCP keepalive
tcp-keepalive 300
```

### Prometheus Configuration

```yaml
# docker/prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'recoloca-backend'
    static_configs:
      - targets: ['backend:8000']
    metrics_path: '/metrics'
    scrape_interval: 30s

  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres:5432']
    scrape_interval: 30s

  - job_name: 'redis'
    static_configs:
      - targets: ['redis:6379']
    scrape_interval: 30s

  - job_name: 'nginx'
    static_configs:
      - targets: ['nginx:80']
    scrape_interval: 30s
```

---

## 🚀 Deployment Scripts

### Development Deployment

```bash
#!/bin/bash
# scripts/deploy-dev.sh

set -e

echo "🚀 Starting Recoloca.ai Development Deployment"

# Load environment variables
if [ -f .env.dev ]; then
    export $(cat .env.dev | xargs)
else
    echo "❌ .env.dev file not found"
    exit 1
fi

# Build and start services
echo "📦 Building and starting services..."
docker-compose -f docker-compose.dev.yml down --remove-orphans
docker-compose -f docker-compose.dev.yml build --no-cache
docker-compose -f docker-compose.dev.yml up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be healthy..."
sleep 30

# Run database migrations
echo "🗄️ Running database migrations..."
docker-compose -f docker-compose.dev.yml exec backend alembic upgrade head

# Check service health
echo "🔍 Checking service health..."
docker-compose -f docker-compose.dev.yml ps

# Show logs
echo "📋 Recent logs:"
docker-compose -f docker-compose.dev.yml logs --tail=50

echo "✅ Development deployment completed!"
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📊 Grafana: http://localhost:3001 (admin/admin)"
echo "📈 Prometheus: http://localhost:9090"
```

### Production Deployment

```bash
#!/bin/bash
# scripts/deploy-prod.sh

set -e

echo "🚀 Starting Recoloca.ai Production Deployment"

# Load environment variables
if [ -f .env.prod ]; then
    export $(cat .env.prod | xargs)
else
    echo "❌ .env.prod file not found"
    exit 1
fi

# Pre-deployment checks
echo "🔍 Running pre-deployment checks..."
./scripts/pre-deploy-checks.sh

# Backup database
echo "💾 Creating database backup..."
./scripts/backup-database.sh

# Build images
echo "📦 Building production images..."
docker-compose -f docker-compose.prod.yml build --no-cache

# Deploy with zero downtime
echo "🔄 Deploying with zero downtime..."
docker-compose -f docker-compose.prod.yml up -d --remove-orphans

# Wait for services
echo "⏳ Waiting for services to be ready..."
sleep 60

# Run migrations
echo "🗄️ Running database migrations..."
docker-compose -f docker-compose.prod.yml exec backend alembic upgrade head

# Health checks
echo "🔍 Running health checks..."
./scripts/health-check.sh

# Cleanup old images
echo "🧹 Cleaning up old images..."
docker image prune -f

echo "✅ Production deployment completed successfully!"
```

### Health Check Script

```bash
#!/bin/bash
# scripts/health-check.sh

set -e

echo "🔍 Running health checks..."

# Check backend health
echo "Checking backend health..."
for i in {1..30}; do
    if curl -f http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ Backend is healthy"
        break
    fi
    echo "⏳ Waiting for backend... ($i/30)"
    sleep 2
done

# Check frontend health
echo "Checking frontend health..."
for i in {1..30}; do
    if curl -f http://localhost:3000/api/health > /dev/null 2>&1; then
        echo "✅ Frontend is healthy"
        break
    fi
    echo "⏳ Waiting for frontend... ($i/30)"
    sleep 2
done

# Check database connectivity
echo "Checking database connectivity..."
if docker-compose exec postgres pg_isready -U $POSTGRES_USER -d $POSTGRES_DB > /dev/null 2>&1; then
    echo "✅ Database is healthy"
else
    echo "❌ Database health check failed"
    exit 1
fi

# Check Redis connectivity
echo "Checking Redis connectivity..."
if docker-compose exec redis redis-cli ping > /dev/null 2>&1; then
    echo "✅ Redis is healthy"
else
    echo "❌ Redis health check failed"
    exit 1
fi

echo "✅ All health checks passed!"
```

---

## 📊 Monitoring and Logging

### Docker Logging Configuration

```yaml
# Add to each service in docker-compose files
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
    labels: "service,environment"
```

### Log Aggregation with ELK Stack

```yaml
# docker-compose.logging.yml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    container_name: recoloca-elasticsearch
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - xpack.security.enabled=false
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data
    ports:
      - "9200:9200"
    networks:
      - recoloca-network

  logstash:
    image: docker.elastic.co/logstash/logstash:8.5.0
    container_name: recoloca-logstash
    volumes:
      - ./docker/logstash/pipeline:/usr/share/logstash/pipeline
      - ./docker/logstash/config:/usr/share/logstash/config
    ports:
      - "5044:5044"
    depends_on:
      - elasticsearch
    networks:
      - recoloca-network

  kibana:
    image: docker.elastic.co/kibana/kibana:8.5.0
    container_name: recoloca-kibana
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on:
      - elasticsearch
    networks:
      - recoloca-network

volumes:
  elasticsearch_data:

networks:
  recoloca-network:
    external: true
```

---

## 🔒 Security Best Practices

### Security Scanning

```bash
#!/bin/bash
# scripts/security-scan.sh

echo "🔒 Running security scans..."

# Scan Docker images for vulnerabilities
echo "Scanning backend image..."
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image recoloca-backend:latest

echo "Scanning frontend image..."
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image recoloca-frontend:latest

# Check for secrets in code
echo "Scanning for secrets..."
docker run --rm -v "$(pwd):/code" \
    trufflesecurity/trufflehog:latest filesystem /code

echo "✅ Security scan completed"
```

### Environment Variables Template

```bash
# .env.example
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/recoloca_prod
POSTGRES_DB=recoloca_prod
POSTGRES_USER=username
POSTGRES_PASSWORD=secure_password

# Redis
REDIS_URL=redis://localhost:6379/0

# Application
SECRET_KEY=your-super-secret-key-here
ENVIRONMENT=production

# External APIs
GEMINI_API_KEY=your-gemini-api-key
STRIPE_SECRET_KEY=sk_live_your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

# Frontend
NEXT_PUBLIC_API_URL=https://api.recoloca.ai/v1
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_your_stripe_publishable_key

# Monitoring
SENTRY_DSN=https://your-sentry-dsn

# Backup
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
BACKUP_S3_BUCKET=recoloca-backups
```

---

## 🔗 Related Documents

- [[CI_CD_Pipeline.md]] - Continuous Integration/Deployment
- [[Infrastructure_as_Code.md]] - Terraform Configuration
- [[Monitoring_and_Alerting.md]] - Observability Setup
- [[Security_Guidelines.md]] - Security Best Practices
- [[Backup_and_Recovery.md]] - Data Protection Strategy
- [[Performance_Optimization.md]] - Performance Tuning

---

**Document Status**: Active  
**Next Review Date**: 2025-03-20  
**Maintained By**: @DevOpsTeam