Ignore the ordering entirely and look at every cell. If any of them equals the target, the answer is `true`; if the whole matrix is exhausted without a hit, it is `false`. This is the most direct thing you can do and a good baseline before exploiting the sorted structure.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (const auto& row : matrix) {
            for (int value : row) {
                if (value == target) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

## Why it works

Every position in the matrix is inspected exactly once, so if the target is present it must be found. The sorted property is never used here — correctness comes purely from exhaustive checking.

## Complexity

- Time: O(m·n) — every cell is visited in the worst case.
- Space: O(1) — only a couple of loop variables.
