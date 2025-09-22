import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeWebServices(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_list_web_services(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.web_services.list_web_services()
            mock_get.assert_called_with(
                "http://localhost:9000/api/webservices/list", params={}
            )

    def test_get_web_service_response_example(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.web_services.get_web_service_response_example(
                action="search", controller="api/issues"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/webservices/response_example",
                params={"action": "search", "controller": "api/issues"},
            )
