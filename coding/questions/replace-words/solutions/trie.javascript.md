Build the dictionary into a trie once instead of rescanning it per word. Each root marks the node at the end of its path as a root-end; resolving a word is then just a walk down the trie, one character at a time, stopping the moment a root-end node is reached — that is guaranteed to be the shortest matching root.

Preprocessing the dictionary this way turns per-word resolution into an O(word length) walk of the trie, independent of how many roots exist.

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.isRootEnd = false;
  }
}

function replaceWords(dictionary, sentence) {
  const trieRoot = new TrieNode();
  for (const root of dictionary) {
    let node = trieRoot;
    for (const ch of root) {
      if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
      node = node.children.get(ch);
    }
    node.isRootEnd = true;
  }

  const shortestRoot = (word) => {
    let node = trieRoot;
    for (let i = 0; i < word.length; i++) {
      const ch = word[i];
      if (!node.children.has(ch)) return word;
      node = node.children.get(ch);
      if (node.isRootEnd) return word.slice(0, i + 1);
    }
    return word;
  };

  return sentence.split(" ").map(shortestRoot).join(" ");
}
```

## Why it works

Each root traces a unique path from `trieRoot`, and its final node is flagged `isRootEnd`. Walking a word along that same structure follows the path spelled by its own letters, so the first `isRootEnd` node encountered is, by construction, the shortest root that prefixes the word. If the walk runs off the trie or never crosses a flagged node, the word has no root and is returned as-is.

## Complexity

- Time: O(R + wL) — R total characters across all roots, built once; each word of length L costs O(L) to resolve.
- Space: O(R) — one trie node per distinct character position across all roots.
