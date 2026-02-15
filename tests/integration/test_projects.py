def test_project_lifecycle(sonarqube_client):
    project_key = "test-project-integration"
    project_name = "Test Project Integration"

    # Ensure clean state
    try:
        sonarqube_client.projects.delete_project(project_key=project_key)
    except Exception:
        pass

    # Create
    response = sonarqube_client.projects.create_project(
        project_key=project_key, name=project_name
    )
    assert response.status_code in [200, 204], f"Creation failed: {response.text}"

    # Search
    projects_response = sonarqube_client.projects.search_projects(q=project_key)
    assert projects_response.status_code == 200
    projects = projects_response.json()
    found = any(p["key"] == project_key for p in projects["components"])
    assert found

    # Delete
    sonarqube_client.projects.delete_project(project_key=project_key)

    # Verify Deletion
    projects_response = sonarqube_client.projects.search_projects(q=project_key)
    projects = projects_response.json()
    found = any(p["key"] == project_key for p in projects["components"])
    assert not found
