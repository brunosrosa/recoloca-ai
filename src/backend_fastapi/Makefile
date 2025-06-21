# Recoloca.AI FastAPI Backend - Makefile
# Automation for development, testing, and deployment tasks

.PHONY: help install dev test lint format clean docker run logs stop
.DEFAULT_GOAL := help

# =============================================================================
# VARIABLES
# =============================================================================
PYTHON := python
PIP := pip
PYTEST := pytest
BLACK := black
ISORT := isort
FLAKE8 := flake8
MYPY := mypy
DOCKER := docker
DOCKER_COMPOSE := docker-compose

APP_NAME := recoloca-api
IMAGE_NAME := $(APP_NAME):latest
CONTAINER_NAME := $(APP_NAME)-container

# Source directories
SRC_DIR := app
TEST_DIR := tests

# =============================================================================
# HELP
# =============================================================================
help: ## Show this help message
	@echo "Recoloca.AI FastAPI Backend - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Examples:"
	@echo "  make install     # Install dependencies"
	@echo "  make dev         # Start development server"
	@echo "  make test        # Run all tests"
	@echo "  make docker-up   # Start with Docker Compose"

# =============================================================================
# DEVELOPMENT SETUP
# =============================================================================
install: ## Install production dependencies
	$(PIP) install -r requirements.txt

install-dev: ## Install development dependencies
	$(PIP) install -r requirements.txt
	$(PIP) install pytest pytest-cov pytest-asyncio black isort flake8 mypy

setup: ## Setup development environment
	@echo "Setting up Recoloca.AI FastAPI Backend..."
	@if [ ! -f .env ]; then cp .env.example .env; echo "Created .env file from template"; fi
	@$(MAKE) install-dev
	@echo "Setup complete! Edit .env file with your configuration."

venv: ## Create virtual environment
	$(PYTHON) -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  Windows: venv\\Scripts\\activate"
	@echo "  Linux/Mac: source venv/bin/activate"

# =============================================================================
# DEVELOPMENT
# =============================================================================
dev: ## Start development server with auto-reload
	$(PYTHON) main.py

run: ## Start production server
	uvicorn main:app --host 0.0.0.0 --port 8000

run-prod: ## Start production server with Gunicorn
	gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

shell: ## Start Python shell with app context
	$(PYTHON) -c "from app.core.config import settings; print(f'Environment: {settings.ENVIRONMENT}'); import IPython; IPython.start_ipython()"

# =============================================================================
# CODE QUALITY
# =============================================================================
format: ## Format code with black and isort
	$(BLACK) $(SRC_DIR) $(TEST_DIR) main.py
	$(ISORT) $(SRC_DIR) $(TEST_DIR) main.py
	@echo "Code formatted successfully!"

lint: ## Run linting with flake8
	$(FLAKE8) $(SRC_DIR) $(TEST_DIR) main.py
	@echo "Linting completed!"

type-check: ## Run type checking with mypy
	$(MYPY) $(SRC_DIR) main.py
	@echo "Type checking completed!"

check: ## Run all code quality checks
	@echo "Running code quality checks..."
	@$(MAKE) format
	@$(MAKE) lint
	@$(MAKE) type-check
	@echo "All checks passed!"

# =============================================================================
# TESTING
# =============================================================================
test: ## Run all tests
	$(PYTEST)

test-unit: ## Run unit tests only
	$(PYTEST) -m "unit"

test-integration: ## Run integration tests only
	$(PYTEST) -m "integration"

test-e2e: ## Run end-to-end tests only
	$(PYTEST) -m "e2e"

test-cov: ## Run tests with coverage report
	$(PYTEST) --cov=$(SRC_DIR) --cov-report=html --cov-report=term

test-watch: ## Run tests in watch mode
	$(PYTEST) -f

test-fast: ## Run fast tests only (exclude slow markers)
	$(PYTEST) -m "not slow"

test-smoke: ## Run smoke tests
	$(PYTEST) -m "smoke"

# =============================================================================
# DOCKER
# =============================================================================
docker-build: ## Build Docker image
	$(DOCKER) build -t $(IMAGE_NAME) .

docker-run: ## Run Docker container
	$(DOCKER) run -d --name $(CONTAINER_NAME) -p 8000:8000 --env-file .env $(IMAGE_NAME)

docker-stop: ## Stop Docker container
	$(DOCKER) stop $(CONTAINER_NAME) || true
	$(DOCKER) rm $(CONTAINER_NAME) || true

docker-logs: ## Show Docker container logs
	$(DOCKER) logs -f $(CONTAINER_NAME)

docker-shell: ## Access Docker container shell
	$(DOCKER) exec -it $(CONTAINER_NAME) bash

# =============================================================================
# DOCKER COMPOSE
# =============================================================================
docker-up: ## Start all services with Docker Compose
	$(DOCKER_COMPOSE) up -d

docker-up-build: ## Build and start all services
	$(DOCKER_COMPOSE) up -d --build

docker-down: ## Stop all services
	$(DOCKER_COMPOSE) down

docker-down-volumes: ## Stop all services and remove volumes
	$(DOCKER_COMPOSE) down -v

docker-logs-api: ## Show API service logs
	$(DOCKER_COMPOSE) logs -f api

docker-logs-redis: ## Show Redis service logs
	$(DOCKER_COMPOSE) logs -f redis

docker-restart: ## Restart all services
	$(DOCKER_COMPOSE) restart

docker-ps: ## Show running containers
	$(DOCKER_COMPOSE) ps

# =============================================================================
# DATABASE
# =============================================================================
db-migrate: ## Run database migrations (placeholder)
	@echo "Database migrations not implemented yet"

db-seed: ## Seed database with test data (placeholder)
	@echo "Database seeding not implemented yet"

db-reset: ## Reset database (placeholder)
	@echo "Database reset not implemented yet"

# =============================================================================
# UTILITIES
# =============================================================================
clean: ## Clean up temporary files
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type f -name "coverage.xml" -delete 2>/dev/null || true
	@echo "Cleanup completed!"

clean-docker: ## Clean up Docker resources
	$(DOCKER) system prune -f
	$(DOCKER) volume prune -f

requirements: ## Generate requirements.txt from current environment
	$(PIP) freeze > requirements.txt
	@echo "Requirements updated!"

env-check: ## Check environment variables
	@echo "Checking environment configuration..."
	@$(PYTHON) -c "from app.core.config import settings; print(f'App: {settings.APP_NAME}'); print(f'Environment: {settings.ENVIRONMENT}'); print(f'Debug: {settings.DEBUG}'); print(f'RAG Enabled: {settings.RAG_ENABLED}')"

health: ## Check application health
	@echo "Checking application health..."
	@curl -f http://localhost:8000/health || echo "Application not running or unhealthy"

logs: ## Show application logs
	tail -f logs/recoloca_api.log 2>/dev/null || echo "Log file not found"

# =============================================================================
# DEPLOYMENT
# =============================================================================
deploy-staging: ## Deploy to staging (placeholder)
	@echo "Staging deployment not implemented yet"

deploy-prod: ## Deploy to production (placeholder)
	@echo "Production deployment not implemented yet"

backup: ## Backup data (placeholder)
	@echo "Backup not implemented yet"

# =============================================================================
# MONITORING
# =============================================================================
stats: ## Show application statistics
	@echo "Application Statistics:"
	@echo "Lines of code:"
	@find $(SRC_DIR) -name "*.py" | xargs wc -l | tail -1
	@echo "Test files:"
	@find $(TEST_DIR) -name "*.py" 2>/dev/null | wc -l || echo "0"
	@echo "Docker images:"
	@$(DOCKER) images | grep $(APP_NAME) || echo "No images found"

perf: ## Run performance tests (placeholder)
	@echo "Performance tests not implemented yet"

security: ## Run security checks (placeholder)
	@echo "Security checks not implemented yet"

# =============================================================================
# DOCUMENTATION
# =============================================================================
docs: ## Generate API documentation
	@echo "API documentation available at: http://localhost:8000/docs"
	@echo "Alternative documentation: http://localhost:8000/redoc"

docs-export: ## Export OpenAPI specification
	@echo "Exporting OpenAPI specification..."
	@curl -s http://localhost:8000/openapi.json > openapi.json
	@echo "OpenAPI spec exported to openapi.json"

# =============================================================================
# MAINTENANCE
# =============================================================================
update: ## Update dependencies
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade -r requirements.txt
	@echo "Dependencies updated!"

check-deps: ## Check for outdated dependencies
	$(PIP) list --outdated

info: ## Show project information
	@echo "Recoloca.AI FastAPI Backend"
	@echo "==========================="
	@echo "Python version: $$(python --version)"
	@echo "FastAPI version: $$(pip show fastapi | grep Version | cut -d' ' -f2)"
	@echo "Current directory: $$(pwd)"
	@echo "Environment: $$(python -c 'from app.core.config import settings; print(settings.ENVIRONMENT)' 2>/dev/null || echo 'Not configured')"
	@echo "Git branch: $$(git branch --show-current 2>/dev/null || echo 'Not a git repository')"