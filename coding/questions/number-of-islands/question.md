You are given a 2D grid of `'1'` (land) and `'0'` (water) cells, given as a `grid` of strings. An island is a group of `'1'` cells connected horizontally or vertically — diagonal connections don't count, and the whole grid is surrounded by water. Return the number of islands.

## Examples

```text
Input:  grid = [
  "11000",
  "11000",
  "00100",
  "00011"
]
Output: 3
```

```text
Input:  grid = [
  "111",
  "010",
  "111"
]
Output: 1        # the outer ring of land is fully connected
```

```text
Input:  grid = [
  "10",
  "01"
]
Output: 2        # the two land cells only touch diagonally, so they are separate
```

## Constraints

- 1 <= grid.length, grid[i].length <= 300
- `grid[i][j]` is `'0'` or `'1'`.

## Follow-up

Can you solve it without recursion, in case the grid is too large for the call stack to hold?
