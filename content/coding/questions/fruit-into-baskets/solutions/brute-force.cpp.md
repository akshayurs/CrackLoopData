Restate the problem as: find the longest run that never holds more than two kinds of fruit. The most direct attack is to try every possible starting tree, then keep walking right while the set of collected types stays at size two or fewer, stopping as soon as a third type appears.

Track the running answer as the largest window length seen across all starts. It is quadratic, but it makes the rule crystal clear before optimising.

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = (int)fruits.size();
        int best = 0;
        for (int start = 0; start < n; start++) {
            unordered_set<int> types;
            for (int end = start; end < n; end++) {
                types.insert(fruits[end]);
                if ((int)types.size() > 2) break;
                best = max(best, end - start + 1);
            }
        }
        return best;
    }
};
```

## Why it works

For each `start`, the inner loop grows the window one tree at a time and records every distinct type. The instant a third distinct type is added the run is illegal, so we break and move the start forward. Every valid two-type run is the prefix of some start, so the global maximum is guaranteed to be examined.

## Complexity

- Time: O(n^2) — each of n starts scans up to n trees.
- Space: O(1) — the type set holds at most three entries before breaking.
