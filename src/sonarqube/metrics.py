class SonarQubeMetrics:
    def __init__(self, client):
        self.client = client

    def search_metrics(self, p=None, ps=None):
        """
        Search for metrics.
        :param p: Page number
        :param ps: Page size
        """
        params = {}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self.client._get("api/metrics/search", params=params)

    def get_metric_types(self):
        """
        List all available metric types.
        """
        return self.client._get("api/metrics/types")
