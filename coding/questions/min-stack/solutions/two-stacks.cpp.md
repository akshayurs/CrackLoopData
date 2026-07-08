The insight is that the minimum only ever changes at push and pop boundaries, so you can precompute it. Alongside the main stack, keep a second "min stack" whose back always holds the minimum of everything below and including the current top of the main stack. When you push `val`, push `min(val, previousMin)` onto the min stack; when you pop, pop both in lockstep.

Now `getMin` is just reading the back of the min stack — no scan. Because the two stacks grow and shrink together, the min stack's back is always in sync with the current contents, which turns the linear query into a constant-time lookup.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class MinStack {
public:
    void push(int val) {
        data.push_back(val);
        int curMin = mins.empty() ? val : min(val, mins.back());
        mins.push_back(curMin);
    }
    void pop() {
        data.pop_back();
        mins.pop_back();
    }
    int top() {
        return data.back();
    }
    int getMin() {
        return mins.back();
    }
private:
    vector<int> data;
    vector<int> mins;
};
```

## Why it works

The back of `mins` is invariant: it equals the minimum of every value currently on the main stack. On push, the new minimum is either the new value or the old minimum, so `min(val, mins.back())` maintains it. On pop, removing the back of both vectors restores the exact state that existed one push earlier — including the correct minimum. Duplicate minimums are handled naturally: each push records its own min entry, so popping one copy leaves the other's entry intact.

## Complexity

- Time: O(1) for every operation, including `getMin`.
- Space: O(n) — the auxiliary min stack mirrors the main stack's size.
