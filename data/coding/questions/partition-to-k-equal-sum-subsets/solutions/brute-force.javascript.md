The most direct reading of the problem: try to build the `k` buckets one number at a time. Walk the array in order, and for each number try dropping it into every bucket that still has room; if a full assignment of all numbers ever leaves every bucket exactly at the target sum, we found a partition.

This is the honest baseline — no memoization, just backtracking with one simple prune: never try the same number in two different *empty* buckets, since that always leads to the same dead end twice.

```javascript
function canPartitionKSubsets(nums, k) {
  const total = nums.reduce((a, b) => a + b, 0);
  if (total % k !== 0) return false;
  const target = total / k;
  const buckets = new Array(k).fill(0);

  function backtrack(i) {
    if (i === nums.length) {
      return buckets.every((b) => b === target);
    }
    for (let j = 0; j < k; j++) {
      if (buckets[j] + nums[i] <= target) {
        buckets[j] += nums[i];
        if (backtrack(i + 1)) return true;
        buckets[j] -= nums[i];
      }
      if (buckets[j] === 0) break;
    }
    return false;
  }

  return backtrack(0);
}
```

## Why it works

`buckets[j]` tracks the running sum of the j-th subset. Placing `nums[i]` is only attempted where it fits under `target`, and after a failed placement it is removed before the next bucket is tried — standard backtracking. The `if (buckets[j] === 0) break` prune skips redundant empty buckets: trying an empty bucket that just failed can never succeed in a different empty bucket either. A full assignment succeeds only if every bucket lands exactly on `target`.

## Complexity

- Time: O(k^n) — each of the n numbers can go into any of k buckets in the worst case.
- Space: O(k + n) — bucket sums plus the recursion stack.
