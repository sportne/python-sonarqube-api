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
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   └── sonarqube
│       ├── __init__.py
│       ├── client.py
│       └── ...
├── tests
│   ├── __init__.py
│   ├── test_applications.py
│   └── ...
└── documentation
    ├── index.md
    └── ...
```

### Formatting

To format the code, run black:

```bash
black src tests
```

### Testing

To run the tests, use pytest:

```bash
pytest
```

## API Documentation

The SonarQube REST API documentation can be found here:
- https://next.sonarqube.com/sonarqube/web_api/api/
- https://next.sonarqube.com/sonarqube/web_api_v2

## Future Work

- Add more examples and use cases to the documentation.
