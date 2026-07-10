Drop every word into a `Set` so membership checks are O(1), then test each word directly: it is buildable exactly when all of its proper prefixes also live in that set. Track the best answer seen so far, preferring a longer word or, on a length tie, the lexicographically smaller one.

This is the straightforward reading of the definition — no trie, just prefix slicing and a hash lookup for each one.

```javascript
function longestWord(words) {
  const wordSet = new Set(words);
  let best = "";
  for (const word of words) {
    let buildable = true;
    for (let i = 1; i < word.length; i++) {
      if (!wordSet.has(word.slice(0, i))) {
        buildable = false;
        break;
      }
    }
    if (buildable && (word.length > best.length || (word.length === best.length && word < best))) {
      best = word;
    }
  }
  return best;
}
```

## Why it works

A word is buildable only if every shorter prefix that would have been typed on the way to it is itself a word in the array. Checking `word.slice(0, i)` for every `i` from 1 up to (but not including) the full length verifies exactly that chain. Comparing candidates by length first, then lexicographically, reproduces the required tie-break rule.

## Complexity

- Time: O(n · L²) — n words, each with up to L prefixes, each prefix slice and lookup costing O(L).
- Space: O(n · L) — the set stores every word.
