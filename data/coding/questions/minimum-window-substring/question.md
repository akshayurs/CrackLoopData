You are given two strings `s` and `t`. Return the shortest substring of `s` that contains every character of `t`, including duplicates. If no such substring exists, return the empty string `""`.

The characters of `t` may appear in any order within the window, and the window may contain extra characters. If several windows tie for the shortest length, return the one that starts at the smallest index.

## Examples

```text
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"        # smallest window covering A, B, and C
```

```text
Input:  s = "a", t = "a"
Output: "a"
```

```text
Input:  s = "a", t = "aa"
Output: ""            # only one 'a' available, two are required
```

## Constraints

- 1 <= s.length, t.length <= 10^5
- `s` and `t` consist of uppercase and lowercase English letters.
- The answer is unique for the given inputs (guaranteed shortest, leftmost on ties).

## Follow-up

Can you solve it in a single left-to-right scan, in O(|s| + |t|) time?
