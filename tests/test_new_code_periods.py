import unittest
from unittest.mock import patch
from src.sonarqube import SonarQubeAPI


class TestSonarQubeNewCodePeriods(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQubeAPI(host="http://localhost:9000", token="test_token")

    def test_list_new_code_periods(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.list_new_code_periods(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/new_code_periods/list",
                params={"project": "my-project"},
            )

    def test_set_new_code_period(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_new_code_period(
                project="my-project", type="PREVIOUS_VERSION", value="1.0"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/new_code_periods/set",
                params={
                    "project": "my-project",
                    "type": "PREVIOUS_VERSION",
                    "value": "1.0",
                },
            )

    def test_show_new_code_period(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.show_new_code_period(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/new_code_periods/show",
                params={"project": "my-project"},
            )

    def test_unset_new_code_period(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.unset_new_code_period(project="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/new_code_periods/unset",
                params={"project": "my-project"},
            )


if __name__ == "__main__":
    unittest.main()
