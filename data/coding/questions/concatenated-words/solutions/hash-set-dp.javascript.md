Same idea in JavaScript: load every word into a `Set`, then for each word run a prefix DP that asks whether the string can be cut into two or more pieces that are all in the set. `dp[j]` tracks whether the prefix of length `j` is fully coverable.

The single-piece split (the word matching itself whole) is explicitly skipped so a word is never counted as its own concatenation.

```javascript
function findConcatenatedWords(words) {
  const wordSet = new Set(words);
  const result = [];
  for (const word of words) {
    const n = word.length;
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let j = 1; j <= n; j++) {
      for (let i = 0; i < j; i++) {
        if (!dp[i]) continue;
        if (i === 0 && j === n) continue;
        if (wordSet.has(word.slice(i, j))) {
          dp[j] = true;
          break;
        }
      }
      if (dp[n]) break;
    }
    if (dp[n]) result.push(word);
  }
  return result.sort();
}
```

## Why it works

`dp[i]` true means `word.slice(0, i)` is fully built from set members. Extending to `dp[j]` requires some boundary `i` with `dp[i]` true where `word.slice(i, j)` is also a member. Excluding `i === 0 && j === n` removes the trivial whole-word match, so `dp[n]` only becomes true via a real multi-piece split.

## Complexity

- Time: O(n · L³) — n words, each running an O(L²) DP whose transitions slice and hash O(L)-length substrings.
- Space: O(n · L) — the set stores every word.
