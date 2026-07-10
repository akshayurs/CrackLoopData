The direct reading of the problem: treat each word independently. For every word, scan every cell of the board as a possible starting point and run a backtracking DFS that follows the word letter by letter through neighboring cells, marking a cell visited while it's part of the current path and unmarking it on the way back out.

This is exactly "Word Search I" repeated once per word, so it never shares work between words — the same board region gets re-explored from scratch for every entry in the list.

```java
import java.util.*;

class Solution {
    private char[][] board;
    private int rows, cols;

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        rows = board.length;
        cols = board[0].length;
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (exists(word)) result.add(word);
        }
        Collections.sort(result);
        return result;
    }

    private boolean exists(String word) {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(r, c, word, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(int r, int c, String word, int i) {
        if (i == word.length()) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word.charAt(i)) return false;
        char tmp = board[r][c];
        board[r][c] = '*';
        boolean found = dfs(r + 1, c, word, i + 1) || dfs(r - 1, c, word, i + 1) ||
                         dfs(r, c + 1, word, i + 1) || dfs(r, c - 1, word, i + 1);
        board[r][c] = tmp;
        return found;
    }
}
```

## Why it works

`dfs` walks the word index by index, only stepping to a neighbor whose letter matches the next required character and refusing to step onto a cell already used in the current path (marked `'*'`). Restoring the cell after exploring each direction lets the same cell be reused by a different starting point or a different word. A word is kept only if some starting cell leads to a complete match; the collected list is sorted so the output is deterministic regardless of `words` order.

## Complexity

- Time: O(W · m · n · 4^L) — for each of the W words, every cell can start a search that branches up to 4 ways per letter of length L.
- Space: O(L) — recursion depth is bounded by the word length (board mutation is in place).
