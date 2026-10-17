class SonarQubeAlmSettings:
    def __init__(self, client):
        self.client = client

    def count_binding(self, almSetting):
        """
        Count projects bound to a DevOps Platform setting.
        Requires 'Administer System' permission.
        :param almSetting: DevOps Platform setting key
        """
        params = {"almSetting": almSetting}
        return self.client._get("api/alm_settings/count_binding", params=params)

    def create_azure(self, key, personalAccessToken, url):
        """
        Create an Azure DevOps instance setting.
        Requires 'Administer System' permission.
        :param key: Unique DevOps Platform setting key
        :param personalAccessToken: Azure DevOps personal access token
        :param url: Absolute HTTP(S) Azure API URL
        """
        params = {"key": key, "personalAccessToken": personalAccessToken, "url": url}
        return self.client._post("api/alm_settings/create_azure", params=params)

    def create_bitbucket(self, key, url, personalAccessToken):
        """
        Create a Bitbucket Server instance setting.
        Requires 'Administer System' permission.
        :param key: Unique DevOps Platform setting key
        :param url: Bitbucket Server API URL
        :param personalAccessToken: Bitbucket personal access token
        """
        params = {"key": key, "url": url, "personalAccessToken": personalAccessToken}
        return self.client._post("api/alm_settings/create_bitbucket", params=params)

    def create_bitbucketcloud(self, key, workspace, clientId, clientSecret):
        """
        Create a Bitbucket Cloud instance setting.
        Requires 'Administer System' permission.
        :param key: Unique DevOps Platform setting key
        :param workspace: Bitbucket Cloud workspace ID
        :param clientId: Bitbucket Cloud OAuth client ID
        :param clientSecret: Bitbucket Cloud OAuth client secret
        """
        params = {
            "key": key,
            "workspace": workspace,
            "clientId": clientId,
            "clientSecret": clientSecret,
        }
        return self.client._post(
            "api/alm_settings/create_bitbucketcloud", params=params
        )

    def create_github(
        self, key, url, appId, privateKey, clientId, clientSecret, webhookSecret=None
    ):
        """
        Create a GitHub instance setting.
        Requires 'Administer System' permission.
        :param key: Unique DevOps Platform setting key
        :param url: GitHub API URL
        :param appId: GitHub App ID
        :param privateKey: GitHub App private key
        :param clientId: GitHub App client ID
        :param clientSecret: GitHub App client secret
        :param webhookSecret: Optional GitHub App webhook secret
        """
        params = {
            "key": key,
            "url": url,
            "appId": appId,
            "privateKey": privateKey,
            "clientId": clientId,
            "clientSecret": clientSecret,
        }
        if webhookSecret:
            params["webhookSecret"] = webhookSecret
        return self.client._post("api/alm_settings/create_github", params=params)

    def create_gitlab(self, key, url, personalAccessToken):
        """
        Create a GitLab instance setting.
        Requires 'Administer System' permission.
        :param key: Unique DevOps Platform setting key
        :param url: GitLab API URL
        :param personalAccessToken: GitLab personal access token
        """
        params = {"key": key, "url": url, "personalAccessToken": personalAccessToken}
        return self.client._post("api/alm_settings/create_gitlab", params=params)

    def delete_setting(self, key):
        """
        Delete a DevOps Platform setting and its project bindings.
        Requires 'Administer System' permission.
        :param key: DevOps Platform setting key
        """
        params = {"key": key}
        return self.client._post("api/alm_settings/delete", params=params)

    def update_azure(self, key, url, newKey=None, personalAccessToken=None):
        """
        Update an Azure DevOps instance setting.
        Requires 'Administer System' permission.
        :param key: Existing DevOps Platform setting key
        :param url: Azure API URL; changing it requires personalAccessToken
        :param newKey: Optional replacement setting key
        :param personalAccessToken: Optional replacement personal access token
        """
        params = {"key": key, "url": url}
        if newKey:
            params["newKey"] = newKey
        if personalAccessToken:
            params["personalAccessToken"] = personalAccessToken
        return self.client._post("api/alm_settings/update_azure", params=params)

    def update_bitbucket(self, key, url, newKey=None, personalAccessToken=None):
        """
        Update a Bitbucket Server instance setting.
        Requires 'Administer System' permission.
        :param key: Existing DevOps Platform setting key
        :param url: Bitbucket Server API URL; changing it requires personalAccessToken
        :param newKey: Optional replacement setting key
        :param personalAccessToken: Optional replacement personal access token
        """
        params = {"key": key, "url": url}
        if newKey:
            params["newKey"] = newKey
        if personalAccessToken:
            params["personalAccessToken"] = personalAccessToken
        return self.client._post("api/alm_settings/update_bitbucket", params=params)

    def update_bitbucketcloud(
        self, key, workspace, clientId, newKey=None, clientSecret=None
    ):
        """
        Update a Bitbucket Cloud instance setting.
        Requires 'Administer System' permission.
        :param key: Existing DevOps Platform setting key
        :param workspace: Bitbucket Cloud workspace ID
        :param clientId: Bitbucket Cloud OAuth client ID
        :param newKey: Optional replacement setting key
        :param clientSecret: Optional replacement OAuth client secret
        """
        params = {"key": key, "workspace": workspace, "clientId": clientId}
        if newKey:
            params["newKey"] = newKey
        if clientSecret:
            params["clientSecret"] = clientSecret
        return self.client._post(
            "api/alm_settings/update_bitbucketcloud", params=params
        )

    def update_github(
        self,
        key,
        url,
        appId,
        clientId,
        newKey=None,
        privateKey=None,
        clientSecret=None,
        webhookSecret=None,
    ):
        """
        Update a GitHub instance setting.
        Requires 'Administer System' permission.
        :param key: Existing DevOps Platform setting key
        :param url: GitHub API URL; changing it requires privateKey
        :param appId: GitHub App ID
        :param clientId: GitHub App client ID
        :param newKey: Optional replacement setting key
        :param privateKey: Optional replacement GitHub App private key
        :param clientSecret: Optional replacement GitHub App client secret
        :param webhookSecret: None preserves the secret; an empty string clears it
        """
        params = {"key": key, "url": url, "appId": appId, "clientId": clientId}
        if newKey:
            params["newKey"] = newKey
        if privateKey:
            params["privateKey"] = privateKey
        if clientSecret:
            params["clientSecret"] = clientSecret
        # Unlike other optional strings, an empty webhook secret clears the value.
        if webhookSecret is not None:
            params["webhookSecret"] = webhookSecret
        return self.client._post("api/alm_settings/update_github", params=params)

    def update_gitlab(self, key, url, newKey=None, personalAccessToken=None):
        """
        Update a GitLab instance setting.
        Requires 'Administer System' permission.
        :param key: Existing DevOps Platform setting key
        :param url: GitLab API URL; changing it requires personalAccessToken
        :param newKey: Optional replacement setting key
        :param personalAccessToken: Optional replacement personal access token
        """
        params = {"key": key, "url": url}
        if newKey:
            params["newKey"] = newKey
        if personalAccessToken:
            params["personalAccessToken"] = personalAccessToken
        return self.client._post("api/alm_settings/update_gitlab", params=params)

    def validate(self, key):
        """
        Validate a DevOps Platform setting's connectivity and permissions.
        Requires 'Administer System' permission.
        :param key: DevOps Platform setting key
        """
        params = {"key": key}
        return self.client._get("api/alm_settings/validate", params=params)

    def delete_binding(self, project):
        """
        Delete the DevOps Platform binding of a project.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._post("api/alm_settings/delete_binding", params=params)

    def get_binding(self, project):
        """
        Get DevOps Platform binding of a given project.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/alm_settings/get_binding", params=params)

    def list_settings(self, project=None):
        """
        List DevOps Platform setting available for a given project.
        :param project: Project key
        """
        params = {}
        if project:
            params["project"] = project
        return self.client._get("api/alm_settings/list", params=params)

    def list_definitions(self):
        """
        List DevOps Platform setting definitions.
        Requires 'Administer System' permission.
        """
        return self.client._get("api/alm_settings/list_definitions")

    def set_azure_binding(
        self, almSetting, project, projectName=None, repositoryName=None, monorepo=None
    ):
        """
        Bind a project to an Azure DevOps Platform setting.
        :param almSetting: DevOps Platform setting key
        :param project: Project key
        :param projectName: Azure project name
        :param repositoryName: Azure repository name
        :param monorepo: Is this project part of a monorepo
        """
        params = {"almSetting": almSetting, "project": project}
        if projectName:
            params["projectName"] = projectName
        if repositoryName:
            params["repositoryName"] = repositoryName
        if monorepo is not None:
            params["monorepo"] = monorepo
        return self.client._post("api/alm_settings/set_azure_binding", params=params)

    def set_bitbucket_binding(
        self, almSetting, project, repository, slug=None, monorepo=None
    ):
        """
        Bind a project to a Bitbucket Platform setting.
        :param almSetting: DevOps Platform setting key
        :param project: Project key
        :param repository: Bitbucket repository key
        :param slug: Bitbucket repository slug
        :param monorepo: Is this project part of a monorepo
        """
        params = {
            "almSetting": almSetting,
            "project": project,
            "repository": repository,
        }
        if slug:
            params["slug"] = slug
        if monorepo is not None:
            params["monorepo"] = monorepo
        return self.client._post(
            "api/alm_settings/set_bitbucket_binding", params=params
        )

    def set_github_binding(self, almSetting, project, repository, monorepo=None):
        """
        Bind a project to a GitHub DevOps Platform setting.
        :param almSetting: DevOps Platform setting key
        :param project: Project key
        :param repository: GitHub repository identifier
        :param monorepo: Is this project part of a monorepo
        """
        params = {
            "almSetting": almSetting,
            "project": project,
            "repository": repository,
        }
        if monorepo is not None:
            params["monorepo"] = monorepo
        return self.client._post("api/alm_settings/set_github_binding", params=params)

    def set_gitlab_binding(self, almSetting, project, repository=None, monorepo=None):
        """
        Bind a project to a GitLab DevOps Platform setting.
        :param almSetting: DevOps Platform setting key
        :param project: Project key
        :param repository: GitLab repository identifier
        :param monorepo: Is this project part of a monorepo
        """
        params = {"almSetting": almSetting, "project": project}
        if repository:
            params["repository"] = repository
        if monorepo is not None:
            params["monorepo"] = monorepo
        return self.client._post("api/alm_settings/set_gitlab_binding", params=params)
