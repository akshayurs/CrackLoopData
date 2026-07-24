The definition talks about permutations, so the most literal solution is to generate every permutation of `1..n` and test each one against the divisibility rule.

There is no cleverness here — just `itertools.permutations` plus a check per candidate. It is slow, but it is the natural first thing to reach for and a good way to confirm you understand the rule before optimizing.

```python
from itertools import permutations

def count_arrangement(n):
    total = 0
    for perm in permutations(range(1, n + 1)):
        if all(perm[i] % (i + 1) == 0 or (i + 1) % perm[i] == 0 for i in range(n)):
            total += 1
    return total
```

## Why it works

`permutations(range(1, n + 1))` produces every ordering of the n values exactly once. For a given ordering, position `i` (0-indexed) holds value `perm[i]` and corresponds to 1-indexed position `i + 1`; the arrangement counts only if every position satisfies the divisibility rule, which `all(...)` checks directly.

## Complexity

- Time: O(n! * n) — n! permutations, each checked in O(n).
- Space: O(n) — recursion depth inside the permutation generator, aside from output.
