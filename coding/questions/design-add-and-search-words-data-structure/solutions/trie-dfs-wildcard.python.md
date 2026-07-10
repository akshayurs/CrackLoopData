Build a real trie so `addWord` shares structure between words the way `Trie.insert` does: each node holds 26 child slots, one per lowercase letter, plus a flag marking whether a word ends there. Adding a word walks down one character at a time, creating child nodes as needed.

The wildcard is what makes `search` more than a plain trie walk. At an ordinary letter, follow the single matching child, exactly as before. At a `.`, the query doesn't commit to one branch — it means "try every child here and succeed if any of them lead to a match," so `search` becomes a small depth-first exploration that only branches at dots and stays a single path everywhere else.

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_word = True

    def search(self, word):
        def dfs(node, i):
            if node is None:
                return False
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch != '.':
                return dfs(node.children[ord(ch) - ord('a')], i + 1)
            return any(dfs(child, i + 1) for child in node.children)
        return dfs(self.root, 0)
```

## Why it works

Each `TrieNode` groups the 26 possible next letters, so words sharing a prefix share the same chain of nodes. `dfs` advances one query character per call: a concrete letter narrows the search to exactly one child, while `.` fans out over every non-null child and succeeds if any branch eventually reaches the end of `word` on a node flagged as a word ending. Returning `False` on a `None` node prunes dead branches immediately instead of exploring further. Because dots only appear a handful of times per query (bounded by the constraints), the fan-out stays cheap in practice even though it is exponential in the dot count.

## Complexity

- Time: O(L) for `addWord`. `search` is O(26^d * L) in the worst case, where L is the word length and d is the number of dots; with few dots this is close to O(L).
- Space: O(total characters added), since each new character can create one new node; shared prefixes reuse existing nodes.
