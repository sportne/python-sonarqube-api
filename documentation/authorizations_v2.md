[Back to Index](index.md)

# Authorizations V2

The `SonarQubeAuthorizationsV2` client exposes helpers for managing groups and
their memberships through the `/api/v2/authorizations` endpoints.

### `POST /api/v2/authorizations/group-memberships`

Add a user to a group.

**Request Body**

- `userId` (string, optional): ID of the user to add to the group.
- `groupId` (string, optional): ID of the group that should receive the
  member.

---

### `GET /api/v2/authorizations/group-memberships`

Retrieve memberships matching the supplied filters.

**Query Parameters**

- `userId` (string, optional): Limit the results to memberships for this user.
- `groupId` (string, optional): Limit the results to memberships of this group.
- `pageSize` (integer, optional): Number of results per page. Maximum 500,
  minimum 0, default 50. Setting `0` returns only pagination metadata.
- `pageIndex` (integer, optional): 1-based page index. Minimum 1, default 1.

---

### `DELETE /api/v2/authorizations/group-memberships/{id}`

Remove a user from a group.

**Path Parameters**

- `id` (string, required): Identifier of the membership to delete.

---

### `POST /api/v2/authorizations/groups`

Create a new group.

**Request Body**

- `name` (string, required): Group name. Must be unique. Maximum length 255,
  minimum 1. The reserved name `anyone` cannot be used.
- `description` (string, optional): Group description. Maximum length 200.

---

### `GET /api/v2/authorizations/groups`

List groups.

**Query Parameters**

- `managed` (boolean, optional): Filter by managed status. Only available on
  managed instances.
- `q` (string, optional): Case-insensitive substring filter on the group
  name.
- `userId` (string, optional): Only return groups that contain this user. Using
  `!=` searches for groups without the user (administrator only).
- `pageSize` (integer, optional): Number of results per page. Maximum 500,
  minimum 0, default 50. Setting `0` returns only pagination metadata.
- `pageIndex` (integer, optional): 1-based page index. Minimum 1, default 1.

---

### `GET /api/v2/authorizations/groups/{id}`

Fetch a single group.

**Path Parameters**

- `id` (string, required): Identifier of the group to fetch.

---

### `PATCH /api/v2/authorizations/groups/{id}`

Update a group's metadata.

**Path Parameters**

- `id` (string, required): Identifier of the group to update.

**Request Body**

- `name` (string, optional): New group name. Maximum length 255, minimum 1.
- `description` (string, optional): New group description. Maximum length 200.

---

### `DELETE /api/v2/authorizations/groups/{id}`

Delete a group.

**Path Parameters**

- `id` (string, required): Identifier of the group to delete.
