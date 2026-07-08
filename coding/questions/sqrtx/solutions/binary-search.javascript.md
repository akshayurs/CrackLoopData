The answer lives somewhere in `[0, x]`, and the predicate "is `mid * mid <= x`?" is monotonic — true for small candidates, false once you pass the root. That is exactly the setup for binary search: halve the range each step instead of walking it.

Track the best candidate that still satisfies `mid * mid <= x`. When the search window closes, that candidate is the floored square root.

```javascript
function mySqrt(x) {
  let lo = 0;
  let hi = x;
  let ans = 0;
  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (mid * mid <= x) {
      ans = mid;
      lo = mid + 1;
    } else {
      hi = mid - 1;
    }
  }
  return ans;
}
```

## Why it works

Because squares increase monotonically, once `mid * mid <= x` we know the true root is `mid` or larger, so we record `mid` and search the upper half; otherwise the root is smaller and we search the lower half. Each iteration halves the interval, and `ans` always holds the largest verified candidate, which is the floor of √x when the loop ends.

## Complexity

- Time: O(log x) — the search interval halves each step.
- Space: O(1) — only a few integers are stored.
