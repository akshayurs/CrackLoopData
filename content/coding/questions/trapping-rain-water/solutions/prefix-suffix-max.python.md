The brute force recomputes the same left and right maxima over and over. Precompute them once instead: `left_max[i]` is the tallest bar at or before `i`, and `right_max[i]` is the tallest at or after `i`. Both fill in a single sweep each.

With those tables ready, the water at every column is just `min(left_max[i], right_max[i]) - height[i]`, summed in a final linear pass.

```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
```

## Why it works

`left_max` and `right_max` capture exactly the two walls that bound the water above each column. Because they are built cumulatively, each entry reuses the previous result in O(1), turning the quadratic rescans into three linear passes while producing the identical per-column depth.

## Complexity

- Time: O(n) — three linear passes.
- Space: O(n) — two auxiliary arrays of size n.
