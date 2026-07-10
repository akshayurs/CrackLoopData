The quadratic cost of the brute force comes from recounting the same value again and again. Tally every value's frequency in a single pass instead: a hash map from value to running count means each element is touched once.

As soon as any count crosses `n / 2` we have the answer, so we can even return early without scanning the rest.

```python
def majority_element(nums):
    threshold = len(nums) // 2
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > threshold:
            return x
    return -1
```

## Why it works

The map accumulates exact occurrence counts as we stream through the array. The majority element, by definition, is the only value whose tally can exceed `n // 2`, and it must reach that threshold on some iteration — at which point we return it immediately.

## Complexity

- Time: O(n) — one pass; each map read and write is O(1) on average.
- Space: O(n) — the map may hold up to n distinct keys.
