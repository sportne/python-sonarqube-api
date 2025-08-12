class SonarQubeProjectPullRequests:
    def __init__(self, client):
        self.client = client

    def delete_project_pull_request(self, project, pullRequest):
        """
        Delete a pull request.
        :param project: Project key
        :param pullRequest: Pull request key
        """
        params = {"project": project, "pullRequest": pullRequest}
        return self.client._post("api/project_pull_requests/delete", params=params)

    def list_project_pull_requests(self, project):
        """
        List the pull requests of a project.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/project_pull_requests/list", params=params)
