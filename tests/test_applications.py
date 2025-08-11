import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeApplications(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_add_project_to_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.add_project_to_application(
                application="my-app", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/add_project",
                params={"application": "my-app", "project": "my-project"},
            )

    def test_create_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.create_application(
                name="my-app",
                key="my-app-key",
                visibility="public",
                description="My App",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/create",
                params={
                    "name": "my-app",
                    "key": "my-app-key",
                    "visibility": "public",
                    "description": "My App",
                },
            )

    def test_create_branch_in_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.create_branch_in_application(
                application="my-app",
                branch="feature/new-branch",
                project="my-project",
                projectBranch="main",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/create_branch",
                params={
                    "application": "my-app",
                    "branch": "feature/new-branch",
                    "project": "my-project",
                    "projectBranch": "main",
                },
            )

    def test_delete_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.delete_application(application="my-app")
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/delete",
                params={"application": "my-app"},
            )

    def test_delete_branch_in_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.delete_branch_in_application(
                application="my-app", branch="feature/new-branch"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/delete_branch",
                params={"application": "my-app", "branch": "feature/new-branch"},
            )

    def test_refresh_applications(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.refresh_applications(key="my-app")
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/refresh",
                params={"key": "my-app"},
            )

    def test_remove_project_from_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.remove_project_from_application(
                application="my-app", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/remove_project",
                params={"application": "my-app", "project": "my-project"},
            )

    def test_search_application_projects(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_application_projects(
                application="my-app", q="test", p=1, ps=10
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/applications/search_projects",
                params={"application": "my-app", "q": "test", "p": 1, "ps": 10},
            )

    def test_set_application_tags(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_application_tags(application="my-app", tags="tag1,tag2")
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/set_tags",
                params={"application": "my-app", "tags": "tag1,tag2"},
            )

    def test_show_application(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.show_application(application="my-app", branch="main")
            mock_get.assert_called_with(
                "http://localhost:9000/api/applications/show",
                params={"application": "my-app", "branch": "main"},
            )

    def test_show_application_leak(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.show_application_leak(application="my-app", pullRequest="123")
            mock_get.assert_called_with(
                "http://localhost:9000/api/applications/show_leak",
                params={"application": "my-app", "pullRequest": "123"},
            )

    def test_update_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.update_application(
                application="my-app", name="new-name", description="new-desc"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/update",
                params={
                    "application": "my-app",
                    "name": "new-name",
                    "description": "new-desc",
                },
            )

    def test_update_branch_in_application(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.update_branch_in_application(
                application="my-app", branch="main", name="new-main"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/applications/update_branch",
                params={"application": "my-app", "branch": "main", "name": "new-main"},
            )


if __name__ == "__main__":
    unittest.main()
