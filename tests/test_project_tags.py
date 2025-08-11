import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeProjectTags(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_search_project_tags(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_project_tags(q="my-tag")
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_tags/search",
                params={"q": "my-tag"},
            )

    def test_set_project_tags(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_project_tags(project="my-project", tags="tag1,tag2")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_tags/set",
                params={"project": "my-project", "tags": "tag1,tag2"},
            )
