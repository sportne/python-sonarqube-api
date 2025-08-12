[Back to Index](index.md)

# Editions

### `POST api/editions/activate_grace_period`
*since 10.3*

Enable a license 7-days grace period if the Server ID is invalid. Require 'Administer System' permission.

---

### `GET api/editions/is_valid_license`
*internal since 7.3*

Return the validity of the license. Error message can be thrown under the following circumstances:
- "404 License not found" will be thrown if no license has been set.
- "404 Unknown URL : /api/editions/is_valid_license" will be thrown if the instance is under community edition
- "500 An error has occurred. Please contact your administrator" can be thrown when the license is corrupted. Additional details can be found in the logs.

**Response Example**
```json
{
  "valid": true
}
```

---

### `POST api/editions/set_license`
*since 7.2*

Set the license for enabling features of commercial editions. Require 'Administer System' permission.

**Parameters**
- `license` (required): License key.

---

### `GET api/editions/show_license`
*internal since 7.2*

Show information about currently installed license. Requires 'Administer System' permission.

**Response Example**
```json
{
  "edition": "Enterprise",
  "licensee": "SonarSource",
  "expiresAt": "2027-12-31"
}
```

---

### `POST api/editions/unset_license`
*internal since 7.2*

Un-sets license. Require 'Administer System' permission.
