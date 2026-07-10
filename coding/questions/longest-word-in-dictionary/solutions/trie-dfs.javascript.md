Insert every word into a trie, marking the node at the end of each word. Now "buildable" has a direct meaning on this structure: a node represents a buildable word exactly when every node on the path from the root down to it — not just the last one — is marked as an end-of-word. So a depth-first walk that only steps into children which are themselves end-of-word nodes visits precisely the set of buildable words, in one pass, without ever slicing a string to re-check a prefix.

Track the best word found during the walk the same way as before: longer wins, and a length tie goes to the lexicographically smaller string.

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

function longestWord(words) {
  const root = new TrieNode();
  for (const w of words) {
    let node = root;
    for (const ch of w) {
      if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
      node = node.children.get(ch);
    }
    node.isEnd = true;
  }

  let best = "";
  const stack = [[root, ""]];
  while (stack.length) {
    const [node, prefix] = stack.pop();
    for (const [ch, child] of node.children) {
      if (child.isEnd) {
        const word = prefix + ch;
        if (word.length > best.length || (word.length === best.length && word < best)) {
          best = word;
        }
        stack.push([child, word]);
      }
    }
  }
  return best;
}
```

## Why it works

Each edge walked during the DFS corresponds to typing one more letter, and the walk only continues through nodes flagged `isEnd` — meaning the prefix formed so far is itself a real word. So every string the traversal reaches is guaranteed buildable, and since the trie is only as deep as the longest word, no candidate is ever missed. The length-then-lexicographic comparison at each visited node keeps the required best answer.

## Complexity

- Time: O(∑Lᵢ) — building the trie visits every character once; the traversal visits at most one node per character across all words.
- Space: O(∑Lᵢ) — trie nodes, one per distinct character position inserted.
