The definition of the problem hands you the baseline: a subarray is fixed by its start and end, so try every pair. Anchor a starting index, then walk forward, keeping a running sum of the elements you pass. Every time that running sum hits `k`, you have found one more qualifying subarray.

Accumulating the sum as the end index moves means you never re-add elements from scratch, so this is two loops rather than three — still quadratic, but the honest starting point before reaching for a hash map.

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int n = nums.length;
        for (int start = 0; start < n; start++) {
            int total = 0;
            for (int end = start; end < n; end++) {
                total += nums[end];
                if (total == k) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Why it works

For a fixed `start`, the inner loop produces the sum of every subarray beginning at `start` — first just `nums[start]`, then `nums[start] + nums[start+1]`, and so on. Because `total` carries over between iterations, extending the window by one element costs a single addition. Checking `total == k` at each step counts every subarray exactly once, and negative numbers are handled naturally since we test after every extension rather than stopping early.

## Complexity

- Time: O(n²) — for each of n start positions we may scan to the end.
- Space: O(1) — only the running sum and a counter.
