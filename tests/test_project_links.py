import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeProjectLinks(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_create_project_link(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_links.create_project_link(
                projectId="my-project-id", name="my-link", url="http://my-link.com"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_links/create",
                params={
                    "projectId": "my-project-id",
                    "name": "my-link",
                    "url": "http://my-link.com",
                },
            )

    def test_delete_project_link(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_links.delete_project_link(id="my-link-id")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_links/delete",
                params={"id": "my-link-id"},
            )

    def test_search_project_links(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_links.search_project_links(projectId="my-project-id")
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_links/search",
                params={"projectId": "my-project-id"},
            )
