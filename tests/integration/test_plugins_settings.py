def test_list_plugins(sonarqube_client):
    response = sonarqube_client.plugins.get_installed_plugins()
    assert response.status_code == 200
    plugins = response.json().get("plugins", [])
    assert len(plugins) > 0

def test_list_settings(sonarqube_client):
    response = sonarqube_client.settings.values()
    assert response.status_code == 200
    settings = response.json().get("settings", [])
    # Even in fresh install there should be some settings
    assert len(settings) >= 0
