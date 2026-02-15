class SonarQubeSettings:
    def __init__(self, client):
        self.client = client

    def list_definitions(self, component=None):
        """
        List settings definitions.
        Requires 'Browse' permission when a component is specified.
        :param component: Component key
        """
        params = {}
        if component:
            params["component"] = component
        return self.client._get("api/settings/list_definitions", params=params)

    def reset(self, keys, component=None, branch=None, pullRequest=None):
        """
        Remove a setting value.
        :param keys: Comma-separated list of keys
        :param component: Component key
        :param branch: Branch key
        :param pullRequest: Pull request id
        """
        params = {"keys": keys}
        if component:
            params["component"] = component
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._post("api/settings/reset", params=params)

    def set(self, key, value=None, values=None, fieldValues=None, component=None):
        """
        Update a setting value.
        :param key: Setting key
        :param value: Setting value (for single value settings)
        :param values: Setting multi value (for multi-value settings)
        :param fieldValues: Setting field values (for property set settings)
        :param component: Component key
        """
        params = {"key": key}
        if value is not None:
            params["value"] = value
        if values is not None:
            params["values"] = values
        if fieldValues is not None:
            params["fieldValues"] = fieldValues
        if component:
            params["component"] = component
        return self.client._post("api/settings/set", params=params)

    def values(self, keys=None, component=None):
        """
        List settings values.
        :param keys: Comma-separated list of keys
        :param component: Component key
        """
        params = {}
        if keys:
            params["keys"] = keys
        if component:
            params["component"] = component
        return self.client._get("api/settings/values", params=params)
