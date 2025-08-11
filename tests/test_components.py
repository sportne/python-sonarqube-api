import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeComponents(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_get_components_app(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_components_app(component="my-project", branch="main")
            mock_get.assert_called_with(
                "http://localhost:9000/api/components/app",
                params={"component": "my-project", "branch": "main"},
            )

    def test_search_components(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_components(qualifiers="TRK", q="test", p=1, ps=10)
            mock_get.assert_called_with(
                "http://localhost:9000/api/components/search",
                params={"qualifiers": "TRK", "q": "test", "p": 1, "ps": 10},
            )

    def test_search_components_projects(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_components_projects(q="test", p=1, ps=10)
            mock_get.assert_called_with(
                "http://localhost:9000/api/components/search_projects",
                params={"q": "test", "p": 1, "ps": 10},
            )

    def test_show_component(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.show_component(component="my-project", branch="main")
            mock_get.assert_called_with(
                "http://localhost:9000/api/components/show",
                params={"component": "my-project", "branch": "main"},
            )

    def test_get_component_suggestions(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_component_suggestions(q="test")
            mock_get.assert_called_with(
                "http://localhost:9000/api/components/suggestions", params={"q": "test"}
            )

    def test_get_component_tree(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_component_tree(component="my-project", s="name", asc="true")
            mock_get.assert_called_with(
                "http://localhost:9000/api/components/tree",
                params={"component": "my-project", "s": "name", "asc": "true"},
            )


if __name__ == "__main__":
    unittest.main()
