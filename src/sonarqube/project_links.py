class SonarQubeProjectLinks:
    def __init__(self, client):
        self.client = client

    def create_project_link(self, projectId, name, url):
        """
        Create a new project link.
        :param projectId: Project Id
        :param name: Link name
        :param url: Link url
        """
        params = {"projectId": projectId, "name": name, "url": url}
        return self.client._post("api/project_links/create", params=params)

    def delete_project_link(self, id):
        """
        Delete existing project link.
        :param id: Link ID
        """
        params = {"id": id}
        return self.client._post("api/project_links/delete", params=params)

    def search_project_links(self, projectId):
        """
        List links of a project.
        :param projectId: Project Id
        """
        params = {"projectId": projectId}
        return self.client._get("api/project_links/search", params=params)
