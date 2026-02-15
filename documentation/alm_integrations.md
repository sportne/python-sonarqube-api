[Back to Index](index.md)

# ALM Integrations

### `GET api/alm_integrations/list_azure_projects`
*since 8.6*

List Azure projects. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key

---

### `GET api/alm_integrations/list_bitbucketserver_projects`
*since 8.2*

List the Bitbucket Server projects. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key

---

### `GET api/alm_integrations/search_azure_repos`
*since 8.6*

Search the Azure DevOps repositories. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `projectName` (optional): Project name filter
- `searchQuery` (optional): Search query filter

---

### `GET api/alm_integrations/search_bitbucketcloud_repos`
*since 9.0*

Search the Bitbucket Cloud repositories. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key

---

### `GET api/alm_integrations/search_bitbucketserver_repos`
*since 8.2*

Search the Bitbucket Server repositories. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `projectName` (optional): Project name filter
- `searchQuery` (optional): Search query filter

---

### `GET api/alm_integrations/search_gitlab_repos`
*since 8.5*

Search the GitLab repositories. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `projectName` (optional): Project name filter

---

### `POST api/alm_integrations/import_github_project`
*since 8.4*

Import a GitHub project to SonarQube. Requires the 'Create Projects' permission.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `organization` (required): GitHub organization
- `repository` (required): GitHub repository name

---

### `POST api/alm_integrations/set_pat`
*since 8.2*

Set a Personal Access Token for the given DevOps Platform setting.

**Parameters**
- `almSetting` (required): DevOps Platform setting key
- `pat` (required): Personal Access Token
- `username` (optional): Username (required for Bitbucket Server)
