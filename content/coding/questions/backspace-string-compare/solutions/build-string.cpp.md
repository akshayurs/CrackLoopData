The most literal reading: actually type each string out. Walk left to right pushing letters onto a `string` used as a stack, and whenever a `#` appears, pop the last letter (if any). Whatever remains is the final text.

Do this for both strings and compare the results directly. It is the honest baseline you would describe first before worrying about extra space.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return build(s) == build(t);
    }

private:
    string build(const string& str) {
        string out;
        for (char ch : str) {
            if (ch == '#') {
                if (!out.empty()) out.pop_back();
            } else {
                out.push_back(ch);
            }
        }
        return out;
    }
};
```

## Why it works

The output string mirrors the editor exactly: typing a letter appends it, and a backspace removes the most recent letter — which is always the last character. Guarding `pop_back` with an emptiness check handles a backspace on empty text as a no-op. Two strings are equal after editing iff their reconstructed contents match character for character.

## Complexity

- Time: O(m + n) — each character of both strings is processed once.
- Space: O(m + n) — the two rebuilt strings are stored explicitly.
