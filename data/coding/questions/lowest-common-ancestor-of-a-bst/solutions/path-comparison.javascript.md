Ignore the BST ordering for a moment and solve the general-tree version: find the root-to-node path for `p`, find the root-to-node path for `q`, then walk both paths together from the start. The last value where they still agree is the deepest shared ancestor.

Recording a path is plain DFS — push the current value, recurse into the children looking for the target, and pop it back out if neither side finds it.

```javascript
function findPath(node, target, path) {
  if (node === null) return false;
  path.push(node.val);
  if (node.val === target) return true;
  if (findPath(node.left, target, path) || findPath(node.right, target, path)) return true;
  path.pop();
  return false;
}

function lowestCommonAncestor(root, p, q) {
  const pathP = [];
  const pathQ = [];
  findPath(root, p, pathP);
  findPath(root, q, pathQ);
  let lca = pathP[0];
  for (let i = 0; i < pathP.length && i < pathQ.length; i++) {
    if (pathP[i] !== pathQ[i]) break;
    lca = pathP[i];
  }
  return lca;
}
```

## Why it works

Both paths start at the root, so their prefixes describe the same ancestors until the two nodes' branches actually diverge. The loop tracks the last value that still matched in both paths — that's precisely the deepest node both `p` and `q` descend from, including the case where one is an ancestor of the other.

## Complexity

- Time: O(n) — each path search may visit every node once.
- Space: O(n) — the recursion stack and the two stored paths can each grow to the tree's size.
