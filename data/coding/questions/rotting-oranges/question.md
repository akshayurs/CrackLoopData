You are given a `grid` of integers representing a crate of oranges: `0` is an empty cell, `1` is a fresh orange, and `2` is a rotten orange. Every minute, any fresh orange that is horizontally or vertically adjacent to a rotten orange becomes rotten too — all such infections happen simultaneously each minute. Return the minimum number of minutes until no fresh orange remains, or `-1` if some fresh orange can never rot.

## Examples

```text
Input:  grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1]
]
Output: 4
```

```text
Input:  grid = [
  [2, 1, 1],
  [0, 1, 1],
  [1, 0, 1]
]
Output: -1        # the orange at [2][0] is cut off by empty cells, so it never rots
```

```text
Input:  grid = [
  [0, 2]
]
Output: 0        # no fresh oranges to begin with
```

## Constraints

- 1 <= grid.length, grid[i].length <= 10
- grid[i][j] is 0, 1, or 2.

## Follow-up

Can you do it in a single pass over the grid instead of re-scanning every cell each minute?
