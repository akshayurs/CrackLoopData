You are given an integer array `nums` that was originally sorted in non-decreasing order and then rotated at some unknown pivot, so a suffix of the array was moved to the front. Unlike the classic version, `nums` **may contain duplicate values**. Given a `target`, return `true` if `target` is present in `nums` and `false` otherwise.

## Examples

```text
Input:  nums = [2, 5, 6, 0, 0, 1, 2], target = 0
Output: true
```

```text
Input:  nums = [2, 5, 6, 0, 0, 1, 2], target = 3
Output: false
```

```text
Input:  nums = [1, 0, 1, 1, 1], target = 0
Output: true
```

## Constraints

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- `nums` is guaranteed to be a rotation of a non-decreasing array.
- -10^4 <= target <= 10^4

## Follow-up

Duplicates break the clean O(log n) guarantee of the no-duplicates version. Can you explain why the worst case degrades to O(n), and when it still runs in O(log n)?
