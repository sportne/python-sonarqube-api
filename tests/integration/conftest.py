import pytest
import subprocess
import time
import requests
import os


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

    yield base_url

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
