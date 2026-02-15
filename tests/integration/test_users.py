def test_user_lifecycle(sonarqube_client):
    login = "testuser_integration"
    name = "Test User Integration"
    password = "password123"

    # Create
    try:
        # V2 API: create_user(login, name, password=..., etc.)
        sonarqube_client.users_v2.create_user(login=login, name=name, password=password)
    except Exception:
        # If exists, we might proceed or try to cleanup
        pass

    # Search
    # V2 API: search_users(**kwargs) -> returns list/page of users
    users_response = sonarqube_client.users_v2.search_users(q=login)
    assert users_response.status_code == 200
    users_data = users_response.json()
    # Check structure of response for V2. Assuming standard paging or list.
    # It might be users_data['users'] or similar.
    found = any(u.get("login") == login for u in users_data.get("users", []))
    assert found

    # Deactivate - V2 API needs user_id, not login!
    # We need to find the user ID first.
    user_id = next(
        (u.get("id") for u in users_data.get("users", []) if u.get("login") == login),
        None,
    )
    assert user_id is not None

    sonarqube_client.users_v2.deactivate_user(user_id=user_id)

    # Verify Deactivation
    users_response = sonarqube_client.users_v2.search_users(q=login)
    users_data = users_response.json()
    user = next(
        (u for u in users_data.get("users", []) if u.get("login") == login), None
    )

    if user:
        assert not user.get("active", True)
