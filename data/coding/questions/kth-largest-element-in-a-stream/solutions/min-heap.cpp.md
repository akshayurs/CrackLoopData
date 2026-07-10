You never need the full sorted history — only the k largest values matter, and among those only the smallest one (the k-th largest overall). Keep a min-heap capped at size k: whenever it grows past k, pop the smallest, since anything smaller than the current k-th largest can never become the answer again.

`priority_queue` is a max-heap by default, so it is instantiated with `greater<int>` to flip it into a min-heap. After seeding it with the initial array (trimmed to its k largest), every `add` is a single push, and possibly one pop, followed by peeking at the heap's root.

```cpp
#include <vector>
#include <queue>
using namespace std;

class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        for (int n : nums) {
            heap.push(n);
            if ((int)heap.size() > k) heap.pop();
        }
    }

    int add(int val) {
        heap.push(val);
        if ((int)heap.size() > k) heap.pop();
        return heap.top();
    }

private:
    int k;
    priority_queue<int, vector<int>, greater<int>> heap;
};
```

## Why it works

A min-heap of size k always holds exactly the k largest values seen so far, with the smallest of that group at the root. Pushing a new value and evicting the root when the heap overflows keeps that invariant intact, so the root is always the k-th largest element after every `add`.

## Complexity

- Time: O(log k) per call to `add` — one push and at most one pop on a heap of size k.
- Space: O(k) — the heap only ever holds the k largest values.
