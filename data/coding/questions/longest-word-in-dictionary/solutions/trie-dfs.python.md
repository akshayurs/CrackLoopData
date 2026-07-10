Insert every word into a trie, marking the node at the end of each word. Now "buildable" has a direct meaning on this structure: a node represents a buildable word exactly when every node on the path from the root down to it — not just the last one — is marked as an end-of-word. So a depth-first walk that only steps into children which are themselves end-of-word nodes visits precisely the set of buildable words, in one pass, without ever slicing a string to re-check a prefix.

Track the best word found during the walk the same way as before: longer wins, and a length tie goes to the lexicographically smaller string.

```python
class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False


def longest_word(words):
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    best = ""
    stack = [(root, "")]
    while stack:
        node, prefix = stack.pop()
        for ch, child in node.children.items():
            if child.is_end:
                word = prefix + ch
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
                stack.append((child, word))
    return best
```

## Why it works

Each edge walked during the DFS corresponds to typing one more letter, and the walk only continues through nodes flagged `is_end` — meaning the prefix formed so far is itself a real word. So every string the traversal reaches is guaranteed buildable, and since the trie is only as deep as the longest word, no candidate is ever missed. The length-then-lexicographic comparison at each visited node keeps the required best answer.

## Complexity

- Time: O(∑Lᵢ) — building the trie visits every character once; the traversal visits at most one node per character across all words.
- Space: O(∑Lᵢ) — trie nodes, one per distinct character position inserted.
