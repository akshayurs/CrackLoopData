You are hopping across a row of rooftops, given as `heights`. Starting on building `0`, you want to reach as far right as possible. Moving from building `i` to building `i + 1` is free if `heights[i + 1] <= heights[i]`; otherwise you must climb a gap of `heights[i + 1] - heights[i]`, and you can cover that gap in one of two ways:

- Spend that many `bricks` (bricks are consumed one at a time and never come back).
- Use one of your `ladders` instead, which crosses any single gap regardless of its size but is limited in supply.

Given the number of `bricks` and `ladders` you start with, return the furthest building index you can reach.

## Examples

```text
Input:  heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1
Output: 4        # climb the 5-gap (2->7) with bricks, the 5-gap (9->14) with the ladder
```

```text
Input:  heights = [4, 12, 2, 7, 3, 18, 20, 3, 19], bricks = 10, ladders = 2
Output: 7
```

```text
Input:  heights = [14, 3, 19, 3], bricks = 17, ladders = 0
Output: 3
```

## Constraints

- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^6
- 0 <= bricks <= 10^9
- 0 <= ladders <= heights.length
