import unittest
from unittest.mock import MagicMock

from src.sonarqube.authorizations_v2 import SonarQubeAuthorizationsV2


class TestSonarQubeAuthorizationsV2(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock()
        self.auth = SonarQubeAuthorizationsV2(self.client)

    def test_add_group_member(self):
        self.auth.add_group_member(userId="123", groupId="456")
        self.client._post.assert_called_once_with(
            "api/v2/authorizations/group-memberships",
            json={"userId": "123", "groupId": "456"},
        )

    def test_search_group_members(self):
        self.auth.search_group_members(q="test")
        self.client._get.assert_called_once_with(
            "api/v2/authorizations/group-memberships",
            params={"q": "test"},
        )

    def test_remove_group_member(self):
        self.auth.remove_group_member("123")
        self.client._delete.assert_called_once_with(
            "api/v2/authorizations/group-memberships/123"
        )

    def test_create_group(self):
        self.auth.create_group("test-group", description="A test group")
        self.client._post.assert_called_once_with(
            "api/v2/authorizations/groups",
            json={"name": "test-group", "description": "A test group"},
        )

    def test_search_groups(self):
        self.auth.search_groups(q="test")
        self.client._get.assert_called_once_with(
            "api/v2/authorizations/groups",
            params={"q": "test"},
        )

    def test_get_group(self):
        self.auth.get_group("123")
        self.client._get.assert_called_once_with("api/v2/authorizations/groups/123")

    def test_update_group(self):
        self.auth.update_group("123", name="new-name")
        self.client._patch.assert_called_once_with(
            "api/v2/authorizations/groups/123",
            json={"name": "new-name"},
        )

    def test_delete_group(self):
        self.auth.delete_group("123")
        self.client._delete.assert_called_once_with("api/v2/authorizations/groups/123")


if __name__ == "__main__":
    unittest.main()
