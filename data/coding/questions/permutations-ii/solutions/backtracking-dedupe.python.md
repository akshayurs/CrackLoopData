Instead of generating every arrangement and cleaning up afterward, avoid building the duplicates in the first place. Sort `nums` so equal values sit next to each other, then during backtracking only let a repeated value start a new branch if the *previous* copy of that value has already been fully used elsewhere in the current arrangement.

The rule is: at a given recursion depth, skip index `i` if `nums[i] == nums[i - 1]` and the earlier copy (`i - 1`) is currently unused. That forces equal values to be placed in a fixed relative order across branches, which is exactly what eliminates duplicate permutations without ever forming one.

```python
def permute_unique(nums):
    nums = sorted(nums)
    used = [False] * len(nums)
    current = []
    result = []

    def backtrack():
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack()
            current.pop()
            used[i] = False

    backtrack()
    return result
```

## Why it works

Sorting groups equal values together. When two equal values are both available at the same recursion depth, using the *later* one first before the earlier one is used would build a permutation identical to one reachable by using the earlier one first — so skipping that case removes the redundant branch entirely, not just its output. Because `nums` is sorted and indices are tried in increasing order, the recursion also naturally emits results in lexicographic order.

## Complexity

- Time: O(n! · n) worst case (all distinct values) — the pruning only removes branches that would have produced duplicates; each surviving branch still costs O(n) to materialize.
- Space: O(n) for the recursion stack, `used`, and `current`, plus O(n! · n) for the collected output.
