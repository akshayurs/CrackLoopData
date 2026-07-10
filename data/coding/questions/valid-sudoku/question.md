You are given a 9×9 grid `board` representing a partially filled Sudoku. Each cell holds a digit character `'1'`–`'9'`, or `'.'` for an empty cell. Decide whether the current filling is **valid** according to three rules:

- every row contains each digit `'1'`–`'9'` at most once,
- every column contains each digit `'1'`–`'9'` at most once,
- each of the nine `3×3` sub-grids (aligned to the fixed 3×3 partition) contains each digit at most once.

Only the filled cells are checked. The board does **not** have to be complete or solvable — you are validating the digits already placed, not solving the puzzle.

## Examples

```text
Input:
  ["5","3",".",  ".","7",".",  ".",".","."]
  ["6",".",".",  "1","9","5",  ".",".","."]
  [".","9","8",  ".",".",".",  ".","6","."]
  ["8",".",".",  ".","6",".",  ".",".","3"]
  ["4",".",".",  "8",".","3",  ".",".","1"]
  ["7",".",".",  ".","2",".",  ".",".","6"]
  [".","6",".",  ".",".",".",  "2","8","."]
  [".",".",".",  "4","1","9",  ".",".","5"]
  [".",".",".",  ".","8",".",  ".","7","9"]
Output: true        # no row, column, or box repeats a digit
```

```text
Input:  same board as above, but the top-left cell is "8" instead of "5"
  ["8","3",".",  ".","7",".",  ".",".","."]
  ["6",".",".",  "1","9","5",  ".",".","."]
  [".","9","8",  ".",".",".",  ".","6","."]
  ["8",".",".",  ".","6",".",  ".",".","3"]
  ... (rows 5-9 unchanged)
Output: false       # column 0 now holds "8" twice (row 0 and row 3)
```

## Constraints

- `board.length == 9` and `board[i].length == 9`.
- Each `board[i][j]` is a digit `'1'`–`'9'` or the character `'.'`.
- Validation applies only to filled cells; the puzzle may be incomplete.

## Follow-up

Can you decide validity in a single pass over the 81 cells? And can you replace the hash sets with `O(1)` extra integers using bit masks?
