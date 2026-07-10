The direct reading of the problem is "try every node as a path start." For a fixed starting node, walk downward through its descendants, keeping a running sum from that start, and count every descendant where the running sum hits `targetSum`.

Do that for every node in the tree — not just the root — since a valid path can begin anywhere.

```javascript
function pathSum(root, targetSum) {
  if (root === null) return 0;
  return (
    countFrom(root, targetSum) +
    pathSum(root.left, targetSum) +
    pathSum(root.right, targetSum)
  );
}

function countFrom(node, remaining) {
  if (node === null) return 0;
  let count = node.val === remaining ? 1 : 0;
  count += countFrom(node.left, remaining - node.val);
  count += countFrom(node.right, remaining - node.val);
  return count;
}
```

## Why it works

`pathSum` visits every node as a candidate path start, and `countFrom` explores every downward path beginning there, decrementing the remaining target by each node's value until it either hits zero (a match) or the branch runs out. Between the two functions every downward path in the tree gets considered exactly once.

## Complexity

- Time: O(n^2) — in the worst case (a skewed tree) `countFrom` is called from every node and walks O(n) further nodes.
- Space: O(h) — recursion depth is bounded by the tree height h.
