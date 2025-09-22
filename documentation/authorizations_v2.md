[Back to Index](index.md)

# Authorizations V2

### `POST /api/v2/authorizations/group-memberships`
Add a user to a group.

**Parameters**
- `userId` (optional): ID of the user to add to group.
- `groupId` (optional): ID of the group where a member needs to be added.

---

### `GET /api/v2/authorizations/group-memberships`
Get the list of groups and members matching the query.

**Parameters**
- `q` (optional): Limit search to names that contain the supplied string.
- `groupId` (optional): The id of the group to filter for.
- `userId` (optional): The id of the user to filter for.
- `pageSize` (optional): The number of results to return.
- `page` (optional): The page of results to return.

---

### `DELETE /api/v2/authorizations/group-memberships/{member_id}`
Remove a user from a group.

**Parameters**
- `member_id` (required): The ID of the group membership to delete.

---

### `POST /api/v2/authorizations/groups`
Create a new group.

**Parameters**
- `name` (required): Name for the new group.
- `description` (optional): Description for the new group.

---

### `GET /api/v2/authorizations/groups`
Get the list of groups.

**Parameters**
- `q` (optional): Limit search to names that contain the supplied string.
- `organization` (optional): The key of the organization to filter for.
- `pageSize` (optional): The number of results to return.
- `page` (optional): The page of results to return.

---

### `GET /api/v2/authorizations/groups/{group_id}`
Fetch a single group.

**Parameters**
- `group_id` (required): The id of the group to fetch.

---

### `PATCH /api/v2/authorizations/groups/{group_id}`
Update a group name or description.

**Parameters**
- `group_id` (required): The id of the group to update.
- `name` (optional): The new name for the group.
- `description` (optional): The new description for the group.

---

### `DELETE /api/v2/authorizations/groups/{group_id}`
Deletes a group.

**Parameters**
- `group_id` (required): The ID of the group to delete.
