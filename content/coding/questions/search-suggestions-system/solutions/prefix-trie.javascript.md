Instead of re-scanning the whole catalog for every prefix, build the answer once while inserting the products into a trie. Sort the catalog first, then insert products in that order; at every node along a word's path, append the word to that node's own suggestion list as long as it has fewer than three entries. Because insertion happens in sorted order, each node's list ends up already sorted — no extra work needed later.

Answering the query is now just a walk down the trie one character at a time: at each step read the current node's cached list. The moment a character has no matching child, every remaining prefix is a dead end and gets an empty list.

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.suggestions = [];
  }
}

function searchSuggestions(products, searchWord) {
  const root = new TrieNode();
  for (const word of [...products].sort()) {
    let node = root;
    for (const ch of word) {
      if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
      node = node.children.get(ch);
      if (node.suggestions.length < 3) node.suggestions.push(word);
    }
  }

  const result = [];
  let node = root;
  let dead = false;
  for (const ch of searchWord) {
    if (!dead) {
      node = node.children.get(ch) || null;
      dead = node === null;
    }
    result.push(node ? node.suggestions : []);
  }
  return result;
}
```

## Why it works

Inserting products in sorted order means the first (at most) three words that ever pass through a node are, by construction, the three lexicographically smallest words sharing that node's prefix — exactly the suggestions the problem wants, already in order. Once the trie is built, each query character is a single map lookup, so producing all `m` answer lists costs only O(m) node visits plus the O(1) cost of copying each cached list.

## Complexity

- Time: O(N log N + S + m) — sorting the catalog (N products), building the trie over S total characters, then O(m) to answer the query.
- Space: O(S) — the trie holds every character of every product, each node caching at most 3 strings.
