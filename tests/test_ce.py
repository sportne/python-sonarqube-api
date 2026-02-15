import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeCE(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_ce_activity(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_activity(componentId="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/ce/activity",
                params={"componentId": "my-project"},
            )

    def test_get_ce_activity_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_activity_status(componentId="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/ce/activity_status",
                params={"componentId": "my-project"},
            )

    def test_get_ce_analysis_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_analysis_status(analysisId="12345")
            mock_get.assert_called_with(
                "http://localhost:9000/api/ce/analysis_status",
                params={"analysisId": "12345"},
            )

    def test_cancel_ce_task(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.cancel_ce_task(id="12345")
            mock_post.assert_called_with(
                "http://localhost:9000/api/ce/cancel", params={"id": "12345"}
            )

    def test_cancel_all_ce_tasks(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.cancel_all_ce_tasks()
            mock_post.assert_called_with("http://localhost:9000/api/ce/cancel_all")

    def test_get_ce_component(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_component(component="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/ce/component",
                params={"component": "my-project"},
            )

    def test_dismiss_ce_analysis_warning(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.dismiss_ce_analysis_warning(
                project="my-project", warning="my-warning"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/ce/dismiss_analysis_warning",
                params={"project": "my-project", "warning": "my-warning"},
            )

    def test_get_ce_indexation_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_indexation_status()
            mock_get.assert_called_with(
                "http://localhost:9000/api/ce/indexation_status"
            )

    def test_get_ce_info(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_info()
            mock_get.assert_called_with("http://localhost:9000/api/ce/info")

    def test_pause_ce(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.pause_ce()
            mock_post.assert_called_with("http://localhost:9000/api/ce/pause")

    def test_resume_ce(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.resume_ce()
            mock_post.assert_called_with("http://localhost:9000/api/ce/resume")

    def test_set_ce_worker_count(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.set_ce_worker_count(count=5)
            mock_post.assert_called_with(
                "http://localhost:9000/api/ce/set_worker_count", params={"count": 5}
            )

    def test_submit_scanner_report(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.ce.submit_scanner_report(projectKey="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/ce/submit",
                params={"projectKey": "my-project"},
            )

    def test_get_ce_task(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_task(id="12345")
            mock_get.assert_called_with(
                "http://localhost:9000/api/ce/task", params={"id": "12345"}
            )

    def test_get_ce_task_types(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_task_types()
            mock_get.assert_called_with("http://localhost:9000/api/ce/task_types")

    def test_get_ce_worker_count(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.ce.get_ce_worker_count()
            mock_get.assert_called_with("http://localhost:9000/api/ce/worker_count")


if __name__ == "__main__":
    unittest.main()
