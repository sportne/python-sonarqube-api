import pytest


@pytest.fixture
def project_with_data(sonarqube_client):
    project_key = "test-project-data"
    project_name = "Test Project Data"

    # Create project
    try:
        sonarqube_client.projects.create_project(
            project_key=project_key, name=project_name
        )
    except Exception:
        pass

    yield project_key

    # Cleanup
    try:
        sonarqube_client.projects.delete_project(project_key=project_key)
    except Exception:
        pass


def test_show_component(sonarqube_client, project_with_data):
    response = sonarqube_client.components.show_component(component=project_with_data)
    assert response.status_code == 200
    assert response.json()["component"]["key"] == project_with_data


def test_component_measures(sonarqube_client, project_with_data):
    # Use the analyzed project instead of a fresh one for coverage data
    project_key = "python-sonarqube-api-test"

    # Get ncloc, complexity and coverage metrics
    response = sonarqube_client.measures.get_measures_component(
        component=project_key,
        metricKeys="ncloc,complexity,coverage,lines_to_cover,uncovered_lines",
    )
    assert response.status_code == 200
    component = response.json().get("component")
    assert component is not None
    assert component["key"] == project_key

    measures = {m["metric"]: m["value"] for m in component.get("measures", [])}
    assert "ncloc" in measures
    assert "coverage" in measures
    print(f"Coverage for {project_key}: {measures['coverage']}%")


def test_notifications_list(sonarqube_client):
    response = sonarqube_client.notifications.list_notifications()
    assert response.status_code == 200
    # Might be empty but the call should succeed
    assert "notifications" in response.json()
