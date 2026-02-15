import unittest
from unittest.mock import MagicMock, patch

from src.sonarqube import SonarQube


class TestSources(unittest.TestCase):
    def setUp(self):
        self.patcher = patch("src.sonarqube.client.requests.Session")
        self.mock_session_cls = self.patcher.start()
        self.mock_session = self.mock_session_cls.return_value
        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {}
        self.mock_session.get.return_value = self.mock_response
        self.client = SonarQube(host="http://localhost:9000", token="my_token")

    def tearDown(self):
        self.patcher.stop()

    def test_get_sources_index(self):
        self.client.sources.get_sources_index(resource="my-resource")

        self.mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/sources/index",
            params={"resource": "my-resource"},
        )

    def test_get_issue_snippets(self):
        self.client.sources.get_issue_snippets(issueKey="my-issue-key")

        self.mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/sources/issue_snippets",
            params={"issueKey": "my-issue-key"},
        )

    def test_get_sources_lines(self):
        self.client.sources.get_sources_lines(key="my-key")

        self.mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/sources/lines",
            params={"key": "my-key"},
        )

    def test_get_sources_raw(self):
        self.client.sources.get_sources_raw(key="my-key")

        self.mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/sources/raw",
            params={"key": "my-key"},
        )

    def test_get_sources_scm(self):
        self.client.sources.get_sources_scm(key="my-key")

        self.mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/sources/scm",
            params={"key": "my-key"},
        )

    def test_get_sources_show(self):
        self.client.sources.get_sources_show(key="my-key")

        self.mock_session.get.assert_called_once_with(
            "http://localhost:9000/api/sources/show",
            params={"key": "my-key"},
        )
