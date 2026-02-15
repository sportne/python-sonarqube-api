import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeMetrics(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_search_metrics(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.metrics.search_metrics(p=1, ps=10)
            mock_get.assert_called_with(
                "http://localhost:9000/api/metrics/search", params={"p": 1, "ps": 10}
            )

    def test_get_metric_types(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.metrics.get_metric_types()
            mock_get.assert_called_with("http://localhost:9000/api/metrics/types")


if __name__ == "__main__":
    unittest.main()
