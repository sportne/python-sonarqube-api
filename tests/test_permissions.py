import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubePermissions(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_add_group_to_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.add_group_to_permission_template(
                template_name="my-template", group_name="my-group", permission="scan"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/add_group_to_template",
                params={
                    "templateName": "my-template",
                    "groupName": "my-group",
                    "permission": "scan",
                },
            )

    def test_add_project_creator_to_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.add_project_creator_to_permission_template(
                template_name="my-template", permission="scan"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/add_project_creator_to_template",
                params={"templateName": "my-template", "permission": "scan"},
            )

    def test_add_user_to_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.add_user_to_permission_template(
                template_name="my-template", login="my-user", permission="scan"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/add_user_to_template",
                params={
                    "templateName": "my-template",
                    "login": "my-user",
                    "permission": "scan",
                },
            )

    def test_apply_permission_template_to_project(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.apply_permission_template_to_project(
                template_name="my-template", project_key="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/apply_template",
                params={"templateName": "my-template", "projectKey": "my-project"},
            )

    def test_bulk_apply_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.bulk_apply_permission_template(
                template_name="my-template", projects="my-project-1,my-project-2"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/bulk_apply_template",
                params={
                    "templateName": "my-template",
                    "projects": "my-project-1,my-project-2",
                },
            )

    def test_create_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.create_permission_template(
                name="my-template", description="my-description"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/create_template",
                params={"name": "my-template", "description": "my-description"},
            )

    def test_delete_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.delete_permission_template(
                template_name="my-template"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/delete_template",
                params={"templateName": "my-template"},
            )

    def test_get_permission_groups(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.permissions.get_permission_groups(q="my-group")
            mock_get.assert_called_with(
                "http://localhost:9000/api/permissions/groups", params={"q": "my-group"}
            )

    def test_remove_group_from_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.remove_group_from_permission_template(
                template_name="my-template", group_name="my-group", permission="scan"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/remove_group_from_template",
                params={
                    "templateName": "my-template",
                    "groupName": "my-group",
                    "permission": "scan",
                },
            )

    def test_remove_project_creator_from_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.remove_project_creator_from_permission_template(
                template_name="my-template", permission="scan"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/remove_project_creator_from_template",
                params={"templateName": "my-template", "permission": "scan"},
            )

    def test_remove_user_from_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.remove_user_from_permission_template(
                template_name="my-template", login="my-user", permission="scan"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/remove_user_from_template",
                params={
                    "templateName": "my-template",
                    "login": "my-user",
                    "permission": "scan",
                },
            )

    def test_search_permission_templates(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.permissions.search_permission_templates(q="my-template")
            mock_get.assert_called_with(
                "http://localhost:9000/api/permissions/search_templates",
                params={"q": "my-template"},
            )

    def test_set_default_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.set_default_permission_template(
                template_name="my-template"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/set_default_template",
                params={"templateName": "my-template"},
            )

    def test_get_permission_template_groups(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.permissions.get_permission_template_groups(
                template_name="my-template", q="my-group"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/permissions/template_groups",
                params={"templateName": "my-template", "q": "my-group"},
            )

    def test_get_permission_template_users(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.permissions.get_permission_template_users(
                template_name="my-template", q="my-user"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/permissions/template_users",
                params={"templateName": "my-template", "q": "my-user"},
            )

    def test_update_permission_template(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.permissions.update_permission_template(
                id="my-template-id", name="new-name"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/permissions/update_template",
                params={"id": "my-template-id", "name": "new-name"},
            )

    def test_get_permission_users(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.permissions.get_permission_users(q="my-user")
            mock_get.assert_called_with(
                "http://localhost:9000/api/permissions/users", params={"q": "my-user"}
            )


if __name__ == "__main__":
    unittest.main()
