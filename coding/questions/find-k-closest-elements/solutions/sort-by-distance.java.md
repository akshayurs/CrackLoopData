The most direct reading of the problem: rank every element by how far it is from `x`, keep the best `k`, then put them back in order. Sort boxed values by distance first and, for ties, by value so the smaller one wins.

Taking the first `k` of that ordering gives the closest set; a final ascending sort restores the required output order.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> vals = new ArrayList<>();
        for (int a : arr) vals.add(a);
        vals.sort((a, b) -> {
            int da = Math.abs(a - x), db = Math.abs(b - x);
            return da == db ? Integer.compare(a, b) : Integer.compare(da, db);
        });
        List<Integer> result = new ArrayList<>(vals.subList(0, k));
        Collections.sort(result);
        return result;
    }
}
```

## Why it works

The comparator orders by distance first and, on ties, by value — so equal-distance elements place the smaller one earlier, matching the tie-break rule. The first `k` entries are the closest integers. Because the answer must be ascending, `Collections.sort` reorders that sublist by value.

## Complexity

- Time: O(n log n) — dominated by the distance sort over all n elements.
- Space: O(n) — the boxed list of values.
