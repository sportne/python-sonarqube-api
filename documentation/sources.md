[Back to Index](index.md)

# Sources

### `GET api/sources/index`
*internal since 5.0*

Get source code as line number / text pairs. Require See Source Code permission on file

**Parameters**
- `from` (optional): First line. Default value: 1
- `resource` (required): File key. Example value: `my_project:/src/foo/Bar.php`
- `to` (optional): Last line (excluded). If not specified, all lines are returned until end of file

---

### `GET api/sources/issue_snippets`
*internal since 7.8*

Get code snippets involved in an issue or hotspot. Requires 'See Source Code permission' permission on the project

**Parameters**
- `issueKey` (required): Issue or hotspot key. Example value: `AU-Tpxb--iU5OvuD2FLy`

---

### `GET api/sources/lines`
*internal since 5.0*

Show source code with line oriented info. Requires See Source Code permission on file's project
Each element of the result array is an object which contains:
- Line number
- Content of the line
- Author of the line (from SCM information)
- Revision of the line (from SCM information)
- Last commit date of the line (from SCM information)
- Line hits from coverage
- Number of conditions to cover in tests
- Number of conditions covered by tests
- Whether the line is new

**Parameters**
- `branch` (optional): Branch key. Example value: `feature/my_branch`
- `from` (optional): First line to return. Starts from 1. Default value: 1. Example value: 10
- `key` (optional): File key. Mandatory if param 'uuid' is not set. Available since 5.2. Example value: `my_project:/src/foo/Bar.php`
- `pullRequest` (optional): Pull request id. Example value: `5461`
- `to` (optional): Optional last line to return (inclusive). It must be greater than or equal to parameter 'from'. If unset, then all the lines greater than or equal to 'from' are returned. Example value: 20
- `uuid` (optional): File uuid. Mandatory if param 'key' is not set. Example value: `f333aab4-7e3a-4d70-87e1-f4c491f05e5c`

---

### `GET api/sources/raw`
*since 5.0*

Get source code as raw text. Require 'See Source Code' permission on file

**Parameters**
- `branch` (optional): Branch key. Example value: `feature/my_branch`
- `key` (required): File key. Example value: `my_project:src/foo/Bar.php`
- `pullRequest` (optional): Pull request id. Example value: `5461`

---

### `GET api/sources/scm`
*since 4.4*

Get SCM information of source files. Require See Source Code permission on file's project
Each element of the result array is composed of:
- Line number
- Author of the commit
- Datetime of the commit (before 5.2 it was only the Date)
- Revision of the commit (added in 5.2)

**Parameters**
- `commits_by_line` (optional): Group lines by SCM commit if value is false, else display commits for each line, even if two consecutive lines relate to the same commit. Possible values: `true`, `false`, `yes`, `no`. Default value: `false`
- `from` (optional): First line to return. Starts at 1. Default value: 1. Example value: 10
- `key` (required): File key. Example value: `my_project:/src/foo/Bar.php`
- `to` (optional): Last line to return (inclusive). Example value: 20

---

### `GET api/sources/show`
*since 4.4*

Get source code. Requires See Source Code permission on file's project
Each element of the result array is composed of:
- Line number
- Content of the line

**Parameters**
- `from` (optional): First line to return. Starts at 1. Default value: 1. Example value: 10
- `key` (required): File key. Example value: `my_project:/src/foo/Bar.php`
- `to` (optional): Last line to return (inclusive). Example value: 20
