class SonarQubeProjects:
    def __init__(self, client):
        self.client = client

    def search_projects(self, q):
        """
        Search for projects.
        :param q: The query to search for.
        """
        params = {"q": q}
        return self.client._get("api/projects/search", params=params)

    def create_project(self, project_key, name):
        """
        Create a new project.
        :param project_key: The key of the new project.
        :param name: The name of the new project.
        """
        params = {"project": project_key, "name": name}
        return self.client._post("api/projects/create", params=params)

    def delete_project(self, project_key):
        """
        Delete a project.
        :param project_key: The key of the project to delete.
        """
        params = {"project": project_key}
        return self.client._post("api/projects/delete", params=params)

    def bulk_delete_projects(self, analyzedBefore=None, projects=None, q=None):
        """
        Delete one or several projects.
        :param analyzedBefore: Delete projects analyzed before the given date (inclusive).
        :param projects: Comma-separated list of project keys
        :param q: Query string
        """
        params = {}
        if analyzedBefore:
            params["analyzedBefore"] = analyzedBefore
        if projects:
            params["projects"] = projects
        if q:
            params["q"] = q
        return self.client._post("api/projects/bulk_delete", params=params)

    def export_project_findings(self, project, branch=None, pullRequest=None):
        """
        Export all findings (issues and hotspots) of a specific project branch.
        :param project: Project key
        :param branch: Branch key
        :param pullRequest: Pull request key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/projects/export_findings", params=params)

    def get_project_contains_ai_code(self, project):
        """
        Get whether a project contains AI code or not
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/projects/get_contains_ai_code", params=params)

    def get_project_detected_ai_code(self, project):
        """
        Get detected AI code
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/projects/get_detected_ai_code", params=params)

    def get_project_license_usage(self):
        """
        Help admins to understand how much each project affects the total number of lines of code.
        """
        return self.client._get("api/projects/license_usage")

    def search_my_projects(self, organization=None):
        """
        Return list of projects for which the current user has 'Administer' permission.
        :param organization: Organization key
        """
        params = {}
        if organization:
            params["organization"] = organization
        return self.client._get("api/projects/search_my_projects", params=params)

    def search_my_scannable_projects(self, organization=None):
        """
        List projects that a user can scan.
        :param organization: Organization key
        """
        params = {}
        if organization:
            params["organization"] = organization
        return self.client._get(
            "api/projects/search_my_scannable_projects", params=params
        )

    def set_project_contains_ai_code(self, project, contains_ai_code):
        """
        Sets if the project passed as parameter contains or not AI code according to the value of the contains_ai_code parameter.
        :param project: Project key
        :param contains_ai_code: Boolean indicating if the project contains AI code
        """
        params = {"project": project, "contains_ai_code": contains_ai_code}
        return self.client._post("api/projects/set_contains_ai_code", params=params)

    def update_project_default_visibility(self, visibility):
        """
        Update the default visibility for new projects.
        :param visibility: New visibility (private or public)
        """
        params = {"visibility": visibility}
        return self.client._post(
            "api/projects/update_default_visibility", params=params
        )

    def update_project_key(self, project, new_key):
        """
        Update a project all its sub-components keys.
        :param project: Project key
        :param new_key: New project key
        """
        params = {"from": project, "to": new_key}
        return self.client._post("api/projects/update_key", params=params)

    def update_project_visibility(self, project, visibility):
        """
        Updates visibility of a project, application or a portfolio.
        :param project: Project, application or portfolio key
        :param visibility: New visibility (private or public)
        """
        params = {"project": project, "visibility": visibility}
        return self.client._post("api/projects/update_visibility", params=params)
