You are given an integer array `nums` sorted in strictly ascending order. Build a **height-balanced** binary search tree from it and return the root.

A tree is height-balanced when, for every node, the heights of its left and right subtrees differ by no more than 1. Since several balanced trees can satisfy a given array, when a subtree's remaining slice has an even number of elements always root it at the **left-of-center** element (the lower of the two middle indices) — this makes the output deterministic. Trees are printed in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  nums = [-10, -3, 0, 5, 9]
Output: [0, -10, 5, null, -3, null, 9]
```

```text
Input:  nums = [1, 3]
Output: [1, null, 3]
```

```text
Input:  nums = []
Output: []
```

## Constraints

- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in strictly increasing order.
