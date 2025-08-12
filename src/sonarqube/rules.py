class SonarQubeRules:
    def __init__(self, client):
        self.client = client

    def get_rules_app(self):
        """
        Get data required for rendering the page 'Coding Rules'.
        """
        return self.client._get("api/rules/app")

    def create_rule(self, custom_key, name, markdown_description, **kwargs):
        """
        Create a custom rule.
        :param custom_key: Rule key
        :param name: Rule name
        :param markdown_description: Rule description
        :param kwargs: Additional parameters
        """
        params = {
            "custom_key": custom_key,
            "name": name,
            "markdown_description": markdown_description,
        }
        params.update(kwargs)
        return self.client._post("api/rules/create", params=params)

    def delete_rule(self, key):
        """
        Delete custom rule.
        :param key: Rule key
        """
        params = {"key": key}
        return self.client._post("api/rules/delete", params=params)

    def list_rules(self, **kwargs):
        """
        List rules.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/rules/list", params=kwargs)

    def list_rule_repositories(self, **kwargs):
        """
        List available rule repositories.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/rules/repositories", params=kwargs)

    def search_rules(self, **kwargs):
        """
        Search for a collection of relevant rules matching a specified query.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/rules/search", params=kwargs)

    def show_rule(self, key, **kwargs):
        """
        Get detailed information about a rule.
        :param key: Rule key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._get("api/rules/show", params=params)

    def list_rule_tags(self, **kwargs):
        """
        List rule tags.
        :param kwargs: Additional parameters
        """
        return self.client._get("api/rules/tags", params=kwargs)

    def update_rule(self, key, **kwargs):
        """
        Update an existing rule.
        :param key: Rule key
        :param kwargs: Additional parameters
        """
        params = {"key": key}
        params.update(kwargs)
        return self.client._post("api/rules/update", params=params)
