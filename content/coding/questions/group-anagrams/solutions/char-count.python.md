Sorting each string is more work than the problem needs. What actually defines an anagram group is the count of each of the 26 lowercase letters — not their order. So build a fixed 26-length count vector for each string and use *that* as the key, skipping the O(k log k) sort entirely.

Turn the counts into a hashable tuple (e.g. `(1, 0, 0, ..., 1)`) and bucket by it. Every anagram produces the same tuple, so the grouping is identical to sorting but each key costs only a linear pass over the string.

```python
from collections import defaultdict


def group_anagrams(strs):
    buckets = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        buckets[tuple(counts)].append(s)
    return list(buckets.values())
```

## Why it works

Two strings are anagrams if and only if their per-letter frequency vectors are equal, so the tuple of 26 counts is a perfect canonical key. Building it scans the string once — no comparison sort. Identical vectors collide into one bucket; any difference in even a single letter's count yields a different key and a separate group.

## Complexity

- Time: O(n · k) — n strings, each scanned once in O(k); building the 26-length key is O(k + 26).
- Space: O(n · k) — the stored strings dominate; each key is a constant 26 entries.
