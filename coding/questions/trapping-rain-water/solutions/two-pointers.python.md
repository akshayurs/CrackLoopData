The prefix/suffix arrays can be dropped entirely. Keep two pointers walking inward from both ends, along with the best wall seen from each side. The key insight: at whichever side has the *shorter* running maximum, that side's wall alone decides the water level — the opposite side is guaranteed to hold at least as high, so the far max never matters.

So always advance the pointer on the smaller-wall side. If the current bar is below that side's running max, the gap fills with water; otherwise it raises the wall.

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    total = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            total += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total += right_max - height[right]
            right -= 1
    return total
```

## Why it works

When `height[left] < height[right]`, the right side has a bar at least as tall as `height[left]`, so the true right max is `>= height[left]` and cannot be the limiting wall. That makes `left_max` the sole cap at `left`, and `left_max - height[left]` is exactly the trapped water there. The symmetric argument holds on the other branch. Each column is settled once as its pointer moves, so no lookahead is needed.

## Complexity

- Time: O(n) — each pointer moves inward at most n times total.
- Space: O(1) — four scalars, no auxiliary arrays.
