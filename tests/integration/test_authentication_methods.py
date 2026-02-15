from sonarqube import SonarQube

def test_auth_with_credentials(sonarqube_server, api_auth):
    username, password = api_auth
    client = SonarQube(sonarqube_server, user=username, password=password)
    
    # Verify we can perform an action
    response = client.authentication.validate()
    assert response.status_code == 200
    assert response.json()["valid"] is True

def test_auth_with_token(sonarqube_server, sonarqube_client):
    # First, generate a token using the default client (which uses credentials)
    token_name = "test-auth-token"
    
    # Cleanup if exists
    try:
        sonarqube_client.user_tokens.revoke(name=token_name)
    except:
        pass
        
    response = sonarqube_client.user_tokens.generate(name=token_name)
    assert response.status_code == 200
    token = response.json()["token"]
    
    try:
        # Initialize a NEW client using the token
        token_client = SonarQube(sonarqube_server, token=token)
        
        # Verify we can perform an action
        response = token_client.authentication.validate()
        assert response.status_code == 200
        assert response.json()["valid"] is True
        
        # Another action to be sure
        response = token_client.projects.search_projects(q="python")
        assert response.status_code == 200
        
    finally:
        # Cleanup token
        sonarqube_client.user_tokens.revoke(name=token_name)
