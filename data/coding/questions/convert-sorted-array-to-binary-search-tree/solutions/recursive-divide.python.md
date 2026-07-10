A sorted array is already "in order" for a BST — the only question is which element becomes the root. Pick the middle of the current slice, and everything to its left is smaller (goes in the left subtree) while everything to its right is bigger (goes in the right subtree). Recursing on each half with that same rule keeps every subtree balanced automatically, since the two halves can never differ in size by more than one.

The base case is an empty slice, which contributes no node at all.

```python
def sorted_array_to_bst(nums):
    def build(lo, hi):
        if lo > hi:
            return None
        mid = lo + (hi - lo) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(nums) - 1)
```

## Why it works

`build(lo, hi)` always hands back a valid height-balanced BST over `nums[lo..hi]`: the middle element sits above two halves that are each within one element in size of each other, and both halves are themselves built by the same rule, so the balance property holds at every level by induction. Since `nums` is sorted, everything left of `mid` is less than `nums[mid]` and everything right of it is greater, which is exactly the BST ordering requirement.

## Complexity

- Time: O(n) — every index is visited exactly once to create its node.
- Space: O(log n) — the recursion stack is as deep as the tree's height, which is O(log n) because the split always halves the range, excluding the O(n) output tree itself.
