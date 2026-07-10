Instead of generating everything and filtering, build combinations one number at a time and abandon a partial choice the moment it can no longer succeed. Track a `path` of numbers picked so far and a `start` index; at each step try every candidate from `start` up to `n`, recurse, then undo the pick before trying the next candidate.

The key prune: if `path` needs `remainingNeeded` more numbers, there is no point starting past `n - remainingNeeded + 1`, since not enough numbers would be left to finish the combination. Because candidates are always tried in increasing order, combinations are produced already in lexicographic order — no sort needed.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), 1, n, k);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> path, int start, int n, int k) {
        if (path.size() == k) {
            result.add(new ArrayList<>(path));
            return;
        }
        int remainingNeeded = k - path.size();
        for (int i = start; i <= n - remainingNeeded + 1; i++) {
            path.add(i);
            backtrack(result, path, i + 1, n, k);
            path.remove(path.size() - 1);
        }
    }
}
```

## Why it works

The recursion explores a decision tree where each level picks the next number to add, always larger than the last pick — this guarantees no combination is produced twice and every combination is already sorted internally. Removing the last element after each recursive call restores the state, so sibling branches start clean. The bound `n - remainingNeeded + 1` prunes branches that cannot possibly reach size `k`, skipping work the brute-force approach would otherwise waste on doomed subsets.

## Complexity

- Time: O(k * C(n, k)) — there are C(n, k) complete combinations, each costing O(k) to copy into the result.
- Space: O(k) — recursion depth and the `path` buffer, excluding the returned combinations.
