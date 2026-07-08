Splitting first builds an intermediate list of every component. You can skip that allocation by scanning the string once, accumulating characters into a token and finalizing it each time you hit a slash. Appending a sentinel `/` at the end flushes the last token without a special case.

The stack logic is identical to the split version — the only change is that tokens are produced on the fly instead of up front, which keeps peak extra memory to the stack alone.

```python
def simplify_path(path):
    stack = []
    token = []
    for ch in path + '/':
        if ch == '/':
            part = ''.join(token)
            token = []
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        else:
            token.append(ch)
    return '/' + '/'.join(stack)
```

## Why it works

Each character is either part of a name or a boundary. On a boundary the completed token is classified: empty and `.` are dropped, `..` pops the parent when one exists, anything else is a real directory that gets pushed. The trailing sentinel guarantees the final segment is processed. Ignoring `..` on an empty stack prevents rising above root, and joining the stack under a leading `/` yields the canonical path.

## Complexity

- Time: O(n) — every character is visited once.
- Space: O(n) — the stack holds up to n characters; no split array is built.
