Design a `Codec` that turns a binary tree into a single string (serialization) and can rebuild the exact same tree from that string (deserialization). The string doesn't need to be human-readable — the only requirement is that running deserialize on the output of serialize always reconstructs a tree with identical structure and node values to the original, including duplicate values and an empty tree.

## Examples

```text
Input:  root = [1, 2, 3, null, null, 4, 5]
Output: [1, 2, 3, null, null, 4, 5]
```

```text
Input:  root = []
Output: []
```

```text
Input:  root = [1]
Output: [1]
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

## Follow-up

Can you serialize and deserialize each in a single O(n) traversal without needing to know the tree's height or shape up front?
