Postfix notation is built to be read with a stack in one pass. Push every number you see; when you hit an operator, the two operands it needs are exactly the top two values on the stack. Pop them (the second popped is the left operand), apply the operator, and push the result back. After processing all tokens, the single value left on the stack is the answer.

This mirrors how a stack machine actually evaluates expressions, and it visits each token once.

```javascript
function evalRPN(tokens) {
  const stack = [];
  for (const t of tokens) {
    if (t === "+" || t === "-" || t === "*" || t === "/") {
      const b = stack.pop();
      const a = stack.pop();
      if (t === "+") stack.push(a + b);
      else if (t === "-") stack.push(a - b);
      else if (t === "*") stack.push(a * b);
      else stack.push(Math.trunc(a / b));
    } else {
      stack.push(Number(t));
    }
  }
  return stack[0];
}
```

## Why it works

For any valid postfix expression, the operands of each operator are the most recently produced values still unconsumed — precisely the top of the stack. Popping `b` then `a` recovers the original left-to-right order (`a op b`), and pushing the result lets it serve as an operand for a later operator. `Math.trunc` reproduces division that truncates toward zero, and validity guarantees exactly one value remains at the end.

## Complexity

- Time: O(n) — each token is pushed or triggers a constant-work pop-pop-push once.
- Space: O(n) — the stack holds up to O(n) operands.
