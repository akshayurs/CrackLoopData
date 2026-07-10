Walk the tree in preorder — root, then left, then right — and record every value as you visit it, writing a sentinel like `'#'` wherever a child is missing. That single string captures the whole shape: because preorder always visits a node before its subtrees, replaying the same tokens in the same order rebuilds the tree exactly.

Deserializing reverses the walk. Split the string back into tokens and consume them one at a time with a shared index; a sentinel means that subtree is `null`, otherwise build a node and recursively fill its left and right children from the same token stream, in the same left-then-right order they were written.

```javascript
class Codec {
  serialize(root) {
    const vals = [];
    const dfs = (node) => {
      if (node === null) {
        vals.push('#');
        return;
      }
      vals.push(String(node.val));
      dfs(node.left);
      dfs(node.right);
    };
    dfs(root);
    return vals.join(',');
  }

  deserialize(data) {
    const tokens = data.split(',');
    let i = 0;
    const build = () => {
      const val = tokens[i++];
      if (val === '#') return null;
      const node = new TreeNode(Number(val));
      node.left = build();
      node.right = build();
      return node;
    };
    return build();
  }
}
```

## Why it works

Preorder order is unambiguous: a node's token is always immediately followed by the complete encoding of its left subtree, then its right subtree. Because deserialize reads tokens off the same array in that exact order, each recursive call lands on the right next token without needing to store subtree lengths.

## Complexity

- Time: O(n) — serialize visits every node once; deserialize consumes every token once.
- Space: O(n) — the token array holds one entry per node (plus nulls); the recursion stack is O(h).
