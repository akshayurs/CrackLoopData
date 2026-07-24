Ignore the sorted order for a moment and just look at every element. Walk left to right, and the first index whose value equals `target` is the answer; if you reach the end without a match, it is not there.

This is the simplest possible baseline. It always works, but it throws away the sorted structure that the problem hands you for free.

```python
def binary_search(nums, target):
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1
```

## Why it works

Every position is examined exactly once. If `target` exists, its index is found on the iteration that reaches it; if the loop finishes untouched, no element matched and `-1` is correct.

## Complexity

- Time: O(n) — a single pass over the array in the worst case.
- Space: O(1) — no extra storage.
