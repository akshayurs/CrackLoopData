Instead of picking all three cut points up front and validating afterward, build the address one octet at a time and abandon a branch the instant it can't possibly lead anywhere. At each step, try consuming 1, 2, or 3 characters for the next octet; skip a length immediately if it produces a leading zero or a value over 255, and skip the whole branch if the remaining characters can't be split into the remaining octets.

Because every octet is at most 3 digits and there are always exactly 4 of them, the search tree stays tiny regardless of the input length — the pruning turns what looks like exponential search into a small, fixed amount of work.

```python
def restore_ip_addresses(digits):
    n = len(digits)
    results = []
    parts = []

    def backtrack(start):
        remaining_parts = 4 - len(parts)
        remaining_chars = n - start
        if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
            return
        if len(parts) == 4:
            if start == n:
                results.append(".".join(parts))
            return

        for length in range(1, 4):
            if start + length > n:
                break
            piece = digits[start:start + length]
            if piece[0] == "0" and length > 1:
                break
            if int(piece) > 255:
                break
            parts.append(piece)
            backtrack(start + length)
            parts.pop()

    backtrack(0)
    return sorted(results)
```

## Why it works

The `remaining_chars` bound prunes any branch where the leftover string is too short or too long to fill the remaining octets, so hopeless prefixes are dropped before any recursion happens. Within a single octet, the loop stops as soon as a length is invalid (leading zero or value over 255), since a longer piece starting the same way can only be worse. `parts` is built and unwound in place, so each successful path down to 4 octets that exactly consumes the string is one valid address.

## Complexity

- Time: O(1) — each octet has at most 3 candidate lengths and there are always exactly 4 octets, so the search explores at most 3^4 branches no matter how long `digits` is.
- Space: O(n) — recursion depth is bounded by the string length, plus the output list of matched addresses.
