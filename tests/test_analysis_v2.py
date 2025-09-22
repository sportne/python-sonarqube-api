import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeAnalysisV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_active_rules(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.analysis_v2.get_active_rules(projectKey="my-project")
            mock_get.assert_called_with(
                "/api/v2/analysis/active_rules", params={"projectKey": "my-project"}
            )

    def test_get_scanner_engine(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.analysis_v2.get_scanner_engine()
            mock_get.assert_called_with("/api/v2/analysis/engine")

    def test_list_jres(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.analysis_v2.list_jres()
            mock_get.assert_called_with("/api/v2/analysis/jres", params={})

    def test_get_jre(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.analysis_v2.get_jre(jre_id="my-jre-id")
            mock_get.assert_called_with("/api/v2/analysis/jres/my-jre-id")

    def test_get_scanner_engine_version(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.analysis_v2.get_scanner_engine_version()
            mock_get.assert_called_with("/api/v2/analysis/version")
