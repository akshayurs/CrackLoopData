The same idea in Java: recurse over the array, and for each number try every bucket that still has room under the target sum. A full assignment wins if all buckets end up exactly at the target.

No memoization here — just the empty-bucket prune, which skips trying the same failed number in a second empty bucket.

```java
class Solution {
    private int[] buckets;
    private int target;

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int n : nums) total += n;
        if (total % k != 0) return false;
        target = total / k;
        buckets = new int[k];
        return backtrack(nums, 0);
    }

    private boolean backtrack(int[] nums, int i) {
        if (i == nums.length) {
            for (int b : buckets) {
                if (b != target) return false;
            }
            return true;
        }
        for (int j = 0; j < buckets.length; j++) {
            if (buckets[j] + nums[i] <= target) {
                buckets[j] += nums[i];
                if (backtrack(nums, i + 1)) return true;
                buckets[j] -= nums[i];
            }
            if (buckets[j] == 0) break;
        }
        return false;
    }
}
```

## Why it works

`buckets[j]` tracks the running sum of the j-th subset. A number is only placed where it fits under `target`, and a failed placement is undone before the next bucket is tried. The `if (buckets[j] == 0) break` prune skips redundant empty buckets, since a failed attempt in one empty bucket would fail identically in any other empty bucket. Success requires every bucket to land exactly on `target`.

## Complexity

- Time: O(k^n) — each of the n numbers can go into any of k buckets in the worst case.
- Space: O(k + n) — bucket sums plus the recursion stack.
