The brute-force approach wastes effort because many words share prefixes — searching for `"eat"` and `"eaten"` separately walks the same first three letters twice. Merge every word into a single trie first, then make **one** DFS pass over the board, walking the trie in step with the board instead of walking a fixed word string.

At each board cell, follow the trie edge matching that cell's letter. Whenever the trie node reached marks the end of a word, record it and delete the marker so the same word is never added twice. Once a trie branch has no children and no word left in it, prune it from its parent so future searches skip dead ends sooner.

```javascript
function findWords(board, words) {
  if (!board.length || !board[0].length) return [];
  const root = {};
  for (const word of words) {
    let node = root;
    for (const ch of word) {
      node = node[ch] || (node[ch] = {});
    }
    node.word = word;
  }

  const rows = board.length, cols = board[0].length;
  const found = [];

  function dfs(r, c, node) {
    const ch = board[r][c];
    const next = node[ch];
    if (!next) return;
    if (next.word) {
      found.push(next.word);
      delete next.word;
    }
    board[r][c] = "*";
    for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      const nr = r + dr, nc = c + dc;
      if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] !== "*") {
        dfs(nr, nc, next);
      }
    }
    board[r][c] = ch;
    if (Object.keys(next).length === 0) delete node[ch];
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      dfs(r, c, root);
    }
  }

  return found.sort();
}
```

## Why it works

The trie lets every board path be walked once and checked against all words that share its prefix simultaneously, instead of once per word. Marking a cell `"*"` during the current path prevents reusing it within one word, and restoring it afterward lets other paths use it. Deleting the `word` marker guarantees a word is reported at most once even if multiple paths could spell it, and pruning exhausted trie nodes keeps later searches from wasting time on branches with nothing left to find.

## Complexity

- Time: O(m · n · 4^L) — one DFS pass over the board, where each cell's search branches up to 4 ways per remaining trie depth (bounded by max word length L); building the trie is O(sum of word lengths).
- Space: O(sum of word lengths) — the trie, plus O(L) recursion depth.
