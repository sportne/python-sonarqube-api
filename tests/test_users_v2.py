import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeUsersV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_create_user(self):
        with patch.object(self.sonar, "_post") as mock_post:
            self.sonar.users_v2.create_user(login="my-user", name="My User")
            mock_post.assert_called_with(
                "api/v2/users-management/users",
                json={"login": "my-user", "name": "My User"},
            )

    def test_search_users(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.users_v2.search_users(q="my-user")
            mock_get.assert_called_with(
                "api/v2/users-management/users", params={"q": "my-user"}
            )

    def test_get_user(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.users_v2.get_user(user_id="my-user-id")
            mock_get.assert_called_with("api/v2/users-management/users/my-user-id")

    def test_update_user(self):
        with patch.object(self.sonar, "_patch") as mock_patch:
            self.sonar.users_v2.update_user(user_id="my-user-id", name="new-name")
            mock_patch.assert_called_with(
                "api/v2/users-management/users/my-user-id",
                json={"name": "new-name"},
            )

    def test_deactivate_user(self):
        with patch.object(self.sonar, "_delete") as mock_delete:
            self.sonar.users_v2.deactivate_user(user_id="my-user-id")
            mock_delete.assert_called_with(
                "api/v2/users-management/users/my-user-id", params={}
            )
