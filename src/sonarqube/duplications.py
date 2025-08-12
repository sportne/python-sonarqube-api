class SonarQubeDuplications:
    def __init__(self, client):
        self.client = client

    def get_duplications(self, key, branch=None, pullRequest=None):
        """
        Get duplications.
        :param key: File key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"key": key}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/duplications/show", params=params)
