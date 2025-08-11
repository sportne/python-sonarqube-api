import unittest
from unittest.mock import patch, MagicMock
from src.sonarqube import SonarQubeAPI


class TestProjects(unittest.TestCase):
    @patch("src.sonarqube.requests.Session")
    def test_search_projects(self, mock_session_cls):
        """
        Test searching for projects.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"paging": {}, "components": []}
        mock_session.get.return_value = mock_response

        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.search_projects(q="my-project")

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/search",
            params={"q": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_project_details(self, mock_session_cls):
        """
        Test getting project details.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"project": {}}
        mock_session.get.return_value = mock_response

        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.get_project_details(project_key="my-project")

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/show",
            params={"project": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_create_project(self, mock_session_cls):
        """
        Test creating a new project.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.post.return_value = mock_response

        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.create_project(project_key="my-project", name="My Project")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/create",
            params={"project": "my-project", "name": "My Project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_delete_project(self, mock_session_cls):
        """
        Test deleting a project.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response

        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.delete_project(project_key="my-project")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/delete",
            params={"project": "my-project"},
        )
