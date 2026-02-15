import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeAnalysisCache(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.analysis_cache.get(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/analysis_cache/get",
                params={"project": "my-project"},
            )

    def test_get_with_branch(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.analysis_cache.get(project="my-project", branch="main")
            mock_get.assert_called_with(
                "http://localhost:9000/api/analysis_cache/get",
                params={"project": "my-project", "branch": "main"},
            )
