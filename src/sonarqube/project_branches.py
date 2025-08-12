class SonarQubeProjectBranches:
    def __init__(self, client):
        self.client = client

    def delete_project_branch(self, project, branch):
        """
        Delete a non-main branch of a project.
        :param project: Project key
        :param branch: Branch name
        """
        params = {"project": project, "branch": branch}
        return self.client._post("api/project_branches/delete", params=params)

    def get_project_branch_ai_code_assurance(self, project, branch=None):
        """
        Gets whether a project passed as parameter is AI Code Assured or not.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self.client._get(
            "api/project_branches/get_ai_code_assurance", params=params
        )

    def list_project_branches(self, project):
        """
        List the branches of a project.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/project_branches/list", params=params)

    def rename_project_branch(self, project, name):
        """
        Rename the main branch of a project.
        :param project: Project key
        :param name: New branch name
        """
        params = {"project": project, "name": name}
        return self.client._post("api/project_branches/rename", params=params)

    def set_project_branch_automatic_deletion_protection(
        self, project, branch, is_protected
    ):
        """
        Protect a specific branch from automatic deletion.
        :param project: Project key
        :param branch: Branch name
        :param is_protected: Boolean indicating if the branch should be protected
        """
        params = {"project": project, "branch": branch, "isProtected": is_protected}
        return self.client._post(
            "api/project_branches/set_automatic_deletion_protection", params=params
        )

    def set_project_main_branch(self, project, branch):
        """
        Allow to set a new main branch.
        :param project: Project key
        :param branch: Branch name
        """
        params = {"project": project, "branch": branch}
        return self.client._post("api/project_branches/set_main", params=params)
