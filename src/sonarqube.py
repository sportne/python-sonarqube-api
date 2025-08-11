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

    def search_projects(self, q):
        """
        Search for projects.
        :param q: The query to search for.
        """
        params = {"q": q}
        return self._get("api/projects/search", params=params)

    def get_project_details(self, project_key):
        """
        Get project details.
        :param project_key: The key of the project to get details for.
        """
        params = {"project": project_key}
        return self._get("api/projects/show", params=params)

    def create_project(self, project_key, name):
        """
        Create a new project.
        :param project_key: The key of the new project.
        :param name: The name of the new project.
        """
        params = {"project": project_key, "name": name}
        return self._post("api/projects/create", params=params)

    def delete_project(self, project_key):
        """
        Delete a project.
        :param project_key: The key of the project to delete.
        """
        params = {"project": project_key}
        return self._post("api/projects/delete", params=params)
