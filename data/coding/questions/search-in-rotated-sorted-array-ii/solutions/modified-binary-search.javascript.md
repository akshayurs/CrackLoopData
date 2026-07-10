A rotated sorted array always has at least one sorted half around the midpoint. Binary search exploits this: compare `nums[mid]` to the endpoint of a half to decide which side is cleanly sorted, then check whether `target` falls inside that sorted range to know which way to move.

Duplicates add one wrinkle. When `nums[left]`, `nums[mid]`, and `nums[right]` are all equal, you cannot tell which half is sorted. The fix is to shrink the window by one from both ends and retry. That single ambiguity is what pushes the worst case (an array like all-equal values) to O(n), while typical inputs still halve each step.

```javascript
function search(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left <= right) {
    const mid = (left + right) >> 1;
    if (nums[mid] === target) {
      return true;
    }
    if (nums[left] === nums[mid] && nums[mid] === nums[right]) {
      left++;
      right--;
    } else if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return false;
}
```

## Why it works

At each step one half `[left, mid]` or `[mid, right]` is guaranteed non-decreasing. If the left half is sorted and `target` lies within `[nums[left], nums[mid])`, the answer can only be there, so discard the right; the symmetric rule handles a sorted right half. When the three probe values coincide the sorted-half test is inconclusive, so trimming both ends by one removes a duplicate without skipping any possible position, and the invariant is preserved.

## Complexity

- Time: O(log n) average; O(n) worst case when many duplicates force one-step trimming.
- Space: O(1) — only index variables.
