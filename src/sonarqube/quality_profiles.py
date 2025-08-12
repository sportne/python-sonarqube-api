class SonarQubeQualityProfiles:
    def __init__(self, client):
        self.client = client

    def activate_rule_in_quality_profile(
        self, key, rule, reset=None, severity=None, params=None
    ):
        """
        Activate a rule on a Quality Profile.
        :param key: Quality Profile key
        :param rule: Rule key
        :param reset: Reset the severity and parameters of the rule
        :param severity: Severity
        :param params: Parameters
        """
        request_params = {"key": key, "rule": rule}
        if reset:
            request_params["reset"] = reset
        if severity:
            request_params["severity"] = severity
        if params:
            request_params["params"] = params
        return self.client._post(
            "api/qualityprofiles/activate_rule", params=request_params
        )

    def activate_rules_in_quality_profile(self, key, **kwargs):
        """
        Bulk-activate rules on one quality profile.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._post("api/qualityprofiles/activate_rules", params=params)

    def add_group_to_quality_profile(self, key, groupName, organization=None):
        """
        Allow a group to edit a Quality Profile.
        :param key: Quality Profile key
        :param groupName: Group name
        :param organization: Organization key
        """
        params = {"key": key, "groupName": groupName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/add_group", params=params)

    def add_project_to_quality_profile(self, key, project, organization=None):
        """
        Associate a project with a quality profile.
        :param key: Quality Profile key
        :param project: Project key
        :param organization: Organization key
        """
        params = {"key": key, "project": project}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/add_project", params=params)

    def add_user_to_quality_profile(self, key, userName, organization=None):
        """
        Allow a user to edit a Quality Profile.
        :param key: Quality Profile key
        :param userName: User login
        :param organization: Organization key
        """
        params = {"key": key, "userName": userName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/add_user", params=params)

    def backup_quality_profile(self, key):
        """
        Backup a quality profile in XML form.
        :param key: Quality Profile key
        """
        params = {"key": key}
        return self.client._get("api/qualityprofiles/backup", params=params)

    def change_quality_profile_parent(self, key, parentKey, organization=None):
        """
        Change a quality profile's parent.
        :param key: Quality Profile key
        :param parentKey: Parent Quality Profile key
        :param organization: Organization key
        """
        params = {"key": key, "parentKey": parentKey}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/change_parent", params=params)

    def get_quality_profile_changelog(self, key, **kwargs):
        """
        Get the history of changes on a quality profile.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._get("api/qualityprofiles/changelog", params=params)

    def compare_quality_profiles(self, fromKey, toKey, organization=None):
        """
        Compare two quality profiles.
        :param fromKey: 'From' Quality Profile key
        :param toKey: 'To' Quality Profile key
        :param organization: Organization key
        """
        params = {"fromKey": fromKey, "toKey": toKey}
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualityprofiles/compare", params=params)

    def copy_quality_profile(self, fromKey, toName, organization=None):
        """
        Copy a quality profile.
        :param fromKey: 'From' Quality Profile key
        :param toName: 'To' Quality Profile name
        :param organization: Organization key
        """
        params = {"fromKey": fromKey, "toName": toName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/copy", params=params)

    def create_quality_profile(self, name, language, organization=None):
        """
        Create a quality profile.
        :param name: Quality Profile name
        :param language: Language
        :param organization: Organization key
        """
        params = {"name": name, "language": language}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/create", params=params)

    def deactivate_rule_from_quality_profile(self, key, rule, organization=None):
        """
        Deactivate a rule on a quality profile.
        :param key: Quality Profile key
        :param rule: Rule key
        :param organization: Organization key
        """
        params = {"key": key, "rule": rule}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/deactivate_rule", params=params)

    def deactivate_rules_from_quality_profile(self, key, **kwargs):
        """
        Bulk deactivate rules on Quality profiles.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._post("api/qualityprofiles/deactivate_rules", params=params)

    def delete_quality_profile(self, key, organization=None):
        """
        Delete a quality profile.
        :param key: Quality Profile key
        :param organization: Organization key
        """
        params = {"key": key}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/delete", params=params)

    def get_quality_profile_inheritance(self, key, organization=None):
        """
        Show a quality profile's ancestors and children.
        :param key: Quality Profile key
        :param organization: Organization key
        """
        params = {"key": key}
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualityprofiles/inheritance", params=params)

    def list_quality_profile_projects(self, key, **kwargs):
        """
        List projects with their association status regarding a quality profile.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._get("api/qualityprofiles/projects", params=params)

    def remove_group_from_quality_profile(self, key, groupName, organization=None):
        """
        Remove the ability from a group to edit a Quality Profile.
        :param key: Quality Profile key
        :param groupName: Group name
        :param organization: Organization key
        """
        params = {"key": key, "groupName": groupName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/remove_group", params=params)

    def remove_project_from_quality_profile(self, key, project, organization=None):
        """
        Remove a project's association with a quality profile.
        :param key: Quality Profile key
        :param project: Project key
        :param organization: Organization key
        """
        params = {"key": key, "project": project}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/remove_project", params=params)

    def remove_user_from_quality_profile(self, key, userName, organization=None):
        """
        Remove the ability from a user to edit a Quality Profile.
        :param key: Quality Profile key
        :param userName: User login
        :param organization: Organization key
        """
        params = {"key": key, "userName": userName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/remove_user", params=params)

    def rename_quality_profile(self, key, name, organization=None):
        """
        Rename a quality profile.
        :param key: Quality Profile key
        :param name: New name
        :param organization: Organization key
        """
        params = {"key": key, "name": name}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/rename", params=params)

    def restore_quality_profile(self, backup, organization=None):
        """
        Restore a quality profile using an XML file.
        :param backup: Backup file
        :param organization: Organization key
        """
        params = {}
        if organization:
            params["organization"] = organization
        with open(backup, "rb") as f:
            files = {"backup": f}
            return self.client._post(
                "api/qualityprofiles/restore", params=params, files=files
            )

    def search_quality_profiles(self, **kwargs):
        """
        Search quality profiles.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/qualityprofiles/search", params=kwargs)

    def search_quality_profile_groups(self, key, **kwargs):
        """
        List the groups that are allowed to edit a Quality Profile.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._get("api/qualityprofiles/search_groups", params=params)

    def search_quality_profile_users(self, key, **kwargs):
        """
        List the users that are allowed to edit a Quality Profile.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._get("api/qualityprofiles/search_users", params=params)

    def set_default_quality_profile(self, key, organization=None):
        """
        Select the default profile for a given language.
        :param key: Quality Profile key
        :param organization: Organization key
        """
        params = {"key": key}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualityprofiles/set_default", params=params)

    def show_quality_profile(self, key, **kwargs):
        """
        Show a quality profile.
        :param key: Quality Profile key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._get("api/qualityprofiles/show", params=params)
