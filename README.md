# python-sonarqube-api

A Python wrapper for the Sonarqube Web API that allows you to easily interact with your SonarQube instance. This library will provide access to the full functionality of the SonarQube API, allowing you to automate tasks, extract data, and integrate SonarQube into your existing workflows.

## Features Checklist

This is a list of features that need to be implemented to consider this a complete SonarQube Python API client.

### Authentication
- [ ] Support for authentication using user tokens.
- [ ] Support for authentication using login/password (legacy).

### Projects
- [ ] Search for projects.
- [ ] Get project details.
- [ ] Create a new project.
- [ ] Delete a project.

### Issues
- [ ] Search for issues.
- [ ] Get issue details.
- [ ] Assign an issue.
- [ ] Add a comment to an issue.
- [ ] Transition an issue (e.g., confirm, resolve, reopen).

### Measures and Metrics
- [ ] Get measures for a component (project, file, etc.).
- [ ] Get the history of a measure.
- [ ] Get the list of available metrics.

### Users
- [ ] Search for users.
- [ ] Get user details.
- [ ] Create a new user.
- [ ] Deactivate a user.

### Quality Gates
- [ ] Get the quality gate status of a project.
- [ ] Get the list of quality gates.

### Rules
- [ ] Search for rules.
- [ ] Get rule details.

### System
- [ ] Get system health.
- [ ] Get system metrics.
