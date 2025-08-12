[Back to Index](index.md)

# Project Links

### `POST api/project_links/create`
*since 6.1*

Create a new project link. Requires 'Administer' permission on the specified project, or global 'Administer' permission.

**Parameters**
- `projectId` (required): Project Id.
- `name` (required): Link name.
- `url` (required): Link URL.

---

### `POST api/project_links/delete`
*since 6.1*

Delete existing project link. Requires 'Administer' permission on the specified project, or global 'Administer' permission.

**Parameters**
- `id` (required): Link ID.

---

### `GET api/project_links/search`
*since 6.1*

List links of a project. The 'projectId' or 'projectKey' must be provided. Requires one of the following permissions: 'Administer System', 'Administer' rights on the specified project, or 'Browse' on the specified project.

**Parameters**
- `projectId` or `projectKey` (required): Project context.
