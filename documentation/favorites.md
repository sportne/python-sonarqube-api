[Back to Index](index.md)

# Favorites

### `POST api/favorites/add`
*since 6.3*

Add a component (project, portfolio, etc.) as favorite for the authenticated user. Only 100 components by qualifier can be added as favorite. Requires authentication and the following permission: 'Browse' on the component.

**Parameters**
- `component` (required): Component key.

---

### `POST api/favorites/remove`
*since 6.3*

Remove a component (project, portfolio, application etc.) as favorite for the authenticated user. Requires authentication.

**Parameters**
- `component` (required): Component key.

---

### `GET api/favorites/search`
*since 6.3*

Search for the authenticated user favorites. Requires authentication.

**Parameters**
- `p` (optional): 1-based page number. Default: 1
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default: 100

**Response Example**
```json
{
  "paging": {
    "pageIndex": 1,
    "pageSize": 100,
    "total": 1
  },
  "favorites": [
    {
      "key": "my_project",
      "name": "My Project",
      "qualifier": "TRK",
      "lastAnalysisDate": "2017-04-04T13:30:05+0200"
    }
  ]
}
```
