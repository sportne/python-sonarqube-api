class SonarQubeSystemV2:
    def __init__(self, client):
        self.client = client

    def get_system_health(self, passcode=None):
        """
        Get system health.
        :param passcode: Passcode can be provided.
        """
        headers = {}
        if passcode:
            headers["X-Sonar-Passcode"] = passcode
        return self.client._get("api/v2/system/health", headers=headers)

    def get_system_liveness(self, passcode=None):
        """
        Provide liveness of SonarQube.
        :param passcode: Passcode can be provided.
        """
        headers = {}
        if passcode:
            headers["X-Sonar-Passcode"] = passcode
        return self.client._get("api/v2/system/liveness", headers=headers)

    def get_migrations_status(self):
        """
        Return the detailed status of ongoing database migrations.
        """
        return self.client._get("api/v2/system/migrations-status")
