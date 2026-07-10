Start with the obvious plan: count how many times each value appears, then rank the values by that count. A hash map builds the counts in one pass, and sorting the distinct values by their frequency puts the most common ones at the front.

Once sorted, the answer is just the first `k` values. The counting is linear, but the sort of the distinct values is what dominates the running time.

```python
from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    ordered = sorted(counts, key=lambda value: counts[value], reverse=True)
    return sorted(ordered[:k])
```

## Why it works

`Counter` maps each value to its number of occurrences. Sorting the distinct values by `counts[value]` in descending order lines them up from most to least frequent, so slicing off the first `k` gives exactly the `k` most common values. Because the answer is guaranteed unique, there is no tie to break at the boundary. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct values costs O(n log n); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the counter and the sorted list each hold up to n entries.
