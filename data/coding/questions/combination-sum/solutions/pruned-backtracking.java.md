Once the candidates are sorted, a wasted branch becomes easy to spot early: if the current candidate already exceeds what's left to reach the target, every candidate after it (all larger) will too, so the whole rest of the loop can be skipped instead of merely skipped-per-branch at the base case.

That one change — breaking out of the loop instead of recursing one level deeper only to fail — is what turns the same index-based backtracking into something that stops fanning out the moment a subtree is provably useless.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int remaining, int start,
                            List<Integer> path, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) {
                break;
            }
            path.add(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

## Why it works

Because `candidates` is sorted, the moment `candidates[i] > remaining` is true, every candidate after it is also too large — `break` discards all of them in one step instead of recursing into each and failing individually. The `start` index still prevents duplicate orderings of the same multiset, and the base case still fires exactly when a path sums to `target`, so the set of results is identical to the unpruned version; only the amount of wasted work changes.

## Complexity

- Time: O(N^(T/M + 1)) — N is the candidate count, T the target, M the smallest candidate; that bounds the depth and branching of the pruned tree.
- Space: O(target) — the recursion depth and `path` are bounded by how many times the smallest candidate divides into `target`.
