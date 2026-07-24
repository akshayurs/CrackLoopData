Build the real tree: each node holds 26 child slots, one per lowercase letter, plus a flag marking whether a word ends there. Inserting a word walks down the tree one character at a time, creating child nodes as needed; the last character's node gets flagged as a word ending.

Both `search` and `startsWith` reduce to the same walk — follow the characters down as far as they exist. `search` additionally requires the node reached to be flagged as a word ending, while `startsWith` only needs the path to exist at all. Shared prefixes between words share nodes, so no work or memory is repeated across similar words.

```javascript
class Trie {
  constructor() {
    this.children = new Array(26).fill(null);
    this.isWord = false;
  }

  insert(word) {
    let node = this;
    for (const ch of word) {
      const idx = ch.charCodeAt(0) - 97;
      if (!node.children[idx]) node.children[idx] = new Trie();
      node = node.children[idx];
    }
    node.isWord = true;
  }

  _walk(s) {
    let node = this;
    for (const ch of s) {
      const idx = ch.charCodeAt(0) - 97;
      if (!node.children[idx]) return null;
      node = node.children[idx];
    }
    return node;
  }

  search(word) {
    const node = this._walk(word);
    return node !== null && node.isWord;
  }

  startsWith(prefix) {
    return this._walk(prefix) !== null;
  }
}
```

## Why it works

Each `Trie` instance is simultaneously the root and every internal node — `children[i]` points to the subtree reached by following letter `i`. `insert` follows an existing path where one exists and extends it with fresh nodes otherwise, so words sharing a prefix share the same nodes for that prefix. `_walk` is the one traversal both queries need: it returns the node at the end of the path, or `null` if the path breaks early. `search` then checks the extra condition that some inserted word actually ended there, distinguishing a real word from a prefix that merely happens to exist because of a longer word.

## Complexity

- Time: O(L) for `insert`, `search`, and `startsWith`, where L is the length of the word or prefix.
- Space: O(total characters inserted) in the worst case, since each new character can create one new node; shared prefixes reuse existing nodes.
