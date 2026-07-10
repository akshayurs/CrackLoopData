You are given an array of non-negative integers `nums` and an integer `k`. Split `nums` into exactly `k` non-empty **contiguous** subarrays so that the largest subarray sum among the `k` pieces is as small as possible.

Return that minimized largest sum.

## Examples

```text
Input:  nums = [7, 2, 5, 10, 8], k = 2
Output: 18        # split into [7, 2, 5] and [10, 8]; sums are 14 and 18
```

```text
Input:  nums = [1, 2, 3, 4, 5], k = 2
Output: 9         # split into [1, 2, 3] and [4, 5]; sums are 6 and 9
```

```text
Input:  nums = [1, 4, 4], k = 3
Output: 4         # each element is its own subarray; largest sum is 4
```

## Constraints

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= k <= nums.length

## Follow-up

The obvious dynamic program is O(k · n²). Can you do better by searching over the answer itself instead of over the split points?
