You are given a string `digits` containing only digit characters. A valid IPv4 address is four numbers (each called an octet) separated by dots, where every octet is between `0` and `255` and has no leading zero (unless the octet is exactly `"0"`). Return every valid IPv4 address that can be formed by splitting `digits` into four octets **without reordering or dropping any character** — every digit must be used exactly once.

Return the addresses sorted lexicographically as strings; there is no other defined order.

## Examples

```text
Input:  digits = "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

```text
Input:  digits = "0000"
Output: ["0.0.0.0"]
```

```text
Input:  digits = "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

## Constraints

- 1 <= digits.length <= 20
- `digits` consists of digits only, `0-9`.
