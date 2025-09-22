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

    def change_log_level(self, level):
        """
        Temporarily changes level of logs.
        :param level: The new level. Possible values: TRACE, DEBUG, INFO
        """
        params = {"level": level}
        return self.client._post("api/system/change_log_level", params=params)

    def get_system_liveness(self):
        """
        Provide liveness of SonarQube.
        """
        return self.client._get("api/system/liveness")

    def migrate_db(self):
        """
        Migrate the database.
        """
        return self.client._post("api/system/migrate_db")

    def ping_system(self):
        """
        Answers 'pong' as plain-text.
        """
        return self.client._get("api/system/ping")

    def restart_system(self):
        """
        Restarts server.
        """
        return self.client._post("api/system/restart")
