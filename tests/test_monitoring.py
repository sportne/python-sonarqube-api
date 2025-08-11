import unittest
from unittest.mock import patch
from src.sonarqube import SonarQubeAPI


class TestSonarQubeMonitoring(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQubeAPI(host="http://localhost:9000", token="test_token")

    def test_get_monitoring_metrics(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_monitoring_metrics()
            mock_get.assert_called_with("http://localhost:9000/api/monitoring/metrics")


if __name__ == "__main__":
    unittest.main()
