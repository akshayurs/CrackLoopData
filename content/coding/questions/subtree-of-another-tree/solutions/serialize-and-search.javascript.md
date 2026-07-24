Instead of re-comparing trees node by node, turn each tree into a single string and reduce the whole problem to substring search. If we serialize a tree with a preorder walk that records every node value *and* every empty slot, the string uniquely captures the tree's shape. Then `subRoot` is a subtree of `root` exactly when its serialization appears inside `root`'s serialization.

The two guards that make this correct are: a delimiter (`^`) written before every token so that value `2` never matches inside value `12`, and an explicit null marker (`#`) so that structure is preserved and a shorter tree cannot masquerade as part of a taller one.

```javascript
function isSubtree(root, subRoot) {
  function serialize(node) {
    if (node === null) return "^#";
    return "^" + node.val + serialize(node.left) + serialize(node.right);
  }

  return serialize(root).includes(serialize(subRoot));
}
```

## Why it works

Preorder with null markers is an invertible encoding: two subtrees produce the same string only if they are structurally identical with equal values. The leading `^` fixes each token's left boundary, so no partial-number or partial-token match can slip through, and `#` records the exact positions of missing children. Therefore the substring test is equivalent to "does some node in `root` head a subtree identical to `subRoot`?"

## Complexity

- Time: O(m + n) — building both serializations is linear, and the substring search runs in linear time with an efficient string matcher.
- Space: O(m + n) — the two serialized strings dominate.
