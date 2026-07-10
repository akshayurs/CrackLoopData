A collision only ever happens between adjacent asteroids where a right-mover sits directly left of a left-mover — a `+, -` pair. The most direct approach is to keep scanning the array for the first such pair, resolve it, and start over, repeating until a full pass finds nothing left to collide.

Each resolution removes one or both of the colliding asteroids, so the list only shrinks. When a pass completes without touching anything, the arrangement is stable and we return it. It is simple to reason about but wasteful: one explosion forces a re-scan from the beginning.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        List<Integer> arr = new ArrayList<>();
        for (int a : asteroids) arr.add(a);
        boolean stable = false;
        while (!stable) {
            stable = true;
            for (int i = 0; i < arr.size() - 1; i++) {
                if (arr.get(i) > 0 && arr.get(i + 1) < 0) {
                    stable = false;
                    int right = arr.get(i), left = -arr.get(i + 1);
                    if (right < left) arr.remove(i);
                    else if (right > left) arr.remove(i + 1);
                    else { arr.remove(i + 1); arr.remove(i); }
                    break;
                }
            }
        }
        int[] out = new int[arr.size()];
        for (int i = 0; i < out.length; i++) out[i] = arr.get(i);
        return out;
    }
}
```

## Why it works

Only a `positive, negative` adjacency can collide; any other pair is stable. We always resolve the leftmost such pair, delete the loser (or both on a tie), then restart the scan because deleting an element can create a brand-new adjacency. The list shrinks on every non-trivial pass, so the loop terminates, and it exits exactly when no collidable pair remains.

## Complexity

- Time: O(n^2) — up to O(n) explosions, each triggering an O(n) rescan.
- Space: O(n) — a working list of the surviving asteroids.
