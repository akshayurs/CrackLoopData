Instead of tracking `k` separate bucket sums, track a single bitmask of which numbers have already been used, plus how much is still needed to finish the *current* bucket. Sort the numbers descending first — placing the biggest numbers early fails fast when a partition is impossible, and it lets a bucket fill up in fewer steps.

The key speedup is memoizing on the combination of `mask` and `remaining`: many different orders of picking numbers reach the same "used set + amount left in the current bucket" state, and once we know that state can't finish a valid partition, we never re-explore it.

```javascript
function canPartitionKSubsets(nums, k) {
  const total = nums.reduce((a, b) => a + b, 0);
  if (total % k !== 0) return false;
  const target = total / k;
  const sorted = [...nums].sort((a, b) => b - a);
  const n = sorted.length;
  if (sorted[0] > target) return false;

  const memo = new Map();

  function dfs(mask, remaining) {
    if (mask === (1 << n) - 1) return true;
    const key = mask + ':' + remaining;
    if (memo.has(key)) return memo.get(key);
    let ok = false;
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i) || sorted[i] > remaining) continue;
      let nextRemaining = remaining - sorted[i];
      if (nextRemaining === 0) nextRemaining = target;
      if (dfs(mask | (1 << i), nextRemaining)) {
        ok = true;
        break;
      }
    }
    memo.set(key, ok);
    return ok;
  }

  return dfs(0, target);
}
```

## Why it works

`mask` records exactly which numbers are already assigned; `remaining` is how much room is left in the bucket currently being filled. Trying index `i` only when it is unused and fits within `remaining` mirrors the same backtracking as before, but whenever a bucket exactly fills (`nextRemaining === 0`) we reset to a fresh `target` and start the next bucket. Since every number is eventually used and each bucket is forced to sum to `target`, reaching the full mask means a valid k-way partition was built. Memoizing on `mask` + `remaining` avoids recomputing states reached by different orderings of the same used set.

## Complexity

- Time: O(n * 2^n) — at most 2^n distinct masks, each doing O(n) work to try the next number.
- Space: O(2^n) — the memo table, keyed by mask and remaining.
