[Back to Index](index.md)

# Measures

### `GET api/measures/component`
*since 5.4*

Return component with specified measures. Requires one of the following permissions:
- 'Browse' on the project of the specified component
- 'Execute Analysis' on the project of the specified component

**Parameters**
- `component` (required): Component key. Example: `my_project`
- `metricKeys` (required): Comma-separated list of metric keys. Example: `ncloc,coverage`
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request ID.

**Response Example**
```json
{
  "component": {
    "key": "my_project",
    "name": "My Project",
    "qualifier": "TRK",
    "measures": [
      {
        "metric": "ncloc",
        "value": "1000"
      },
      {
        "metric": "coverage",
        "value": "80.0"
      }
    ]
  }
}
```

---

### `GET api/measures/component_tree`
*since 5.4*

Navigate through components based on the chosen strategy with specified measures. Requires the following permission: 'Browse' on the specified project. For applications, it also requires 'Browse' permission on its child projects. When limiting search with the q parameter, directories are not returned.

**Parameters**
- `component` (required): Component key.
- `metricKeys` (required): Comma-separated list of metric keys.
- `p` (optional): Page number.
- `ps` (optional): Page size.
- `q` (optional): Query string.
- `s` (optional): Sort fields.
- `strategy` (optional): Traversal strategy.

**Response Example**
```json
{
  "paging": { ... },
  "baseComponent": { ... },
  "components": [ ... ]
}
```

---

### `GET api/measures/search`
*internal since 6.2*

Search for project measures ordered by project names. At most 100 projects can be provided. Returns the projects with the 'Browse' permission.

**Parameters**
- `projectKeys` (required): Comma-separated list of project keys.
- `metricKeys` (required): Comma-separated list of metric keys.

---

### `GET api/measures/search_history`
*since 6.3*

Search measures history of a component. Measures are ordered chronologically. Pagination applies to the number of measures for each metric. Requires the following permission: 'Browse' on the specified component. For applications, it also requires 'Browse' permission on its child projects.

**Parameters**
- `component` (required): Component key.
- `metrics` (required): Comma-separated list of metric keys.
- `p` (optional): Page number.
- `ps` (optional): Page size.
- `from` (optional): From date.
- `to` (optional): To date.
- `branch` (optional): Branch key.
- `pullRequest` (optional): Pull request ID.

**Response Example**
```json
{
  "paging": { ... },
  "measures": [
    {
      "metric": "ncloc",
      "history": [
        { "date": "2017-10-19T13:00:00+0200", "value": "100" },
        { "date": "2017-10-20T13:00:00+0200", "value": "110" }
      ]
    }
  ]
}
```
