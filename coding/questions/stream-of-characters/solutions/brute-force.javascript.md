Keep every letter the stream has produced in a growing array. On each `query`, walk the dictionary and test whether the buffer's tail matches that word exactly.

This is easy to write correctly first, then optimize once it's clear where the time goes.

```javascript
class StreamChecker {
  constructor(words) {
    this.words = words;
    this.stream = [];
  }

  query(letter) {
    this.stream.push(letter);
    for (const word of this.words) {
      const n = word.length;
      if (n <= this.stream.length) {
        const tail = this.stream.slice(this.stream.length - n).join("");
        if (tail === word) return true;
      }
    }
    return false;
  }
}
```

## Why it works

`this.stream` holds the full history in order, so its last `n` entries joined together are exactly the last `n` letters seen — comparing that to `word` directly answers "does the stream end with this word?". Checking every word on every call is correct because there is no shortcut yet for skipping non-matching prefixes.

## Complexity

- Time: O(Q * W * L) — Q queries, each scanning W words of average length L to build and compare a slice.
- Space: O(Q + W * L) — the buffer grows with the stream; the dictionary is stored as given.
