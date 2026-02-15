import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeUserTokens(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_generate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.user_tokens.generate(name="my-token")
            mock_post.assert_called_with(
                "http://localhost:9000/api/user_tokens/generate",
                params={"name": "my-token"},
            )

    def test_generate_with_options(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.user_tokens.generate(
                name="my-token",
                login="admin",
                type="PROJECT_ANALYSIS_TOKEN",
                projectKey="my-project",
                expirationDate="2025-12-31",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/user_tokens/generate",
                params={
                    "name": "my-token",
                    "login": "admin",
                    "type": "PROJECT_ANALYSIS_TOKEN",
                    "projectKey": "my-project",
                    "expirationDate": "2025-12-31",
                },
            )

    def test_revoke(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.user_tokens.revoke(name="my-token")
            mock_post.assert_called_with(
                "http://localhost:9000/api/user_tokens/revoke",
                params={"name": "my-token"},
            )

    def test_revoke_with_login(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.user_tokens.revoke(name="my-token", login="admin")
            mock_post.assert_called_with(
                "http://localhost:9000/api/user_tokens/revoke",
                params={"name": "my-token", "login": "admin"},
            )

    def test_search(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.user_tokens.search()
            mock_get.assert_called_with(
                "http://localhost:9000/api/user_tokens/search",
                params={},
            )

    def test_search_with_login(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.user_tokens.search(login="admin")
            mock_get.assert_called_with(
                "http://localhost:9000/api/user_tokens/search",
                params={"login": "admin"},
            )
