The same idea in Java: keep a running list of every gap climbed so far. Each time a new gap appears, sort the list descending and let the largest `ladders` gaps go free, then check whether the rest still fit in the brick budget.

```java
import java.util.*;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        List<Integer> climbs = new ArrayList<>();
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) continue;
            climbs.add(diff);
            climbs.sort(Collections.reverseOrder());
            long bricksNeeded = 0;
            for (int j = ladders; j < climbs.size(); j++) bricksNeeded += climbs.get(j);
            if (bricksNeeded > bricks) return i;
        }
        return heights.length - 1;
    }
}
```

## Why it works

`climbs` always holds every positive gap seen up to the current building. Sorting it descending and skipping the first `ladders` entries assigns ladders to the biggest gaps, which minimizes the leftover brick cost. Whatever remains is the true minimum number of bricks needed to have reached this point; once that exceeds `bricks`, `i` is the furthest reachable index.

## Complexity

- Time: O(n² log n) — up to n gaps collected, re-sorted after every addition.
- Space: O(n) — the list of climbs seen so far.
