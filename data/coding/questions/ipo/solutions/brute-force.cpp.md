Simulate the process literally. At each of the `k` rounds, scan every project that hasn't been used yet, keep only the ones whose `capital` the company can currently afford, and greedily take the affordable one with the largest `profit`. Add that profit to the money and mark the project used.

This mirrors the problem statement exactly — no cleverness, just "look at everything, pick the best affordable option, repeat" — so it's a solid first pass before optimizing the repeated scanning.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    long long maxCapital(int k, long long w, vector<int>& profit, vector<int>& capital) {
        int n = profit.size();
        vector<bool> used(n, false);
        long long money = w;

        for (int round = 0; round < k; round++) {
            int best = -1;
            for (int i = 0; i < n; i++) {
                if (!used[i] && capital[i] <= money) {
                    if (best == -1 || profit[i] > profit[best]) {
                        best = i;
                    }
                }
            }
            if (best == -1) break;
            money += profit[best];
            used[best] = true;
        }

        return money;
    }
};
```

## Why it works

Each round is a local greedy choice: among everything currently affordable, taking the largest profit can never hurt, because money only grows and every affordable project stays affordable (or more so) later. Doing this `k` times, re-scanning from scratch each round, reproduces the optimal simulation — it's just slow because affordability and "used" status are recomputed every round instead of tracked incrementally.

## Complexity

- Time: O(k * n) — each of the `k` rounds rescans all `n` projects.
- Space: O(n) — the `used` vector.
