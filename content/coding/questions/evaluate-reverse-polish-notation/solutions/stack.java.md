Postfix notation is built to be read with a stack in one pass. Push every number you see; when you hit an operator, the two operands it needs are exactly the top two values on the stack. Pop them (the second popped is the left operand), apply the operator, and push the result back. After processing all tokens, the single value left on the stack is the answer.

This mirrors how a stack machine actually evaluates expressions, and it visits each token once.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+": stack.push(stack.pop() + stack.pop()); break;
                case "*": stack.push(stack.pop() * stack.pop()); break;
                case "-": { int b = stack.pop(); stack.push(stack.pop() - b); break; }
                case "/": { int b = stack.pop(); stack.push(stack.pop() / b); break; }
                default: stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }
}
```

## Why it works

For any valid postfix expression, the operands of each operator are the most recently produced values still unconsumed — precisely the top of the stack. Addition and multiplication commute, so the pop order does not matter; for subtraction and division the top value is the right operand `b`, so we pop it first and compute `a - b` / `a / b`. Java integer division truncates toward zero, and validity guarantees exactly one value remains at the end.

## Complexity

- Time: O(n) — each token is pushed or triggers a constant-work pop-pop-push once.
- Space: O(n) — the stack holds up to O(n) operands.
