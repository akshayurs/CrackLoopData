Instead of tracking `k` separate bucket sums, track a single bitmask of which numbers have already been used, plus how much is still needed to finish the *current* bucket. Sort the numbers descending first — placing the biggest numbers early fails fast when a partition is impossible, and it lets a bucket fill up in fewer steps.

The key speedup is memoizing on `(mask, remaining)`: many different orders of picking numbers reach the same "used set + amount left in the current bucket" state, and once we know that state can't finish a valid partition, we never re-explore it.

```python
def can_partition_k_subsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k
    nums.sort(reverse=True)
    n = len(nums)
    if nums[0] > target:
        return False

    memo = {}

    def dfs(mask, remaining):
        if mask == (1 << n) - 1:
            return True
        key = (mask, remaining)
        if key in memo:
            return memo[key]
        ok = False
        for i in range(n):
            if mask & (1 << i) or nums[i] > remaining:
                continue
            next_remaining = remaining - nums[i]
            if next_remaining == 0:
                next_remaining = target
            if dfs(mask | (1 << i), next_remaining):
                ok = True
                break
        memo[key] = ok
        return ok

    return dfs(0, target)
```

## Why it works

`mask` records exactly which numbers are already assigned; `remaining` is how much room is left in the bucket currently being filled. Trying index `i` only when it is unused and fits within `remaining` mirrors the same backtracking as before, but whenever a bucket exactly fills (`next_remaining == 0`) we reset to a fresh `target` and start the next bucket. Since every number is eventually used and each bucket is forced to sum to `target`, reaching the full mask means a valid k-way partition was built. Memoizing on `(mask, remaining)` avoids recomputing states reached by different orderings of the same used set.

## Complexity

- Time: O(n * 2^n) — at most 2^n distinct masks, each doing O(n) work to try the next number.
- Space: O(2^n) — the memo table, keyed by mask (remaining takes only a handful of values per mask in practice, but bounded by target).
