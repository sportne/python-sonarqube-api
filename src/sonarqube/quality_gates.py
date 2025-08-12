class SonarQubeQualityGates:
    def __init__(self, client):
        self.client = client

    def add_group_to_quality_gate(self, gateId, groupId, organization=None):
        """
        Allow a group of users to edit a Quality Gate.
        :param gateId: Quality Gate ID
        :param groupId: Group ID
        :param organization: Organization key
        """
        params = {"gateId": gateId, "groupId": groupId}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/add_group", params=params)

    def add_user_to_quality_gate(self, gateId, userId, organization=None):
        """
        Allow a user to edit a Quality Gate.
        :param gateId: Quality Gate ID
        :param userId: User ID
        :param organization: Organization key
        """
        params = {"gateId": gateId, "userId": userId}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/add_user", params=params)

    def get_application_quality_gate_status(
        self, application, branch=None, pullRequest=None
    ):
        """
        Get the quality gate status of an application.
        :param application: Application key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"application": application}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/qualitygates/application_status", params=params)

    def copy_quality_gate(self, sourceName, destName, organization=None):
        """
        Copy a Quality Gate.
        :param sourceName: Source Quality Gate name
        :param destName: Destination Quality Gate name
        :param organization: Organization key
        """
        params = {"sourceName": sourceName, "name": destName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/copy", params=params)

    def create_quality_gate(self, name, organization=None):
        """
        Create a Quality Gate.
        :param name: Quality Gate name
        :param organization: Organization key
        """
        params = {"name": name}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/create", params=params)

    def create_quality_gate_condition(
        self, gateName, metric, op, error, organization=None
    ):
        """
        Add a new condition to a quality gate.
        :param gateName: Quality Gate name
        :param metric: Metric key
        :param op: Operator (LT or GT)
        :param error: Error threshold
        :param organization: Organization key
        """
        params = {"gateName": gateName, "metric": metric, "op": op, "error": error}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/create_condition", params=params)

    def delete_quality_gate_condition(self, id, organization=None):
        """
        Delete a condition from a quality gate.
        :param id: Condition ID
        :param organization: Organization key
        """
        params = {"id": id}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/delete_condition", params=params)

    def deselect_project_from_quality_gate(self, projectKey, organization=None):
        """
        Remove the association of a project from a quality gate.
        :param projectKey: Project key
        :param organization: Organization key
        """
        params = {"projectKey": projectKey}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/deselect", params=params)

    def destroy_quality_gate(self, name, organization=None):
        """
        Delete a Quality Gate.
        :param name: Quality Gate name
        :param organization: Organization key
        """
        params = {"name": name}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/destroy", params=params)

    def get_quality_gate_by_project(self, projectKey, organization=None):
        """
        Get the quality gate of a project.
        :param projectKey: Project key
        :param organization: Organization key
        """
        params = {"projectKey": projectKey}
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualitygates/get_by_project", params=params)

    def list_quality_gates(self, organization=None):
        """
        Get a list of quality gates.
        :param organization: Organization key
        """
        params = {}
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualitygates/list", params=params)

    def get_project_quality_gate_status(
        self,
        analysisId=None,
        projectId=None,
        projectKey=None,
        branch=None,
        pullRequest=None,
    ):
        """
        Get the quality gate status of a project or a Compute Engine task.
        :param analysisId: Analysis ID
        :param projectId: Project ID
        :param projectKey: Project key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {}
        if analysisId:
            params["analysisId"] = analysisId
        if projectId:
            params["projectId"] = projectId
        if projectKey:
            params["projectKey"] = projectKey
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/qualitygates/project_status", params=params)

    def remove_group_from_quality_gate(self, gateId, groupId, organization=None):
        """
        Remove the ability from a group to edit a Quality Gate.
        :param gateId: Quality Gate ID
        :param groupId: Group ID
        :param organization: Organization key
        """
        params = {"gateId": gateId, "groupId": groupId}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/remove_group", params=params)

    def remove_user_from_quality_gate(self, gateId, userId, organization=None):
        """
        Remove the ability from an user to edit a Quality Gate.
        :param gateId: Quality Gate ID
        :param userId: User ID
        :param organization: Organization key
        """
        params = {"gateId": gateId, "userId": userId}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/remove_user", params=params)

    def rename_quality_gate(self, currentName, newName, organization=None):
        """
        Rename a Quality Gate.
        :param currentName: Current Quality Gate name
        :param newName: New Quality Gate name
        :param organization: Organization key
        """
        params = {"name": newName, "id": currentName}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/rename", params=params)

    def search_quality_gates(
        self, gateId, p=None, ps=None, q=None, selected=None, organization=None
    ):
        """
        Search for projects associated (or not) to a quality gate.
        :param gateId: Quality Gate ID
        :param p: Page number
        :param ps: Page size
        :param q: Query string
        :param selected: Selection status
        :param organization: Organization key
        """
        params = {"gateId": gateId}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if q:
            params["q"] = q
        if selected:
            params["selected"] = selected
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualitygates/search", params=params)

    def search_quality_gate_groups(
        self, gateId, p=None, ps=None, q=None, organization=None
    ):
        """
        List the groups that are allowed to edit a Quality Gate.
        :param gateId: Quality Gate ID
        :param p: Page number
        :param ps: Page size
        :param q: Query string
        :param organization: Organization key
        """
        params = {"gateId": gateId}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if q:
            params["q"] = q
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualitygates/search_groups", params=params)

    def search_quality_gate_users(
        self, gateId, p=None, ps=None, q=None, organization=None
    ):
        """
        List the users that are allowed to edit a Quality Gate.
        :param gateId: Quality Gate ID
        :param p: Page number
        :param ps: Page size
        :param q: Query string
        :param organization: Organization key
        """
        params = {"gateId": gateId}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if q:
            params["q"] = q
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualitygates/search_users", params=params)

    def select_project_for_quality_gate(self, projectKey, gateId, organization=None):
        """
        Associate a project to a quality gate.
        :param projectKey: Project key
        :param gateId: Quality Gate ID
        :param organization: Organization key
        """
        params = {"projectKey": projectKey, "gateId": gateId}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/select", params=params)

    def set_quality_gate_ai_code_assurance(self, gateId, isAssured, organization=None):
        """
        Qualify or disqualify a custom Quality Gate as AI Code Assured.
        :param gateId: Quality Gate ID
        :param isAssured: Boolean indicating if the Quality Gate is AI Code Assured
        :param organization: Organization key
        """
        params = {"gateId": gateId, "isAssured": isAssured}
        if organization:
            params["organization"] = organization
        return self.client._post(
            "api/qualitygates/set_ai_code_assurance", params=params
        )

    def set_default_quality_gate(self, name, organization=None):
        """
        Set a quality gate as the default quality gate.
        :param name: Quality Gate name
        :param organization: Organization key
        """
        params = {"name": name}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/set_as_default", params=params)

    def show_quality_gate(self, name, organization=None):
        """
        Display the details of a quality gate
        :param name: Quality Gate name
        :param organization: Organization key
        """
        params = {"name": name}
        if organization:
            params["organization"] = organization
        return self.client._get("api/qualitygates/show", params=params)

    def update_quality_gate_condition(self, id, metric, op, error, organization=None):
        """
        Update a condition attached to a quality gate.
        :param id: Condition ID
        :param metric: Metric key
        :param op: Operator (LT or GT)
        :param error: Error threshold
        :param organization: Organization key
        """
        params = {"id": id, "metric": metric, "op": op, "error": error}
        if organization:
            params["organization"] = organization
        return self.client._post("api/qualitygates/update_condition", params=params)
