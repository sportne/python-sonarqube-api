class SonarQubePermissions:
    def __init__(self, client):
        self.client = client

    def add_group_to_permission_template(self, template_name, group_name, permission):
        """
        Add a group to a permission template.
        :param template_name: Template name
        :param group_name: Group name
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "groupName": group_name,
            "permission": permission,
        }
        return self.client._post("api/permissions/add_group_to_template", params=params)

    def add_project_creator_to_permission_template(self, template_name, permission):
        """
        Add a project creator to a permission template.
        :param template_name: Template name
        :param permission: Permission
        """
        params = {"templateName": template_name, "permission": permission}
        return self.client._post(
            "api/permissions/add_project_creator_to_template", params=params
        )

    def add_user_to_permission_template(self, template_name, login, permission):
        """
        Add a user to a permission template.
        :param template_name: Template name
        :param login: User login
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "login": login,
            "permission": permission,
        }
        return self.client._post("api/permissions/add_user_to_template", params=params)

    def apply_permission_template_to_project(self, template_name, project_key):
        """
        Apply a permission template to one project.
        :param template_name: Template name
        :param project_key: Project key
        """
        params = {"templateName": template_name, "projectKey": project_key}
        return self.client._post("api/permissions/apply_template", params=params)

    def bulk_apply_permission_template(self, template_name, **kwargs):
        """
        Apply a permission template to several components.
        :param template_name: Template name
        :param kwargs: Additional parameters
        """
        params = {"templateName": template_name}
        params.update(kwargs)
        return self.client._post("api/permissions/bulk_apply_template", params=params)

    def create_permission_template(self, name, **kwargs):
        """
        Create a permission template.
        :param name: Template name
        :param kwargs: Additional parameters
        """
        params = {"name": name}
        params.update(kwargs)
        return self.client._post("api/permissions/create_template", params=params)

    def delete_permission_template(self, template_name):
        """
        Delete a permission template.
        :param template_name: Template name
        """
        params = {"templateName": template_name}
        return self.client._post("api/permissions/delete_template", params=params)

    def get_permission_groups(self, **kwargs):
        """
        Lists the groups with their permissions.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/permissions/groups", params=kwargs)

    def remove_group_from_permission_template(
        self, template_name, group_name, permission
    ):
        """
        Remove a group from a permission template.
        :param template_name: Template name
        :param group_name: Group name
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "groupName": group_name,
            "permission": permission,
        }
        return self.client._post(
            "api/permissions/remove_group_from_template", params=params
        )

    def remove_project_creator_from_permission_template(
        self, template_name, permission
    ):
        """
        Remove a project creator from a permission template.
        :param template_name: Template name
        :param permission: Permission
        """
        params = {"templateName": template_name, "permission": permission}
        return self.client._post(
            "api/permissions/remove_project_creator_from_template", params=params
        )

    def remove_user_from_permission_template(self, template_name, login, permission):
        """
        Remove a user from a permission template.
        :param template_name: Template name
        :param login: User login
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "login": login,
            "permission": permission,
        }
        return self.client._post(
            "api/permissions/remove_user_from_template", params=params
        )

    def search_permission_templates(self, q=None):
        """
        List permission templates.
        :param q: Query to filter templates
        """
        params = {}
        if q:
            params["q"] = q
        return self.client._get("api/permissions/search_templates", params=params)

    def set_default_permission_template(self, template_name):
        """
        Set a permission template as default.
        :param template_name: Template name
        """
        params = {"templateName": template_name}
        return self.client._post("api/permissions/set_default_template", params=params)

    def get_permission_template_groups(self, template_name, **kwargs):
        """
        Lists the groups with their permission on the chosen template.
        :param template_name: Template name
        :param kwargs: Additional parameters
        """
        params = {"templateName": template_name}
        params.update(kwargs)
        return self.client._get("api/permissions/template_groups", params=params)

    def get_permission_template_users(self, template_name, **kwargs):
        """
        Lists the users with their permission on the chosen template.
        :param template_name: Template name
        :param kwargs: Additional parameters
        """
        params = {"templateName": template_name}
        params.update(kwargs)
        return self.client._get("api/permissions/template_users", params=params)

    def update_permission_template(self, id, **kwargs):
        """
        Update a permission template.
        :param id: Template ID
        :param kwargs: Additional parameters
        """
        params = {"id": id}
        params.update(kwargs)
        return self.client._post("api/permissions/update_template", params=params)

    def get_permission_users(self, **kwargs):
        """
        Lists the users with their permissions.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/permissions/users", params=kwargs)
