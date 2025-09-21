[Back to Index](index.md)

# Permissions V2

### `POST /api/v2/authorizations/group-memberships`

Add a user to a group.

**Request Body**
- `userId` (string, optional): ID of the user to add to group.
- `groupId` (string, optional): ID of the group where a member needs to be added.

**Response**
```json
{
  "id": "string",
  "groupId": "string",
  "userId": "string"
}
```

---

### `GET /api/v2/authorizations/group-memberships`

Get the list of groups and members matching the query.

**Query Parameters**
- `userId` (string, optional): ID of the user for which to search groups. If not set, all groups are returned.
- `groupId` (string, optional): ID of the group for which to search members. If not set, all groups are returned.
- `pageSize` (integer, optional): Number of results per page. A value of 0 will only return the pagination information. Max: 500, Min: 0, Default: 50.
- `pageIndex` (integer, optional): 1-based page index. Min: 1, Default: 1.

**Response**
```json
{
  "groupMemberships": [
    {
      "id": "string",
      "groupId": "string",
      "userId": "string"
    }
  ],
  "page": {
    "pageIndex": "integer (int32)",
    "pageSize": "integer (int32)",
    "total": "integer (int32)"
  }
}
```

---

### `DELETE /api/v2/authorizations/group-memberships/{id}`

Remove a user from a group.

**Path Parameters**
- `id` (string, required): The ID of the group membership to delete.

---

### `POST /api/v2/authorizations/groups`

Create a new group.

**Request Body**
- `name` (string, required): Name for the new group. Must be unique. The value 'anyone' is reserved and cannot be used. Max: 255, Min: 1.
- `description` (string, optional): Description for the new group. Max: 200, Min: 0.

**Response**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "managed": "boolean",
  "default": "boolean"
}
```

---

### `GET /api/v2/authorizations/groups`

Get the list of groups. The results are sorted alphabetically by group name.

**Query Parameters**
- `managed` (boolean, optional): Return managed or non-managed groups. Only available for managed instances, throws for non-managed instances.
- `q` (string, optional): Filter on name. This parameter performs a partial match (contains), it is case insensitive.
- `userId` (string, optional): Filter groups containing the user. Only available for system administrators. Using != operator will search for groups without the user.
- `pageSize` (integer, optional): Number of results per page. A value of 0 will only return the pagination information. Max: 500, Min: 0, Default: 50.
- `pageIndex` (integer, optional): 1-based page index. Min: 1, Default: 1.

**Response**
```json
{
  "groups": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "managed": "boolean",
      "default": "boolean"
    }
  ],
  "page": {
    "pageIndex": "integer (int32)",
    "pageSize": "integer (int32)",
    "total": "integer (int32)"
  }
}
```

---

### `GET /api/v2/authorizations/groups/{id}`

Fetch a single group.

**Path Parameters**
- `id` (string, required): The id of the group to fetch.

**Response**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "managed": "boolean",
  "default": "boolean"
}
```

---

### `PATCH /api/v2/authorizations/groups/{id}`

Update a group name or description.

**Path Parameters**
- `id` (string, required): The id of the group to update.

**Request Body**
- `name` (string, optional): Group name. Max: 255, Min: 1.
- `description` (string, optional): Description of the group. Max: 200, Min: 0.

**Response**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "managed": "boolean",
  "default": "boolean"
}
```

---

### `DELETE /api/v2/authorizations/groups/{id}`

Deletes a group.

**Path Parameters**
- `id` (string, required): The ID of the group to delete.
