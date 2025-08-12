class SonarQubePlugins:
    def __init__(self, client):
        self.client = client

    def get_available_plugins(self):
        """
        Get the list of all the plugins available for installation.
        """
        return self.client._get("api/plugins/available")

    def cancel_all_pending_plugins(self):
        """
        Cancels any operation pending on any plugin.
        """
        return self.client._post("api/plugins/cancel_all")

    def download_plugin(self, key):
        """
        Download plugin JAR.
        :param key: Plugin key
        """
        params = {"key": key}
        return self.client._get("api/plugins/download", params=params)

    def install_plugin(self, key):
        """
        Installs the latest version of a plugin.
        :param key: Plugin key
        """
        params = {"key": key}
        return self.client._post("api/plugins/install", params=params)

    def get_installed_plugins(self):
        """
        Get the list of all the plugins installed.
        """
        return self.client._get("api/plugins/installed")

    def get_pending_plugins(self):
        """
        Get the list of plugins with pending operations.
        """
        return self.client._get("api/plugins/pending")

    def uninstall_plugin(self, key):
        """
        Uninstalls the plugin.
        :param key: Plugin key
        """
        params = {"key": key}
        return self.client._post("api/plugins/uninstall", params=params)

    def update_plugin(self, key):
        """
        Updates a plugin.
        :param key: Plugin key
        """
        params = {"key": key}
        return self.client._post("api/plugins/update", params=params)

    def get_plugin_updates(self):
        """
        Lists plugins with available updates.
        """
        return self.client._get("api/plugins/updates")
