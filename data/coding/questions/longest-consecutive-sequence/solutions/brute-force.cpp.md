The most literal reading: for every value in the array, pretend it is the start of a run and keep asking "is the next integer here too?" Each lookup scans the whole vector, and we grow the run one step at a time until the next value is missing.

No extra data structures, no sorting — just repeated linear searches. It is the honest baseline you would state before reaching for something faster.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int best = 0;
        for (int start : nums) {
            if (find(nums.begin(), nums.end(), start - 1) != nums.end()) continue;
            int length = 1;
            while (find(nums.begin(), nums.end(), start + length) != nums.end()) length++;
            best = max(best, length);
        }
        return best;
    }
};
```

## Why it works

A value only begins a run if `start - 1` is absent, so we skip interior values and only count each run from its true left end. From a start we walk `start + 1`, `start + 2`, … using `find` over the vector, extending `length` until the chain breaks. The largest length seen wins. Each `find` is a linear scan, which is what makes this slow.

## Complexity

- Time: O(n³) — for each of n values we may walk a run of length up to n, and every `find` scans the n-element vector.
- Space: O(1) — only counters, no auxiliary structure.
