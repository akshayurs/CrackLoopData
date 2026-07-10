Start with the simplest thing that works: keep the values in one `vector` used as a stack. Push, pop, and top are trivial operations on the back of the vector. The only interesting method is `getMin`, and the naive answer is to walk everything currently stored and take the smallest.

This is easy to reason about and obviously correct, but it pays for that simplicity on every `getMin` call — scanning the whole stack means the minimum query is linear, not constant.

```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class MinStack {
public:
    void push(int val) {
        data.push_back(val);
    }
    void pop() {
        data.pop_back();
    }
    int top() {
        return data.back();
    }
    int getMin() {
        int m = INT_MAX;
        for (int v : data) m = min(m, v);
        return m;
    }
private:
    vector<int> data;
};
```

## Why it works

A `vector` used as a stack gives O(1) `push_back`, `pop_back`, and `back`, so the LIFO behaviour is exactly right. `getMin` iterates over every element still on the stack, keeping the smallest seen — by definition the current minimum. Nothing extra is tracked, so there is no bookkeeping to get wrong.

## Complexity

- Time: O(1) for `push`, `pop`, `top`; O(n) for `getMin` — it inspects every element.
- Space: O(n) — the single stack holds all pushed values.
