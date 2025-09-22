import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeCleanCodePolicyV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_create_custom_rule(self):
        with patch.object(self.sonar, "_post") as mock_post:
            self.sonar.clean_code_policy_v2.create_custom_rule(
                key="my-rule-key",
                templateKey="my-template-key",
                name="my-rule-name",
                markdownDescription="my-description",
                impacts=[],
            )
            mock_post.assert_called_with(
                "api/v2/clean-code-policy/rules",
                json={
                    "key": "my-rule-key",
                    "templateKey": "my-template-key",
                    "name": "my-rule-name",
                    "markdownDescription": "my-description",
                    "impacts": [],
                },
            )
