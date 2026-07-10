Sort the array first so equal values sit next to each other and every subset comes out in ascending order. There are `2^n` possible subsets, so walk every integer mask from `0` to `2^n - 1`, treat each bit as "include this index," and build the subset that mask describes.

Duplicate values in `nums` mean different masks can build the exact same subset. Serialize each subset to a string key and stash it in a `HashMap` to collapse those repeats, then sort what's left — comparing element by element, the way tuple comparison works — so the final order is deterministic.

```java
import java.util.*;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        int n = sorted.length;
        Map<String, List<Integer>> byKey = new HashMap<>();
        for (int mask = 0; mask < (1 << n); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) subset.add(sorted[i]);
            }
            byKey.put(subset.toString(), subset);
        }
        List<List<Integer>> result = new ArrayList<>(byKey.values());
        result.sort((a, b) -> {
            int len = Math.min(a.size(), b.size());
            for (int i = 0; i < len; i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return a.size() - b.size();
        });
        return result;
    }
}
```

## Why it works

Every mask from `0` to `2^n - 1` corresponds to exactly one way of including/excluding each index, so the loop enumerates every possible subset at least once. Because the array is pre-sorted, two masks that pick the same multiset of values always build the same subset, so the string key collapses them in the map. The final comparator walks both subsets element by element and falls back to size when one is a prefix of the other — the same rule tuple comparison uses — so a shorter subset always sorts before a longer one that extends it, fixing a single canonical order.

## Complexity

- Time: O(n · 2^n) — 2^n masks, each costing O(n) to build and key.
- Space: O(n · 2^n) — up to 2^n subsets stored before deduping.
