The simplest dictionary "implementation" doesn't build any tree at all — it just remembers every added word in a list. `addWord` is a single append. `search` compares the query against every stored word of the same length, treating each `.` as an automatic match for whatever letter sits in that position.

This is the honest baseline: correct and easy to write under pressure, but it re-scans everything stored so far on every query, and the comparison itself costs a full pass over the word.

```python
class WordDictionary:
    def __init__(self):
        self.words = []

    def addWord(self, word):
        self.words.append(word)

    def search(self, word):
        for w in self.words:
            if len(w) != len(word):
                continue
            if all(c == '.' or c == wc for c, wc in zip(word, w)):
                return True
        return False
```

## Why it works

`words` records everything added, duplicates included. For a query to match a stored word they must first be the same length, since `.` stands for exactly one letter, never zero or many. `zip(word, w)` pairs up characters position by position, and `all(...)` confirms every pair either has `.` on the query side or an identical letter on both sides — which is exactly the wildcard-match rule. The first stored word that satisfies this short-circuits the search.

## Complexity

- Time: O(1) for `addWord`; O(n * L) for `search`, where n is the number of stored words and L is the word length.
- Space: O(n * L) to store every added word.
