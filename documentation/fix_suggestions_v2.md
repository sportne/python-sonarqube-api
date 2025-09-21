[Back to Index](index.md)

# Fix Suggestions V2

### `POST /api/v2/fix-suggestions/ai-suggestions`

Suggest a fix for the given issueId. Requires Code Viewer permission.

**Request Body**
- `projectKey` (string, required)
- `issueId` (string, required): Issue key.
- `issue` (object, optional)
    - `message` (string)
    - `startLine` (integer)
    - `endLine` (integer)
    - `ruleKey` (string)
    - `sourceCode` (string)

**Response**
```json
{
  "id": "string (uuid)",
  "issueId": "string",
  "explanation": "string",
  "changes": [
    {
      "startLine": "integer (int32)",
      "endLine": "integer (int32)",
      "newCode": "string"
    }
  ]
}
```

---

### `GET /api/v2/fix-suggestions/issues/{issueId}`

Fetch AI suggestion availability for the given issueId. Requires Code Viewer permission.

**Path Parameters**
- `issueId` (string, required)

**Response**
```json
{
  "issueId": "string",
  "aiSuggestion": "Enum (string): AVAILABLE, NOT_AVAILABLE_FILE_LEVEL_ISSUE, NOT_AVAILABLE_UNSUPPORTED_RULE, NOT_AVAILABLE_FILE_SIZE"
}
```
