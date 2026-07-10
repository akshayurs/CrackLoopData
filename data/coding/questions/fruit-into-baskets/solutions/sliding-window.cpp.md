Grow a window from the left and let the right edge advance one tree at a time, keeping a count of how many trees of each type sit inside the window. The window is always allowed to contain at most two distinct types.

Whenever adding the newest tree pushes the distinct-type count to three, shrink from the left — dropping one tree per step and removing a type from the map when its count hits zero — until only two types remain. After each repair the window is valid again, so its current length is a candidate answer.

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> counts;
        int left = 0, best = 0;
        for (int right = 0; right < (int)fruits.size(); right++) {
            counts[fruits[right]]++;
            while ((int)counts.size() > 2) {
                int drop = fruits[left];
                if (--counts[drop] == 0) {
                    counts.erase(drop);
                }
                left++;
            }
            best = max(best, right - left + 1);
        }
        return best;
    }
};
```

## Why it works

`counts` is a live tally of the current window, so `counts.size()` is exactly the number of baskets in use. The `while` loop only runs when there are three types, and it always restores the two-type invariant before the length is recorded, so every measured window is legal. Because `left` never moves backward, the answer is the widest valid window ever seen.

## Complexity

- Time: O(n) — each index is added once by `right` and removed at most once by `left`.
- Space: O(1) — the map holds at most three keys at any moment.
