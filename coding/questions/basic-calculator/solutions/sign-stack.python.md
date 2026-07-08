Recursion is really just an explicit stack in disguise, so replace it with one and make a single left-to-right pass. Keep a running `result`, the number being built (`num`), and the current `sign`. Whenever you meet `+` or `-`, add `sign * num` into `result` and reset for the next term.

The only tricky part is parentheses. When you reach `(`, remember the outer context by pushing the accumulated `result` and the sign that applies to the whole group; then reset and start the group fresh. When you reach `)`, close the current group into `result`, multiply by the group's sign, and add back the saved outer `result`. Because the sign is captured once per group, nesting resolves correctly.

```python
def calculate(s):
    stack = []
    result = 0
    num = 0
    sign = 1
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '+':
            result += sign * num
            num, sign = 0, 1
        elif ch == '-':
            result += sign * num
            num, sign = 0, -1
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result, sign = 0, 1
        elif ch == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    return result + sign * num
```

## Why it works

At any moment `result` is the value of the expression seen so far in the current group, and `sign` is the pending sign for the next number. Pushing `result` then `sign` at `(` freezes the outer computation; the group evaluates against a fresh zero. At `)` the group's value is finalized, scaled by its sign (popped first), and merged into the restored outer `result` (popped second). Spaces are ignored implicitly since they match no branch.

## Complexity

- Time: O(n) — one pass; each character does O(1) work.
- Space: O(n) — the stack grows with parenthesis nesting depth.
