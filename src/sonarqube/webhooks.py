class SonarQubeWebhooks:
    def __init__(self, client):
        self.client = client

    def create_webhook(self, name, url, project=None, secret=None):
        """
        Create a Webhook.
        :param name: Name displayed in the administration console of webhooks.
        :param url: Server endpoint that will receive the webhook payload.
        :param project: The key of the project that will own the webhook.
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value.
        """
        params = {"name": name, "url": url}
        if project:
            params["project"] = project
        if secret:
            params["secret"] = secret
        return self.client._post("api/webhooks/create", params=params)

    def delete_webhook(self, webhook):
        """
        Delete a Webhook.
        :param webhook: The key of the webhook to be deleted.
        """
        params = {"webhook": webhook}
        return self.client._post("api/webhooks/delete", params=params)

    def get_webhook_deliveries(self, p=None, ps=None, webhook=None):
        """
        Get the recent deliveries for a specified project or Compute Engine task.
        :param p: 1-based page number.
        :param ps: Page size.
        :param webhook: Key of the webhook that triggered those deliveries.
        """
        params = {}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if webhook:
            params["webhook"] = webhook
        return self.client._get("api/webhooks/deliveries", params=params)

    def get_webhook_delivery(self, deliveryId):
        """
        Get a webhook delivery by its id.
        :param deliveryId: Id of delivery.
        """
        params = {"deliveryId": deliveryId}
        return self.client._get("api/webhooks/delivery", params=params)

    def list_webhooks(self, project=None):
        """
        Search for global webhooks or project webhooks.
        :param project: Project key.
        """
        params = {}
        if project:
            params["project"] = project
        return self.client._get("api/webhooks/list", params=params)

    def update_webhook(self, name, url, webhook, secret=None):
        """
        Update a Webhook.
        :param name: new name of the webhook.
        :param url: new url to be called by the webhook.
        :param webhook: The key of the webhook to be updated.
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value.
        """
        params = {"name": name, "url": url, "webhook": webhook}
        if secret:
            params["secret"] = secret
        return self.client._post("api/webhooks/update", params=params)
