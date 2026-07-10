First check the obvious: the total length must divide evenly by 4, otherwise no square exists. Once we know the target side length, try to build the square one matchstick at a time — for each stick, attempt to drop it onto each of the four sides in turn, and recurse. If a side ever overshoots the target, back off and try the next side.

This is the plain-English translation of the problem into code: explore every way to bucket the sticks into four groups, and stop as soon as one bucketing works.

```java
class Solution {
    public boolean canFormSquare(int[] matchsticks) {
        int total = 0;
        for (int m : matchsticks) total += m;
        if (total % 4 != 0) return false;
        int side = total / 4;
        int[] sides = new int[4];
        return backtrack(matchsticks, 0, sides, side);
    }

    private boolean backtrack(int[] sticks, int i, int[] sides, int side) {
        if (i == sticks.length) {
            return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side;
        }
        for (int s = 0; s < 4; s++) {
            if (sides[s] + sticks[i] <= side) {
                sides[s] += sticks[i];
                if (backtrack(sticks, i + 1, sides, side)) return true;
                sides[s] -= sticks[i];
            }
        }
        return false;
    }
}
```

## Why it works

`sides` tracks the running length of each of the four sides. Placing a stick on a side that would push it past `side` is never useful, so that branch is skipped. When every stick has been placed (`i == sticks.length`), the square is valid only if all four running totals equal `side` exactly. Undoing `sides[s] -= sticks[i]` after a failed recursive call restores the state so the next side can be tried — standard backtracking.

## Complexity

- Time: O(4^n) — each of the n sticks can go on any of 4 sides in the worst case.
- Space: O(n) — recursion depth plus the fixed-size `sides` array.
