import unittest
from unittest.mock import patch
from src.sonarqube import SonarQubeAPI


class TestSonarQubeDuplications(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQubeAPI(host="http://localhost:9000", token="test_token")

    def test_get_duplications(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_duplications(key="my-file-key", branch="main")
            mock_get.assert_called_with(
                "http://localhost:9000/api/duplications/show",
                params={"key": "my-file-key", "branch": "main"},
            )


if __name__ == "__main__":
    unittest.main()
