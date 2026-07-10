The most literal reading of the problem: consider every pair of lines `(i, j)`, compute the water it holds, and keep the largest. Two nested loops enumerate all pairs.

This is the honest baseline you would state first in an interview — no insight required, just definition applied directly.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = (int)heights.size();
        int best = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int area = min(heights[i], heights[j]) * (j - i);
                best = max(best, area);
            }
        }
        return best;
    }
};
```

## Why it works

Every container is defined by an unordered pair of indices, and the outer/inner loops visit each such pair exactly once. For each pair we apply the area rule directly — width times the shorter wall — and track the running maximum, so the final answer is the best over all possible containers.

## Complexity

- Time: O(n²) — about n²/2 pairs are evaluated.
- Space: O(1) — only the running maximum is stored.
