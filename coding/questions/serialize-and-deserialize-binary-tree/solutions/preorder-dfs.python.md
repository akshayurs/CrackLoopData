Walk the tree in preorder — root, then left, then right — and write down every value as you visit it, using a sentinel like `#` wherever a child is missing. That single string encodes the whole shape: because preorder always visits a node before its subtrees, replaying the same tokens in the same order recreates the tree without any extra bookkeeping.

Deserializing just reverses the walk. Read one token at a time from an iterator; if it's the sentinel, that subtree is `None`, otherwise build a node and recursively fill its left and right children from the *same* stream of tokens, in the same left-then-right order they were written.

```python
class Codec:
    def serialize(self, root):
        vals = []

        def dfs(node):
            if node is None:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        tokens = iter(data.split(','))

        def build():
            val = next(tokens)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
```

## Why it works

Preorder order is unambiguous: a node's token is always immediately followed by the complete encoding of its left subtree, then its right subtree. Since deserialize consumes tokens off the same iterator in that exact order, each recursive call naturally lands on the correct next token — no lengths or indices need to be stored separately.

## Complexity

- Time: O(n) — serialize visits every node once; deserialize consumes every token once.
- Space: O(n) — the token string holds one entry per node (plus nulls); the recursion stack is O(h).
