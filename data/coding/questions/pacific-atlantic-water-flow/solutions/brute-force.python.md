The direct reading of the problem: for every single cell, simulate where its water can go. Run a DFS from that cell following only downhill-or-equal moves, and check whether the reachable set ever touches the top/left border (Pacific) and separately whether it touches the bottom/right border (Atlantic).

This retraces huge amounts of shared ground — cells near the middle of the grid get re-explored once per starting cell — but it mirrors the problem statement almost line for line, which makes it a solid first answer before optimizing.

```python
def pacific_atlantic(heights):
    if not heights or not heights[0]:
        return []
    m, n = len(heights), len(heights[0])

    def reaches(start, is_target):
        seen = {start}
        stack = [start]
        touched = is_target(*start)
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen
                        and heights[nr][nc] <= heights[r][c]):
                    seen.add((nr, nc))
                    stack.append((nr, nc))
                    touched = touched or is_target(nr, nc)
        return touched

    pacific = lambda r, c: r == 0 or c == 0
    atlantic = lambda r, c: r == m - 1 or c == n - 1

    result = []
    for r in range(m):
        for c in range(n):
            if reaches((r, c), pacific) and reaches((r, c), atlantic):
                result.append([r, c])
    return result
```

## Why it works

Each DFS from a cell visits exactly the set of cells reachable by non-increasing steps, which is precisely the water-flow rule in the problem. A cell qualifies once its own reachable set includes at least one Pacific-border cell and at least one Atlantic-border cell — including itself. Iterating cells in row-major order keeps the output naturally sorted.

## Complexity

- Time: O(m^2 * n^2) — a DFS over up to m*n cells is run from every one of the m*n starting cells.
- Space: O(m * n) — the visited set and recursion stack for a single DFS.
