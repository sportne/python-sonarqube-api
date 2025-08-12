import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeUsers(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_search_users(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.search_users(q="my-user")
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/search",
                params={"q": "my-user"},
            )

    def test_create_user(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.create_user(login="my-user", name="My User")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/create",
                params={"login": "my-user", "name": "My User"},
            )

    def test_deactivate_user(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.deactivate_user(login="my-user")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/deactivate",
                params={"login": "my-user"},
            )

    def test_update_user(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.update_user(login="my-user", name="new-name")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/update",
                params={"login": "my-user", "name": "new-name"},
            )

    def test_change_user_password(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.change_user_password(
                login="my-user", new_password="new-password"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/change_password",
                params={"login": "my-user", "password": "new-password"},
            )

    def test_get_user_groups(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.get_user_groups(login="my-user")
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/groups",
                params={"login": "my-user"},
            )

    def test_search_user_tokens(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.search_user_tokens(login="my-user")
            mock_get.assert_called_with(
                "http://localhost:9000/api/user_tokens/search",
                params={"login": "my-user"},
            )

    def test_generate_user_token(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.generate_user_token(login="my-user", name="my-token")
            mock_post.assert_called_with(
                "http://localhost:9000/api/user_tokens/generate",
                params={"login": "my-user", "name": "my-token"},
            )

    def test_revoke_user_token(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.revoke_user_token(login="my-user", name="my-token")
            mock_post.assert_called_with(
                "http://localhost:9000/api/user_tokens/revoke",
                params={"login": "my-user", "name": "my-token"},
            )
