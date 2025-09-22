import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeDopTranslationV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_create_project(self):
        with patch.object(self.sonar, "_post") as mock_post:
            self.sonar.dop_translation_v2.create_project(
                projectKey="my-project-key",
                projectName="my-project-name",
                devOpsPlatformSettingId="my-setting-id",
                repositoryIdentifier="my-repo-id",
                monorepo=False,
            )
            mock_post.assert_called_with(
                "api/v2/dop-translation/bound-projects",
                json={
                    "projectKey": "my-project-key",
                    "projectName": "my-project-name",
                    "devOpsPlatformSettingId": "my-setting-id",
                    "repositoryIdentifier": "my-repo-id",
                    "monorepo": False,
                },
            )

    def test_list_dop_settings(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.dop_translation_v2.list_dop_settings()
            mock_get.assert_called_with("api/v2/dop-translation/dop-settings")
