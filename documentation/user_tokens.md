[Back to Index](index.md)

# User Tokens

### `POST api/user_tokens/generate`
*since 5.3*

Generate a user access token.
Please keep your tokens secret. They enable to authenticate and analyze projects.
It requires administration permissions to specify a 'login' and generate a token for another user. Otherwise, a token is generated for the current user.

**Parameters**
- `expirationDate` (optional): since 9.6, The expiration date of the token being generated, in ISO 8601 format (YYYY-MM-DD). If not set, default to no expiration.
- `login` (optional): User login. If not set, the token is generated for the authenticated user. Example value: `g.hopper`
- `name` (required): Token name. Example value: `Project scan on Travis`. Maximum length: 100
- `projectKey` (optional): since 9.5, The key of the only project that can be analyzed by the PROJECT_ANALYSIS_TOKEN being generated.
- `type` (optional): since 9.5, Token Type. If this parameters is set to PROJECT_ANALYSIS_TOKEN, it is necessary to provide the projectKey parameter too. Possible values: `USER_TOKEN`, `GLOBAL_ANALYSIS_TOKEN`, `PROJECT_ANALYSIS_TOKEN`. Default value: `USER_TOKEN`

---

### `POST api/user_tokens/revoke`
*since 5.3*

Revoke a user access token.
It requires administration permissions to specify a 'login' and revoke a token for another user. Otherwise, the token for the current user is revoked.

**Parameters**
- `login` (optional): User login. Example value: `g.hopper`
- `name` (required): Token name. Example value: `Project scan on Travis`

---

### `GET api/user_tokens/search`
*since 5.3*

List the access tokens of a user.
The login must exist and active.
Field 'lastConnectionDate' is only updated every hour, so it may not be accurate, for instance when a user is using a token many times in less than one hour.
It requires administration permissions to specify a 'login' and list the tokens of another user. Otherwise, tokens for the current user are listed.
Authentication is required for this API endpoint

**Parameters**
- `login` (optional): User login. Example value: `g.hopper`
