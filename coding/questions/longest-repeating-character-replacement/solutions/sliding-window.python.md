Grow a window from the right and only shrink it when it becomes invalid. A window is valid when the letters you'd have to overwrite — `window_length - max_count`, where `max_count` is the frequency of the most common letter inside — is at most `k`. Keep the letter counts in a fixed 26-slot array so each step is constant work.

The trick that makes it a single pass: `max_count` never needs to be lowered. If a previous window achieved a higher `max_count`, no shorter window can beat the answer it already produced, so we let the window slide forward one step at a time rather than shrinking it. The window's width at the end is the longest valid substring seen.

```python
def character_replacement(s, k):
    counts = [0] * 26
    left = 0
    max_count = 0
    best = 0
    for right in range(len(s)):
        idx = ord(s[right]) - ord('A')
        counts[idx] += 1
        max_count = max(max_count, counts[idx])
        if (right - left + 1) - max_count > k:
            counts[ord(s[left]) - ord('A')] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

## Why it works

`(right - left + 1) - max_count` counts the letters in the window that are not the majority letter — exactly the replacements needed to unify it. When that exceeds `k`, the window is one too wide, so we advance `left` by one, keeping the width monotonic. Because `max_count` only ever rises, the window can only expand past widths that were already valid, so `best` correctly tracks the maximum achievable length in one sweep.

## Complexity

- Time: O(n) — each index enters and leaves the window at most once.
- Space: O(1) — a fixed array of 26 counters.
