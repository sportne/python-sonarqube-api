class SonarQubeServer:
    def __init__(self, client):
        self.client = client

    def get_version(self):
        """
        Get the version of SonarQube.
        """
        return self.client._get("api/server/version")
