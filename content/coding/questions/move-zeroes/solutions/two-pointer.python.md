Do it in place with two indices. Keep a slow pointer `insert` marking where the next non-zero value belongs, and a fast pointer `i` scanning the array. Every time the scan finds a non-zero, swap it into the `insert` slot and advance `insert`.

Because `insert` only moves when a non-zero is placed, everything at or past it is either about to be overwritten or already a zero — so the zeros naturally collect at the tail with no extra memory.

```python
def move_zeroes(nums):
    insert = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert], nums[i] = nums[i], nums[insert]
            insert += 1
    return nums
```

## Why it works

`insert` counts how many non-zeros have been fixed in place. When `i` hits a non-zero, swapping with position `insert` puts it right after the previously placed non-zero, so order is preserved. The value swapped back to `i` is whatever sat at `insert` — always a zero once `i` has moved past `insert`. After the loop, indices `[insert, n)` are all zeros.

## Complexity

- Time: O(n) — a single scan.
- Space: O(1) — swaps happen in the original array.
