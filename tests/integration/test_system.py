def test_system_status(sonarqube_client):
    response = sonarqube_client.system.get_system_status()
    assert response.status_code == 200
    status = response.json()
    assert status["status"] == "UP"


# Not testing system info as it might require permission or not interesting for basic checks
