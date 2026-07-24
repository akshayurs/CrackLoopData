The blunt approach: any well-formed string of length `2n` is some arrangement of `n` opening and `n` closing brackets, so enumerate *every* binary sequence of that length and keep the ones that are balanced. Treat each of the `2n` positions as a bit that is either `(` or `)`, generate all `2^(2n)` candidates, and test each one.

A candidate is valid when scanning left to right never drives the running balance negative and it ends back at zero. Collect the survivors and sort them so the result is identical no matter the traversal order.

```python
def generate_parenthesis(n):
    def valid(seq):
        balance = 0
        for ch in seq:
            balance += 1 if ch == "(" else -1
            if balance < 0:
                return False
        return balance == 0

    result = []
    for mask in range(1 << (2 * n)):
        seq = "".join("(" if mask & (1 << i) else ")" for i in range(2 * n))
        if valid(seq):
            result.append(seq)
    return sorted(result)
```

## Why it works

Every valid combination is one of the `2^(2n)` bracket sequences, so exhaustively generating and filtering cannot miss any. The `valid` check enforces both well-formedness rules at once: `balance < 0` catches a closing bracket with no open partner, and a nonzero final balance catches unmatched openings. Sorting at the end guarantees a canonical, deterministic order.

## Complexity

- Time: O(2^(2n) · n) — every sequence is generated and scanned.
- Space: O(2^(2n) · n) — worst-case storage for the candidate strings.
