A **binary tree** is a set of nodes where each node holds a value and points to at most two children, `left` and `right`. A **binary search tree (BST)** adds one invariant: every node's left subtree holds smaller values and its right subtree holds larger ones. That invariant is what turns a tree into a fast lookup structure — O(log n) search on a balanced BST instead of O(n) for a plain tree.

Almost every tree problem is **recursion in disguise**. A tree is defined in terms of smaller trees (its subtrees), so the natural solution asks the same question of the left child, asks it of the right child, and combines the two answers at the current node. This "solve the subproblem, then combine" shape is why trees are the canonical example of divide-and-conquer thinking in interviews.

The other half of the pattern is **traversal order**, which decides what you see and when: preorder (node, left, right) is useful for copying/serializing a tree top-down; inorder (left, node, right) visits BST values in sorted order; postorder (left, right, node) is needed whenever a node's answer depends on both children's answers first (heights, sums, "balanced?" checks). Breadth-first traversal (level order, via a queue) instead visits the tree level by level, which is what you want for "shortest path," "level averages," or "right side view" questions.

A typical recursive shape:

```
function solve(node):
    if node is null:
        return base_case
    left_answer = solve(node.left)
    right_answer = solve(node.right)
    return combine(node.value, left_answer, right_answer)
```

Most trees you will see in interviews are not guaranteed balanced, so watch for the O(n) vs O(log n) distinction — and remember that a BST's ordering is a tool for pruning search, not a guarantee of balance.
