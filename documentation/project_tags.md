[Back to Index](index.md)

# Project Tags

### `GET api/project_tags/search`
*since 6.4*

Search tags.

**Parameters**
- `q` (optional): Query string.
- `ps` (optional): Page size.

---

### `POST api/project_tags/set`
*since 6.4*

Set tags on a project. Requires 'Administer' rights on the specified project.

**Parameters**
- `project` (required): Project key.
- `tags` (required): Comma-separated list of tags.
