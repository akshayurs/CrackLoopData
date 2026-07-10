A parenthesized group is just a smaller expression whose value slots into the outer one, so let recursion mirror that structure. Scan left to right keeping a running `result`, a pending `num`, and the `sign` (`+1`/`-1`) that applies to the next number. On `+` or `-` you finalize the pending number into `result` and set the sign for what comes next.

When you hit `(`, recurse to evaluate the inner expression and treat its return value as the next `num`; when you hit `)`, fold the pending number in and return. A shared index tells the caller where the inner group ended so scanning resumes past the matching `)`.

```python
def calculate(s):
    def parse(i):
        result, num, sign = 0, 0, 1
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
                i += 1
            elif ch == '(':
                num, i = parse(i + 1)
            elif ch == ')':
                return result + sign * num, i + 1
            else:
                if ch != ' ':
                    result += sign * num
                    num = 0
                    sign = 1 if ch == '+' else -1
                i += 1
        return result + sign * num, i
    return parse(0)[0]
```

## Why it works

`result` accumulates every completed term, while `num` and `sign` hold the term currently being read. An operator commits the pending term with its sign, then arms the sign for the next one. A `(` defers to a recursive call that returns both the group's value and the index just past its `)`, so the value behaves exactly like a literal number and scanning continues seamlessly. Unary minus falls out for free: a leading `-` simply flips `sign` while `num` is still `0`.

## Complexity

- Time: O(n) — each character is examined once across all recursive frames.
- Space: O(n) — recursion depth equals the maximum parenthesis nesting.
