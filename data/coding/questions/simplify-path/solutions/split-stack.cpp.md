The path is a sequence of components separated by slashes, so split on `/` and process each component in order. A vector used as a stack mirrors the directory hierarchy: pushing a real name descends into it, and hitting `..` pops the most recent name to climb back to the parent.

Empty strings (from `//` or a trailing slash) and `.` carry no meaning, so skip them. When `..` appears with an empty stack you are already at the root and simply stay there. Joining what remains with single slashes yields the canonical path.

```cpp
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        stringstream ss(path);
        string part;
        while (getline(ss, part, '/')) {
            if (part.empty() || part == ".") continue;
            if (part == "..") {
                if (!stack.empty()) stack.pop_back();
            } else {
                stack.push_back(part);
            }
        }
        string result;
        for (const string& dir : stack) result += "/" + dir;
        return result.empty() ? "/" : result;
    }
};
```

## Why it works

`getline` with a `/` delimiter yields each component; the vector holds the surviving names in order. A normal name is pushed; `..` removes the deepest name it can find, exactly matching "go to parent"; `.` and empty tokens are noise and dropped. Because `..` on an empty stack is ignored, the result can never rise above root. Rebuilding with a leading `/` before each name reconstructs the absolute path, and an empty stack degrades to just `"/"`.

## Complexity

- Time: O(n) — one split plus one pass over the components.
- Space: O(n) — the vector holds up to n characters.
