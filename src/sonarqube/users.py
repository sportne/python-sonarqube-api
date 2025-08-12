class SonarQubeUsers:
    def __init__(self, client):
        self.client = client

    def search_users(self, **kwargs):
        """
        Search for users.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/users/search", params=kwargs)

    def create_user(self, login, name, **kwargs):
        """
        Create a new user.
        :param login: User login
        :param name: User name
        :param kwargs: Additional parameters
        """
        params = {"login": login, "name": name}
        params.update(kwargs)
        return self.client._post("api/users/create", params=params)

    def deactivate_user(self, login):
        """
        Deactivate a user.
        :param login: User login
        """
        params = {"login": login}
        return self.client._post("api/users/deactivate", params=params)

    def update_user(self, login, **kwargs):
        """
        Update user properties.
        :param login: User login
        :param kwargs: Additional parameters
        """
        params = {"login": login}
        params.update(kwargs)
        return self.client._post("api/users/update", params=params)

    def change_user_password(self, login, new_password, previous_password=None):
        """
        Change user password.
        :param login: User login
        :param new_password: New password
        :param previous_password: Previous password
        """
        params = {"login": login, "password": new_password}
        if previous_password:
            params["previousPassword"] = previous_password
        return self.client._post("api/users/change_password", params=params)

    def get_user_groups(self, login, **kwargs):
        """
        Get user groups.
        :param login: User login
        :param kwargs: Additional parameters
        """
        params = {"login": login}
        params.update(kwargs)
        return self.client._get("api/users/groups", params=params)

    def search_user_tokens(self, login):
        """
        Get user tokens.
        :param login: User login
        """
        params = {"login": login}
        return self.client._get("api/user_tokens/search", params=params)

    def generate_user_token(self, login, name=None):
        """
        Generate a user token.
        :param login: User login
        :param name: Token name
        """
        params = {"login": login}
        if name:
            params["name"] = name
        return self.client._post("api/user_tokens/generate", params=params)

    def revoke_user_token(self, login, name):
        """
        Revoke a user token.
        :param login: User login
        :param name: Token name
        """
        params = {"login": login, "name": name}
        return self.client._post("api/user_tokens/revoke", params=params)
