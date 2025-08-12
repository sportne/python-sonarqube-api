[Back to Index](index.md)

# New Code Periods

### `GET api/new_code_periods/list`
*since 8.0*

Lists the new code definition for all branches in a project. Requires the permission to browse the project.

**Parameters**
- `project` (required): Project key.

**Response Example**
```json
{
  "project": "my_project",
  "newCodePeriods": [
    {
      "branch": "master",
      "type": "previous_version",
      "value": "1.0"
    }
  ]
}
```

---

### `POST api/new_code_periods/set`
*since 8.0*

Updates the new code definition on different levels:
- Not providing a project key and a branch key will update the default value at global level.
- Existing projects or branches having a specific new code definition will not be impacted
- Project key must be provided to update the value for a project
- Both project and branch keys must be provided to update the value for a branch

Requires one of the following permissions:
- 'Administer System' to change the global setting
- 'Administer' rights on the specified project to change the project setting

**Parameters**
- `project` (optional): Project key.
- `branch` (optional): Branch key.
- `type` (required): New code period type.
- `value` (optional): New code period value.

---

### `GET api/new_code_periods/show`
*since 8.0*

Shows the new code definition. If the component requested doesn't exist or if no new code definition is set for it, a value is inherited from the project or from the global setting.Requires one of the following permissions if a component is specified:
- 'Administer' rights on the specified component
- 'Execute analysis' rights on the specified component

**Parameters**
- `project` (optional): Project key.
- `branch` (optional): Branch key.

**Response Example**
```json
{
  "type": "previous_version",
  "value": "1.0"
}
```

---

### `POST api/new_code_periods/unset`
*since 8.0*

Unsets the new code definition for a branch, project or global. It requires the inherited New Code Definition to be compatible with the Clean as You Code methodology, and one of the following permissions:
- 'Administer System' to change the global setting
- 'Administer' rights for a specified component

**Parameters**
- `project` (optional): Project key.
- `branch` (optional): Branch key.
