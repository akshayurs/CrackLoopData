Start by assuming every node is its own component, then process the edges one at a time, merging the components of the two endpoints. A disjoint-set (union-find) structure with path compression and union by size makes each merge and lookup nearly O(1), so there is no need to build an adjacency list or recurse at all.

Track how many components remain as a single counter that decreases by one every time a union actually merges two previously separate groups.

```javascript
function countComponents(n, edges) {
  const parent = Array.from({ length: n }, (_, i) => i);
  const size = new Array(n).fill(1);
  let count = n;

  function find(x) {
    while (parent[x] !== x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  function union(a, b) {
    let ra = find(a);
    let rb = find(b);
    if (ra === rb) return;
    if (size[ra] < size[rb]) [ra, rb] = [rb, ra];
    parent[rb] = ra;
    size[ra] += size[rb];
    count--;
  }

  for (const [a, b] of edges) {
    union(a, b);
  }

  return count;
}
```

## Why it works

`find` follows parent pointers up to a group's representative, compressing the path along the way so future lookups are faster. `union` merges two groups only when their representatives differ, attaching the smaller tree under the larger one to keep trees shallow. Since `count` starts at `n` and drops by exactly one per genuine merge, it always equals the number of surviving components once every edge has been processed.

## Complexity

- Time: O(n + e * α(n)) — n initializations plus e near-constant-time union/find operations (α is the inverse Ackermann function).
- Space: O(n) — the `parent` and `size` arrays.
