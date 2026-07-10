Instead of building a full permutation and checking it at the end, fill positions one at a time — `1`, then `2`, and so on — and only ever place a value that already satisfies the rule for the current position. A bad choice is rejected immediately instead of surviving to the final check, so most of the search tree never gets explored.

Track which values are already used with a boolean vector, and count how many ways the remaining positions can be completed once a value is placed. When every position from `1` to `n` has been filled, that is one valid arrangement.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countArrangement(int n) {
        used.assign(n + 1, false);
        N = n;
        return backtrack(1);
    }

private:
    vector<bool> used;
    int N;

    int backtrack(int pos) {
        if (pos > N) return 1;
        int total = 0;
        for (int val = 1; val <= N; val++) {
            if (!used[val] && (val % pos == 0 || pos % val == 0)) {
                used[val] = true;
                total += backtrack(pos + 1);
                used[val] = false;
            }
        }
        return total;
    }
};
```

## Why it works

`backtrack(pos)` counts completions of positions `pos..N` given the values already used. At each call it only tries values that are both unused and legal for `pos`, so every path it explores is a valid prefix — no wasted work checking arrangements that were already doomed by an earlier position. When `pos` exceeds `N`, every position has a legal value, so that branch contributes exactly one arrangement.

## Complexity

- Time: O(n!) worst case, but pruning cuts off branches as soon as a position has no legal candidate, so the actual number of recursive calls is far smaller in practice.
- Space: O(n) — the `used` vector plus recursion depth up to n.
