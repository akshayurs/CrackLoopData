The most direct reading of RPN: an operator always sits right after the two numbers it combines. So repeatedly scan left to right for the first operator, fold the two integers before it into a single result, and splice that result back into the array. Each fold shrinks the array by two entries, and eventually one number remains — the answer.

Restarting the scan from the front after every fold keeps the logic simple at the cost of rescanning, which makes this quadratic; it is a fine way to build intuition before reaching for a stack.

```javascript
function evalRPN(tokens) {
  const ops = new Set(["+", "-", "*", "/"]);
  tokens = tokens.slice();
  let i = 0;
  while (tokens.length > 1) {
    if (ops.has(tokens[i])) {
      const a = Number(tokens[i - 2]);
      const b = Number(tokens[i - 1]);
      let r;
      if (tokens[i] === "+") r = a + b;
      else if (tokens[i] === "-") r = a - b;
      else if (tokens[i] === "*") r = a * b;
      else r = Math.trunc(a / b);
      tokens.splice(i - 2, 3, String(r));
      i = 0;
    } else {
      i++;
    }
  }
  return Number(tokens[0]);
}
```

## Why it works

A valid RPN expression guarantees that the first operator encountered is preceded by exactly the two operands it applies to. Folding `[a, b, op]` into its numeric result is therefore always safe, and it preserves the postfix structure of everything around it. Repeating until one token is left evaluates the whole expression. `Math.trunc` reproduces division that truncates toward zero.

## Complexity

- Time: O(n²) — up to n/2 folds, and each fold may rescan and splice O(n) tokens.
- Space: O(n) — the working copy of the token array.
