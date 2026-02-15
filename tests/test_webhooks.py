import unittest
from unittest.mock import patch

from src.sonarqube import SonarQube


class TestSonarQubeWebhooks(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarQube(host="http://localhost:9000", token="test_token")

    def test_create_webhook(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.webhooks.create_webhook(
                name="my-webhook", url="http://my-webhook-listener.com/sonar"
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/webhooks/create",
                params={
                    "name": "my-webhook",
                    "url": "http://my-webhook-listener.com/sonar",
                },
            )

    def test_delete_webhook(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.webhooks.delete_webhook(webhook="my-webhook-key")
            mock_post.assert_called_with(
                "http://localhost:9000/api/webhooks/delete",
                params={"webhook": "my-webhook-key"},
            )

    def test_get_webhook_deliveries(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.webhooks.get_webhook_deliveries(webhook="my-webhook-key")
            mock_get.assert_called_with(
                "http://localhost:9000/api/webhooks/deliveries",
                params={"webhook": "my-webhook-key"},
            )

    def test_get_webhook_delivery(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.webhooks.get_webhook_delivery(deliveryId="my-delivery-id")
            mock_get.assert_called_with(
                "http://localhost:9000/api/webhooks/delivery",
                params={"deliveryId": "my-delivery-id"},
            )

    def test_list_webhooks(self):
        with patch.object(self.sonar.session, "get") as mock_get:
            self.sonar.webhooks.list_webhooks(project="my-project")
            mock_get.assert_called_with(
                "http://localhost:9000/api/webhooks/list",
                params={"project": "my-project"},
            )

    def test_update_webhook(self):
        with patch.object(self.sonar.session, "post") as mock_post:
            self.sonar.webhooks.update_webhook(
                name="new-name",
                url="http://new-url.com/sonar",
                webhook="my-webhook-key",
            )
            mock_post.assert_called_with(
                "http://localhost:9000/api/webhooks/update",
                params={
                    "name": "new-name",
                    "url": "http://new-url.com/sonar",
                    "webhook": "my-webhook-key",
                },
            )
