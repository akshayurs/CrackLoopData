Walk the string left to right, parsing one number at a time and remembering the operator that came right before it. Whenever that operator is `*` or `/`, resolve it immediately against the previous number on a stack, so only `+`/`-` terms are ever left waiting. At the end, every value on the stack has the correct sign baked in, so the answer is just their sum.

This avoids building any expression tree or doing a second full pass — one scan builds the stack, and it's already reduced to something you can add up.

```cpp
#include <string>
#include <vector>
#include <cctype>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        vector<int> stack;
        int num = 0;
        char sign = '+';
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            char ch = s[i];
            if (isdigit(ch)) {
                num = num * 10 + (ch - '0');
            }
            bool isLast = i == n - 1;
            if ((ch != ' ' && !isdigit(ch)) || isLast) {
                if (sign == '+') {
                    stack.push_back(num);
                } else if (sign == '-') {
                    stack.push_back(-num);
                } else if (sign == '*') {
                    stack.back() *= num;
                } else if (sign == '/') {
                    stack.back() /= num;
                }
                sign = ch;
                num = 0;
            }
        }
        int total = 0;
        for (int v : stack) total += v;
        return total;
    }
};
```

## Why it works

Every term between two additive operators (`+`/`-`) collapses to a single signed value before it's pushed, because `*` and `/` are resolved against the stack's top the instant they're seen — that top is always the most recently completed term. Digits accumulate into `num`; hitting a non-digit, non-space character (or the end of the string) flushes the pending number using the operator seen before it. Once the scan finishes, the stack holds only signed additive terms, so summing it gives the expression's value. C++'s integer division already truncates toward zero, matching the required rounding.

## Complexity

- Time: O(n) — each character is visited once.
- Space: O(n) — the stack can hold up to n/2 terms in the worst case (all `+`/`-`).
