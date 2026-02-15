[Back to Index](index.md)

# Settings

### `GET api/settings/list_definitions`
*since 6.3*

List settings definitions. Requires 'Browse' permission when a component is specified.

**Parameters**
- `component` (optional): Component key

---

### `POST api/settings/reset`
*since 6.1*

Remove a setting value. The settings defined in config/sonar.properties are read-only and can't be changed.

**Parameters**
- `keys` (required): Comma-separated list of keys
- `component` (optional): Component key
- `branch` (optional): Branch key
- `pullRequest` (optional): Pull request id

---

### `POST api/settings/set`
*since 6.1*

Update a setting value. The settings defined in config/sonar.properties are read-only and can't be changed.

**Parameters**
- `key` (required): Setting key
- `value` (optional): Setting value. To reset a value, please use the reset web service.
- `values` (optional): Setting multi value. To set several values, the parameter must be called once for each value.
- `fieldValues` (optional): Setting field values. To set several values, the parameter must be called once for each value.
- `component` (optional): Component key

---

### `GET api/settings/values`
*since 6.3*

List settings values. If no value has been set for a setting, then the default value is returned.

**Parameters**
- `keys` (optional): Comma-separated list of keys
- `component` (optional): Component key
