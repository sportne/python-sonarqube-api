def test_get_sources_raw(sonarqube_client):
    # Use a file we know exists in the analyzed project
    file_key = "python-sonarqube-api-test:src/sonarqube/client.py"
    
    response = sonarqube_client.sources.get_sources_raw(key=file_key)
    assert response.status_code == 200
    assert "class SonarQube" in response.text

def test_get_sources_lines(sonarqube_client):
    file_key = "python-sonarqube-api-test:src/sonarqube/client.py"
    
    response = sonarqube_client.sources.get_sources_lines(key=file_key, from_line=1, to_line=10)
    assert response.status_code == 200
    data = response.json()
    assert "sources" in data
    assert len(data["sources"]) > 0

def test_get_sources_show(sonarqube_client):
    file_key = "python-sonarqube-api-test:src/sonarqube/client.py"
    
    response = sonarqube_client.sources.get_sources_show(key=file_key, from_line=1, to_line=10)
    assert response.status_code == 200
    # The output of api/sources/show is an HTML-like structure or similar
    assert "sources" in response.json()
