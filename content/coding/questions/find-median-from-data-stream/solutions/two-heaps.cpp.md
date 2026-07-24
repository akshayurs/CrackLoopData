Split the numbers into two halves around the median: a max-heap `lo` holding the smaller half, and a min-heap `hi` holding the larger half, kept the same size (or `lo` one larger). The median then always sits at the top of one or both heaps — no sorting needed.

`priority_queue` is a max-heap by default, so `hi` is built with `greater<int>` to act as a min-heap. On every `addNum`, push into one heap and rebalance by moving the top of one to the other so the size invariant holds.

```cpp
#include <queue>
#include <vector>
using namespace std;

class MedianFinder {
public:
    MedianFinder() {}

    void addNum(int num) {
        lo.push(num);
        hi.push(lo.top());
        lo.pop();
        if (hi.size() > lo.size()) {
            lo.push(hi.top());
            hi.pop();
        }
    }

    double findMedian() {
        if (lo.size() > hi.size()) return lo.top();
        return (lo.top() + hi.top()) / 2.0;
    }

private:
    priority_queue<int> lo;                                   // max-heap, smaller half
    priority_queue<int, vector<int>, greater<int>> hi;         // min-heap, larger half
};
```

## Why it works

Every value first goes into `lo`, then its largest member is immediately promoted to `hi` — this guarantees every element of `lo` is `<=` every element of `hi`. Rebalancing keeps the sizes equal or `lo` exactly one larger, so the median is either `lo`'s top (odd total) or the average of both tops (even total).

## Complexity

- Time: O(log n) per `addNum` (heap push/pop); O(1) per `findMedian`.
- Space: O(n) — the two heaps together hold every number added.
