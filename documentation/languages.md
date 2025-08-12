[Back to Index](index.md)

# Languages

### `GET api/languages/list`
*since 5.1*

List supported programming languages.

**Parameters**
- `q` (optional): A pattern to match language keys/names against. Example: `java`
- `ps` (optional): The size of the list to return, 0 for all languages. Default: 0. Example: `25`

**Response Example**
```json
{
  "languages": [
    {
      "key": "java",
      "name": "Java"
    },
    {
      "key": "js",
      "name": "JavaScript"
    }
  ]
}
```
