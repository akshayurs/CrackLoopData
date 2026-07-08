**Two pointers** means walking an array (or string) with two indices instead of one, moving them according to a rule so that each step throws away work you would otherwise redo. It replaces an O(n²) nested loop with a single O(n) pass, using O(1) extra space.

There are two common shapes:

- **Converging pointers** — one starts at the left, one at the right, and they move toward each other. This is the shape for sorted-array problems: compare the pair's combined value to a target and move whichever pointer improves the comparison.
- **Parallel (fast/slow) pointers** — both start near the same end and move in the same direction at different speeds or under different conditions, useful for in-place partitioning, deduplication, and cycle detection.

The key insight that makes converging pointers work on **sorted** data: if `left + right` is too big, only shrinking `right` can help — increasing `left` only makes it bigger. That monotonicity is what lets you discard a whole side of the search space per step instead of trying every pair.

A typical converging shape:

```
left = 0, right = n - 1
while left < right:
    if combine(a[left], a[right]) == target:
        record/return
        left += 1; right -= 1
    elif combine(a[left], a[right]) < target:
        left += 1
    else:
        right -= 1
```

The trade being made is the mirror image of hashing's: instead of spending O(n) space to avoid a second loop, two pointers spend **no extra space** but require the data to already be sorted (or sortable up front) so that pointer movement is guaranteed to make progress in the right direction.
