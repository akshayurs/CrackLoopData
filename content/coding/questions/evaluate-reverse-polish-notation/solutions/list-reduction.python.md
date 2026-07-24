The most direct reading of RPN: an operator always sits right after the two numbers it combines. So repeatedly scan left to right for the first operator, fold the two integers before it into a single result, and splice that result back into the list. Each fold shrinks the list by two entries, and eventually one number remains — the answer.

Restarting the scan from the front after every fold keeps the logic simple at the cost of rescanning, which makes this quadratic; it is a fine way to build intuition before reaching for a stack.

```python
def eval_rpn(tokens):
    ops = {"+", "-", "*", "/"}
    tokens = list(tokens)
    i = 0
    while len(tokens) > 1:
        if tokens[i] in ops:
            a, b = int(tokens[i - 2]), int(tokens[i - 1])
            if tokens[i] == "+":
                r = a + b
            elif tokens[i] == "-":
                r = a - b
            elif tokens[i] == "*":
                r = a * b
            else:
                r = abs(a) // abs(b) * (1 if (a < 0) == (b < 0) else -1)
            tokens[i - 2:i + 1] = [str(r)]
            i = 0
        else:
            i += 1
    return int(tokens[0])
```

## Why it works

A valid RPN expression guarantees that the first operator encountered is preceded by exactly the two operands it applies to. Folding `[a, b, op]` into its numeric result is therefore always safe, and it preserves the postfix structure of everything around it. Repeating until one token is left evaluates the whole expression. The sign-aware floor division reproduces truncation toward zero.

## Complexity

- Time: O(n²) — up to n/2 folds, and each fold may rescan and splice O(n) tokens.
- Space: O(n) — the working copy of the token list.
