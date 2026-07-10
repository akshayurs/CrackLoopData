Since the array is already sorted, you never need a second buffer — you can overwrite duplicates in place. Keep a slow pointer at the last position you have committed a distinct value to, and a fast pointer that scans ahead. Whenever the fast pointer finds a value different from the one at slow, advance slow and copy the new value there.

The slow pointer effectively grows the "kept" prefix one element at a time, and everything it writes lands in already-visited slots, so nothing useful is ever clobbered.

```python
def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

## Why it works

`nums[slow]` is always the most recent distinct value written. Because equal values are adjacent in a sorted array, `nums[fast] != nums[slow]` fires exactly once per new distinct value; each such value is placed immediately after the previous one, so the prefix `nums[0..slow]` stays sorted and duplicate-free. The count of distinct values is `slow + 1` (the single starting element plus every advance).

## Complexity

- Time: O(n) — the fast pointer visits each element once.
- Space: O(1) — only two indices, no extra array.
