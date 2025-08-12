class SonarQubeMeasures:
    def __init__(self, client):
        self.client = client

    def get_measures_component(
        self,
        component,
        metricKeys,
        branch=None,
        pullRequest=None,
        additionalFields=None,
    ):
        """
        Return component with specified measures.
        :param component: Component key
        :param metricKeys: Comma-separated list of metric keys
        :param branch: Branch key
        :param pullRequest: Pull request ID
        :param additionalFields: Comma-separated list of additional fields
        """
        params = {"component": component, "metricKeys": metricKeys}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        if additionalFields:
            params["additionalFields"] = additionalFields
        return self.client._get("api/measures/component", params=params)

    def get_measures_component_tree(self, component, metricKeys, **kwargs):
        """
        Navigate through components based on the chosen strategy with specified measures.
        :param component: Base component key
        :param metricKeys: Comma-separated list of metric keys
        :param kwargs: Additional parameters
        """
        params = {"component": component, "metricKeys": metricKeys}
        params.update(kwargs)
        return self.client._get("api/measures/component_tree", params=params)

    def search_measures(self, projectKeys, metricKeys, **kwargs):
        """
        Search for project measures ordered by project names.
        :param projectKeys: Comma-separated list of project keys
        :param metricKeys: Comma-separated list of metric keys
        :param kwargs: Additional parameters
        """
        params = {"projectKeys": projectKeys, "metricKeys": metricKeys}
        params.update(kwargs)
        return self.client._get("api/measures/search", params=params)

    def search_measures_history(self, component, metrics, **kwargs):
        """
        Search measures history of a component.
        :param component: Component key
        :param metrics: Comma-separated list of metric keys
        :param kwargs: Additional parameters
        """
        params = {"component": component, "metrics": metrics}
        params.update(kwargs)
        return self.client._get("api/measures/search_history", params=params)
