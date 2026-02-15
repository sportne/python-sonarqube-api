class SonarQubeAnalysisCache:
    def __init__(self, client):
        self.client = client

    def get(self, project, branch=None):
        """
        Get the scanner's cached data for a branch.
        Requires scan permission on the project.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self.client._get("api/analysis_cache/get", params=params)
