The most direct reading of the problem: keep a running list of every gap you've had to climb so far. Whenever you add a new gap, re-decide from scratch which gaps deserve the free ladders — sort the list and let the largest `ladders` gaps go free, then check whether the rest fit in your remaining bricks budget.

It is wasteful (you re-sort on every step) but it mirrors exactly what the problem asks: "am I still able to continue?"

```python
def furthest_building(heights, bricks, ladders):
    climbs = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        climbs.append(diff)
        climbs.sort(reverse=True)
        bricks_needed = sum(climbs[ladders:])
        if bricks_needed > bricks:
            return i
    return len(heights) - 1
```

## Why it works

At every building, `climbs` holds every positive gap encountered up to that point. Sorting it descending and skipping the first `ladders` entries always gives the cheapest possible assignment: the biggest gaps are the ones most worth saving a ladder for, so anything left over is the true minimum brick cost to have gotten this far. If that minimum exceeds `bricks`, no assignment of ladders could have made it work, so `i` is the furthest reachable index.

## Complexity

- Time: O(n² log n) — up to n gaps are collected, and the list is re-sorted after each addition.
- Space: O(n) — the list of climbs seen so far.
