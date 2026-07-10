If the numbers were sorted, consecutive values would sit next to each other, so the longest run becomes a single left-to-right scan. Sort once, then walk the vector tracking how long the current increasing-by-one streak is.

The only subtlety is duplicates: when the next value equals the current one it neither extends nor breaks the run, so we skip past it without changing the streak.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        int best = 1, current = 1;
        for (size_t i = 1; i < sorted.size(); i++) {
            if (sorted[i] == sorted[i - 1]) continue;
            if (sorted[i] == sorted[i - 1] + 1) {
                current++;
                best = max(best, current);
            } else {
                current = 1;
            }
        }
        return best;
    }
};
```

## Why it works

Once sorted, values are ascending. Equal neighbors are skipped so a duplicate never disturbs the streak; a true consecutive pair (`sorted[i] == sorted[i-1] + 1`) grows `current`, and any gap resets it to 1. `best` tracks the longest streak observed across the scan.

## Complexity

- Time: O(n log n) — dominated by `sort`; the scan afterward is linear.
- Space: O(n) — the sorted copy of the input.
