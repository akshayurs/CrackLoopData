You are given an `m x n` board containing the letters `'X'` and `'O'`. Capture every region of `'O'`s that is completely surrounded by `'X'`s by flipping every `'O'` in that region to `'X'`, in place. A region is a group of `'O'`s connected 4-directionally (up, down, left, right). A region is **not** captured if any cell in it touches the border of the board.

Modify `board` directly — the function does not need to return anything.

## Examples

```text
Input:
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output:
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
# The O's at (1,1), (1,2), (2,2) form a region with no border cell, so they flip to X.
# The O at (3,1) touches the bottom border, so it survives.
```

```text
Input:
board = [
  ["X"]
]
Output:
[
  ["X"]
]
```

```text
Input:
board = [
  ["O","O"],
  ["O","O"]
]
Output:
[
  ["O","O"],
  ["O","O"]
]
# Every cell touches the border, so nothing is captured.
```

## Constraints

- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

## Follow-up

Can you avoid the extra visited set some approaches use, and instead mark safe cells directly on the board?
