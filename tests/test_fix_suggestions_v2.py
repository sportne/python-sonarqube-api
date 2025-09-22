import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeFixSuggestionsV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_suggest_fix(self):
        with patch.object(self.sonar, "_post") as mock_post:
            self.sonar.fix_suggestions_v2.suggest_fix(
                projectKey="my-project", issueId="my-issue-id"
            )
            mock_post.assert_called_with(
                "/api/v2/fix-suggestions/ai-suggestions",
                json={"projectKey": "my-project", "issueId": "my-issue-id"},
            )

    def test_get_suggestion_availability(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.fix_suggestions_v2.get_suggestion_availability(
                issueId="my-issue-id"
            )
            mock_get.assert_called_with("/api/v2/fix-suggestions/issues/my-issue-id")
