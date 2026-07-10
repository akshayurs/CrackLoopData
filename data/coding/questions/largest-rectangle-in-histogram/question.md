You are given an array `heights` where each entry is the height of a bar in a histogram, and every bar has width `1`. Consider every rectangle that can be formed using one or more **contiguous** bars, where the rectangle's height is limited by the shortest bar it spans. Return the area of the **largest** such rectangle.

## Examples

```text
Input:  heights = [2, 1, 5, 6, 2, 3]
Output: 10        # bars at indices 2..3 (5 and 6): height 5 × width 2 = 10
```

```text
Input:  heights = [2, 4]
Output: 4         # the single bar of height 4 × width 1
```

```text
Input:  heights = [1, 1]
Output: 2         # both bars at height 1 × width 2
```

## Constraints

- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

## Follow-up

The obvious solution tries every span in O(n²). Can you reach O(n) with a single scan?
