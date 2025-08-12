[Back to Index](index.md)

# Metrics

### `GET api/metrics/search`
*since 5.2*

Search for metrics.

**Parameters**
- `f` (optional): Comma-separated list of fields to be returned in response.
- `p` (optional): 1-based page number. Default: 1
- `ps` (optional): Page size. Must be greater than 0 and less or equal than 500. Default: 100

**Response Example**
```json
{
  "metrics": [
    {
      "id": "1",
      "key": "ncloc",
      "type": "INT",
      "name": "Lines of code",
      "description": "Non Commenting Lines of Code",
      "domain": "Size",
      "direction": -1,
      "qualitative": false,
      "hidden": false,
      "custom": false
    }
  ],
  "total": 1,
  "p": 1,
  "ps": 100
}
```

---

### `GET api/metrics/types`
*since 5.2*

List all available metric types.

**Response Example**
```json
{
  "types": [
    "INT",
    "FLOAT",
 "PERCENT",
    "BOOL"
  ]
}
```
