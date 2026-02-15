def test_webhook_lifecycle(sonarqube_client):
    webhook_name = "test-webhook-integration"
    webhook_url = "http://example.com/webhook"

    # Create
    response = sonarqube_client.webhooks.create_webhook(
        name=webhook_name, url=webhook_url
    )
    assert response.status_code == 200
    webhook = response.json().get("webhook", {})
    webhook_key = webhook.get("key")
    assert webhook_key is not None

    # List
    response = sonarqube_client.webhooks.list_webhooks()
    assert response.status_code == 200
    webhooks = response.json().get("webhooks", [])
    assert any(w["key"] == webhook_key for w in webhooks)

    # Delete
    response = sonarqube_client.webhooks.delete_webhook(webhook=webhook_key)
    assert response.status_code == 204

    # Verify Deletion
    response = sonarqube_client.webhooks.list_webhooks()
    webhooks = response.json().get("webhooks", [])
    assert not any(w["key"] == webhook_key for w in webhooks)
