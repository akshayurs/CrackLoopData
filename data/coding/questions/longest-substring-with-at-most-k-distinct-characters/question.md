Given a string `s` and an integer `k`, return the length of the longest contiguous substring of `s` that contains **at most `k` distinct characters**.

A substring is a run of consecutive characters. If `k` is `0`, no characters are allowed, so the answer is `0`.

## Examples

```text
Input:  s = "eceba", k = 2
Output: 3        # "ece" uses only {e, c} — 2 distinct characters
```

```text
Input:  s = "aa", k = 1
Output: 2        # the whole string uses a single distinct character
```

```text
Input:  s = "aabbcc", k = 2
Output: 4        # "aabb" or "bbcc" — any window of 2 letters caps at length 4
```

## Constraints

- 1 <= s.length <= 10^5
- s consists of lowercase and/or uppercase English letters.
- 0 <= k <= s.length

## Follow-up

Can you do it in a single pass over `s`, in O(n) time?
