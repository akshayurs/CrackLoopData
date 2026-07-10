Checking "does the stream end with any word" is the mirror image of "does the stream start with any word" — so reverse every dictionary word before inserting it into a trie. Then, to answer a query, walk that trie backwards from the newest letter toward older ones; a full path to a marked node means some word matches the current suffix.

Only the longest word's length worth of history can ever matter, so a small deque as a sliding buffer replaces the unbounded stream from the brute-force version — memory per query stays bounded no matter how long the stream runs.

```python
class StreamChecker:
    def __init__(self, words):
        self.root = {}
        self.max_len = 0
        for word in words:
            node = self.root
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node["$"] = True
            self.max_len = max(self.max_len, len(word))
        self.buffer = []

    def query(self, letter):
        self.buffer.append(letter)
        if len(self.buffer) > self.max_len:
            self.buffer.pop(0)

        node = self.root
        for ch in reversed(self.buffer):
            if "$" in node:
                return True
            if ch not in node:
                return False
            node = node[ch]
        return "$" in node
```

## Why it works

Reversing every word before insertion turns "ends with word" into "starts with reversed word", which a trie answers naturally by walking from the root. Traversing the buffer newest-letter-first retraces that reversed path; hitting a `$` marker at any point means the letters consumed so far — read backwards, i.e. the actual suffix — spell a dictionary word. The buffer only needs to hold `max_len` letters because no word longer than that could ever match.

## Complexity

- Time: O(L) per query, where L is the longest word length — the trie walk stops as soon as it runs out of buffer or matching edges. Building the trie is O(W * L) once.
- Space: O(W * L) for the trie plus O(L) for the buffer.
