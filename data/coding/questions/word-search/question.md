You are given an `m x n` grid of characters `board` and a string `word`. Return `true` if `word` can be traced through the board, `false` otherwise.

A trace starts at any cell and moves to horizontally or vertically adjacent cells, spelling out `word` one letter at a time. The same cell cannot be reused twice within a single trace.

## Examples

```text
Input:  board = [["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]]
        word = "ABCCED"
Output: true
```

```text
Input:  board = [["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]]
        word = "SEE"
Output: true
```

```text
Input:  board = [["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]]
        word = "ABCB"
Output: false        # tracing "ABC" reaches the only "C" adjacent to "B", leaving no unused cell for the second "B"
```

## Constraints

- 1 <= board.length, board[i].length <= 6
- 1 <= word.length <= 15
- board and word consist of only uppercase and lowercase English letters.
