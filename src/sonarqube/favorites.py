class SonarQubeFavorites:
    def __init__(self, client):
        self.client = client

    def add_favorite(self, component):
        """
        Add a component as favorite.
        :param component: Component key
        """
        params = {"component": component}
        return self.client._post("api/favorites/add", params=params)

    def remove_favorite(self, component):
        """
        Remove a component as favorite.
        :param component: Component key
        """
        params = {"component": component}
        return self.client._post("api/favorites/remove", params=params)

    def search_favorites(self, p=None, ps=None):
        """
        Search for favorites.
        :param p: Page number
        :param ps: Page size
        """
        params = {}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self.client._get("api/favorites/search", params=params)
