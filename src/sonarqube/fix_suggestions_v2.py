class SonarQubeFixSuggestionsV2:
    def __init__(self, client):
        self.client = client

    def suggest_fix(self, projectKey, issueId, issue=None):
        """
        Suggest a fix for the given issueId.
        :param projectKey: Project key
        :param issueId: Issue key
        :param issue: Issue object
        """
        params = {"projectKey": projectKey, "issueId": issueId}
        if issue:
            params["issue"] = issue
        return self.client._post("/api/v2/fix-suggestions/ai-suggestions", json=params)

    def get_suggestion_availability(self, issueId):
        """
        Fetch AI suggestion availability for the given issueId.
        :param issueId: Issue key
        """
        return self.client._get(f"/api/v2/fix-suggestions/issues/{issueId}")
