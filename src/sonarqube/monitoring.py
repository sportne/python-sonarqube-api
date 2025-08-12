class SonarQubeMonitoring:
    def __init__(self, client):
        self.client = client

    def get_monitoring_metrics(self):
        """
        Return monitoring metrics in Prometheus format.
        """
        return self.client._get("api/monitoring/metrics")
