Since the array is sorted, we do not need to inspect every element — we can halve the search space each step. Keep a `[lo, hi]` window that always contains the answer position. Compare `target` to the middle value and discard the half that cannot hold it.

When the window closes, `lo` has landed on the first index whose value is not less than `target` — that is precisely the insert position, whether or not `target` was actually found.

```javascript
function searchInsert(nums, target) {
  let lo = 0, hi = nums.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (nums[mid] < target) {
      lo = mid + 1;
    } else {
      hi = mid;
    }
  }
  return lo;
}
```

## Why it works

The invariant is that the answer lies in `[lo, hi]`. When `nums[mid] < target`, `mid` and everything left of it are too small, so `lo` jumps past `mid`. Otherwise `mid` might be the answer, so `hi` shrinks to `mid`. The loop ends with `lo === hi`, the smallest index where `nums[index] >= target`, or `nums.length` if `target` exceeds all elements.

## Complexity

- Time: O(log n) — the window halves each iteration.
- Space: O(1) — two pointers only.
