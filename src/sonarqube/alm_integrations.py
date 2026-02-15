class SonarQubeAlmIntegrations:
    def __init__(self, client):
        self.client = client

    def list_azure_projects(self, almSetting):
        """
        List Azure projects.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        """
        params = {"almSetting": almSetting}
        return self.client._get(
            "api/alm_integrations/list_azure_projects", params=params
        )

    def list_bitbucketserver_projects(self, almSetting):
        """
        List the Bitbucket Server projects.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        """
        params = {"almSetting": almSetting}
        return self.client._get(
            "api/alm_integrations/list_bitbucketserver_projects", params=params
        )

    def search_azure_repos(self, almSetting, projectName=None, searchQuery=None):
        """
        Search the Azure DevOps repositories.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        :param projectName: Project name filter
        :param searchQuery: Search query filter
        """
        params = {"almSetting": almSetting}
        if projectName:
            params["projectName"] = projectName
        if searchQuery:
            params["searchQuery"] = searchQuery
        return self.client._get(
            "api/alm_integrations/search_azure_repos", params=params
        )

    def search_bitbucketcloud_repos(self, almSetting):
        """
        Search the Bitbucket Cloud repositories.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        """
        params = {"almSetting": almSetting}
        return self.client._get(
            "api/alm_integrations/search_bitbucketcloud_repos", params=params
        )

    def search_bitbucketserver_repos(
        self, almSetting, projectName=None, searchQuery=None
    ):
        """
        Search the Bitbucket Server repositories.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        :param projectName: Project name filter
        :param searchQuery: Search query filter
        """
        params = {"almSetting": almSetting}
        if projectName:
            params["projectName"] = projectName
        if searchQuery:
            params["searchQuery"] = searchQuery
        return self.client._get(
            "api/alm_integrations/search_bitbucketserver_repos", params=params
        )

    def search_gitlab_repos(self, almSetting, projectName=None):
        """
        Search the GitLab repositories.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        :param projectName: Project name filter
        """
        params = {"almSetting": almSetting}
        if projectName:
            params["projectName"] = projectName
        return self.client._get(
            "api/alm_integrations/search_gitlab_repos", params=params
        )

    def import_github_project(self, almSetting, organization, repository):
        """
        Import a GitHub project to SonarQube.
        Requires the 'Create Projects' permission.
        :param almSetting: DevOps Platform setting key
        :param organization: GitHub organization
        :param repository: GitHub repository name
        """
        params = {
            "almSetting": almSetting,
            "organization": organization,
            "repository": repository,
        }
        return self.client._post(
            "api/alm_integrations/import_github_project", params=params
        )

    def set_pat(self, almSetting, pat, username=None):
        """
        Set a Personal Access Token for the given DevOps Platform setting.
        :param almSetting: DevOps Platform setting key
        :param pat: Personal Access Token
        :param username: Username (required for Bitbucket Server)
        """
        params = {"almSetting": almSetting, "pat": pat}
        if username:
            params["username"] = username
        return self.client._post("api/alm_integrations/set_pat", params=params)
