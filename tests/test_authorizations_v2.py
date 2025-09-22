import unittest
from unittest.mock import patch
from src.sonarqube import SonarQube


class TestSonarQubeAuthorizationsV2(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_add_group_member(self):
        with patch.object(self.sonar, "_post") as mock_post:
            self.sonar.authorizations_v2.add_group_member(
                userId="my-user-id", groupId="my-group-id"
            )
            mock_post.assert_called_with(
                "/api/v2/authorizations/group-memberships",
                json={"userId": "my-user-id", "groupId": "my-group-id"},
            )

    def test_search_group_members(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.authorizations_v2.search_group_members(userId="my-user-id")
            mock_get.assert_called_with(
                "/api/v2/authorizations/group-memberships",
                params={"userId": "my-user-id"},
            )

    def test_remove_group_member(self):
        with patch.object(self.sonar, "_delete") as mock_delete:
            self.sonar.authorizations_v2.remove_group_member(member_id="my-member-id")
            mock_delete.assert_called_with(
                "/api/v2/authorizations/group-memberships/my-member-id"
            )

    def test_create_group(self):
        with patch.object(self.sonar, "_post") as mock_post:
            self.sonar.authorizations_v2.create_group(name="my-group-name")
            mock_post.assert_called_with(
                "/api/v2/authorizations/groups",
                json={"name": "my-group-name"},
            )

    def test_search_groups(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.authorizations_v2.search_groups(q="my-group")
            mock_get.assert_called_with(
                "/api/v2/authorizations/groups", params={"q": "my-group"}
            )

    def test_get_group(self):
        with patch.object(self.sonar, "_get") as mock_get:
            self.sonar.authorizations_v2.get_group(group_id="my-group-id")
            mock_get.assert_called_with("/api/v2/authorizations/groups/my-group-id")

    def test_update_group(self):
        with patch.object(self.sonar, "_patch") as mock_patch:
            self.sonar.authorizations_v2.update_group(
                group_id="my-group-id", name="new-name"
            )
            mock_patch.assert_called_with(
                "/api/v2/authorizations/groups/my-group-id",
                json={"name": "new-name"},
            )

    def test_delete_group(self):
        with patch.object(self.sonar, "_delete") as mock_delete:
            self.sonar.authorizations_v2.delete_group(group_id="my-group-id")
            mock_delete.assert_called_with("/api/v2/authorizations/groups/my-group-id")
