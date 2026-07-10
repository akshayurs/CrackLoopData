Build prefix sums so that the sum of any window `[i, j)` is `prefix[j] - prefix[i]`. Because every value is positive, `prefix` is strictly increasing — which means for a fixed left end `i` you can *binary search* for the smallest right end whose prefix is at least `prefix[i] + target`.

Each left end contributes one logarithmic lookup instead of a linear scan, trading the quadratic inner loop for a sorted-array search.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = (int)nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        int best = n + 1;
        for (int i = 0; i < n; i++) {
            long long need = prefix[i] + (long long)target;
            int j = (int)(lower_bound(prefix.begin() + i + 1, prefix.end(), need) - prefix.begin());
            if (j <= n) best = min(best, j - i);
        }
        return best <= n ? best : 0;
    }
};
```

## Why it works

`prefix[j] - prefix[i] >= target` is equivalent to `prefix[j] >= prefix[i] + target`. Since `prefix` is monotonically increasing, `lower_bound` finds the first index `j` satisfying that bound; that `j` gives the shortest window starting at `i`. Minimizing `j - i` over all left ends produces the global shortest window.

## Complexity

- Time: O(n log n) — one binary search per starting index.
- Space: O(n) — the prefix-sum array.
