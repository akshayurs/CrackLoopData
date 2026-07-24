Ignore the BST ordering for a moment and solve the general-tree version: find the root-to-node path for `p`, find the root-to-node path for `q`, then walk both paths together from the start. The last value where they still agree is the deepest shared ancestor.

Recording a path is plain DFS — append the current value, recurse into the children looking for the target, and remove it again if neither side finds it.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private boolean findPath(TreeNode node, int target, List<Integer> path) {
        if (node == null) return false;
        path.add(node.val);
        if (node.val == target) return true;
        if (findPath(node.left, target, path) || findPath(node.right, target, path)) return true;
        path.remove(path.size() - 1);
        return false;
    }

    public int lowestCommonAncestor(TreeNode root, int p, int q) {
        List<Integer> pathP = new ArrayList<>();
        List<Integer> pathQ = new ArrayList<>();
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        int lca = pathP.get(0);
        for (int i = 0; i < pathP.size() && i < pathQ.size(); i++) {
            if (!pathP.get(i).equals(pathQ.get(i))) break;
            lca = pathP.get(i);
        }
        return lca;
    }
}
```

## Why it works

Both paths start at the root, so their prefixes describe the same ancestors until the two nodes' branches actually diverge. The loop tracks the last value that still matched in both paths — that's precisely the deepest node both `p` and `q` descend from, including the case where one is an ancestor of the other.

## Complexity

- Time: O(n) — each path search may visit every node once.
- Space: O(n) — the recursion stack and the two stored paths can each grow to the tree's size.
