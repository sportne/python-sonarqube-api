class SonarQubeProjectDump:
    def __init__(self, client):
        self.client = client

    def export_project_dump(self, project, projectKey=None):
        """
        Triggers project dump so that the project can be imported to another SonarQube server.
        :param project: Project key
        :param projectKey: Project key (optional)
        """
        params = {"project": project}
        if projectKey:
            params["projectKey"] = projectKey
        return self.client._post("api/project_dump/export", params=params)

    def import_project_dump(self, file, project=None, projectKey=None):
        """
        Triggers the import of a project dump.
        :param file: Path to the project dump file
        :param project: Project key (optional)
        :param projectKey: Project key (optional)
        """
        params = {}
        if project:
            params["project"] = project
        if projectKey:
            params["projectKey"] = projectKey
        with open(file, "rb") as f:
            files = {"file": f}
            return self.client._post(
                "api/project_dump/import", params=params, files=files
            )

    def get_project_dump_status(self, project=None, projectKey=None, id=None):
        """
        Provide the import and export status of a project.
        :param project: Project key (optional)
        :param projectKey: Project key (optional)
        :param id: Project id (optional)
        """
        params = {}
        if project:
            params["project"] = project
        if projectKey:
            params["projectKey"] = projectKey
        if id:
            params["id"] = id
        return self.client._get("api/project_dump/status", params=params)
