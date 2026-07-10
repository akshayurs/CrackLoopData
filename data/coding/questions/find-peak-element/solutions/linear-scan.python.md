The most direct idea: walk left to right and stop at the first index whose value is greater than the element right after it. Because positions past the ends count as negative infinity, if you never find such a drop the array climbed all the way to the end, so the last index is the peak.

Scanning for the first "downhill step" works because the very first time the values stop rising, the element just before the drop is higher than both its neighbors.

```python
def find_peak_element(nums):
    n = len(nums)
    for i in range(n):
        if i == n - 1 or nums[i] > nums[i + 1]:
            return i
    return -1
```

## Why it works

At index `i`, the left neighbor is already known to be smaller — either `i` is the start, or you only reached `i` because `nums[i - 1] < nums[i]` (otherwise you would have returned earlier). The moment `nums[i] > nums[i + 1]`, both sides are lower, so `i` is a peak. If the loop reaches the last index without a drop, the sequence was strictly increasing and the final element is the peak.

## Complexity

- Time: O(n) — one pass over the array in the worst case.
- Space: O(1) — only a loop index is stored.
