import unittest
from unittest.mock import patch, MagicMock
from src.sonarqube import SonarQube


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

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.search_projects(q="my-project")

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/search",
            params={"q": "my-project"},
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

        client = SonarQube(host="http://localhost:9000", token="my_token")
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

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.delete_project(project_key="my-project")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/delete",
            params={"project": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_bulk_delete_projects(self, mock_session_cls):
        """
        Test bulk deleting projects.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.bulk_delete_projects(projects="my-project-1,my-project-2")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/bulk_delete",
            params={"projects": "my-project-1,my-project-2"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_export_project_findings(self, mock_session_cls):
        """
        Test exporting project findings.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.export_project_findings(project="my-project")

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/export_findings",
            params={"project": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_project_contains_ai_code(self, mock_session_cls):
        """
        Test getting project contains AI code.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.get_project_contains_ai_code(project="my-project")

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/get_contains_ai_code",
            params={"project": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_project_detected_ai_code(self, mock_session_cls):
        """
        Test getting project detected AI code.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.get_project_detected_ai_code(project="my-project")

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/get_detected_ai_code",
            params={"project": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_project_license_usage(self, mock_session_cls):
        """
        Test getting project license usage.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.get_project_license_usage()

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/license_usage"
        )

    @patch("src.sonarqube.requests.Session")
    def test_search_my_projects(self, mock_session_cls):
        """
        Test searching my projects.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.search_my_projects()

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/search_my_projects",
            params={},
        )

    @patch("src.sonarqube.requests.Session")
    def test_search_my_scannable_projects(self, mock_session_cls):
        """
        Test searching my scannable projects.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.search_my_scannable_projects()

        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/projects/search_my_scannable_projects",
            params={},
        )

    @patch("src.sonarqube.requests.Session")
    def test_set_project_contains_ai_code(self, mock_session_cls):
        """
        Test setting project contains AI code.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.set_project_contains_ai_code(project="my-project", contains_ai_code=True)

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/set_contains_ai_code",
            params={"project": "my-project", "contains_ai_code": True},
        )

    @patch("src.sonarqube.requests.Session")
    def test_update_project_default_visibility(self, mock_session_cls):
        """
        Test updating project default visibility.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.update_project_default_visibility(visibility="public")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/update_default_visibility",
            params={"visibility": "public"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_update_project_key(self, mock_session_cls):
        """
        Test updating project key.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.update_project_key(project="my-project", new_key="new-project-key")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/update_key",
            params={"from": "my-project", "to": "new-project-key"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_update_project_visibility(self, mock_session_cls):
        """
        Test updating project visibility.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        client.update_project_visibility(project="my-project", visibility="public")

        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/projects/update_visibility",
            params={"project": "my-project", "visibility": "public"},
        )
