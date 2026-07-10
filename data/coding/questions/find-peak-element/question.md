You are given an integer array `nums`. A **peak** is an element that is strictly greater than both of its neighbors. Return the index of any peak element.

Treat the positions just outside the array as negative infinity — so `nums[-1]` and `nums[n]` are considered smaller than everything. This guarantees a peak always exists (for example, the array's maximum is always a peak).

## Examples

```text
Input:  nums = [1, 2, 3, 1]
Output: 2        # nums[2] = 3 is greater than nums[1] = 2 and nums[3] = 1
```

```text
Input:  nums = [1]
Output: 0        # the only element has no neighbors, so it is a peak
```

```text
Input:  nums = [5, 4, 3, 2, 1]
Output: 0        # nums[0] = 5 is greater than nums[1] = 4
```

## Constraints

- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- No two adjacent elements are equal (`nums[i] != nums[i + 1]`).

## Follow-up

A linear scan finds a peak in O(n). Can you do it in O(log n)?
