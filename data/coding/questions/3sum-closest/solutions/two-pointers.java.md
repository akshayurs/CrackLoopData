Sort the array first. Then fix the smallest element of the triple with an index `i` and let two pointers — `lo` just after `i` and `hi` at the end — sweep toward each other. Because the array is ordered, the sum tells you which way to move: too small means advance `lo` to grow it, too large means retreat `hi` to shrink it.

Sorting turns the third loop into a single linear sweep: for each `i` you scan the remaining window once instead of trying every pair, collapsing the cubic search to quadratic. Track the closest sum seen across all sweeps.

```java
import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int best = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; i++) {
            int lo = i + 1, hi = n - 1;
            while (lo < hi) {
                int s = nums[i] + nums[lo] + nums[hi];
                if (Math.abs(s - target) < Math.abs(best - target)) {
                    best = s;
                }
                if (s < target) lo++;
                else if (s > target) hi--;
                else return s;
            }
        }
        return best;
    }
}
```

## Why it works

For a fixed `i`, moving `lo` right can only increase the sum and moving `hi` left can only decrease it, since the array is sorted. Comparing `s` to `target` picks the one move that can bring the sum closer, and no promising pair is skipped. An exact hit (`s == target`) has distance 0, so it is immediately optimal and we return.

## Complexity

- Time: O(n²) — an O(n log n) sort plus, for each of n anchors, a linear two-pointer sweep.
- Space: O(1) — in-place sort aside, only a few indices.
