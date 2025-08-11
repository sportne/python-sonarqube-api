import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeMeasures(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_measures_component(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_measures_component(
                component="my-project", metricKeys="ncloc,coverage"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/measures/component",
                params={"component": "my-project", "metricKeys": "ncloc,coverage"},
            )

    def test_get_measures_component_tree(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_measures_component_tree(
                component="my-project", metricKeys="ncloc,coverage", s="metric,name"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/measures/component_tree",
                params={
                    "component": "my-project",
                    "metricKeys": "ncloc,coverage",
                    "s": "metric,name",
                },
            )

    def test_search_measures(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_measures(
                projectKeys="my-project", metricKeys="ncloc,coverage"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/measures/search",
                params={"projectKeys": "my-project", "metricKeys": "ncloc,coverage"},
            )

    def test_search_measures_history(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_measures_history(
                component="my-project", metrics="ncloc,coverage"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/measures/search_history",
                params={"component": "my-project", "metrics": "ncloc,coverage"},
            )


if __name__ == "__main__":
    unittest.main()
