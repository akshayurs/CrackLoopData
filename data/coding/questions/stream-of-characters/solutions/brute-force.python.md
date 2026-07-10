Keep every letter the stream has produced in a growing buffer. On each `query`, walk the dictionary and test whether the buffer's tail matches that word exactly — Python's slicing makes this a one-liner per word.

This is easy to write correctly first, then optimize once it's clear where the time goes.

```python
class StreamChecker:
    def __init__(self, words):
        self.words = words
        self.stream = []

    def query(self, letter):
        self.stream.append(letter)
        for word in self.words:
            n = len(word)
            if n <= len(self.stream) and "".join(self.stream[-n:]) == word:
                return True
        return False
```

## Why it works

`self.stream` holds the full history in order, so `self.stream[-n:]` is exactly the last `n` letters seen — comparing it to `word` directly answers "does the stream end with this word?". Checking every word on every call is correct because there is no shortcut yet for skipping non-matching prefixes.

## Complexity

- Time: O(Q * W * L) — Q queries, each scanning W words of average length L to build and compare a slice.
- Space: O(Q + W * L) — the buffer grows with the stream; the dictionary is stored as given.
