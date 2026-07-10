The simplest thing that works: forget the matrix structure entirely. Every value is a candidate, so copy them all into one flat vector, sort it, and index into position `k`.

This throws away the sortedness of the rows and columns, but it's a correct baseline and easy to reason about — a good place to start before optimizing.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> flat;
        for (const auto& row : matrix) {
            for (int value : row) {
                flat.push_back(value);
            }
        }
        sort(flat.begin(), flat.end());
        return flat[k - 1];
    }
};
```

## Why it works

Copying gathers all n² values into one vector, and `sort` orders them ascending including duplicates. The `k`th smallest in overall order is then the element at zero-based index `k - 1`.

## Complexity

- Time: O(n² log n) — sorting n² values dominates.
- Space: O(n²) — the flattened vector holds every value.
