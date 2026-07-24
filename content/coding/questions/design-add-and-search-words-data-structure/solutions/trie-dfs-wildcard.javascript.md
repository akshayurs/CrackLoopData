Build a real trie so `addWord` shares structure between words the way a plain `Trie.insert` does: each node holds 26 child slots, one per lowercase letter, plus a flag marking whether a word ends there. Adding a word walks down one character at a time, creating child nodes as needed.

The wildcard is what makes `search` more than a plain trie walk. At an ordinary letter, follow the single matching child, exactly as before. At a `.`, the query doesn't commit to one branch — it means "try every child here and succeed if any of them lead to a match," so `search` becomes a small depth-first exploration that only branches at dots and stays a single path everywhere else.

```javascript
class TrieNode {
  constructor() {
    this.children = new Array(26).fill(null);
    this.isWord = false;
  }
}

class WordDictionary {
  constructor() {
    this.root = new TrieNode();
  }
  addWord(word) {
    let node = this.root;
    for (const ch of word) {
      const idx = ch.charCodeAt(0) - 97;
      if (node.children[idx] === null) node.children[idx] = new TrieNode();
      node = node.children[idx];
    }
    node.isWord = true;
  }
  search(word) {
    const dfs = (node, i) => {
      if (node === null) return false;
      if (i === word.length) return node.isWord;
      const ch = word[i];
      if (ch !== '.') return dfs(node.children[ch.charCodeAt(0) - 97], i + 1);
      return node.children.some((child) => dfs(child, i + 1));
    };
    return dfs(this.root, 0);
  }
}
```

## Why it works

Each `TrieNode` groups the 26 possible next letters, so words sharing a prefix share the same chain of nodes. `dfs` advances one query character per call: a concrete letter narrows the search to exactly one child, while `.` fans out over every non-null child via `some`, succeeding as soon as any branch reaches the end of `word` on a node flagged as a word ending. Returning `false` on a `null` node prunes dead branches immediately instead of exploring further. Because dots only appear a handful of times per query (bounded by the constraints), the fan-out stays cheap in practice even though it is exponential in the dot count.

## Complexity

- Time: O(L) for `addWord`. `search` is O(26^d * L) in the worst case, where L is the word length and d is the number of dots; with few dots this is close to O(L).
- Space: O(total characters added), since each new character can create one new node; shared prefixes reuse existing nodes.
