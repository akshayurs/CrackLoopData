The most direct reading of the problem: rank every element by how far it is from `x`, keep the best `k`, then put them back in order. The comparator must encode both rules — first the distance `|a - x|`, and for ties the smaller value wins.

Taking the first `k` of that ordering gives the closest set; a final ascending sort restores the required output order.

```javascript
function findClosestElements(arr, k, x) {
  const byDistance = [...arr].sort((a, b) => {
    const da = Math.abs(a - x);
    const db = Math.abs(b - x);
    return da === db ? a - b : da - db;
  });
  return byDistance.slice(0, k).sort((a, b) => a - b);
}
```

## Why it works

The comparator orders by distance first and, on ties, by value — so equal-distance elements place the smaller one earlier, matching the tie-break rule. The first `k` entries are the closest integers. Because the answer must be ascending, the trailing numeric `sort` reorders that slice by value.

## Complexity

- Time: O(n log n) — dominated by the distance sort over all n elements.
- Space: O(n) — the copied array being sorted.
