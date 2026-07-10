The same idea in JavaScript: keep a running array of every gap climbed so far. Each time a new gap shows up, re-sort the array and let the largest `ladders` gaps go free, then check whether the remaining gaps still fit in the brick budget.

It re-sorts on every step, which is wasteful, but it directly mirrors the question "can I still continue from here?"

```javascript
function furthestBuilding(heights, bricks, ladders) {
  const climbs = [];
  for (let i = 0; i < heights.length - 1; i++) {
    const diff = heights[i + 1] - heights[i];
    if (diff <= 0) continue;
    climbs.push(diff);
    climbs.sort((a, b) => b - a);
    let bricksNeeded = 0;
    for (let j = ladders; j < climbs.length; j++) bricksNeeded += climbs[j];
    if (bricksNeeded > bricks) return i;
  }
  return heights.length - 1;
}
```

## Why it works

`climbs` always holds every positive gap seen up to the current building. Sorting it descending and skipping the first `ladders` entries assigns ladders to the biggest gaps — the assignment that minimizes leftover brick cost. Whatever remains is the true minimum number of bricks needed to have reached this point; if that exceeds `bricks`, the building is unreachable and `i` is returned.

## Complexity

- Time: O(n² log n) — up to n gaps collected, re-sorted after every addition.
- Space: O(n) — the array of climbs seen so far.
