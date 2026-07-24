Take the definition literally: try removing each index in turn, and for every resulting array measure the longest stretch of consecutive `1`s. The best of those measurements is the answer.

Rather than physically rebuilding the array each time, just skip the deleted index while scanning and track the current run length, resetting it whenever a `0` is met.

```java
class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        int best = 0;
        for (int skip = 0; skip < n; skip++) {
            int run = 0;
            for (int i = 0; i < n; i++) {
                if (i == skip) continue;
                if (nums[i] == 1) {
                    run++;
                    best = Math.max(best, run);
                } else {
                    run = 0;
                }
            }
        }
        return best;
    }
}
```

## Why it works

Deleting index `skip` and then finding the longest consecutive `1`s is exactly the quantity the problem asks about for that one choice of deletion. By trying every possible `skip` we cover all deletions, and the maximum over them is optimal. The inner scan resets `run` at each `0`, so it only ever counts unbroken runs; the mandatory deletion is honoured because one index is always removed.

## Complexity

- Time: O(n^2) — for each of n deletions we rescan the whole array.
- Space: O(1) — only counters are kept.
