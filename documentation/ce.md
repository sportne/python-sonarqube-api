[Back to Index](index.md)

# Compute Engine (ce)

### `GET api/ce/activity`
*since 5.2*

Search for tasks. Requires the system administration permission, or project administration permission if component is set.

**Parameters**
- `component` (optional): Component key.
- `status` (optional): Comma-separated list of task statuses.
- `type` (optional): Task type.

**Response Example**
```json
{
  "paging": {
    "pageIndex": 1,
    "pageSize": 100,
    "total": 1
  },
  "tasks": [
    {
      "id": "AV-a_3p249829849",
      "type": "REPORT",
      "componentId": "AV-a_3p249829849",
      "componentKey": "my_project",
      "componentName": "My Project",
      "componentQualifier": "TRK",
      "analysisId": "AV-a_3p249829849",
      "status": "SUCCESS",
      "submittedAt": "2017-04-04T13:30:00+0200",
      "submitterLogin": "admin",
      "startedAt": "2017-04-04T13:30:01+0200",
      "executedAt": "2017-04-04T13:30:05+0200",
      "executionTimeMs": 4000,
      "logs": false,
      "hasError": false,
      "hasScannerContext": true,
      "organization": "my-org"
    }
  ]
}
```

**Changelog**
- 6.1: `logs` field is deprecated.

---

### `GET api/ce/activity_status`
*since 5.5*

Returns CE activity related metrics. Requires 'Administer System' permission or 'Administer' rights on the specified project.

**Parameters**
- `componentId` (optional): Component ID.

**Response Example**
```json
{
  "pending": 0,
  "inProgress": 1,
  "failing": 0,
  "pendingTime": 0,
  "lastActivity": 1491305405000,
  "queueDepth": 1
}
```

**Changelog**
- 8.4: `failing` property was added.

---

### `GET api/ce/analysis_status`
*internal since 7.4*

Get the analysis status of a given component: a project, branch or pull request. Requires the following permission: 'Browse' on the specified component.

**Parameters**
- `analysisId` (required): Analysis ID.

**Response Example**
```json
{
  "status": "SUCCESS"
}
```

---

### `POST api/ce/cancel`
*internal since 5.2*

Cancels a pending task. In-progress tasks cannot be canceled. Requires one of the following permissions:
- 'Administer System'
- 'Administer' rights on the project related to the task

**Parameters**
- `id` (required): Task ID.

---

### `POST api/ce/cancel_all`
*internal since 5.2*

Cancels all pending tasks. Requires system administration permission. In-progress tasks are not canceled.

---

### `GET api/ce/component`
*since 5.2*

Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project). Requires the following permission: 'Browse' on the specified component.

**Parameters**
- `component` (required): Component key.

**Response Example**
```json
{
  "queue": [],
  "current": {
    "id": "AV-a_3p249829849",
    "type": "REPORT",
    "componentId": "AV-a_3p249829849",
    "componentKey": "my_project",
    "componentName": "My Project",
    "componentQualifier": "TRK",
    "analysisId": "AV-a_3p249829849",
    "status": "IN_PROGRESS",
    "submittedAt": "2017-04-04T13:30:00+0200",
    "submitterLogin": "admin",
    "startedAt": "2017-04-04T13:30:01+0200",
    "executionTimeMs": 4000,
    "logs": false,
    "hasError": false,
    "hasScannerContext": true,
    "organization": "my-org"
  },
  "last": {
    "id": "AV-a_3p249829848",
    "type": "REPORT",
    "componentId": "AV-a_3p249829848",
    "componentKey": "my_project",
    "componentName": "My Project",
    "componentQualifier": "TRK",
    "analysisId": "AV-a_3p249829848",
    "status": "SUCCESS",
    "submittedAt": "2017-04-04T13:20:00+0200",
    "submitterLogin": "admin",
    "startedAt": "2017-04-04T13:20:01+0200",
    "executedAt": "2017-04-04T13:20:05+0200",
    "executionTimeMs": 4000,
    "logs": false,
    "hasError": false,
    "hasScannerContext": true,
    "organization": "my-org"
  }
}
```

---

### `POST api/ce/dismiss_analysis_warning`
*internal since 8.5*

Permanently dismiss a specific analysis warning. Requires authentication and 'Browse' permission on the specified project.

**Parameters**
- `project` (required): Project key.
- `warningId` (required): Warning ID.

---

### `GET api/ce/indexation_status`
*internal since 8.4*

Returns the count of projects with completed issue indexing.

**Response Example**
```json
{
  "total": 100,
  "processed": 50
}
```

---

### `GET api/ce/info`
*internal since 7.2*

Gets information about Compute Engine. Requires the system administration permission or system passcode (see WEB_SYSTEM_PASS_CODE in sonar.properties).

**Response Example**
```json
{
  "version": "8.4.0.35506",
  "startedAt": "2020-07-20T10:00:00+0200",
  "status": "UP"
}
```

---

### `POST api/ce/pause`
*internal since 7.2*

Requests pause of Compute Engine workers. Requires the system administration permission or system passcode (see WEB_SYSTEM_PASS_CODE in sonar.properties).

---

### `POST api/ce/resume`
*internal since 7.2*

Resumes pause of Compute Engine workers. Requires the system administration permission or system passcode (see WEB_SYSTEM_PASS_CODE in sonar.properties).

---

### `POST api/ce/set_worker_count`
*internal since 2.10*

Set the number of workers in the Compute Engine. If your queue backs up behind analysis reports from large projects, increasing the number of Compute Engine workers will allow you to take full advantage of having configured increased Compute Engine memory on a multi-core server (vertical scaling). Requires the system administration permission.

**Parameters**
- `count` (required): Number of workers.

---

### `POST api/ce/submit`
*internal since 5.2*

Submits a scanner report to the queue. Report is processed asynchronously. Requires analysis permission. If the project does not exist, then the provisioning permission is also required.

**Parameters**
- `projectKey` (required): Project key.
- `report` (required): Scanner report.

**Response Example**
```json
{
  "taskId": "AV-a_3p249829849",
  "taskUrl": "/api/ce/task?id=AV-a_3p249829849"
}
```

---

### `GET api/ce/task`
*since 5.2*

Give Compute Engine task details such as type, status, duration and associated component. Requires one of the following permissions:
- 'Administer' at global or project level
- 'Execute Analysis' at global or project level
Since 6.1, field "logs" is deprecated and its value is always false.

**Parameters**
- `id` (required): Task ID.

**Response Example**
```json
{
  "task": {
    "id": "AV-a_3p249829849",
    "type": "REPORT",
    "componentId": "AV-a_3p249829849",
    "componentKey": "my_project",
    "componentName": "My Project",
    "componentQualifier": "TRK",
    "analysisId": "AV-a_3p249829849",
    "status": "SUCCESS",
    "submittedAt": "2017-04-04T13:30:00+0200",
    "submitterLogin": "admin",
    "startedAt": "2017-04-04T13:30:01+0200",
    "executedAt": "2017-04-04T13:30:05+0200",
    "executionTimeMs": 4000,
    "logs": false,
    "hasError": false,
    "hasScannerContext": true,
    "organization": "my-org"
  }
}
```

---

### `GET api/ce/task_types`
*internal since 5.5*

List available task types.

**Response Example**
```json
{
  "taskTypes": [
    "REPORT",
    "PROJECT_ANALYSIS_CLEANUP",
    "PORTFOLIO_REFRESH",
    "APPLICATION_REFRESH"
  ]
}
```

---

### `GET api/ce/worker_count`
*internal since 6.5*

Return number of Compute Engine workers. Requires the system administration permission.

**Response Example**
```json
{
  "value": 5,
  "canSetWorkerCount": true
}
```
