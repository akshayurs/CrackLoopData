Given an integer array `nums` and an integer `target`, find every unique quadruplet `[nums[a], nums[b], nums[c], nums[d]]` drawn from four **distinct** indices whose values sum to `target`. Two quadruplets are considered the same when they contain the same four values in the same amounts, so the answer must never list a quadruplet twice.

Return the quadruplets in **canonical form**: each quadruplet sorted in non-decreasing order, and the list of quadruplets sorted in ascending (lexicographic) order. This keeps the output deterministic no matter which order the quadruplets are discovered in.

## Examples

```text
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

```text
Input:  nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]
```

```text
Input:  nums = [1, 2, 3, 4], target = 50
Output: []        # no four values reach the target
```

## Constraints

- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- The sum of four elements can exceed 32-bit range — use a 64-bit accumulator when adding.

## Follow-up

The naive answer checks every group of four in O(n⁴). Can you generalize the two-pointer idea from 3Sum to reach O(n³)?
