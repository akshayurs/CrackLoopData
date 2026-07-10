You are given an array of integers `nums` and a window size `k`. A window of `k` consecutive elements slides from the left end of the array to the right, one position at a time. For every position of the window, record the largest value inside it.

Return a list of these maximums, one per window, in the order the windows appear.

## Examples

```text
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
# windows: [1 3 -1]=3, [3 -1 -3]=3, [-1 -3 5]=5, [-3 5 3]=5, [5 3 6]=6, [3 6 7]=7
```

```text
Input:  nums = [4, 2, 12, 11, -5], k = 2
Output: [4, 12, 12, 11]
```

```text
Input:  nums = [9, 9, 9], k = 1
Output: [9, 9, 9]
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

## Follow-up

The brute force reruns the max over every window. Can you produce each answer in amortized O(1), for O(n) overall?
