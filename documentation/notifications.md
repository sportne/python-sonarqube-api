[Back to Index](index.md)

# Notifications

### `POST api/notifications/add`
*since 6.3*

Add a notification for the authenticated user. Requires one of the following permissions:
- Authentication if no login is provided. If a project is provided, requires the 'Browse' permission on the specified project.
- System administration if a login is provided. If a project is provided, requires the 'Browse' permission on the specified project.

**Parameters**
- `login` (optional): User login.
- `project` (optional): Project key.
- `type` (required): Notification type.
- `channel` (optional): Channel.

---

### `GET api/notifications/list`
*since 6.3*

List notifications of the authenticated user. Requires one of the following permissions:
- Authentication if no login is provided
- System administration if a login is provided

**Parameters**
- `login` (optional): User login.

**Response Example**
```json
{
  "notifications": [
    {
      "channel": "EmailNotificationChannel",
      "type": "SQ-MyNewIssues",
      "project": "my_project"
    }
  ]
}
```

---

### `POST api/notifications/remove`
*since 6.3*

Remove a notification for the authenticated user. Requires one of the following permissions:
- Authentication if no login is provided
- System administration if a login is provided

**Parameters**
- `login` (optional): User login.
- `project` (optional): Project key.
- `type` (required): Notification type.
- `channel` (optional): Channel.
