import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeQualityGates(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_add_group_to_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.add_group_to_quality_gate(
                gateId="my-gate", groupId="my-group"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/add_group",
                params={"gateId": "my-gate", "groupId": "my-group"},
            )

    def test_add_user_to_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.add_user_to_quality_gate(
                gateId="my-gate", userId="my-user"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/add_user",
                params={"gateId": "my-gate", "userId": "my-user"},
            )

    def test_get_application_quality_gate_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.get_application_quality_gate_status(
                application="my-app"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/application_status",
                params={"application": "my-app"},
            )

    def test_copy_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.copy_quality_gate(
                sourceName="my-gate", destName="new-gate"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/copy",
                params={"sourceName": "my-gate", "name": "new-gate"},
            )

    def test_create_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.create_quality_gate(name="my-gate")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/create",
                params={"name": "my-gate"},
            )

    def test_create_quality_gate_condition(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.create_quality_gate_condition(
                gateName="my-gate", metric="coverage", op="LT", error="80"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/create_condition",
                params={
                    "gateName": "my-gate",
                    "metric": "coverage",
                    "op": "LT",
                    "error": "80",
                },
            )

    def test_delete_quality_gate_condition(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.delete_quality_gate_condition(id="my-condition")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/delete_condition",
                params={"id": "my-condition"},
            )

    def test_deselect_project_from_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.deselect_project_from_quality_gate(
                projectKey="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/deselect",
                params={"projectKey": "my-project"},
            )

    def test_destroy_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.destroy_quality_gate(name="my-gate")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/destroy",
                params={"name": "my-gate"},
            )

    def test_get_quality_gate_by_project(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.get_quality_gate_by_project(
                projectKey="my-project"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/get_by_project",
                params={"projectKey": "my-project"},
            )

    def test_list_quality_gates(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.list_quality_gates()
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/list", params={}
            )

    def test_get_project_quality_gate_status(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.get_project_quality_gate_status(
                projectKey="my-project"
            )
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/project_status",
                params={"projectKey": "my-project"},
            )

    def test_remove_group_from_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.remove_group_from_quality_gate(
                gateId="my-gate", groupId="my-group"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/remove_group",
                params={"gateId": "my-gate", "groupId": "my-group"},
            )

    def test_remove_user_from_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.remove_user_from_quality_gate(
                gateId="my-gate", userId="my-user"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/remove_user",
                params={"gateId": "my-gate", "userId": "my-user"},
            )

    def test_rename_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.rename_quality_gate(
                currentName="my-gate", newName="new-gate"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/rename",
                params={"id": "my-gate", "name": "new-gate"},
            )

    def test_search_quality_gates(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.search_quality_gates(gateId="my-gate")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/search",
                params={"gateId": "my-gate"},
            )

    def test_search_quality_gate_groups(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.search_quality_gate_groups(gateId="my-gate")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/search_groups",
                params={"gateId": "my-gate"},
            )

    def test_search_quality_gate_users(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.search_quality_gate_users(gateId="my-gate")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/search_users",
                params={"gateId": "my-gate"},
            )

    def test_select_project_for_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.select_project_for_quality_gate(
                projectKey="my-project", gateId="my-gate"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/select",
                params={"projectKey": "my-project", "gateId": "my-gate"},
            )

    def test_set_quality_gate_ai_code_assurance(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.set_quality_gate_ai_code_assurance(
                gateId="my-gate", isAssured=True
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/set_ai_code_assurance",
                params={"gateId": "my-gate", "isAssured": True},
            )

    def test_set_default_quality_gate(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.set_default_quality_gate(name="my-gate")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/set_as_default",
                params={"name": "my-gate"},
            )

    def test_show_quality_gate(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.quality_gates.show_quality_gate(name="my-gate")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualitygates/show",
                params={"name": "my-gate"},
            )

    def test_update_quality_gate_condition(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.quality_gates.update_quality_gate_condition(
                id="my-condition", metric="coverage", op="LT", error="90"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualitygates/update_condition",
                params={
                    "id": "my-condition",
                    "metric": "coverage",
                    "op": "LT",
                    "error": "90",
                },
            )
