Instead of rescanning the dictionary for every word, build it into a trie once. Each root marks the node at the end of its path as a root-end. Then, to resolve a word, just walk the trie one character at a time — the instant you land on a node marked as a root-end, that path is the shortest matching root, so you can stop immediately.

This turns the per-word cost from "scan every root" into "walk your own characters," which is exactly the preprocessing the follow-up asks for.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_root_end = False

def replace_words(dictionary, sentence):
    trie_root = TrieNode()
    for root in dictionary:
        node = trie_root
        for ch in root:
            node = node.children.setdefault(ch, TrieNode())
        node.is_root_end = True

    def shortest_root(word):
        node = trie_root
        for i, ch in enumerate(word):
            if ch not in node.children:
                return word
            node = node.children[ch]
            if node.is_root_end:
                return word[:i + 1]
        return word

    return " ".join(shortest_root(w) for w in sentence.split(" "))
```

## Why it works

Every root's characters form a path from `trie_root`, ending at a node flagged `is_root_end`. Walking a word down that same structure follows the unique path spelled by its own letters; the first `is_root_end` node hit is, by construction, the shortest root that is a prefix of the word, so returning there is safe. If the walk falls off the trie or never hits a marked node, no root matches and the word is returned untouched.

## Complexity

- Time: O(R + wL) — R is the total characters across all dictionary roots (built once); each word of length L is resolved in O(L) by walking its own characters.
- Space: O(R) — the trie stores at most one node per distinct character position across all roots.
