The most literal reading of the problem: for every node, look back at the full path from the root and ask whether anything on it beats the node's value. Track the path explicitly as you recurse, and at each node recompute the maximum of everything seen so far by scanning the whole path list.

It works, but it throws away information — the maximum of the path up to the parent was already known one call earlier, yet this approach re-derives it from scratch at every node.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private int count = 0;

    public int countGoodNodes(TreeNode root) {
        dfs(root, new ArrayList<>());
        return count;
    }

    private void dfs(TreeNode node, List<Integer> path) {
        if (node == null) {
            return;
        }
        path.add(node.val);
        int max = Integer.MIN_VALUE;
        for (int v : path) {
            max = Math.max(max, v);
        }
        if (node.val == max) {
            count++;
        }
        dfs(node.left, path);
        dfs(node.right, path);
        path.remove(path.size() - 1);
    }
}
```

## Why it works

`path` always holds the values from the root down to the current node, inclusive, because entries are added before recursing and removed after both subtrees return. A node is good exactly when its own value equals the maximum of that path — no ancestor exceeds it. Scanning `path` at every node is correct but redundant, since most of that list was already scanned one level up.

## Complexity

- Time: O(n * h) — each of the n nodes triggers an O(h) scan of its path, where h is the tree height (worst case O(n^2) on a skewed tree).
- Space: O(h) — the path list and recursion stack both grow to the height of the tree.
