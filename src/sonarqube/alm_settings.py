class SonarQubeAlmSettings:
    def __init__(self, client):
        self.client = client

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
