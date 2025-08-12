import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeSystem(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_system_health(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.system.get_system_health()
            mock_get.assert_called_with("http://localhost:9000/api/system/health")

    def test_get_system_metrics(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.system.get_system_metrics()
            mock_get.assert_called_with("http://localhost:9000/api/system/metrics")

    def test_get_system_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.system.get_system_status()
            mock_get.assert_called_with("http://localhost:9000/api/system/status")

    def test_get_system_upgrades(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.system.get_system_upgrades()
            mock_get.assert_called_with("http://localhost:9000/api/system/upgrades")

    def test_get_system_logs(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.system.get_system_logs()
            mock_get.assert_called_with("http://localhost:9000/api/system/logs")

    def test_get_system_info(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.system.get_system_info()
            mock_get.assert_called_with("http://localhost:9000/api/system/info")
