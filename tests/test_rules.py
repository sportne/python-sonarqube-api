import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeRules(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_rules_app(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.rules.get_rules_app()
            mock_get.assert_called_with("http://localhost:9000/api/rules/app")

    def test_create_rule(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.rules.create_rule(
                custom_key="my-rule",
                name="My Rule",
                markdown_description="My rule description",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/rules/create",
                params={
                    "custom_key": "my-rule",
                    "name": "My Rule",
                    "markdown_description": "My rule description",
                },
            )

    def test_delete_rule(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.rules.delete_rule(key="my-rule")
            mock_post.assert_called_with(
                "http://localhost:9000/api/rules/delete",
                params={"key": "my-rule"},
            )

    def test_list_rules(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.rules.list_rules(q="my-rule")
            mock_get.assert_called_with(
                "http://localhost:9000/api/rules/list",
                params={"q": "my-rule"},
            )

    def test_list_rule_repositories(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.rules.list_rule_repositories(language="java")
            mock_get.assert_called_with(
                "http://localhost:9000/api/rules/repositories",
                params={"language": "java"},
            )

    def test_search_rules(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.rules.search_rules(q="my-rule")
            mock_get.assert_called_with(
                "http://localhost:9000/api/rules/search",
                params={"q": "my-rule"},
            )

    def test_show_rule(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.rules.show_rule(key="my-rule")
            mock_get.assert_called_with(
                "http://localhost:9000/api/rules/show",
                params={"key": "my-rule"},
            )

    def test_list_rule_tags(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.rules.list_rule_tags(q="security")
            mock_get.assert_called_with(
                "http://localhost:9000/api/rules/tags",
                params={"q": "security"},
            )

    def test_update_rule(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.rules.update_rule(key="my-rule", name="new-name")
            mock_post.assert_called_with(
                "http://localhost:9000/api/rules/update",
                params={"key": "my-rule", "name": "new-name"},
            )
