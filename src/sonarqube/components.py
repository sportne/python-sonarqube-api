class SonarQubeComponents:
    def __init__(self, client):
        self.client = client

    def get_components_app(self, component, branch=None, pullRequest=None):
        """
        Coverage data required for rendering the component viewer.
        :param component: Component key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"component": component}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/components/app", params=params)

    def search_components(self, qualifiers, q=None, p=None, ps=None):
        """
        Search for components.
        :param qualifiers: Comma-separated list of component qualifiers.
        :param q: Query to filter components
        :param p: Page number
        :param ps: Page size
        """
        params = {"qualifiers": qualifiers}
        if q:
            params["q"] = q
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self.client._get("api/components/search", params=params)

    def search_components_projects(self, q=None, p=None, ps=None):
        """
        Search for projects.
        :param q: Query to filter projects
        :param p: Page number
        :param ps: Page size
        """
        params = {}
        if q:
            params["q"] = q
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self.client._get("api/components/search_projects", params=params)

    def show_component(self, component, branch=None, pullRequest=None):
        """
        Returns a component and its ancestors.
        :param component: Component key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"component": component}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/components/show", params=params)

    def get_component_suggestions(self, q=None):
        """
        Internal WS for the top-right search engine.
        :param q: Query to filter components
        """
        params = {}
        if q:
            params["q"] = q
        return self.client._get("api/components/suggestions", params=params)

    def get_component_tree(self, component, **kwargs):
        """
        Navigate through components based on the chosen strategy.
        :param component: Base component key
        :param kwargs: Additional parameters
        """
        params = {"component": component}
        params.update(kwargs)
        return self.client._get("api/components/tree", params=params)
