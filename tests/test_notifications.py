import unittest
from unittest.mock import patch
from src.sonarqube import SonarQubeAPI


class TestSonarQubeNotifications(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQubeAPI(host="http://localhost:9000", token="test_token")

    def test_add_notification(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.add_notification(
                login="my-user", type="my-type", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/notifications/add",
                params={"login": "my-user", "type": "my-type", "project": "my-project"},
            )

    def test_list_notifications(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.list_notifications(login="my-user")
            mock_get.assert_called_with(
                "http://localhost:9000/api/notifications/list",
                params={"login": "my-user"},
            )

    def test_remove_notification(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.remove_notification(
                login="my-user", type="my-type", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/notifications/remove",
                params={"login": "my-user", "type": "my-type", "project": "my-project"},
            )


if __name__ == "__main__":
    unittest.main()
