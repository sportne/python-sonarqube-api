[Back to Index](index.md)

# System V2

### `GET /api/v2/system/health`

**Headers**
- `X-Sonar-Passcode` (string, optional)

**Response**
```json
{
  "status": "Enum (string): GREEN, YELLOW, RED",
  "causes": [
    "string"
  ]
}
```

---

### `GET /api/v2/system/liveness`

Provide liveness of SonarQube, meant to be used as a liveness probe on Kubernetes.
Require 'Administer System' permission or authentication with passcode. When SonarQube is fully started, liveness check for database connectivity, Compute Engine status, and, except for DataCenter Edition, if ElasticSearch is Green or Yellow. When SonarQube is on Safe Mode (for example when a database migration is running), liveness check only for database connectivity.

**Headers**
- `X-Sonar-Passcode` (string, optional): Passcode can be provided, see SonarQube documentation.

---

### `GET /api/v2/system/migrations-status`

Return the detailed status of ongoing database migrations including starting date. If no migration is ongoing or needed it is still possible to call this endpoint and receive appropriate information.

**Response**
```json
{
  "status": "string",
  "completedSteps": "integer (int32)",
  "totalSteps": "integer (int32)",
  "startedAt": "string",
  "message": "string",
  "expectedFinishTimestamp": "string"
}
```
