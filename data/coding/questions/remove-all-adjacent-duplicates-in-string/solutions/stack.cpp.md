A stack captures the "collide with the previous survivor" behaviour perfectly. Walk the string once; the stack always holds the result-so-far. For each character, if it equals the character on top of the stack, they annihilate — pop the top and drop the current one. Otherwise push the current character.

The result `string` itself doubles as the stack: its back is the top, so we either pop the back or push the new character. This handles the cascade automatically without any restart.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string removeDuplicates(string s) {
        string stack;
        for (char ch : s) {
            if (!stack.empty() && stack.back() == ch) {
                stack.pop_back();
            } else {
                stack.push_back(ch);
            }
        }
        return stack;
    }
};
```

## Why it works

The result string is an invariant: it is exactly the fully-reduced string of everything processed so far. When a new character matches the back, that pair is adjacent in the reduced string and must cancel, so we pop it. When it does not match, it safely extends the reduced string. Because a pop re-exposes the earlier character as the new back, chains like `"aaaa"` collapse in the same single pass. What remains is the unique pair-free result.

## Complexity

- Time: O(n) — each character is pushed and popped at most once.
- Space: O(n) — the string in the worst case (no removals) holds the whole input.
