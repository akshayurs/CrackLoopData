Think of the choice as *where to place the cuts*. Let `best[j][i]` be the smallest possible "largest piece" when the first `i` elements are split into `j` groups. To fill it, let the last group start at index `t`: everything before `t` is split into `j-1` groups, and the last group `nums[t..i-1]` contributes its own sum. The cost of that plan is the *max* of the earlier answer and the last group's sum, and we take the minimum over every valid start `t`.

Prefix sums give each subarray sum in O(1), and we sweep `j` from 1 to `k` and `i` over the array, so the whole table is built bottom-up.

```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        const long long INF = LLONG_MAX;
        vector<vector<long long>> best(k + 1, vector<long long>(n + 1, INF));
        best[0][0] = 0;
        for (int j = 1; j <= k; j++) {
            for (int i = 1; i <= n; i++) {
                for (int t = j - 1; t < i; t++) {
                    if (best[j - 1][t] == INF) continue;
                    long long last = prefix[i] - prefix[t];
                    long long cost = max(best[j - 1][t], last);
                    best[j][i] = min(best[j][i], cost);
                }
            }
        }
        return (int)best[k][n];
    }
};
```

## Why it works

Any split of `i` elements into `j` groups is uniquely defined by where the last group begins. Trying every start `t` and combining the optimal sub-solution `best[j-1][t]` with the last group's sum covers all splits, and the `max` captures that the objective is the largest piece. Taking the minimum over `t` gives the optimum for `best[j][i]`, so `best[k][n]` is the answer.

## Complexity

- Time: O(k · n²) — three nested loops over groups, endpoints, and cut positions.
- Space: O(k · n) — the DP table.
