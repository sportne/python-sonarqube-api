[Back to Index](index.md)

# Project Dump

### `POST api/project_dump/export`
*since 1.0*

Triggers project dump so that the project can be imported to another SonarQube server. Requires the 'Administer' permission.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull Request key.

---

### `POST api/project_dump/import`
*since 1.0*

Triggers the import of a project dump. Permission 'Administer' is required. This feature is provided by the Governance plugin.

**Parameters**
- `dump` (required): The dump file.

---

### `GET api/project_dump/status`
*internal since 1.0*

Provide the import and export status of a project. Permission 'Administer' is required.

**Parameters**
- `id` or `key` (required): Project id or key.
