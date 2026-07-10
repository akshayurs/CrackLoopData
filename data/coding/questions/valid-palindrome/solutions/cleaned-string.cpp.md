The cleanest first attempt mirrors the definition word for word: strip out everything that is not a letter or digit, lowercase what remains, and check whether that reduced string equals its own reverse.

It costs an extra copy of the string, but it is short, obviously correct, and a great baseline to state before optimizing away the extra memory.

```cpp
#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned;
        for (char c : s) {
            if (isalnum((unsigned char)c)) {
                cleaned += (char)tolower((unsigned char)c);
            }
        }
        string reversed(cleaned.rbegin(), cleaned.rend());
        return cleaned == reversed;
    }
};
```

## Why it works

The loop keeps only alphanumeric characters, each folded to lowercase, building exactly the "cleaned form" the problem describes. A string is a palindrome precisely when it matches its reverse, so constructing `reversed` from the reverse iterators and comparing is a direct test of the definition. Casting to `unsigned char` keeps `isalnum` and `tolower` well-defined for every byte.

## Complexity

- Time: O(n) — one pass to build the cleaned text, one comparison over its length.
- Space: O(n) — the cleaned string and its reversed copy both scale with the input.
