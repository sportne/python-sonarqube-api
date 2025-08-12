class SonarQubeApplications:
    def __init__(self, client):
        self.client = client

    def add_project_to_application(self, application, project):
        """
        Add a project to an application.
        :param application: Application key
        :param project: Project key
        """
        params = {"application": application, "project": project}
        return self.client._post("api/applications/add_project", params=params)

    def create_application(self, name, key=None, visibility=None, description=None):
        """
        Create a new application.
        :param name: Name of the application
        :param key: Key of the application
        :param visibility: Visibility of the application
        :param description: Description of the application
        """
        params = {"name": name}
        if key:
            params["key"] = key
        if visibility:
            params["visibility"] = visibility
        if description:
            params["description"] = description
        return self.client._post("api/applications/create", params=params)

    def create_branch_in_application(self, application, branch, project, projectBranch):
        """
        Create a new branch on a given application.
        :param application: Application key
        :param branch: Branch name
        :param project: Project keys
        :param projectBranch: Project branches
        """
        params = {
            "application": application,
            "branch": branch,
            "project": project,
            "projectBranch": projectBranch,
        }
        return self.client._post("api/applications/create_branch", params=params)

    def delete_application(self, application):
        """
        Delete an application definition.
        :param application: Application key
        """
        params = {"application": application}
        return self.client._post("api/applications/delete", params=params)

    def delete_branch_in_application(self, application, branch):
        """
        Delete a branch on a given application.
        :param application: Application key
        :param branch: Branch name
        """
        params = {"application": application, "branch": branch}
        return self.client._post("api/applications/delete_branch", params=params)

    def refresh_applications(self, key=None):
        """
        Refresh one or all applications.
        :param key: Application key. If not specified, all applications are refreshed.
        """
        params = {}
        if key:
            params["key"] = key
        return self.client._post("api/applications/refresh", params=params)

    def remove_project_from_application(self, application, project):
        """
        Remove a project from an application.
        :param application: Application key
        :param project: Project key
        """
        params = {"application": application, "project": project}
        return self.client._post("api/applications/remove_project", params=params)

    def search_application_projects(self, application, q=None, p=None, ps=None):
        """
        List projects manually selected in an application.
        :param application: Application key
        :param q: Query to filter projects
        :param p: Page number
        :param ps: Page size
        """
        params = {"application": application}
        if q:
            params["q"] = q
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self.client._get("api/applications/search_projects", params=params)

    def set_application_tags(self, application, tags):
        """
        Set tags on a application.
        :param application: Application key
        :param tags: Comma-separated list of tags
        """
        params = {"application": application, "tags": tags}
        return self.client._post("api/applications/set_tags", params=params)

    def show_application(self, application, branch=None, pullRequest=None):
        """
        Returns an application and its associated projects.
        :param application: Application key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"application": application}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/applications/show", params=params)

    def show_application_leak(self, application, branch=None, pullRequest=None):
        """
        Show leak of an application.
        :param application: Application key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"application": application}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/applications/show_leak", params=params)

    def update_application(self, application, name=None, description=None):
        """
        Update an application.
        :param application: Application key
        :param name: New name of the application
        :param description: New description of the application
        """
        params = {"application": application}
        if name:
            params["name"] = name
        if description:
            params["description"] = description
        return self.client._post("api/applications/update", params=params)

    def update_branch_in_application(self, application, branch, name):
        """
                Update a branch on a given application.
        .       :param application: Application key
                :param branch: Branch name
                :param name: New branch name
        """
        params = {"application": application, "branch": branch, "name": name}
        return self.client._post("api/applications/update_branch", params=params)
