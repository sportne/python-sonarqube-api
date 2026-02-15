import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeServer(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_version(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.server.get_version()
            mock_get.assert_called_with("http://localhost:9000/api/server/version")
