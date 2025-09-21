[Back to Index](index.md)

# DevOps Platform Translation V2

### `POST /api/v2/dop-translation/bound-projects`

Create a SonarQube project with the information from the provided DevOps platform project. Autoconfigure Pull-Request decoration mechanism. Requires the 'Create Projects' permission and setting a Personal Access Token with api/alm_integrations/set_pat for a user who will be using this endpoint.

**Request Body**
- `projectKey` (string, required): Key of the project to create. Min: 1.
- `projectName` (string, required): Name of the project to create. Min: 1.
- `devOpsPlatformSettingId` (string, required): Identifier of DevOps platform configuration to use. Use /dop-translation/dop-settings to retrieve the settings and their ID. Min: 1.
- `repositoryIdentifier` (string, required): Identifier of the DevOps platform repository to import:
  - repository slug for GitHub and Bitbucket (Cloud and Server)
  - repository id for GitLab
  - repository name for Azure DevOps
  Min: 1.
- `projectIdentifier` (string, optional): Identifier of the DevOps platform project in which the repository is located. This is only needed for Azure and BitBucket Server platforms.
- `newCodeDefinitionType` (string, optional): Project New Code Definition Type. New code definitions of the following types are allowed: PREVIOUS_VERSION, NUMBER_OF_DAYS, REFERENCE_BRANCH - will default to the main branch.
- `newCodeDefinitionValue` (string, optional): Project New Code Definition Value. For each new code definition type, a different value is expected:
  - no value, when the new code definition type is PREVIOUS_VERSION and REFERENCE_BRANCH
  - a number between 1 and 90, when the new code definition type is NUMBER_OF_DAYS
- `monorepo` (boolean, required): True if project is part of a mono repo.

**Response**
```json
{
  "projectId": "string",
  "bindingId": "string"
}
```

---

### `GET /api/v2/dop-translation/dop-settings`

List all DevOps Platform Integration settings. Requires the 'Create Projects' permission.

**Response**
```json
{
  "dopSettings": [
    {
      "id": "string",
      "type": "string",
      "key": "string",
      "url": "string",
      "appId": "string"
    }
  ],
  "page": {
    "pageIndex": "integer (int32)",
    "pageSize": "integer (int32)",
    "total": "integer (int32)"
  }
}
```
