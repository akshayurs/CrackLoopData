Postfix notation is built to be read with a stack in one pass. Push every number you see; when you hit an operator, the two operands it needs are exactly the top two values on the stack. Pop them (the second popped is the left operand), apply the operator, and push the result back. After processing all tokens, the single value left on the stack is the answer.

This mirrors how a stack machine actually evaluates expressions, and it visits each token once.

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        for (const string& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                int b = stack.back(); stack.pop_back();
                int a = stack.back(); stack.pop_back();
                if (t == "+") stack.push_back(a + b);
                else if (t == "-") stack.push_back(a - b);
                else if (t == "*") stack.push_back(a * b);
                else stack.push_back(a / b);
            } else {
                stack.push_back(stoi(t));
            }
        }
        return stack.back();
    }
};
```

## Why it works

For any valid postfix expression, the operands of each operator are the most recently produced values still unconsumed — precisely the top of the stack. Popping `b` then `a` recovers the original left-to-right order (`a op b`), and pushing the result lets it serve as an operand for a later operator. C++ integer division truncates toward zero, matching the required semantics, and validity guarantees exactly one value remains at the end.

## Complexity

- Time: O(n) — each token is pushed or triggers a constant-work pop-pop-push once.
- Space: O(n) — the stack holds up to O(n) operands.
