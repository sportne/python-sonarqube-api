[Back to Index](index.md)

# Views

### `POST api/views/add_application`
*since 9.3*

Add an existing application to a portfolio.
Authentication is required for this API endpoint.

**Parameters**
- `application` (required): Key of the application to be added
- `portfolio` (required): Key of the portfolio where the application will be added

---

### `POST api/views/add_application_branch`
*since 9.3*

Add a branch of an application selected in a portfolio.
Requires 'Administrator' permission on the portfolio and 'Browse' permission for the application.

**Parameters**
- `application` (required): Key of the application. Example value: `my_app`
- `branch` (required): Key of the branch. Example value: `feature/my_branch`
- `key` (required): Key of the portfolio

---

### `POST api/views/add_portfolio`
*since 9.3*

Add an existing portfolio to the structure of another portfolio.
Authentication is required for this API endpoint.

**Parameters**
- `portfolio` (required): Key of the portfolio where a reference will be added
- `reference` (required): Key of the portfolio to be added

---

### `POST api/views/add_project`
*since 1.0*

Add a project to a portfolio.
Requires 'Administrator' permission on the portfolio and 'Browse' permission for adding project.

**Parameters**
- `key` (required): Key of the portfolio
- `project` (required): Key of the project. Example value: `my_project`

---

### `POST api/views/add_project_branch`
*since 9.2*

Add a branch of a project selected in a portfolio.
Requires 'Administrator' permission on the portfolio and 'Browse' permission for the project.

**Parameters**
- `branch` (required): Key of the branch. Example value: `feature/my_branch`
- `key` (required): Key of the portfolio
- `project` (required): Key of the project. Example value: `my_project`

---

### `GET api/views/applications`
*since 9.3*

List applications which the user has access to that can be added to a portfolio.
Authentication is required for this API endpoint

**Parameters**
- `portfolio` (required): Key of the would-be parent portfolio

---

### `POST api/views/create`
*since 1.0*

Create a new portfolio.
Requires 'Administer System' permission or 'Create Portfolios' permission,

**Parameters**
- `description` (optional): Description for the new portfolio, can be left blank. Maximum length: 256
- `key` (optional): Key for the new portfolio. A suitable key will be generated if not provided. Maximum length: 400
- `name` (required): Name for the new portfolio. Maximum length: 256
- `parent` (optional): Key of the parent portfolio, when creating a sub portfolio. Maximum length: 400
- `visibility` (optional): since 2.0, Whether the created portfolio or application should be visible to everyone, or only specific user/groups. Only applies to root portfolios. If no visibility is specified, the default visibility will be used. Possible values: `private`, `public`

---

### `POST api/views/delete`
*since 1.0*

Delete a portfolio definition.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `key` (required): Portfolio key

---

### `GET api/views/list`
*since 1.0*

List root portfolios.
Requires authentication. Only portfolios with the admin permission are returned.

**Response Example**
```json
{
  "views": [
    {
      "key": "apache-jakarta-commons",
      "name": "Apache Jakarta Commons",
      "qualifier": "VW",
      "visibility": "public"
    },
    {
      "key": "Languages",
      "name": "Languages",
      "qualifier": "VW",
      "visibility": "private"
    }
  ]
}
```

---

### `POST api/views/move`
*since 1.0*

Move a portfolio.
Authentication is required for this API endpoint.

**Parameters**
- `destination` (required): Key of the destination portfolio
- `key` (required): Key of the portfolio to move

---

### `GET api/views/move_options`
*since 1.0*

List possible portfolio destinations.
Authentication is required for this API endpoint.

**Parameters**
- `key` (required): Key of the portfolio to move

---

### `GET api/views/portfolios`
*since 9.3*

List portfolios that can be referenced.
Authentication is required for this API endpoint.

**Parameters**
- `portfolio` (required): Key of the would-be parent portfolio

---

### `GET api/views/projects`
*internal since 1.0*

List projects manually selected in a portfolio.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `key` (required): Portfolio key
- `p` (optional): Index of the page to display. Default value: 1
- `ps` (optional): Size for the paging to apply. Default value: 100
- `query` (optional): If specified, only projects whose key contain the query will be returned
- `selected` (optional): Depending on the value, show only selected items (selected=selected), deselected items (selected=deselected), or all items with their selection status (selected=all). Possible values: `all`, `deselected`, `selected`. Default value: `selected`

---

### `GET api/views/projects_status`
*internal since 9.3*

Return projects with a failed quality gate belonging to the provided portfolio hierarchy.

**Parameters**
- `p` (optional): 1-based page number. Default value: 1. Example value: 42
- `portfolio` (required): Portfolio key.
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default value: 20. Example value: 20. Maximum value: 500
- `status` (optional): Quality gate status to filter projects by. Possible values: `OK`, `ERROR`

---

### `POST api/views/refresh`
*internal since 7.1*

Refresh one or all of the portfolios.
When a key is not specified, all portfolios are refreshed.
Requires one of a following permissions:
- 'Administer System' when key is not specified
- 'Administer' rights on the specified portfolio when key is specified

**Parameters**
- `key` (optional): Key: Root portfolio key. If not specified, all portfolios are refreshed.

---

### `POST api/views/remove_application`
*since 9.3*

Remove an application from a portfolio.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `application` (required): Key of the application to be removed
- `portfolio` (required): Portfolio key

---

### `POST api/views/remove_application_branch`
*since 9.3*

Remove a branch of an application selected in a portfolio.
Requires 'Administrator' permission on the portfolio and 'Browse' permission for the application.

**Parameters**
- `application` (required): Key of the project. Example value: `my_app`
- `branch` (required): Key of the branch. Example value: `feature/my_branch`
- `key` (required): Key of the portfolio

---

### `POST api/views/remove_portfolio`
*since 9.3*

Remove a reference to a portfolio.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `portfolio` (required): Portfolio key
- `reference` (required): Key of the referenced portfolio to be removed

---

### `POST api/views/remove_project`
*since 1.0*

Remove a project from a portfolio.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `key` (required): Key of the portfolio
- `project` (required): Key of the project

---

### `POST api/views/remove_project_branch`
*since 9.2*

Remove a branch of a project selected in a portfolio.
Requires 'Administrator' permission on the portfolio and 'Browse' permission for the project.

**Parameters**
- `branch` (required): Key of the branch. Example value: `feature/my_branch`
- `key` (required): Key of the portfolio
- `project` (required): Key of the project. Example value: `my_project`

---

### `GET api/views/search`
*internal since 2.0*

Search for portfolios.

**Parameters**
- `onlyFavorites` (optional): To return only favorite portfolios. Possible values: `true`, `false`, `yes`, `no`. Default value: `false`
- `p` (optional): 1-based page number. Default value: 1. Example value: 42
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default value: 100. Example value: 20. Maximum value: 500
- `q` (optional): Limit search to names or keys that contain the supplied string. Example value: `sona`
- `qualifiers` (optional): since 7.2, To return only portfolios with specified qualifiers. Possible values: `VW`, `SVW`

---

### `POST api/views/set_manual_mode`
*since 7.4*

Set the projects selection mode of a portfolio on manual selection.
In order to add project, please use api/view/add_project.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `portfolio` (required): Key of the portfolio or sub-portfolio to update

---

### `POST api/views/set_none_mode`
*since 9.1*

Set the projects selection mode of a portfolio to none.
After setting this mode portfolio will not have any projects assigned.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `portfolio` (required): Key of the portfolio or sub-portfolio to update

---

### `POST api/views/set_regexp_mode`
*since 7.4*

Set the projects selection mode of a portfolio on regular expression.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `branch` (optional): Selects a branch in all matched projects, instead of using their main branches
- `portfolio` (required): Key of the portfolio or sub-portfolio to update
- `regexp` (required): A valid regexp with respect to the JDK's ``java.util.regex.Pattern`` class

---

### `POST api/views/set_remaining_projects_mode`
*since 7.4*

Set the projects selection mode of a portfolio on unassociated projects in hierarchy.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `branch` (optional): Selects a branch in all matched projects, instead of using their main branches
- `portfolio` (required): Key of the portfolio or sub-portfolio to update

---

### `POST api/views/set_tags_mode`
*since 7.4*

Set the projects selection mode of a portfolio on project tags.
Requires 'Administrator' permission on a portfolio.

**Parameters**
- `branch` (optional): Selects a branch in all matched projects, instead of using their main branches
- `portfolio` (required): Key of the portfolio or sub-portfolio to update
- `tags` (required): Comma-separated list of tags. It's not possible to set nothing.

---

### `GET api/views/show`
*since 1.0*

Show the details of a portfolio, including its hierarchy and project selection mode.
Authentication is required for this API endpoint.

**Parameters**
- `key` (required): The key of the portfolio

---

### `POST api/views/update`
*since 1.0*

Update a portfolio.
Requires 'Administrator' permission on the portfolio.

**Parameters**
- `description` (optional): New description for the portfolio. Maximum length: 256
- `key` (required): Key of the portfolio to update
- `name` (required): New name for the portfolio. Maximum length: 256
