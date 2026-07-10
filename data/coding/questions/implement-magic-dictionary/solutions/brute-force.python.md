The simplest reading of the rule "changing exactly one character" is to just check it directly against every stored word: same length, and exactly one position differs. No trie, no preprocessing beyond keeping the list around.

It is the honest baseline you would state first in an interview before reaching for a trie.

```python
class MagicDictionary:
    def __init__(self):
        self.words = []

    def buildDict(self, words):
        self.words = words

    def search(self, word):
        for candidate in self.words:
            if len(candidate) != len(word):
                continue
            diff = sum(1 for a, b in zip(candidate, word) if a != b)
            if diff == 1:
                return True
        return False
```

## Why it works

`buildDict` just remembers the words. `search` scans every stored word, skips any whose length doesn't match (a length mismatch can never be a one-letter substitution), and counts differing positions with `zip`. A candidate qualifies only if exactly one position differs — zero differences means the words are identical, not a genuine change.

## Complexity

- Time: O(N·L) — each search compares against up to N stored words of length up to L.
- Space: O(N·L) — storing all the words.
