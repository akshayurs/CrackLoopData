Reach for a tree traversal or recursion the moment a problem gives you a `TreeNode` with `left`/`right` pointers, or describes any of these shapes:

- **"Depth / height / diameter / balanced?"** — anything about the shape of the tree needs a postorder recursion that returns info about subtrees to their parent.
- **"Is this a valid BST?" / "Kth smallest in a BST"** — the ordering invariant means inorder traversal visits values in sorted order.
- **"Level order" / "level averages" / "zigzag" / "right side view"** — process the tree one level at a time, which signals BFS with a queue, not plain recursion.
- **"Path sum" / "path from root to leaf" / "maximum path sum"** — carry a running value down the recursion (root-to-leaf) or combine left+right at each node (any-node-to-any-node paths).
- **"Lowest common ancestor"** — find where two search paths diverge; the BST version prunes using value comparisons, the plain binary tree version needs both subtrees searched.
- **"Serialize / deserialize" / "construct tree from traversals"** — encode/decode structure using preorder or level order, and rebuild recursively using index ranges.
- **"Same tree" / "subtree of another tree" / "symmetric tree"** — structural comparison, usually two trees walked in lockstep.

Signal words: *"binary tree"*, *"binary search tree"*, *"root"*, *"leaf"*, *"ancestor"*, *"level"*, *"depth"*, *"subtree"*. If the input is a linked structure with at most two children per node, trees are the pattern — the only real decision left is DFS (recursion/stack) vs BFS (queue), and whether you need pre/in/postorder.
