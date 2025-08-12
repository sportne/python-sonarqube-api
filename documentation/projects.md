[Back to Index](index.md)

# Projects

### `POST api/projects/bulk_delete`
*since 5.2*

Delete one or several projects. Requires 'Administer System' permission.

**Parameters**
- `analyzedBefore` (optional): Delete projects analyzed before this date.
- `projects` (optional): Comma-separated list of project keys.
- `q` (optional): Query string to filter projects.

---

### `POST api/projects/create`
*since 4.0*

Create a project. Requires 'Create Projects' permission.

**Parameters**
- `name` (required): Project name.
- `project` (required): Project key.
- `visibility` (optional): `private` or `public`.

---

### `POST api/projects/delete`
*since 5.2*

Delete a project. Requires 'Administer System' permission or 'Administer' permission on the project.

**Parameters**
- `project` (required): Project key.

---

### `GET api/projects/export_findings`
*since 9.1*

Export all findings (issues and hotspots) of a specific project branch. Requires 'Administer System' permission.

**Parameters**
- `project` (required): Project key.
- `branch` or `pullRequest` (optional): Branch or pull request key.

---

### `GET api/projects/get_contains_ai_code`
*since 2025.1*

Get whether a project contains AI code or not.

**Parameters**
- `projectKey` (required): Project key.

---

### `GET api/projects/get_detected_ai_code`
*internal since 2025.1*

Get detected AI code.

**Parameters**
- `projectKey` (required): Project key.
- `branch` or `pullRequest` (optional): Branch or pull request key.

---

### `GET api/projects/license_usage`
*since 9.4*

Help admins to understand how much each project affects the total number of lines of code. Requires Administer System permission.

---

### `GET api/projects/search`
*since 6.3*

Search for projects or views to administrate them. Requires 'Administer System' permission.

**Parameters**
- `...` (many filter parameters)

---

### `GET api/projects/search_my_projects`
*internal since 6.0*

Return list of projects for which the current user has 'Administer' permission.

---

### `GET api/projects/search_my_scannable_projects`
*internal since 9.5*

List projects that a user can scan.

---

### `POST api/projects/set_contains_ai_code`
*since 10.8*

Sets if the project passed as parameter contains or not AI code. Requires 'Administer' rights on the specified project.

**Parameters**
- `project` (required): Project key.
- `contains_ai_code` (required): Boolean value.

---

### `POST api/projects/update_default_visibility`
*internal since 6.4*

Update the default visibility for new projects. Requires System Administrator privileges.

**Parameters**
- `visibility` (required): `private` or `public`.

---

### `POST api/projects/update_key`
*since 6.1*

Update a project all its sub-components keys. Requires 'Administer' permission on the project.

**Parameters**
- `from` (required): Old project key.
- `to` (required): New project key.

---

### `POST api/projects/update_visibility`
*since 6.4*

Updates visibility of a project, application or a portfolio. Requires 'Project administer' permission on the specified entity.

**Parameters**
- `project` (required): Project, application or portfolio key.
- `visibility` (required): New visibility.
