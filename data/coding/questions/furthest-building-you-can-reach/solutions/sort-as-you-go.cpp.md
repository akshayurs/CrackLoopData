The same idea in C++: keep a running vector of every gap climbed so far. Each time a new gap appears, sort the vector descending and let the largest `ladders` gaps go free, then check whether the rest still fit in the brick budget.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        vector<int> climbs;
        for (int i = 0; i < (int)heights.size() - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) continue;
            climbs.push_back(diff);
            sort(climbs.rbegin(), climbs.rend());
            long long bricksNeeded = 0;
            for (int j = ladders; j < (int)climbs.size(); j++) bricksNeeded += climbs[j];
            if (bricksNeeded > bricks) return i;
        }
        return (int)heights.size() - 1;
    }
};
```

## Why it works

`climbs` always holds every positive gap seen up to the current building. Sorting it descending and skipping the first `ladders` entries assigns ladders to the biggest gaps, which minimizes the leftover brick cost. Whatever remains is the true minimum number of bricks needed to have reached this point; once that exceeds `bricks`, `i` is the furthest reachable index.

## Complexity

- Time: O(n² log n) — up to n gaps collected, re-sorted after every addition.
- Space: O(n) — the vector of climbs seen so far.
