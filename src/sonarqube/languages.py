class SonarQubeLanguages:
    def __init__(self, client):
        self.client = client

    def list_languages(self, q=None, ps=None):
        """
        List supported programming languages.
        :param q: A pattern to match language keys/names against.
        :param ps: The size of the list to return, 0 for all languages.
        """
        params = {}
        if q:
            params["q"] = q
        if ps:
            params["ps"] = ps
        return self.client._get("api/languages/list", params=params)
