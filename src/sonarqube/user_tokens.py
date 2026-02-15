class SonarQubeUserTokens:
    def __init__(self, client):
        self.client = client

    def generate(
        self, name, login=None, expirationDate=None, projectKey=None, type=None
    ):
        """
        Generate a user access token.
        :param name: Token name
        :param login: User login. If not set, the token is generated for the authenticated user.
        :param expirationDate: The expiration date of the token (YYYY-MM-DD)
        :param projectKey: The key of the only project that can be analyzed by the PROJECT_ANALYSIS_TOKEN
        :param type: Token Type. Possible values: USER_TOKEN, GLOBAL_ANALYSIS_TOKEN, PROJECT_ANALYSIS_TOKEN
        """
        params = {"name": name}
        if login:
            params["login"] = login
        if expirationDate:
            params["expirationDate"] = expirationDate
        if projectKey:
            params["projectKey"] = projectKey
        if type:
            params["type"] = type
        return self.client._post("api/user_tokens/generate", params=params)

    def revoke(self, name, login=None):
        """
        Revoke a user access token.
        :param name: Token name
        :param login: User login. If not set, the token for the current user is revoked.
        """
        params = {"name": name}
        if login:
            params["login"] = login
        return self.client._post("api/user_tokens/revoke", params=params)

    def search(self, login=None):
        """
        List the access tokens of a user.
        :param login: User login. If not set, tokens for the current user are listed.
        """
        params = {}
        if login:
            params["login"] = login
        return self.client._get("api/user_tokens/search", params=params)
