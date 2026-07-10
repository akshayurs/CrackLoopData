You are given an `m x n` integer matrix `heights` where `heights[r][c]` is the height of the cell at row `r`, column `c`. Water can flow from a cell to any of its 4 orthogonal neighbors if the neighbor's height is **less than or equal to** the current cell's height. Rain falling on any cell can flow through a chain of such neighbors and eventually off the edge of the grid.

The **Pacific** ocean touches the top row and the left column; the **Atlantic** ocean touches the bottom row and the right column. Return the list of coordinates `[r, c]` from which water can reach **both** oceans, sorted first by row then by column.

## Examples

```text
Input:  heights = [[1,2,2,3,5],
                    [3,2,3,4,4],
                    [2,4,5,3,1],
                    [6,7,1,4,5],
                    [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

```text
Input:  heights = [[1]]
Output: [[0,0]]        # the single cell touches both oceans at once
```

```text
Input:  heights = [[2,1],
                    [1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
```

## Constraints

- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5
- m == heights.length, n == heights[r].length
