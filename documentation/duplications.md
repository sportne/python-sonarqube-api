[Back to Index](index.md)

# Duplications

### `GET api/duplications/show`
*since 4.4*

Get duplications. Require Browse permission on file's project.

**Parameters**
- `key` (required): File key. Example: `my_project:/src/foo/Bar.php`
- `branch` (optional): Branch key. Example: `feature/my_branch`
- `pullRequest` (optional): Pull request id. Example: `5461`

**Response Example**
```json
{
  "duplications": [
    {
      "blocks": [
        {
          "_ref": "1",
          "startLine": 10,
          "endLine": 20,
          "size": 11
        }
      ],
      "files": {
        "1": {
          "key": "my_project:src/foo/Bar.php",
          "name": "Bar.php",
          "projectName": "My Project"
        }
      }
    }
  ]
}
```

**Changelog**
- 7.1: `pullRequest` parameter added.
- 6.6: `branch` parameter added.
