Split the four arrays into two halves. Precompute every pairwise sum `a[i] + b[j]` and tally how often each sum occurs in a `HashMap`. Then, for every pair from `c` and `d`, the tuple sums to zero exactly when `a[i] + b[j] == -(c[k] + d[l])`, so you just look up how many left-half pairs produce that complement.

This turns two of the four loops into O(1) map lookups: `n²` pairs on the left build the map, `n²` pairs on the right query it, and the stored count contributes all matching tuples at once.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int fourSumCount(int[] a, int[] b, int[] c, int[] d) {
        Map<Integer, Integer> left = new HashMap<>();
        for (int x : a)
            for (int y : b)
                left.merge(x + y, 1, Integer::sum);
        int count = 0;
        for (int z : c)
            for (int w : d)
                count += left.getOrDefault(-(z + w), 0);
        return count;
    }
}
```

## Why it works

`left` maps a pairwise sum to how many `(i, j)` pairs produce it. A full tuple sums to zero iff its right-half sum `c[k] + d[l]` cancels some left-half sum, i.e. `left` holds `-(c[k] + d[l])`. Adding that stored count folds in every matching `(i, j)` pair in one step, so no tuple is missed or double-counted.

## Complexity

- Time: O(n²) — one `n²` pass to build the map, one `n²` pass to query it.
- Space: O(n²) — the map holds up to n² distinct pairwise sums.
