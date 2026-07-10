Push the summation work into `insert` instead of redoing it in every `sum` call. Build a trie over the key characters, and let every node cache the total value of all keys that pass through it. Then `sum(prefix)` just walks down to the node for `prefix` and reads its cached total — no scanning.

The only wrinkle is overwrites: if `"apple"` is inserted with 3 and later re-inserted with 2, every node on the `"apple"` path must lose 3 and gain 2, not gain both. Track each key's latest value in a side map, compute `delta = newVal - oldVal` on every insert, and add that delta (which can be negative) to every node along the path.

```java
import java.util.HashMap;
import java.util.Map;

class MapSum {
    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        int total = 0;
    }

    private final TrieNode root = new TrieNode();
    private final Map<String, Integer> keyVals = new HashMap<>();

    public void insert(String key, int val) {
        int delta = val - keyVals.getOrDefault(key, 0);
        keyVals.put(key, val);
        TrieNode node = root;
        node.total += delta;
        for (char ch : key.toCharArray()) {
            node = node.children.computeIfAbsent(ch, c -> new TrieNode());
            node.total += delta;
        }
    }

    public int sum(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            node = node.children.get(ch);
            if (node == null) {
                return 0;
            }
        }
        return node.total;
    }
}
```

## Why it works

`keyVals` remembers the current value of every key, so `delta` is exactly the change needed to bring every node on that key's path up to date — 0 on a first insert (relative to nothing), positive when a value grows, negative when it shrinks. Applying `delta` to every node from the root down to the last character of `key` keeps each node's `total` equal to the sum of all *current* key values that pass through it, because a key passes through a node exactly when the node's path is a prefix of that key. `sum(prefix)` walks the same path and returns the cached total directly, returning 0 the moment the path runs out (no key has that prefix).

## Complexity

- Time: O(L) for both `insert` and `sum`, where L is the length of the key or prefix.
- Space: O(n * L) in the worst case for the trie nodes and the `keyVals` map, where n is the number of distinct keys.
