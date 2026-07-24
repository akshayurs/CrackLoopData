If the numbers were sorted, consecutive values would sit next to each other, so the longest run becomes a single left-to-right scan. Sort once, then walk the list tracking how long the current increasing-by-one streak is.

The only subtlety is duplicates: when the next value equals the current one it neither extends nor breaks the run, so we just skip past it.

```python
def longest_consecutive(nums):
    if not nums:
        return 0
    nums = sorted(set(nums))
    best = current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best
```

## Why it works

After `sorted(set(...))` the values are unique and ascending. Each adjacent pair is either consecutive (`nums[i] == nums[i-1] + 1`), in which case the streak grows, or it has a gap, which resets the streak to 1. Deduping first removes the duplicate case entirely, so a plain adjacency test suffices, and `best` records the longest streak observed.

## Complexity

- Time: O(n log n) — dominated by the sort; the scan afterward is linear.
- Space: O(n) — the deduplicated sorted copy (O(1) beyond that if sorting in place).
