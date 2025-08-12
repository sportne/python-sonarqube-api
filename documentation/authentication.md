[Back to Index](index.md)

# Authentication

### `POST api/authentication/login`
*since 6.0*

Authenticate a user.

**Parameters**
- `login` (required): Login of the user.
- `password` (required): Password of the user.

---

### `POST api/authentication/logout`
*since 6.3*

Logout a user.

---

### `GET api/authentication/validate`
*since 3.3*

Check credentials.

**Response Example**
```json
{"valid": true}
```
