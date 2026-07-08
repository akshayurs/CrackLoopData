The floor of the square root is simply the last integer `r` whose square has not yet passed `x`. So start from `0` and count upward, squaring each candidate, until the square exceeds `x`.

The moment `r * r > x`, the previous value `r - 1` is the answer. Multiplying is enough — no square-root function required.

```javascript
function mySqrt(x) {
  if (x < 2) return x;
  let r = 1;
  while (r * r <= x) {
    r += 1;
  }
  return r - 1;
}
```

## Why it works

Squares grow monotonically, so scanning `r = 1, 2, 3, …` crosses `x` exactly once. The first `r` with `r * r > x` marks the boundary, so `r - 1` is the largest integer whose square is `<= x`. The early return handles `0` and `1`, where the answer equals `x` itself.

## Complexity

- Time: O(√x) — the loop runs until `r` reaches roughly √x.
- Space: O(1) — only a counter is kept.
