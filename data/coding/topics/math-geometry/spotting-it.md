Reach for math/geometry reasoning the moment a problem sounds like any of these:

- **"Rotate / transpose / traverse the matrix in some order"** — Rotate Image, Spiral Matrix. The grid itself *is* the data structure; you manipulate indices, not a map or stack.
- **"Do this without extra space" on a grid** — Set Matrix Zeroes, Rotate Image in-place. Signals you should use the matrix's own borders/cells as scratch space instead of allocating a copy.
- **"Is this number happy / prime / a palindrome / ugly?"** — pure number-theory questions where you simulate the definition (digit-by-digit, divisibility, repeated squaring) rather than search or sort.
- **"Compute x^n / factorial trailing zeros / column number"** — closed-form or divide-and-conquer arithmetic. Look for a pattern that lets you skip brute-force iteration (fast power, counting factors of 5, base-26 conversion).
- **"Simulate N rounds / steps and report the final state"** — Game of Life, Robot Bounded in Circle. You must apply a rule to every element "simultaneously," which usually needs encoding old+new state in the same cell or buffering.
- **"Parse/convert a number-like string"** — atoi, Roman numerals, Add Strings/Multiply Strings — manual digit and carry handling instead of built-in parsing.

Signal words: *"in place"*, *"without extra memory"*, *"digit"*, *"prime"*, *"modulo"*, *"rotate"*, *"spiral"*, *"simulate"*, *"clockwise/counter-clockwise"*. If the input is a grid of numbers and the question is about geometric movement rather than search, it's this bucket. If it's a single integer/string and the question is about its numeric properties, it's number theory.
