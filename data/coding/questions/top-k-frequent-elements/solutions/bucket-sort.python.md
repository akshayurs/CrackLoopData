The key observation: a value can appear at most `n` times, so frequency is a small integer in the range `1..n`. That means you can bucket values by their exact count instead of comparing counts against each other — no sorting needed.

Build an array of buckets indexed by frequency, drop each value into the bucket matching its count, then walk the buckets from the highest frequency downward, collecting values until you have `k`. Every step is linear, so the whole thing runs in O(n).

```python
from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for value, count in counts.items():
        buckets[count].append(value)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return sorted(result)
    return sorted(result)
```

## Why it works

`buckets[f]` holds every value that occurs exactly `f` times, and `f` can never exceed `len(nums)`, so the array is big enough. Scanning from the highest index down visits values in strictly decreasing frequency, so the first `k` collected are the `k` most frequent. Indexing by count replaces comparison-based sorting entirely. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n + k log k) — counting, filling buckets, and scanning are each linear in n; the final ascending sort of the k results costs O(k log k).
- Space: O(n) — the counter and the bucket array together hold O(n) entries.
