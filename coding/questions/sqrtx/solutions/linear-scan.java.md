The floor of the square root is simply the last integer `r` whose square has not yet passed `x`. So start from `0` and count upward, squaring each candidate, until the square exceeds `x`.

The moment the square passes `x`, the previous value is the answer. Use a `long` for the product so squaring never overflows near `2^31 - 1`.

```java
class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        int r = 1;
        while ((long) r * r <= x) {
            r += 1;
        }
        return r - 1;
    }
}
```

## Why it works

Squares grow monotonically, so scanning `r = 1, 2, 3, …` crosses `x` exactly once. The first `r` with `r * r > x` marks the boundary, so `r - 1` is the largest integer whose square is `<= x`. The early return handles `0` and `1`, where the answer equals `x` itself.

## Complexity

- Time: O(√x) — the loop runs until `r` reaches roughly √x.
- Space: O(1) — only a counter is kept.
