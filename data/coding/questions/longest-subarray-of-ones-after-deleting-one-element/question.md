You are given a binary array `nums` containing only `0`s and `1`s. You must delete **exactly one** element from it. Return the length of the longest contiguous run of `1`s in the resulting array.

The deletion is mandatory even when the array is all `1`s. If no subarray of `1`s remains after the deletion, return `0`.

## Examples

```text
Input:  nums = [1, 1, 0, 1]
Output: 3        # delete the 0 → [1, 1, 1], a run of three 1s
```

```text
Input:  nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
Output: 5        # delete the 0 at index 4 → 1,1,1 joins 1,1 into a run of five
```

```text
Input:  nums = [1, 1, 1]
Output: 2        # a deletion is required, so the best run left is two 1s
```

## Constraints

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

## Follow-up

Can you solve it in a single pass with O(1) extra space?
