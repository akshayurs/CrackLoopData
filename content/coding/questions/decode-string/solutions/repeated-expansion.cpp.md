The most literal reading of the rule: keep expanding the innermost `k[...]` group until no brackets remain. An innermost group is a `]` whose matching `[` has no other `[` between them, so its contents are pure letters and can be repeated immediately.

Each pass scans for the first `]`, walks back to its `[`, reads the digits before that `[`, and splices in the repeated text. Repeat until the string is bracket-free. It is the honest baseline you would describe before reaching for a stack.

```cpp
#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        size_t close;
        while ((close = s.find(']')) != string::npos) {
            size_t open = s.rfind('[', close);
            string inner = s.substr(open + 1, close - open - 1);
            size_t j = open;
            while (j > 0 && isdigit((unsigned char)s[j - 1])) j--;
            int k = stoi(s.substr(j, open - j));
            string repeated;
            for (int r = 0; r < k; r++) repeated += inner;
            s = s.substr(0, j) + repeated + s.substr(close + 1);
        }
        return s;
    }
};
```

## Why it works

The first `]` in the string always closes an innermost group, and the nearest `[` to its left is its partner, so the text between them contains only letters. Reading the run of digits just before that `[` gives the repeat count `k`. Replacing the whole `k[inner]` span with `inner` repeated `k` times removes exactly one bracket pair while preserving every character outside it. Since each pass eliminates one pair, the loop terminates with a fully decoded string.

## Complexity

- Time: O(m · n) — one pass per bracket pair (m pairs), each rescanning a string up to the final length n.
- Space: O(n) — new strings built during expansion.
