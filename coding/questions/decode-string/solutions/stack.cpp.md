Rescanning the string on every expansion is wasteful. A single left-to-right pass with two stacks avoids it entirely: one stack holds the pending repeat counts, the other holds the partially built string from each enclosing bracket level.

Walk the characters once. Digits accumulate into the current count. On `[`, push the count and the string built so far, then start fresh for the new group. On `]`, pop the count and the outer string, and fold the just-finished group into it. Anything else is a plain letter appended to the current string.

```cpp
#include <string>
#include <stack>
#include <cctype>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<int> counts;
        stack<string> outer;
        string current;
        int num = 0;
        for (char ch : s) {
            if (isdigit((unsigned char)ch)) {
                num = num * 10 + (ch - '0');
            } else if (ch == '[') {
                counts.push(num);
                outer.push(current);
                current.clear();
                num = 0;
            } else if (ch == ']') {
                int k = counts.top(); counts.pop();
                string built = current;
                current = outer.top(); outer.pop();
                for (int r = 0; r < k; r++) current += built;
            } else {
                current += ch;
            }
        }
        return current;
    }
};
```

## Why it works

Each `[` opens a new scope: the count and the text accumulated so far in the parent scope are saved on their stacks, and `current` restarts empty for the nested content. Each `]` closes the innermost open scope — the one that must be complete, since brackets are balanced — by repeating `current` its stored count of times and reattaching it to the parent's saved text. By the time the loop ends, every scope has closed exactly once and `current` holds the fully decoded string.

## Complexity

- Time: O(n) — every character is processed once, and each stack push/pop is O(1).
- Space: O(n) — the stacks and the output can each hold up to the decoded string's length.
