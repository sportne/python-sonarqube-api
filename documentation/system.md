[Back to Index](index.md)

# System

### `POST api/system/change_log_level`
*since 5.2*

Temporarily changes level of logs. New level is not persistent and is lost when restarting server. Requires system administration permission.

**Parameters**
- `level` (required): The new level. Be cautious: DEBUG, and even more TRACE, may have performance impacts. Possible values: `TRACE`, `DEBUG`, `INFO`

---

### `GET api/system/health`
*since 6.6*

Provide health status of SonarQube.
Although global health is calculated based on both application and search nodes, detailed information is returned only for application nodes.

GREEN: SonarQube is fully operational
YELLOW: SonarQube is usable, but it needs attention in order to be fully operational
RED: SonarQube is not operational

Requires the 'Administer System' permission or system passcode (see WEB_SYSTEM_PASS_CODE in sonar.properties).
When SonarQube is in safe mode (waiting or running a database upgrade), only the authentication with a system passcode is supported.

**Response Example**
```json
{
  "health": "RED",
  "causes": [
    {
      "message": "Application node app-1 is RED"
    }
  ],
  "nodes": [
    {
      "name": "app-1",
      "type": "APPLICATION",
      "host": "192.168.1.1",
      "port": 999,
      "startedAt": "2015-08-13T23:34:59+0200",
      "health": "RED",
      "causes": [
        {
          "message": "foo"
        }
      ]
    },
    {
      "name": "app-2",
      "type": "APPLICATION",
      "host": "[2001:db8:abcd:1234::1]",
      "port": 999,
      "startedAt": "2015-08-13T23:34:59+0200",
      "health": "YELLOW",
      "causes": [
        {
          "message": "bar"
        }
      ]
    }
  ]
}
```

---

### `GET api/system/info`
*since 5.1*

Get detailed information about system configuration.
Requires 'Administer' permissions.

---

### `GET api/system/liveness`
*internal since 9.1*

Provide liveness of SonarQube, meant to be used for a liveness probe on Kubernetes
Require 'Administer System' permission or authentication with passcode

When SonarQube is fully started, liveness check for database connectivity, Compute Engine status, and, except for DataCenter Edition, if ElasticSearch is Green or Yellow

When SonarQube is on Safe Mode (for example when a database migration is running), liveness check only for database connectivity

HTTP 204: this SonarQube node is alive
Any other HTTP code: this SonarQube node is not alive, and should be reschedule

---

### `GET api/system/logs`
*since 5.2*

Get system logs in plain-text format. Requires system administration permission.

**Parameters**
- `name` (optional): since 6.2, Name of the logs to get. Possible values: `access`, `app`, `ce`, `deprecation`, `es`, `web`. Default value: `app`

---

### `POST api/system/migrate_db`
*since 5.2*

Migrate the database to match the current version of SonarQube.
Sending a POST request to this URL starts the DB migration. It is strongly advised to make a database backup before invoking this WS.
State values are:
- `NO_MIGRATION`: DB is up to date with current version of SonarQube.
- `NOT_SUPPORTED`: Migration is not supported on embedded databases.
- `MIGRATION_RUNNING`: DB migration is under go.
- `MIGRATION_SUCCEEDED`: DB migration has run and has been successful.
- `MIGRATION_FAILED`: DB migration has run and failed. SonarQube must be restarted in order to retry a DB migration (optionally after DB has been restored from backup).
- `MIGRATION_REQUIRED`: DB migration is required.

---

### `GET api/system/ping`
*since 6.3*

Answers "pong" as plain-text

---

### `POST api/system/restart`
*since 4.3*

Restarts server. Requires 'Administer System' permission. Performs a full restart of the Web, Search and Compute Engine Servers processes. Does not reload sonar.properties.

---

### `GET api/system/status`
*since 5.2*

Get state information about SonarQube.
- `status`: the running status
- `STARTING`: SonarQube Web Server is up and serving some Web Services (eg. api/system/status) but initialization is still ongoing
- `UP`: SonarQube instance is up and running
- `DOWN`: SonarQube instance is up but not running because migration has failed (refer to WS /api/system/migrate_db for details) or some other reason (check logs).
- `RESTARTING`: SonarQube instance is still up but a restart has been requested (refer to WS /api/system/restart for details).
- `DB_MIGRATION_NEEDED`: database migration is required. DB migration can be started using WS /api/system/migrate_db.
- `DB_MIGRATION_RUNNING`: DB migration is running (refer to WS /api/system/migrate_db for details)

---

### `GET api/system/upgrades`
*since 5.2*

Lists available upgrades for the SonarQube instance (if any) and for each one, lists incompatible plugins and plugins requiring upgrade.
Plugin information is retrieved from Update Center. Date and time at which Update Center was last refreshed is provided in the response.
