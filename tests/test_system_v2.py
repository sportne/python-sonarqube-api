import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeSystemV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_system_health(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.system_v2.get_system_health()
            mock_get.assert_called_with("/api/v2/system/health", headers={})

    def test_get_system_liveness(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.system_v2.get_system_liveness()
            mock_get.assert_called_with("/api/v2/system/liveness", headers={})

    def test_get_migrations_status(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.system_v2.get_migrations_status()
            mock_get.assert_called_with("/api/v2/system/migrations-status")
