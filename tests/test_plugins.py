import unittest
from unittest.mock import patch
from src.sonarqube import SonarQubeAPI


class TestSonarQubePlugins(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQubeAPI(host="http://localhost:9000", token="test_token")

    def test_get_available_plugins(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_available_plugins()
            mock_get.assert_called_with("http://localhost:9000/api/plugins/available")

    def test_cancel_all_pending_plugins(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.cancel_all_pending_plugins()
            mock_post.assert_called_with("http://localhost:9000/api/plugins/cancel_all")

    def test_download_plugin(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.download_plugin(key="my-plugin")
            mock_get.assert_called_with(
                "http://localhost:9000/api/plugins/download",
                params={"key": "my-plugin"},
            )

    def test_install_plugin(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.install_plugin(key="my-plugin")
            mock_post.assert_called_with(
                "http://localhost:9000/api/plugins/install", params={"key": "my-plugin"}
            )

    def test_get_installed_plugins(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_installed_plugins()
            mock_get.assert_called_with("http://localhost:9000/api/plugins/installed")

    def test_get_pending_plugins(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_pending_plugins()
            mock_get.assert_called_with("http://localhost:9000/api/plugins/pending")

    def test_uninstall_plugin(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.uninstall_plugin(key="my-plugin")
            mock_post.assert_called_with(
                "http://localhost:9000/api/plugins/uninstall",
                params={"key": "my-plugin"},
            )

    def test_update_plugin(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.update_plugin(key="my-plugin")
            mock_post.assert_called_with(
                "http://localhost:9000/api/plugins/update", params={"key": "my-plugin"}
            )

    def test_get_plugin_updates(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_plugin_updates()
            mock_get.assert_called_with("http://localhost:9000/api/plugins/updates")


if __name__ == "__main__":
    unittest.main()
