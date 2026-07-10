The key observation: when you split a rotated sorted array at any midpoint, at least one of the two halves is still perfectly sorted. Compare the midpoint against the ends to figure out which half that is, then check whether the target lies inside that sorted half's value range. If it does, search there; otherwise the target must be in the other half. Each step halves the search space, giving `O(log n)`.

Concretely: if `nums[low] <= nums[mid]`, the left half is sorted; the target belongs there only when `nums[low] <= target < nums[mid]`. Otherwise the right half is sorted and you apply the mirror test.

```java
class Solution {
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

## Why it works

A single rotation of a sorted array leaves one contiguous sorted run on each side of any pivot point, so one half around `mid` is always sorted. Once you know which half is sorted, its range is defined by two known endpoints, and a range check tells you definitively whether the target can be inside. Discarding the half that cannot contain the target preserves correctness while cutting the window in half every iteration.

## Complexity

- Time: O(log n) — the search interval halves each step.
- Space: O(1) — only a few index variables.
