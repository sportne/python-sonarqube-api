import unittest
from unittest.mock import patch, MagicMock
from src.sonarqube import SonarQubeAPI


class TestIssues(unittest.TestCase):
    @patch("src.sonarqube.requests.Session")
    def test_search_issues(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.search_issues(componentKeys="my-project")
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/issues/search",
            params={"componentKeys": "my-project"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_issue_details(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.get_issue_details("my-issue-key")
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/issues/search",
            params={"issues": "my-issue-key"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_assign_issue(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.assign_issue("my-issue-key", "my-user")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/assign",
            params={"issue": "my-issue-key", "assignee": "my-user"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_add_comment_to_issue(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.add_comment_to_issue("my-issue-key", "my comment")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/add_comment",
            params={"issue": "my-issue-key", "text": "my comment"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_transition_issue(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.transition_issue("my-issue-key", "confirm")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/do_transition",
            params={"issue": "my-issue-key", "transition": "confirm"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_bulk_change_issues(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.bulk_change_issues(issues="my-issue-1,my-issue-2", severity="MAJOR")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/bulk_change",
            params={"issues": "my-issue-1,my-issue-2", "severity": "MAJOR"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_issue_changelog(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.get_issue_changelog("my-issue-key")
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/issues/changelog",
            params={"issue": "my-issue-key"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_delete_comment(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.delete_comment("my-comment-key")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/delete_comment",
            params={"comment": "my-comment-key"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_edit_comment(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.edit_comment("my-comment-key", "new comment")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/edit_comment",
            params={"comment": "my-comment-key", "text": "new comment"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_set_issue_severity(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.set_issue_severity("my-issue-key", "CRITICAL")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/set_severity",
            params={"issue": "my-issue-key", "severity": "CRITICAL"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_set_issue_tags(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.post.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.set_issue_tags("my-issue-key", "tag1,tag2")
        mock_session.post.assert_called_once_with(
            "http://localhost:9000/api/issues/set_tags",
            params={"issue": "my-issue-key", "tags": "tag1,tag2"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_tags(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.get_tags(q="security")
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/issues/tags",
            params={"q": "security"},
        )

    @patch("src.sonarqube.requests.Session")
    def test_get_authors(self, mock_session_cls):
        mock_session = mock_session_cls.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response
        client = SonarQubeAPI(host="http://localhost:9000", token="my_token")
        client.get_authors(q="john")
        mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/issues/authors",
            params={"q": "john"},
        )
