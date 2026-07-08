Start with the widest possible container: one pointer at each end. This pair already maximizes the width, so any narrower container can only beat it by being taller. The wall that limits the current area is the shorter of the two, and moving the taller wall inward can never help — width shrinks and the height is still capped by the short wall. So always move the shorter wall inward, hunting for a taller line.

Each step discards the shorter wall, which cannot be part of any better container involving that side, so no candidate is missed while the pointers converge in a single pass.

```python
def max_area(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        if area > best:
            best = area
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
```

## Why it works

The area is `min(left_wall, right_wall) * width`. Moving the taller wall keeps the height capped by the shorter wall while strictly reducing width, so it never improves the result — every container that used the shorter wall as a limiter has already been measured at its maximum width. Advancing the shorter wall is the only move that can raise the limiting height, so discarding it loses nothing. Both pointers together traverse the array once.

## Complexity

- Time: O(n) — each pointer moves inward at most n times total.
- Space: O(1) — two indices and the running maximum.
