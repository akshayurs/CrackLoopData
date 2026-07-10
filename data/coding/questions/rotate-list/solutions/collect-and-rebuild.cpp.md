The most literal way to think about rotation is by value, not by pointer surgery. Walk the list once to copy every `val` into a vector, and reduce `k` modulo the length first, since a full rotation is a no-op. The value that ends up at position `i` of the rotated list always came from position `(n - k + i) % n` of the original — that single formula sidesteps any explicit slicing.

Once the mapping is known, build a fresh chain of new nodes in the rotated order.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        vector<int> values;
        ListNode* node = head;
        while (node != nullptr) {
            values.push_back(node->val);
            node = node->next;
        }
        int n = values.size();
        if (n == 0) return nullptr;

        k %= n;
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        for (int i = 0; i < n; i++) {
            int v = values[(n - k + i) % n];
            tail->next = new ListNode(v);
            tail = tail->next;
        }
        return dummy->next;
    }
};
```

## Why it works

Rotating right by `k` moves the last `k` values to the front. Indexing the original vector with `(n - k + i) % n` starts reading from the value that should land first after rotation and wraps around, so as `i` runs from `0` to `n - 1` it produces exactly the rotated order — including the `k == 0` case, where the formula reduces to `i % n`, i.e. no change.

## Complexity

- Time: O(n) — one pass to read values, one pass to rebuild.
- Space: O(n) — the values vector plus n freshly allocated nodes.
