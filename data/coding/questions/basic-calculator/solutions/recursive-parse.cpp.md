A parenthesized group is just a smaller expression whose value slots into the outer one, so let recursion mirror that structure. Scan left to right keeping a running `result`, a pending `num`, and the `sign` (`+1`/`-1`) that applies to the next number. On `+` or `-` you finalize the pending number into `result` and set the sign for what comes next.

When you hit `(`, recurse to evaluate the inner expression and treat its return value as the next `num`; when you hit `)`, fold the pending number in and return. A shared cursor member `pos` tells every frame where scanning currently sits, so it resumes past the matching `)`.

```cpp
#include <string>
using namespace std;

class Solution {
    int pos = 0;

    int parse(const string& s) {
        long result = 0, num = 0, sign = 1;
        while (pos < (int)s.size()) {
            char ch = s[pos];
            if (ch >= '0' && ch <= '9') {
                num = num * 10 + (ch - '0');
                pos++;
            } else if (ch == '(') {
                pos++;
                num = parse(s);
            } else if (ch == ')') {
                pos++;
                return (int)(result + sign * num);
            } else {
                if (ch != ' ') {
                    result += sign * num;
                    num = 0;
                    sign = ch == '+' ? 1 : -1;
                }
                pos++;
            }
        }
        return (int)(result + sign * num);
    }

public:
    int calculate(string s) {
        pos = 0;
        return parse(s);
    }
};
```

## Why it works

`result` accumulates every completed term, while `num` and `sign` hold the term currently being read. An operator commits the pending term with its sign, then arms the sign for the next one. A `(` recurses; the inner call consumes through its own `)` (advancing the shared `pos`) and returns its value, which behaves exactly like a literal number. Unary minus falls out for free: a leading `-` simply flips `sign` while `num` is still `0`.

## Complexity

- Time: O(n) — each character is examined once across all recursive frames.
- Space: O(n) — recursion depth equals the maximum parenthesis nesting.
