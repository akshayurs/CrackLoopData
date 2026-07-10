A sorted array of **distinct** integers was rotated at some unknown pivot before you received it. For example, `[0, 1, 2, 4, 5, 6, 7]` might arrive as `[4, 5, 6, 7, 0, 1, 2]`. Given the rotated array `nums` and an integer `target`, return the index of `target` in `nums`, or `-1` if it is not present.

Aim for `O(log n)` runtime.

## Examples

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

```text
Input:  nums = [1], target = 1
Output: 0
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- All values in nums are distinct.
- nums is a (possibly zero) rotation of an ascending sorted array.
- -10^4 <= target <= 10^4

## Follow-up

Can you achieve `O(log n)` time with a single modified binary search, rather than an `O(n)` scan?
