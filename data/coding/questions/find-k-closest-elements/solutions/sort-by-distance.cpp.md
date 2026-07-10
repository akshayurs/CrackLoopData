The most direct reading of the problem: rank every element by how far it is from `x`, keep the best `k`, then put them back in order. Sort a copy by distance first and, for ties, by value so the smaller one wins.

Taking the first `k` of that ordering gives the closest set; a final ascending sort restores the required output order.

```cpp
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> byDistance(arr);
        sort(byDistance.begin(), byDistance.end(), [x](int a, int b) {
            int da = abs(a - x), db = abs(b - x);
            return da != db ? da < db : a < b;
        });
        vector<int> result(byDistance.begin(), byDistance.begin() + k);
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

The comparator orders by distance first and, on ties, by value — so equal-distance elements place the smaller one earlier, matching the tie-break rule. The first `k` entries are the closest integers. Because the answer must be ascending, the closing `sort` reorders that slice by value.

## Complexity

- Time: O(n log n) — dominated by the distance sort over all n elements.
- Space: O(n) — the sorted copy of the array.
