class SonarQubeAuthentication:
    def __init__(self, client):
        self.client = client

    def login(self, login, password):
        """
        Authenticate a user.
        :param login: Login of the user.
        :param password: Password of the user.
        """
        params = {"login": login, "password": password}
        return self.client._post("api/authentication/login", params=params)

    def logout(self):
        """
        Logout a user.
        """
        return self.client._post("api/authentication/logout")

    def validate(self):
        """
        Check credentials.
        """
        return self.client._get("api/authentication/validate")

    def is_authenticated(self):
        """
        Check if the client is authenticated.
        """
        response = self.validate()
        return response.status_code == 200 and response.json().get("valid") is True
