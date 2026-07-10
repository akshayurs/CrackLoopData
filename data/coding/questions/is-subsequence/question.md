You are given two strings `s` and `t`. Return `true` if `s` is a subsequence of `t`, and `false` otherwise.

A subsequence is formed by deleting zero or more characters from `t` without changing the order of the characters that remain. For example, `"ace"` is a subsequence of `"abcde"`, but `"aec"` is not.

## Examples

```text
Input:  s = "abc", t = "ahbgdc"
Output: true          # a…b…c appear in order inside t
```

```text
Input:  s = "axc", t = "ahbgdc"
Output: false         # there is no 'x' to match in t
```

```text
Input:  s = "", t = "ahbgdc"
Output: true          # the empty string is a subsequence of everything
```

## Constraints

- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- `s` and `t` consist only of lowercase English letters.

## Follow-up

Suppose there are many strings `s1, s2, ..., sk` (with k >= 10^9) to check against the same `t`, one after another. How would you preprocess `t` so each query is fast?
