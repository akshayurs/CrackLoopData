A collision only ever happens between adjacent asteroids where a right-mover sits directly left of a left-mover — a `+, -` pair. The most direct approach is to keep scanning the vector for the first such pair, resolve it, and start over, repeating until a full pass finds nothing left to collide.

Each resolution removes one or both of the colliding asteroids, so the vector only shrinks. When a pass completes without touching anything, the arrangement is stable and we return it. It is simple to reason about but wasteful: one explosion forces a re-scan from the beginning.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> arr(asteroids);
        bool stable = false;
        while (!stable) {
            stable = true;
            for (int i = 0; i + 1 < (int)arr.size(); i++) {
                if (arr[i] > 0 && arr[i + 1] < 0) {
                    stable = false;
                    int right = arr[i], left = -arr[i + 1];
                    if (right < left) arr.erase(arr.begin() + i);
                    else if (right > left) arr.erase(arr.begin() + i + 1);
                    else arr.erase(arr.begin() + i, arr.begin() + i + 2);
                    break;
                }
            }
        }
        return arr;
    }
};
```

## Why it works

Only a `positive, negative` adjacency can collide; any other pair is stable. We always resolve the leftmost such pair, delete the loser (or both on a tie), then restart the scan because deleting an element can create a brand-new adjacency. The vector shrinks on every non-trivial pass, so the loop terminates, and it exits exactly when no collidable pair remains.

## Complexity

- Time: O(n^2) — up to O(n) explosions, each triggering an O(n) rescan.
- Space: O(1) — resolved in place, ignoring the output copy.
