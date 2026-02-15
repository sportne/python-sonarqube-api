import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeAlmIntegrations(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_list_azure_projects(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.list_azure_projects(almSetting="my-azure")
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/list_azure_projects",
                params={"almSetting": "my-azure"},
            )

    def test_list_bitbucketserver_projects(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.list_bitbucketserver_projects(
                almSetting="my-bbs"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/list_bitbucketserver_projects",
                params={"almSetting": "my-bbs"},
            )

    def test_search_azure_repos(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_azure_repos(
                almSetting="my-azure", projectName="MyProject"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_azure_repos",
                params={"almSetting": "my-azure", "projectName": "MyProject"},
            )

    def test_search_bitbucketcloud_repos(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_bitbucketcloud_repos(almSetting="my-bbc")
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_bitbucketcloud_repos",
                params={"almSetting": "my-bbc"},
            )

    def test_search_bitbucketserver_repos(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_bitbucketserver_repos(
                almSetting="my-bbs", projectName="MyProject"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_bitbucketserver_repos",
                params={"almSetting": "my-bbs", "projectName": "MyProject"},
            )

    def test_search_gitlab_repos(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_gitlab_repos(almSetting="my-gitlab")
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_gitlab_repos",
                params={"almSetting": "my-gitlab"},
            )

    def test_import_github_project(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_integrations.import_github_project(
                almSetting="my-github",
                organization="my-org",
                repository="my-repo",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_integrations/import_github_project",
                params={
                    "almSetting": "my-github",
                    "organization": "my-org",
                    "repository": "my-repo",
                },
            )

    def test_set_pat(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_integrations.set_pat(
                almSetting="my-bbs", pat="my-pat", username="admin"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_integrations/set_pat",
                params={
                    "almSetting": "my-bbs",
                    "pat": "my-pat",
                    "username": "admin",
                },
            )

    def test_search_azure_repos_with_search_query(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_azure_repos(
                almSetting="my-azure", searchQuery="test"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_azure_repos",
                params={"almSetting": "my-azure", "searchQuery": "test"},
            )

    def test_search_bitbucketserver_repos_with_search_query(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_bitbucketserver_repos(
                almSetting="my-bbs", searchQuery="myrepo"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_bitbucketserver_repos",
                params={"almSetting": "my-bbs", "searchQuery": "myrepo"},
            )

    def test_search_gitlab_repos_with_project_name(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.alm_integrations.search_gitlab_repos(
                almSetting="my-gitlab", projectName="TestProject"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/alm_integrations/search_gitlab_repos",
                params={
                    "almSetting": "my-gitlab",
                    "projectName": "TestProject",
                },
            )

    def test_set_pat_without_username(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.alm_integrations.set_pat(almSetting="my-bb", pat="my-pat")
            mock_post.assert_called_with(
                "http://localhost:9000/api/alm_integrations/set_pat",
                params={"almSetting": "my-bb", "pat": "my-pat"},
            )
