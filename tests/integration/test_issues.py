def test_issues_search(sonarqube_client):
    # Search for issues - expectation is 200 OK, result might be empty on fresh instance
    response = sonarqube_client.issues.search_issues()
    assert response.status_code == 200
    issues = response.json()
    assert "issues" in issues
    assert "paging" in issues


def test_issues_authors(sonarqube_client):
    # Search for authors
    response = sonarqube_client.issues.get_authors()
    assert response.status_code == 200
    authors = response.json()
    assert "authors" in authors


def test_issues_tags(sonarqube_client):
    # Search for tags
    response = sonarqube_client.issues.get_tags()
    assert response.status_code == 200
    tags = response.json()
    assert "tags" in tags
