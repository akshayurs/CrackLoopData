The definition is almost a set of instructions: for each position, walk forward until you meet a bigger value, and because the array is circular, keep walking past the end by taking indices modulo `n`. Do that independently for every element.

For index `i`, we probe the next `n - 1` positions `(i + 1) % n, (i + 2) % n, …`. That covers every other element exactly once — enough to decide the answer, since the current element can never be its own next greater.

```python
def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        for step in range(1, n):
            j = (i + step) % n
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    return result
```

## Why it works

Scanning `step = 1 … n-1` visits all `n - 1` other elements in circular order starting right after `i`. The first one strictly greater than `nums[i]` is by definition its next greater element, so we record it and stop. If the loop finishes without a hit, no larger value exists anywhere and the pre-filled `-1` stands.

## Complexity

- Time: O(n^2) — each of the n elements scans up to n-1 others.
- Space: O(1) — ignoring the output array.
