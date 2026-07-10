The hash-set version keeps re-slicing and re-hashing overlapping substrings, which is wasted work. A trie fixes that: insert every word once, then for each candidate word walk the trie one character at a time, checking at every step whether the current position marks the end of some dictionary word — no substring is ever materialized.

The same prefix DP as before rides along the walk: whenever the trie says "a word ends here," the DP boundary at that index becomes reachable, exactly like before but discovered incrementally instead of via repeated lookups.

```python
class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False

def find_concatenated_words(words):
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    result = []
    for word in words:
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            node = root
            for j in range(i + 1, n + 1):
                ch = word[j - 1]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end and not (i == 0 and j == n):
                    dp[j] = True
        if dp[n]:
            result.append(word)
    return sorted(result)
```

## Why it works

Starting a trie walk from every reachable boundary `i` (where `dp[i]` is true) and advancing one character at a time visits the same set of "is this chunk a word?" facts the hash-set DP checked, but each character is examined once per walk instead of being re-hashed inside every substring. Reaching a node with `is_end` set means `word[i:j]` is a dictionary word, so `dp[j]` becomes reachable — excluding `i == 0 and j == n` again blocks the trivial self-match.

## Complexity

- Time: O(n · L²) — n words, each with up to L trie walks of length up to L, no substring allocation.
- Space: O(n · L) — the trie holds at most that many characters.
