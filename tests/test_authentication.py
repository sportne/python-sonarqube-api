import unittest
from unittest.mock import MagicMock

from src.sonarqube.authentication import SonarQubeAuthentication


class TestSonarQubeAuthentication(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock()
        self.auth = SonarQubeAuthentication(self.client)

    def test_login(self):
        self.auth.login("admin", "password")
        self.client._post.assert_called_once_with(
            "api/authentication/login",
            params={"login": "admin", "password": "password"},
        )

    def test_logout(self):
        self.auth.logout()
        self.client._post.assert_called_once_with("api/authentication/logout")

    def test_validate(self):
        self.auth.validate()
        self.client._get.assert_called_once_with("api/authentication/validate")

    def test_is_authenticated_success(self):
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"valid": True}
        self.client._get.return_value = response
        self.assertTrue(self.auth.is_authenticated())

    def test_is_authenticated_failure(self):
        response = MagicMock()
        response.status_code = 401
        response.json.return_value = {"valid": False}
        self.client._get.return_value = response
        self.assertFalse(self.auth.is_authenticated())


if __name__ == "__main__":
    unittest.main()
