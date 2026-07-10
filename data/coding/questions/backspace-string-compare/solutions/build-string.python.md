The most literal reading: actually type each string out. Walk left to right pushing letters onto a stack, and whenever a `#` appears, pop the last letter (if any). Whatever remains on the stack is the final text.

Do this for both strings and compare the results directly. It is the honest baseline you would describe first before worrying about extra space.

```python
def backspace_compare(s, t):
    def build(string):
        stack = []
        for ch in string:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    return build(s) == build(t)
```

## Why it works

A stack mirrors the editor exactly: typing a letter pushes it, and a backspace removes the most recent letter — which is always the top of the stack. Guarding the pop with `if stack` handles a backspace on empty text as a no-op. Two strings are equal after editing iff their reconstructed contents match character for character.

## Complexity

- Time: O(m + n) — each character of both strings is processed once.
- Space: O(m + n) — the two rebuilt strings are stored explicitly.
