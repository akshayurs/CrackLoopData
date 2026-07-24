The simplest way to think about it: the answer is just "all the non-zero values, in order, followed by enough zeros to fill the rest." So build that list directly.

Collect the non-zero elements into a fresh list, pad it with as many zeros as were removed, then copy the result back into `nums` in place.

```python
def move_zeroes(nums):
    result = [n for n in nums if n != 0]
    result += [0] * (len(nums) - len(result))
    nums[:] = result
    return nums
```

## Why it works

Filtering keeps the non-zero values in their original left-to-right order, so their relative positions are preserved. The count of missing slots equals the number of zeros, and padding fills exactly those with `0`. Writing back via `nums[:]` mutates the original array so the caller sees the rearranged result.

## Complexity

- Time: O(n) — one pass to filter, one pass to copy back.
- Space: O(n) — the temporary list holds up to n elements.
