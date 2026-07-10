Re-sorting the whole vector every round is overkill — all that's ever needed is the current two largest values, and a heap gives those in O(log n). C++'s `priority_queue` is a max-heap by default, which fits the problem directly.

Pop the two largest stones each round, smash them, and push the remainder back if the stones weren't equal.

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> heap(stones.begin(), stones.end());
        while (heap.size() > 1) {
            int heaviest = heap.top(); heap.pop();
            int second = heap.top(); heap.pop();
            if (heaviest != second) {
                heap.push(heaviest - second);
            }
        }
        return heap.empty() ? 0 : heap.top();
    }
};
```

## Why it works

A `priority_queue<int>` keeps the largest element at `top()`, so two consecutive pops always retrieve the current two heaviest stones in O(log n) each. Pushing the remainder back, only when the stones differ, keeps the heap representing the true multiset of stones after each smash, matching the problem's rules exactly.

## Complexity

- Time: O(n log n) — n insertions to build the heap, then O(1) pop/push per round at O(log n) each.
- Space: O(n) — the heap holds the stones.
