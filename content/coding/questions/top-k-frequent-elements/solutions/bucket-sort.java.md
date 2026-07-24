The key observation: a value can appear at most `n` times, so frequency is a small integer in the range `1..n`. That means you can bucket values by their exact count instead of comparing counts against each other — no sorting needed.

Build an array of buckets indexed by frequency, drop each value into the bucket matching its count, then walk the buckets from the highest frequency downward, collecting values until you have `k`. Every step is linear, so the whole thing runs in O(n).

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int n : nums) counts.merge(n, 1, Integer::sum);

        List<Integer>[] buckets = new List[nums.length + 1];
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            int count = e.getValue();
            if (buckets[count] == null) buckets[count] = new ArrayList<>();
            buckets[count].add(e.getKey());
        }
        int[] result = new int[k];
        int filled = 0;
        for (int freq = buckets.length - 1; freq > 0 && filled < k; freq--) {
            if (buckets[freq] == null) continue;
            for (int value : buckets[freq]) {
                result[filled++] = value;
                if (filled == k) break;
            }
        }
        java.util.Arrays.sort(result);
        return result;
    }
}
```

## Why it works

`buckets[f]` holds every value that occurs exactly `f` times, and `f` can never exceed `nums.length`, so the array is big enough. Scanning from the highest index down visits values in strictly decreasing frequency, so the first `k` collected are the `k` most frequent. Indexing by count replaces comparison-based sorting entirely. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n + k log k) — counting, filling buckets, and scanning are each linear in n; the final ascending sort of the k results costs O(k log k).
- Space: O(n) — the map and the bucket array together hold O(n) entries.
