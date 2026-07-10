Instead of re-scanning the whole catalog for every prefix, build the answer once while inserting the products into a trie. Sort the catalog first, then insert products in that order; at every node along a word's path, append the word to that node's own suggestion list as long as it has fewer than three entries. Because insertion happens in sorted order, each node's list ends up already sorted — no extra work needed later.

Answering the query is now just a walk down the trie one character at a time: at each step read the current node's cached list. The moment a character has no matching child, every remaining prefix is a dead end and gets an empty list.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

def search_suggestions(products, search_word):
    root = TrieNode()
    for word in sorted(products):
        node = root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    result = []
    node = root
    dead = False
    for ch in search_word:
        if not dead:
            node = node.children.get(ch)
            dead = node is None
        result.append(node.suggestions if node else [])
    return result
```

## Why it works

Inserting products in sorted order means the first (at most) three words that ever pass through a node are, by construction, the three lexicographically smallest words sharing that node's prefix — exactly the suggestions the problem wants, already in order. Once the trie is built, each query character is a single dictionary lookup, so producing all `m` answer lists costs only O(m) node visits plus the O(1) cost of copying each cached list.

## Complexity

- Time: O(N log N + S + m) — sorting the catalog (N products), building the trie over S total characters, then O(m) to answer the query.
- Space: O(S) — the trie holds every character of every product, each node caching at most 3 strings.
