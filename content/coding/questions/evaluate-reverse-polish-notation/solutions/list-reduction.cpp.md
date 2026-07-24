The most direct reading of RPN: an operator always sits right after the two numbers it combines. So repeatedly scan left to right for the first operator, fold the two integers before it into a single result, and rebuild the vector around that result. Each fold shrinks the vector by two entries, and eventually one number remains — the answer.

Restarting the scan from the front after every fold keeps the logic simple at the cost of rescanning, which makes this quadratic; it is a fine way to build intuition before reaching for a stack.

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<string> t(tokens);
        int i = 0;
        while (t.size() > 1) {
            const string& s = t[i];
            if (s == "+" || s == "-" || s == "*" || s == "/") {
                int a = stoi(t[i - 2]), b = stoi(t[i - 1]);
                int r = s == "+" ? a + b : s == "-" ? a - b
                        : s == "*" ? a * b : a / b;
                t.erase(t.begin() + i - 2, t.begin() + i + 1);
                t.insert(t.begin() + i - 2, to_string(r));
                i = 0;
            } else {
                i++;
            }
        }
        return stoi(t[0]);
    }
};
```

## Why it works

A valid RPN expression guarantees that the first operator encountered is preceded by exactly the two operands it applies to. Folding `[a, b, op]` into its numeric result is therefore always safe, and it preserves the postfix structure of everything around it. Repeating until one token is left evaluates the whole expression. C++ integer division truncates toward zero, matching the required semantics.

## Complexity

- Time: O(n²) — up to n/2 folds, and each fold may rescan and shift O(n) tokens.
- Space: O(n) — the working copy of the token vector.
