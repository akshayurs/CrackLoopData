The simplest reading of the rule "changing exactly one character" is to just check it directly against every stored word: same length, and exactly one position differs. No trie, no preprocessing beyond keeping the list around.

It is the honest baseline you would state first in an interview before reaching for a trie.

```javascript
class MagicDictionary {
  constructor() {
    this.words = [];
  }

  buildDict(words) {
    this.words = words;
  }

  search(word) {
    for (const candidate of this.words) {
      if (candidate.length !== word.length) continue;
      let diff = 0;
      for (let i = 0; i < word.length; i++) {
        if (candidate[i] !== word[i]) diff++;
      }
      if (diff === 1) return true;
    }
    return false;
  }
}
```

## Why it works

`buildDict` just remembers the words. `search` scans every stored word, skips any whose length doesn't match (a length mismatch can never be a one-letter substitution), and counts differing positions. A candidate qualifies only if exactly one position differs — zero differences means the words are identical, not a genuine change.

## Complexity

- Time: O(N·L) — each search compares against up to N stored words of length up to L.
- Space: O(N·L) — storing all the words.
