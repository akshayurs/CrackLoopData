You are given a binary array `nums` (containing only `0`s and `1`s) and an integer `k`. You may flip at most `k` of the zeros into ones. Return the length of the longest contiguous subarray that contains only ones after performing at most `k` such flips.

## Examples

```text
Input:  nums = [1, 1, 0, 0, 1, 1, 1, 0, 1], k = 2
Output: 7        # flip the two 0s at indices 2 and 3, making indices 0..6 all 1s
```

```text
Input:  nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3
Output: 10       # flipping three 0s inside a window yields ten consecutive 1s
```

```text
Input:  nums = [0, 0, 0], k = 0
Output: 0        # no flips allowed and no ones exist
```

## Constraints

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length

## Follow-up

Can you do it in a single pass over the array, in O(n) time and O(1) extra space?
