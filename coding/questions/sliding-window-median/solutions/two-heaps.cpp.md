Re-sorting the whole window every step throws away almost all of the previous work. Instead, keep the window split across two heaps: a max-heap `small` holding the lower half and a min-heap `large` holding the upper half, kept balanced in size so the median always sits at one (or both) of their tops.

The wrinkle is deletion — `priority_queue` doesn't support "remove this arbitrary value" efficiently. The trick is lazy deletion: when a number slides out of the window, record that it owes a removal in a `delayed` map, and only actually pop it once it would otherwise surface at the top. Sizes are still tracked exactly, so balancing and the median calculation stay correct even while stale values linger deeper in a heap. A small `DualHeap` helper keeps this state self-contained per call.

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

class DualHeap {
public:
    explicit DualHeap(int k) : k(k) {}

    void insert(int num) {
        if (small.empty() || num <= small.top()) { small.push(num); smallSize++; }
        else { large.push(num); largeSize++; }
        balance();
    }

    void erase(int num) {
        delayed[num]++;
        if (num <= small.top()) { smallSize--; if (num == small.top()) prune(small); }
        else { largeSize--; if (num == large.top()) prune(large); }
        balance();
    }

    double getMedian() {
        if (k % 2 == 1) return small.top();
        return ((long long)small.top() + large.top()) / 2.0;
    }

private:
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<int>> large;
    unordered_map<int, int> delayed;
    int k, smallSize = 0, largeSize = 0;

    template <typename Heap>
    void prune(Heap& heap) {
        while (!heap.empty() && delayed.count(heap.top()) && delayed[heap.top()] > 0) {
            if (--delayed[heap.top()] == 0) delayed.erase(heap.top());
            heap.pop();
        }
    }

    void balance() {
        if (smallSize > largeSize + 1) { large.push(small.top()); small.pop(); smallSize--; largeSize++; prune(small); }
        else if (smallSize < largeSize) { small.push(large.top()); large.pop(); largeSize--; smallSize++; prune(large); }
    }
};

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        DualHeap dh(k);
        vector<double> result;
        for (int i = 0; i < (int)nums.size(); i++) {
            dh.insert(nums[i]);
            if (i >= k) dh.erase(nums[i - k]);
            if (i >= k - 1) result.push_back(dh.getMedian());
        }
        return result;
    }
};
```

## Why it works

`small` and `large` are kept the same size (or `small` one larger), so the median is always `small`'s top for odd `k`, or the average of both tops for even `k`. Lazy deletion keeps the heaps' logical sizes accurate — `smallSize`/`largeSize` reflect reality even before a stale entry is physically popped — so every balance and median read uses correct counts, and pruning only touches values that have actually become garbage.

## Complexity

- Time: O(n log k) — each insert, erase, and balance touches a heap of size O(k), and each element causes O(1) amortized heap operations overall.
- Space: O(k) — the two heaps together hold the current window (plus bounded stale entries awaiting cleanup).
