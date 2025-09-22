import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeUsers(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_change_password(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.change_password(login="my-user", password="new-password")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/change_password",
                params={"login": "my-user", "password": "new-password"},
            )

    def test_get_current_user(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.get_current_user()
            mock_get.assert_called_with("http://localhost:9000/api/users/current")

    def test_dismiss_notice(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.dismiss_notice(notice="my-notice")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/dismiss_notice",
                params={"notice": "my-notice"},
            )

    def test_get_identity_providers(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.get_identity_providers()
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/identity_providers"
            )

    def test_set_ai_tool_usage(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.set_ai_tool_usage(project="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/set_ai_tool_usage",
                params={"project": "my-project"},
            )

    def test_set_homepage(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.set_homepage(type="PROJECT", component="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/set_homepage",
                params={"type": "PROJECT", "component": "my-project"},
            )
