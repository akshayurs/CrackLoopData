The most literal reading of the problem: for every node, look back at the full path from the root and ask whether anything on it beats the node's value. Track the path explicitly as you recurse, and at each node recompute the maximum of everything seen so far by scanning the whole path array.

It works, but it throws away information — the maximum of the path up to the parent was already known one call earlier, yet this approach re-derives it from scratch at every node.

```javascript
function countGoodNodes(root) {
  let count = 0;

  function dfs(node, path) {
    if (node === null) return;
    path.push(node.val);
    if (node.val === Math.max(...path)) count++;
    dfs(node.left, path);
    dfs(node.right, path);
    path.pop();
  }

  dfs(root, []);
  return count;
}
```

## Why it works

`path` always holds the values from the root down to the current node, inclusive, because entries are pushed before recursing and popped after both subtrees return. A node is good exactly when its own value equals the maximum of that path — no ancestor exceeds it. Scanning `path` with `Math.max` at every node is correct but redundant, since most of that array was already scanned one level up.

## Complexity

- Time: O(n * h) — each of the n nodes triggers an O(h) scan of its path, where h is the tree height (worst case O(n^2) on a skewed tree).
- Space: O(h) — the path array and recursion stack both grow to the height of the tree.
