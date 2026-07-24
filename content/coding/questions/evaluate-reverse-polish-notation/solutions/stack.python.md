Postfix notation is built to be read with a stack in one pass. Push every number you see; when you hit an operator, the two operands it needs are exactly the top two values on the stack. Pop them (the second popped is the left operand), apply the operator, and push the result back. After processing all tokens, the single value left on the stack is the answer.

This mirrors how a stack machine actually evaluates expressions, and it visits each token once.

```python
def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(abs(a) // abs(b) * (1 if (a < 0) == (b < 0) else -1))
        else:
            stack.append(int(t))
    return stack[0]
```

## Why it works

For any valid postfix expression, the operands of each operator are the most recently produced values still unconsumed — precisely the top of the stack. Popping `b` then `a` recovers the original left-to-right order (`a op b`), and pushing the result lets it serve as an operand for a later operator. The sign-aware floor division reproduces truncation toward zero, and validity guarantees exactly one value remains at the end.

## Complexity

- Time: O(n) — each token is pushed or triggers a constant-work pop-pop-push once.
- Space: O(n) — the stack holds up to O(n) operands.
