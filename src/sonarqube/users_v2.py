class SonarQubeUsersV2:
    def __init__(self, client):
        self.client = client

    def create_user(self, login, name, **kwargs):
        """
        Create a user.
        :param login: User login
        :param name: User name
        :param kwargs: Additional parameters
        """
        params = {"login": login, "name": name}
        params.update(kwargs)
        return self.client._post("/api/v2/users-management/users", json=params)

    def search_users(self, **kwargs):
        """
        Get a list of users.
        :param kwargs: Additional parameters
        """
        return self.client._get("/api/v2/users-management/users", params=kwargs)

    def get_user(self, user_id):
        """
        Fetch a single user.
        :param user_id: The id of the user to fetch.
        """
        return self.client._get(f"/api/v2/users-management/users/{user_id}")

    def update_user(self, user_id, **kwargs):
        """
        Update users attributes.
        :param user_id: The id of the user to update.
        :param kwargs: Additional parameters
        """
        return self.client._patch(
            f"/api/v2/users-management/users/{user_id}", json=kwargs
        )

    def deactivate_user(self, user_id, anonymize=None):
        """
        Deactivates a user.
        :param user_id: The ID of the user to delete.
        :param anonymize: Anonymize user in addition to deactivating it.
        """
        params = {}
        if anonymize:
            params["anonymize"] = anonymize
        return self.client._delete(
            f"/api/v2/users-management/users/{user_id}", params=params
        )
