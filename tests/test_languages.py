import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeLanguages(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_list_languages(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.languages.list_languages(q="java")
            mock_get.assert_called_with(
                "http://localhost:9000/api/languages/list", params={"q": "java"}
            )


if __name__ == "__main__":
    unittest.main()
