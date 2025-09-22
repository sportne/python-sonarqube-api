[Back to Index](index.md)

# Clean Code Policy V2

### `POST /api/v2/clean-code-policy/rules`

Create a custom rule. Requires the "Administer Quality Profiles" permission.

**Request Body**

- `key` (string, required): Key of the custom rule to create, must include the
  repository. Max: 200.
- `templateKey` (string, required): Key of the rule template to use when
  creating the custom rule. Max: 200.
- `name` (string, required): Rule name. Max: 200.
- `markdownDescription` (string, required): Rule description in markdown
  format.
- `status` (string, optional): Rule status. Valid values: `BETA`, `DEPRECATED`,
  `READY`, `REMOVED`. Default: `READY`.
- `parameters` (array of objects, optional): Custom rule parameters.
- `cleanCodeAttribute` (string, optional): Clean code attribute. Valid values:
  `CONVENTIONAL`, `FORMATTED`, `IDENTIFIABLE`, `CLEAR`, `COMPLETE`,
  `EFFICIENT`, `LOGICAL`, `DISTINCT`, `FOCUSED`, `MODULAR`, `TESTED`,
  `LAWFUL`, `RESPECTFUL`, `TRUSTWORTHY`.
- `impacts` (array of objects, required): Impacts to associate with the rule.
- `severity` (string, optional): Severity of the rule.
- `type` (string, optional): Rule type. Valid values: `CODE_SMELL`, `BUG`,
  `VULNERABILITY`, `SECURITY_HOTSPOT`.

**Response**

```json
{
  "id": "string",
  "key": "string",
  "repositoryKey": "string",
  "name": "string",
  "severity": "string",
  "type": "Enum (string): CODE_SMELL, BUG, VULNERABILITY, SECURITY_HOTSPOT",
  "impacts": [
    {
      "softwareQuality": "Enum (string): MAINTAINABILITY, RELIABILITY, SECURITY",
      "severity": "Enum (string): INFO, LOW, MEDIUM, HIGH, BLOCKER"
    }
  ],
  "cleanCodeAttribute": "Enum (string): CONVENTIONAL, FORMATTED, IDENTIFIABLE, CLEAR, COMPLETE, EFFICIENT, LOGICAL, DISTINCT, FOCUSED, MODULAR, TESTED, LAWFUL, RESPECTFUL, TRUSTWORTHY",
  "cleanCodeAttributeCategory": "Enum (string): ADAPTABLE, CONSISTENT, INTENTIONAL, RESPONSIBLE",
  "status": "Enum (string): BETA, DEPRECATED, READY, REMOVED",
  "external": "boolean",
  "createdAt": "string",
  "descriptionSections": [
    {
      "key": "string",
      "content": "string",
      "context": {
        "key": "string",
        "displayName": "string"
      }
    }
  ],
  "markdownDescription": "string",
  "gapDescription": "string",
  "htmlNote": "string",
  "markdownNote": "string",
  "educationPrinciples": [
    "string"
  ],
  "template": "boolean",
  "templateId": "string",
  "tags": [
    "string"
  ],
  "systemTags": [
    "string"
  ],
  "languageKey": "string",
  "languageName": "string",
  "parameters": [
    {
      "key": "string",
      "htmlDescription": "string",
      "defaultValue": "string",
      "type": "Enum (string): STRING, TEXT, BOOLEAN, INTEGER, FLOAT"
    }
  ],
  "remediationFunctionType": "string",
  "remediationFunctionGapMultiplier": "string",
  "remediationFunctionBaseEffort": "string"
}
```
