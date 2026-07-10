The same idea in Java: two nested loops over the array, returning the first pair that reaches the target. No auxiliary storage.

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}
```

## Why it works

The outer loop fixes the first index; the inner loop scans every later index, so each unordered pair is tested exactly once. The first matching pair is returned immediately; the one-solution guarantee means the empty return is never hit.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — no extra structure.
