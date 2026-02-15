# python-sonarqube-api

⚠️ **Warning:** This is an experimental project for exploring how far a LLM driven coding agent can go toward implementing a Python library for a documened REST API.

A Python wrapper for the Sonarqube Web API that allows you to easily interact with your SonarQube instance.

This library provides access to almost the full functionality of the SonarQube API, allowing you to automate tasks, extract data, and integrate SonarQube into your existing workflows.

## Features

A comprehensive checklist of all implemented features can be found in [FEATURES.md](FEATURES.md).

## Development

### Project Structure
```
.
├── .github
│   └── workflows
│       ├── ci.yaml
│       └── release.yaml
├── .gitignore
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
├── src
│   ├── __init__.py
│   └── sonarqube
│       ├── __init__.py
│       ├── client.py
│       └── ...
├── tests
│   ├── __init__.py
│   ├── ...
│   └── integration
│       ├── ...
└── documentation
    ├── index.md
    └── ...
```

### Dev Workflow

The project uses a `Makefile` to simplify common development tasks.

#### Setup

To create a virtual environment and install development dependencies:

```bash
make setup-venv
make install-dev
```

#### Formatting

To auto-format the code with `black` and `isort`:

```bash
make format
```

#### Linting

To run `ruff` and `mypy` (static analysis):

```bash
make lint
make typecheck
```

#### Testing

To run the full unit test suite:

```bash
make test
```

To run tests with coverage reporting (minimum 80% threshold):

```bash
make coverage
```

To run integration tests (requires Docker and a running SonarQube instance):

```bash
make test-integration
```

> **Note:** The integration test suite automatically handles SonarQube setup, project analysis, and code coverage reporting using Docker.

## API Documentation

The SonarQube REST API documentation can be found here:
- https://next.sonarqube.com/sonarqube/web_api/api/
- https://next.sonarqube.com/sonarqube/web_api_v2

## Future Work

- Add more examples and use cases to the documentation.
