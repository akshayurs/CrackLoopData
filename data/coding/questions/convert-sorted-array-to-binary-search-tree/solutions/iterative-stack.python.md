Recursion is the natural fit here, but it ties one stack frame to every pending subtree. You can get the same result by managing that "pending work" yourself with an explicit stack of `(node, lo, hi)` frames instead of letting the language do it.

Create the root from the middle of the full range, then repeatedly pop a frame, recompute its middle, and — for whichever side still has elements — create that child up front and push a new frame so its own subtree gets built the same way later.

```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    n = len(nums)
    root = TreeNode(nums[(n - 1) // 2])
    stack = [(root, 0, n - 1)]
    while stack:
        node, lo, hi = stack.pop()
        mid = lo + (hi - lo) // 2
        if lo <= mid - 1:
            left_mid = lo + ((mid - 1) - lo) // 2
            node.left = TreeNode(nums[left_mid])
            stack.append((node.left, lo, mid - 1))
        if mid + 1 <= hi:
            right_mid = (mid + 1) + (hi - (mid + 1)) // 2
            node.right = TreeNode(nums[right_mid])
            stack.append((node.right, mid + 1, hi))
    return root
```

## Why it works

Each frame owns a slice `[lo, hi]` of the array whose middle element already sits at `node`. Popping the frame and picking `mid` again tells us exactly which indices still need a left child and a right child; creating those children immediately and pushing their own `(lo, hi)` ranges means every remaining slice eventually gets its turn. Because the middle index is always the same floor-division formula, the tree shape matches the recursive version exactly, and it's built without ever growing the call stack.

## Complexity

- Time: O(n) — every element becomes exactly one node, and each is pushed and popped once.
- Space: O(log n) — the explicit stack holds at most one pending frame per level of the balanced tree, excluding the O(n) output tree itself.
