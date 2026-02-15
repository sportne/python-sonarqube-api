class SonarQubeAuditLogs:
    def __init__(self, client):
        self.client = client

    def download(self, **kwargs):
        """
        Download security related audit log entries in JSON format.
        Requires 'Administer System' permission.
        :param kwargs: Additional parameters (e.g., from, to as ISO dates)
        """
        return self.client._get("api/audit_logs/download", params=kwargs)
