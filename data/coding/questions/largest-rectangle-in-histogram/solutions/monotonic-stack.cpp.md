Keep a stack of bar indices whose heights are strictly increasing. While the stack rises we can't yet tell how far right each bar reaches. The moment a shorter bar arrives, every taller bar on the stack is closed off on the right — pop it and settle its rectangle: its height is the popped bar's height, and its width runs from just after the new stack top up to the current index.

A trailing sentinel of height `0` forces every remaining bar to be popped and measured at the end. Each bar is pushed and popped once, so it is a single linear scan.

```cpp
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int n = (int)heights.size(), best = 0;
        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!st.empty() && heights[st.top()] >= h) {
                int height = heights[st.top()]; st.pop();
                int width = st.empty() ? i : i - st.top() - 1;
                best = max(best, height * width);
            }
            st.push(i);
        }
        return best;
    }
};
```

## Why it works

When bar `i` is shorter than the stack's top, that top bar reaches no further right than `i - 1`, and no further left than the index just above the new top (every bar between is taller). Its maximal rectangle therefore has width `i - top - 1`, or `i` if the stack empties (it extended to the far left). The `0` sentinel drains the stack so every bar is measured exactly once.

## Complexity

- Time: O(n) — each index is pushed and popped at most once.
- Space: O(n) — the stack holds up to n indices.
