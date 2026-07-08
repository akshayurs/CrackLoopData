The most direct reading: try every pair `(i, j)` with `i < j` and check whether they sum to the target. It ignores the sorted order, but it is the honest baseline before optimizing.

Because positions are 1-indexed, we add one to each loop counter when returning.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = (int)numbers.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (numbers[i] + numbers[j] == target) {
                    return {i + 1, j + 1};
                }
            }
        }
        return {};
    }
};
```

## Why it works

The outer loop fixes the first element; the inner loop scans every later element, so each unordered pair is examined exactly once. The first pair that reaches `target` is returned as 1-indexed positions, and the one-solution guarantee means the empty return is never reached.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — no extra structure.
