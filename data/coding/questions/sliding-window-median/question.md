You're given an array of integers `nums` and a window size `k`. A window of size `k` slides across `nums` from left to right, one position at a time. For every position, compute the median of the `k` numbers currently inside the window — if `k` is odd, the median is the middle value once those numbers are sorted; if `k` is even, it's the average of the two middle values. Return the medians in the order the windows appear.

## Examples

```text
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]   # windows: [1,3,-1] [3,-1,-3] [-1,-3,5] [-3,5,3] [5,3,6] [3,6,7]
```

```text
Input:  nums = [1, 2, 3, 4], k = 2
Output: [1.5, 2.5, 3.5]        # k is even, so each median averages the two middle values
```

```text
Input:  nums = [5, 2, 8, 10, 3], k = 1
Output: [5, 2, 8, 10, 3]       # a window of size 1 is its own median
```

## Constraints

- 1 <= k <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- The window always moves forward by exactly one element until it reaches the end of `nums`.
