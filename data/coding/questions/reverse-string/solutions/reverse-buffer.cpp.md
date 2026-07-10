The most literal approach: read the input from the last character to the first and append each one to a fresh buffer. Whatever was at the end lands at the front of the new string, which is exactly reversal.

It is the honest baseline — no pointer bookkeeping, just walk backwards and collect. The cost is a second string the size of the input.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string reverseString(string s) {
        string result;
        result.reserve(s.size());
        for (int i = (int)s.size() - 1; i >= 0; i--) {
            result.push_back(s[i]);
        }
        return result;
    }
};
```

## Why it works

Iterating with the index going from `s.size() - 1` down to `0` visits characters in reverse order, and `push_back` preserves that order in `result`. The finished buffer is the input read back-to-front.

## Complexity

- Time: O(n) — one pass over every character.
- Space: O(n) — a separate buffer holds all n characters.
