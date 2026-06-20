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
        if p is not None and p != "":
            params["p"] = p
        if ps is not None and ps != "":
            params["ps"] = ps
        return self.client._get("api/metrics/search", params=params)

    def get_metric_types(self):
        """
        List all available metric types.
        """
        return self.client._get("api/metrics/types")
