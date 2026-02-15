def test_list_metrics(sonarqube_client):
    response = sonarqube_client.metrics.search_metrics()
    assert response.status_code == 200
    metrics = response.json().get("metrics", [])
    assert len(metrics) > 0
    # Check for some standard metrics
    metric_keys = [m["key"] for m in metrics]
    assert "ncloc" in metric_keys
    assert "complexity" in metric_keys
    assert "violations" in metric_keys
