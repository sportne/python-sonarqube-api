class SonarQubeSystem:
    def __init__(self, client):
        self.client = client

    def get_system_health(self):
        """
        Get system health.
        """
        return self.client._get("api/system/health")

    def get_system_metrics(self):
        """
        Get system metrics.
        """
        return self.client._get("api/system/metrics")

    def get_system_status(self):
        """
        Get system status.
        """
        return self.client._get("api/system/status")

    def get_system_upgrades(self):
        """
        Get system upgrades.
        """
        return self.client._get("api/system/upgrades")

    def get_system_logs(self):
        """
        Get system logs.
        """
        return self.client._get("api/system/logs")

    def get_system_info(self):
        """
        Get system configuration.
        """
        return self.client._get("api/system/info")
