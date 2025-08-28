---
title: "CI/CD Pipeline - Recoloca.ai"
doc_id: "CICD-PIPELINE-RECOLOCA"
version: "1.0"
last_updated: "2025-01-20 15:45:00"
timezone: "America/Sao_Paulo"
status: "Active"
owner: "@DevOpsTeam"
tags: [cicd, github-actions, deployment, automation, testing]
description: "Complete CI/CD pipeline configuration for the Recoloca.ai platform using GitHub Actions, including automated testing, building, and deployment workflows."
---

# CI/CD Pipeline - Recoloca.ai

## 📋 Overview

This document defines the **Continuous Integration and Continuous Deployment (CI/CD)** pipeline for the **Recoloca.ai** platform. The pipeline automates testing, building, security scanning, and deployment processes using **GitHub Actions**.

## 🎯 Objectives

- **Automation**: Fully automated testing, building, and deployment processes
- **Quality Assurance**: Comprehensive testing and code quality checks
- **Security**: Automated security scanning and vulnerability detection
- **Reliability**: Consistent and repeatable deployments
- **Speed**: Fast feedback loops and efficient deployment cycles
- **Rollback**: Safe deployment with automatic rollback capabilities

---

## 🏗️ Pipeline Architecture

### Pipeline Stages

```mermaid
graph LR
    A[Code Push] --> B[Lint & Format]
    B --> C[Unit Tests]
    C --> D[Integration Tests]
    D --> E[Security Scan]
    E --> F[Build Images]
    F --> G[Deploy to Staging]
    G --> H[E2E Tests]
    H --> I[Deploy to Production]
    I --> J[Health Checks]
    J --> K[Notify Team]
```

### Environments

- **Development**: Feature branches, pull requests
- **Staging**: Main branch, pre-production testing
- **Production**: Tagged releases, live environment

---

## 🔄 GitHub Actions Workflows

### Main CI/CD Workflow

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
    tags: ['v*']
  pull_request:
    branches: [main, develop]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  NODE_VERSION: '18'
  PYTHON_VERSION: '3.11'

jobs:
  # Code Quality and Linting
  lint-and-format:
    name: 🔍 Lint and Format
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'
          cache-dependency-path: backend/requirements.txt

      - name: Install frontend dependencies
        working-directory: ./frontend
        run: npm ci

      - name: Install backend dependencies
        working-directory: ./backend
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      - name: Lint frontend (ESLint)
        working-directory: ./frontend
        run: npm run lint

      - name: Format frontend (Prettier)
        working-directory: ./frontend
        run: npm run format:check

      - name: Type check frontend
        working-directory: ./frontend
        run: npm run type-check

      - name: Lint backend (Flake8)
        working-directory: ./backend
        run: flake8 .

      - name: Format backend (Black)
        working-directory: ./backend
        run: black --check .

      - name: Sort imports (isort)
        working-directory: ./backend
        run: isort --check-only .

      - name: Type check backend (mypy)
        working-directory: ./backend
        run: mypy .

  # Unit Tests
  unit-tests:
    name: 🧪 Unit Tests
    runs-on: ubuntu-latest
    needs: lint-and-format
    
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
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'
          cache-dependency-path: backend/requirements.txt

      - name: Install frontend dependencies
        working-directory: ./frontend
        run: npm ci

      - name: Install backend dependencies
        working-directory: ./backend
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      - name: Run frontend tests
        working-directory: ./frontend
        run: npm run test:ci
        env:
          CI: true

      - name: Run backend tests
        working-directory: ./backend
        run: |
          pytest --cov=app --cov-report=xml --cov-report=html
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379/0
          SECRET_KEY: test-secret-key
          ENVIRONMENT: testing

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./backend/coverage.xml,./frontend/coverage/lcov.info
          flags: unittests
          name: codecov-umbrella

  # Security Scanning
  security-scan:
    name: 🔒 Security Scan
    runs-on: ubuntu-latest
    needs: lint-and-format
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy scan results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/secrets
            p/python
            p/typescript
        env:
          SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}

      - name: Scan for secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main
          head: HEAD

  # Build Docker Images
  build-images:
    name: 🐳 Build Images
    runs-on: ubuntu-latest
    needs: [unit-tests, security-scan]
    if: github.event_name != 'pull_request'
    
    outputs:
      backend-image: ${{ steps.backend-meta.outputs.tags }}
      frontend-image: ${{ steps.frontend-meta.outputs.tags }}
      backend-digest: ${{ steps.backend-build.outputs.digest }}
      frontend-digest: ${{ steps.frontend-build.outputs.digest }}
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract backend metadata
        id: backend-meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-backend
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix={{branch}}-

      - name: Extract frontend metadata
        id: frontend-meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-frontend
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix={{branch}}-

      - name: Build and push backend image
        id: backend-build
        uses: docker/build-push-action@v5
        with:
          context: ./backend
          file: ./backend/Dockerfile
          push: true
          tags: ${{ steps.backend-meta.outputs.tags }}
          labels: ${{ steps.backend-meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64

      - name: Build and push frontend image
        id: frontend-build
        uses: docker/build-push-action@v5
        with:
          context: ./frontend
          file: ./frontend/Dockerfile
          push: true
          tags: ${{ steps.frontend-meta.outputs.tags }}
          labels: ${{ steps.frontend-meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64
          build-args: |
            NEXT_PUBLIC_API_URL=${{ secrets.STAGING_API_URL }}
            NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=${{ secrets.STRIPE_PUBLISHABLE_KEY }}

  # Deploy to Staging
  deploy-staging:
    name: 🚀 Deploy to Staging
    runs-on: ubuntu-latest
    needs: build-images
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.recoloca.ai
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup SSH
        uses: webfactory/ssh-agent@v0.7.0
        with:
          ssh-private-key: ${{ secrets.STAGING_SSH_KEY }}

      - name: Deploy to staging server
        run: |
          ssh -o StrictHostKeyChecking=no ${{ secrets.STAGING_USER }}@${{ secrets.STAGING_HOST }} << 'EOF'
            cd /opt/recoloca-staging
            
            # Pull latest images
            docker pull ${{ needs.build-images.outputs.backend-image }}
            docker pull ${{ needs.build-images.outputs.frontend-image }}
            
            # Update docker-compose with new image tags
            sed -i 's|image: .*backend.*|image: ${{ needs.build-images.outputs.backend-image }}|' docker-compose.staging.yml
            sed -i 's|image: .*frontend.*|image: ${{ needs.build-images.outputs.frontend-image }}|' docker-compose.staging.yml
            
            # Deploy with zero downtime
            docker-compose -f docker-compose.staging.yml up -d --remove-orphans
            
            # Run migrations
            docker-compose -f docker-compose.staging.yml exec -T backend alembic upgrade head
            
            # Health check
            sleep 30
            curl -f https://staging.recoloca.ai/health || exit 1
          EOF

      - name: Run staging smoke tests
        run: |
          # Wait for deployment to stabilize
          sleep 60
          
          # Basic health checks
          curl -f https://staging.recoloca.ai/health
          curl -f https://staging.recoloca.ai/api/v1/health
          
          # API endpoint tests
          curl -f https://staging.recoloca.ai/api/v1/auth/health

  # End-to-End Tests
  e2e-tests:
    name: 🎭 E2E Tests
    runs-on: ubuntu-latest
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          cache-dependency-path: e2e/package-lock.json

      - name: Install Playwright
        working-directory: ./e2e
        run: |
          npm ci
          npx playwright install --with-deps

      - name: Run E2E tests
        working-directory: ./e2e
        run: npx playwright test
        env:
          BASE_URL: https://staging.recoloca.ai
          TEST_USER_EMAIL: ${{ secrets.TEST_USER_EMAIL }}
          TEST_USER_PASSWORD: ${{ secrets.TEST_USER_PASSWORD }}

      - name: Upload E2E test results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: e2e-test-results
          path: e2e/test-results/
          retention-days: 7

  # Deploy to Production
  deploy-production:
    name: 🌟 Deploy to Production
    runs-on: ubuntu-latest
    needs: [build-images, e2e-tests]
    if: startsWith(github.ref, 'refs/tags/v')
    environment:
      name: production
      url: https://recoloca.ai
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup SSH
        uses: webfactory/ssh-agent@v0.7.0
        with:
          ssh-private-key: ${{ secrets.PRODUCTION_SSH_KEY }}

      - name: Create database backup
        run: |
          ssh -o StrictHostKeyChecking=no ${{ secrets.PRODUCTION_USER }}@${{ secrets.PRODUCTION_HOST }} << 'EOF'
            cd /opt/recoloca-production
            ./scripts/backup-database.sh
          EOF

      - name: Deploy to production server
        run: |
          ssh -o StrictHostKeyChecking=no ${{ secrets.PRODUCTION_USER }}@${{ secrets.PRODUCTION_HOST }} << 'EOF'
            cd /opt/recoloca-production
            
            # Pull latest images
            docker pull ${{ needs.build-images.outputs.backend-image }}
            docker pull ${{ needs.build-images.outputs.frontend-image }}
            
            # Update docker-compose with new image tags
            sed -i 's|image: .*backend.*|image: ${{ needs.build-images.outputs.backend-image }}|' docker-compose.prod.yml
            sed -i 's|image: .*frontend.*|image: ${{ needs.build-images.outputs.frontend-image }}|' docker-compose.prod.yml
            
            # Deploy with zero downtime
            docker-compose -f docker-compose.prod.yml up -d --remove-orphans
            
            # Run migrations
            docker-compose -f docker-compose.prod.yml exec -T backend alembic upgrade head
            
            # Health check
            sleep 60
            curl -f https://recoloca.ai/health || exit 1
          EOF

      - name: Run production health checks
        run: |
          # Wait for deployment to stabilize
          sleep 120
          
          # Comprehensive health checks
          curl -f https://recoloca.ai/health
          curl -f https://recoloca.ai/api/v1/health
          
          # Check critical endpoints
          curl -f https://recoloca.ai/api/v1/auth/health
          curl -f https://recoloca.ai/api/v1/users/health

      - name: Rollback on failure
        if: failure()
        run: |
          ssh -o StrictHostKeyChecking=no ${{ secrets.PRODUCTION_USER }}@${{ secrets.PRODUCTION_HOST }} << 'EOF'
            cd /opt/recoloca-production
            ./scripts/rollback.sh
          EOF

  # Notification
  notify:
    name: 📢 Notify Team
    runs-on: ubuntu-latest
    needs: [deploy-staging, deploy-production]
    if: always()
    
    steps:
      - name: Notify Slack on success
        if: success()
        uses: 8398a7/action-slack@v3
        with:
          status: success
          channel: '#deployments'
          text: |
            ✅ Deployment successful!
            
            **Repository**: ${{ github.repository }}
            **Branch**: ${{ github.ref_name }}
            **Commit**: ${{ github.sha }}
            **Author**: ${{ github.actor }}
            
            🚀 Staging: https://staging.recoloca.ai
            🌟 Production: https://recoloca.ai
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}

      - name: Notify Slack on failure
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: failure
          channel: '#deployments'
          text: |
            ❌ Deployment failed!
            
            **Repository**: ${{ github.repository }}
            **Branch**: ${{ github.ref_name }}
            **Commit**: ${{ github.sha }}
            **Author**: ${{ github.actor }}
            
            Please check the GitHub Actions logs for details.
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

---

## 🔧 Additional Workflows

### Dependency Updates

```yaml
# .github/workflows/dependency-updates.yml
name: Dependency Updates

on:
  schedule:
    - cron: '0 2 * * 1'  # Every Monday at 2 AM
  workflow_dispatch:

jobs:
  update-dependencies:
    name: 📦 Update Dependencies
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Update frontend dependencies
        working-directory: ./frontend
        run: |
          npm update
          npm audit fix

      - name: Update backend dependencies
        working-directory: ./backend
        run: |
          pip install --upgrade pip
          pip-review --auto

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'chore: update dependencies'
          title: 'chore: automated dependency updates'
          body: |
            This PR contains automated dependency updates.
            
            Please review the changes and ensure all tests pass before merging.
          branch: chore/dependency-updates
          delete-branch: true
```

### Performance Testing

```yaml
# .github/workflows/performance-tests.yml
name: Performance Tests

on:
  schedule:
    - cron: '0 4 * * *'  # Daily at 4 AM
  workflow_dispatch:

jobs:
  performance-tests:
    name: ⚡ Performance Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Install k6
        run: |
          sudo gpg -k
          sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
          echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
          sudo apt-get update
          sudo apt-get install k6

      - name: Run load tests
        run: |
          k6 run --out json=results.json tests/performance/load-test.js
        env:
          BASE_URL: https://staging.recoloca.ai

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: performance-test-results
          path: results.json

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('results.json', 'utf8'));
            
            const comment = `## ⚡ Performance Test Results
            
            - **Average Response Time**: ${results.metrics.http_req_duration.avg}ms
            - **95th Percentile**: ${results.metrics.http_req_duration['p(95)']}ms
            - **Requests per Second**: ${results.metrics.http_reqs.rate}
            - **Error Rate**: ${results.metrics.http_req_failed.rate * 100}%
            `;
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

### Security Monitoring

```yaml
# .github/workflows/security-monitoring.yml
name: Security Monitoring

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM
  workflow_dispatch:

jobs:
  security-scan:
    name: 🔒 Security Scan
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run OWASP ZAP scan
        uses: zaproxy/action-full-scan@v0.4.0
        with:
          target: 'https://staging.recoloca.ai'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a'

      - name: Run dependency vulnerability scan
        run: |
          # Frontend
          cd frontend
          npm audit --audit-level high
          
          # Backend
          cd ../backend
          pip install safety
          safety check

      - name: Upload security report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: security-report
          path: report_html.html
```

---

## 📊 Monitoring and Metrics

### Deployment Metrics

```yaml
# .github/workflows/metrics.yml
name: Deployment Metrics

on:
  workflow_run:
    workflows: ["CI/CD Pipeline"]
    types: [completed]

jobs:
  collect-metrics:
    name: 📊 Collect Metrics
    runs-on: ubuntu-latest
    
    steps:
      - name: Collect deployment metrics
        uses: actions/github-script@v6
        with:
          script: |
            const { data: workflow } = await github.rest.actions.getWorkflowRun({
              owner: context.repo.owner,
              repo: context.repo.repo,
              run_id: context.payload.workflow_run.id
            });
            
            const metrics = {
              deployment_time: new Date(workflow.updated_at) - new Date(workflow.created_at),
              success: workflow.conclusion === 'success',
              branch: workflow.head_branch,
              commit: workflow.head_sha
            };
            
            // Send metrics to monitoring system
            console.log('Deployment metrics:', metrics);

      - name: Update deployment dashboard
        run: |
          # Update Grafana dashboard or send to monitoring system
          echo "Updating deployment metrics dashboard"
```

---

## 🚨 Rollback Procedures

### Automatic Rollback Script

```bash
#!/bin/bash
# scripts/rollback.sh

set -e

echo "🔄 Starting rollback procedure..."

# Get previous successful deployment
PREVIOUS_TAG=$(docker images --format "table {{.Repository}}:{{.Tag}}" | grep recoloca | head -2 | tail -1 | cut -d':' -f2)

if [ -z "$PREVIOUS_TAG" ]; then
    echo "❌ No previous deployment found for rollback"
    exit 1
fi

echo "📦 Rolling back to: $PREVIOUS_TAG"

# Update docker-compose with previous tags
sed -i "s|image: .*backend.*|image: ghcr.io/recoloca/recoloca-backend:$PREVIOUS_TAG|" docker-compose.prod.yml
sed -i "s|image: .*frontend.*|image: ghcr.io/recoloca/recoloca-frontend:$PREVIOUS_TAG|" docker-compose.prod.yml

# Deploy previous version
docker-compose -f docker-compose.prod.yml up -d --remove-orphans

# Wait and health check
sleep 60
if curl -f https://recoloca.ai/health > /dev/null 2>&1; then
    echo "✅ Rollback successful"
else
    echo "❌ Rollback failed - manual intervention required"
    exit 1
fi

echo "📢 Notifying team about rollback"
# Send notification to team
```

---

## 🔐 Secrets Management

### Required GitHub Secrets

```bash
# Production Environment
PRODUCTION_SSH_KEY          # SSH private key for production server
PRODUCTION_HOST             # Production server hostname
PRODUCTION_USER             # Production server username

# Staging Environment
STAGING_SSH_KEY             # SSH private key for staging server
STAGING_HOST                # Staging server hostname
STAGING_USER                # Staging server username
STAGING_API_URL             # Staging API URL

# Application Secrets
SECRET_KEY                  # Application secret key
GEMINI_API_KEY              # Google Gemini API key
STRIPE_SECRET_KEY           # Stripe secret key
STRIPE_PUBLISHABLE_KEY      # Stripe publishable key
STRIPE_WEBHOOK_SECRET       # Stripe webhook secret

# Database
DATABASE_URL                # Production database URL
REDIS_URL                   # Production Redis URL

# Monitoring
SENTRY_DSN                  # Sentry DSN for error tracking
SLACK_WEBHOOK_URL           # Slack webhook for notifications

# Testing
TEST_USER_EMAIL             # Test user email for E2E tests
TEST_USER_PASSWORD          # Test user password for E2E tests

# Security
SEMGREP_APP_TOKEN           # Semgrep token for security scanning

# Backup
AWS_ACCESS_KEY_ID           # AWS access key for backups
AWS_SECRET_ACCESS_KEY       # AWS secret key for backups
BACKUP_S3_BUCKET            # S3 bucket for backups
```

### Environment Variables Template

```bash
# .env.staging
ENVIRONMENT=staging
DATABASE_URL=postgresql://user:pass@staging-db:5432/recoloca_staging
REDIS_URL=redis://staging-redis:6379/0
SECRET_KEY=staging-secret-key
GEMINI_API_KEY=your-gemini-api-key
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
SENTRY_DSN=https://your-sentry-dsn
NEXT_PUBLIC_API_URL=https://staging-api.recoloca.ai/v1
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
```

---

## 📈 Performance Optimization

### Build Optimization

```yaml
# Build cache optimization
- name: Setup build cache
  uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      ~/.cache/pip
      /tmp/.buildx-cache
    key: ${{ runner.os }}-build-${{ hashFiles('**/package-lock.json', '**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-build-

# Parallel job execution
strategy:
  matrix:
    service: [backend, frontend]
  max-parallel: 2
```

### Resource Limits

```yaml
# Resource optimization for runners
runs-on: ubuntu-latest
container:
  image: ubuntu:22.04
  options: --cpus 2 --memory 4g
```

---

## 🔗 Related Documents

- [[Docker_Configuration.md]] - Container Configuration
- [[Infrastructure_as_Code.md]] - Terraform Setup
- [[Monitoring_and_Alerting.md]] - Observability
- [[Security_Guidelines.md]] - Security Best Practices
- [[Testing_Strategy.md]] - Testing Framework
- [[Deployment_Guide.md]] - Manual Deployment Procedures

---

**Document Status**: Active  
**Next Review Date**: 2025-03-20  
**Maintained By**: @DevOpsTeam