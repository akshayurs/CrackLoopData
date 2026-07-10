The same idea in Java: a bitmask tracks which numbers are used, and `remaining` tracks how much is left to fill the current bucket. Numbers are sorted descending first so impossible cases fail fast, and a `HashMap` memoizes on the combined `(mask, remaining)` state so repeated states are never re-explored.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[] nums;
    private int target;
    private int n;
    private Map<Long, Boolean> memo = new HashMap<>();

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int x : nums) total += x;
        if (total % k != 0) return false;
        target = total / k;
        Integer[] boxed = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) boxed[i] = nums[i];
        java.util.Arrays.sort(boxed, (a, b) -> b - a);
        this.nums = new int[boxed.length];
        for (int i = 0; i < boxed.length; i++) this.nums[i] = boxed[i];
        n = this.nums.length;
        if (this.nums[0] > target) return false;
        return dfs(0, target);
    }

    private boolean dfs(int mask, int remaining) {
        if (mask == (1 << n) - 1) return true;
        long key = ((long) mask << 20) | remaining;
        if (memo.containsKey(key)) return memo.get(key);
        boolean ok = false;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0 || nums[i] > remaining) continue;
            int nextRemaining = remaining - nums[i];
            if (nextRemaining == 0) nextRemaining = target;
            if (dfs(mask | (1 << i), nextRemaining)) {
                ok = true;
                break;
            }
        }
        memo.put(key, ok);
        return ok;
    }
}
```

## Why it works

`mask` records exactly which numbers are already assigned; `remaining` is how much room is left in the bucket currently being filled. Trying index `i` only when it is unused and fits within `remaining` mirrors plain backtracking, but whenever a bucket exactly fills (`nextRemaining == 0`) we reset to a fresh `target` and start the next bucket. Reaching the full mask means a valid k-way partition was built. Memoizing on the packed `(mask, remaining)` key avoids recomputing states reached by different orderings of the same used set.

## Complexity

- Time: O(n * 2^n) — at most 2^n distinct masks, each doing O(n) work to try the next number.
- Space: O(2^n) — the memo map, keyed by mask and remaining.
