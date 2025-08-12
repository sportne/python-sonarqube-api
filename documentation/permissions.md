[Back to Index](index.md)

# Permissions

### `POST api/permissions/add_group`
*since 5.2*

Add a permission to a group. This service defaults to global permissions, but can be limited to project permissions by providing project id or project key. The group name must be provided. Requires one of the following permissions: 'Administer System' or 'Administer' rights on the specified project.

**Parameters**
- `groupName` (required): Group name.
- `permission` (required): Permission.
- `projectId` or `projectKey` (optional): Project context.

---

### `POST api/permissions/add_group_to_template`
*since 5.2*

Add a group to a permission template. The group name must be provided. Requires 'Administer System' permission.

**Parameters**
- `groupName` (required): Group name.
- `templateName` or `templateId` (required): Template context.
- `permission` (required): Permission.

---

### `POST api/permissions/add_project_creator_to_template`
*since 6.0*

Add a project creator to a permission template. Requires 'Administer System' permission.

**Parameters**
- `templateName` or `templateId` (required): Template context.
- `permission` (required): Permission.

---

### `POST api/permissions/add_user`
*since 5.2*

Add permission to a user. This service defaults to global permissions, but can be limited to project permissions by providing project id or project key. Requires one of the following permissions: 'Administer System' or 'Administer' rights on the specified project.

**Parameters**
- `login` (required): User login.
- `permission` (required): Permission.
- `projectId` or `projectKey` (optional): Project context.

---

### `POST api/permissions/add_user_to_template`
*since 5.2*

Add a user to a permission template. Requires 'Administer System' permission.

**Parameters**
- `login` (required): User login.
- `templateName` or `templateId` (required): Template context.
- `permission` (required): Permission.

---

### `POST api/permissions/apply_template`
*since 5.2*

Apply a permission template to one project. Requires 'Administer System' permission.

**Parameters**
- `templateName` or `templateId` (required): Template context.
- `projectId` or `projectKey` (required): Project context.

---

### `POST api/permissions/bulk_apply_template`
*since 5.5*

Apply a permission template to several components. Managed projects will be ignored. Requires 'Administer System' permission.

**Parameters**
- `templateName` or `templateId` (required): Template context.
- `projects` or `q` (optional): Projects to apply template to.

---

### `POST api/permissions/create_template`
*since 5.2*

Create a permission template. Requires 'Administer System' permission.

**Parameters**
- `name` (required): Template name.
- `description` (optional): Template description.
- `projectKeyPattern` (optional): Project key pattern.

---

### `POST api/permissions/delete_template`
*since 5.2*

Delete a permission template. Requires 'Administer System' permission.

**Parameters**
- `templateName` or `templateId` (required): Template context.

---

### `GET api/permissions/groups`
*internal since 5.2*

Lists the groups with their permissions.

**Parameters**
- `q` (optional): Query string.
- `permission` (optional): Filter by permission.
- `projectId` or `projectKey` (optional): Project context.
- `p`, `ps` (optional): Pagination.

---

### `POST api/permissions/remove_group`
*since 5.2*

Remove a permission from a group.

**Parameters**
- `groupName` (required): Group name.
- `permission` (required): Permission.
- `projectId` or `projectKey` (optional): Project context.

---

### `POST api/permissions/remove_group_from_template`
*since 5.2*

Remove a group from a permission template.

**Parameters**
- `groupName` (required): Group name.
- `templateName` or `templateId` (required): Template context.
- `permission` (required): Permission.

---

### `POST api/permissions/remove_project_creator_from_template`
*since 6.0*

Remove a project creator from a permission template.

**Parameters**
- `templateName` or `templateId` (required): Template context.
- `permission` (required): Permission.

---

### `POST api/permissions/remove_user`
*since 5.2*

Remove permission from a user.

**Parameters**
- `login` (required): User login.
- `permission` (required): Permission.
- `projectId` or `projectKey` (optional): Project context.

---

### `POST api/permissions/remove_user_from_template`
*since 5.2*

Remove a user from a permission template.

**Parameters**
- `login` (required): User login.
- `templateName` or `templateId` (required): Template context.
- `permission` (required): Permission.

---

### `GET api/permissions/search_templates`
*since 5.2*

List permission templates. Requires 'Administer System' permission.

**Parameters**
- `q` (optional): Query string.

---

### `POST api/permissions/set_default_template`
*since 5.2*

Set a permission template as default. Requires 'Administer System' permission.

**Parameters**
- `templateName` or `templateId` (required): Template context.

---

### `GET api/permissions/template_groups`
*internal since 5.2*

Lists the groups with their permission on a template.

**Parameters**
- `templateName` or `templateId` (required): Template context.
- `q` (optional): Query string.
- `p`, `ps` (optional): Pagination.

---

### `GET api/permissions/template_users`
*internal since 5.2*

Lists the users with their permission on a template.

**Parameters**
- `templateName` or `templateId` (required): Template context.
- `q` (optional): Query string.
- `p`, `ps` (optional): Pagination.

---

### `POST api/permissions/update_template`
*since 5.2*

Update a permission template. Requires 'Administer System' permission.

**Parameters**
- `id` (required): Template ID.
- `name` (optional): New name.
- `description` (optional): New description.
- `projectKeyPattern` (optional): New project key pattern.

---

### `GET api/permissions/users`
*internal since 5.2*

Lists the users with their permissions.

**Parameters**
- `q` (optional): Query string.
- `permission` (optional): Filter by permission.
- `projectId` or `projectKey` (optional): Project context.
- `p`, `ps` (optional): Pagination.
