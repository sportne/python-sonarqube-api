import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeAlmSettings(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_delete_binding(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.delete_binding(project="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/delete_binding",
                params={"project": "my-project"},
            )

    def test_get_binding(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_settings.get_binding(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_settings/get_binding",
                params={"project": "my-project"},
            )

    def test_list_settings(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_settings.list_settings(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_settings/list",
                params={"project": "my-project"},
            )

    def test_list_definitions(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_settings.list_definitions()
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_settings/list_definitions"
            )

    def test_set_azure_binding(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_azure_binding(
                almSetting="my-azure", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_azure_binding",
                params={"almSetting": "my-azure", "project": "my-project"},
            )

    def test_set_bitbucket_binding(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_bitbucket_binding(
                almSetting="my-bbs", project="my-project", repository="my-repo"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_bitbucket_binding",
                params={
                    "almSetting": "my-bbs",
                    "project": "my-project",
                    "repository": "my-repo",
                },
            )

    def test_set_github_binding(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_github_binding(
                almSetting="my-github", project="my-project", repository="my-repo"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_github_binding",
                params={
                    "almSetting": "my-github",
                    "project": "my-project",
                    "repository": "my-repo",
                },
            )

    def test_set_gitlab_binding(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_gitlab_binding(
                almSetting="my-gitlab", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_gitlab_binding",
                params={"almSetting": "my-gitlab", "project": "my-project"},
            )

    def test_list_settings_no_project(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_settings.list_settings()
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_settings/list",
                params={},
            )

    def test_set_azure_binding_all_params(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_azure_binding(
                almSetting="my-azure",
                project="my-project",
                projectName="AzureProject",
                repositoryName="AzureRepo",
                monorepo=True,
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_azure_binding",
                params={
                    "almSetting": "my-azure",
                    "project": "my-project",
                    "projectName": "AzureProject",
                    "repositoryName": "AzureRepo",
                    "monorepo": True,
                },
            )

    def test_set_bitbucket_binding_all_params(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_bitbucket_binding(
                almSetting="my-bbs",
                project="my-project",
                repository="my-repo",
                slug="my-slug",
                monorepo=False,
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_bitbucket_binding",
                params={
                    "almSetting": "my-bbs",
                    "project": "my-project",
                    "repository": "my-repo",
                    "slug": "my-slug",
                    "monorepo": False,
                },
            )

    def test_set_github_binding_with_monorepo(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_github_binding(
                almSetting="my-github",
                project="my-project",
                repository="my-repo",
                monorepo=True,
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_github_binding",
                params={
                    "almSetting": "my-github",
                    "project": "my-project",
                    "repository": "my-repo",
                    "monorepo": True,
                },
            )

    def test_set_gitlab_binding_all_params(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_settings.set_gitlab_binding(
                almSetting="my-gitlab",
                project="my-project",
                repository="my-repo",
                monorepo=False,
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_settings/set_gitlab_binding",
                params={
                    "almSetting": "my-gitlab",
                    "project": "my-project",
                    "repository": "my-repo",
                    "monorepo": False,
                },
            )
