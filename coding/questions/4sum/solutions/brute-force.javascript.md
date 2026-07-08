The honest baseline: examine every group of four distinct indices and keep those whose values sum to `target`. Four nested loops enumerate all combinations directly.

Sorting first means each combination `i < j < k < l` is already non-decreasing, so a joined-key `Set` deduplicates the value-groups; a final comparator sort restores the canonical lexicographic order.

```javascript
function fourSum(nums, target) {
  nums.sort((a, b) => a - b);
  const n = nums.length;
  const seen = new Set();
  const res = [];
  for (let i = 0; i < n; i++)
    for (let j = i + 1; j < n; j++)
      for (let k = j + 1; k < n; k++)
        for (let l = k + 1; l < n; l++)
          if (nums[i] + nums[j] + nums[k] + nums[l] === target) {
            const quad = [nums[i], nums[j], nums[k], nums[l]];
            const key = quad.join(",");
            if (!seen.has(key)) { seen.add(key); res.push(quad); }
          }
  res.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2] || a[3] - b[3]);
  return res;
}
```

## Why it works

The four loops walk strictly increasing indices, so every unordered quadruplet of positions is tried exactly once. Sorting up front makes each stored quadruplet non-decreasing, and the string key skips repeats. JavaScript numbers are doubles, exact well past 4·10^9, so the sum never overflows. The final sort produces the canonical order.

## Complexity

- Time: O(n^4) — every quadruplet of indices is inspected.
- Space: O(m) — the set and result hold the m distinct matching quadruplets.
