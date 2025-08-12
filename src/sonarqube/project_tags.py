class SonarQubeProjectTags:
    def __init__(self, client):
        self.client = client

    def search_project_tags(self, q=None):
        """
        Search tags
        :param q: Limit search to tags that contain the supplied string.
        """
        params = {}
        if q:
            params["q"] = q
        return self.client._get("api/project_tags/search", params=params)

    def set_project_tags(self, project, tags):
        """
        Set tags on a project.
        :param project: Project key
        :param tags: Comma-separated list of tags
        """
        params = {"project": project, "tags": tags}
        return self.client._post("api/project_tags/set", params=params)
