[Back to Index](index.md)

# Audit Logs

### `GET api/audit_logs/download`
*since 9.1*

Download security related audit log entries in JSON format.
Requires 'Administer System' permission. Available only with Enterprise Edition and above.

**Parameters**
- `from` (optional): Inclusive date from which audit logs will be returned. Format: ISO 8601 (YYYY-MM-DD)
- `to` (optional): Exclusive date up to which audit logs will be returned. Format: ISO 8601 (YYYY-MM-DD)
