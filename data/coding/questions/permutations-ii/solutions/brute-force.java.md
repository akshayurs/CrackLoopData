The same idea in Java: build every position-based arrangement of the array, as if the values were all distinct, then let a set of lists collapse the ones that repeat.

A recursive backtrack over indices produces all `n!` orderings. `List<Integer>` has value-based `equals`/`hashCode`, so putting the finished permutations into a `HashSet` deduplicates them by content for free; sorting the survivors makes the result deterministic.

```java
import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> raw = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, new ArrayList<>(), raw);

        List<List<Integer>> unique = new ArrayList<>(new HashSet<>(raw));
        unique.sort((a, b) -> {
            for (int i = 0; i < a.size(); i++) {
                int cmp = Integer.compare(a.get(i), b.get(i));
                if (cmp != 0) return cmp;
            }
            return 0;
        });
        return unique;
    }

    private void backtrack(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> raw) {
        if (current.size() == nums.length) {
            raw.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            backtrack(nums, used, current, raw);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}
```

## Why it works

The backtrack picks every unused index at each depth, so it enumerates all `n!` position-based orderings regardless of repeated values. Two orderings with identical values in identical positions are equal `List`s, so the `HashSet` merges them into one entry. Sorting the surviving lists lexicographically only fixes presentation order.

## Complexity

- Time: O(n! · n) — n! permutations, each O(n) to build, hash, and compare during sort.
- Space: O(n! · n) — every raw permutation is held in memory before deduplication.
