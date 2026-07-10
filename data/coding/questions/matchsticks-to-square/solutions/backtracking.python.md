First check the obvious: the total length must divide evenly by 4, otherwise no square exists. Once we know the target side length, try to build the square one matchstick at a time — for each stick, attempt to drop it onto each of the four sides in turn, and recurse. If a side ever overshoots the target, back off and try the next side.

This is the plain-English translation of the problem into code: explore every way to bucket the sticks into four groups, and stop as soon as one bucketing works.

```python
def can_form_square(matchsticks):
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    side = total // 4
    sides = [0, 0, 0, 0]

    def backtrack(i):
        if i == len(matchsticks):
            return sides[0] == sides[1] == sides[2] == sides[3] == side
        for s in range(4):
            if sides[s] + matchsticks[i] <= side:
                sides[s] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                sides[s] -= matchsticks[i]
        return False

    return backtrack(0)
```

## Why it works

`sides` tracks the running length of each of the four sides. Placing a stick on a side that would push it past `side` is never useful, so that branch is skipped. When every stick has been placed (`i == len(matchsticks)`), the square is valid only if all four running totals equal `side` exactly. Undoing `sides[s] -= matchsticks[i]` after a failed recursive call restores the state so the next side can be tried — standard backtracking.

## Complexity

- Time: O(4^n) — each of the n sticks can go on any of 4 sides in the worst case.
- Space: O(n) — recursion depth plus the fixed-size `sides` array.
