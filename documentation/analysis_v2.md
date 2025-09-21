[Back to Index](index.md)

# Analysis V2

### `GET /api/v2/analysis/active_rules`

Used by the scanner-engine to get all active rules for a given project.

**Query Parameters**
- `projectKey` (string, required): Project Key.

**Response**
```json
[
  {
    "ruleKey": {
      "repository": "string",
      "rule": "string"
    },
    "name": "string",
    "severity": "string",
    "createdAt": "string",
    "updatedAt": "string",
    "internalKey": "string",
    "language": "string",
    "templateRuleKey": "string",
    "qProfileKey": "string",
    "deprecatedKeys": [
      {
        "repository": "string",
        "rule": "string"
      }
    ],
    "params": [
      {
        "key": "string",
        "value": "string"
      }
    ],
    "impacts": {}
  }
]
```

---

### `GET /api/v2/analysis/engine`

This endpoint return the Scanner Engine metadata by default. To download the Scanner Engine, set the Accept header of the request to 'application/octet-stream'.

---

### `GET /api/v2/analysis/jres`

Get metadata of all available JREs.

**Query Parameters**
- `os` (string, optional): Filter the JRE by operating system. Accepted values are 'windows', 'linux', 'macos', 'alpine' (case-insensitive), with some aliases.
- `arch` (string, optional): Filter the JRE by CPU architecture. Accepted values are 'x64' and 'aarch64' (case-insensitive), with some aliases.

**Response**
```json
[
  {
    "id": "string",
    "filename": "string",
    "sha256": "string",
    "javaPath": "string",
    "os": "string",
    "arch": "string"
  }
]
```

---

### `GET /api/v2/analysis/jres/{id}`

This endpoint return the JRE metadata by default. To download the JRE binary asset, set the Accept header of the request to 'application/octet-stream'.

**Path Parameters**
- `id` (string, required): The ID of the JRE.

---

### `GET /api/v2/analysis/version`

Get the version of the Scanner Engine.
