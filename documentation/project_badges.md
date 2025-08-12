[Back to Index](index.md)

# Project Badges

### `GET api/project_badges/ai_code_assurance`
*since 10.7*

Generate a badge for project's AI assurance as an SVG. Requires 'Browse' permission on the specified project.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.

---

### `GET api/project_badges/measure`
*since 7.1*

Generate badge for project's measure as an SVG. Requires 'Browse' permission on the specified project.

**Parameters**
- `project` (required): Project key.
- `metric` (required): Metric key.
- `branch` (optional): Branch key.

---

### `GET api/project_badges/quality_gate`
*since 7.1*

Generate badge for project's quality gate as an SVG. Requires 'Browse' permission on the specified project.

**Parameters**
- `project` (required): Project key.
- `branch` (optional): Branch key.

---

### `POST api/project_badges/renew_token`
*since 9.2*

Creates new token replacing any existing token for project or application badge access for private projects and applications. Requires 'Administer' permission on the specified project or application.

**Parameters**
- `project` (required): Project or application key.

---

### `GET api/project_badges/token`
*since 9.2*

Retrieve a token to use for project or application badge access for private projects or applications. Requires 'Browse' permission on the specified project or application.

**Parameters**
- `project` (required): Project or application key.
