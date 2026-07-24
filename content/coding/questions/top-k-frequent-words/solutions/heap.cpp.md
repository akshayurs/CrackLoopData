Sorting every distinct word costs O(n log n) even though only `k` of them are ever returned. A heap lets you pay for just the `k` extractions you need on top of a linear-time build.

Collect the counted pairs into a vector first, then hand that vector to `priority_queue`'s range constructor, which calls `make_heap` internally — a linear-time build rather than `k` individual pushes. The comparator ranks by frequency descending, word ascending.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    vector<string> topKFrequentWords(vector<string>& words, int k) {
        unordered_map<string, int> counts;
        for (auto& w : words) counts[w]++;

        vector<pair<int, string>> items;
        for (auto& [word, count] : counts) items.push_back({count, word});

        auto cmp = [](const pair<int, string>& a, const pair<int, string>& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second;
        };
        priority_queue<pair<int, string>, vector<pair<int, string>>, decltype(cmp)> heap(cmp, items);

        vector<string> result;
        for (int i = 0; i < k; i++) {
            result.push_back(heap.top().second);
            heap.pop();
        }
        return result;
    }
};
```

## Why it works

`priority_queue` treats `cmp(a, b) == true` as "`a` has lower priority than `b`," so the top is always the current best candidate: a higher count outranks a lower one, and equal counts favor the lexicographically smaller word — exactly the required tie-break. Constructing the queue from `items` runs `make_heap` in linear time, so only the `k` pops that follow cost a logarithm each.

## Complexity

- Time: O(n + k log n) — counting and heap construction over the up-to-n distinct words is O(n); each of the k pops costs O(log n).
- Space: O(n) — the map, the vector of pairs, and the heap each hold up to n entries.
