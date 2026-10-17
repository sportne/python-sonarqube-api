[Back to Index](index.md)

# ALM Settings

## Instance settings management

The following public endpoints are available through `sonar.alm_settings`.
They require **Administer System** permission and return the underlying
`requests.Response`, including server validation and permission errors.
Parameter names match the SonarQube API, including camelCase names.

The contracts below were checked against the official
[SonarQube Community Build 26.10.0.133078 action definitions](https://github.com/SonarSource/sonarqube/tree/26.10.0.133078/server/sonar-webserver-webapi/src/main/java/org/sonar/server/almsettings/ws).
Endpoint availability and behavior depend on the target version and edition.

| Python method | Endpoint | Required parameters | Optional parameters |
| --- | --- | --- | --- |
| `count_binding` | `GET api/alm_settings/count_binding` | `almSetting` | — |
| `create_azure` | `POST api/alm_settings/create_azure` | `key`, `personalAccessToken`, `url` | — |
| `create_bitbucket` | `POST api/alm_settings/create_bitbucket` | `key`, `url`, `personalAccessToken` | — |
| `create_bitbucketcloud` | `POST api/alm_settings/create_bitbucketcloud` | `key`, `workspace`, `clientId`, `clientSecret` | — |
| `create_github` | `POST api/alm_settings/create_github` | `key`, `url`, `appId`, `privateKey`, `clientId`, `clientSecret` | `webhookSecret` |
| `create_gitlab` | `POST api/alm_settings/create_gitlab` | `key`, `url`, `personalAccessToken` | — |
| `delete_setting` | `POST api/alm_settings/delete` | `key` | — |
| `update_azure` | `POST api/alm_settings/update_azure` | `key`, `url` | `newKey`, `personalAccessToken` |
| `update_bitbucket` | `POST api/alm_settings/update_bitbucket` | `key`, `url` | `newKey`, `personalAccessToken` |
| `update_bitbucketcloud` | `POST api/alm_settings/update_bitbucketcloud` | `key`, `workspace`, `clientId` | `newKey`, `clientSecret` |
| `update_github` | `POST api/alm_settings/update_github` | `key`, `url`, `appId`, `clientId` | `newKey`, `privateKey`, `clientSecret`, `webhookSecret` |
| `update_gitlab` | `POST api/alm_settings/update_gitlab` | `key`, `url` | `newKey`, `personalAccessToken` |
| `validate` | `GET api/alm_settings/validate` | `key` | — |

- `key` identifies an instance setting; `newKey` renames it. Binding counts use
  the API's `almSetting` parameter instead. The count response contains `key`
  and `projects`.
- `url` is the provider's API URL. Azure requires an absolute HTTP(S) URL.
  `workspace` is the Bitbucket Cloud workspace ID, and `appId` identifies a GitHub App.
- Update methods keep existing tokens, private keys, and client secrets when
  their optional arguments are `None` or empty strings. These arguments are omitted
  from the request. Non-secret fields listed as required must still be supplied.
- GitHub's `webhookSecret` is an exception on update: `None` preserves it,
  a nonempty string replaces it, and `""` clears it. Changing a GitHub setting's
  URL also requires supplying its `privateKey`.
- `delete_setting` removes an instance setting and its project bindings;
  `delete_binding` below removes only one project's binding.
- `validate` asks SonarQube to contact the configured provider and check its
  credentials and permissions. Successful create/update/delete/validate requests
  return HTTP 204. Creating an Azure setting can also contact Azure for validation.

Count, create, update, and delete actions were introduced in SonarQube 8.1,
except Bitbucket Cloud create/update (8.7). `validate` was introduced in 8.6.
Required Azure/GitLab URLs and optional update credentials reflect the current
contract rather than every historical server version. GitHub webhook secrets
require SonarQube 9.7 or newer.

```python
import os

from sonarqube import SonarQube

sonar = SonarQube(host=os.environ["SONARQUBE_HOST"], token=os.environ["SONARQUBE_TOKEN"])
settings = sonar.alm_settings
settings.create_gitlab(
    key="company-gitlab",
    url="https://gitlab.example.com/api/v4",
    personalAccessToken=os.environ["GITLAB_TOKEN"],
).raise_for_status()

# Rename while retaining the saved personal access token.
settings.update_gitlab(
    key="company-gitlab",
    newKey="engineering-gitlab",
    url="https://gitlab.example.com/api/v4",
).raise_for_status()

response = settings.count_binding(almSetting="engineering-gitlab")
response.raise_for_status()
print(response.json()["projects"])
```

## Project bindings and discovery

### `POST api/alm_settings/delete_binding`
*since 8.1*

Delete the DevOps Platform binding of a project.

**Parameters**
- `project` (required): Project key

---

### `GET api/alm_settings/get_binding`
*since 8.1*

Get DevOps Platform binding of a given project.

**Parameters**
- `project` (required): Project key

---

### `GET api/alm_settings/list`
*since 8.1*

List DevOps Platform settings available for a given project.

**Parameters**
- `project` (optional): Project key

---

### `GET api/alm_settings/list_definitions`
*since 8.1*

List DevOps Platform setting definitions. Requires 'Administer System' permission.

---

### `POST api/alm_settings/set_azure_binding`
*since 8.1*

Bind a project to an Azure DevOps Platform setting.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `project` (required): Project key
- `projectName` (optional): Azure project name
- `repositoryName` (optional): Azure repository name
- `monorepo` (optional): Is this project part of a monorepo

---

### `POST api/alm_settings/set_bitbucket_binding`
*since 8.1*

Bind a project to a Bitbucket Platform setting.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `project` (required): Project key
- `repository` (required): Bitbucket repository key
- `slug` (optional): Bitbucket repository slug
- `monorepo` (optional): Is this project part of a monorepo

---

### `POST api/alm_settings/set_github_binding`
*since 8.1*

Bind a project to a GitHub DevOps Platform setting.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `project` (required): Project key
- `repository` (required): GitHub repository identifier
- `monorepo` (optional): Is this project part of a monorepo

---

### `POST api/alm_settings/set_gitlab_binding`
*since 8.1*

Bind a project to a GitLab DevOps Platform setting.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `project` (required): Project key
- `repository` (optional): GitLab repository identifier
- `monorepo` (optional): Is this project part of a monorepo
