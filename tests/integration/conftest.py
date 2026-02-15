import subprocess
import time

import pytest
import requests


@pytest.fixture(scope="session")
def sonarqube_server():
    # Start Sonarqube
    subprocess.run(["docker-compose", "up", "-d"], check=True)

    base_url = "http://localhost:9000"

    # Wait for Sonarqube to be ready
    max_retries = 60
    for _ in range(max_retries):
        try:
            response = requests.get(f"{base_url}/api/system/status", timeout=5)
            if response.status_code == 200:
                print(f"Sonarqube status: {response.json().get('status')}")
                status = response.json().get("status")
                if status == "UP":
                    break
        except requests.exceptions.ConnectionError:
            print("Sonarqube not reachable yet...")
        except requests.exceptions.ReadTimeout:
            print("Sonarqube timed out...")
        time.sleep(5)
    else:
        subprocess.run(["docker-compose", "down"], check=True)
        pytest.fail("Sonarqube failed to start")

    # Generate coverage report
    print("Generating coverage report...")
    subprocess.run(
        [".venv/bin/pytest", "--cov=src/sonarqube", "--cov-report=xml", "--ignore=tests/integration"],
        check=True
    )

    # Generate a token for analysis
    print("Generating analysis token...")
    from sonarqube import SonarQube
    temp_client = SonarQube(base_url, user="admin", password="admin")
    token_name = f"integration-test-token-{int(time.time())}"
    token_response = temp_client.user_tokens.generate(name=token_name)
    if token_response.status_code != 200:
        pytest.fail(f"Failed to generate analysis token: {token_response.text}")
    auth_token = token_response.json()["token"]

    # Run analysis of the current project
    print("Running SonarQube analysis...")
    project_key = "python-sonarqube-api-test"
    subprocess.run(
        [
            "docker", "run", "--rm",
            "--net=host",
            "-v", f"{subprocess.check_output(['pwd']).decode().strip()}:/usr/src",
            "sonarsource/sonar-scanner-cli",
            "-Dsonar.projectKey=" + project_key,
            "-Dsonar.sources=src/sonarqube",
            "-Dsonar.python.coverage.reportPaths=coverage.xml",
            "-Dsonar.host.url=" + base_url,
            "-Dsonar.token=" + auth_token
        ],
        check=True
    )

    # Wait for background task to finish
    print("Waiting for SonarQube background tasks to complete...")
    max_retries = 30
    for _ in range(max_retries):
        ce_response = temp_client.ce.get_ce_component(component=project_key)
        if ce_response.status_code == 200:
            queue = ce_response.json().get("queue", [])
            if not queue:
                break
        time.sleep(2)
    else:
        print("Warning: SonarQube background tasks timed out.")

    yield base_url

    # Teardown analysis data if needed, or just the token
    try:
        temp_client.user_tokens.revoke(name=token_name)
    except Exception:
        pass

    # Teardown
    subprocess.run(["docker-compose", "down"], check=True)


@pytest.fixture
def api_auth():
    return ("admin", "admin")


@pytest.fixture
def sonarqube_client(sonarqube_server, api_auth):
    from sonarqube import SonarQube

    username, password = api_auth
    return SonarQube(sonarqube_server, user=username, password=password)
