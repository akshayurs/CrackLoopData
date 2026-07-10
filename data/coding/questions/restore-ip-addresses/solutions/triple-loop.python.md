An IP address always has exactly three dots, so it always has exactly three "cut points" inside the digit string. The most direct approach is to try every combination of three cut positions with three nested loops, slice out the four resulting pieces, and keep the combination only if all four pieces are legal octets.

It never looks more than one string ahead — no recursion, no early exit — so it re-validates a lot of dead-end prefixes, but it is the natural first attempt.

```python
def restore_ip_addresses(digits):
    n = len(digits)
    results = []

    def is_valid(piece):
        if not piece or len(piece) > 3:
            return False
        if piece[0] == "0" and len(piece) > 1:
            return False
        return int(piece) <= 255

    for i in range(1, min(4, n)):
        for j in range(i + 1, min(i + 4, n)):
            for k in range(j + 1, min(j + 4, n)):
                a, b, c, d = digits[:i], digits[i:j], digits[j:k], digits[k:]
                if is_valid(a) and is_valid(b) and is_valid(c) and is_valid(d):
                    results.append(f"{a}.{b}.{c}.{d}")

    return sorted(results)
```

## Why it works

Every valid split is uniquely described by the lengths of its first three octets, so scanning `i < j < k` over the string's index range enumerates every possible four-way partition exactly once. `is_valid` rejects empty pieces, pieces longer than three digits, values above 255, and leading zeros on multi-digit pieces — the three conditions that make an octet malformed. Bounding each loop to at most 3 steps ahead keeps the search from wasting time on octets that could never be valid anyway.

## Complexity

- Time: O(n^3) — three nested loops over cut positions, each iteration doing O(1) validation since every piece is at most 3 characters.
- Space: O(1) extra beyond the output list.
