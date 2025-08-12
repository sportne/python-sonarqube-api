[Back to Index](index.md)

# Hotspots

### `POST api/hotspots/add_comment`
*internal since 8.1*

Add a comment to a Security Hotspot. Requires authentication and the following permission: 'Browse' on the project of the specified Security Hotspot.

**Parameters**
- `hotspot` (required): Hotspot key.
- `text` (required): Comment text.

---

### `POST api/hotspots/assign`
*internal since 8.2*

Assign a hotspot to an active user. Requires authentication and Browse permission on project.

**Parameters**
- `hotspot` (required): Hotspot key.
- `assignee` (optional): User login.

---

### `POST api/hotspots/change_status`
*since 8.1*

Change the status of a Security Hotspot. Requires the 'Administer Security Hotspot' permission.

**Parameters**
- `hotspot` (required): Hotspot key.
- `status` (required): The new status.
- `resolution` (optional): The resolution if the new status is 'REVIEWED'.

---

### `POST api/hotspots/delete_comment`
*internal since 8.2*

Delete comment from Security Hotspot. Requires authentication and the following permission: 'Browse' on the project of the specified Security Hotspot.

**Parameters**
- `comment` (required): Comment key.

---

### `POST api/hotspots/edit_comment`
*internal since 8.2*

Edit a comment. Requires authentication and the following permission: 'Browse' on the project of the specified hotspot.

**Parameters**
- `comment` (required): Comment key.
- `text` (required): New comment text.

---

### `GET api/hotspots/list`
*internal since 10.2*

List Security Hotspots. This endpoint is used in degraded mode, when issue indexing is running. Total number of Security Hotspots will be always equal to a page size, as counting all issues is not supported. Requires the 'Browse' permission on the specified project.

**Parameters**
- `project` (required): Project key.
- `p` (optional): 1-based page number. Default: 1
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default: 100

---

### `GET api/hotspots/pull`
*internal since 10.1*

This endpoint fetches and returns all (unless filtered by optional params) the hotspots for a given branch. The hotspots returned are not paginated, so the response size can be big. Requires project 'Browse' permission.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request key.

---

### `GET api/hotspots/search`
*since 8.1*

Search for Security Hotspots. Requires the 'Browse' permission on the specified project(s). For applications, it also requires 'Browse' permission on its child projects. When issue indexing is in progress returns 503 service unavailable HTTP code.

**Parameters**
- `projectKey` (required): Project key.
- `p` (optional): 1-based page number. Default: 1
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default: 100

---

### `GET api/hotspots/show`
*since 8.1*

Provides the details of a Security Hotspot.

**Parameters**
- `hotspot` (required): Key of the Security Hotspot. Example: `AU-TpxcA-iU5OvuD2FL0`

**Response Example**
```json
{
  "key": "AXgS1J6d4EDsXN2a_gN5",
  "component": {
    "key": "my-project-key",
    "name": "My Project",
    "qualifier": "TRK"
  },
  "project": "my-project-key",
  "rule": {
    "key": "security:S2076",
    "name": "Cross-site scripting (XSS)",
    "description": "..."
  },
  "status": "TO_REVIEW",
  "line": 10,
  "message": "...",
  "assignee": "admin",
  "author": "john.doe@example.com",
  "creationDate": "2020-07-20T10:00:00+0200",
  "updateDate": "2020-07-20T10:00:00+0200",
  "comments": [
    {
      "key": "AXgS1J6d4EDsXN2a_gN6",
      "login": "admin",
      "htmlText": "This is a comment",
      "createdAt": "2020-07-20T10:00:00+0200",
      "updatable": true
    }
  ],
  "changelog": [
    {
      "user": "admin",
      "creationDate": "2020-07-20T10:00:00+0200",
      "diffs": [
        {
          "key": "status",
          "newValue": "TO_REVIEW"
        }
      ]
    }
  ]
}
```
