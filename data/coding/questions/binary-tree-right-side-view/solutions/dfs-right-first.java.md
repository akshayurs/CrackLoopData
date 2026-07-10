A queue is not required if the traversal visits nodes in the right order: walk the right child before the left child, and the first time a given depth is reached, that node must be the rightmost one at that depth — anything visited later at the same depth is further left and should be ignored.

This turns the problem into a single depth-first pass carrying the current depth, with the result list itself doubling as the "have I seen this depth yet?" check.

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        dfs(root, 0, result);
        return result;
    }

    private void dfs(TreeNode node, int depth, List<Integer> result) {
        if (node == null) return;
        if (depth == result.size()) {
            result.add(node.val);
        }
        dfs(node.right, depth + 1, result);
        dfs(node.left, depth + 1, result);
    }
}
```

## Why it works

Recursing into the right subtree before the left guarantees that, for any given depth, the first node the traversal reaches is the rightmost one. `depth == result.size()` is true exactly once per depth — at that first visit — so later, more-left nodes at the same depth see `depth < result.size()` and add nothing.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) — the recursion stack depth is the tree's height, plus O(n) for the output list.
