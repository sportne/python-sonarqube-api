[Back to Index](index.md)

# ALM Settings

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
