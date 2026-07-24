Walk the array from the front and stop at the first element that is greater than or equal to `target`. Because the array is sorted, that position is exactly where `target` belongs — either it holds `target` itself, or it is the first slot large enough to sit ahead of it.

If no such element exists, every value was smaller than `target`, so it belongs at the very end.

```python
def search_insert(nums, target):
    for i, n in enumerate(nums):
        if n >= target:
            return i
    return len(nums)
```

## Why it works

The first index where `nums[i] >= target` is the answer in both cases: when `nums[i] == target` we return its index, and when `nums[i] > target` inserting before it keeps the order intact. Falling off the end means `target` is larger than all elements, so its insert position is `len(nums)`.

## Complexity

- Time: O(n) — a single pass over the array.
- Space: O(1) — only an index is tracked.
