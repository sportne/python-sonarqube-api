import requests


class SonarQubeAPI:
    def __init__(self, host=None, token=None, user=None, password=None):
        """
        Create a SonarQube API client.
        :param host: SonarQube host, eg. http://localhost:9000
        :param token: SonarQube user token
        :param user: SonarQube user
        :param password: SonarQube password
        """
        self.host = host
        self.token = token
        self.user = user
        self.password = password

        # Configure authentication
        self.session = requests.Session()
        if self.token:
            self.session.auth = (self.token, "")
        elif self.user and self.password:
            self.session.auth = (self.user, self.password)

    def _get(self, endpoint, **kwargs):
        """
        Send a GET request to the SonarQube API.
        """
        return self.session.get(f"{self.host}/{endpoint}", **kwargs)

    def _post(self, endpoint, **kwargs):
        """
        Send a POST request to the SonarQube API.
        """
        return self.session.post(f"{self.host}/{endpoint}", **kwargs)

    def is_authenticated(self):
        """
        Check if the client is authenticated.
        """
        response = self._get("api/authentication/validate")
        return response.status_code == 200 and response.json().get("valid") is True
