import unittest
from unittest.mock import patch, mock_open
from src.sonarqube import SonarQube


class TestSonarQubeQualityProfiles(unittest.TestCase):

    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_activate_rule_in_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.activate_rule_in_quality_profile(
                key="my-profile", rule="my-rule"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/activate_rule",
                params={"key": "my-profile", "rule": "my-rule"},
            )

    def test_activate_rules_in_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.activate_rules_in_quality_profile(
                key="my-profile", tags="security"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/activate_rules",
                params={"key": "my-profile", "tags": "security"},
            )

    def test_add_group_to_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.add_group_to_quality_profile(
                key="my-profile", groupName="my-group"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/add_group",
                params={"key": "my-profile", "groupName": "my-group"},
            )

    def test_add_project_to_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.add_project_to_quality_profile(
                key="my-profile", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/add_project",
                params={"key": "my-profile", "project": "my-project"},
            )

    def test_add_user_to_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.add_user_to_quality_profile(key="my-profile", userName="my-user")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/add_user",
                params={"key": "my-profile", "userName": "my-user"},
            )

    def test_backup_quality_profile(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.backup_quality_profile(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/backup",
                params={"key": "my-profile"},
            )

    def test_change_quality_profile_parent(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.change_quality_profile_parent(
                key="my-profile", parentKey="parent-profile"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/change_parent",
                params={"key": "my-profile", "parentKey": "parent-profile"},
            )

    def test_get_quality_profile_changelog(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_quality_profile_changelog(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/changelog",
                params={"key": "my-profile"},
            )

    def test_compare_quality_profiles(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.compare_quality_profiles(fromKey="profile1", toKey="profile2")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/compare",
                params={"fromKey": "profile1", "toKey": "profile2"},
            )

    def test_copy_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.copy_quality_profile(fromKey="profile1", toName="profile2")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/copy",
                params={"fromKey": "profile1", "toName": "profile2"},
            )

    def test_create_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.create_quality_profile(name="my-profile", language="java")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/create",
                params={"name": "my-profile", "language": "java"},
            )

    def test_deactivate_rule_from_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.deactivate_rule_from_quality_profile(
                key="my-profile", rule="my-rule"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/deactivate_rule",
                params={"key": "my-profile", "rule": "my-rule"},
            )

    def test_deactivate_rules_from_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.deactivate_rules_from_quality_profile(
                key="my-profile", tags="security"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/deactivate_rules",
                params={"key": "my-profile", "tags": "security"},
            )

    def test_delete_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.delete_quality_profile(key="my-profile")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/delete",
                params={"key": "my-profile"},
            )

    def test_get_quality_profile_inheritance(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.get_quality_profile_inheritance(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/inheritance",
                params={"key": "my-profile"},
            )

    def test_list_quality_profile_projects(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.list_quality_profile_projects(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/projects",
                params={"key": "my-profile"},
            )

    def test_remove_group_from_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.remove_group_from_quality_profile(
                key="my-profile", groupName="my-group"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/remove_group",
                params={"key": "my-profile", "groupName": "my-group"},
            )

    def test_remove_project_from_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.remove_project_from_quality_profile(
                key="my-profile", project="my-project"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/remove_project",
                params={"key": "my-profile", "project": "my-project"},
            )

    def test_remove_user_from_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.remove_user_from_quality_profile(
                key="my-profile", userName="my-user"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/remove_user",
                params={"key": "my-profile", "userName": "my-user"},
            )

    def test_rename_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.rename_quality_profile(key="my-profile", name="new-name")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/rename",
                params={"key": "my-profile", "name": "new-name"},
            )

    def test_restore_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            with patch("builtins.open", mock_open(read_data=b"test")) as mock_file:
                self.sonar.restore_quality_profile(backup="my-backup.xml")
                mock_file.assert_called_with("my-backup.xml", "rb")
                mock_post.assert_called_with(
                    "http://localhost:9000/api/qualityprofiles/restore",
                    params={},
                    files={"backup": mock_file.return_value},
                )

    def test_search_quality_profiles(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_quality_profiles(qualityProfile="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/search",
                params={"qualityProfile": "my-profile"},
            )

    def test_search_quality_profile_groups(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_quality_profile_groups(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/search_groups",
                params={"key": "my-profile"},
            )

    def test_search_quality_profile_users(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.search_quality_profile_users(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/search_users",
                params={"key": "my-profile"},
            )

    def test_set_default_quality_profile(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.set_default_quality_profile(key="my-profile")
            mock_post.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/set_default",
                params={"key": "my-profile"},
            )

    def test_show_quality_profile(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.show_quality_profile(key="my-profile")
            mock_get.assert_called_with(
                "http://localhost:9000/api/qualityprofiles/show",
                params={"key": "my-profile"},
            )
