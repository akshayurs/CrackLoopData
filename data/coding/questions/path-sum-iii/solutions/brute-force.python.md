The direct reading of the problem is "try every node as a path start." For a fixed starting node, walk downward through its descendants, keeping a running sum from that start, and count every descendant where the running sum hits `target_sum`.

Do that for every node in the tree — not just the root — since a valid path can begin anywhere.

```python
def path_sum(root, target_sum):
    if root is None:
        return 0
    return (
        count_from(root, target_sum)
        + path_sum(root.left, target_sum)
        + path_sum(root.right, target_sum)
    )


def count_from(node, remaining):
    if node is None:
        return 0
    count = 1 if node.val == remaining else 0
    count += count_from(node.left, remaining - node.val)
    count += count_from(node.right, remaining - node.val)
    return count
```

## Why it works

`path_sum` visits every node as a candidate path start, and `count_from` explores every downward path beginning there, decrementing the remaining target by each node's value until it either hits zero (a match) or the branch runs out. Between the two functions every downward path in the tree gets considered exactly once.

## Complexity

- Time: O(n^2) — in the worst case (a skewed tree) `count_from` is called from every node and walks O(n) further nodes.
- Space: O(h) — recursion depth is bounded by the tree height h.
