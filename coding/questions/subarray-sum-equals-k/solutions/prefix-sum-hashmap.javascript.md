Reframe the sum of a subarray in terms of running totals. If `prefix[j]` is the sum of the first `j` elements, then the subarray ending right before index `j` and starting after index `i` sums to `prefix[j] - prefix[i]`. Asking "does this window sum to `k`?" becomes "have I seen an earlier prefix equal to `prefix[j] - k`?".

So carry one running sum and a map that counts how many times each prefix value has occurred. At each element, look up how many earlier prefixes equal `running - k`: each one marks a distinct subarray ending here that sums to `k`. Seeding the map with `0 -> 1` lets a subarray that starts at index 0 be counted.

```javascript
function subarraySum(nums, k) {
  let count = 0;
  let running = 0;
  const seen = new Map([[0, 1]]);
  for (const n of nums) {
    running += n;
    count += seen.get(running - k) || 0;
    seen.set(running, (seen.get(running) || 0) + 1);
  }
  return count;
}
```

## Why it works

`running - k` is the prefix sum some earlier position must have had for the stretch between it and the current position to total `k`. Because `seen` stores counts, not just presence, repeated prefix values (common with negatives and zeros) each contribute a separate subarray. Recording `running` only after the lookup keeps the empty prefix ordering correct, and the `0 -> 1` seed accounts for windows that begin at the very start.

## Complexity

- Time: O(n) — one pass, each map operation O(1) on average.
- Space: O(n) — up to n distinct prefix sums stored.
