You are given an integer array `nums` sorted in non-decreasing order. Remove the duplicates **in place** so that each distinct value appears only once, keeping the relative order of the values. Because the array cannot be resized, do the compaction at the front: after you are done, the first `k` slots of `nums` must hold the `k` distinct values in order, and you should return `k`.

Whatever is left beyond the first `k` positions does not matter — the grader only inspects `nums[0..k)`.

## Examples

```text
Input:  nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]        # two distinct values: 1 and 2
```

```text
Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

```text
Input:  nums = [1, 2, 3]
Output: 3, nums = [1, 2, 3]        # already distinct, nothing to remove
```

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order.

## Follow-up

The array is already sorted — can you compact it using only O(1) extra space, without allocating a second array?
