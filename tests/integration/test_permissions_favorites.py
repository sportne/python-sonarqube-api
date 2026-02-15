def test_permissions_templates_search(sonarqube_client):
    response = sonarqube_client.permissions.search_permission_templates()
    assert response.status_code == 200
    permissions = response.json().get("permissions", [])
    assert len(permissions) > 0


def test_favorites_lifecycle(sonarqube_client):
    project_key = "test-project-favorites"
    project_name = "Test Project Favorites"

    # Ensure project exists
    try:
        sonarqube_client.projects.create_project(
            project_key=project_key, name=project_name
        )
    except Exception:
        pass

    # Add to favorites
    response = sonarqube_client.favorites.add_favorite(component=project_key)
    assert response.status_code in [200, 204]

    # Search favorites
    response = sonarqube_client.favorites.search_favorites()
    assert response.status_code == 200
    favorites = response.json().get("favorites", [])
    assert any(f["key"] == project_key for f in favorites)

    # Remove from favorites
    response = sonarqube_client.favorites.remove_favorite(component=project_key)
    assert response.status_code in [200, 204]

    # Cleanup project
    sonarqube_client.projects.delete_project(project_key=project_key)
