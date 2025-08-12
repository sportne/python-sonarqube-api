import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeHotspots(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_add_hotspot_comment(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.hotspots.add_hotspot_comment(
                hotspot="my-hotspot", text="my comment"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/hotspots/add_comment",
                params={"hotspot": "my-hotspot", "text": "my comment"},
            )

    def test_assign_hotspot(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.hotspots.assign_hotspot(hotspot="my-hotspot", assignee="my-user")
            mock_post.assert_called_with(
                "http://localhost:9000/api/hotspots/assign",
                params={"hotspot": "my-hotspot", "assignee": "my-user"},
            )

    def test_change_hotspot_status(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.hotspots.change_hotspot_status(
                hotspot="my-hotspot",
                status="REVIEWED",
                resolution="FIXED",
                comment="my comment",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/hotspots/change_status",
                params={
                    "hotspot": "my-hotspot",
                    "status": "REVIEWED",
                    "resolution": "FIXED",
                    "comment": "my comment",
                },
            )

    def test_delete_hotspot_comment(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.hotspots.delete_hotspot_comment(comment="my-comment-key")
            mock_post.assert_called_with(
                "http://localhost:9000/api/hotspots/delete_comment",
                params={"comment": "my-comment-key"},
            )

    def test_edit_hotspot_comment(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.hotspots.edit_hotspot_comment(
                comment="my-comment-key", text="new comment"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/hotspots/edit_comment",
                params={"comment": "my-comment-key", "text": "new comment"},
            )

    def test_list_hotspots(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.hotspots.list_hotspots(projectKey="my-project", p=1, ps=10)
            mock_get.assert_called_with(
                "http://localhost:9000/api/hotspots/list",
                params={"projectKey": "my-project", "p": 1, "ps": 10},
            )

    def test_pull_hotspots(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.hotspots.pull_hotspots(branch="main", project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/hotspots/pull",
                params={"branch": "main", "project": "my-project"},
            )

    def test_search_hotspots(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.hotspots.search_hotspots(
                projectKey="my-project", status="TO_REVIEW"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/hotspots/search",
                params={"projectKey": "my-project", "status": "TO_REVIEW"},
            )

    def test_show_hotspot(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.hotspots.show_hotspot(hotspot="my-hotspot")
            mock_get.assert_called_with(
                "http://localhost:9000/api/hotspots/show",
                params={"hotspot": "my-hotspot"},
            )


if __name__ == "__main__":
    unittest.main()
