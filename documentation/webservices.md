[Back to Index](index.md)

# Web Services

### `GET api/webservices/list`
*since 4.2*

List web services

**Parameters**
- `include_internals` (optional): Include web services that are implemented for internal use only. Their forward-compatibility is not assured. Possible values: `true`, `false`, `yes`, `no`. Default value: `false`

---

### `GET api/webservices/response_example`
*since 4.4*

Display web service response example

**Parameters**
- `action` (required): Action of the web service. Example value: `search`
- `controller` (required): Controller of the web service. Example value: `api/issues`
