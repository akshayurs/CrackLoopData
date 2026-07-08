We do not need to visit the whole tree — only the first `k` nodes in sorted order. An iterative in-order traversal driven by an explicit stack lets us pull those values out one at a time and stop the moment we pop the k-th one.

Push the entire left spine onto a stack, then repeatedly pop a node (that pop yields the next-smallest value), decrement `k`, and if it is not yet zero, dive into the popped node's right subtree and repeat. This never touches the nodes larger than the answer.

```python
def kth_smallest(root, k):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    return -1
```

## Why it works

The inner loop walks to the smallest unvisited node, stacking ancestors so we can return to them. Each pop emits the next value in ascending order, so the k-th pop is the k-th smallest. We return immediately, leaving every larger node untouched.

## Complexity

- Time: O(h + k) — we descend one path (height `h`) and then pop `k` nodes.
- Space: O(h) — the stack holds at most one root-to-leaf path.
