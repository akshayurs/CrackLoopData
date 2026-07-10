The instinct is to join the strings with some separator like `#`. That breaks the moment a string *contains* `#`, so the fix is to escape it: before joining, protect every separator (and the escape character itself) with a backslash. On the way back, a backslash means "the next character is literal, not a separator."

This works, but notice the seam it leaves: because the pieces are joined *between* elements, an empty input list and a list holding one empty string both encode to `""`. The length-prefixed approach avoids that ambiguity entirely.

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string encode(vector<string>& strs) {
        string out;
        for (size_t k = 0; k < strs.size(); k++) {
            if (k > 0) out += '#';
            for (char c : strs[k]) {
                if (c == '\\' || c == '#') out += '\\';
                out += c;
            }
        }
        return out;
    }

    vector<string> decode(string s) {
        vector<string> result;
        string buf;
        size_t i = 0;
        while (i < s.size()) {
            char c = s[i];
            if (c == '\\') { buf += s[i + 1]; i += 2; }
            else if (c == '#') { result.push_back(buf); buf.clear(); i += 1; }
            else { buf += c; i += 1; }
        }
        result.push_back(buf);
        return result;
    }
};
```

## Why it works

Escaping guarantees that every unescaped `#` in the encoded string is a real boundary and never part of the data. During decoding, a backslash consumes the character after it verbatim, so an escaped `#` or `\` rejoins the current buffer instead of splitting it. Everything else accumulates until an unescaped `#` flushes the buffer as one recovered string; the trailing buffer after the loop is the final element.

## Complexity

- Time: O(N) where N is the total number of characters across all strings — each character is scanned a constant number of times.
- Space: O(N) — the encoded string and the rebuilt list are proportional to the input.
