Instead of re-slicing and re-hashing overlapping substrings on every DP transition, insert every word into a trie once. Then for each candidate word, walk the trie a character at a time from each reachable boundary, checking whether the current node marks the end of some dictionary word — no substring is ever built.

The prefix DP is unchanged in spirit: whenever the walk lands on a node flagged as a word end, that DP boundary becomes reachable.

```javascript
class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

function findConcatenatedWords(words) {
  const root = new TrieNode();
  for (const w of words) {
    let node = root;
    for (const ch of w) {
      if (!node.children[ch]) node.children[ch] = new TrieNode();
      node = node.children[ch];
    }
    node.isEnd = true;
  }

  const result = [];
  for (const word of words) {
    const n = word.length;
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let i = 0; i < n; i++) {
      if (!dp[i]) continue;
      let node = root;
      for (let j = i + 1; j <= n; j++) {
        const ch = word[j - 1];
        if (!node.children[ch]) break;
        node = node.children[ch];
        if (node.isEnd && !(i === 0 && j === n)) dp[j] = true;
      }
    }
    if (dp[n]) result.push(word);
  }
  return result.sort();
}
```

## Why it works

Walking the trie one character at a time from every reachable boundary `i` visits the same "is this chunk a word?" facts the hash-set version checked with substring lookups, but each character is examined once per walk instead of being re-hashed inside a fresh substring. A node with `isEnd` set means `word.slice(i, j)` is a dictionary word, so `dp[j]` becomes reachable; excluding `i === 0 && j === n` still blocks the trivial self-match.

## Complexity

- Time: O(n · L²) — n words, each with up to L trie walks of length up to L, no substring allocation.
- Space: O(n · L) — the trie stores at most that many characters.
