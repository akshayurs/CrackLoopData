Splitting first builds an intermediate list of every component. You can skip that allocation by scanning the string once, accumulating characters into a token and finalizing it each time you hit a slash. Appending a sentinel `/` to the input flushes the last token without a special case.

The stack logic is identical to the split version — the only change is that tokens are produced on the fly instead of up front, which keeps peak extra memory to the vector alone.

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        string token;
        path += '/';
        for (char ch : path) {
            if (ch == '/') {
                if (token.empty() || token == ".") {
                    // nothing to do
                } else if (token == "..") {
                    if (!stack.empty()) stack.pop_back();
                } else {
                    stack.push_back(token);
                }
                token.clear();
            } else {
                token += ch;
            }
        }
        string result;
        for (const string& dir : stack) result += "/" + dir;
        return result.empty() ? "/" : result;
    }
};
```

## Why it works

Each character is either part of a name or a boundary. On a boundary the completed token is classified: empty and `.` are dropped, `..` pops the parent when one exists, anything else is a real directory that gets pushed. The appended sentinel slash guarantees the final segment is processed. Ignoring `..` on an empty stack prevents rising above root, and rebuilding under a leading `/` yields the canonical path.

## Complexity

- Time: O(n) — every character is visited once.
- Space: O(n) — the vector holds up to n characters; no split array is built.
