import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestIssues(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="my_token")

    def test_search_issues(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.search_issues(componentKeys="my-project")
            mock_get.assert_called_once_with(
                "http://localhost:9000/api/issues/search",
                params={"componentKeys": "my-project"},
            )

    def test_get_issue_details(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.get_issue_details("my-issue-key")
            mock_get.assert_called_once_with(
                "http://localhost:9000/api/issues/search",
                params={"issues": "my-issue-key"},
            )

    def test_assign_issue(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.assign_issue("my-issue-key", "my-user")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/assign",
                params={"issue": "my-issue-key", "assignee": "my-user"},
            )

    def test_add_comment_to_issue(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.add_comment_to_issue("my-issue-key", "my comment")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/add_comment",
                params={"issue": "my-issue-key", "text": "my comment"},
            )

    def test_transition_issue(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.transition_issue("my-issue-key", "confirm")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/do_transition",
                params={"issue": "my-issue-key", "transition": "confirm"},
            )

    def test_bulk_change_issues(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.bulk_change_issues(
                issues="my-issue-1,my-issue-2", severity="MAJOR"
            )
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/bulk_change",
                params={"issues": "my-issue-1,my-issue-2", "severity": "MAJOR"},
            )

    def test_get_issue_changelog(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.get_issue_changelog("my-issue-key")
            mock_get.assert_called_once_with(
                "http://localhost:9000/api/issues/changelog",
                params={"issue": "my-issue-key"},
            )

    def test_delete_comment(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.delete_comment("my-comment-key")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/delete_comment",
                params={"comment": "my-comment-key"},
            )

    def test_edit_comment(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.edit_comment("my-comment-key", "new comment")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/edit_comment",
                params={"comment": "my-comment-key", "text": "new comment"},
            )

    def test_set_issue_severity(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.set_issue_severity("my-issue-key", "CRITICAL")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/set_severity",
                params={"issue": "my-issue-key", "severity": "CRITICAL"},
            )

    def test_set_issue_tags(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.set_issue_tags("my-issue-key", "tag1,tag2")
            mock_post.assert_called_once_with(
                "http://localhost:9000/api/issues/set_tags",
                params={"issue": "my-issue-key", "tags": "tag1,tag2"},
            )

    def test_get_tags(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.get_tags(q="security")
            mock_get.assert_called_once_with(
                "http://localhost:9000/api/issues/tags",
                params={"q": "security"},
            )

    def test_get_authors(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.get_authors(q="john")
            mock_get.assert_called_once_with(
                "http://localhost:9000/api/issues/authors",
                params={"q": "john"},
            )

    def test_get_anticipated_issue_transitions(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.get_anticipated_issue_transitions(issue="my-issue")
            mock_post.assert_called_with(
                "http://localhost:9000/api/issues/anticipated_transitions",
                params={"issue": "my-issue"},
            )

    def test_get_issue_component_tags(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.get_issue_component_tags(component="my-component")
            mock_get.assert_called_with(
                "http://localhost:9000/api/issues/component_tags",
                params={"component": "my-component"},
            )

    def test_export_issues_gitlab_sast(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.export_issues_gitlab_sast(
                project="my-project", branch="main"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/issues/gitlab_sast_export",
                params={"project": "my-project", "branch": "main"},
            )

    def test_list_issues(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.list_issues(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/issues/list",
                params={"project": "my-project"},
            )

    def test_pull_issues(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.pull_issues(branch="main", project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/issues/pull",
                params={"branch": "main", "project": "my-project"},
            )

    def test_pull_taint_issues(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.issues.pull_taint_issues(branch="main", project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/issues/pull_taint",
                params={"branch": "main", "project": "my-project"},
            )

    def test_reindex_issues(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.issues.reindex_issues(project="my-project")
            mock_post.assert_called_with(
                "http://localhost:9000/api/issues/reindex",
                params={"project": "my-project"},
            )
