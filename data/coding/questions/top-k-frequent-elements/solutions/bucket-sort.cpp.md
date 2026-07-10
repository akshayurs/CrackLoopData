The key observation: a value can appear at most `n` times, so frequency is a small integer in the range `1..n`. That means you can bucket values by their exact count instead of comparing counts against each other — no sorting needed.

Build a vector of buckets indexed by frequency, drop each value into the bucket matching its count, then walk the buckets from the highest frequency downward, collecting values until you have `k`. Every step is linear, so the whole thing runs in O(n).

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int n : nums) counts[n]++;

        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [value, count] : counts) buckets[count].push_back(value);

        vector<int> result;
        for (int freq = (int)buckets.size() - 1; freq > 0 && (int)result.size() < k; freq--) {
            for (int value : buckets[freq]) {
                result.push_back(value);
                if ((int)result.size() == k) break;
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

`buckets[f]` holds every value that occurs exactly `f` times, and `f` can never exceed `nums.size()`, so the vector is big enough. Scanning from the highest index down visits values in strictly decreasing frequency, so the first `k` collected are the `k` most frequent. Indexing by count replaces comparison-based sorting entirely. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n + k log k) — counting, filling buckets, and scanning are each linear in n; the final ascending sort of the k results costs O(k log k).
- Space: O(n) — the map and the bucket vector together hold O(n) entries.
