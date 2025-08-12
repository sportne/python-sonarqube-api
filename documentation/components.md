[Back to Index](index.md)

# Components

### `GET api/components/app`
*internal since 4.4*

Coverage data required for rendering the component viewer. Either branch or pull request can be provided, not both. Requires the following permission: 'Browse'.

**Parameters**
- `component` (required): Component key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request ID.

**Response Example**
```json
{
  "measures": [],
  "coverage": {
    "by_line": [],
    "by_condition": []
  }
}
```

---

### `GET api/components/search`
*since 6.3*

Search for components.

**Parameters**
- `qualifiers` (required): Comma-separated list of component qualifiers.
- `q` (optional): Limit search to component names that contain the supplied string.
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
  "components": [
    {
      "organization": "my-org",
      "key": "my_project",
      "name": "My Project",
      "qualifier": "TRK",
      "visibility": "public",
      "lastAnalysisDate": "2017-04-04T13:30:05+0200",
      "revision": "e79c2363e79c2363e79c2363e79c2363e79c2363"
    }
  ]
}
```

---

### `GET api/components/search_projects`
*internal since 6.2*

Search for projects.

**Parameters**
- `q` (optional): Limit search to project names that contain the supplied string.
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
  "components": [
    {
      "organization": "my-org",
      "key": "my_project",
      "name": "My Project",
      "qualifier": "TRK",
      "visibility": "public",
      "lastAnalysisDate": "2017-04-04T13:30:05+0200",
      "revision": "e79c2363e79c2363e79c2363e79c2363e79c2363"
    }
  ]
}
```

---

### `GET api/components/show`
*since 5.4*

Returns a component (file, directory, project, portfolio…) and its ancestors. The ancestors are ordered from the parent to the root project. Requires the following permission: 'Browse' on the project of the specified component.

**Parameters**
- `component` (required): Component key.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request ID.

**Response Example**
```json
{
  "component": {
    "organization": "my-org",
    "key": "my_project:src/foo/Bar.php",
    "name": "Bar.php",
    "qualifier": "FIL",
    "path": "src/foo/Bar.php",
    "language": "php"
  },
  "ancestors": [
    {
      "organization": "my-org",
      "key": "my_project:src/foo",
      "name": "foo",
      "qualifier": "DIR",
      "path": "src/foo"
    },
    {
      "organization": "my-org",
      "key": "my_project",
      "name": "My Project",
      "qualifier": "TRK"
    }
  ]
}
```

---

### `GET api/components/suggestions`
*internal since 4.2*

Internal WS for the top-right search engine. The result will contain component search results, grouped by their qualifiers.

**Parameters**
- `q` (required): Query string.

**Response Example**
```json
{
  "results": [
    {
      "qualifier": "TRK",
      "results": [
        {
          "key": "my_project",
          "name": "My Project"
        }
      ]
    }
  ]
}
```

---

### `GET api/components/tree`
*since 5.4*

Navigate through components based on the chosen strategy. Requires the following permission: 'Browse' on the specified project. When limiting search with the q parameter, directories are not returned.

**Parameters**
- `component` (required): Base component key.
- `strategy` (optional): Strategy to search for descendants.
- `p` (optional): 1-based page number. Default: 1
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default: 100
- `q` (optional): Limit search to component names/keys.
- `qualifiers` (optional): Comma-separated list of component qualifiers.
- `s` (optional): Comma-separated list of sort fields.
- `asc` (optional): Ascending sort.

**Response Example**
```json
{
  "paging": {
    "pageIndex": 1,
    "pageSize": 100,
    "total": 1
  },
  "baseComponent": {
    "key": "my_project",
    "name": "My Project",
    "qualifier": "TRK"
  },
  "components": [
    {
      "key": "my_project:src/foo/Bar.php",
      "name": "Bar.php",
      "qualifier": "FIL",
      "path": "src/foo/Bar.php",
      "language": "php"
    }
  ]
}
```
