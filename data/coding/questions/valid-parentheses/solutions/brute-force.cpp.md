A valid string always contains at least one *innermost* pair — two adjacent matching brackets like `()`, `[]`, or `{}` with nothing between them. Removing such a pair leaves a string that is valid exactly when the original was. So repeatedly strip out every adjacent matched pair; if the string collapses to empty, it was balanced.

This is the naive approach: it keeps rescanning and shrinking the string until no more pairs can be removed. Anything left over is an unmatched or mis-ordered bracket.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        auto stripAll = [](string& str, const string& pair) {
            size_t pos;
            while ((pos = str.find(pair)) != string::npos)
                str.erase(pos, 2);
        };
        size_t prevLen = string::npos;
        while (prevLen != s.size()) {
            prevLen = s.size();
            stripAll(s, "()");
            stripAll(s, "[]");
            stripAll(s, "{}");
        }
        return s.empty();
    }
};
```

## Why it works

Erasing an innermost pair never breaks the balance of the surrounding brackets — the neighbours that were separated by it become adjacent and can match on a later pass. Each outer pass removes at least one pair, so the length strictly shrinks until it stabilizes. A truly balanced string reduces all the way to empty; any leftover character is a bracket that could never find its partner.

## Complexity

- Time: O(n^2) — repeatedly scanning and erasing pairs across the string.
- Space: O(n) — the working string holds up to n characters.
