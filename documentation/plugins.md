[Back to Index](index.md)

# Plugins

### `GET api/plugins/available`
*since 5.2*

Get the list of all the plugins available for installation on the SonarQube instance, sorted by plugin name. Requires 'Administer System' permission.

**Response Example**
```json
{
  "plugins": [ ... ]
}
```

---

### `POST api/plugins/cancel_all`
*since 5.2*

Cancels any operation pending on any plugin (install, update or uninstall). Requires 'Administer System' permissions.

---

### `GET api/plugins/download`
*internal since 7.2*

Download plugin JAR, for usage by scanner engine.

**Parameters**
- `key` (required): Plugin key.

---

### `POST api/plugins/install`
*since 5.2*

Installs the latest version of a plugin specified by its key. Requires 'Administer System' permissions.

**Parameters**
- `key` (required): Plugin key.

---

### `GET api/plugins/installed`
*since 5.2*

Get the list of all the plugins installed on the SonarQube instance, sorted by plugin name. Requires authentication.

**Response Example**
```json
{
  "plugins": [ ... ]
}
```

---

### `GET api/plugins/pending`
*since 5.2*

Get the list of plugins which will either be installed or removed at the next startup of the SonarQube instance. Requires 'Administer System' permission.

**Response Example**
```json
{
  "plugins": [ ... ]
}
```

---

### `POST api/plugins/uninstall`
*since 5.2*

Uninstalls the plugin specified by its key. Requires 'Administer System' permissions.

**Parameters**
- `key` (required): Plugin key.

---

### `POST api/plugins/update`
*since 5.2*

Updates a plugin specified by its key to the latest version compatible with the SonarQube instance. Requires 'Administer System' permissions.

**Parameters**
- `key` (required): Plugin key.

---

### `GET api/plugins/updates`
*since 5.2*

Lists plugins installed on the SonarQube instance for which at least one newer version is available. Requires 'Administer System' permission.

**Response Example**
```json
{
  "plugins": [ ... ]
}
```
