Sorting every point is wasteful when `k` is small — you only need to know the `k` smallest distances, not the full order of `n` of them. A max-heap capped at size `k` does exactly that: push points in, and whenever the heap grows past `k`, pop the farthest one out.

`std::priority_queue` is a max-heap by default, which is exactly the shape needed here: the point on top is always the current farthest among the `k` kept so far.

```cpp
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto dist = [](const vector<int>& p) {
            return (long)p[0] * p[0] + (long)p[1] * p[1];
        };
        auto cmp = [&](const vector<int>& a, const vector<int>& b) {
            return dist(a) < dist(b);
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> heap(cmp);

        for (auto& p : points) {
            heap.push(p);
            if ((int)heap.size() > k) {
                heap.pop();
            }
        }

        vector<vector<int>> result;
        while (!heap.empty()) {
            result.push_back(heap.top());
            heap.pop();
        }
        sort(result.begin(), result.end(), [&](const vector<int>& a, const vector<int>& b) {
            long da = dist(a), db = dist(b);
            if (da != db) return da < db;
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
        return result;
    }
};
```

## Why it works

The heap always holds at most `k` points, with the farthest one on top. Pushing a new point and popping whenever the size exceeds `k` always removes the true farthest among the `k + 1` candidates, so a closer point is never mistakenly discarded. After every point is processed, the heap contains exactly the `k` nearest; the trailing sort applies the required deterministic ordering.

## Complexity

- Time: O(n log k) — each push/pop costs O(log k), plus O(k log k) for the final sort.
- Space: O(k) — the heap never holds more than k points.
