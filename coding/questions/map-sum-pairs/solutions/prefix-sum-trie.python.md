Push the summation work into `insert` instead of redoing it in every `sum` call. Build a trie over the key characters, and let every node cache the total value of all keys that pass through it. Then `sum(prefix)` just walks down to the node for `prefix` and reads its cached total — no scanning.

The only wrinkle is overwrites: if `"apple"` is inserted with 3 and later re-inserted with 2, every node on the `"apple"` path must lose 3 and gain 2, not gain both. Track each key's latest value in a side dictionary, compute `delta = new_val - old_val` on every insert, and add that delta (which can be negative) to every node along the path.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.total = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_vals = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_vals.get(key, 0)
        self.key_vals[key] = val
        node = self.root
        node.total += delta
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.total += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.total
```

## Why it works

`key_vals` remembers the current value of every key, so `delta` is exactly the change needed to bring every node on that key's path up to date — 0 on a first insert (relative to nothing), positive when a value grows, negative when it shrinks. Applying `delta` to every node from the root down to the last character of `key` keeps each node's `total` equal to the sum of all *current* key values that pass through it, because a key passes through a node exactly when the node's path is a prefix of that key. `sum(prefix)` walks the same path and returns the cached total directly, falling back to 0 the moment the path runs out (no key has that prefix).

## Complexity

- Time: O(L) for both `insert` and `sum`, where L is the length of the key or prefix.
- Space: O(n * L) in the worst case for the trie nodes and the `key_vals` map, where n is the number of distinct keys.
