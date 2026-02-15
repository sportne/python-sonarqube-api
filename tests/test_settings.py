import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeSettings(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_list_definitions(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.settings.list_definitions()
            mock_get.assert_called_with(
                "http://localhost:9000/api/settings/list_definitions",
                params={},
            )

    def test_list_definitions_with_component(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.settings.list_definitions(component="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/settings/list_definitions",
                params={"component": "my-project"},
            )

    def test_reset(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.settings.reset(keys="sonar.core.serverBaseURL")
            mock_post.assert_called_with(
                "http://localhost:9000/api/settings/reset",
                params={"keys": "sonar.core.serverBaseURL"},
            )

    def test_set(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.settings.set(
                key="sonar.core.serverBaseURL",
                value="http://my-server.com",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/settings/set",
                params={
                    "key": "sonar.core.serverBaseURL",
                    "value": "http://my-server.com",
                },
            )

    def test_values(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.settings.values(keys="sonar.core.serverBaseURL")
            mock_get.assert_called_with(
                "http://localhost:9000/api/settings/values",
                params={"keys": "sonar.core.serverBaseURL"},
            )

    def test_reset_with_all_params(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.settings.reset(
                keys="sonar.key",
                component="my-project",
                branch="main",
                pullRequest="42",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/settings/reset",
                params={
                    "keys": "sonar.key",
                    "component": "my-project",
                    "branch": "main",
                    "pullRequest": "42",
                },
            )

    def test_set_with_values(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.settings.set(
                key="sonar.links.homepage",
                values=["http://example.com"],
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/settings/set",
                params={
                    "key": "sonar.links.homepage",
                    "values": ["http://example.com"],
                },
            )

    def test_set_with_field_values(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.settings.set(
                key="sonar.issue.enforce",
                fieldValues='{"ruleKey":"squid:S001"}',
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/settings/set",
                params={
                    "key": "sonar.issue.enforce",
                    "fieldValues": '{"ruleKey":"squid:S001"}',
                },
            )

    def test_set_with_component(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.settings.set(
                key="sonar.key", value="val", component="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/settings/set",
                params={
                    "key": "sonar.key",
                    "value": "val",
                    "component": "my-project",
                },
            )

    def test_values_no_params(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.settings.values()
            mock_get.assert_called_with(
                "http://localhost:9000/api/settings/values",
                params={},
            )

    def test_values_with_component(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.settings.values(keys="sonar.key", component="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/settings/values",
                params={"keys": "sonar.key", "component": "my-project"},
            )
