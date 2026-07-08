The escaping approach fights the data — it has to hunt for and disarm every character that looks like a separator. Flip the problem around: instead of marking where each string *ends*, announce up front how *long* it is. Encode every string as its length, a single `#`, then the raw bytes: `4#neet`. Now the `#` is never ambiguous, because the decoder only ever reads it in one place — right after the digits of a length.

This is the "chunked transfer" trick. To decode, read digits until the `#`, parse that as a count `L`, then grab exactly the next `L` characters verbatim — no scanning of the payload, no escaping, and no confusion even if those `L` characters are all `#`. It also cleanly distinguishes an empty list (`""` → `[]`) from a list holding one empty string (`"0#"` → `[""]`).

```python
def encode(strs):
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    result, i = [], 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        start = j + 1
        result.append(s[start:start + length])
        i = start + length
    return result
```

## Why it works

Every chunk is self-describing: the length prefix tells the decoder exactly how many characters to consume, so the payload is copied by count rather than by searching for a boundary. Because the decoder never inspects the content bytes, any character — including the `#` separator — passes through untouched. The pointer always lands on the start of the next length prefix, so the loop cleanly walks chunk by chunk to the end.

## Complexity

- Time: O(N) where N is the total number of characters — the length scan plus the slice copy touch each character a constant number of times.
- Space: O(N) — the encoded string and the decoded list are proportional to the input.
