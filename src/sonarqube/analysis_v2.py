class SonarQubeAnalysisV2:
    def __init__(self, client):
        self.client = client

    def get_active_rules(self, projectKey):
        """
        Get all active rules for a given project.
        :param projectKey: Project Key.
        """
        params = {"projectKey": projectKey}
        return self.client._get("api/v2/analysis/active_rules", params=params)

    def get_scanner_engine(self):
        """
        Get the Scanner Engine metadata.
        """
        return self.client._get("api/v2/analysis/engine")

    def list_jres(self, os=None, arch=None):
        """
        Get metadata of all available JREs.
        :param os: Filter the JRE by operating system.
        :param arch: Filter the JRE by CPU architecture.
        """
        params = {}
        if os:
            params["os"] = os
        if arch:
            params["arch"] = arch
        return self.client._get("api/v2/analysis/jres", params=params)

    def get_jre(self, jre_id):
        """
        Get the JRE metadata.
        :param jre_id: The ID of the JRE.
        """
        return self.client._get(f"api/v2/analysis/jres/{jre_id}")

    def get_scanner_engine_version(self):
        """
        Get the version of the Scanner Engine.
        """
        return self.client._get("api/v2/analysis/version")
