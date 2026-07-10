The instinct is to join the strings with some separator like `#`. That breaks the moment a string *contains* `#`, so the fix is to escape it: before joining, protect every separator (and the escape character itself) inside each string with a backslash. On the way back, a backslash means "the next character is literal, not a separator."

This works, but notice the seam it leaves: because the pieces are joined *between* elements, an empty input list and a list holding one empty string both encode to `""`. The length-prefixed approach avoids that ambiguity entirely.

```python
def encode(strs):
    parts = [s.replace('\\', '\\\\').replace('#', '\\#') for s in strs]
    return '#'.join(parts)

def decode(s):
    result, buf, i = [], [], 0
    while i < len(s):
        if s[i] == '\\':
            buf.append(s[i + 1])
            i += 2
        elif s[i] == '#':
            result.append(''.join(buf))
            buf = []
            i += 1
        else:
            buf.append(s[i])
            i += 1
    result.append(''.join(buf))
    return result
```

## Why it works

Escaping guarantees that every unescaped `#` in the encoded string is a real boundary and never part of the data. During decoding, a backslash consumes the character after it verbatim, so an escaped `#` or `\` rejoins the current buffer instead of splitting it. Everything else accumulates until an unescaped `#` flushes the buffer as one recovered string; the trailing buffer after the loop is the final element.

## Complexity

- Time: O(N) where N is the total number of characters across all strings — each character is scanned a constant number of times.
- Space: O(N) — the encoded string and the rebuilt list are proportional to the input.
