Start with the obvious plan: count how many times each value appears, then rank the distinct values by that count. An `unordered_map` builds the counts in one pass, and sorting the distinct values by their frequency puts the most common ones at the front.

Once sorted, the answer is just the first `k` values. The counting is linear, but the sort of the distinct values is what dominates the running time.

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int n : nums) counts[n]++;
        vector<int> ordered;
        for (auto& [value, count] : counts) ordered.push_back(value);
        sort(ordered.begin(), ordered.end(),
             [&](int a, int b) { return counts[a] > counts[b]; });
        vector<int> result(ordered.begin(), ordered.begin() + k);
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

`counts` maps each value to its number of occurrences. Sorting the distinct values by `counts[value]` in descending order lines them up from most to least frequent, so taking the first `k` gives exactly the `k` most common values. Because the answer is guaranteed unique, there is no tie to break at the boundary. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct values costs O(n log n); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the map and the value list each hold up to n entries.
