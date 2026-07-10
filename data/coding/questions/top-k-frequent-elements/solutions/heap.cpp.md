Sorting every distinct value is wasteful when `k` is small — you only care about the top few. Keep a min-heap of size `k` instead: push each `(count, value)` pair, and whenever the heap grows past `k`, pop the smallest. The heap always holds the `k` most frequent values seen so far, with the cheapest of them at the top ready to be evicted.

This trades the full O(n log n) sort for O(n log k), a clear win when `k` is much smaller than the number of distinct values.

```cpp
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int n : nums) counts[n]++;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> heap;
        for (auto& [value, count] : counts) {
            heap.push({count, value});
            if ((int)heap.size() > k) heap.pop();
        }
        vector<int> result;
        while (!heap.empty()) {
            result.push_back(heap.top().second);
            heap.pop();
        }
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

The min-heap is ordered by count, so its top is always the least frequent value currently retained. After every distinct value has been pushed, anything less frequent than the top `k` has already been popped, leaving precisely the `k` most frequent. With at most `k + 1` elements present, each heap operation costs O(log k). A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log k) — counting is O(n); each of the up-to-n pushes/pops costs O(log k); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the map holds up to n entries; the heap holds k.
