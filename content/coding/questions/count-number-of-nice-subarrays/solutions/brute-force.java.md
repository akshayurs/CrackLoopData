Start from every possible left endpoint and extend the subarray one element at a time, tallying odd numbers as you go. Each time the running count of odds equals `k`, you have found a nice subarray.

The one optimization over a pure triple-nested count: once the odd count passes `k`, no longer subarray starting here can help, so break early.

```java
class Solution {
    public int countNiceSubarrays(int[] nums, int k) {
        int total = 0;
        for (int i = 0; i < nums.length; i++) {
            int odds = 0;
            for (int j = i; j < nums.length; j++) {
                odds += nums[j] & 1;
                if (odds == k) {
                    total++;
                } else if (odds > k) {
                    break;
                }
            }
        }
        return total;
    }
}
```

## Why it works

Fixing the left end at `i` and sweeping the right end at `j` visits every contiguous subarray exactly once. `odds` is the number of odd values in `nums[i..j]`; whenever it hits `k` the window qualifies. Because odd counts only grow as `j` advances, exceeding `k` means every further extension is also too large, so breaking loses nothing.

## Complexity

- Time: O(n^2) — every start/end pair is considered.
- Space: O(1) — only a couple of counters.
