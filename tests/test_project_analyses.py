import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeProjectAnalyses(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_create_project_analysis_event(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_analyses.create_project_analysis_event(
                analysis="my-analysis", name="my-event"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_analyses/create_event",
                params={"analysis": "my-analysis", "name": "my-event"},
            )

    def test_delete_project_analysis(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_analyses.delete_project_analysis(analysis="my-analysis")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_analyses/delete",
                params={"analysis": "my-analysis"},
            )

    def test_delete_project_analysis_event(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_analyses.delete_project_analysis_event(event="my-event")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_analyses/delete_event",
                params={"event": "my-event"},
            )

    def test_search_project_analyses(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.project_analyses.search_project_analyses(
                project="my-project", category="VERSION"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_analyses/search",
                params={"project": "my-project", "category": "VERSION"},
            )

    def test_update_project_analysis_event(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.project_analyses.update_project_analysis_event(
                event="my-event", name="new-name"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_analyses/update_event",
                params={"event": "my-event", "name": "new-name"},
            )


if __name__ == "__main__":
    unittest.main()
