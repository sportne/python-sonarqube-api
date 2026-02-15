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

    def test_create_user(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.create_user(
                login="myuser", name="My User", password="MyPassw0rd%!"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/create",
                params={
                    "login": "myuser",
                    "name": "My User",
                    "password": "MyPassw0rd%!",
                },
            )

    def test_deactivate_user(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.deactivate_user(login="myuser")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/deactivate",
                params={"login": "myuser"},
            )

    def test_get_user_groups(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.get_user_groups(login="admin")
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/groups",
                params={"login": "admin"},
            )

    def test_search_users(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.search_users(q="admin")
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/search",
                params={"q": "admin"},
            )

    def test_update_user(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.update_user(login="myuser", name="New Name")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/update",
                params={"login": "myuser", "name": "New Name"},
            )

    def test_change_password_with_previous(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.change_password(
                login="my-user", password="new-pass", previousPassword="old-pass"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/change_password",
                params={
                    "login": "my-user",
                    "password": "new-pass",
                    "previousPassword": "old-pass",
                },
            )

    def test_dismiss_notice_no_param(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.dismiss_notice()
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/dismiss_notice",
                params={},
            )

    def test_set_homepage_with_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.set_homepage(
                type="PROJECT", branch="main", component="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/set_homepage",
                params={
                    "type": "PROJECT",
                    "branch": "main",
                    "component": "my-project",
                },
            )

    def test_create_user_all_params(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.create_user(
                login="myuser",
                name="My User",
                password="Pass123!",
                email="user@test.com",
                scmAccounts="github-user",
                local=True,
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/create",
                params={
                    "login": "myuser",
                    "name": "My User",
                    "password": "Pass123!",
                    "email": "user@test.com",
                    "scmAccounts": "github-user",
                    "local": True,
                },
            )

    def test_create_user_minimal(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.create_user(login="myuser", name="My User")
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/create",
                params={"login": "myuser", "name": "My User"},
            )

    def test_deactivate_user_with_anonymize(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.deactivate_user(login="myuser", anonymize=True)
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/deactivate",
                params={"login": "myuser", "anonymize": True},
            )

    def test_get_user_groups_all_params(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.get_user_groups(login="admin", q="dev", selected="all")
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/groups",
                params={"login": "admin", "q": "dev", "selected": "all"},
            )

    def test_search_users_all_params(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.search_users(
                q="admin",
                deactivated=True,
                managed=False,
                lastConnectedAfter="2024-01-01",
                lastConnectedBefore="2024-12-31",
                sonarLintLastConnectionDateFrom="2024-06-01",
                sonarLintLastConnectionDateTo="2024-12-31",
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/search",
                params={
                    "q": "admin",
                    "deactivated": True,
                    "managed": False,
                    "lastConnectedAfter": "2024-01-01",
                    "lastConnectedBefore": "2024-12-31",
                    "sonarLintLastConnectionDateFrom": "2024-06-01",
                    "sonarLintLastConnectionDateTo": "2024-12-31",
                },
            )

    def test_search_users_no_params(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.users.search_users()
            mock_get.assert_called_with(
                "http://localhost:9000/api/users/search",
                params={},
            )

    def test_update_user_all_params(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.users.update_user(
                login="myuser",
                name="New Name",
                email="new@test.com",
                scmAccounts="new-scm",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/users/update",
                params={
                    "login": "myuser",
                    "name": "New Name",
                    "email": "new@test.com",
                    "scmAccounts": "new-scm",
                },
            )
