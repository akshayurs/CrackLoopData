Build prefix sums so that the sum of any window `[i, j)` is `prefix[j] - prefix[i]`. Because every value is positive, `prefix` is strictly increasing — which means for a fixed left end `i` you can *binary search* for the smallest right end whose prefix is at least `prefix[i] + target`.

Each left end contributes one logarithmic lookup instead of a linear scan, trading the quadratic inner loop for a sorted-array search.

```javascript
function minSubArrayLen(target, nums) {
  const n = nums.length;
  const prefix = new Array(n + 1).fill(0);
  for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
  let best = n + 1;
  for (let i = 0; i < n; i++) {
    const need = prefix[i] + target;
    let lo = i + 1, hi = n + 1;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (prefix[mid] >= need) hi = mid;
      else lo = mid + 1;
    }
    if (lo <= n) best = Math.min(best, lo - i);
  }
  return best <= n ? best : 0;
}
```

## Why it works

`prefix[j] - prefix[i] >= target` is equivalent to `prefix[j] >= prefix[i] + target`. Since `prefix` is monotonically increasing, the binary search finds the first index `j` satisfying that bound; that `j` gives the shortest window starting at `i`. Minimizing `j - i` over all left ends produces the global shortest window.

## Complexity

- Time: O(n log n) — one binary search per starting index.
- Space: O(n) — the prefix-sum array.
