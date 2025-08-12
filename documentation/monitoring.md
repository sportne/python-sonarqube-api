[Back to Index](index.md)

# Monitoring

### `GET api/monitoring/metrics`
*since 9.3*

Return monitoring metrics in Prometheus format. Support content type 'text/plain' (default) and 'application/openmetrics-text'. This endpoint can be accessed using a Bearer token, which needs to be defined in sonar.properties with the 'sonar.web.systemPasscode' key.
