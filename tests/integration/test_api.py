import requests

from sonarqube import SonarQube


def test_sonarqube_health(sonarqube_server, api_auth):
    username, password = api_auth
    response = requests.get(
        f"{sonarqube_server}/api/system/health", auth=(username, password)
    )
    assert response.status_code == 200
    assert response.json()["health"] in ["GREEN", "YELLOW", "RED"]


def test_authentication_with_client(sonarqube_server, api_auth):
    username, password = api_auth

    # Initialize the client
    client = SonarQube(sonarqube_server, user=username, password=password)

    # Verify authentication using a simple call, e.g. validating the user
    # Ideally checking something that requires auth
    # The client has an authentication module, let's use it
    assert client.authentication.validate().status_code == 200
