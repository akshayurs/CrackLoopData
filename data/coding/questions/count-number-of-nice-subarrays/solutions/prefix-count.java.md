Replace each number by its parity: odd becomes 1, even becomes 0. Now "exactly `k` odds in a subarray" is just "the values sum to `k`", and counting subarrays with a given sum is the classic prefix-sum trick.

Keep a running count of odds seen so far. A subarray ending at the current position has exactly `k` odds precisely when some earlier prefix had `odds - k` odds. A hash map of how many times each prefix count has occurred lets you add all such subarrays in O(1) per step. Seed it with `0 -> 1` so prefixes that start at index 0 are counted.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countNiceSubarrays(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        count.put(0, 1);
        int odds = 0, total = 0;
        for (int n : nums) {
            odds += n & 1;
            total += count.getOrDefault(odds - k, 0);
            count.put(odds, count.getOrDefault(odds, 0) + 1);
        }
        return total;
    }
}
```

## Why it works

`odds` is the number of odd values in `nums[0..i]`. A subarray `nums[j+1..i]` holds exactly `k` odds when `odds - prefix(j) == k`, i.e. `prefix(j) == odds - k`. `count` records how many earlier prefixes had each value, so `count.getOrDefault(odds - k, 0)` is exactly the number of valid left boundaries for the current right end. Recording the current prefix after the lookup keeps boundaries strictly earlier.

## Complexity

- Time: O(n) — one pass, O(1) map operations.
- Space: O(n) — the map stores up to n distinct prefix counts.
