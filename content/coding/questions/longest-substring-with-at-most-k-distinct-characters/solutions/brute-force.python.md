Start from the definition directly: try every possible starting index, extend the substring one character at a time, and track how many distinct characters it currently holds. The moment a window would exceed `k` distinct characters, stop extending that start and move on.

This checks every substring, so it is quadratic, but it is the most literal translation of the problem and a useful baseline before optimizing.

```python
def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    best = 0
    n = len(s)
    for start in range(n):
        counts = {}
        for end in range(start, n):
            counts[s[end]] = counts.get(s[end], 0) + 1
            if len(counts) > k:
                break
            best = max(best, end - start + 1)
    return best
```

## Why it works

Fixing `start` and growing `end` enumerates every substring beginning at `start`. The `counts` map tracks the distinct characters in the current window; once it grows past `k`, every longer window from the same start is also invalid, so breaking early is safe. Taking the running maximum over all valid windows yields the global answer.

## Complexity

- Time: O(n^2) — up to n starts, each scanning up to n characters.
- Space: O(k) — the map holds at most k + 1 distinct characters.
