Forget for a moment that this is a search tree and treat it as any old binary tree. The lowest common ancestor is where the root-to-`p` path and the root-to-`q` path stop overlapping: both routes leave the root together, march down the same nodes for a while, then diverge. The last node they share is the LCA.

So collect the full path from the root to each target, then walk the two paths in lockstep and remember the deepest node that is still identical in both.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, int p, int q) {
        List<TreeNode> pathP = new ArrayList<>();
        List<TreeNode> pathQ = new ArrayList<>();
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        TreeNode ancestor = null;
        int n = Math.min(pathP.size(), pathQ.size());
        for (int i = 0; i < n; i++) {
            if (pathP.get(i) == pathQ.get(i)) ancestor = pathP.get(i);
            else break;
        }
        return ancestor;
    }

    private boolean findPath(TreeNode node, int target, List<TreeNode> trail) {
        if (node == null) return false;
        trail.add(node);
        if (node.val == target) return true;
        if (findPath(node.left, target, trail) || findPath(node.right, target, trail)) return true;
        trail.remove(trail.size() - 1);
        return false;
    }
}
```

## Why it works

`findPath` does a depth-first search, adding nodes as it descends and removing them on the way back up, so when it returns `true` the `trail` holds exactly the nodes from the root down to the target. Two such paths share a common prefix — the ancestors both nodes descend from — and the moment they differ marks the split point. The last matching node is therefore the deepest common ancestor.

## Complexity

- Time: O(n) — each path search may visit every node.
- Space: O(n) — the recursion stack and stored paths grow with the tree height, up to O(n) when skewed.
