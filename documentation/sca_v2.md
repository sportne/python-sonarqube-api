[Back to Index](index.md)

# SCA V2

### `GET /api/v2/sca/risk-reports`

Get a report for all the current SCA dependency risks for a given component and branch. Returns list of all risks for a given component and branch. CSV format is available by setting `Accept: text/csv` in your request headers.

**Query Parameters**
- `component` (string, required): Key of the component (project, application, portfolio) to build report for.
- `branch` (string, optional): Key of the branch to build report for.
- `riskType` (string, optional): Type of risk to filter the report by. If not provided, all risks types are included. Valid values: VULNERABILITY, PROHIBITED_LICENSE.

**Response**
```json
[
  {
    "projectKey": "string",
    "projectName": "string",
    "branchKey": "string",
    "riskTitle": "string",
    "riskType": "Enum (string): VULNERABILITY, PROHIBITED_LICENSE",
    "riskSeverity": "Enum (string): INFO, LOW, MEDIUM, HIGH, BLOCKER",
    "riskStatus": "Enum (string): OPEN, ACCEPT, CONFIRM, SAFE, FIXED",
    "statusChanges": [
      {
        "comment": "string",
        "newStatus": "string",
        "createdAt": "string"
      }
    ],
    "vulnerabilityId": "string",
    "cvssScore": "number",
    "cweIds": [
      "string"
    ],
    "publishedOn": "string",
    "createdAt": "string",
    "packageUrl": "string",
    "riskUrl": "string",
    "dependencyChains": [
      [
        "string"
      ]
    ]
  }
]
```

---

### `GET /api/v2/sca/sbom-reports`

Get a software bill of materials (SBOM) report. Return a report based on the dependencies in this component's branch, using the type parameter and Accept header to select the report to generate. Right now, the available reports have specialized MIME types that go along with those formats: * CycloneDX: https://cyclonedx.org/specification/overview/ * JSON & XML * SPDX 2.3: https://spdx.github.io/spdx-spec/v2.3/ * JSON & XML

**Query Parameters**
- `component` (string, required): Key of the component (project, application, portfolio) to build report for.
- `branch` (string, optional): Key of the branch to build report for.
- `type` (string, required): Type of report to generate. The `Accept` header sent by the client determines the format of the report. Currently supported: cyclonedx (application/vnd.cyclonedx+json), cyclonedx (application/vnd.cyclonedx+xml), spdx_23 (application/spdx+json), spdx_23 (application/spdx+xml). Valid values: cyclonedx, spdx_23.
