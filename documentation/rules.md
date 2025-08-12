[Back to Index](index.md)

# Rules

### `GET api/rules/app`
*internal since 4.5*

Get data required for rendering the page 'Coding Rules'.

---

### `POST api/rules/create`
*since 4.4*

Create a custom rule. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `key` (required): Rule key.
- `name` (required): Rule name.
- `markdownDescription` (required): Rule description.
- `...` (other rule parameters)

---

### `POST api/rules/delete`
*since 4.4*

Delete custom rule. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `key` (required): Rule key.

---

### `GET api/rules/list`
*internal since 5.2*

List rules, excluding the external rules and the rules with status REMOVED.

**Parameters**
- `qprofile` (optional): Quality profile key.
- `p`, `ps` (optional): Pagination.

---

### `GET api/rules/repositories`
*since 4.5*

List available rule repositories.

---

### `GET api/rules/search`
*since 4.4*

Search for a collection of relevant rules matching a specified query.

**Parameters**
- `...` (many filter parameters)

---

### `GET api/rules/show`
*since 4.2*

Get detailed information about a rule.

**Parameters**
- `key` (required): Rule key.

---

### `GET api/rules/tags`
*since 4.4*

List rule tags.

---

### `POST api/rules/update`
*since 4.4*

Update an existing rule. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `key` (required): Rule key.
- `...` (other rule parameters)
