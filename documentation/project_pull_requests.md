[Back to Index](index.md)

# Project Pull Requests

### `POST api/project_pull_requests/delete`
*since 7.1*

Delete a pull request. Requires 'Administer' rights on the specified project.

**Parameters**
- `project` (required): Project key.
- `pullRequest` (required): Pull request key.

---

### `GET api/project_pull_requests/list`
*since 7.1*

List the pull requests of a project. One of the following permissions is required: 'Browse' rights on the specified project or 'Execute Analysis' rights on the specified project.

**Parameters**
- `project` (required): Project key.
