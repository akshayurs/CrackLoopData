The same idea in C++: two nested loops over the vector, XORing every pair and keeping the best result. No auxiliary storage.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxXor(vector<int>& nums) {
        int best = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            for (int j = i + 1; j < (int)nums.size(); j++) {
                best = max(best, nums[i] ^ nums[j]);
            }
        }
        return best;
    }
};
```

## Why it works

The outer loop fixes the first element; the inner loop pairs it with every later element, so every unordered pair is XORed exactly once. The running maximum captures the largest XOR seen across all pairs.

## Complexity

- Time: O(n²) — every pair is XORed once.
- Space: O(1) — only a running maximum.
