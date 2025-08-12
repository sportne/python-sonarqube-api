import unittest
from unittest.mock import patch, MagicMock
from src.sonarqube import SonarQube


class TestAuthentication(unittest.TestCase):

    @patch("src.sonarqube.client.requests.Session")
    def test_token_authentication(self, mock_session_cls):
        """
        Test that the client correctly uses the provided token for authentication.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"valid": True}
        mock_session.get.return_value = mock_response

        client = SonarQube(host="http://localhost:9000", token="my_token")
        self.assertTrue(client.is_authenticated())
        self.assertEqual(client.session.auth, ("my_token", ""))
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/authentication/validate"
        )

    @patch("src.sonarqube.client.requests.Session")
    def test_user_password_authentication(self, mock_session_cls):
        """
        Test that the client correctly uses the provided user/password for auth.
        """
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"valid": True}
        mock_session.get.return_value = mock_response

        client = SonarQube(
            host="http://localhost:9000", user="my_user", password="my_password"
        )
        self.assertTrue(client.is_authenticated())
        self.assertEqual(client.session.auth, ("my_user", "my_password"))
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/authentication/validate"
        )
