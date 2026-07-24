Matching brackets is a last-in-first-out job: the bracket you must close next is always the one you opened most recently. That is exactly what a stack tracks. Push every opening bracket; when a closing bracket arrives, the top of the stack must be its partner — otherwise the string is invalid.

For each opener, push the closer we expect to see next, so verifying a closing bracket is a single comparison against the top. An empty stack on a closer means nothing to match; a non-empty stack at the end means an opener was never closed.

```cpp
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char ch : s) {
            if (ch == '(') st.push(')');
            else if (ch == '[') st.push(']');
            else if (ch == '{') st.push('}');
            else if (st.empty() || st.top() != ch) return false;
            else st.pop();
        }
        return st.empty();
    }
};
```

## Why it works

Pushing the expected closer for each opener turns validation into "does this closing bracket equal the top?", which captures both the correct bracket type and the most-recently-opened ordering at once. A closer against an empty stack is an unmatched close, and a non-empty stack at the end is an unmatched open — both correctly return false.

## Complexity

- Time: O(n) — one pass over the string, O(1) work per character.
- Space: O(n) — the stack can hold up to n expected closers.
