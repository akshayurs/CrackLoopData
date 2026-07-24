The honest baseline: examine every combination of three distinct indices and keep the ones that sum to zero. The same three values can be reached through different index combinations, so we canonicalize each hit by sorting its three numbers and using the joined string as a de-duplication key.

At the end we sort the collected triplets so the output is deterministic, matching the canonical order the problem asks for.

```javascript
function threeSum(nums) {
  const seen = new Map();
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const t = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
          seen.set(t.join(","), t);
        }
      }
    }
  }
  return [...seen.values()].sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
}
```

## Why it works

Every unordered triple of indices is visited exactly once by the three nested loops. Sorting each zero-sum triple and keying the map by its comma-joined string collapses permutations of the same three values into one entry, so duplicates never survive. The final comparator sorts triplets lexicographically for the required canonical ordering.

## Complexity

- Time: O(n³) — every triple of indices is tested.
- Space: O(m) — the map holds the m unique triplets found.
