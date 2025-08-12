[Back to Index](index.md)

# Project Branches

### `POST api/project_branches/delete`
*since 6.6*

Delete a non-main branch of a project or application. Requires 'Administer' rights on the specified project or application.

**Parameters**
- `project` (required): Project key.
- `branch` (required): Branch name.

---

### `GET api/project_branches/get_ai_code_assurance`
*internal since 2025.1*

Gets whether a project passed as parameter is AI Code Assured or not. Requires 'Browse' permission on the specified project if it is private.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.

---

### `GET api/project_branches/list`
*since 6.6*

List the branches of a project or application. Requires 'Browse' or 'Execute analysis' rights on the specified project or application.

**Parameters**
- `project` (required): Project key.

---

### `POST api/project_branches/rename`
*since 6.6*

Rename the main branch of a project or application. Requires 'Administer' permission on the specified project or application.

**Parameters**
- `project` (required): Project key.
- `name` (required): New name for the main branch.

---

### `POST api/project_branches/set_automatic_deletion_protection`
*since 8.1*

Protect a specific branch from automatic deletion. Protection can't be disabled for the main branch. Requires 'Administer' permission on the specified project or application.

**Parameters**
- `project` (required): Project key.
- `branch` (required): Branch name.
- `protect` (required): Boolean value to enable/disable protection.

---

### `POST api/project_branches/set_main`
*since 10.2*

Allow to set a new main branch. Caution, only applicable on projects. Requires 'Administer' rights on the specified project or application.

**Parameters**
- `project` (required): Project key.
- `branch` (required): Branch key.
