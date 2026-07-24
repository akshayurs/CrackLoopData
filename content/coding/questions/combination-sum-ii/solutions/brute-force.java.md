Explore every way of including or excluding each position: at index `i` you either take `candidates[i]` and recurse, or skip it and recurse. That walks every subset of the array, and any subset whose running sum lands exactly on the target gets recorded.

Duplicate values in the input mean different subsets of indices can produce the same list of numbers, so the raw hits need deduplication. Sorting the candidates first and collecting each hit into a `TreeSet` ordered lexicographically handles both the dedup and the final ordering in one structure.

```java
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        Set<List<Integer>> seen = new TreeSet<>((a, b) -> {
            for (int k = 0; k < Math.min(a.size(), b.size()); k++) {
                if (!a.get(k).equals(b.get(k))) return a.get(k) - b.get(k);
            }
            return a.size() - b.size();
        });
        backtrack(candidates, 0, target, new ArrayDeque<>(), seen);
        return new ArrayList<>(seen);
    }

    private void backtrack(int[] c, int i, int remaining, Deque<Integer> path, Set<List<Integer>> seen) {
        if (remaining == 0) {
            seen.add(new ArrayList<>(path));
            return;
        }
        if (remaining < 0 || i == c.length) return;
        path.addLast(c[i]);
        backtrack(c, i + 1, remaining - c[i], path, seen);
        path.removeLast();
        backtrack(c, i + 1, remaining, path, seen);
    }
}
```

## Why it works

Every combination corresponds to exactly one path through the include/exclude decision tree over indices, so nothing valid is missed. Sorting the array up front means each recorded path already lists its numbers ascending; the `TreeSet` with a lexicographic comparator collapses duplicate combinations and keeps the final result in the required order automatically.

## Complexity

- Time: O(2^n · n log n) — every index is included or excluded, and each of the up to 2^n paths costs O(n log n) to insert/order in the tree set.
- Space: O(2^n · n) — the set can hold up to 2^n combinations of length up to n.
