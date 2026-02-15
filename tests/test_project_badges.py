import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeProjectBadges(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_project_badge_ai_code_assurance(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_badges.get_project_badge_ai_code_assurance(
                project="my-project", branch="main"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_badges/ai_code_assurance",
                params={"project": "my-project", "branch": "main"},
            )

    def test_get_project_badge_measure(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_badges.get_project_badge_measure(
                project="my-project", metric="coverage", branch="main"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_badges/measure",
                params={
                    "project": "my-project",
                    "metric": "coverage",
                    "branch": "main",
                },
            )

    def test_get_project_badge_quality_gate(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_badges.get_project_badge_quality_gate(
                project="my-project", branch="main"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_badges/quality_gate",
                params={"project": "my-project", "branch": "main"},
            )

    def test_renew_project_badge_token(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_badges.renew_project_badge_token(project="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_badges/renew_token",
                params={"project": "my-project"},
            )

    def test_get_project_badge_token(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_badges.get_project_badge_token(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_badges/token",
                params={"project": "my-project"},
            )


if __name__ == "__main__":
    unittest.main()
