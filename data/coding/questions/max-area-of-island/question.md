You are given an `m x n` binary grid `grid` where `1` represents land and `0` represents water. An **island** is a group of `1`s connected horizontally or vertically (not diagonally). The grid's edges are surrounded by water.

The **area** of an island is the number of cells with value `1` that belong to it. Return the area of the largest island in `grid`. If there is no island, return `0`.

## Examples

```text
Input:  grid = [[0,0,1,0],
                [1,1,1,0],
                [0,1,0,0],
                [0,0,0,1]]
Output: 5        # the connected block of 1s in the top-left forms an island of area 5
```

```text
Input:  grid = [[0,0,0],
                [0,0,0]]
Output: 0        # no land cells at all
```

```text
Input:  grid = [[1,1],
                [1,0]]
Output: 3        # all three 1s are connected into one island
```

## Constraints

- 1 <= grid.length, grid[0].length <= 50
- grid[i][j] is either 0 or 1.
