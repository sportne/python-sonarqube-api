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
- The codebase is formatted with **Black**. Run `black .` after making changes. (The test suite contains `tests/test_formatting.py`, which will fail if formatting is off or Black is missing.)
- Avoid wrapping imports in `try/except`; rely on explicit dependencies listed in `requirements.txt`.

## Documentation Expectations
- When adding or significantly changing a resource API, update the matching Markdown file in `documentation/` and, if relevant, the feature checklist in `README.md`.
- Keep examples in `examples/` aligned with the public interface exposed via `src/sonarqube/__init__.py`.
- Cross-check new or modified methods against the upstream SonarQube Web API reference before documenting or releasing them to ensure parameter names and semantics match the official spec.

## Testing & Verification
1. Install dependencies: `pip install -r requirements.txt` (ensures `requests`, `black`, and `pytest` are present).
2. Run the full test suite with `pytest` from the repository root.
3. If tests touch HTTP behavior that is difficult to mock, follow the existing pattern of patching the `requests.Session` methods attached to `SonarQube` instances.

Adhering to the above keeps the client consistent, well-tested, and ready for publication.
