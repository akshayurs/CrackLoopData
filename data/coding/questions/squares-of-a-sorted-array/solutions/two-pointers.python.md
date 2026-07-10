Because the input is sorted, the largest square must come from one of the two ends: either the most negative number on the left or the most positive on the right. Compare the absolute values at both ends and take the bigger square first.

Fill the answer from the back — the largest square goes into the last slot — and move the pointer that supplied it inward. Repeat until the pointers cross, and the result comes out sorted without any final sort.

```python
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for pos in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
    return result
```

## Why it works

In a sorted array the maximum absolute value is always at one end. Whichever end has the larger magnitude produces the larger square, so placing it at the current rightmost empty slot builds the output in strictly non-increasing position order — i.e. sorted ascending. Each element is placed exactly once as its pointer steps inward.

## Complexity

- Time: O(n) — a single pass with two pointers.
- Space: O(n) — the output array (no extra sorting structure).
