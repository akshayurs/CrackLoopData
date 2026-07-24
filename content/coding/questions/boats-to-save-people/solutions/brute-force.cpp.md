Every boat should carry the heaviest person still waiting — that person is the hardest to place, so serve them first. To keep boats full, try to seat the *lightest* available person alongside them; if even the lightest one does not fit, the heavy person rides alone.

Sort the weights, then repeatedly take the heaviest remaining person and linear-scan from the light end for the first partner that fits. Marking people as used makes this correct but costs a scan per boat.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int n = (int)people.size();
        vector<bool> used(n, false);
        int boats = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (used[j]) continue;
            used[j] = true;
            boats++;
            for (int i = 0; i < j; i++) {
                if (!used[i] && people[i] + people[j] <= limit) {
                    used[i] = true;
                    break;
                }
            }
        }
        return boats;
    }
};
```

## Why it works

Processing people from heaviest to lightest guarantees each boat is anchored by the most constrained remaining passenger. Pairing that anchor with the lightest available person never wastes capacity: if the lightest cannot join, no one can, so the anchor sails alone. Every person is placed exactly once, so the boat count is minimal.

## Complexity

- Time: O(n²) — a linear partner scan for each of up to n boats.
- Space: O(n) — the `used` array plus the sort.
