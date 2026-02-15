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

    def create_user(
        self, login, name, password=None, email=None, scmAccounts=None, local=None
    ):
        """
        Create a user.
        If a deactivated user account exists with the given login, it will be reactivated.
        Requires Administer System permission.
        :param login: User login (min 2 chars, max 255 chars)
        :param name: User name (max 200 chars)
        :param password: User password (only for local users)
        :param email: User email
        :param scmAccounts: Comma-separated list of SCM accounts
        :param local: Specify if the user should be authenticated from SonarQube server or from an external authentication system
        """
        params = {"login": login, "name": name}
        if password:
            params["password"] = password
        if email:
            params["email"] = email
        if scmAccounts:
            params["scmAccounts"] = scmAccounts
        if local is not None:
            params["local"] = local
        return self.client._post("api/users/create", params=params)

    def deactivate_user(self, login, anonymize=None):
        """
        Deactivate a user.
        Requires Administer System permission.
        :param login: User login
        :param anonymize: Anonymize user in addition to deactivating it
        """
        params = {"login": login}
        if anonymize is not None:
            params["anonymize"] = anonymize
        return self.client._post("api/users/deactivate", params=params)

    def get_user_groups(self, login, q=None, selected=None):
        """
        Lists the groups a user belongs to.
        Requires Administer System permission.
        :param login: User login
        :param q: Limit search to group names that contain the supplied string
        :param selected: Depending on the value, show only selected, deselected or all items
        """
        params = {"login": login}
        if q:
            params["q"] = q
        if selected:
            params["selected"] = selected
        return self.client._get("api/users/groups", params=params)

    def search_users(
        self,
        q=None,
        deactivated=None,
        managed=None,
        lastConnectedAfter=None,
        lastConnectedBefore=None,
        sonarLintLastConnectionDateFrom=None,
        sonarLintLastConnectionDateTo=None,
    ):
        """
        Get a list of active users.
        :param q: Filter on login, name and email
        :param deactivated: Return deactivated users instead of active users
        :param managed: Return managed or non-managed users
        :param lastConnectedAfter: Filter users by last connection date (>= this date, format: yyyy-MM-dd)
        :param lastConnectedBefore: Filter users by last connection date (<= this date, format: yyyy-MM-dd)
        :param sonarLintLastConnectionDateFrom: Filter users by SonarLint last connection date (>= this date)
        :param sonarLintLastConnectionDateTo: Filter users by SonarLint last connection date (<= this date)
        """
        params = {}
        if q:
            params["q"] = q
        if deactivated is not None:
            params["deactivated"] = deactivated
        if managed is not None:
            params["managed"] = managed
        if lastConnectedAfter:
            params["lastConnectedAfter"] = lastConnectedAfter
        if lastConnectedBefore:
            params["lastConnectedBefore"] = lastConnectedBefore
        if sonarLintLastConnectionDateFrom:
            params["sonarLintLastConnectionDateFrom"] = sonarLintLastConnectionDateFrom
        if sonarLintLastConnectionDateTo:
            params["sonarLintLastConnectionDateTo"] = sonarLintLastConnectionDateTo
        return self.client._get("api/users/search", params=params)

    def update_user(self, login, name=None, email=None, scmAccounts=None):
        """
        Update a user.
        Requires Administer System permission.
        :param login: User login
        :param name: User name
        :param email: User email
        :param scmAccounts: Comma-separated list of SCM accounts
        """
        params = {"login": login}
        if name:
            params["name"] = name
        if email:
            params["email"] = email
        if scmAccounts:
            params["scmAccounts"] = scmAccounts
        return self.client._post("api/users/update", params=params)
