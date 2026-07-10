Think of building a subset one decision at a time: walk the array left to right, and at each index either take the element or skip it. Recording the current partial subset *at every step of the walk* — not just at the end — captures every prefix-consistent combination, because every subset is exactly the set of elements taken along one root-to-node path of that decision tree.

Passing a `start` index instead of a "used" flag per element avoids ever revisiting an earlier index, so each combination is built in increasing index order and produced exactly once — no duplicate subsets to filter out.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        result.sort((a, b) -> {
            if (a.size() != b.size()) return a.size() - b.size();
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return 0;
        });
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> result) {
        result.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

## Why it works

`backtrack(start)` first records the current `path` as a valid subset — including the empty one on the first call — then tries extending it with every element from `start` onward. Recursing with `i + 1` forbids picking an earlier index again, so the same set of values can never be assembled twice. Removing the last element after the recursive call restores `path` before the next sibling choice is tried, which is the "undo" step that makes it backtracking.

## Complexity

- Time: O(n * 2^n) — there are 2^n nodes in the recursion tree, and copying `path` at each costs up to O(n).
- Space: O(n * 2^n) for the output, plus O(n) recursion depth for `path` itself.
