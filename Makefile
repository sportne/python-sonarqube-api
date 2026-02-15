# Makefile for python-sonarqube-api

# Define the virtual environment directory
VENV = .venv
# Define the paths to the binaries directly
PYTHON = $(VENV)/bin/python
PIP    = $(VENV)/bin/pip

# Target to ensure the venv is created and updated
setup-venv:
	python3 -m venv $(VENV)

SRC_DIR     := src
TEST_DIR    := tests
PACKAGE     := sonarqube

.PHONY: \
    help install-dev \
    format format-check \
    lint typecheck \
    test test-integration coverage \
    package clean \
    ci

help:
	@echo "python-sonarqube-api Makefile targets:"
	@echo "  make install-dev      - Install project with dev dependencies"
	@echo "  make format           - Run black and isort (auto-format)"
	@echo "  make format-check     - Check formatting (no changes made)"
	@echo "  make lint             - Run ruff linting"
	@echo "  make typecheck        - Run mypy static type checking"
	@echo "  make test             - Run unit tests (ignoring integration tests)"
	@echo "  make test-integration - Run integration tests"
	@echo "  make coverage         - Run unit tests with coverage threshold"
	@echo "  make package          - Build a source distribution and wheel"
	@echo "  make clean            - Remove build artifacts"
	@echo "  make ci               - Run all phase checks (convenience target)"

install-dev:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .[dev]

# ----- Formatting -----

format:
	$(PYTHON) -m black $(SRC_DIR) $(TEST_DIR)
	$(PYTHON) -m isort $(SRC_DIR) $(TEST_DIR)

format-check:
	$(PYTHON) -m black --check $(SRC_DIR) $(TEST_DIR)
	$(PYTHON) -m isort --check-only $(SRC_DIR) $(TEST_DIR)

# ----- Linting / Static Analysis -----

lint:
	$(PYTHON) -m ruff check $(SRC_DIR) $(TEST_DIR)

typecheck:
	$(PYTHON) -m mypy $(SRC_DIR)

# ----- Testing -----

test:
	$(PYTHON) -m pytest --ignore=tests/integration

test-integration:
	$(PYTHON) -m pytest tests/integration

coverage:
	$(PYTHON) -m pytest --ignore=tests/integration --cov=$(PACKAGE) --cov-report=term-missing --cov-fail-under=80

# ----- Packaging -----

package:
	@echo "Building source distribution and wheel..."
	$(PYTHON) -m pip install --upgrade build
	$(PYTHON) -m build

clean:
	@echo "Cleaning up build artifacts..."
	rm -rf build dist *.egg-info

# ----- Convenience Target -----

ci: format-check lint test coverage
