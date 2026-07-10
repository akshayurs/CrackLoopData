The brute force wastes time re-checking affordability from scratch every round. Instead, sort projects by `capital` once and push them, in that order, into a max-heap ordered by profit as they become affordable. The top of that heap is always the best project money can currently buy.

Once a project moves into the profit max-heap it never needs to be revisited — it either gets picked immediately or waits at the top until it's the best choice, with no re-checking of a "used" list required.

```cpp
#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    long long maxCapital(int k, long long w, vector<int>& profit, vector<int>& capital) {
        int n = profit.size();
        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) {
            return capital[a] < capital[b];
        });

        priority_queue<int> affordable;
        long long money = w;
        int pos = 0;

        for (int round = 0; round < k; round++) {
            while (pos < n && capital[order[pos]] <= money) {
                affordable.push(profit[order[pos]]);
                pos++;
            }
            if (affordable.empty()) break;
            money += affordable.top();
            affordable.pop();
        }

        return money;
    }
};
```

## Why it works

Sorting by capital lets each project be "unlocked" exactly once, in order, as `money` grows — no project is ever re-examined after it enters the profit max-heap. Within a round, taking the globally best-profit affordable project is safe: money is monotonically non-decreasing, so any project affordable now stays affordable later, meaning deferring a cheap high-profit pick can never help and greedily taking the max is optimal for that round.

## Complexity

- Time: O(n log n + k log n) — sorting once, then each of the n pushes and up to k pops costs O(log n).
- Space: O(n) — the capital ordering and the profit heap.
