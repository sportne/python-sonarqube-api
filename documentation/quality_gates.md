[Back to Index](index.md)

# Quality Gates

### `POST api/qualitygates/add_group`
*since 9.2*

Allow a group of users to edit a Quality Gate. Requires 'Administer Quality Gates' or edit right on the specified quality gate.

**Parameters**
- `id` or `name` (required): Quality gate id or name.
- `groupId` or `groupName` (required): Group id or name.

---

### `POST api/qualitygates/add_user`
*since 9.2*

Allow a user to edit a Quality Gate. Requires 'Administer Quality Gates' or edit right on the specified quality gate.

**Parameters**
- `id` or `name` (required): Quality gate id or name.
- `login` (required): User login.

---

### `GET api/qualitygates/application_status`
*internal since 2.0*

Get the quality gate status of an application. Requires 'Browse' on the specified application and its child projects.

**Parameters**
- `application` (required): Application key.

---

### `POST api/qualitygates/copy`
*since 4.3*

Copy a Quality Gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `sourceName` (required): Source quality gate name.
- `name` (required): New quality gate name.

---

### `POST api/qualitygates/create`
*since 4.3*

Create a Quality Gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `name` (required): Quality gate name.

---

### `POST api/qualitygates/create_condition`
*since 4.3*

Add a new condition to a quality gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `gateName` (required): Quality gate name.
- `metric` (required): Metric key.
- `error` (required): Error threshold.
- `op` (optional): Operator.

---

### `POST api/qualitygates/delete_condition`
*since 4.3*

Delete a condition from a quality gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `id` (required): Condition ID.

---

### `POST api/qualitygates/deselect`
*since 4.3*

Remove the association of a project from a quality gate. Requires 'Administer Quality Gates' or 'Administer' rights on the project.

**Parameters**
- `projectId` or `projectKey` (required): Project id or key.

---

### `POST api/qualitygates/destroy`
*since 4.3*

Delete a Quality Gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `name` (required): Quality gate name.

---

### `GET api/qualitygates/get_by_project`
*since 6.1*

Get the quality gate of a project. Requires 'Browse' on the project.

**Parameters**
- `project` (required): Project key.

---

### `GET api/qualitygates/list`
*since 4.3*

Get a list of quality gates.

---

### `GET api/qualitygates/project_status`
*since 5.3*

Get the quality gate status of a project or a Compute Engine task.

**Parameters**
- `analysisId`, `projectId`, or `projectKey` (required).

---

### `POST api/qualitygates/remove_group`
*since 9.2*

Remove the ability from a group to edit a Quality Gate.

**Parameters**
- `id` or `name` (required): Quality gate id or name.
- `groupId` or `groupName` (required): Group id or name.

---

### `POST api/qualitygates/remove_user`
*since 9.2*

Remove the ability from a user to edit a Quality Gate.

**Parameters**
- `id` or `name` (required): Quality gate id or name.
- `login` (required): User login.

---

### `POST api/qualitygates/rename`
*since 4.3*

Rename a Quality Gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `currentName` (required): Current name.
- `name` (required): New name.

---

### `GET api/qualitygates/search`
*since 4.3*

Search for projects associated (or not) to a quality gate.

**Parameters**
- `gateId` (required): Quality gate ID.
- `q` (optional): Query string.
- `p`, `ps` (optional): Pagination.

---

### `GET api/qualitygates/search_groups`
*since 9.2*

List the groups that are allowed to edit a Quality Gate.

**Parameters**
- `id` or `name` (required): Quality gate id or name.
- `q` (optional): Query string.
- `p`, `ps` (optional): Pagination.

---

### `GET api/qualitygates/search_users`
*since 9.2*

List the users that are allowed to edit a Quality Gate.

**Parameters**
- `id` or `name` (required): Quality gate id or name.
- `q` (optional): Query string.
- `p`, `ps` (optional): Pagination.

---

### `POST api/qualitygates/select`
*since 4.3*

Associate a project to a quality gate. Requires 'Administer' right on the project.

**Parameters**
- `gateId` (required): Quality gate ID.
- `projectId` or `projectKey` (required): Project id or key.

---

### `POST api/qualitygates/set_ai_code_assurance`
*internal since 10.8*

Qualify or disqualify a custom Quality Gate as AI Code Assured. Requires 'Administer Quality Gates' permission.

**Parameters**
- `gateId` (required): Quality gate ID.
- `isAiPowered` (required): Boolean value.

---

### `POST api/qualitygates/set_as_default`
*since 4.3*

Set a quality gate as the default quality gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `name` (required): Quality gate name.

---

### `GET api/qualitygates/show`
*since 4.3*

Display the details of a quality gate.

**Parameters**
- `name` (required): Quality gate name.

---

### `POST api/qualitygates/update_condition`
*since 4.3*

Update a condition attached to a quality gate. Requires 'Administer Quality Gates' permission.

**Parameters**
- `id` (required): Condition ID.
- `metric` (required): Metric key.
- `error` (required): Error threshold.
- `op` (optional): Operator.
