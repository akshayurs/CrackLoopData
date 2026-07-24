The simplest correct approach: compute every point's squared distance to the origin, sort the whole vector by that distance, and take the first `k`. Squared distance avoids a needless square root and preserves ordering.

Ties are broken by `x` then `y` so the output is deterministic regardless of the input order.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> ordered = points;
        sort(ordered.begin(), ordered.end(), [](const vector<int>& a, const vector<int>& b) {
            long da = (long)a[0] * a[0] + (long)a[1] * a[1];
            long db = (long)b[0] * b[0] + (long)b[1] * b[1];
            if (da != db) return da < db;
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
        ordered.resize(k);
        return ordered;
    }
};
```

## Why it works

Squared distance is a monotonic function of true distance, so sorting by it yields the same order as sorting by actual distance without a `sqrt` call. Once every point is ordered nearest-to-farthest (with the x/y tiebreak applied when distances match), the first `k` entries are exactly the `k` closest points.

## Complexity

- Time: O(n log n) — one full sort of all points.
- Space: O(n) — the copied vector plus sort overhead.
