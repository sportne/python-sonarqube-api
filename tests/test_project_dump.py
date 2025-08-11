import unittest
from unittest.mock import patch, mock_open
from src.sonarqube import SonarQube


class TestSonarQubeProjectDump(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_export_project_dump(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.export_project_dump(project="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_dump/export",
                params={"project": "my-project"},
            )

    def test_import_project_dump(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            with patch("builtins.open", mock_open(read_data=b"test")) as mock_file:
                self.sonar.import_project_dump(file="my-dump.zip", project="my-project")
                mock_file.assert_called_with("my-dump.zip", "rb")
                mock_post.assert_called_with(
                    "http://localhost:9000/api/project_dump/import",
                    params={"project": "my-project"},
                    files={"file": mock_file.return_value},
                )

    def test_get_project_dump_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_project_dump_status(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_dump/status",
                params={"project": "my-project"},
            )
