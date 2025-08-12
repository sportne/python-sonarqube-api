import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeProjectPullRequests(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_delete_project_pull_request(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_pull_requests.delete_project_pull_request(
                project="my-project", pullRequest="my-pr"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_pull_requests/delete",
                params={"project": "my-project", "pullRequest": "my-pr"},
            )

    def test_list_project_pull_requests(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_pull_requests.list_project_pull_requests(
                project="my-project"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_pull_requests/list",
                params={"project": "my-project"},
            )
