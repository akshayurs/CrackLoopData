You are given a string `s` made of uppercase English letters and an integer `k`. In one operation you may pick any position and change its character to any other uppercase letter; you may do this at most `k` times in total.

Return the length of the longest substring that can be turned into a run of a single repeated character after applying at most `k` such changes.

## Examples

```text
Input:  s = "ABAB", k = 2
Output: 4        # change both A's to B (or both B's to A) → "BBBB"
```

```text
Input:  s = "AABABBA", k = 1
Output: 4        # one change inside "ABBA" gives "AAAA" or "BBBB"
```

```text
Input:  s = "AAAA", k = 0
Output: 4        # already uniform, no changes needed
```

## Constraints

- 1 <= s.length <= 10^5
- `s` consists only of uppercase English letters (A–Z).
- 0 <= k <= s.length

## Follow-up

The brute force scans every substring. Can you find the answer in a single linear pass using a sliding window?
