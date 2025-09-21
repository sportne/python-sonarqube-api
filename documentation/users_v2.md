[Back to Index](index.md)

# Users V2

### `POST /api/v2/users-management/users`

Create a user. If a deactivated user account exists with the given login, it will be reactivated. Requires Administer System permission.

**Request Body**
- `email` (string, optional): User email. Max: 100, Min: 1.
- `local` (boolean, optional): Specify if the user should be authenticated from SonarQube server or from an external authentication system. Password should not be set when local is set to false. Default: true.
- `login` (string, required): User login. Max: 100, Min: 2.
- `name` (string, required): User name. Max: 200, Min: 0.
- `password` (string, optional): User password. Only mandatory when creating local user, otherwise it should not be set.
- `scmAccounts` (array of strings, optional): List of SCM accounts.

**Response**
```json
{
  "id": "string",
  "login": "string",
  "name": "string",
  "email": "string",
  "active": "boolean",
  "local": "boolean",
  "managed": "boolean",
  "externalLogin": "string",
  "externalProvider": "string",
  "externalId": "string",
  "avatar": "string",
  "sonarQubeLastConnectionDate": "string",
  "sonarLintLastConnectionDate": "string",
  "scmAccounts": [
    "string"
  ]
}
```

---

### `GET /api/v2/users-management/users`

Get a list of users. By default, only active users are returned. The following fields are only returned when user has Administer System permission or for logged-in in user : 'email', 'externalIdentity', 'externalProvider', 'groups', 'lastConnectionDate', 'sonarLintLastConnectionDate', 'tokensCount'. Field 'sonarqubeLastConnectionDate' is only updated every hour, so it may not be accurate, for instance when a user authenticates many times in less than one hour. The results are sorted alphabetically by login.

**Query Parameters**
- `active` (boolean, optional): Return active/inactive users. Default: true.
- `managed` (boolean, optional): Return managed or non-managed users. Only available for managed instances, throws for non-managed instances.
- `q` (string, optional): Filter on login, name and email. This parameter performs a partial match (contains), it is case insensitive.
- `externalIdentity` (string, optional): Filter on externalIdentity. This parameter perform a case-sensitive exact match.
- `sonarQubeLastConnectionDateFrom` (string, optional): Filter users based on the last connection date field. Only users who interacted with this instance at or after the date will be returned. The format must be ISO 8601 datetime format (YYYY-MM-DDThh:mm:ss±hhmm). Example: 2020-01-01T00:00:00+0100.
- `sonarQubeLastConnectionDateTo` (string, optional): Filter users based on the last connection date field. Only users that never connected or who interacted with this instance at or before the date will be returned. The format must be ISO 8601 datetime format (YYYY-MM-DDThh:mm:ss±hhmm). Example: 2020-01-01T00:00:00+0100.
- `sonarLintLastConnectionDateFrom` (string, optional): Filter users based on the SonarLint last connection date field Only users who interacted with this instance using SonarLint at or after the date will be returned. The format must be ISO 8601 datetime format (YYYY-MM-DDThh:mm:ss±hhmm). Example: 2020-01-01T00:00:00+0100.
- `sonarLintLastConnectionDateTo` (string, optional): Filter users based on the SonarLint last connection date field. Only users that never connected or who interacted with this instance using SonarLint at or before the date will be returned. The format must be ISO 8601 datetime format (YYYY-MM-DDThh:mm:ss±hhmm). Example: 2020-01-01T00:00:00+0100.
- `groupId` (string, optional): Filter users belonging to group. Only available for system administrators. Using != operator will exclude users from this group.
- `pageSize` (integer, optional): Number of results per page. A value of 0 will only return the pagination information. Max: 500, Min: 0, Default: 50.
- `pageIndex` (integer, optional): 1-based page index. Min: 1, Default: 1.

**Response**
```json
{
  "users": [
    {
      "id": "string",
      "login": "string",
      "name": "string",
      "email": "string",
      "active": "boolean",
      "local": "boolean",
      "managed": "boolean",
      "externalLogin": "string",
      "externalProvider": "string",
      "externalId": "string",
      "avatar": "string",
      "sonarQubeLastConnectionDate": "string",
      "sonarLintLastConnectionDate": "string",
      "scmAccounts": [
        "string"
      ]
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

### `GET /api/v2/users-management/users/{id}`

Fetch a single user. The following fields are only returned when user has Administer System permission or for logged-in in user : 'email' 'externalIdentity' 'externalProvider' 'groups' 'lastConnectionDate' 'sonarLintLastConnectionDate' 'tokensCount' Field 'sonarqubeLastConnectionDate' is only updated every hour, so it may not be accurate, for instance when a user authenticates many times in less than one hour.

**Path Parameters**
- `id` (string, required): The id of the user to fetch.

**Response**
```json
{
  "id": "string",
  "login": "string",
  "name": "string",
  "email": "string",
  "active": "boolean",
  "local": "boolean",
  "managed": "boolean",
  "externalLogin": "string",
  "externalProvider": "string",
  "externalId": "string",
  "avatar": "string",
  "sonarQubeLastConnectionDate": "string",
  "sonarLintLastConnectionDate": "string",
  "scmAccounts": [
    "string"
  ]
}
```

---

### `PATCH /api/v2/users-management/users/{id}`

Update users attributes.

**Path Parameters**
- `id` (string, required): The id of the user to update.

**Request Body**
- `login` (object, optional):
    - `value` (string)
    - `defined` (boolean)
- `name` (string, optional): User first name and last name. Max: 200, Min: 0.
- `email` (string, optional): Email. Max: 100, Min: 1.
- `scmAccounts` (object, optional):
    - `value` (array of strings)
    - `defined` (boolean)
- `externalProvider` (string, optional): New identity provider. Only providers configured in your platform are supported. This could be: github, gitlab, bitbucket, saml, LDAP, LDAP_{serverKey} (according to your server configuration file). Warning: when this is updated, the user will only be able to authenticate using the new identity provider. Also, it is not possible to remove the identity provider of a user.
- `externalLogin` (string, optional): New external login, usually the login used in the authentication system. Max: 255, Min: 1.
- `externalId` (string, optional): New external id in the authentication system. Max: 255, Min: 1.

**Response**
```json
{
  "id": "string",
  "login": "string",
  "name": "string",
  "email": "string",
  "active": "boolean",
  "local": "boolean",
  "managed": "boolean",
  "externalLogin": "string",
  "externalProvider": "string",
  "externalId": "string",
  "avatar": "string",
  "sonarQubeLastConnectionDate": "string",
  "sonarLintLastConnectionDate": "string",
  "scmAccounts": [
    "string"
  ]
}
```

---

### `DELETE /api/v2/users-management/users/{id}`

Deactivates a user. Requires Administer System permission.

**Path Parameters**
- `id` (string, required): The ID of the user to delete.

**Query Parameters**
- `anonymize` (boolean, optional): Anonymize user in addition to deactivating it. Default: false.
