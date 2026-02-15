def test_list_languages(sonarqube_client):
    response = sonarqube_client.languages.list_languages()
    assert response.status_code == 200
    languages = response.json().get("languages", [])
    assert len(languages) > 0
    # Check for a common language
    assert any(lang["key"] == "py" for lang in languages)
