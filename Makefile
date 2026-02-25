# Employee Cyber Risk Monitor - Development Makefile

.PHONY: help install run test clean docker-build docker-run lint format

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install Python dependencies
	pip install -r requirements.txt

run: ## Run the Flask application
	python app.py

test: ## Run the test suite
	python -m pytest tests.py -v

test-cov: ## Run tests with coverage
	python -m pytest tests.py --cov=. --cov-report=html

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -f cyber_monitor.log

docker-build: ## Build Docker image
	docker build -t cyber-risk-monitor .

docker-run: ## Run with Docker
	docker run -p 5000:5000 cyber-risk-monitor

docker-compose-up: ## Start with Docker Compose
	docker-compose up -d

docker-compose-down: ## Stop Docker Compose
	docker-compose down

lint: ## Run code linting (requires flake8)
	flake8 app.py tests.py --max-line-length=100

format: ## Format code (requires black)
	black app.py tests.py

setup-dev: ## Setup development environment
	pip install -r requirements.txt
	pip install pytest flake8 black