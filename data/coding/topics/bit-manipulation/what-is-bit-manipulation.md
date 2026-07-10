**Bit manipulation** works directly on the binary representation of a number using the bitwise operators — `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift). Each operator runs in O(1) per bit, so a 32-bit operation is effectively constant time, and problems that look like they need O(n) extra space often collapse to O(1) once you think in bits.

The core superpower is **XOR's self-cancelling property**: `x ^ x = 0` and `x ^ 0 = x`. XOR every number in a list together and every value that appears twice cancels out, leaving only the one that appears once — no hash set required.

Other recurring building blocks:

- **Isolate the lowest set bit:** `n & (-n)` gives you just that bit; `n & (n - 1)` clears it. Repeating the clear step counts set bits in O(popcount) time.
- **Check/set/clear a specific bit i:** `n & (1 << i)`, `n | (1 << i)`, `n & ~(1 << i)`.
- **Shifts as arithmetic:** `n << 1` doubles, `n >> 1` halves (for non-negative n) — useful for building numbers bit by bit or simulating division/multiplication without the operators.

A typical shape for "find the unique element" problems:

```
result = 0
for each number x in the array:
    result = result ^ x
return result
```

Bit tricks also power arithmetic-without-operators questions (adding two integers using XOR for sum and AND+shift for carry), and combinatorial ones (each subset of a set of n items maps to an n-bit mask from 0 to 2^n - 1).
