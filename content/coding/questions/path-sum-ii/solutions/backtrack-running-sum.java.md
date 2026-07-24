Instead of collecting every path and checking it afterward, carry the answer to "how much is left to reach `targetSum`" down the recursion itself. Subtract the current node's value from the remaining amount before descending; a leaf only qualifies if that remaining amount has hit exactly zero. There is no need to ever revisit a value once it has been folded into `remaining`.

The path buffer is still shared and backtracked the same way as the brute-force version, but now a path is copied into the result only when it is actually valid — never for a discarded candidate.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(root, targetSum, new ArrayList<>(), result);
        return result;
    }

    private void dfs(TreeNode node, int remaining, List<Integer> path, List<List<Integer>> result) {
        if (node == null) return;
        path.add(node.val);
        remaining -= node.val;
        if (node.left == null && node.right == null && remaining == 0) {
            result.add(new ArrayList<>(path));
        } else {
            dfs(node.left, remaining, path, result);
            dfs(node.right, remaining, path, result);
        }
        path.remove(path.size() - 1);
    }
}
```

## Why it works

`remaining` always equals `targetSum` minus the sum of the values on the current root-to-node path, so checking `remaining == 0` at a leaf is exactly checking that the full path sums to `targetSum` — without ever re-summing it. Because `remaining` is a primitive `int` argument, each recursive call gets its own copy, so returning from a call automatically restores the correct amount for the sibling branch. `path` is added to before recursing and trimmed after, so it always mirrors the current DFS stack, and left-before-right recursion keeps the output in DFS order.

## Complexity

- Time: O(n) — each node is visited once and does O(1) work beyond copying a path into the result, and the total copying cost is bounded by the size of the output.
- Space: O(h) — the recursion stack and `path` list are as deep as the tree height, on top of the space needed for the result itself.
