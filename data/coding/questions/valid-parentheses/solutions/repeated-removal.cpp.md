The most literal reading of "balanced": keep deleting any adjacent matched pair — `()`, `[]`, or `{}` — from the string. If the string collapses down to empty, every bracket found a partner right next to it eventually; if something is left over, it never matched.

This is wasteful (each deletion rescans the string) but it mirrors how you'd explain the rule out loud before reaching for a stack.

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        vector<string> pairs = {"()", "[]", "{}"};
        bool changed = true;
        while (changed) {
            changed = false;
            for (const string& pair : pairs) {
                size_t pos = s.find(pair);
                if (pos != string::npos) {
                    s.erase(pos, pair.size());
                    changed = true;
                }
            }
        }
        return s.empty();
    }
};
```

## Why it works

Any balanced string can be fully reduced to empty by repeatedly deleting an innermost matched pair — that pair is exactly an adjacent `()`, `[]`, or `{}` somewhere in the string. Each successful deletion shrinks `s`, so the loop terminates; if no adjacent pair remains but `s` is non-empty, the brackets could never have been balanced.

## Complexity

- Time: O(n²) — up to n/2 deletions, each an O(n) find-and-erase.
- Space: O(1) — the string is edited in place, no auxiliary structure.
