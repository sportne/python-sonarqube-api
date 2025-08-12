[Back to Index](index.md)

# Applications

### `POST api/applications/add_project`
*since 7.3*

Add a project to an application. Requires 'Administrator' permission on the application.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `project` (required): Project keys. To set several values, the parameter must be called once for each value. Example: `project=firstProjectKey&project=secondProjectKey&project=thirdProjectKey`

---

### `POST api/applications/create`
*since 7.3*

Create a new application. Requires 'Administer System' permission or 'Create Applications' permission.

**Parameters**
- `name` (required): New application name.
- `key` (optional): Application key.
- `visibility` (optional): Application visibility.
- `description` (optional): Application description.

**Response Example**
```json
{
  "application": {
    "key": "my-app",
    "name": "My App",
    "description": "This is my new application",
    "visibility": "public",
    "projects": []
  }
}
```

**Changelog**
- 8.3: `description` and `key` parameters added.

---

### `POST api/applications/create_branch`
*since 7.3*

Create a new branch on a given application. Requires 'Administrator' permission on the application and 'Browse' permission on its child projects.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `branch` (required): Branch name. Example: `branch-2.0`
- `project` (required): Project keys. To set several values, the parameter must be called once for each value. Example: `project=firstProjectKey&project=secondProjectKey`
- `projectBranch` (required): Project branches. To set main branch, provide an empty value. To set several values, the parameter must be called once for each value. Example: `projectBranch=&projectBranch=branch-2.0`

---

### `POST api/applications/delete`
*since 7.3*

Delete an application definition. Requires 'Administrator' permission on the application.

**Parameters**
- `application` (required): Application key. Example: `my_application`

---

### `POST api/applications/delete_branch`
*since 7.3*

Delete a branch on a given application. Requires 'Administrator' permission on the application.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `branch` (required): Branch name. Example: `branch-2.0`

---

### `POST api/applications/refresh`
*internal since 8.6*

Refresh one or all applications. When a key is not specified, all applications are refreshed. Requires one of the following permissions:
- 'Administer System' when key is not specified
- 'Administer' rights on the specified application when key is specified

**Parameters**
- `key` (optional): Application key.

---

### `POST api/applications/remove_project`
*since 7.3*

Remove a project from an application. Requires 'Administrator' permission on the application.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `project` (required): Project key. Example: `my_project`

---

### `GET api/applications/search_projects`
*internal since 7.3*

List projects manually selected in an application. Requires 'Administrator' permission on the application.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `q` (optional): Limit search to project names that contain the supplied string.
- `p` (optional): 1-based page number. Default: 1
- `ps` (optional): Page size. Must be greater than 0 and less than or equal to 500. Default: 100

**Response Example**
```json
{
  "paging": {
    "pageIndex": 1,
    "pageSize": 100,
    "total": 1
  },
  "projects": [
    {
      "key": "my_project",
      "name": "My Project",
      "qualifier": "TRK",
      "visibility": "public"
    }
  ]
}
```

**Changelog**
- 7.4: `q` parameter added.

---

### `POST api/applications/set_tags`
*since 8.3*

Set tags on a application. Requires the following permission: 'Administer' rights on the specified application.

**Parameters**
- `application` (required): Application key.
- `tags` (required): Comma-separated list of tags.

---

### `GET api/applications/show`
*since 7.3*

Returns an application and its associated projects. Requires the 'Browse' permission on the application and on its child projects.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `branch` (optional): Branch name.

**Response Example**
```json
{
  "application": {
    "key": "my-app",
    "name": "My App",
    "description": "This is my application",
    "visibility": "public",
    "projects": [
      {
        "key": "my_project",
        "name": "My Project",
        "qualifier": "TRK",
        "visibility": "public"
      }
    ],
    "branches": [
      {
        "name": "master",
        "isMain": true,
        "status": {
          "qualityGateStatus": "OK"
        }
      }
    ]
  }
}
```

**Changelog**
- 7.4: `branch` parameter added.

---

### `GET api/applications/show_leak`
*internal since 7.3*

Show leak of an application. Requires the 'Browse' permission on the application and on its child projects.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `branch` (optional): Branch name.
- `pullRequest` (optional): Pull request ID.

**Response Example**
```json
{
  "leak": {
    "period": {
      "mode": "previous_version",
      "date": "2017-07-14T15:03:33+0200",
      "parameter": "1.0"
    },
    "measures": [
      {
        "metric": "new_bugs",
        "value": "10"
      }
    ]
  }
}
```

---

### `POST api/applications/update`
*since 7.3*

Update an application. Requires 'Administrator' permission on the application.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `name` (optional): New application name.
- `description` (optional): New application description.

---

### `POST api/applications/update_branch`
*since 7.3*

Update a branch on a given application. Requires 'Administrator' permission on the application and 'Browse' permission on its child projects.

**Parameters**
- `application` (required): Application key. Example: `my_application`
- `branch` (required): Branch name. Example: `branch-2.0`
- `name` (required): New branch name. Maximum length 255
- `project` (required): Project keys. To set several values, the parameter must be called once for each value. Example: `project=firstProjectKey&project=secondProjectKey&project=thirdProjectKey`
- `projectBranch` (required): Project branches. To set main branch, provide an empty value. To set several values, the parameter must be called once for each value. Example: `projectBranch=&projectBranch=branch-2.0&projectBranch=branch-2.1`
