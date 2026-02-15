def test_user_token_lifecycle(sonarqube_client):
    token_name = "test-token-integration"

    # Create
    response = sonarqube_client.user_tokens.generate(name=token_name)
    assert response.status_code == 200
    token_data = response.json()
    assert token_data["name"] == token_name
    assert "token" in token_data

    # List
    response = sonarqube_client.user_tokens.search()
    assert response.status_code == 200
    tokens = response.json().get("userTokens", [])
    assert any(t["name"] == token_name for t in tokens)

    # Revoke
    response = sonarqube_client.user_tokens.revoke(name=token_name)
    assert response.status_code == 204

    # Verify Revocation
    response = sonarqube_client.user_tokens.search()
    tokens = response.json().get("userTokens", [])
    assert not any(t["name"] == token_name for t in tokens)
