You have a graph of `n` nodes labeled `0` to `n - 1`. You are given an integer `n` and an array `edges` where each `edges[i] = [a, b]` denotes an undirected edge between node `a` and node `b`. Return the number of connected components in the graph.

## Examples

```text
Input:  n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2              # {0, 1, 2} form one component, {3, 4} form another
```

```text
Input:  n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output: 1              # every node is reachable from every other node
```

```text
Input:  n = 4, edges = []
Output: 4              # no edges means every node is its own component
```

## Constraints

- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= a, b < n
- a != b
- There are no duplicate edges.
