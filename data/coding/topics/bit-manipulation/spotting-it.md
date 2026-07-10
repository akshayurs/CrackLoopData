Reach for bitwise operators the moment a problem sounds like any of these:

- **"Every element appears twice except one"** — XOR-cancellation, no extra space needed.
- **"Count the number of 1 bits / set bits"** — popcount via `n & (n - 1)` or a DP-over-bits table (Counting Bits).
- **"Without using the +/- operator"** — add/subtract via XOR (sum) and AND+shift (carry).
- **"Is this a power of two / power of four?"** — a power of two has exactly one set bit, so `n & (n - 1) == 0`.
- **"Reverse the bits" / "Hamming distance"** — direct bit-by-bit manipulation, XOR then popcount for distance.
- **"Generate all subsets / all combinations of a bitmask"** — iterate masks 0 to 2^n - 1, each mask's set bits pick a subset.
- **"Missing number from 0 to n"** — XOR the array with the range 0..n; the missing value survives.

Signal words: *"XOR"*, *"without arithmetic operators"*, *"bitwise"*, *"appears once/twice/three times"*, *"binary representation"*, *"set bit"*, *"mask"*. If a constraint mentions numbers fitting in 32 bits, or the follow-up asks for O(1) space where hashing would normally be O(n), that's a strong nudge toward bit tricks.

Also watch for **range/interval bit problems** — "bitwise AND of all numbers in [m, n]" reduces to finding the common prefix of m and n's binary forms, a pattern that looks like a brute-force loop but has an O(log n) bit trick underneath.
