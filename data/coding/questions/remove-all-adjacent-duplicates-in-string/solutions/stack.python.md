A stack captures the "collide with the previous survivor" behaviour perfectly. Walk the string once; the stack always holds the result-so-far. For each character, if it equals the character on top of the stack, they annihilate — pop the top and drop the current one. Otherwise push the current character.

This handles the cascade automatically: after a pop, the new top is whatever was behind the removed pair, so the very next character is compared against the correct neighbour without any restart.

```python
def remove_duplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
```

## Why it works

The stack is an invariant: it is exactly the fully-reduced string of everything processed so far. When a new character matches the top, that pair is adjacent in the reduced string and must cancel, so we pop. When it does not match, it safely extends the reduced string. Because a pop re-exposes the earlier character as the new top, chains like `"aaaa"` collapse in the same single pass. What remains on the stack is the unique pair-free result.

## Complexity

- Time: O(n) — each character is pushed and popped at most once.
- Space: O(n) — the stack in the worst case (no removals) holds the whole string.
