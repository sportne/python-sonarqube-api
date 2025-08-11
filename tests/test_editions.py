import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeEditions(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_activate_grace_period(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.activate_grace_period()
            mock_post.assert_called_with(
                "http://localhost:9000/api/editions/activate_grace_period"
            )

    def test_is_valid_license(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.is_valid_license()
            mock_get.assert_called_with(
                "http://localhost:9000/api/editions/is_valid_license"
            )

    def test_set_license(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_license(license="my-license-key")
            mock_post.assert_called_with(
                "http://localhost:9000/api/editions/set_license",
                params={"license": "my-license-key"},
            )

    def test_show_license(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.show_license()
            mock_get.assert_called_with(
                "http://localhost:9000/api/editions/show_license"
            )

    def test_unset_license(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.unset_license()
            mock_post.assert_called_with(
                "http://localhost:9000/api/editions/unset_license"
            )


if __name__ == "__main__":
    unittest.main()
