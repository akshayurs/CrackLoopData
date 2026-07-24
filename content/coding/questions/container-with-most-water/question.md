You are given an array `heights` where `heights[i]` is the height of a vertical line drawn at position `i` on the x-axis. Pick two lines that, together with the x-axis, form a container. Return the **maximum amount of water** such a container can hold.

The water a pair of lines `(i, j)` traps is bounded by the shorter of the two lines, so its area is `min(heights[i], heights[j]) * (j - i)`. The container cannot be tilted.

## Examples

```text
Input:  heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49        # lines at index 1 and 8: min(8, 7) * (8 - 1) = 49
```

```text
Input:  heights = [1, 1]
Output: 1         # min(1, 1) * (1 - 0) = 1
```

```text
Input:  heights = [4, 3, 2, 1, 4]
Output: 16        # lines at index 0 and 4: min(4, 4) * (4 - 0) = 16
```

## Constraints

- 2 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

## Follow-up

The brute force checks every pair in O(n²). Can you find the best container in a single linear scan?
