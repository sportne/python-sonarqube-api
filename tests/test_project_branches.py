import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeProjectBranches(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_delete_project_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.delete_project_branch(project="my-project", branch="my-branch")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_branches/delete",
                params={"project": "my-project", "branch": "my-branch"},
            )

    def test_get_project_branch_ai_code_assurance(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_project_branch_ai_code_assurance(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_branches/get_ai_code_assurance",
                params={"project": "my-project"},
            )

    def test_get_project_branch_ai_code_assurance_with_branch(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_project_branch_ai_code_assurance(
                project="my-project", branch="my-branch"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_branches/get_ai_code_assurance",
                params={"project": "my-project", "branch": "my-branch"},
            )

    def test_list_project_branches(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.list_project_branches(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/project_branches/list",
                params={"project": "my-project"},
            )

    def test_rename_project_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.rename_project_branch(project="my-project", name="new-name")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_branches/rename",
                params={"project": "my-project", "name": "new-name"},
            )

    def test_set_project_branch_automatic_deletion_protection(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_project_branch_automatic_deletion_protection(
                project="my-project", branch="my-branch", is_protected=True
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_branches/set_automatic_deletion_protection",
                params={
                    "project": "my-project",
                    "branch": "my-branch",
                    "isProtected": True,
                },
            )

    def test_set_project_main_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_project_main_branch(project="my-project", branch="new-main")
            mock_post.assert_called_with(
                "http://localhost:9000/api/project_branches/set_main",
                params={"project": "my-project", "branch": "new-main"},
            )
