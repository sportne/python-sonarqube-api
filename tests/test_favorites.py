import unittest
from unittest.mock import patch
from src.sonarqube import SonarQubeAPI


class TestSonarQubeFavorites(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQubeAPI(host="http://localhost:9000", token="test_token")

    def test_add_favorite(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.add_favorite(component="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/favorites/add",
                params={"component": "my-project"},
            )

    def test_remove_favorite(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.remove_favorite(component="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/favorites/remove",
                params={"component": "my-project"},
            )

    def test_search_favorites(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_favorites(p=1, ps=10)
            mock_get.assert_called_with(
                "http://localhost:9000/api/favorites/search", params={"p": 1, "ps": 10}
            )


if __name__ == "__main__":
    unittest.main()
