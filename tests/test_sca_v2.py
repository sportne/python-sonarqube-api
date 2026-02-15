import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeScaV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_risk_reports(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.sca_v2.get_risk_reports(component="my-component")
            mock_get.assert_called_with(
                "api/v2/sca/risk-reports", params={"component": "my-component"}
            )

    def test_get_sbom_reports(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.sca_v2.get_sbom_reports(
                component="my-component", type="cyclonedx"
            )
            mock_get.assert_called_with(
                "api/v2/sca/sbom-reports",
                params={"component": "my-component", "type": "cyclonedx"},
            )
