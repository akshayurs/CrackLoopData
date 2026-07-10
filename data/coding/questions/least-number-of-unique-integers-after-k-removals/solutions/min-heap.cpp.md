The brute-force scan is wasted work: once you know the counts, the removal order never changes — you always want to finish off the value with the smallest remaining count first. A min-heap (`priority_queue` with `greater<int>`) gives you that minimum in O(log u), so seed it with every value's count once, then keep popping and spending removals as long as `k` covers the current minimum.

```cpp
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<int, int> counts;
        for (int num : arr) counts[num]++;

        priority_queue<int, vector<int>, greater<int>> heap;
        for (auto& [key, val] : counts) heap.push(val);

        int unique = heap.size();
        while (!heap.empty() && k >= heap.top()) {
            k -= heap.top();
            heap.pop();
            unique--;
        }
        return unique;
    }
};
```

## Why it works

The heap always exposes the value that is cheapest to eliminate. If `k` is at least that count, removing it entirely is free and strictly reduces the unique count, so it's always safe to take. Once `k` is smaller than the heap's minimum, no remaining value can be fully cleared, so every value still in the heap must survive.

## Complexity

- Time: O(n log n) — building the counts is O(n); building and draining a heap of u values costs O(u log u).
- Space: O(n) — the count map and heap each hold up to n entries.
