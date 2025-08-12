class SonarQubeNewCodePeriods:
    def __init__(self, client):
        self.client = client

    def list_new_code_periods(self, project):
        """
        Lists the new code definition for all branches in a project.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._get("api/new_code_periods/list", params=params)

    def set_new_code_period(self, project=None, branch=None, type=None, value=None):
        """
        Updates the new code definition on different levels.
        :param project: Project key
        :param branch: Branch key
        :param type: Type of new code definition
        :param value: Value of new code definition
        """
        params = {}
        if project:
            params["project"] = project
        if branch:
            params["branch"] = branch
        if type:
            params["type"] = type
        if value:
            params["value"] = value
        return self.client._post("api/new_code_periods/set", params=params)

    def show_new_code_period(self, project=None, branch=None):
        """
        Shows the new code definition.
        :param project: Project key
        :param branch: Branch key
        """
        params = {}
        if project:
            params["project"] = project
        if branch:
            params["branch"] = branch
        return self.client._get("api/new_code_periods/show", params=params)

    def unset_new_code_period(self, project=None, branch=None):
        """
        Unsets the new code definition for a branch, project or global.
        :param project: Project key
        :param branch: Branch key
        """
        params = {}
        if project:
            params["project"] = project
        if branch:
            params["branch"] = branch
        return self.client._post("api/new_code_periods/unset", params=params)
