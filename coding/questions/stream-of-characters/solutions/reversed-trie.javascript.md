Checking "does the stream end with any word" is the mirror image of "does the stream start with any word" — so reverse every dictionary word before inserting it into a trie. Then, to answer a query, walk that trie backwards from the newest letter toward older ones; a full path to a marked node means some word matches the current suffix.

Only the longest word's length worth of history can ever matter, so a small array used as a sliding buffer replaces the unbounded stream from the brute-force version — memory per query stays bounded no matter how long the stream runs.

```javascript
class StreamChecker {
  constructor(words) {
    this.root = {};
    this.maxLen = 0;
    for (const word of words) {
      let node = this.root;
      for (let i = word.length - 1; i >= 0; i--) {
        const ch = word[i];
        node = node[ch] ?? (node[ch] = {});
      }
      node.$ = true;
      this.maxLen = Math.max(this.maxLen, word.length);
    }
    this.buffer = [];
  }

  query(letter) {
    this.buffer.push(letter);
    if (this.buffer.length > this.maxLen) this.buffer.shift();

    let node = this.root;
    for (let i = this.buffer.length - 1; i >= 0; i--) {
      if (node.$) return true;
      const ch = this.buffer[i];
      if (!(ch in node)) return false;
      node = node[ch];
    }
    return !!node.$;
  }
}
```

## Why it works

Reversing every word before insertion turns "ends with word" into "starts with reversed word", which a trie answers naturally by walking from the root. Traversing the buffer newest-letter-first retraces that reversed path; hitting a `$` marker at any point means the letters consumed so far — read backwards, i.e. the actual suffix — spell a dictionary word. The buffer only needs to hold `maxLen` letters because no word longer than that could ever match.

## Complexity

- Time: O(L) per query, where L is the longest word length — the trie walk stops as soon as it runs out of buffer or matching edges. Building the trie is O(W * L) once.
- Space: O(W * L) for the trie plus O(L) for the buffer.
