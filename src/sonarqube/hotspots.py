class SonarQubeHotspots:
    def __init__(self, client):
        self.client = client

    def add_hotspot_comment(self, hotspot, text):
        """
        Add a comment to a Security Hotspot.
        :param hotspot: Hotspot key
        :param text: Comment text
        """
        params = {"hotspot": hotspot, "text": text}
        return self.client._post("api/hotspots/add_comment", params=params)

    def assign_hotspot(self, hotspot, assignee):
        """
        Assign a hotspot to an active user.
        :param hotspot: Hotspot key
        :param assignee: User login
        """
        params = {"hotspot": hotspot, "assignee": assignee}
        return self.client._post("api/hotspots/assign", params=params)

    def change_hotspot_status(self, hotspot, status, resolution=None, comment=None):
        """
        Change the status of a Security Hotspot.
        :param hotspot: Hotspot key
        :param status: The new status
        :param resolution: The resolution if the new status is "REVIEWED"
        :param comment: A comment to add
        """
        params = {"hotspot": hotspot, "status": status}
        if resolution:
            params["resolution"] = resolution
        if comment:
            params["comment"] = comment
        return self.client._post("api/hotspots/change_status", params=params)

    def delete_hotspot_comment(self, comment):
        """
        Delete comment from Security Hotspot.
        :param comment: Comment key
        """
        params = {"comment": comment}
        return self.client._post("api/hotspots/delete_comment", params=params)

    def edit_hotspot_comment(self, comment, text):
        """
        Edit a comment.
        :param comment: Comment key
        :param text: New comment text
        """
        params = {"comment": comment, "text": text}
        return self.client._post("api/hotspots/edit_comment", params=params)

    def list_hotspots(self, projectKey, p=None, ps=None):
        """
        List Security Hotpots.
        :param projectKey: Project key
        :param p: Page number
        :param ps: Page size
        """
        params = {"projectKey": projectKey}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self.client._get("api/hotspots/list", params=params)

    def pull_hotspots(self, branch, project):
        """
        Fetch and return all hotspots for a given branch.
        :param branch: Branch key
        :param project: Project key
        """
        params = {"branch": branch, "project": project}
        return self.client._get("api/hotspots/pull", params=params)

    def search_hotspots(self, projectKey, **kwargs):
        """
        Search for Security Hotspots.
        :param projectKey: Project key
        :param kwargs: Additional parameters
        """
        params = {"projectKey": projectKey}
        params.update(kwargs)
        return self.client._get("api/hotspots/search", params=params)

    def show_hotspot(self, hotspot):
        """
        Provides the details of a Security Hotspot.
        :param hotspot: Hotspot key
        """
        params = {"hotspot": hotspot}
        return self.client._get("api/hotspots/show", params=params)
