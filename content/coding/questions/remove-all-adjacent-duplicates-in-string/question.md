You are given a string `s` made of lowercase English letters. A **duplicate removal** deletes two adjacent, equal characters and glues the remaining parts together. Keep performing duplicate removals until no adjacent pair of equal characters is left.

Return the final string after all possible removals. The answer is guaranteed to be unique.

## Examples

```text
Input:  s = "abbaca"
Output: "ca"          # "abbaca" -> remove "bb" -> "aaca" -> remove "aa" -> "ca"
```

```text
Input:  s = "azxxzy"
Output: "ay"          # remove "xx" -> "azzy" -> remove "zz" -> "ay"
```

```text
Input:  s = "aaaaa"
Output: "a"           # pairs cancel from the left, one character survives
```

## Constraints

- 1 <= s.length <= 10^5
- `s` consists of lowercase English letters only.

## Follow-up

Repeatedly rebuilding the string is quadratic. Can you finish in a single pass with O(n) time?
