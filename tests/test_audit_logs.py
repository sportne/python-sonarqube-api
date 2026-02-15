import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeAuditLogs(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_download(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.audit_logs.download(**{"from": "2024-01-01", "to": "2024-12-31"})
            mock_get.assert_called_with(
                "http://localhost:9000/api/audit_logs/download",
                params={"from": "2024-01-01", "to": "2024-12-31"},
            )

    def test_download_no_params(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.audit_logs.download()
            mock_get.assert_called_with(
                "http://localhost:9000/api/audit_logs/download",
                params={},
            )
