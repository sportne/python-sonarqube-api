class SonarQubeCleanCodePolicyV2:
    def __init__(self, client):
        self.client = client

    def create_custom_rule(
        self, key, templateKey, name, markdownDescription, impacts, **kwargs
    ):
        """
        Create a custom rule.
        :param key: Key of the custom rule to create.
        :param templateKey: Key of the rule template to be used.
        :param name: Rule name.
        :param markdownDescription: Rule description in markdown format.
        :param impacts: Impacts.
        :param kwargs: Additional parameters
        """
        params = {
            "key": key,
            "templateKey": templateKey,
            "name": name,
            "markdownDescription": markdownDescription,
            "impacts": impacts,
        }
        params.update(kwargs)
        return self.client._post("/api/v2/clean-code-policy/rules", json=params)
