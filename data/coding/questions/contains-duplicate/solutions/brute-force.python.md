The most literal reading of the problem: compare every element against every element that comes after it, and if two match, a duplicate exists. No extra memory, just two nested loops.

It is the honest baseline you would state first in an interview before reaching for anything faster.

```python
def contains_duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

## Why it works

The outer loop fixes one element; the inner loop scans every later position, so each unordered pair is examined exactly once. The instant two equal values are found we return `True`; if no pair ever matches, the array is all-distinct and we fall through to `False`.

## Complexity

- Time: O(n²) — about n²/2 pairs are compared.
- Space: O(1) — only loop counters, no extra structure.
