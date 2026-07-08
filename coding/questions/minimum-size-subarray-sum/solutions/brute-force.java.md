Start from every index and extend a window rightward, accumulating the sum until it reaches `target`. The moment a start position produces a qualifying window, record its length and break — no shorter window can begin at that same start.

Because all values are positive, the running sum only grows as the window widens, so the inner scan stops as soon as `target` is met.

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int best = n + 1;
        for (int start = 0; start < n; start++) {
            long total = 0;
            for (int end = start; end < n; end++) {
                total += nums[end];
                if (total >= target) {
                    best = Math.min(best, end - start + 1);
                    break;
                }
            }
        }
        return best <= n ? best : 0;
    }
}
```

## Why it works

Every possible starting index is tried, and for each one the window grows until it first hits `target`. Since positive values guarantee a monotonically increasing sum, the first qualifying window from a given start is also the shortest from that start. Taking the minimum over all starts yields the global answer; `best` staying above `n` means nothing ever reached `target`.

## Complexity

- Time: O(n²) — each start scans up to the end of the array.
- Space: O(1) — only a few counters are kept.
