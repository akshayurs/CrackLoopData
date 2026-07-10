You are given a string `s`. Split it into one or more pieces such that every piece reads the same forwards and backwards. Return every way to do this — each way described as the ordered list of pieces used.

The order of pieces within a partition must follow their left-to-right position in `s`. The list of partitions itself must be sorted (lexicographically, comparing partitions piece by piece) so the output is deterministic.

## Examples

```text
Input:  s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]
```

```text
Input:  s = "raceacar"
Output: [["r", "a", "c", "e", "a", "c", "a", "r"], ["r", "a", "c", "e", "aca", "r"]]
```

```text
Input:  s = "b"
Output: [["b"]]
```

## Constraints

- 1 <= s.length <= 16
- `s` consists only of lowercase English letters.
