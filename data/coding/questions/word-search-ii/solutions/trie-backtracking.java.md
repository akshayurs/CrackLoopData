The brute-force approach wastes effort because many words share prefixes — searching for `"eat"` and `"eaten"` separately walks the same first three letters twice. Merge every word into a single trie first, then make **one** DFS pass over the board, walking the trie in step with the board instead of walking a fixed word string.

At each board cell, follow the trie edge matching that cell's letter. Whenever the trie node reached marks the end of a word, record it and clear the marker so the same word is never added twice.

```java
import java.util.*;

class Solution {
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word = null;
    }

    private char[][] board;
    private int rows, cols;
    private List<String> found = new ArrayList<>();

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        rows = board.length;
        cols = board[0].length;
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char ch : w.toCharArray()) {
                int idx = ch - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.word = w;
        }
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                dfs(r, c, root);
            }
        }
        Collections.sort(found);
        return found;
    }

    private void dfs(int r, int c, TrieNode node) {
        char ch = board[r][c];
        if (ch == '*') return;
        TrieNode next = node.children[ch - 'a'];
        if (next == null) return;
        if (next.word != null) {
            found.add(next.word);
            next.word = null;
        }
        board[r][c] = '*';
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                dfs(nr, nc, next);
            }
        }
        board[r][c] = ch;
    }
}
```

## Why it works

The trie lets every board path be walked once and checked against all words that share its prefix simultaneously, instead of once per word. Marking a cell `'*'` during the current path prevents reusing it within one word, and restoring it afterward lets other paths use it. Clearing the `word` field guarantees a word is reported at most once even if multiple paths could spell it.

## Complexity

- Time: O(m · n · 4^L) — one DFS pass over the board, where each cell's search branches up to 4 ways per remaining trie depth (bounded by max word length L); building the trie is O(sum of word lengths).
- Space: O(sum of word lengths) — the trie, plus O(L) recursion depth.
