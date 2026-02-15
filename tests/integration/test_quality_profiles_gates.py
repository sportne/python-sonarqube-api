def test_quality_profiles_search(sonarqube_client):
    # Search for quality profiles (default ones should exist)
    response = sonarqube_client.quality_profiles.search_quality_profiles()
    assert response.status_code == 200
    profiles = response.json()
    assert len(profiles["profiles"]) > 0


def test_quality_gates_list(sonarqube_client):
    # List quality gates (default one should exist)
    response = sonarqube_client.quality_gates.list_quality_gates()
    assert response.status_code == 200
    gates = response.json()
    assert len(gates["qualitygates"]) > 0

    # Check for "Sonar way"
    sonar_way = next(
        (g for g in gates["qualitygates"] if g["name"] == "Sonar way"), None
    )
    assert sonar_way is not None
