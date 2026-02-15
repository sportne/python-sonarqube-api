import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeViews(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_add_application_to_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.add_application_to_portfolio(
                application="my-app", portfolio="my-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/add_application",
                params={"application": "my-app", "portfolio": "my-portfolio"},
            )

    def test_add_application_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.add_application_branch(
                application="my-app", branch="my-branch", key="my-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/add_application_branch",
                params={
                    "application": "my-app",
                    "branch": "my-branch",
                    "key": "my-portfolio",
                },
            )

    def test_add_portfolio_to_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.add_portfolio_to_portfolio(
                portfolio="my-portfolio", reference="my-ref-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/add_portfolio",
                params={"portfolio": "my-portfolio", "reference": "my-ref-portfolio"},
            )

    def test_add_project_to_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.add_project_to_portfolio(
                key="my-portfolio", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/add_project",
                params={"key": "my-portfolio", "project": "my-project"},
            )

    def test_add_project_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.add_project_branch(
                branch="my-branch", key="my-portfolio", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/add_project_branch",
                params={
                    "branch": "my-branch",
                    "key": "my-portfolio",
                    "project": "my-project",
                },
            )

    def test_list_applications_for_portfolio(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.list_applications_for_portfolio(portfolio="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/applications",
                params={"portfolio": "my-portfolio"},
            )

    def test_create_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.create_portfolio(name="my-portfolio")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/create",
                params={"name": "my-portfolio"},
            )

    def test_delete_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.delete_portfolio(key="my-portfolio")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/delete",
                params={"key": "my-portfolio"},
            )

    def test_list_portfolios(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.list_portfolios()
            mock_get.assert_called_with("http://localhost:9000/api/views/list")

    def test_move_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.move_portfolio(
                destination="dest-portfolio", key="my-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/move",
                params={"destination": "dest-portfolio", "key": "my-portfolio"},
            )

    def test_list_move_options(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.list_move_options(key="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/move_options",
                params={"key": "my-portfolio"},
            )

    def test_list_portfolios_for_portfolio(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.list_portfolios_for_portfolio(portfolio="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/portfolios",
                params={"portfolio": "my-portfolio"},
            )

    def test_list_projects_in_portfolio(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.list_projects_in_portfolio(key="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/projects",
                params={"key": "my-portfolio"},
            )

    def test_list_projects_status_in_portfolio(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.list_projects_status_in_portfolio(portfolio="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/projects_status",
                params={"portfolio": "my-portfolio"},
            )

    def test_refresh_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.refresh_portfolio(key="my-portfolio")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/refresh",
                params={"key": "my-portfolio"},
            )

    def test_remove_application_from_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.remove_application_from_portfolio(
                application="my-app", portfolio="my-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/remove_application",
                params={"application": "my-app", "portfolio": "my-portfolio"},
            )

    def test_remove_application_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.remove_application_branch(
                application="my-app", branch="my-branch", key="my-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/remove_application_branch",
                params={
                    "application": "my-app",
                    "branch": "my-branch",
                    "key": "my-portfolio",
                },
            )

    def test_remove_portfolio_from_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.remove_portfolio_from_portfolio(
                portfolio="my-portfolio", reference="my-ref-portfolio"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/remove_portfolio",
                params={"portfolio": "my-portfolio", "reference": "my-ref-portfolio"},
            )

    def test_remove_project_from_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.remove_project_from_portfolio(
                key="my-portfolio", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/remove_project",
                params={"key": "my-portfolio", "project": "my-project"},
            )

    def test_remove_project_branch(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.remove_project_branch(
                branch="my-branch", key="my-portfolio", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/remove_project_branch",
                params={
                    "branch": "my-branch",
                    "key": "my-portfolio",
                    "project": "my-project",
                },
            )

    def test_search_portfolios(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.search_portfolios(q="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/search",
                params={"q": "my-portfolio"},
            )

    def test_set_manual_mode(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.set_manual_mode(portfolio="my-portfolio")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/set_manual_mode",
                params={"portfolio": "my-portfolio"},
            )

    def test_set_none_mode(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.set_none_mode(portfolio="my-portfolio")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/set_none_mode",
                params={"portfolio": "my-portfolio"},
            )

    def test_set_regexp_mode(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.set_regexp_mode(
                portfolio="my-portfolio", regexp="my-regexp"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/set_regexp_mode",
                params={"portfolio": "my-portfolio", "regexp": "my-regexp"},
            )

    def test_set_remaining_projects_mode(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.set_remaining_projects_mode(portfolio="my-portfolio")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/set_remaining_projects_mode",
                params={"portfolio": "my-portfolio"},
            )

    def test_set_tags_mode(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.set_tags_mode(portfolio="my-portfolio", tags="my-tags")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/set_tags_mode",
                params={"portfolio": "my-portfolio", "tags": "my-tags"},
            )

    def test_show_portfolio(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.views.show_portfolio(key="my-portfolio")
            mock_get.assert_called_with(
                "http://localhost:9000/api/views/show",
                params={"key": "my-portfolio"},
            )

    def test_update_portfolio(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.views.update_portfolio(key="my-portfolio", name="new-name")
            mock_post.assert_called_with(
                "http://localhost:9000/api/views/update",
                params={"key": "my-portfolio", "name": "new-name"},
            )
