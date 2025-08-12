[Back to Index](index.md)

# Issues

### `POST api/issues/add_comment`
*since 3.6*

Add a comment. Requires authentication and the following permission: 'Browse' on the project of the specified issue.

**Parameters**
- `issue` (required): Issue key.
- `text` (required): Comment text.

**Response Example**
```json
{
  "issue": { ... },
  "comment": { ... }
}
```

---

### `POST api/issues/anticipated_transitions`
*internal since 10.2*

Receive a list of anticipated transitions that can be applied to not yet discovered issues on a specific project. Requires the following permission: 'Administer Issues' on the specified project. Only falsepositive, wontfix and accept transitions are supported. Upon successful execution, the HTTP status code returned is 202 (Accepted).

**Parameters**
- `project` (required): Project key.
- `issues` (required): List of issues.

---

### `POST api/issues/assign`
*since 3.6*

Assign/Unassign an issue. Requires authentication and Browse permission on project.

**Parameters**
- `issue` (required): Issue key.
- `assignee` (optional): User login.

---

### `GET api/issues/authors`
*since 5.1*

Search SCM accounts which match a given query. Requires authentication. When issue indexing is in progress returns 503 service unavailable HTTP code.

**Parameters**
- `q` (optional): Query.
- `ps` (optional): Page size. Default: 100
- `project` (optional): Project key.

**Response Example**
```json
{
  "authors": ["john.doe@example.com"]
}
```

---

### `POST api/issues/bulk_change`
*since 3.7*

Bulk change on issues. Up to 500 issues can be updated. Requires authentication.

**Parameters**
- `issues` (required): Comma-separated list of issue keys.
- `...` (other parameters for changes)

---

### `GET api/issues/changelog`
*since 4.1*

Display changelog of an issue. Requires the 'Browse' permission on the project of the specified issue.

**Parameters**
- `issue` (required): Issue key.

**Response Example**
```json
{
  "changelog": [ ... ]
}
```

---

### `GET api/issues/component_tags`
*internal since 5.1*

List tags for the issues under a given component (including issues on the descendants of the component) When issue indexing is in progress returns 503 service unavailable HTTP code.

**Parameters**
- `component` (required): Component key.
- `q` (optional): Query string.

**Response Example**
```json
{
  "tags": ["security", "bug"]
}
```

---

### `POST api/issues/delete_comment`
*since 3.6*

Delete a comment. Requires authentication and the following permission: 'Browse' on the project of the specified issue.

**Parameters**
- `comment` (required): Comment key.

---

### `POST api/issues/do_transition`
*since 3.6*

Do workflow transition on an issue. Requires authentication and Browse permission on project. The transitions 'accept', 'wontfix' and 'falsepositive' require the permission 'Administer Issues'. The transitions involving security hotspots require the permission 'Administer Security Hotspot'.

**Parameters**
- `issue` (required): Issue key.
- `transition` (required): Transition.

---

### `POST api/issues/edit_comment`
*since 3.6*

Edit a comment. Requires authentication and the following permission: 'Browse' on the project of the specified issue.

**Parameters**
- `comment` (required): Comment key.
- `text` (required): New text.

---

### `GET api/issues/gitlab_sast_export`
*since 10.2*

Return a list of vulnerabilities according to the Gitlab SAST JSON format. The JSON produced can be used in GitLab for generating the Vulnerability Report.Requires the 'Browse' or 'Scan' permission on the specified project.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request key.

---

### `GET api/issues/list`
*internal since 10.2*

List issues. This endpoint is used in degraded mode, when issue indexing is running. Either 'project' or 'component' parameter is required. Total number of issues will be always equal to a page size, as this counting all issues is not supported. Requires the 'Browse' permission on the specified project.

**Parameters**
- `project` or `component` (required): Project or component key.
- `p` (optional): Page number.
- `ps` (optional): Page size.

---

### `GET api/issues/pull`
*internal since 9.5*

This endpoint fetches and returns all (unless filtered by optional params) the issues for a given branch. The issues returned are not paginated, so the response size can be big. Requires project 'Browse' permission.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request key.

---

### `GET api/issues/pull_taint`
*internal since 9.6*

This endpoint fetches and returns all (unless filtered by optional params) the taint vulnerabilities for a given branch. The taint vulnerabilities returned are not paginated, so the response size can be big. Requires project 'Browse' permission.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request key.

---

### `POST api/issues/reindex`
*since 9.8*

Reindex issues for a project. Require 'Administer System' permission.

**Parameters**
- `projectKey` (required): Project key.

---

### `GET api/issues/search`
*since 3.6*

Search for issues. Requires the 'Browse' permission on the specified project(s). For applications, it also requires 'Browse' permission on its child projects. When issue indexing is in progress returns 503 service unavailable HTTP code.

**Parameters**
- `...` (many filter parameters)

---

### `POST api/issues/set_severity`
*since 3.6*

Change severity. Requires the following permissions: 'Authentication', 'Browse' rights on project of the specified issue, 'Administer Issues' rights on project of the specified issue.

**Parameters**
- `issue` (required): Issue key.
- `severity` (required): New severity.

---

### `POST api/issues/set_tags`
*since 5.1*

Set tags on an issue. Requires authentication and Browse permission on project.

**Parameters**
- `issue` (required): Issue key.
- `tags` (optional): Comma-separated list of tags.

---

### `GET api/issues/tags`
*since 5.1*

List tags matching a given query.

**Parameters**
- `q` (optional): Query string.
- `ps` (optional): Page size.
- `project` (optional): Project key.
- `branch` (optional): Branch key.
- `all` (optional): Search all tags or only in main branch.

**Response Example**
```json
{
  "tags": ["security", "bug"]
}
```
