# Repository Guide for `python-sonarqube-api`

## Overview
- This package provides a thin, well-documented wrapper around the SonarQube Web API.
- Source code lives under `src/sonarqube/`; tests under `tests/`; end-user docs are in `documentation/` and should be kept in sync with the Python surface area.
- For official endpoint details and payload descriptions, refer to the SonarQube Web API reference at <https://next.sonarqube.com/sonarqube/web_api/api/> (linked from the repository `README.md`).

## Coding Principles
- Each SonarQube resource has its own class (e.g., `SonarQubeIssues`) that accepts the shared client in its constructor and invokes the client's `_get`/`_post` helpers. Follow this pattern for any new resource modules or methods.
- Method names should mirror the SonarQube endpoint intent (e.g., `add_project_to_application` for `api/applications/add_project`).
- Build the request payload in a local `params` dictionary. Only include optional keys when their value is not `None` (or an empty string) so requests remain minimal and tests can assert exact argument dictionaries.
- Write descriptive docstrings that summarize the endpoint and document parameters using the `:param` style already used across the codebase.
- Tests use `unittest.mock.patch` to assert the exact HTTP verb and argument payload. Any new helper should have an accompanying test asserting the request made by the client.

## Style & Tooling
- The codebase is formatted with **Black** and **isort**. Use `make format` to auto-format.
- Linting is performed by **ruff** and static typing by **mypy**. Run `make lint` and `make typecheck` respectively.
- Configuration is consolidated in `pyproject.toml`. Avoid creating separate config files (like `pytest.ini` or `.ruff.toml`) unless absolutely necessary.

## Documentation Expectations
- When adding or significantly changing a resource API, update the matching Markdown file in `documentation/` and ensure the feature checklist in `FEATURES.md` is updated.
- Keep examples in `examples/` aligned with the public interface exposed via `src/sonarqube/__init__.py`.
- Cross-check new or modified methods against the upstream SonarQube Web API reference before documenting or releasing them to ensure parameter names and semantics match the official spec.

## Testing & Verification
1. Install development dependencies: `make setup-venv` and `make install-dev`.
2. Run the unit test suite: `make test`.
3. Run with coverage verification: `make coverage` (strives for 80%+ branch coverage).
4. Run integration tests: `make test-integration`. This suite uses Docker to spin up SonarQube, perform project analysis, and verify API interactions against a live instance with real data and coverage.
5. If tests touch HTTP behavior that is difficult to mock, follow the existing pattern of patching the `requests.Session` methods attached to `SonarQube` instances or add an integration test to `tests/integration/`.

Adhering to the above keeps the client consistent, well-tested, and ready for publication.
