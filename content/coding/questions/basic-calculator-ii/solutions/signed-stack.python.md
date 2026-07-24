Walk the string left to right, parsing one number at a time and remembering the operator that came right before it. Whenever that operator is `*` or `/`, resolve it immediately against the previous number on a stack, so only `+`/`-` terms are ever left waiting. At the end, every value on the stack has the correct sign baked in, so the answer is just their sum.

This avoids building any expression tree or doing a second full pass — one scan builds the stack, and it's already reduced to something you can add up.

```python
def calculate(s):
    stack = []
    num = 0
    sign = "+"
    n = len(s)
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        is_last = i == n - 1
        if (not ch.isdigit() and ch != " ") or is_last:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                prev = stack.pop()
                stack.append(int(prev / num))
            sign = ch
            num = 0
    return sum(stack)
```

## Why it works

Every term between two additive operators (`+`/`-`) collapses to a single signed value before it's pushed, because `*` and `/` are resolved against the stack's top the instant they're seen — that top is always the most recently completed term. Spaces and digits just accumulate `num`; anything else (including reaching the end of the string) flushes the pending number using the operator that preceded it. Once the scan finishes, the stack holds only signed additive terms, so summing it gives the expression's value.

## Complexity

- Time: O(n) — each character is visited once.
- Space: O(n) — the stack can hold up to n/2 terms in the worst case (all `+`/`-`).
