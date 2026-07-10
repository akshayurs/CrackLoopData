The brute-force approach wastes effort because many words share prefixes — searching for `"eat"` and `"eaten"` separately walks the same first three letters twice. Merge every word into a single trie first, then make **one** DFS pass over the board, walking the trie in step with the board instead of walking a fixed word string.

At each board cell, follow the trie edge matching that cell's letter. Whenever the trie node reached marks the end of a word, record it and delete the marker so the same word is never added twice. Once a trie branch has no children and no word left in it, prune it from its parent so future searches skip dead ends sooner.

```python
def find_words(board, words):
    if not board or not board[0]:
        return []
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = word

    rows, cols = len(board), len(board[0])
    found = []

    def dfs(r, c, node):
        ch = board[r][c]
        nxt = node.get(ch)
        if nxt is None:
            return
        if "#" in nxt:
            found.append(nxt.pop("#"))
        board[r][c] = "*"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "*":
                dfs(nr, nc, nxt)
        board[r][c] = ch
        if not nxt:
            del node[ch]

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return sorted(found)
```

## Why it works

The trie lets every board path be walked once and checked against all words that share its prefix simultaneously, instead of once per word. Marking a cell `"*"` during the current path prevents reusing it within one word, and restoring it afterward lets other paths use it. Popping the `"#"` marker guarantees a word is reported at most once even if multiple paths could spell it, and deleting exhausted trie nodes keeps later searches from wasting time on branches with nothing left to find.

## Complexity

- Time: O(m · n · 4^L) — one DFS pass over the board, where each cell's search branches up to 4 ways per remaining trie depth (bounded by max word length L); building the trie is O(sum of word lengths).
- Space: O(sum of word lengths) — the trie, plus O(L) recursion depth.
