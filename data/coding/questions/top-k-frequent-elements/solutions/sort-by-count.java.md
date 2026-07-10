Start with the obvious plan: count how many times each value appears, then rank the distinct values by that count. A `HashMap` builds the counts in one pass, and sorting the distinct values by their frequency puts the most common ones at the front.

Once sorted, the answer is just the first `k` values. The counting is linear, but the sort of the distinct values is what dominates the running time.

```java
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int n : nums) {
            counts.merge(n, 1, Integer::sum);
        }
        List<Integer> ordered = new java.util.ArrayList<>(counts.keySet());
        ordered.sort((a, b) -> counts.get(b) - counts.get(a));
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = ordered.get(i);
        }
        java.util.Arrays.sort(result);
        return result;
    }
}
```

## Why it works

`counts` maps each value to its number of occurrences. Sorting the distinct values by `counts.get(value)` in descending order lines them up from most to least frequent, so taking the first `k` gives exactly the `k` most common values. Because the answer is guaranteed unique, there is no tie to break at the boundary. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct values costs O(n log n); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the map and the list each hold up to n entries.
