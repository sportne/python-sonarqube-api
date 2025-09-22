class SonarQubeDopTranslationV2:
    def __init__(self, client):
        self.client = client

    def create_project(
        self,
        projectKey,
        projectName,
        devOpsPlatformSettingId,
        repositoryIdentifier,
        monorepo,
        **kwargs,
    ):
        """
        Create a SonarQube project with the information from the provided DevOps platform project.
        :param projectKey: Key of the project to create.
        :param projectName: Name of the project to create.
        :param devOpsPlatformSettingId: Identifier of DevOps platform configuration to use.
        :param repositoryIdentifier: Identifier of the DevOps platform repository to import.
        :param monorepo: True if project is part of a mono repo.
        :param kwargs: Additional parameters
        """
        params = {
            "projectKey": projectKey,
            "projectName": projectName,
            "devOpsPlatformSettingId": devOpsPlatformSettingId,
            "repositoryIdentifier": repositoryIdentifier,
            "monorepo": monorepo,
        }
        params.update(kwargs)
        return self.client._post("api/v2/dop-translation/bound-projects", json=params)

    def list_dop_settings(self):
        """
        List all DevOps Platform Integration settings.
        """
        return self.client._get("api/v2/dop-translation/dop-settings")
