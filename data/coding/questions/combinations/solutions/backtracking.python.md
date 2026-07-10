Instead of generating everything and filtering, build combinations one number at a time and abandon a partial choice the moment it can no longer succeed. Track a `path` of numbers picked so far and a `start` index; at each step try every candidate from `start` up to `n`, recurse, then undo the pick before trying the next candidate.

The key prune: if `path` needs `remaining_needed` more numbers, there is no point starting past `n - remaining_needed + 1`, since not enough numbers would be left to finish the combination. Because candidates are always tried in increasing order, combinations are produced already in lexicographic order — no sort needed.

```python
def combine(n, k):
    result = []
    path = []

    def backtrack(start):
        if len(path) == k:
            result.append(path[:])
            return
        remaining_needed = k - len(path)
        for i in range(start, n - remaining_needed + 2):
            path.append(i)
            backtrack(i + 1)
            path.pop()

    backtrack(1)
    return result
```

## Why it works

The recursion explores a decision tree where each level picks the next number to add, always larger than the last pick — this guarantees no combination is produced twice and every combination is already sorted internally. `path.pop()` restores the state after each recursive call, so sibling branches start clean. The bound `n - remaining_needed + 1` prunes branches that cannot possibly reach size `k`, skipping work the brute-force approach would otherwise waste on doomed subsets.

## Complexity

- Time: O(k * C(n, k)) — there are C(n, k) complete combinations, each costing O(k) to copy into the result.
- Space: O(k) — recursion depth and the `path` buffer, excluding the returned combinations.
