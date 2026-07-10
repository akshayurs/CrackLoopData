Fix each bar as the shortest one in the rectangle. From bar `i` at height `heights[i]`, extend as far left and as far right as every neighbouring bar is at least that tall — that span is the widest rectangle whose height is capped by bar `i`. Take the best area over all choices of `i`.

Because every rectangle is limited by its shortest bar, and we try each bar as that limiter, no rectangle is missed.

```python
def largest_rectangle_area(heights):
    n = len(heights)
    best = 0
    for i in range(n):
        left = i
        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1
        right = i
        while right < n - 1 and heights[right + 1] >= heights[i]:
            right += 1
        best = max(best, heights[i] * (right - left + 1))
    return best
```

## Why it works

For a fixed limiter `i`, the tallest rectangle of height `heights[i]` stretches until it hits a strictly shorter bar on either side. The width `right - left + 1` counts every bar in that run. Since the true maximal rectangle has some shortest bar, the iteration that fixes that bar as `i` reconstructs it exactly.

## Complexity

- Time: O(n²) — each bar may scan across the whole array while expanding.
- Space: O(1) — only a few index and running-max variables.
