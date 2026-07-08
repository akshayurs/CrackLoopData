The shrink loop can be replaced by arithmetic. Track only the two fruit types currently in the baskets and the **last index** at which each was seen. When a third type appears, the new window cannot include anything at or before the earlier of the two last-seen positions — so jump `left` there in one move instead of stepping.

Keeping just two "last seen" markers means the window is repaired in constant time per tree, giving a genuine single pass with a fixed handful of variables.

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> last;
        int left = 0, best = 0;
        for (int right = 0; right < (int)fruits.size(); right++) {
            last[fruits[right]] = right;
            if ((int)last.size() > 2) {
                int dropAt = right;
                for (auto& kv : last) dropAt = min(dropAt, kv.second);
                last.erase(fruits[dropAt]);
                left = dropAt + 1;
            }
            best = max(best, right - left + 1);
        }
        return best;
    }
};
```

## Why it works

`last` holds the rightmost position of each active type, so at most two entries survive. When a third type arrives, the type whose last appearance is smallest is the one we must abandon; every earlier tree of that type also leaves the window, so the new left boundary is exactly one past that position. Since two types remain valid, the jump never skips a better answer, and `best` captures the widest window at each step.

## Complexity

- Time: O(n) — one pass; the min is over at most three entries, i.e. constant.
- Space: O(1) — `last` never exceeds three keys.
