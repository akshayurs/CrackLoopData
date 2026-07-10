The literal reading of the problem: scan the string, delete the first adjacent equal pair you find, then start over — because a removal can create a brand-new pair where the two halves meet. Repeat until a full scan makes no deletion.

Each pass rebuilds the string while skipping any character that matches the one right after it. If a pass changed nothing, the string is stable and we are done.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string removeDuplicates(string s) {
        bool changed = true;
        while (changed) {
            changed = false;
            string result;
            int i = 0;
            int n = (int)s.size();
            while (i < n) {
                if (i + 1 < n && s[i] == s[i + 1]) {
                    i += 2;
                    changed = true;
                } else {
                    result += s[i];
                    i += 1;
                }
            }
            s = result;
        }
        return s;
    }
};
```

## Why it works

Every pass removes at least one adjacent pair whenever one exists, so the string strictly shrinks until it is pair-free. Newly exposed pairs (created when the characters around a deletion become neighbours) are caught by the next pass. The loop only exits when an entire scan finds nothing to delete, which is exactly the "no adjacent duplicates remain" stopping condition.

## Complexity

- Time: O(n^2) — each pass is O(n) and up to O(n) passes may be needed (e.g. a long run collapsing two characters at a time).
- Space: O(n) — the rebuilt string for each pass.
