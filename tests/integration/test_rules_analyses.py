def test_rules_search(sonarqube_client):
    response = sonarqube_client.rules.search_rules(languages="py")
    assert response.status_code == 200
    assert "rules" in response.json()


def test_project_analyses_search(sonarqube_client):
    # This might return empty as we haven't run an analysis, but the API should work
    project_key = "test-project-analyses"
    try:
        sonarqube_client.projects.create_project(
            project_key=project_key, name="Test Project Analyses"
        )
        response = sonarqube_client.project_analyses.search_project_analyses(
            project=project_key
        )
        assert response.status_code == 200
        assert "analyses" in response.json()
    finally:
        try:
            sonarqube_client.projects.delete_project(project_key=project_key)
        except Exception:
            pass
