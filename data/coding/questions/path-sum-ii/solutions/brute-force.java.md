The most direct reading: find *every* root-to-leaf path first, ignoring the target entirely, then go back and keep only the ones that happen to add up to `targetSum`. Recording a path is a depth-first walk that adds the current value, recurses, and removes it again before returning to the parent — backtracking so one list serves every branch.

Once every path is collected, filtering is a second, separate pass: sum each stored path and compare it to `targetSum`. It works, but it does strictly more work than necessary since most collected paths are usually discarded.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> allPaths = new ArrayList<>();
        collect(root, new ArrayList<>(), allPaths);

        List<List<Integer>> result = new ArrayList<>();
        for (List<Integer> path : allPaths) {
            int total = 0;
            for (int v : path) total += v;
            if (total == targetSum) result.add(path);
        }
        return result;
    }

    private void collect(TreeNode node, List<Integer> path, List<List<Integer>> allPaths) {
        if (node == null) return;
        path.add(node.val);
        if (node.left == null && node.right == null) {
            allPaths.add(new ArrayList<>(path));
        } else {
            collect(node.left, path, allPaths);
            collect(node.right, path, allPaths);
        }
        path.remove(path.size() - 1);
    }
}
```

## Why it works

`collect` performs a standard DFS, growing `path` on the way down and shrinking it on the way back up, so by the time a leaf is reached `path` holds exactly the values from the root to that leaf. Copying it into `allPaths` at each leaf preserves left-to-right, root-to-leaf order across the whole tree. The final loop then re-derives each path's sum independently and keeps only the matches.

## Complexity

- Time: O(n^2) — the DFS visits every node once, but each of the up to O(n) leaf paths can be O(n) long, and both copying and summing a path cost O(path length).
- Space: O(n^2) — `allPaths` retains every root-to-leaf path, not just the matching ones, before filtering.
