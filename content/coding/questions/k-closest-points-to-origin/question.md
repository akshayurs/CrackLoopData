You are given a list of `points` on the 2D plane, where `points[i] = [xi, yi]`, and an integer `k`. Return the `k` points closest to the origin `(0, 0)`, using ordinary Euclidean distance.

You may return the answer in any order the distance ties allow, but for this exercise report it **sorted by distance ascending, breaking ties by x then by y** — that keeps the output deterministic no matter how you selected the points.

## Examples

```text
Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]        # dist² = 8 vs 10, so (-2, 2) is closer
```

```text
Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]   # dist² = 18, 26, 20 -> two smallest are 18 and 20
```

```text
Input:  points = [[0, 1], [1, 0], [1, 1], [-1, -1]], k = 2
Output: [[0, 1], [1, 0]]    # (0,1) and (1,0) both have dist² = 1; tie broken by x then y
```

## Constraints

- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

## Follow-up

Can you avoid sorting the entire input when `k` is much smaller than `n`?
