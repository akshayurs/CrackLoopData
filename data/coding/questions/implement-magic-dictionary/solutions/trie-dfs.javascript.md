Store the dictionary in a trie so shared prefixes are explored once instead of per word. Then answer `search` with a depth-first walk that tracks a "mismatch budget" of exactly one: at each letter of the query you're either allowed to follow the matching child for free, or spend your one allowed substitution to step into a different child.

A query is a hit only if the walk reaches the end of the word with the mismatch budget spent exactly to zero remaining (i.e. used exactly once) and lands on a node marked as the end of a dictionary word.

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.isWord = false;
  }
}

class MagicDictionary {
  constructor() {
    this.root = new TrieNode();
  }

  buildDict(words) {
    for (const word of words) {
      let node = this.root;
      for (const ch of word) {
        if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
        node = node.children.get(ch);
      }
      node.isWord = true;
    }
  }

  search(word) {
    const dfs = (node, i, mismatches) => {
      if (i === word.length) return mismatches === 1 && node.isWord;
      const ch = word[i];
      for (const [edge, child] of node.children) {
        const extra = edge === ch ? 0 : 1;
        if (mismatches + extra > 1) continue;
        if (dfs(child, i + 1, mismatches + extra)) return true;
      }
      return false;
    };

    return dfs(this.root, 0, 0);
  }
}
```

## Why it works

The trie lets one substitution be "spent" at any depth: following the edge equal to the query's current letter costs nothing, following any other edge costs the single mismatch we're allowed. Pruning as soon as `mismatches` would exceed 1 keeps the branching bounded — at most one extra edge is ever explored per level beyond the matching one. Requiring `mismatches === 1` at the end rejects exact matches (zero changes) exactly as the problem demands.

## Complexity

- Time: O(26·L) per search, where L is the query length — at each of the L levels at most 26 children are considered, and the mismatch budget stops runaway branching. Building the trie is O(N·L).
- Space: O(N·L) for the trie, where N is the number of words and L their average length.
