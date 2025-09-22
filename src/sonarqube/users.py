class SonarQubeUsers:
    def __init__(self, client):
        self.client = client

    def change_password(self, login, password, previousPassword=None):
        """
        Update a user's password.
        :param login: User login
        :param password: New password
        :param previousPassword: Previous password
        """
        params = {"login": login, "password": password}
        if previousPassword:
            params["previousPassword"] = previousPassword
        return self.client._post("api/users/change_password", params=params)

    def get_current_user(self):
        """
        Get the details of the current authenticated user.
        """
        return self.client._get("api/users/current")

    def dismiss_notice(self, notice=None):
        """
        Dismiss a notice for the current user.
        :param notice: Notice key to dismiss
        """
        params = {}
        if notice:
            params["notice"] = notice
        return self.client._post("api/users/dismiss_notice", params=params)

    def get_identity_providers(self):
        """
        List the external identity providers.
        """
        return self.client._get("api/users/identity_providers")

    def set_ai_tool_usage(self, project):
        """
        Set AI tool usage.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._post("api/users/set_ai_tool_usage", params=params)

    def set_homepage(self, type, branch=None, component=None):
        """
        Set homepage of current user.
        :param type: Type of the requested page
        :param branch: Branch key
        :param component: Project key
        """
        params = {"type": type}
        if branch:
            params["branch"] = branch
        if component:
            params["component"] = component
        return self.client._post("api/users/set_homepage", params=params)
